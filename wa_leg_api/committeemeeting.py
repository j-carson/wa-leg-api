from typing import Dict
from datetime import datetime  # noqa
from . import waleg


def get_committee_meetings(begin_date: datetime, end_date: datetime) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(beginDate=begin_date, endDate=end_date)
    return waleg.call("CommitteeMeeting", "GetCommitteeMeetings", argdict=argdict)


def get_revised_committee_meetings(changed_since_date: datetime) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(changedSinceDate=changed_since_date)
    return waleg.call("CommitteeMeeting", "GetRevisedCommitteeMeetings", argdict=argdict)


def get_committee_meeting_items(agenda_id: int) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(agendaId=agenda_id)
    return waleg.call("CommitteeMeeting", "GetCommitteeMeetingItems", argdict=argdict)
