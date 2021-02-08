from wa_leg_api.amendment import *


def test_get_amendments():
    """
    Make sure amendment function runs without crashing
    """
    get_amendments(2019)
