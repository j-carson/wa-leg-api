from datetime import datetime  # noqa
from typing import Any, Dict

from dateutil import parser  # noqa

from wa_leg_api import waleg


def get_do_pass_by_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetDoPassByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetDoPassByCommittee", argdict, keydict)


def get_do_pass_with_amendments_by_committee(
    biennium: str, agency: str, committee_name: str
) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetDoPassWithAmendmentsByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetDoPassWithAmendmentsByCommittee", argdict, keydict)


def get_do_pass_with_amendments_to_sub_by_committee(
    biennium: str, agency: str, committee_name: str
) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetDoPassWithAmendmentsToSubByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetDoPassWithAmendmentsToSubByCommittee", argdict, keydict)


def get_in_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetInCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetInCommittee", argdict, keydict)


def get_majority_report_by_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetMajorityReportByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetMajorityReportByCommittee", argdict, keydict)


def get_minority_report_by_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetMinorityReportByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetMinorityReportByCommittee", argdict, keydict)


def get_re_referral_by_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetReReferralByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetReReferralByCommittee", argdict, keydict)


def get_referred_to_another_committee_by_committee(
    biennium: str, agency: str, committee_name: str
) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetReferredToAnotherCommitteeByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetReferredToAnotherCommitteeByCommittee", argdict, keydict)


def get_referred_to_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetReferredToCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetReferredToCommittee", argdict, keydict)


def get_committee_referrals_by_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetCommitteeReferralsByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
        "referreddate": parser.parse,
    }
    return waleg.call("CommitteeAction", "GetCommitteeReferralsByCommittee", argdict, keydict)


def get_committee_referrals_by_bill(biennium: str, bill_number: int) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetCommitteeReferralsByBill"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
        "referreddate": parser.parse,
    }
    return waleg.call("CommitteeAction", "GetCommitteeReferralsByBill", argdict, keydict)


def get_removed_from_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetRemovedFromCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetRemovedFromCommittee", argdict, keydict)


def get_do_pass_substitute_by_committee(biennium: str, agency: str, committee_name: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetDoPassSubstituteByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetDoPassSubstituteByCommittee", argdict, keydict)


def get_without_recommendation_by_committee(
    biennium: str, agency: str, committee_name: str
) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetWithoutRecommendationByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetWithoutRecommendationByCommittee", argdict, keydict)


def get_committee_executive_actions_by_bill(biennium: str, bill_number: int) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetCommitteeExecutiveActionsByBill"""
    argdict: Dict[str, Any] = dict(biennium=biennium, billNumber=bill_number)
    keydict: Dict[str, Any] = {
        "agendaid": int,
        "hearingdate": parser.parse,
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
        "memberid": int,
        "positionsort": int,
    }
    return waleg.call("CommitteeAction", "GetCommitteeExecutiveActionsByBill", argdict, keydict)


def get_legislation_reported_out_of_committee(
    committee_name: str, agency: str, begin_date: datetime, end_date: datetime
) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetLegislationReportedOutOfCommittee"""
    argdict: Dict[str, Any] = dict(
        committeeName=committee_name, agency=agency, beginDate=begin_date, endDate=end_date
    )
    keydict: Dict[str, Any] = {
        "billnumber": int,
        "substituteversion": int,
        "engrossedversion": int,
        "active": lambda boolstr: (boolstr.lower() == "true"),
    }
    return waleg.call("CommitteeAction", "GetLegislationReportedOutOfCommittee", argdict, keydict)


def get_legislation_scheduled_hearings_by_committee(
    biennium: str, agency: str, committee_name: str
) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetLegislationScheduledHearingsByCommittee"""
    argdict: Dict[str, Any] = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    keydict: Dict[str, Any] = {
        "legislationnumber": int,
        "meetingtime": parser.parse,
    }
    return waleg.call("CommitteeAction", "GetLegislationScheduledHearingsByCommittee", argdict, keydict)
