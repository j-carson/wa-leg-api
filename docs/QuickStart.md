# Quick Start

## Installation

```bash
git clone https://github.com/j-carson/wa-leg-api.git
cd wa-leg-api
pip install . 
```

Dependecies are:
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [requests](https://pypi.org/project/requests/)
- [python-dateutil](https://pypi.org/project/python-dateutil/)

## Usage

The stub functions are in modules named after each service in all lower case.
The function names are the request type changed from CamelCase to snake_case.

Example: If you want to call the function GetAmendments from the AmendmentService, do:

```python
from wa_leg_api.amendment import get_amendments
result = get_amendments(2021)
```

All stubs return dicts.

For more information about the Washington State Legislature web services 
available visit [wslwebservices.leg.wa.gov](http://wslwebservices.leg.wa.gov/)

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

Exceptions thrown directly by the requests package are not re-wrapped.

## To dos

The input arg names are in python-standard camelcase, but the return keys 
in the dictionary are all lower case. Sorry for the inconsistency.

The documentation should really include the dict structure returned by each 
function, rather than pointing to the leg.wa.gov documentation. 

The function GetLegislativeBillListFeatureData in the LegislationService
is not yet implemented.

## Developers

[The source is here.](https://https://github.com/j-carson/wa-leg-api/)

In addition to the required packages to use the library, the lxml package is 
needed to regenerate the stubs. The function that makes the stubs is 
called make_stubs.py  

The tests are compatible with pytest.  The documentation is built with sphinx.
There is an initial setup to check the source with mypy as well. TODO: need 
to add library stubs.
