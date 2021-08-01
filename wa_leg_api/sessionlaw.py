from datetime import datetime  # noqa
from typing import Any, Dict

from dateutil import parser  # noqa

from wa_leg_api import waleg


def get_session_law_by_bill(biennium: str, bill_number: int) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/sessionlawservice.asmx?op=GetSessionLawByBill"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "chapternumber": int,
        "year": int,
        "legislaturenumber": int,
        "effectivedate": parser.parse,
        "multipleeffectivedates": lambda boolstr: (boolstr.lower() == "true"),
        "partialveto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "legtypeid": int,
    }
    return waleg.call("SessionLaw", "GetSessionLawByBill", argdict, keydict)


def get_bill_by_chapter_number(year: int, session: int, chapter_number: int) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/sessionlawservice.asmx?op=GetBillByChapterNumber"""
    argdict: Dict[str, Any] = dict(year=year, session=session, chapterNumber=chapter_number)
    keydict: Dict[str, Any] = {
        "statefiscalnote": lambda boolstr: (boolstr.lower() == "true"),
        "localfiscalnote": lambda boolstr: (boolstr.lower() == "true"),
        "appropriations": lambda boolstr: (boolstr.lower() == "true"),
        "requestedbygovernor": lambda boolstr: (boolstr.lower() == "true"),
        "requestedbybudgetcommittee": lambda boolstr: (boolstr.lower() == "true"),
        "requestedbydepartment": lambda boolstr: (boolstr.lower() == "true"),
        "requestedbyother": lambda boolstr: (boolstr.lower() == "true"),
        "introduceddate": parser.parse,
        "actiondate": parser.parse,
        "amendedbyoppositebody": lambda boolstr: (boolstr.lower() == "true"),
        "partialveto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "amendmentsexist": lambda boolstr: (boolstr.lower() == "true"),
        "primesponsorid": int,
    }
    return waleg.call("SessionLaw", "GetBillByChapterNumber", argdict, keydict)


def get_chapter_numbers_by_year(year: int) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/sessionlawservice.asmx?op=GetChapterNumbersByYear"""
    argdict: Dict[str, Any] = dict(year=year)
    keydict: Dict[str, Any] = {
        "chapternumber": int,
        "year": int,
        "legislaturenumber": int,
        "effectivedate": parser.parse,
        "multipleeffectivedates": lambda boolstr: (boolstr.lower() == "true"),
        "partialveto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "legtypeid": int,
    }
    return waleg.call("SessionLaw", "GetChapterNumbersByYear", argdict, keydict)


def get_session_law_by_bill_id(biennium: str, bill_id: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/sessionlawservice.asmx?op=GetSessionLawByBillId"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billId=bill_id)
    keydict: Dict[str, Any] = {
        "chapternumber": int,
        "year": int,
        "legislaturenumber": int,
        "effectivedate": parser.parse,
        "multipleeffectivedates": lambda boolstr: (boolstr.lower() == "true"),
        "partialveto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "legtypeid": int,
    }
    return waleg.call("SessionLaw", "GetSessionLawByBillId", argdict, keydict)


def get_session_law_by_initiative_number(initiative_number: int) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/sessionlawservice.asmx?op=GetSessionLawByInitiativeNumber"""
    argdict: Dict[str, Any] = dict(initiativeNumber=initiative_number)
    keydict: Dict[str, Any] = {
        "chapternumber": int,
        "year": int,
        "legislaturenumber": int,
        "effectivedate": parser.parse,
        "multipleeffectivedates": lambda boolstr: (boolstr.lower() == "true"),
        "partialveto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "legtypeid": int,
    }
    return waleg.call("SessionLaw", "GetSessionLawByInitiativeNumber", argdict, keydict)
