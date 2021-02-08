from typing import Dict
from datetime import datetime  # noqa
from . import waleg


def get_sponsors(biennium: str) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(biennium=biennium)
    return waleg.call("Sponsor", "GetSponsors", argdict=argdict)


def get_house_sponsors(biennium: str) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(biennium=biennium)
    return waleg.call("Sponsor", "GetHouseSponsors", argdict=argdict)


def get_senate_sponsors(biennium: str) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(biennium=biennium)
    return waleg.call("Sponsor", "GetSenateSponsors", argdict=argdict)


def get_requesters(biennium: str) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(biennium=biennium)
    return waleg.call("Sponsor", "GetRequesters", argdict=argdict)
