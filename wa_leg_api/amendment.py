from typing import Dict
from datetime import datetime
import waleg

def get_amendments(year:int) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("Amendment", "GetAmendments", argdict=dict(year=year))


