from typing import Dict
from datetime import datetime  # noqa
from dateutil import parser  # noqa
from wa_leg_api import waleg


def get_committee_meetings(begin_date: datetime, end_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeemeetingservice.asmx?op=GetCommitteeMeetings"""
    argdict = dict(beginDate=begin_date, endDate=end_date)
    keydict = {'agendaid':int,
'zipcode':int,
'date':parser.parse,
'cancelled':lambda boolstr: (boolstr.lower() == "true"),
'reviseddate':parser.parse,
}
    return waleg.call("CommitteeMeeting", "GetCommitteeMeetings", argdict, keydict)


def get_revised_committee_meetings(changed_since_date: datetime) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeemeetingservice.asmx?op=GetRevisedCommitteeMeetings"""
    argdict = dict(changedSinceDate=changed_since_date)
    keydict = {'agendaid':int,
'zipcode':int,
'date':parser.parse,
'cancelled':lambda boolstr: (boolstr.lower() == "true"),
'reviseddate':parser.parse,
}
    return waleg.call("CommitteeMeeting", "GetRevisedCommitteeMeetings", argdict, keydict)


def get_committee_meeting_items(agenda_id: int) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/committeemeetingservice.asmx?op=GetCommitteeMeetingItems"""
    argdict = dict(agendaId=agenda_id)
    keydict = {'agendaid':int,
'order':int,
}
    return waleg.call("CommitteeMeeting", "GetCommitteeMeetingItems", argdict, keydict)
