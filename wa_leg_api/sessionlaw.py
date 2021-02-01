from typing import Dict
from datetime import datetime
import waleg

def get_session_law_by_bill(bill_number:int,biennium:str=None) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("SessionLaw", "GetSessionLawByBill", argdict=dict(biennium=biennium,billNumber=bill_number))


def get_bill_by_chapter_number(year:int,session:int,chapter_number:int) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("SessionLaw", "GetBillByChapterNumber", argdict=dict(year=year,session=session,chapterNumber=chapter_number))


def get_chapter_numbers_by_year(year:int) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("SessionLaw", "GetChapterNumbersByYear", argdict=dict(year=year))


def get_session_law_by_bill_id(biennium:str=None,bill_id:str=None) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("SessionLaw", "GetSessionLawByBillId", argdict=dict(biennium=biennium,billId=bill_id))


def get_session_law_by_initiative_number(initiative_number:int) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("SessionLaw", "GetSessionLawByInitiativeNumber", argdict=dict(initiativeNumber=initiative_number))


