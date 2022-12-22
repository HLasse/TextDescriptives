import textdescriptives as td


def test_get_valid_metrics():
    metrics = td.get_valid_metrics()
    assert isinstance(metrics, set)
    assert len(metrics) > 0
    assert isinstance(metrics.pop(), str)


def test_get_columns():
    columns_ = set()
    for metric in td.get_valid_metrics():
        columns = td.get_columns(metric)
        assert isinstance(columns, list)
        assert len(columns) > 0
        assert isinstance(columns[0], str)
        columns_.update(columns)
    columns_all = td.get_columns("all")
    assert set(columns_all) == columns_
    assert set(columns_all) == columns_
