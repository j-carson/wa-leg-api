from datetime import datetime  # noqa
from typing import Any, Dict

from dateutil import parser  # noqa

from wa_leg_api import waleg


def get_documents_by_class(biennium: str, document_class: str, named_like: str) -> Dict[str, Any]:
    """Lists legislative documents of the given document class with names starting with the namedlike value.
    Exception thrown for invalid biennium, documentClass or namedLike or when no documents found.
    Expects the biennium in the format: 2005-06.  Information is available back to 1991-92. For Initiatives to the Legislature, enter the following in namedLike: Initiative.
    The results will include URLs to PDF and HTM versions of each document.

    See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetDocumentsByClass"""
    argdict: Dict[str, Any] = dict(biennium=biennium, documentClass=document_class, namedLike=named_like)
    keydict: Dict[str, Any] = {
        "htm_create_date": parser.parse,
        "htm_last_modified_date": parser.parse,
        "pdf_create_date": parser.parse,
        "pdf_last_modified_date": parser.parse,
    }
    return waleg.call("LegislativeDocument", "GetDocumentsByClass", argdict, keydict)


def get_documents(biennium: str, named_like: str) -> Dict[str, Any]:
    """Lists legislative documents with names starting with the namedlike value.
    Exception thrown for invalid biennium or namedLike or when no documents found.
    Expects the biennium in the format: 2005-06. Information is available back to 1991-92.For Initiatives to the Legislature, enter the following in namedLike: Initiative.<br>The results will include URLs to PDF and HTM versions of each document.

    See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetDocuments"""
    argdict: Dict[str, Any] = dict(biennium=biennium, namedLike=named_like)
    keydict: Dict[str, Any] = {
        "htm_create_date": parser.parse,
        "htm_last_modified_date": parser.parse,
        "pdf_create_date": parser.parse,
        "pdf_last_modified_date": parser.parse,
    }
    return waleg.call("LegislativeDocument", "GetDocuments", argdict, keydict)


def get_document_classes(biennium: str) -> Dict[str, Any]:
    """Returns available bill family document types for the given biennium.
    Exception thrown for invalid biennium.
    Expects biennium to be in the format: 2005-06.  Information is available back to 1991-92.

    See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetDocumentClasses"""
    argdict: Dict[str, Any] = dict(biennium=biennium)
    keydict: Dict[str, Any] = {}
    return waleg.call("LegislativeDocument", "GetDocumentClasses", argdict, keydict)


def get_all_documents_by_class(biennium: str, document_class: str) -> Dict[str, Any]:
    """Lists all legislative documents of the given document class.
    Exception thrown for invalid biennium or documentClass.
    Expects the biennium in the format: 2005-06.  Information is available back to 1991-92.
    The results will include URLs to PDF and HTM versions of each document.

    See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetAllDocumentsByClass"""
    argdict: Dict[str, Any] = dict(biennium=biennium, documentClass=document_class)
    keydict: Dict[str, Any] = {
        "htm_create_date": parser.parse,
        "htm_last_modified_date": parser.parse,
        "pdf_create_date": parser.parse,
        "pdf_last_modified_date": parser.parse,
    }
    return waleg.call("LegislativeDocument", "GetAllDocumentsByClass", argdict, keydict)
