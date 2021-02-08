User-level API's
================

The user-level API consists of thin python stubs 
for each interface provided by the Washington legislature's web services.

To find the API you want:

* The module name is the XML service name, converted to lower case, without the word "Service" on the end. The module name is not converted to snake_case, so CommitteeMeetingService is in the committeemeeting module

* The function in the service is the XML API name, converted from camel case to snake case, so GetAmendments becomes get_amendments.

* The argment names are also converted to camel_case 
  within each wrapper function

The details of using each API are not documented
here, but a link to the page on the legistature website
with technical details and a test form is provided.


AmendmentService
----------------
.. automodule:: wa_leg_api.amendment
   :members: 
   
CommitteeService
---------
.. automodule:: wa_leg_api.committee
   :members: 
   
CommitteeMeetingService
----------------
.. automodule:: wa_leg_api.committeemeeting
   :members: 
   
LegislationService
------------------
.. automodule:: wa_leg_api.legislation
   :members: 
   
LegislativeDocumentService
--------------------------
.. automodule:: wa_leg_api.legislativedocument
   :members: 
   
   
RCWCiteAffectedService
----------------------
.. automodule:: wa_leg_api.rcwciteaffected
   :members: 
   
   
SessionLawService
-----------------
.. automodule:: wa_leg_api.sessionlaw
   :members: 
   
SponsorService
--------------
.. automodule:: wa_leg_api.sponsor
   :members: 
   
Exception
=========

If the leg.wa.gov server returns status other than 200, the
exception raised is WaLegApiException:

.. automodule:: wa_leg_api.exceptions
   :members: 


Low-level Modules
==================

These modules below are likely only of interest if you want to 
develop new features for this library.

make_stubs
----------
This module auto-generates source code for the user-level API's

.. automodule:: wa_leg_api.make_stubs
   make_stub_files

waleg
-----
This module is the backend for the stub functions

.. automodule:: wa_leg_api.waleg
   call