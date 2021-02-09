from typing import Dict
from datetime import datetime  # noqa
from wa_leg_api import waleg


def get_session_law_by_bill(biennium: str, bill_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/sessionlawservice.asmx?op=GetSessionLawByBill"""
    argdict = dict(biennium=biennium, billNumber=bill_number)
    return waleg.call("SessionLaw", "GetSessionLawByBill", argdict)


def get_bill_by_chapter_number(year: int, session: int, chapter_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/sessionlawservice.asmx?op=GetBillByChapterNumber"""
    argdict = dict(year=year, session=session, chapterNumber=chapter_number)
    return waleg.call("SessionLaw", "GetBillByChapterNumber", argdict)


def get_chapter_numbers_by_year(year: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/sessionlawservice.asmx?op=GetChapterNumbersByYear"""
    argdict = dict(year=year)
    return waleg.call("SessionLaw", "GetChapterNumbersByYear", argdict)


def get_session_law_by_bill_id(biennium: str, bill_id: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/sessionlawservice.asmx?op=GetSessionLawByBillId"""
    argdict = dict(biennium=biennium, billId=bill_id)
    return waleg.call("SessionLaw", "GetSessionLawByBillId", argdict)


def get_session_law_by_initiative_number(initiative_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/sessionlawservice.asmx?op=GetSessionLawByInitiativeNumber"""
    argdict = dict(initiativeNumber=initiative_number)
    return waleg.call("SessionLaw", "GetSessionLawByInitiativeNumber", argdict)
