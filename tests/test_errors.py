from wa_leg_api.committee import get_active_committee_members
from wa_leg_api.exceptions import WaLegApiException


def test_errors():
    try:
        get_active_committee_members("Senate", "Not a real committee")
    except WaLegApiException as e:
        print("http_error_num =", e.http_error_num)
        print("http_error_text =", e.http_error_text)
        print("http_text =", e.http_text)
        print("args_sent =", e.args_sent)
    else:
        assert False, "Should have raised exception here"


if __name__ == "__main__":
    test_errors()
