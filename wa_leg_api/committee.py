from typing import Dict
from datetime import datetime
from . import waleg

def get_committees(biennium:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("Committee", "GetCommittees", argdict=dict(biennium=biennium))


def get_house_committees(biennium:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("Committee", "GetHouseCommittees", argdict=dict(biennium=biennium))


def get_senate_committees(biennium:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("Committee", "GetSenateCommittees", argdict=dict(biennium=biennium))


def get_committee_members(biennium:str,agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("Committee", "GetCommitteeMembers", argdict=dict(biennium=biennium,agency=agency,committeeName=committee_name))


def get_active_committees() -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("Committee", "GetActiveCommittees", argdict=dict())


def get_active_house_committees() -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("Committee", "GetActiveHouseCommittees", argdict=dict())


def get_active_senate_committees() -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("Committee", "GetActiveSenateCommittees", argdict=dict())


def get_active_committee_members(agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("Committee", "GetActiveCommitteeMembers", argdict=dict(agency=agency,committeeName=committee_name))


