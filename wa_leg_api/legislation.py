from typing import Dict
from datetime import datetime  # noqa
from wa_leg_api import waleg


def get_amendments_for_year(year: int, bill_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetAmendmentsForYear"""
    argdict = dict(year=year, billNumber=bill_number)
    return waleg.call("Legislation", "GetAmendmentsForYear", argdict)


def get_amendments_for_biennium(biennium: str, bill_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetAmendmentsForBiennium"""
    argdict = dict(biennium=biennium, billNumber=bill_number)
    return waleg.call("Legislation", "GetAmendmentsForBiennium", argdict)


def get_hearings(biennium: str, bill_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetHearings"""
    argdict = dict(biennium=biennium, billNumber=bill_number)
    return waleg.call("Legislation", "GetHearings", argdict)


def get_legislation_by_request_number(biennium: str, request_number: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationByRequestNumber"""
    argdict = dict(biennium=biennium, requestNumber=request_number)
    return waleg.call("Legislation", "GetLegislationByRequestNumber", argdict)


def get_rcw_cites_affected(biennium: str, bill_id: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetRcwCitesAffected"""
    argdict = dict(biennium=biennium, billId=bill_id)
    return waleg.call("Legislation", "GetRcwCitesAffected", argdict)


def get_session_law_chapter(biennium: str, bill_id: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSessionLawChapter"""
    argdict = dict(biennium=biennium, billId=bill_id)
    return waleg.call("Legislation", "GetSessionLawChapter", argdict)


def get_sponsors(biennium: str, bill_id: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSponsors"""
    argdict = dict(biennium=biennium, billId=bill_id)
    return waleg.call("Legislation", "GetSponsors", argdict)


def get_roll_calls(biennium: str, bill_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetRollCalls"""
    argdict = dict(biennium=biennium, billNumber=bill_number)
    return waleg.call("Legislation", "GetRollCalls", argdict)


def get_current_status(biennium: str, bill_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetCurrentStatus"""
    argdict = dict(biennium=biennium, billNumber=bill_number)
    return waleg.call("Legislation", "GetCurrentStatus", argdict)


def get_legislation_types() -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationTypes"""
    argdict = dict()
    return waleg.call("Legislation", "GetLegislationTypes", argdict)


def get_total_legislation_introduced_by_date_range(begin_date: datetime, end_date: datetime, leg_type_id: int, agency_id: int, all_versions: bool) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetTotalLegislationIntroducedByDateRange"""
    argdict = dict(beginDate=begin_date, endDate=end_date, legTypeId=leg_type_id, agencyId=agency_id, allVersions=all_versions)
    return waleg.call("Legislation", "GetTotalLegislationIntroducedByDateRange", argdict)


def get_legislation(biennium: str, bill_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislation"""
    argdict = dict(biennium=biennium, billNumber=bill_number)
    return waleg.call("Legislation", "GetLegislation", argdict)


def get_legislation_introduced_since(since_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationIntroducedSince"""
    argdict = dict(sinceDate=since_date)
    return waleg.call("Legislation", "GetLegislationIntroducedSince", argdict)


def get_prefiled_legislation() -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetPrefiledLegislation"""
    argdict = dict()
    return waleg.call("Legislation", "GetPrefiledLegislation", argdict)


def get_legislative_status_changes_by_bill_number(biennium: str, bill_number: int, begin_date: datetime, end_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislativeStatusChangesByBillNumber"""
    argdict = dict(biennium=biennium, billNumber=bill_number, beginDate=begin_date, endDate=end_date)
    return waleg.call("Legislation", "GetLegislativeStatusChangesByBillNumber", argdict)


def get_legislative_status_changes_by_bill_id(biennium: str, bill_id: str, begin_date: datetime, end_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislativeStatusChangesByBillId"""
    argdict = dict(biennium=biennium, billId=bill_id, beginDate=begin_date, endDate=end_date)
    return waleg.call("Legislation", "GetLegislativeStatusChangesByBillId", argdict)


def get_legislative_status_changes_by_date_range(biennium: str, begin_date: datetime, end_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislativeStatusChangesByDateRange"""
    argdict = dict(biennium=biennium, beginDate=begin_date, endDate=end_date)
    return waleg.call("Legislation", "GetLegislativeStatusChangesByDateRange", argdict)


def get_legislation_by_year(year: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationByYear"""
    argdict = dict(year=year)
    return waleg.call("Legislation", "GetLegislationByYear", argdict)


def get_legislation_info_introduced_since(since_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationInfoIntroducedSince"""
    argdict = dict(sinceDate=since_date)
    return waleg.call("Legislation", "GetLegislationInfoIntroducedSince", argdict)


def get_pre_filed_legislation_info() -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetPreFiledLegislationInfo"""
    argdict = dict()
    return waleg.call("Legislation", "GetPreFiledLegislationInfo", argdict)


def get_house_legislation_passed_house(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetHouseLegislationPassedHouse"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetHouseLegislationPassedHouse", argdict)


def get_house_legislation_passed_senate(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetHouseLegislationPassedSenate"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetHouseLegislationPassedSenate", argdict)


def get_senate_legislation_passed_senate(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSenateLegislationPassedSenate"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetSenateLegislationPassedSenate", argdict)


def get_senate_legislation_passed_house(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSenateLegislationPassedHouse"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetSenateLegislationPassedHouse", argdict)


def get_legislation_passed_legislature(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedLegislature"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetLegislationPassedLegislature", argdict)


def get_legislation_passed_legislature_within_time_frame(begin_date: datetime, end_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedLegislatureWithinTimeFrame"""
    argdict = dict(beginDate=begin_date, endDate=end_date)
    return waleg.call("Legislation", "GetLegislationPassedLegislatureWithinTimeFrame", argdict)


def get_legislation_passed_house(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedHouse"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetLegislationPassedHouse", argdict)


def get_legislation_passed_senate(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedSenate"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetLegislationPassedSenate", argdict)


def get_legislation_governor_signed(biennium: str, agency: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationGovernorSigned"""
    argdict = dict(biennium=biennium, agency=agency)
    return waleg.call("Legislation", "GetLegislationGovernorSigned", argdict)


def get_legislation_governor_veto(biennium: str, agency: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationGovernorVeto"""
    argdict = dict(biennium=biennium, agency=agency)
    return waleg.call("Legislation", "GetLegislationGovernorVeto", argdict)


def get_legislation_governor_partial_veto(biennium: str, agency: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationGovernorPartialVeto"""
    argdict = dict(biennium=biennium, agency=agency)
    return waleg.call("Legislation", "GetLegislationGovernorPartialVeto", argdict)


def get_published_enrolled_legislation(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetPublishedEnrolledLegislation"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetPublishedEnrolledLegislation", argdict)


def get_legislation_passed_house_within_time_frame(begin_date: datetime, end_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedHouseWithinTimeFrame"""
    argdict = dict(beginDate=begin_date, endDate=end_date)
    return waleg.call("Legislation", "GetLegislationPassedHouseWithinTimeFrame", argdict)


def get_legislation_passed_senate_within_time_frame(begin_date: datetime, end_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedSenateWithinTimeFrame"""
    argdict = dict(beginDate=begin_date, endDate=end_date)
    return waleg.call("Legislation", "GetLegislationPassedSenateWithinTimeFrame", argdict)


def get_legislation_not_yet_introduced_in_house_of_origin(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationNotYetIntroducedInHouseOfOrigin"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetLegislationNotYetIntroducedInHouseOfOrigin", argdict)


def get_legislation_passed_original_body_and_not_introduced_in_opposite_body(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedOriginalBodyAndNotIntroducedInOppositeBody"""
    argdict = dict(biennium=biennium)
    return waleg.call("Legislation", "GetLegislationPassedOriginalBodyAndNotIntroducedInOppositeBody", argdict)


def get_legislative_bill_list_feature_data() -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislativeBillListFeatureData"""
    argdict = dict()
    return waleg.call("Legislation", "GetLegislativeBillListFeatureData", argdict)
