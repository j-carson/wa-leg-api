from typing import Dict
from datetime import datetime  # noqa
from dateutil import parser  # noqa
from wa_leg_api import waleg


def get_sponsors(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/sponsorservice.asmx?op=GetSponsors"""
    argdict = dict(biennium=biennium)
    keydict = {'district':int,
}
    return waleg.call("Sponsor", "GetSponsors", argdict, keydict)


def get_house_sponsors(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/sponsorservice.asmx?op=GetHouseSponsors"""
    argdict = dict(biennium=biennium)
    keydict = {'district':int,
}
    return waleg.call("Sponsor", "GetHouseSponsors", argdict, keydict)


def get_senate_sponsors(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/sponsorservice.asmx?op=GetSenateSponsors"""
    argdict = dict(biennium=biennium)
    keydict = {'district':int,
}
    return waleg.call("Sponsor", "GetSenateSponsors", argdict, keydict)


def get_requesters(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/sponsorservice.asmx?op=GetRequesters"""
    argdict = dict(biennium=biennium)
    keydict = {'id':int,
}
    return waleg.call("Sponsor", "GetRequesters", argdict, keydict)
