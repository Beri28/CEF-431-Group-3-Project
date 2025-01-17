import pytest

def pytest_html_report_title(report):
    report.title = "Dreamland Restaurant Automation Test Report"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    # Add test case ID and description to the report
    if hasattr(item.function, 'test_id'):
        report.test_id = item.function.test_id
    if hasattr(item.function, 'description'):
        report.description = item.function.description
    
    # Add extra details to the report
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # Add timestamps
        import datetime
        extra.append(('Timestamp', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
    report.extra = extra