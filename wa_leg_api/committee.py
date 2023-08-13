from datetime import datetime  # noqa
from typing import Any, Dict

from dateutil import parser  # noqa

from wa_leg_api import waleg


def get_committees(biennium: str) -> Dict[str, Any]:
    """All House and Senate standing committees during the given biennium.
    Exception thrown for invalid biennium.
    Expects iennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetCommittees"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {}
    return waleg.call("Committee", "GetCommittees", argdict, keydict)


def get_house_committees(biennium: str) -> Dict[str, Any]:
    """All House standing committees during the given biennium.
    Exception thrown for invalid biennium.
    Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetHouseCommittees"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {}
    return waleg.call("Committee", "GetHouseCommittees", argdict, keydict)


def get_senate_committees(biennium: str) -> Dict[str, Any]:
    """All Senate standing committees during the given biennium.
    Exception thrown for invalid biennium.
    Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetSenateCommittees"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {}
    return waleg.call("Committee", "GetSenateCommittees", argdict, keydict)


def get_committee_members(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """Lists committee members for the given standing committee.
    Exception thrown for invalid biennium, agency, or committee name.
    Expects biennium to be in the format: 2005-06. Agency should be House or Senate.  CommitteeName is the Name Property returned in GetHouseCommittees/GetSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetCommitteeMembers"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {}
    return waleg.call("Committee", "GetCommitteeMembers", argdict, keydict)


def get_active_committees() -> Dict[str, Any]:
    """All active House and Senate standing committees.

    See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveCommittees"""
    argdict: Dict[str, Any] = dict()
    keydict: Dict[str, Any] = {}
    return waleg.call("Committee", "GetActiveCommittees", argdict, keydict)


def get_active_house_committees() -> Dict[str, Any]:
    """All active House standing committees.

    See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveHouseCommittees"""
    argdict: Dict[str, Any] = dict()
    keydict: Dict[str, Any] = {}
    return waleg.call("Committee", "GetActiveHouseCommittees", argdict, keydict)


def get_active_senate_committees() -> Dict[str, Any]:
    """All active Senate standing committees.

    See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveSenateCommittees"""
    argdict: Dict[str, Any] = dict()
    keydict: Dict[str, Any] = {}
    return waleg.call("Committee", "GetActiveSenateCommittees", argdict, keydict)


def get_active_committee_members(agency: str, committee_name: str) -> Dict[str, Any]:
    """Lists active committee members for the given standing committee.
    Exception thrown for invalid agency or committee name.
    Agency should be House or Senate.  CommitteeName is the Name Property returned in GetActiveHouseCommittees/GetActiveSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveCommitteeMembers"""
    argdict: Dict[str, Any] = dict(agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {}
    return waleg.call("Committee", "GetActiveCommitteeMembers", argdict, keydict)
