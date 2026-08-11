import json
from pathlib import Path
import pytest

MAPPING_PATH = Path("qase_mapping.json")


def _normalize_nodeid(nodeid: str) -> str:
    # Remove parameter values: [admin], [user], etc.
    return nodeid.split("[")[0]


def pytest_collection_modifyitems(session, config, items):
    if not MAPPING_PATH.exists():
        return

    mapping = json.loads(MAPPING_PATH.read_text(encoding="utf-8"))

    for item in items:
        nodeid = _normalize_nodeid(item.nodeid)
        case_ids = mapping.get(nodeid)

        if not case_ids:
            continue

        if isinstance(case_ids, int):
            case_ids = [case_ids]

        # ✅ THIS is what Qase reads
        item.add_marker(pytest.mark.qase(id=case_ids))
