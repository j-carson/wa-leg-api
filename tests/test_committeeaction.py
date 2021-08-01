from datetime import datetime

from wa_leg_api.committeeaction import *


def test_committeeaction():
    biennium = "2019-20"
    agencies = ["House", "Senate"]
    committee_name = "Transportation"
    bill_number = dict(House=1010, Senate=5010)
    begin_date = datetime(2019, 1, 24)
    end_date = datetime(2019, 2, 10)

    for agency in agencies:
        get_do_pass_by_committee(biennium, agency, committee_name)
        get_do_pass_with_amendments_by_committee(biennium, agency, committee_name)
        get_do_pass_with_amendments_to_sub_by_committee(biennium, agency, committee_name)
        get_in_committee(biennium, agency, committee_name)
        get_majority_report_by_committee(biennium, agency, committee_name)
        get_minority_report_by_committee(biennium, agency, committee_name)
        get_re_referral_by_committee(biennium, agency, committee_name)
        get_referred_to_another_committee_by_committee(biennium, agency, committee_name)
        get_referred_to_committee(biennium, agency, committee_name)
        get_committee_referrals_by_committee(biennium, agency, committee_name)
        get_removed_from_committee(biennium, agency, committee_name)
        get_do_pass_substitute_by_committee(biennium, agency, committee_name)
        get_without_recommendation_by_committee(biennium, agency, committee_name)

        get_committee_referrals_by_bill(biennium, bill_number[agency])
        get_committee_executive_actions_by_bill(biennium, bill_number[agency])

        get_legislation_reported_out_of_committee(committee_name, agency, begin_date, end_date)

        get_legislation_scheduled_hearings_by_committee(biennium, agency, committee_name)


if __name__ == "__main__":
    test_committeeaction()
