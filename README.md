# wa-leg-api

Python wrapper library around Washington State Legislature web services API

# Installation

```bash
git clone https://github.com/j-carson/wa-leg-api.git
cd wa-leg-api
pip install . 
```

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

## Exceptions

There is one exception defined by this library:

```python
try:
    result = get_amendments(2100)  # an invalid year!
except WaLegApiException as e:
    print(e.http_error)      # HTTP Error code
    print(e.http_error_text) # HTTP Error code as text
    print(e.http_text)       # Additional text returned from leg.wa.gov 
    print(e.args_sent)       # Record of arguments sent with request
```

Sample output:

```
500
Internal Server Error
System.Web.Services.Protocols.SoapException: Invalid Input. ---> System.ArgumentException: You have not submitted a valid year.  Please enter year in the following format:  YYYY.  Information is only available back to 1991.
Parameter name: Year
   --- End of inner exception stack trace ---
   at WslWebServices.AmendmentService.GetAmendments(Int32 year)

{'year': 2100}
```

# To dos

The stub functions accept arguments of the correct type, but applying type 
information for the return values is not yet implemented, so every field 
is returned as a string.

# Developers

In addition to the required packages to use the library, the lxml package is 
needed to regenerate the stubs. The function that makes the stubs is 
called make_stubs.py 
