from datetime import datetime  # noqa
from typing import Any, Dict

from dateutil import parser  # noqa

from wa_leg_api import waleg


def get_amendments_for_year(year: int, bill_number: int) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetAmendmentsForYear"""
    argdict: Dict[str, Any] = dict(year=year, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "floornumber": int,
        "flooractiondate": parser.parse,
        "documentexists": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetAmendmentsForYear", argdict, keydict)


def get_amendments_for_biennium(biennium: str, bill_number: int) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetAmendmentsForBiennium"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "floornumber": int,
        "flooractiondate": parser.parse,
        "documentexists": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetAmendmentsForBiennium", argdict, keydict)


def get_hearings(biennium: str, bill_number: int) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetHearings"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "agendaid": int,
        "zipcode": int,
        "date": parser.parse,
        "cancelled": lambda boolstr: (boolstr.lower() == "true"),
        "reviseddate": parser.parse,
    }
    return waleg.call("Legislation", "GetHearings", argdict, keydict)


def get_legislation_by_request_number(biennium: str, request_number: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationByRequestNumber"""
    argdict: Dict[str, Any] = dict(biennium=biennium, requestNumber=request_number)
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
    return waleg.call("Legislation", "GetLegislationByRequestNumber", argdict, keydict)


def get_rcw_cites_affected(biennium: str, bill_id: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetRcwCitesAffected"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billId=bill_id)
    keydict: Dict[str, Any] = {}
    return waleg.call("Legislation", "GetRcwCitesAffected", argdict, keydict)


def get_session_law_chapter(biennium: str, bill_id: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSessionLawChapter"""
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
    return waleg.call("Legislation", "GetSessionLawChapter", argdict, keydict)


def get_sponsors(biennium: str, bill_id: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSponsors"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billId=bill_id)
    keydict: Dict[str, Any] = {
        "order": int,
    }
    return waleg.call("Legislation", "GetSponsors", argdict, keydict)


def get_roll_calls(biennium: str, bill_number: int) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetRollCalls"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "sequencenumber": int,
        "votedate": parser.parse,
        "count": int,
        "memberid": int,
    }
    return waleg.call("Legislation", "GetRollCalls", argdict, keydict)


def get_current_status(biennium: str, bill_number: int) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetCurrentStatus"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "actiondate": parser.parse,
        "amendedbyoppositebody": lambda boolstr: (boolstr.lower() == "true"),
        "partialveto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "amendmentsexist": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetCurrentStatus", argdict, keydict)


def get_legislation_types() -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationTypes"""
    argdict: Dict[str, Any] = dict()
    keydict: Dict[str, Any] = {}
    return waleg.call("Legislation", "GetLegislationTypes", argdict, keydict)


def get_total_legislation_introduced_by_date_range(
    begin_date: datetime, end_date: datetime, leg_type_id: int, agency_id: int, all_versions: bool
) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetTotalLegislationIntroducedByDateRange"""
    argdict: Dict[str, Any] = dict(
        beginDate=begin_date,
        endDate=end_date,
        legTypeId=leg_type_id,
        agencyId=agency_id,
        allVersions=all_versions,
    )
    keydict: Dict[str, Any] = {
        "gettotallegislationintroducedbydaterangeresult": int,
    }
    return waleg.call("Legislation", "GetTotalLegislationIntroducedByDateRange", argdict, keydict)


def get_legislation(biennium: str, bill_number: int) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislation"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
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
    return waleg.call("Legislation", "GetLegislation", argdict, keydict)


def get_legislation_introduced_since(since_date: datetime) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationIntroducedSince"""
    argdict: Dict[str, Any] = dict(sinceDate=since_date)
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
    return waleg.call("Legislation", "GetLegislationIntroducedSince", argdict, keydict)


def get_prefiled_legislation() -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetPrefiledLegislation"""
    argdict: Dict[str, Any] = dict()
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
    return waleg.call("Legislation", "GetPrefiledLegislation", argdict, keydict)


def get_legislative_status_changes_by_bill_number(
    biennium: str, bill_number: int, begin_date: datetime, end_date: datetime
) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislativeStatusChangesByBillNumber"""
    argdict: Dict[str, Any] = dict(
        biennium=biennium, billNumber=bill_number, beginDate=begin_date, endDate=end_date
    )
    keydict: Dict[str, Any] = {
        "actiondate": parser.parse,
        "amendedbyoppositebody": lambda boolstr: (boolstr.lower() == "true"),
        "partialveto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "amendmentsexist": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislativeStatusChangesByBillNumber", argdict, keydict)


def get_legislative_status_changes_by_bill_id(
    biennium: str, bill_id: str, begin_date: datetime, end_date: datetime
) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislativeStatusChangesByBillId"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billId=bill_id, beginDate=begin_date, endDate=end_date)
    keydict: Dict[str, Any] = {
        "actiondate": parser.parse,
        "amendedbyoppositebody": lambda boolstr: (boolstr.lower() == "true"),
        "partialveto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "amendmentsexist": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislativeStatusChangesByBillId", argdict, keydict)


def get_legislative_status_changes_by_date_range(
    biennium: str, begin_date: datetime, end_date: datetime
) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislativeStatusChangesByDateRange"""
    argdict: Dict[str, Any] = dict(biennium=biennium, beginDate=begin_date, endDate=end_date)
    keydict: Dict[str, Any] = {
        "actiondate": parser.parse,
        "amendedbyoppositebody": lambda boolstr: (boolstr.lower() == "true"),
        "partialveto": lambda boolstr: (boolstr.lower() == "true"),
        "veto": lambda boolstr: (boolstr.lower() == "true"),
        "amendmentsexist": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislativeStatusChangesByDateRange", argdict, keydict)


def get_legislation_by_year(year: int) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationByYear"""
    argdict: Dict[str, Any] = dict(year=year)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationByYear", argdict, keydict)


def get_legislation_info_introduced_since(since_date: datetime) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationInfoIntroducedSince"""
    argdict: Dict[str, Any] = dict(sinceDate=since_date)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationInfoIntroducedSince", argdict, keydict)


def get_pre_filed_legislation_info() -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetPreFiledLegislationInfo"""
    argdict: Dict[str, Any] = dict()
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetPreFiledLegislationInfo", argdict, keydict)


def get_house_legislation_passed_house(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetHouseLegislationPassedHouse"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetHouseLegislationPassedHouse", argdict, keydict)


def get_house_legislation_passed_senate(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetHouseLegislationPassedSenate"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetHouseLegislationPassedSenate", argdict, keydict)


def get_senate_legislation_passed_senate(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSenateLegislationPassedSenate"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetSenateLegislationPassedSenate", argdict, keydict)


def get_senate_legislation_passed_house(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetSenateLegislationPassedHouse"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetSenateLegislationPassedHouse", argdict, keydict)


def get_legislation_passed_legislature(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedLegislature"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationPassedLegislature", argdict, keydict)


def get_legislation_passed_legislature_within_time_frame(
    begin_date: datetime, end_date: datetime
) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedLegislatureWithinTimeFrame"""
    argdict: Dict[str, Any] = dict(beginDate=begin_date, endDate=end_date)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationPassedLegislatureWithinTimeFrame", argdict, keydict)


def get_legislation_passed_house(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedHouse"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationPassedHouse", argdict, keydict)


def get_legislation_passed_senate(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedSenate"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationPassedSenate", argdict, keydict)


def get_legislation_governor_signed(biennium: str, agency: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationGovernorSigned"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationGovernorSigned", argdict, keydict)


def get_legislation_governor_veto(biennium: str, agency: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationGovernorVeto"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationGovernorVeto", argdict, keydict)


def get_legislation_governor_partial_veto(biennium: str, agency: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationGovernorPartialVeto"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationGovernorPartialVeto", argdict, keydict)


def get_published_enrolled_legislation(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetPublishedEnrolledLegislation"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetPublishedEnrolledLegislation", argdict, keydict)


def get_legislation_passed_house_within_time_frame(
    begin_date: datetime, end_date: datetime
) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedHouseWithinTimeFrame"""
    argdict: Dict[str, Any] = dict(beginDate=begin_date, endDate=end_date)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationPassedHouseWithinTimeFrame", argdict, keydict)


def get_legislation_passed_senate_within_time_frame(
    begin_date: datetime, end_date: datetime
) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedSenateWithinTimeFrame"""
    argdict: Dict[str, Any] = dict(beginDate=begin_date, endDate=end_date)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationPassedSenateWithinTimeFrame", argdict, keydict)


def get_legislation_not_yet_introduced_in_house_of_origin(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationNotYetIntroducedInHouseOfOrigin"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("Legislation", "GetLegislationNotYetIntroducedInHouseOfOrigin", argdict, keydict)


def get_legislation_passed_original_body_and_not_introduced_in_opposite_body(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislationservice.asmx?op=GetLegislationPassedOriginalBodyAndNotIntroducedInOppositeBody"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call(
        "Legislation", "GetLegislationPassedOriginalBodyAndNotIntroducedInOppositeBody", argdict, keydict
    )
