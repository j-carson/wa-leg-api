from datetime import datetime  # noqa
from typing import Any, Dict

from dateutil import parser  # noqa

from wa_leg_api import waleg


def get_documents_by_class(biennium: str, document_class: str, named_like: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetDocumentsByClass"""
    argdict: Dict[str, Any] = dict(biennium=biennium, documentClass=document_class, namedLike=named_like)
    keydict: Dict[str, Any] = {
        "htmcreatedate": parser.parse,
        "htmlastmodifieddate": parser.parse,
        "pdfcreatedate": parser.parse,
        "pdflastmodifieddate": parser.parse,
    }
    return waleg.call("LegislativeDocument", "GetDocumentsByClass", argdict, keydict)


def get_documents(biennium: str, named_like: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetDocuments"""
    argdict: Dict[str, Any] = dict(biennium=biennium, namedLike=named_like)
    keydict: Dict[str, Any] = {
        "htmcreatedate": parser.parse,
        "htmlastmodifieddate": parser.parse,
        "pdfcreatedate": parser.parse,
        "pdflastmodifieddate": parser.parse,
    }
    return waleg.call("LegislativeDocument", "GetDocuments", argdict, keydict)


def get_document_classes(biennium: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetDocumentClasses"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {}
    return waleg.call("LegislativeDocument", "GetDocumentClasses", argdict, keydict)


def get_all_documents_by_class(biennium: str, document_class: str) -> Dict[str, Any]:
    """See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetAllDocumentsByClass"""
    argdict: Dict[str, Any] = dict(biennium=biennium, documentClass=document_class)
    keydict: Dict[str, Any] = {
        "htmcreatedate": parser.parse,
        "htmlastmodifieddate": parser.parse,
        "pdfcreatedate": parser.parse,
        "pdflastmodifieddate": parser.parse,
    }
    return waleg.call("LegislativeDocument", "GetAllDocumentsByClass", argdict, keydict)
