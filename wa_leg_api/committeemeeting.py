from typing import Dict
from datetime import datetime
import waleg

def get_committee_meetings(begin_date:datetime,end_date:datetime) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeMeeting", "GetCommitteeMeetings", argdict=dict(beginDate=begin_date,endDate=end_date))


def get_revised_committee_meetings(changed_since_date:datetime) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeMeeting", "GetRevisedCommitteeMeetings", argdict=dict(changedSinceDate=changed_since_date))


def get_committee_meeting_items(agenda_id:int) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("CommitteeMeeting", "GetCommitteeMeetingItems", argdict=dict(agendaId=agenda_id))


