from typing import Dict
from datetime import datetime  # noqa
from . import waleg


def get_amendments(year: int) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(year=year)
    return waleg.call("Amendment", "GetAmendments", argdict=argdict)
