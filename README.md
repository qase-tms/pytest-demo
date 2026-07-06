# Bug repro — `qase-api-client` 2.0.10: `TestCase` fails on boolean `isManual` / `isToBeAutomated`

This branch is a **minimal, self-contained reproduction** of a deserialization
regression in the `qase-api-client` (V1) Python client. It contains only what is
needed to reproduce the bug.

- **Package:** `qase-api-client` (V1 client)
- **Broken in:** `2.0.10`  |  **Last working:** `2.0.7`
- **Status:** reproduced — offline (model-level) and live (`get_case`)

## Symptom

After upgrading `qase-api-client` from `2.0.7` to `2.0.10`, fetching **any** existing
test case raises:

```
pydantic_core._pydantic_core.ValidationError: 2 validation errors for TestCase
isManual
  Input should be a valid integer [type=int_type, input_value=True, input_type=bool]
isToBeAutomated
  Input should be a valid integer [type=int_type, input_value=False, input_type=bool]
```

## Root cause

- In `2.0.10`, `TestCase` declares these fields as **strict integers**
  (`qase/api_client_v1/models/test_case.py`):

  ```python
  is_manual: Optional[StrictInt] = Field(default=None, alias="isManual")
  is_to_be_automated: Optional[StrictInt] = Field(default=None, alias="isToBeAutomated")
  ```

- The Qase REST API serializes these fields as **JSON booleans** (`true`/`false`)
  for existing/GUI-created cases. Verified against a live workspace: **100/100**
  cases in a sample project returned `isManual`/`isToBeAutomated` as booleans.

- Pydantic v2 `StrictInt` **rejects `bool`** (in strict mode a bool is not an int),
  so `TestCase.from_dict()` — and therefore `CasesApi.get_case()` / `get_cases()` —
  fails for normal cases.

- `2.0.7` had **no** `isManual`/`isToBeAutomated` fields on the model, so it ignored
  them and deserialized fine. The regression was introduced with the new strict-int
  fields. This is a **client/API contract mismatch**, not bad data — the values are
  set by the GUI and returned on read, so there is no client-side workaround.

## Reproduce

```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 1) Offline, deterministic (no network) — reproduces the failure:
pytest test_ismanual_bool_regression.py -k from_dict -v

# 2) Live reproduction (optional) — needs a token and any project with GUI-created cases:
export QASE_API_TOKEN=<token>
export QASE_PROJECT=ALLCAP
export QASE_CASE_ID=1
pytest test_ismanual_bool_regression.py -v
```

Both tests **fail on `2.0.10`** and should **pass once the client is fixed**.

## Suggested fix

Make the client accept the boolean the API actually returns:

1. **Client model (fastest, unblocks users):** change the field type to accept both
   and normalize to `int` — e.g. `Optional[StrictBool]` coerced, or a `field_validator`
   mapping `bool -> int`. Regenerate from a corrected OpenAPI spec so the fix survives codegen.
2. **API side:** return `isManual`/`isToBeAutomated` as integers (`0`/`1`) to match the
   documented contract and the model's `StrictInt`.

Whichever is chosen, the OpenAPI spec and the API response must agree — otherwise the
next codegen reintroduces the mismatch.
