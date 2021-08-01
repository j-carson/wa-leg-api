from datetime import datetime  # noqa
from typing import Any, Dict

from dateutil import parser  # noqa

from wa_leg_api import waleg


def get_committee_meetings(begin_date: datetime, end_date: datetime) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeemeetingservice.asmx?op=GetCommitteeMeetings"""
    argdict: Dict[str, Any] = dict(beginDate=begin_date, endDate=end_date)
    keydict: Dict[str, Any] = {
        "agendaid": int,
        "zipcode": int,
        "date": parser.parse,
        "cancelled": lambda boolstr: (boolstr.lower() == "true"),
        "reviseddate": parser.parse,
    }
    return waleg.call("CommitteeMeeting", "GetCommitteeMeetings", argdict, keydict)


def get_revised_committee_meetings(changed_since_date: datetime) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeemeetingservice.asmx?op=GetRevisedCommitteeMeetings"""
    argdict: Dict[str, Any] = dict(changedSinceDate=changed_since_date)
    keydict: Dict[str, Any] = {
        "agendaid": int,
        "zipcode": int,
        "date": parser.parse,
        "cancelled": lambda boolstr: (boolstr.lower() == "true"),
        "reviseddate": parser.parse,
    }
    return waleg.call("CommitteeMeeting", "GetRevisedCommitteeMeetings", argdict, keydict)


def get_committee_meeting_items(agenda_id: int) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/committeemeetingservice.asmx?op=GetCommitteeMeetingItems"""
    argdict: Dict[str, Any] = dict(agendaId=agenda_id)
    keydict: Dict[str, Any] = {
        "agendaid": int,
        "order": int,
    }
    return waleg.call("CommitteeMeeting", "GetCommitteeMeetingItems", argdict, keydict)
