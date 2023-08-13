from datetime import datetime  # noqa
from typing import Any, Dict

from dateutil import parser  # noqa

from wa_leg_api import waleg


def get_do_pass_by_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills with status do pass by committee.<br/>Exception thrown for invalid agency or committee name or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.<br/>CommitteeName is the Name Property returned in GetActiveHouseCommittees/GetActiveSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetDoPassByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetDoPassByCommittee", argdict, keydict)


def get_do_pass_with_amendments_by_committee(
    biennium: str, agency: str, committee_name: str
) -> Dict[str, Any]:
    """Returns summary legislation information on all bills with status do pass with amendments by committee.<br/>Exception thrown for invalid agency or committee name or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.<br/>CommitteeName is the Name Property returned in GetActiveHouseCommittees/GetActiveSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetDoPassWithAmendmentsByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetDoPassWithAmendmentsByCommittee", argdict, keydict)


def get_do_pass_with_amendments_to_sub_by_committee(
    biennium: str, agency: str, committee_name: str
) -> Dict[str, Any]:
    """Returns summary legislation information on all bills with status do pass with amendments to sub by committee.<br/>Exception thrown for invalid agency or committee name or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.<br/>CommitteeName is the Name Property returned in GetActiveHouseCommittees/GetActiveSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetDoPassWithAmendmentsToSubByCommittee
    """
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetDoPassWithAmendmentsToSubByCommittee", argdict, keydict)


def get_in_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills with status in committee.<br/>Exception thrown for invalid agency or committee name or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.<br/>CommitteeName is the Name Property returned in GetActiveHouseCommittees/GetActiveSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetInCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetInCommittee", argdict, keydict)


def get_majority_report_by_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills with status majority report by committee.<br/>Exception thrown for invalid agency or committee name or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.<br/>CommitteeName is the Name Property returned in GetActiveHouseCommittees/GetActiveSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetMajorityReportByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetMajorityReportByCommittee", argdict, keydict)


def get_minority_report_by_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills with status minority report by committee.<br/>Exception thrown for invalid agency or committee name or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.<br/>CommitteeName is the Name Property returned in GetActiveHouseCommittees/GetActiveSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetMinorityReportByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetMinorityReportByCommittee", argdict, keydict)


def get_re_referral_by_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills with status re-referral by committee.<br/>Exception thrown for invalid agency or committee name or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.<br/>CommitteeName is the Name Property returned in GetActiveHouseCommittees/GetActiveSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetReReferralByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetReReferralByCommittee", argdict, keydict)


def get_referred_to_another_committee_by_committee(
    biennium: str, agency: str, committee_name: str
) -> Dict[str, Any]:
    """Returns summary legislation information on all bills with status referred to another committee by committee.<br/>Exception thrown for invalid agency or committee name or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.<br/>CommitteeName is the Name Property returned in GetActiveHouseCommittees/GetActiveSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetReferredToAnotherCommitteeByCommittee
    """
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetReferredToAnotherCommitteeByCommittee", argdict, keydict)


def get_referred_to_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills with status referred to committee.<br/>Exception thrown for invalid agency or committee name or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.<br/>CommitteeName is the Name Property returned in GetActiveHouseCommittees/GetActiveSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetReferredToCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetReferredToCommittee", argdict, keydict)


def get_committee_referrals_by_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills that have been referred to the committee by committee.<br/>Exception thrown for invalid agency or committee name or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.<br/>CommitteeName is the Name Property returned in GetActiveHouseCommittees/GetActiveSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetCommitteeReferralsByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
        "referred_date": parser.parse,
    }
    return waleg.call("CommitteeAction", "GetCommitteeReferralsByCommittee", argdict, keydict)


def get_committee_referrals_by_bill(biennium: str, bill_number: int) -> Dict[str, Any]:
    """Returns summary legislation information on all bills that have been referred to the committee by bill.<br/>Exception thrown for invalid biennium.<br/>Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetCommitteeReferralsByBill"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
        "referred_date": parser.parse,
    }
    return waleg.call("CommitteeAction", "GetCommitteeReferralsByBill", argdict, keydict)


def get_removed_from_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills with status removed by committee.<br/>Exception thrown for invalid agency or committee name or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.<br/>CommitteeName is the Name Property returned in GetActiveHouseCommittees/GetActiveSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetRemovedFromCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetRemovedFromCommittee", argdict, keydict)


def get_do_pass_substitute_by_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """Returns summary legislation information on all bills with status substitute do pass by committee.<br/>Exception thrown for invalid agency or committee name or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.<br/>CommitteeName is the Name Property returned in GetActiveHouseCommittees/GetActiveSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetDoPassSubstituteByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetDoPassSubstituteByCommittee", argdict, keydict)


def get_without_recommendation_by_committee(
    biennium: str, agency: str, committee_name: str
) -> Dict[str, Any]:
    """Returns summary legislation information on all bills with status without recommendation by committee.<br/>Exception thrown for invalid agency or committee name or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.<br/>CommitteeName is the Name Property returned in GetActiveHouseCommittees/GetActiveSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetWithoutRecommendationByCommittee
    """
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetWithoutRecommendationByCommittee", argdict, keydict)


def get_committee_executive_actions_by_bill(biennium: str, bill_number: int) -> Dict[str, Any]:
    """Returns executive committee executive actions by bill.<br/>Exception thrown for invalid biennium.<br/>Expects biennium to be in the format: 2005-06

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetCommitteeExecutiveActionsByBill"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "agenda_id": int,
        "hearing_date": parser.parse,
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
        "member_id": int,
        "position_sort": int,
    }
    return waleg.call("CommitteeAction", "GetCommitteeExecutiveActionsByBill", argdict, keydict)


def get_legislation_reported_out_of_committee(
    committee_name: str, agency: str, begin_date: datetime, end_date: datetime
) -> Dict[str, Any]:
    """Returns summary legislation information on all bills that were reported out of the given committee between the begin and end date.

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetLegislationReportedOutOfCommittee
    """
    argdict: Dict[str, Any] = dict(
        committeeName=committee_name, agency=agency, beginDate=begin_date, endDate=end_date
    )
    keydict: Dict[str, Any] = {
        "bill_number": int,
        "substitute_version": int,
        "engrossed_version": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetLegislationReportedOutOfCommittee", argdict, keydict)


def get_legislation_scheduled_hearings_by_committee(
    biennium: str, agency: str, committee_name: str
) -> Dict[str, Any]:
    """Returns bills that have had a hearing scheduled in the committee.<br/>Exception thrown for invalid agency or committee name or biennium.<br/>Expects biennium to be in the format: 2005-06<br/>Agency should be House or Senate.<br/>CommitteeName is the Name Property returned in GetActiveHouseCommittees/GetActiveSenateCommittees.

    See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetLegislationScheduledHearingsByCommittee
    """
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "legislation_number": int,
        "meeting_time": parser.parse,
    }
    return waleg.call("CommitteeAction", "GetLegislationScheduledHearingsByCommittee", argdict, keydict)
