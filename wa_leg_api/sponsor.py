from typing import Dict
from datetime import datetime
from . import waleg

def get_sponsors(biennium:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("Sponsor", "GetSponsors", argdict=dict(biennium=biennium))


def get_house_sponsors(biennium:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("Sponsor", "GetHouseSponsors", argdict=dict(biennium=biennium))


def get_senate_sponsors(biennium:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("Sponsor", "GetSenateSponsors", argdict=dict(biennium=biennium))


def get_requesters(biennium:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("Sponsor", "GetRequesters", argdict=dict(biennium=biennium))


