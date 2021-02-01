from typing import Dict
from datetime import datetime
from . import waleg

def get_legislation_affecting_rcw_cite(biennium:str,rcw_cite:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("RcwCiteAffected", "GetLegislationAffectingRcwCite", argdict=dict(biennium=biennium,rcwCite=rcw_cite))


def get_legislation_affecting_rcw(biennium:str,rcw_cite:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("RcwCiteAffected", "GetLegislationAffectingRcw", argdict=dict(biennium=biennium,rcwCite=rcw_cite))


