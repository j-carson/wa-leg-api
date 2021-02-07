from wa_leg_api.sponsor import *


def test_sponsor():
    biennium = '2019-20'

    x = get_sponsors(biennium)
    x = get_house_sponsors(biennium)
    x = get_senate_sponsors(biennium)
    x = get_requesters(biennium)

if __name__ == '__main__':
    test_sponsor()
