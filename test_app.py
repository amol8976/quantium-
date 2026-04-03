from app import app

def test_header_present():
    # Test if the header is present by checking the layout string
    assert "Sales Visualizer" in str(app.layout), "Header text not found in layout"

def test_visualization_present():
    # Test if the line chart visualization is present
    assert "sales-line-chart" in str(app.layout), "Visualization graph not found in layout"

def test_region_picker_present():
    # Test if the region picker radio buttons are present
    assert "region-filter" in str(app.layout), "Region picker not found in layout"
