from wa_leg_api.rcwciteaffected import *


def test_rcwciteaffected():
    biennium = "2019-20"
    cite = "18"
    get_legislation_affecting_rcw(biennium, cite)
    get_legislation_affecting_rcw_cite(biennium, cite)


if __name__ == "__main__":
    test_rcwciteaffected()
