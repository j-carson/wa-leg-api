from wa_leg_api.legislativedocument import *


def test_legislative_document():
    biennium = '2019-20'
    document_class = 'Bills'
    named_like = '1010'

    x = get_document_classes(biennium)
    x = get_all_documents_by_class(biennium,document_class)
    x = get_documents_by_class(biennium,document_class,named_like)
    x = get_documents(biennium,named_like)

if __name__ == "__main__":
    test_legislative_document()


