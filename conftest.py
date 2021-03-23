# import pytest
# from selenium import webdriver
#
# from base_data.main_data import MainData
# driver = None
#
# @pytest.fixture(scope='session', autouse=True)
# def browser():
#     global driver
#     if driver is None:
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(5)
#         driver.maximize_window()
#         driver.get(MainData.BaseUrl)
#         yield driver
#         driver.quit()
#
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = "screen_error/"+report.nodeid.replace("::", "_")+".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)