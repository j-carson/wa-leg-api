from typing import Dict
from datetime import datetime  # noqa
from . import waleg


def get_committees(biennium: str) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(biennium=biennium)
    return waleg.call("Committee", "GetCommittees", argdict=argdict)


def get_house_committees(biennium: str) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(biennium=biennium)
    return waleg.call("Committee", "GetHouseCommittees", argdict=argdict)


def get_senate_committees(biennium: str) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(biennium=biennium)
    return waleg.call("Committee", "GetSenateCommittees", argdict=argdict)


def get_committee_members(biennium: str, agency: str, committee_name: str) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("Committee", "GetCommitteeMembers", argdict=argdict)


def get_active_committees() -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict()
    return waleg.call("Committee", "GetActiveCommittees", argdict=argdict)


def get_active_house_committees() -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict()
    return waleg.call("Committee", "GetActiveHouseCommittees", argdict=argdict)


def get_active_senate_committees() -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict()
    return waleg.call("Committee", "GetActiveSenateCommittees", argdict=argdict)


def get_active_committee_members(agency: str, committee_name: str) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(agency=agency, committeeName=committee_name)
    return waleg.call("Committee", "GetActiveCommitteeMembers", argdict=argdict)
