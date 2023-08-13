from datetime import datetime  # noqa
from typing import Any, Dict

from dateutil import parser  # noqa

from wa_leg_api import waleg


def get_session_law_by_bill(biennium: str, bill_number: int) -> Dict[str, Any]:
    """Returns session law information for a bill. Note: This will not return information on Initiatives to the Legislature.
    Exception thrown for invalid biennium or when no session law found.
    Expects biennium to be in the format: 2005-06.

    See: http://wslwebservices.leg.wa.gov/sessionlawservice.asmx?op=GetSessionLawByBill"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "chapter_number": int,
        "year": int,
        "legislature_number": int,
        "effective_date": parser.parse,
        "multiple_effective_dates": lambda boolstr: (boolstr.lower() == "true"),
        "partial_veto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "leg_type_id": int,
    }
    return waleg.call("SessionLaw", "GetSessionLawByBill", argdict, keydict)


def get_bill_by_chapter_number(year: int, session: int, chapter_number: int) -> Dict[str, Any]:
    """Returns Bill information for a chapter.
    Exception thrown for invalid year or when no legislation found.
    Expects year in the format: YYYY. Session is the SessionCode (0=Regular Session, 1=1st Special Session, etc.).

    See: http://wslwebservices.leg.wa.gov/sessionlawservice.asmx?op=GetBillByChapterNumber"""
    argdict: Dict[str, Any] = dict(year=year, session=session, chapterNumber=chapter_number)
    keydict: Dict[str, Any] = {
        "state_fiscal_note": lambda boolstr: (boolstr.lower() == "true"),
        "local_fiscal_note": lambda boolstr: (boolstr.lower() == "true"),
        "appropriations": lambda boolstr: (boolstr.lower() == "true"),
        "requested_by_governor": lambda boolstr: (boolstr.lower() == "true"),
        "requested_by_budget_committee": lambda boolstr: (boolstr.lower() == "true"),
        "requested_by_department": lambda boolstr: (boolstr.lower() == "true"),
        "requested_by_other": lambda boolstr: (boolstr.lower() == "true"),
        "introduced_date": parser.parse,
        "action_date": parser.parse,
        "amended_by_opposite_body": lambda boolstr: (boolstr.lower() == "true"),
        "partial_veto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "amendments_exist": lambda boolstr: (boolstr.lower() == "true"),
        "prime_sponsor_i_d": int,
    }
    return waleg.call("SessionLaw", "GetBillByChapterNumber", argdict, keydict)


def get_chapter_numbers_by_year(year: int) -> Dict[str, Any]:
    """Returns all Chapters for a year.
    Exception thrown for invalid year.
    Expects year in the format: YYYY.

    See: http://wslwebservices.leg.wa.gov/sessionlawservice.asmx?op=GetChapterNumbersByYear"""
    argdict: Dict[str, Any] = dict(year=year)
    keydict: Dict[str, Any] = {
        "chapter_number": int,
        "year": int,
        "legislature_number": int,
        "effective_date": parser.parse,
        "multiple_effective_dates": lambda boolstr: (boolstr.lower() == "true"),
        "partial_veto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "leg_type_id": int,
    }
    return waleg.call("SessionLaw", "GetChapterNumbersByYear", argdict, keydict)


def get_session_law_by_bill_id(biennium: str, bill_id: str) -> Dict[str, Any]:
    """Returns session law information for a billId.
    Exception thrown for invalid biennium or when no session law found.
    Expects biennium to be in the format: 2005-06.

    See: http://wslwebservices.leg.wa.gov/sessionlawservice.asmx?op=GetSessionLawByBillId"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billId=bill_id)
    keydict: Dict[str, Any] = {
        "chapter_number": int,
        "year": int,
        "legislature_number": int,
        "effective_date": parser.parse,
        "multiple_effective_dates": lambda boolstr: (boolstr.lower() == "true"),
        "partial_veto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "leg_type_id": int,
    }
    return waleg.call("SessionLaw", "GetSessionLawByBillId", argdict, keydict)


def get_session_law_by_initiative_number(initiative_number: int) -> Dict[str, Any]:
    """Returns session law information for an Initiative to the Legislature.
    Exception thrown when no session law found.

    See: http://wslwebservices.leg.wa.gov/sessionlawservice.asmx?op=GetSessionLawByInitiativeNumber"""
    argdict: Dict[str, Any] = dict(initiativeNumber=initiative_number)
    keydict: Dict[str, Any] = {
        "chapter_number": int,
        "year": int,
        "legislature_number": int,
        "effective_date": parser.parse,
        "multiple_effective_dates": lambda boolstr: (boolstr.lower() == "true"),
        "partial_veto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "leg_type_id": int,
    }
    return waleg.call("SessionLaw", "GetSessionLawByInitiativeNumber", argdict, keydict)
