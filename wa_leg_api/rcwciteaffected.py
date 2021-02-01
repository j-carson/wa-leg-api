from typing import Dict
from datetime import datetime
import waleg

def get_legislation_affecting_rcw_cite(biennium:str=None,rcw_cite:str=None) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("RcwCiteAffected", "GetLegislationAffectingRcwCite", argdict=dict(biennium=biennium,rcwCite=rcw_cite))


def get_legislation_affecting_rcw(biennium:str=None,rcw_cite:str=None) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("RcwCiteAffected", "GetLegislationAffectingRcw", argdict=dict(biennium=biennium,rcwCite=rcw_cite))


