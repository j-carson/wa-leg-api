from typing import Dict
from datetime import datetime  # noqa
from dateutil import parser  # noqa
from wa_leg_api import waleg


def get_documents_by_class(biennium: str, document_class: str, named_like: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetDocumentsByClass"""
    argdict = dict(biennium=biennium, documentClass=document_class, namedLike=named_like)
    keydict = {'htmcreatedate':parser.parse,
'htmlastmodifieddate':parser.parse,
'pdfcreatedate':parser.parse,
'pdflastmodifieddate':parser.parse,
}
    return waleg.call("LegislativeDocument", "GetDocumentsByClass", argdict, keydict)


def get_documents(biennium: str, named_like: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetDocuments"""
    argdict = dict(biennium=biennium, namedLike=named_like)
    keydict = {'htmcreatedate':parser.parse,
'htmlastmodifieddate':parser.parse,
'pdfcreatedate':parser.parse,
'pdflastmodifieddate':parser.parse,
}
    return waleg.call("LegislativeDocument", "GetDocuments", argdict, keydict)


def get_document_classes(biennium: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetDocumentClasses"""
    argdict = dict(biennium=biennium)
    keydict = {}
    return waleg.call("LegislativeDocument", "GetDocumentClasses", argdict, keydict)


def get_all_documents_by_class(biennium: str, document_class: str) -> Dict:
    """See: http://wslwebservices.leg.wa.gov/legislativedocumentservice.asmx?op=GetAllDocumentsByClass"""
    argdict = dict(biennium=biennium, documentClass=document_class)
    keydict = {'htmcreatedate':parser.parse,
'htmlastmodifieddate':parser.parse,
'pdfcreatedate':parser.parse,
'pdflastmodifieddate':parser.parse,
}
    return waleg.call("LegislativeDocument", "GetAllDocumentsByClass", argdict, keydict)
