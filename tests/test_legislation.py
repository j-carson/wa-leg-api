from datetime import datetime

from wa_leg_api.legislation import *


def test_legislation():
    """Make sure that the legislation module functions run without crashing"""
    biennium = "2019-20"
    year = 2019
    bill_number = 1750
    bill_id = "HB 1750"
    begin_date = datetime(2019, 1, 1)
    end_date = datetime(2019, 3, 1)

    # Doesn't acutally return any laws
    # Need docs to what agency_id and leg_type_id should be???
    get_total_legislation_introduced_by_date_range(begin_date, end_date, 0, 0, True)

    # only supposed to return non-empty results
    # when prefiled bills exist, just before session starts
    get_prefiled_legislation()
    get_pre_filed_legislation_info()

    # bug: results are not unpacked correctly!
    # get_legislative_bill_list_feature_data()

    get_legislation_types()
    get_amendments_for_year(year, bill_number)
    get_amendments_for_biennium(biennium, bill_number)
    get_hearings(biennium, bill_number)
    get_rcw_cites_affected(biennium, bill_id)
    get_session_law_chapter(biennium, bill_id)
    get_sponsors(biennium, bill_id)
    get_roll_calls(biennium, bill_number)

    get_current_status(biennium, bill_number)
    get_legislation(biennium, bill_number)
    get_legislation_by_request_number(biennium, "H-0210.1")
    get_legislation_introduced_since(datetime(2021, 2, 1))
    get_legislative_status_changes_by_bill_number(biennium, bill_number, begin_date, end_date)
    get_legislative_status_changes_by_bill_id(biennium, bill_id, begin_date, end_date)
    get_legislative_status_changes_by_date_range(biennium, begin_date, end_date)
    get_legislation_by_year(2019)
    get_legislation_info_introduced_since(datetime(2021, 2, 1))
    get_house_legislation_passed_house(biennium)
    get_house_legislation_passed_senate(biennium)
    get_senate_legislation_passed_house(biennium)
    get_senate_legislation_passed_senate(biennium)
    get_legislation_passed_legislature(biennium)
    get_legislation_passed_house(biennium)
    get_legislation_passed_senate(biennium)
    get_legislation_governor_signed(biennium, "House")
    get_legislation_governor_veto(biennium, "House")
    get_legislation_governor_partial_veto(biennium, "House")
    get_published_enrolled_legislation(biennium)
    get_legislation_passed_legislature_within_time_frame(begin_date, end_date)
    get_legislation_passed_house_within_time_frame(begin_date, end_date)
    get_legislation_passed_senate_within_time_frame(begin_date, end_date)
    get_legislation_not_yet_introduced_in_house_of_origin(biennium)
    get_legislation_passed_original_body_and_not_introduced_in_opposite_body(biennium)


if __name__ == "__main__":
    test_legislation()
