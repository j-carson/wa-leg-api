from typing import Dict
from datetime import datetime  # noqa
from wa_leg_api import waleg


def get_documents_by_class(biennium: str, document_class: str, named_like: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetDocumentsByClass"""
    argdict = dict(biennium=biennium, documentClass=document_class, namedLike=named_like)
    return waleg.call("LegislativeDocument", "GetDocumentsByClass", argdict)


def get_documents(biennium: str, named_like: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetDocuments"""
    argdict = dict(biennium=biennium, namedLike=named_like)
    return waleg.call("LegislativeDocument", "GetDocuments", argdict)


def get_document_classes(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetDocumentClasses"""
    argdict = dict(biennium=biennium)
    return waleg.call("LegislativeDocument", "GetDocumentClasses", argdict)


def get_all_documents_by_class(biennium: str, document_class: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetAllDocumentsByClass"""
    argdict = dict(biennium=biennium, documentClass=document_class)
    return waleg.call("LegislativeDocument", "GetAllDocumentsByClass", argdict)
