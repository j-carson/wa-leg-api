from typing import Dict
from datetime import datetime  # noqa
from dateutil import parser  # noqa
from wa_leg_api import waleg


def get_legislation_affecting_rcw_cite(biennium: str, rcw_cite: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/rcwciteaffectedservice.asmx?op=GetLegislationAffectingRcwCite"""
    argdict = dict(biennium=biennium, rcwCite=rcw_cite)
    keydict = {'billnumber':int,
'substituteversion':int,
'engrossedversion':int,
'active':lambda boolstr: (boolstr.lower() == "true"),
}
    return waleg.call("RcwCiteAffected", "GetLegislationAffectingRcwCite", argdict, keydict)


def get_legislation_affecting_rcw(biennium: str, rcw_cite: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/rcwciteaffectedservice.asmx?op=GetLegislationAffectingRcw"""
    argdict = dict(biennium=biennium, rcwCite=rcw_cite)
    keydict = {'billnumber':int,
'substituteversion':int,
'engrossedversion':int,
'active':lambda boolstr: (boolstr.lower() == "true"),
}
    return waleg.call("RcwCiteAffected", "GetLegislationAffectingRcw", argdict, keydict)
