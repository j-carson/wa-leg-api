# wa-leg-api

Python wrapper library around Washington State Legislature web services API

# Quick Start

The stub functions are in modules named after each service in all lower case.
The function names are the request type changed from CamelCase to snake_case.

Example: If you want to call the function GetAmendments from the AmendmentService, do:

```python
from wa_leg_api.amendment import get_amendments
result = get_amendments(2021)
```

All stubs return dicts.

For more information about the Washington State Legislature web services 
available visit [leg.wa.gov](http://wslwebservices.leg.wa.gov/)

# To dos

The stub functions accept arguments of the correct type, but applying type 
information for the return values is not yet implemented, so every field 
is returned as a string.

# Developers

In addition to the required packages to use the library, the lxml package is 
needed to regenerate the stubs. The function that makes the stubs is 
called make_stubs.py 
