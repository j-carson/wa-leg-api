from typing import Dict
from datetime import datetime  # noqa
from dateutil import parser  # noqa
from wa_leg_api import waleg


def get_committees(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetCommittees"""
    argdict = dict(biennium=biennium)
    keydict = {}
    return waleg.call("Committee", "GetCommittees", argdict, keydict)


def get_house_committees(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetHouseCommittees"""
    argdict = dict(biennium=biennium)
    keydict = {}
    return waleg.call("Committee", "GetHouseCommittees", argdict, keydict)


def get_senate_committees(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetSenateCommittees"""
    argdict = dict(biennium=biennium)
    keydict = {}
    return waleg.call("Committee", "GetSenateCommittees", argdict, keydict)


def get_committee_members(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetCommitteeMembers"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict = {'district':int,
}
    return waleg.call("Committee", "GetCommitteeMembers", argdict, keydict)


def get_active_committees() -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveCommittees"""
    argdict = dict()
    keydict = {}
    return waleg.call("Committee", "GetActiveCommittees", argdict, keydict)


def get_active_house_committees() -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveHouseCommittees"""
    argdict = dict()
    keydict = {}
    return waleg.call("Committee", "GetActiveHouseCommittees", argdict, keydict)


def get_active_senate_committees() -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveSenateCommittees"""
    argdict = dict()
    keydict = {}
    return waleg.call("Committee", "GetActiveSenateCommittees", argdict, keydict)


def get_active_committee_members(agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeservice.asmx?op=GetActiveCommitteeMembers"""
    argdict = dict(agency=agency, committeeName=committee_name)
    keydict = {'district':int,
}
    return waleg.call("Committee", "GetActiveCommitteeMembers", argdict, keydict)
