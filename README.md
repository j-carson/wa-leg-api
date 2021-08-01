# wa-leg-api

Python wrapper library around Washington State Legislature web services API

# Installation

```bash
pip install wa-leg-api
```

Dependecies are:
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [requests](https://pypi.org/project/requests/)
- [python-dateutil](https://pypi.org/project/python-dateutil/)

# Basic Usage

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

# Full documentation

Please visit  [https://wa-leg-api.readthedocs.io](https://wa-leg-api.readthedocs.io)
