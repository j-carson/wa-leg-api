from typing import Dict
from datetime import datetime  # noqa
from . import waleg


def get_documents_by_class(biennium: str, document_class: str, named_like: str) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(biennium=biennium, documentClass=document_class, namedLike=named_like)
    return waleg.call("LegislativeDocument", "GetDocumentsByClass", argdict=argdict)


def get_documents(biennium: str, named_like: str) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(biennium=biennium, namedLike=named_like)
    return waleg.call("LegislativeDocument", "GetDocuments", argdict=argdict)


def get_document_classes(biennium: str) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(biennium=biennium)
    return waleg.call("LegislativeDocument", "GetDocumentClasses", argdict=argdict)


def get_all_documents_by_class(biennium: str, document_class: str) -> Dict:
    """Auto-generated python interface to Washington Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    argdict = dict(biennium=biennium, documentClass=document_class)
    return waleg.call("LegislativeDocument", "GetAllDocumentsByClass", argdict=argdict)
