from wa_leg_api.sessionlaw import *


def test_sessionlaw():
    biennium = "2019-20"
    bill_number = 1011
    bill_id = "HB 1011"
    # Session is the SessionCode (0=Regular Session, 1=1st Special Session, etc.).
    session = 0
    initiative_number = 940
    chapter_number = 10
    year = 2020

    get_session_law_by_bill(biennium, bill_number)
    get_bill_by_chapter_number(year, session, chapter_number)
    get_chapter_numbers_by_year(year)
    get_session_law_by_bill_id(biennium, bill_id)
    get_session_law_by_initiative_number(initiative_number)


if __name__ == "__main__":
    test_sessionlaw()
