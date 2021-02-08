from typing import Dict
from datetime import datetime  # noqa
from . import waleg


def get_legislation_affecting_rcw_cite(biennium: str, rcw_cite: str) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(biennium=biennium, rcwCite=rcw_cite)
    return waleg.call(
        "RcwCiteAffected", "GetLegislationAffectingRcwCite", argdict=argdict
    )


def get_legislation_affecting_rcw(biennium: str, rcw_cite: str) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(biennium=biennium, rcwCite=rcw_cite)
    return waleg.call("RcwCiteAffected", "GetLegislationAffectingRcw", argdict=argdict)
