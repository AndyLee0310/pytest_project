import pytest
from appium.options.common import AppiumOptions

@pytest.fixture(scope='session')
def android_setting():
    PORT = '4723'
    NO_RESET = 'False'

    options = AppiumOptions()
    options.set_capability('platformName', 'Android')
    options.set_capability('platformVersion', '14')
    options.set_capability('deviceName', 'CN48E3M00036')
    options.set_capability('automationName', 'uiautomator2')
    options.set_capability('appPackage', 'com.google.android.calculator')
    options.set_capability('appActivity', 'com.android.calculator2.Calculator')
    options.set_capability('noReset', NO_RESET)
    return options

# @pytest.fixture(scope='function')
# def android_setting():
#     PORT = '4723'
#     NO_RESET = 'False'

#     appium_options = AppiumOptions()
#     appium_options.set_capability('platformName', 'Android')
#     appium_options.set_capability('platformVersion', '14')
#     appium_options.set_capability('deviceName', 'CN48E3M00036')
#     appium_options.set_capability('automationName', 'uiautomator2')
#     # appium_options.set_capability('autoGrantPermissions', True)
#     # appium_options.set_capability('enableMultiWindows', True)
#     appium_options.set_capability('appPackage', 'com.google.android.calculator')
#     appium_options.set_capability('appActivity', 'com.android.calculator2.Calculator')
#     appium_options.set_capability('noReset', NO_RESET)
#     # appium_options.set_capability('shouldTerminateApp', True)
#     # appium_options.set_capability('disableWindowAnimation', True)
#     # appium_options.set_capability('waitForIdleTimeout', 100)

#     driver = webdriver.Remote(f'http://localhost:{PORT}', options=appium_options)
#     logging.info('driver start')
#     yield driver
#     driver.quit()
#     logging.info('driver quit')