User-level API's
================

The user-level API consists of thin python stubs 
for each interface provided by the Washington legislature's web services.

* The module name is the XML service name, converted to lower case, without the word "Service" on the end. The module name is not converted to snake_case, so CommitteeMeetingService is in the committeemeeting module

* The function in the service is the XML API name, converted from camel case to snake case, so GetAmendments becomes get_amendments.

* The argment names are also converted to camel_case 
  within each wrapper function

.. note::  
   The details of using each API are not documented
   here. See the link to the page on the legistature website
   with technical details and a test form.
   

AmendmentService
----------------

.. automodule:: amendment
   :members: 
   
CommitteeService
----------------

.. automodule:: committee
   :members: 
   
CommitteeMeetingService
-----------------------

.. automodule:: committeemeeting
   :members: 
   
LegislationService
------------------

The wrapper function for GetLegislativeBillListFeatureData in the LegislationService
is not yet implemented.

.. automodule:: legislation
   :members: 
   
LegislativeDocumentService
--------------------------

.. automodule:: legislativedocument
   :members: 
   
   
RCWCiteAffectedService
----------------------

.. automodule:: rcwciteaffected
   :members: 
   
   
SessionLawService
-----------------

.. automodule:: sessionlaw
   :members: 
   
SponsorService
--------------

.. automodule:: sponsor
   :members: 
