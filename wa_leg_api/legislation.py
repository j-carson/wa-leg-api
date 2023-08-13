from datetime import datetime  # noqa
from typing import Any, Dict

from dateutil import parser  # noqa

from wa_leg_api import waleg


def get_amendments_for_year(year: int, bill_number: int) -> Dict[str, Any]:
    """Returns a list of all pending and acted on amendments for the bill during the year.
    Exception thrown for invalid year.

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetAmendmentsForYear"""
    argdict: Dict[str, Any] = dict(year=year, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "floor_number": int,
        "floor_action_date": parser.parse,
        "document_exists": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetAmendmentsForYear", argdict, keydict)


def get_amendments_for_biennium(biennium: str, bill_number: int) -> Dict[str, Any]:
    """Returns a list of all pending and acted on amendments for the bill during the biennium.
    Exception thrown for invalid biennium.
    Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetAmendmentsForBiennium"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "floor_number": int,
        "floor_action_date": parser.parse,
        "document_exists": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetAmendmentsForBiennium", argdict, keydict)


def get_hearings(biennium: str, bill_number: int) -> Dict[str, Any]:
    """Returns a list of committee hearings for the bill.
    Exception thrown for invalid biennium.
    Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetHearings"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "agenda_id": int,
        "zip_code": int,
        "date": parser.parse,
        "cancelled": lambda boolstr: (boolstr.lower() == "true"),
        "revised_date": parser.parse,
    }
    return waleg.call("Legislation", "GetHearings", argdict, keydict)


def get_legislation_by_request_number(biennium: str, request_number: str) -> Dict[str, Any]:
    """Returns legislation information based on the original request number of the draft submitted.
    Exception thrown for invalid biennium or requestNumber or if no information found.
    Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationByRequestNumber"""
    argdict: Dict[str, Any] = dict(biennium=biennium, requestNumber=request_number)
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
    return waleg.call("Legislation", "GetLegislationByRequestNumber", argdict, keydict)


def get_rcw_cites_affected(biennium: str, bill_id: str) -> Dict[str, Any]:
    """Returns RCW Cites referenced within the legislation.
    Exception thrown for invalid biennium or billId.
    Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetRcwCitesAffected"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billId=bill_id)
    keydict: Dict[str, Any] = {}
    return waleg.call("Legislation", "GetRcwCitesAffected", argdict, keydict)


def get_session_law_chapter(biennium: str, bill_id: str) -> Dict[str, Any]:
    """Returns chapter and session law information on given bill.
    Exception thrown for invalid biennium or billId.
    Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSessionLawChapter"""
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
    return waleg.call("Legislation", "GetSessionLawChapter", argdict, keydict)


def get_sponsors(biennium: str, bill_id: str) -> Dict[str, Any]:
    """Returns list of bill sponsors.
    Exception thrown for invalid biennium or billId.
    Expects biennium in the format 2005-06.

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSponsors"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billId=bill_id)
    keydict: Dict[str, Any] = {
        "order": int,
    }
    return waleg.call("Legislation", "GetSponsors", argdict, keydict)


def get_roll_calls(biennium: str, bill_number: int) -> Dict[str, Any]:
    """Returns list of roll calls taken on the bill.
    Exception thrown for invalid biennium.
    Expects biennium in the format 2005-06.

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetRollCalls"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "sequence_number": int,
        "vote_date": parser.parse,
        "count": int,
        "member_id": int,
    }
    return waleg.call("Legislation", "GetRollCalls", argdict, keydict)


def get_current_status(biennium: str, bill_number: int) -> Dict[str, Any]:
    """Returns the current status of the bill in the legislative process.
    Exception thrown for invalid biennium or if no status found.
    Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetCurrentStatus"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "action_date": parser.parse,
        "amended_by_opposite_body": lambda boolstr: (boolstr.lower() == "true"),
        "partial_veto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "amendments_exist": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetCurrentStatus", argdict, keydict)


def get_legislation_types() -> Dict[str, Any]:
    """Returns a list of all valid types of legislation.

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationTypes"""
    argdict: Dict[str, Any] = dict()
    keydict: Dict[str, Any] = {}
    return waleg.call("Legislation", "GetLegislationTypes", argdict, keydict)


def get_total_legislation_introduced_by_date_range(
    begin_date: datetime, end_date: datetime, leg_type_id: int, agency_id: int, all_versions: bool
) -> Dict[str, Any]:
    """Returns legislation introduced in the given date range by the given legislation type.

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetTotalLegislationIntroducedByDateRange
    """
    argdict: Dict[str, Any] = dict(
        beginDate=begin_date,
        endDate=end_date,
        legTypeId=leg_type_id,
        agencyId=agency_id,
        allVersions=all_versions,
    )
    keydict: Dict[str, Any] = {
        "get_total_legislation_introduced_by_date_range_result": int,
    }
    return waleg.call("Legislation", "GetTotalLegislationIntroducedByDateRange", argdict, keydict)


