from typing import Dict
from datetime import datetime  # noqa
from wa_leg_api import waleg


def get_sponsors(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/sponsorservice.asmx?op=GetSponsors"""
    argdict = dict(biennium=biennium)
    return waleg.call("Sponsor", "GetSponsors", argdict)


def get_house_sponsors(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/sponsorservice.asmx?op=GetHouseSponsors"""
    argdict = dict(biennium=biennium)
    return waleg.call("Sponsor", "GetHouseSponsors", argdict)


def get_senate_sponsors(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/sponsorservice.asmx?op=GetSenateSponsors"""
    argdict = dict(biennium=biennium)
    return waleg.call("Sponsor", "GetSenateSponsors", argdict)


def get_requesters(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/sponsorservice.asmx?op=GetRequesters"""
    argdict = dict(biennium=biennium)
    return waleg.call("Sponsor", "GetRequesters", argdict)
