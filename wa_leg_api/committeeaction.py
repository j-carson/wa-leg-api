from typing import Dict
from datetime import datetime
from . import waleg

def get_do_pass_by_committee(biennium:str,agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetDoPassByCommittee", argdict=dict(biennium=biennium,agency=agency,committeeName=committee_name))


def get_do_pass_with_amendments_by_committee(biennium:str,agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetDoPassWithAmendmentsByCommittee", argdict=dict(biennium=biennium,agency=agency,committeeName=committee_name))


def get_do_pass_with_amendments_to_sub_by_committee(biennium:str,agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetDoPassWithAmendmentsToSubByCommittee", argdict=dict(biennium=biennium,agency=agency,committeeName=committee_name))


def get_in_committee(biennium:str,agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetInCommittee", argdict=dict(biennium=biennium,agency=agency,committeeName=committee_name))


def get_majority_report_by_committee(biennium:str,agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetMajorityReportByCommittee", argdict=dict(biennium=biennium,agency=agency,committeeName=committee_name))


def get_minority_report_by_committee(biennium:str,agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetMinorityReportByCommittee", argdict=dict(biennium=biennium,agency=agency,committeeName=committee_name))


def get_re_referral_by_committee(biennium:str,agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetReReferralByCommittee", argdict=dict(biennium=biennium,agency=agency,committeeName=committee_name))


def get_referred_to_another_committee_by_committee(biennium:str,agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetReferredToAnotherCommitteeByCommittee", argdict=dict(biennium=biennium,agency=agency,committeeName=committee_name))


def get_referred_to_committee(biennium:str,agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetReferredToCommittee", argdict=dict(biennium=biennium,agency=agency,committeeName=committee_name))


def get_committee_referrals_by_committee(biennium:str,agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetCommitteeReferralsByCommittee", argdict=dict(biennium=biennium,agency=agency,committeeName=committee_name))


def get_committee_referrals_by_bill(biennium:str,bill_number:int) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetCommitteeReferralsByBill", argdict=dict(biennium=biennium,billNumber=bill_number))


def get_removed_from_committee(biennium:str,agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetRemovedFromCommittee", argdict=dict(biennium=biennium,agency=agency,committeeName=committee_name))


def get_do_pass_substitute_by_committee(biennium:str,agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetDoPassSubstituteByCommittee", argdict=dict(biennium=biennium,agency=agency,committeeName=committee_name))


def get_without_recommendation_by_committee(biennium:str,agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetWithoutRecommendationByCommittee", argdict=dict(biennium=biennium,agency=agency,committeeName=committee_name))


def get_committee_executive_actions_by_bill(biennium:str,bill_number:int) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetCommitteeExecutiveActionsByBill", argdict=dict(biennium=biennium,billNumber=bill_number))


def get_legislation_reported_out_of_committee(committee_name:str,agency:str,begin_date:datetime,end_date:datetime) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetLegislationReportedOutOfCommittee", argdict=dict(committeeName=committee_name,agency=agency,beginDate=begin_date,endDate=end_date))


def get_legislation_scheduled_hearings_by_committee(biennium:str,agency:str,committee_name:str) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeAction", "GetLegislationScheduledHearingsByCommittee", argdict=dict(biennium=biennium,agency=agency,committeeName=committee_name))


