from datetime import datetime  # noqa
from typing import Any, Dict

from dateutil import parser  # noqa

from wa_leg_api import waleg


def get_amendments(year: int) -> Dict[str, Any]:
    """Returns list of amendments submitted to the rostrum during the year.
    Exception thrown for invalid year.

    See: http://wslwebservices.leg.wa.gov/amendmentservice.asmx?op=GetAmendments"""
    argdict: Dict[str, Any] = dict(year=year)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "floor_number": int,
        "floor_action_date": parser.parse,
        "document_exists": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Amendment", "GetAmendments", argdict, keydict)
