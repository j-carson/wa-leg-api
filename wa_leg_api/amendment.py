from typing import Dict
from datetime import datetime  # noqa
from dateutil import parser  # noqa
from wa_leg_api import waleg


def get_amendments(year: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/amendmentservice.asmx?op=GetAmendments"""
    argdict = dict(year=year)
    keydict = {'billnumber':int,
'floornumber':int,
'flooractiondate':parser.parse,
'documentexists':lambda boolstr: (boolstr.lower() == "true"),
}
    return waleg.call("Amendment", "GetAmendments", argdict, keydict)
