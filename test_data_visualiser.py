from data_visualiser import app

def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#line_chart", timeout=10)


def test_region_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region_picker", timeout=10)
