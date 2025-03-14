import pytest
from appium.options.common import AppiumOptions

@pytest.fixture(scope='session')
def android_setting():
    NO_RESET =  False

    options = AppiumOptions()
    options.set_capability('platformName', 'Android')
    options.set_capability('platformVersion', '14')
    options.set_capability('deviceName', 'CN48E3M00036')
    options.set_capability('automationName', 'uiautomator2')
    options.set_capability('appPackage', 'com.google.android.calculator')
    options.set_capability('appActivity', 'com.android.calculator2.Calculator')
    options.set_capability('noReset', NO_RESET)
    return options

    # appium_options.set_capability('autoGrantPermissions', True)
    # appium_options.set_capability('enableMultiWindows', True)
    # appium_options.set_capability('shouldTerminateApp', True)
    # appium_options.set_capability('disableWindowAnimation', True)
    # appium_options.set_capability('waitForIdleTimeout', 100)
