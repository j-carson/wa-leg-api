from typing import Dict
from datetime import datetime  # noqa
from wa_leg_api import waleg


def get_committee_meetings(begin_date: datetime, end_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeemeetingservice.asmx?op=GetCommitteeMeetings"""
    argdict = dict(beginDate=begin_date, endDate=end_date)
    return waleg.call("CommitteeMeeting", "GetCommitteeMeetings", argdict)


def get_revised_committee_meetings(changed_since_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeemeetingservice.asmx?op=GetRevisedCommitteeMeetings"""
    argdict = dict(changedSinceDate=changed_since_date)
    return waleg.call("CommitteeMeeting", "GetRevisedCommitteeMeetings", argdict)


def get_committee_meeting_items(agenda_id: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeemeetingservice.asmx?op=GetCommitteeMeetingItems"""
    argdict = dict(agendaId=agenda_id)
    return waleg.call("CommitteeMeeting", "GetCommitteeMeetingItems", argdict)
