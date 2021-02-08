from wa_leg_api.sponsor import *


def test_sponsor():
    biennium = "2019-20"

    get_sponsors(biennium)
    get_house_sponsors(biennium)
    get_senate_sponsors(biennium)
    get_requesters(biennium)


if __name__ == "__main__":
    test_sponsor()