def get_legislation(biennium: str, bill_number: int) -> Dict[str, Any]:
    """Returns legislation information on the bill.  If substitutes to the bill have been proposed, they will be listed separately.  The active flag is true for versions that can be passed on the floor.
    Exception thrown for invalid biennium.
    Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislation"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
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
    return waleg.call("Legislation", "GetLegislation", argdict, keydict)


def get_legislation_introduced_since(since_date: datetime) -> Dict[str, Any]:
    """Returns detailed legislation information on all bills introduced since the date given.  If substitutes to the bill have been proposed, they will be listed separately.  The active flag is true for versions that can be passed on the floor.

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationIntroducedSince"""
    argdict: Dict[str, Any] = dict(sinceDate=since_date)
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
    return waleg.call("Legislation", "GetLegislationIntroducedSince", argdict, keydict)


def get_prefiled_legislation() -> Dict[str, Any]:
    """Returns detailed legislation information on all prefiled bills (currently in prefiled status).
    Once a bill is formally introduced, its information can be obtained by calling the GetLegislation method.

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetPrefiledLegislation"""
    argdict: Dict[str, Any] = dict()
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
    return waleg.call("Legislation", "GetPrefiledLegislation", argdict, keydict)


def get_legislative_status_changes_by_bill_number(
    biennium: str, bill_number: int, begin_date: datetime, end_date: datetime
) -> Dict[str, Any]:
    """

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislativeStatusChangesByBillNumber
    """
    argdict: Dict[str, Any] = dict(
        biennium=biennium, billNumber=bill_number, beginDate=begin_date, endDate=end_date
    )
    keydict: Dict[str, Any] = {
        "action_date": parser.parse,
        "amended_by_opposite_body": lambda boolstr: (boolstr.lower() == "true"),
        "partial_veto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "amendments_exist": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislativeStatusChangesByBillNumber", argdict, keydict)


def get_legislative_status_changes_by_bill_id(
    biennium: str, bill_id: str, begin_date: datetime, end_date: datetime
) -> Dict[str, Any]:
    """

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislativeStatusChangesByBillId"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billId=bill_id, beginDate=begin_date, endDate=end_date)
    keydict: Dict[str, Any] = {
        "action_date": parser.parse,
        "amended_by_opposite_body": lambda boolstr: (boolstr.lower() == "true"),
        "partial_veto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "amendments_exist": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislativeStatusChangesByBillId", argdict, keydict)


def get_legislative_status_changes_by_date_range(
    biennium: str, begin_date: datetime, end_date: datetime
) -> Dict[str, Any]:
    """

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislativeStatusChangesByDateRange"""
    argdict: Dict[str, Any] = dict(biennium=biennium, beginDate=begin_date, endDate=end_date)
    keydict: Dict[str, Any] = {
        "action_date": parser.parse,
        "amended_by_opposite_body": lambda boolstr: (boolstr.lower() == "true"),
        "partial_veto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "amendments_exist": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislativeStatusChangesByDateRange", argdict, keydict)


def get_legislation_by_year(year: int) -> Dict[str, Any]:
    """Returns summary legislation information on all bills active during the year.  If substitutes to the bill have been proposed, they will be listed separately.  The active flag is true for versions that can be passed on the floor.
    Exception thrown for invalid year.
    Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationByYear"""
    argdict: Dict[str, Any] = dict(year=year)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationByYear", argdict, keydict)


def get_legislation_info_introduced_since(since_date: datetime) -> Dict[str, Any]:
    """Returns summary legislation information on all bills introduced since the date given.  If substitutes to the bill have been proposed, they will be listed separately.  The active flag is true for versions that can be passed on the floor.

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationInfoIntroducedSince"""
    argdict: Dict[str, Any] = dict(sinceDate=since_date)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationInfoIntroducedSince", argdict, keydict)


def get_pre_filed_legislation_info() -> Dict[str, Any]:
    """Returns summary legislation information on all prefiled bills (currently in prefiled status).
    Once a bill is formally introduced, its information can be obtained by calling the GetLegislation method.

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetPreFiledLegislationInfo"""
    argdict: Dict[str, Any] = dict()
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetPreFiledLegislationInfo", argdict, keydict)


def get_house_legislation_passed_house(biennium: str) -> Dict[str, Any]:
    """Returns summary legislation information on all House bills that have passed the House.<br/>Exception thrown for invalid biennium.<br/>Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetHouseLegislationPassedHouse"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetHouseLegislationPassedHouse", argdict, keydict)


def get_house_legislation_passed_senate(biennium: str) -> Dict[str, Any]:
    """Returns summary legislation information on all House bills that have passed the Senate.<br/>Exception thrown for invalid biennium.<br/>Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetHouseLegislationPassedSenate"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetHouseLegislationPassedSenate", argdict, keydict)


