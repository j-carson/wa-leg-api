from typing import Dict
from datetime import datetime  # noqa
from . import waleg


def get_amendments_for_year(year: int, bill_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetAmendmentsForYear"""
    argdict = dict(year=year, billNumber=bill_number)
    return waleg.call("Legislation", "GetAmendmentsForYear", argdict=argdict)


def get_amendments_for_biennium(biennium: str, bill_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetAmendmentsForBiennium"""
    argdict = dict(biennium=biennium, billNumber=bill_number)
    return waleg.call("Legislation", "GetAmendmentsForBiennium", argdict=argdict)


def get_hearings(biennium: str, bill_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetHearings"""
    argdict = dict(biennium=biennium, billNumber=bill_number)
    return waleg.call("Legislation", "GetHearings", argdict=argdict)


def get_legislation_by_request_number(biennium: str, request_number: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationByRequestNumber"""
    argdict = dict(biennium=biennium, requestNumber=request_number)
    return waleg.call("Legislation", "GetLegislationByRequestNumber", argdict=argdict)


def get_rcw_cites_affected(biennium: str, bill_id: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetRcwCitesAffected"""
    argdict = dict(biennium=biennium, billId=bill_id)
    return waleg.call("Legislation", "GetRcwCitesAffected", argdict=argdict)


def get_session_law_chapter(biennium: str, bill_id: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSessionLawChapter"""
    argdict = dict(biennium=biennium, billId=bill_id)
    return waleg.call("Legislation", "GetSessionLawChapter", argdict=argdict)


def get_sponsors(biennium: str, bill_id: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSponsors"""
    argdict = dict(biennium=biennium, billId=bill_id)
    return waleg.call("Legislation", "GetSponsors", argdict=argdict)


def get_roll_calls(biennium: str, bill_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetRollCalls"""
    argdict = dict(biennium=biennium, billNumber=bill_number)
    return waleg.call("Legislation", "GetRollCalls", argdict=argdict)


def get_current_status(biennium: str, bill_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetCurrentStatus"""
    argdict = dict(biennium=biennium, billNumber=bill_number)
    return waleg.call("Legislation", "GetCurrentStatus", argdict=argdict)


def get_legislation_types() -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationTypes"""
    argdict = dict()
    return waleg.call("Legislation", "GetLegislationTypes", argdict=argdict)


def get_total_legislation_introduced_by_date_range(begin_date: datetime, end_date: datetime, leg_type_id: int, agency_id: int, all_versions: bool) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetTotalLegislationIntroducedByDateRange"""
    argdict = dict(beginDate=begin_date, endDate=end_date, legTypeId=leg_type_id, agencyId=agency_id, allVersions=all_versions)
    return waleg.call("Legislation", "GetTotalLegislationIntroducedByDateRange", argdict=argdict)


def get_legislation(biennium: str, bill_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislation"""
    argdict = dict(biennium=biennium, billNumber=bill_number)
    return waleg.call("Legislation", "GetLegislation", argdict=argdict)


def get_legislation_introduced_since(since_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationIntroducedSince"""
    argdict = dict(sinceDate=since_date)
    return waleg.call("Legislation", "GetLegislationIntroducedSince", argdict=argdict)


def get_prefiled_legislation() -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetPrefiledLegislation"""
    argdict = dict()
    return waleg.call("Legislation", "GetPrefiledLegislation", argdict=argdict)


def get_legislative_status_changes_by_bill_number(biennium: str, bill_number: int, begin_date: datetime, end_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislativeStatusChangesByBillNumber"""
    argdict = dict(biennium=biennium, billNumber=bill_number, beginDate=begin_date, endDate=end_date)
    return waleg.call("Legislation", "GetLegislativeStatusChangesByBillNumber", argdict=argdict)


def get_legislative_status_changes_by_bill_id(biennium: str, bill_id: str, begin_date: datetime, end_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislativeStatusChangesByBillId"""
    argdict = dict(biennium=biennium, billId=bill_id, beginDate=begin_date, endDate=end_date)
    return waleg.call("Legislation", "GetLegislativeStatusChangesByBillId", argdict=argdict)


def get_legislative_status_changes_by_date_range(biennium: str, begin_date: datetime, end_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislativeStatusChangesByDateRange"""
    argdict = dict(biennium=biennium, beginDate=begin_date, endDate=end_date)
    return waleg.call("Legislation", "GetLegislativeStatusChangesByDateRange", argdict=argdict)


def get_legislation_by_year(year: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationByYear"""
    argdict = dict(year=year)
    return waleg.call("Legislation", "GetLegislationByYear", argdict=argdict)


def get_legislation_info_introduced_since(since_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationInfoIntroducedSince"""
    argdict = dict(sinceDate=since_date)
    return waleg.call("Legislation", "GetLegislationInfoIntroducedSince", argdict=argdict)


def get_pre_filed_legislation_info() -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetPreFiledLegislationInfo"""
    argdict = dict()
    return waleg.call("Legislation", "GetPreFiledLegislationInfo", argdict=argdict)


def get_house_legislation_passed_house(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetHouseLegislationPassedHouse"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetHouseLegislationPassedHouse", argdict=argdict)


def get_house_legislation_passed_senate(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetHouseLegislationPassedSenate"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetHouseLegislationPassedSenate", argdict=argdict)


def get_senate_legislation_passed_senate(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSenateLegislationPassedSenate"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetSenateLegislationPassedSenate", argdict=argdict)


def get_senate_legislation_passed_house(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSenateLegislationPassedHouse"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetSenateLegislationPassedHouse", argdict=argdict)


def get_legislation_passed_legislature(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedLegislature"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetLegislationPassedLegislature", argdict=argdict)


def get_legislation_passed_legislature_within_time_frame(begin_date: datetime, end_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedLegislatureWithinTimeFrame"""
    argdict = dict(beginDate=begin_date, endDate=end_date)
    return waleg.call("Legislation", "GetLegislationPassedLegislatureWithinTimeFrame", argdict=argdict)


def get_legislation_passed_house(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedHouse"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetLegislationPassedHouse", argdict=argdict)


def get_legislation_passed_senate(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedSenate"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetLegislationPassedSenate", argdict=argdict)


def get_legislation_governor_signed(biennium: str, agency: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationGovernorSigned"""
    argdict = dict(biennium=biennium, agency=agency)
    return waleg.call("Legislation", "GetLegislationGovernorSigned", argdict=argdict)


def get_legislation_governor_veto(biennium: str, agency: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationGovernorVeto"""
    argdict = dict(biennium=biennium, agency=agency)
    return waleg.call("Legislation", "GetLegislationGovernorVeto", argdict=argdict)


def get_legislation_governor_partial_veto(biennium: str, agency: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationGovernorPartialVeto"""
    argdict = dict(biennium=biennium, agency=agency)
    return waleg.call("Legislation", "GetLegislationGovernorPartialVeto", argdict=argdict)


def get_published_enrolled_legislation(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetPublishedEnrolledLegislation"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetPublishedEnrolledLegislation", argdict=argdict)


def get_legislation_passed_house_within_time_frame(begin_date: datetime, end_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedHouseWithinTimeFrame"""
    argdict = dict(beginDate=begin_date, endDate=end_date)
    return waleg.call("Legislation", "GetLegislationPassedHouseWithinTimeFrame", argdict=argdict)


def get_legislation_passed_senate_within_time_frame(begin_date: datetime, end_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedSenateWithinTimeFrame"""
    argdict = dict(beginDate=begin_date, endDate=end_date)
    return waleg.call("Legislation", "GetLegislationPassedSenateWithinTimeFrame", argdict=argdict)


def get_legislation_not_yet_introduced_in_house_of_origin(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationNotYetIntroducedInHouseOfOrigin"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetLegislationNotYetIntroducedInHouseOfOrigin", argdict=argdict)


def get_legislation_passed_original_body_and_not_introduced_in_opposite_body(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedOriginalBodyAndNotIntroducedInOppositeBody"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetLegislationPassedOriginalBodyAndNotIntroducedInOppositeBody", argdict=argdict)


def get_legislative_bill_list_feature_data() -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislativeBillListFeatureData"""
    argdict = dict()
    return waleg.call("Legislation", "GetLegislativeBillListFeatureData", argdict=argdict)
