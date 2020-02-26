from solsrv import api

# TODO: add tests for add_documents


def test_get_unknown_document():
    solsrv = api.Solsrv()
    _, code = solsrv.get_document("0")
    assert code == 404


def test_add_single_document():
    solsrv = api.Solsrv()
    assert solsrv.add_document("0", "a b c") is None
    assert solsrv.get_document("0") == "a b c"
    assert solsrv.status()["len(store)"] == 1


def test_add_duplicate_document():
    solsrv = api.Solsrv()
    assert solsrv.add_document("0", "a b c") is None
    assert solsrv.get_document("0") == "a b c"
    assert solsrv.status()["len(store)"] == 1
    _, code = solsrv.add_document("0", "x y z")
    assert code == 409
    assert solsrv.status()["len(store)"] == 1


def test_add_too_long_id():
    solsrv = api.Solsrv()
    id_ = "0" * 128
    _, code = solsrv.add_document(id_, "a b c")
    assert code == 400
    assert solsrv.status()["len(store)"] == 0


def test_add_max_length_id():
    solsrv = api.Solsrv()
    id_ = "0" * 42
    assert solsrv.add_document(id_, "a b c") is None
    assert solsrv.get_document(id_) == "a b c"
    assert solsrv.status()["len(store)"] == 1


def test_get_too_long_id():
    solsrv = api.Solsrv()
    id_ = "0" * 128
    _, code = solsrv.get_document(id_)
    assert code == 404