def get_senate_legislation_passed_senate(biennium: str) -> Dict[str, Any]:
    """Returns summary legislation information on all Senate bills that have passed the Senate.<br/>Exception thrown for invalid biennium.<br/>Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSenateLegislationPassedSenate"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetSenateLegislationPassedSenate", argdict, keydict)


def get_senate_legislation_passed_house(biennium: str) -> Dict[str, Any]:
    """Returns summary legislation information on all Senate bills that have passed the House.<br/>Exception thrown for invalid biennium.<br/>Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSenateLegislationPassedHouse"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetSenateLegislationPassedHouse", argdict, keydict)


def get_legislation_passed_legislature(biennium: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills that have passed the legislature.<br/>Exception thrown for invalid biennium.<br/>Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedLegislature"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationPassedLegislature", argdict, keydict)


def get_legislation_passed_legislature_within_time_frame(
    begin_date: datetime, end_date: datetime
) -> Dict[str, Any]:
    """Returns summary legislation information on all bills that have passed the legislature within the begin and end date.

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedLegislatureWithinTimeFrame
    """
    argdict: Dict[str, Any] = dict(beginDate=begin_date, endDate=end_date)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationPassedLegislatureWithinTimeFrame", argdict, keydict)


def get_legislation_passed_house(biennium: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills that have passed the House.<br/>Exception thrown for invalid biennium.<br/>Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedHouse"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationPassedHouse", argdict, keydict)


def get_legislation_passed_senate(biennium: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills that have passed the Senate.<br/>Exception thrown for invalid biennium.<br/>Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedSenate"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationPassedSenate", argdict, keydict)


def get_legislation_governor_signed(biennium: str, agency: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills that have been signed by the governor.<br/>Exception thrown for invalid agency or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationGovernorSigned"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationGovernorSigned", argdict, keydict)


def get_legislation_governor_veto(biennium: str, agency: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills that have been vetoed by the governor.<br/>Exception thrown for invalid agency or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationGovernorVeto"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationGovernorVeto", argdict, keydict)


def get_legislation_governor_partial_veto(biennium: str, agency: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills that have been partially vetoed by the governor.<br/>Exception thrown for invalid agency or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationGovernorPartialVeto"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationGovernorPartialVeto", argdict, keydict)


def get_published_enrolled_legislation(biennium: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills that have been enrolled and published by the legislature.<br/>Exception thrown for invalid biennium.<br/>Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetPublishedEnrolledLegislation"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetPublishedEnrolledLegislation", argdict, keydict)


def get_legislation_passed_house_within_time_frame(
    begin_date: datetime, end_date: datetime
) -> Dict[str, Any]:
    """Returns summary legislation information on all bills that House passed off the floor for the first time between the begin and end date (even if the bill is not currently passed the House - For example, a House bill that the House passed may have been amended in the Senate and the House has not passed the amended version of the bill.  This bill would still be returned in this method.  If you don't want that bill, use the GetLegislationPassedHouse.).

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedHouseWithinTimeFrame
    """
    argdict: Dict[str, Any] = dict(beginDate=begin_date, endDate=end_date)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationPassedHouseWithinTimeFrame", argdict, keydict)


def get_legislation_passed_senate_within_time_frame(
    begin_date: datetime, end_date: datetime
) -> Dict[str, Any]:
    """Returns summary legislation information on all bills that Senate passed off the floor for the first time between the begin and end date (even if the bill is not currently passed the House - For example, a Senate bill that the Senate passed may have been amended in the House and the Senate has not passed the amended version of the bill.  This bill would still be returned in this method.  If you don't want that bill, use the GetLegislationPassedSenate.).

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedSenateWithinTimeFrame
    """
    argdict: Dict[str, Any] = dict(beginDate=begin_date, endDate=end_date)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationPassedSenateWithinTimeFrame", argdict, keydict)


def get_legislation_not_yet_introduced_in_house_of_origin(biennium: str) -> Dict[str, Any]:
    """Returns summary legislation information on bills that are active, have available bill text, and have not yet been introduced in the house of origin.<br/>Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationNotYetIntroducedInHouseOfOrigin
    """
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationNotYetIntroducedInHouseOfOrigin", argdict, keydict)


def get_legislation_passed_original_body_and_not_introduced_in_opposite_body(biennium: str) -> Dict[str, Any]:
    """Returns summary legislation information on bills that have passed the originating body and not yet introduced in opposite body.<br/>Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedOriginalBodyAndNotIntroducedInOppositeBody
    """
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call(
        "Legislation", "GetLegislationPassedOriginalBodyAndNotIntroducedInOppositeBody", argdict, keydict
    )
