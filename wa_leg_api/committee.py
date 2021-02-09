from typing import Dict
from datetime import datetime  # noqa
from wa_leg_api import waleg


def get_committees(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetCommittees"""
    argdict = dict(biennium=biennium)
    return waleg.call("Committee", "GetCommittees", argdict)


def get_house_committees(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetHouseCommittees"""
    argdict = dict(biennium=biennium)
    return waleg.call("Committee", "GetHouseCommittees", argdict)


def get_senate_committees(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetSenateCommittees"""
    argdict = dict(biennium=biennium)
    return waleg.call("Committee", "GetSenateCommittees", argdict)


def get_committee_members(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetCommitteeMembers"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("Committee", "GetCommitteeMembers", argdict)


def get_active_committees() -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveCommittees"""
    argdict = dict()
    return waleg.call("Committee", "GetActiveCommittees", argdict)


def get_active_house_committees() -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveHouseCommittees"""
    argdict = dict()
    return waleg.call("Committee", "GetActiveHouseCommittees", argdict)


def get_active_senate_committees() -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveSenateCommittees"""
    argdict = dict()
    return waleg.call("Committee", "GetActiveSenateCommittees", argdict)


def get_active_committee_members(agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveCommitteeMembers"""
    argdict = dict(agency=agency, committeeName=committee_name)
    return waleg.call("Committee", "GetActiveCommitteeMembers", argdict)
