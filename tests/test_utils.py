import textdescriptives as td


def test_get_valid_metrics():
    metrics = td.get_valid_metrics()
    assert isinstance(metrics, set)
    assert len(metrics) > 0
    assert isinstance(metrics.pop(), str)


def test_get_columns():
    columns_ = set()
    for metric in td.get_valid_metrics():
        columns = td.get_doc_assigns(metric)
        assert isinstance(columns, list)
        assert len(columns) > 0
        assert isinstance(columns[0], str)
        columns_.update(columns)
    columns_all = td.get_doc_assigns("all")
    assert set(columns_all) == columns_
