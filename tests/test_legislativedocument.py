from wa_leg_api.legislativedocument import *


def test_legislative_document():
    biennium = "2019-20"
    document_class = "Bills"
    named_like = "1010"

    get_document_classes(biennium)
    get_all_documents_by_class(biennium, document_class)
    get_documents_by_class(biennium, document_class, named_like)
    get_documents(biennium, named_like)


if __name__ == "__main__":
    test_legislative_document()
