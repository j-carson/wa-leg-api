from datetime import datetime

from wa_leg_api.committeemeeting import *


def test_committeemeeting():
    begin_date = datetime(2019, 1, 10)
    end_date = datetime(2019, 2, 10)

    meetings = get_committee_meetings(begin_date, end_date)
    meeting = meetings["arrayofcommitteemeeting"][0]
    agenda_id = int(meeting["agendaid"])
    get_revised_committee_meetings(end_date)
    get_committee_meeting_items(agenda_id)
