from typing import Dict
from datetime import datetime  # noqa
from . import waleg


def get_do_pass_by_committee(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetDoPassByCommittee"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("CommitteeAction", "GetDoPassByCommittee", argdict=argdict)


def get_do_pass_with_amendments_by_committee(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetDoPassWithAmendmentsByCommittee"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("CommitteeAction", "GetDoPassWithAmendmentsByCommittee", argdict=argdict)


def get_do_pass_with_amendments_to_sub_by_committee(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetDoPassWithAmendmentsToSubByCommittee"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("CommitteeAction", "GetDoPassWithAmendmentsToSubByCommittee", argdict=argdict)


def get_in_committee(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetInCommittee"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("CommitteeAction", "GetInCommittee", argdict=argdict)


def get_majority_report_by_committee(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetMajorityReportByCommittee"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("CommitteeAction", "GetMajorityReportByCommittee", argdict=argdict)


def get_minority_report_by_committee(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetMinorityReportByCommittee"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("CommitteeAction", "GetMinorityReportByCommittee", argdict=argdict)


def get_re_referral_by_committee(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetReReferralByCommittee"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("CommitteeAction", "GetReReferralByCommittee", argdict=argdict)


def get_referred_to_another_committee_by_committee(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetReferredToAnotherCommitteeByCommittee"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("CommitteeAction", "GetReferredToAnotherCommitteeByCommittee", argdict=argdict)


def get_referred_to_committee(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetReferredToCommittee"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("CommitteeAction", "GetReferredToCommittee", argdict=argdict)


def get_committee_referrals_by_committee(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetCommitteeReferralsByCommittee"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("CommitteeAction", "GetCommitteeReferralsByCommittee", argdict=argdict)


def get_committee_referrals_by_bill(biennium: str, bill_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetCommitteeReferralsByBill"""
    argdict = dict(biennium=biennium, billNumber=bill_number)
    return waleg.call("CommitteeAction", "GetCommitteeReferralsByBill", argdict=argdict)


def get_removed_from_committee(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetRemovedFromCommittee"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("CommitteeAction", "GetRemovedFromCommittee", argdict=argdict)


def get_do_pass_substitute_by_committee(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetDoPassSubstituteByCommittee"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("CommitteeAction", "GetDoPassSubstituteByCommittee", argdict=argdict)


def get_without_recommendation_by_committee(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetWithoutRecommendationByCommittee"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("CommitteeAction", "GetWithoutRecommendationByCommittee", argdict=argdict)


def get_committee_executive_actions_by_bill(biennium: str, bill_number: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetCommitteeExecutiveActionsByBill"""
    argdict = dict(biennium=biennium, billNumber=bill_number)
    return waleg.call("CommitteeAction", "GetCommitteeExecutiveActionsByBill", argdict=argdict)


def get_legislation_reported_out_of_committee(committee_name: str, agency: str, begin_date: datetime, end_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetLegislationReportedOutOfCommittee"""
    argdict = dict(committeeName=committee_name, agency=agency, beginDate=begin_date, endDate=end_date)
    return waleg.call("CommitteeAction", "GetLegislationReportedOutOfCommittee", argdict=argdict)


def get_legislation_scheduled_hearings_by_committee(biennium: str, agency: str, committee_name: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeeactionservice.asmx?op=GetLegislationScheduledHearingsByCommittee"""
    argdict = dict(biennium=biennium, agency=agency, committeeName=committee_name)
    return waleg.call("CommitteeAction", "GetLegislationScheduledHearingsByCommittee", argdict=argdict)
