from wa_leg_api.committee import *

def test_committee():
    """ Make sure that committee module functions run without crashing
    """
    biennium = '2019-20'
    agencies = ['House', 'Senate']

    get_committees(biennium)
    get_house_committees(biennium)
    get_senate_committees(biennium)
    get_active_committees()
    get_active_house_committees()
    get_active_senate_committees()

    for agency in agencies:
        get_committee_members(biennium, agency, 'Transportation')
        get_active_committee_members(agency, 'Transportation')


