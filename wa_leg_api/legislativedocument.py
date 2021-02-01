from typing import Dict
from datetime import datetime
from . import waleg

def get_documents_by_class(biennium:str=None,document_class:str=None,named_like:str=None) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("LegislativeDocument", "GetDocumentsByClass", argdict=dict(biennium=biennium,documentClass=document_class,namedLike=named_like))


def get_documents(biennium:str=None,named_like:str=None) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("LegislativeDocument", "GetDocuments", argdict=dict(biennium=biennium,namedLike=named_like))


def get_document_classes(biennium:str=None) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("LegislativeDocument", "GetDocumentClasses", argdict=dict(biennium=biennium))


def get_all_documents_by_class(biennium:str=None,document_class:str=None) -> Dict:
    """Auto-generated python interface to Washington State Legislature Web Services
    See http://wslwebservices.leg.wa.gov/lwsDetails.htm"""
    return waleg.call("LegislativeDocument", "GetAllDocumentsByClass", argdict=dict(biennium=biennium,documentClass=document_class))


