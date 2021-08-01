from datetime import datetime  # noqa
from typing import Any, Dict

from dateutil import parser  # noqa

from wa_leg_api import waleg


def get_amendments(year: int) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/amendmentservice.asmx?op=GetAmendments"""
    argdict: Dict[str, Any] = dict(year=year)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "floornumber": int,
        "flooractiondate": parser.parse,
        "documentexists": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Amendment", "GetAmendments", argdict, keydict)
