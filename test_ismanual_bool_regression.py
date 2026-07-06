"""
Regression reproduction for the `qase-api-client` (V1) TestCase deserialization bug.

Symptom: after upgrading `qase-api-client` 2.0.7 -> 2.0.10, fetching ANY existing
test case raises a pydantic ValidationError:

    pydantic_core._pydantic_core.ValidationError: 2 validation errors for TestCase
    isManual
      Input should be a valid integer [type=int_type, input_value=True, input_type=bool]
    isToBeAutomated
      Input should be a valid integer [type=int_type, input_value=True, input_type=bool]

Root cause: in 2.0.10 the generated `TestCase` model declares `isManual` /
`isToBeAutomated` as pydantic `StrictInt`, but the Qase REST API serializes these
fields as JSON booleans (true/false). Pydantic v2 StrictInt rejects `bool`, so
`TestCase.from_dict()` (and therefore `CasesApi.get_case` / `get_cases`) fails for
normal, GUI-created cases. 2.0.7 had no such fields, so it was unaffected.

Two tests:
  1. test_from_dict_boolean_ismanual_regression  -- offline, deterministic, no network.
  2. test_live_get_case_boolean_ismanual          -- live API; runs only if
     QASE_API_TOKEN (and optionally QASE_PROJECT/QASE_CASE_ID) are set.

Both are EXPECTED TO FAIL on qase-api-client==2.0.10 and PASS once the client is fixed.
"""
import os
import pytest

from qase.api_client_v1.models.test_case import TestCase as CaseModel


# Minimal payload mirroring what the Qase API returns for a GUI-created case:
# isManual / isToBeAutomated come back as JSON booleans.
API_LIKE_PAYLOAD = {
    "id": 1,
    "title": "Authorization",
    "automation": 0,
    "isManual": True,
    "isToBeAutomated": False,
    "status": 0,
}


def test_from_dict_boolean_ismanual_regression():
    """The API returns booleans for isManual/isToBeAutomated; the client must accept them."""
    case = CaseModel.from_dict(API_LIKE_PAYLOAD)
    assert case is not None
    # Whatever the eventual normalization, these must not raise and must be truthy/falsey correctly.
    assert bool(case.is_manual) is True
    assert bool(case.is_to_be_automated) is False


@pytest.mark.skipif(
    not os.getenv("QASE_API_TOKEN"),
    reason="Set QASE_API_TOKEN to run the live get_case reproduction.",
)
def test_live_get_case_boolean_ismanual():
    """Live reproduction: get_case on a normal case fails to deserialize on 2.0.10."""
    from qase.api_client_v1.configuration import Configuration
    from qase.api_client_v1.api_client import ApiClient
    from qase.api_client_v1.api.cases_api import CasesApi

    token = os.environ["QASE_API_TOKEN"]
    project = os.getenv("QASE_PROJECT", "ALLCAP")
    case_id = int(os.getenv("QASE_CASE_ID", "1"))

    config = Configuration()
    config.api_key["TokenAuth"] = token
    with ApiClient(config) as api_client:
        res = CasesApi(api_client).get_case(code=project, id=case_id)
    assert res.result is not None
