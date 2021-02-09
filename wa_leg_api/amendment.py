from typing import Dict
from datetime import datetime  # noqa
from wa_leg_api import waleg


def get_amendments(year: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/amendmentservice.asmx?op=GetAmendments"""
    argdict = dict(year=year)
    return waleg.call("Amendment", "GetAmendments", argdict)
