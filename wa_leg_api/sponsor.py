from datetime import datetime  # noqa
from typing import Any, Dict

from dateutil import parser  # noqa

from wa_leg_api import waleg


def get_sponsors(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/sponsorservice.asmx?op=GetSponsors"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "district": int,
    }
    return waleg.call("Sponsor", "GetSponsors", argdict, keydict)


def get_house_sponsors(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/sponsorservice.asmx?op=GetHouseSponsors"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "district": int,
    }
    return waleg.call("Sponsor", "GetHouseSponsors", argdict, keydict)


def get_senate_sponsors(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/sponsorservice.asmx?op=GetSenateSponsors"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "district": int,
    }
    return waleg.call("Sponsor", "GetSenateSponsors", argdict, keydict)


def get_requesters(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/sponsorservice.asmx?op=GetRequesters"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {
        "id": int,
    }
    return waleg.call("Sponsor", "GetRequesters", argdict, keydict)
