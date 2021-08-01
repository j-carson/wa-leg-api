from datetime import datetime  # noqa
from typing import Any, Dict

from dateutil import parser  # noqa

from wa_leg_api import waleg


def get_committees(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetCommittees"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {}
    return waleg.call("Committee", "GetCommittees", argdict, keydict)


def get_house_committees(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetHouseCommittees"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {}
    return waleg.call("Committee", "GetHouseCommittees", argdict, keydict)


def get_senate_committees(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetSenateCommittees"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {}
    return waleg.call("Committee", "GetSenateCommittees", argdict, keydict)


def get_committee_members(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetCommitteeMembers"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "district": int,
    }
    return waleg.call("Committee", "GetCommitteeMembers", argdict, keydict)


def get_active_committees() -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveCommittees"""
    argdict: Dict[str, Any] = dict()
    keydict: Dict[str, Any] = {}
    return waleg.call("Committee", "GetActiveCommittees", argdict, keydict)


def get_active_house_committees() -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveHouseCommittees"""
    argdict: Dict[str, Any] = dict()
    keydict: Dict[str, Any] = {}
    return waleg.call("Committee", "GetActiveHouseCommittees", argdict, keydict)


def get_active_senate_committees() -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveSenateCommittees"""
    argdict: Dict[str, Any] = dict()
    keydict: Dict[str, Any] = {}
    return waleg.call("Committee", "GetActiveSenateCommittees", argdict, keydict)


def get_active_committee_members(agency: str, committee_name: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveCommitteeMembers"""
    argdict: Dict[str, Any] = dict(agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "district": int,
    }
    return waleg.call("Committee", "GetActiveCommitteeMembers", argdict, keydict)
