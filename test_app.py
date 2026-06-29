import app


def test_header_present():
    layout = app.app.layout
    assert any("Soul Foods Sales Visualiser" in str(child) for child in layout.children)


def test_graph_present():
    layout = app.app.layout
    assert any("sales-chart" in str(child) for child in layout.children)


def test_region_picker_present():
    layout = app.app.layout
    assert any("region-filter" in str(child) for child in layout.children)