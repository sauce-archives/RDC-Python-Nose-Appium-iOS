import os
import sys
import inspect
from nose.tools import with_setup
from appium import webdriver
import monkeypatch_rc

browsers = [{
    'platformName':    'Android',
    'platformVersion': '7',
    'deviceName':      'LG Nexus 5X'
}]

def launchBrowser(caps):
    caps['name'] = inspect.stack()[1][3]
    caps['testobject_api_key'] = os.environ['TESTOBJECT_API_KEY']
    return webdriver.Remote(
            command_executor = "http://us1.appium.testobject.com/wd/hub",
            desired_capabilities = caps);

def teardown_func():
    global driver
    driver.quit()
    status = sys.exc_info() == (None, None, None)

# Will generate a test for each browser and os configuration
def test_generator():
    for browser in browsers:
        yield compute_sum, browser

@with_setup(None, teardown_func)
def compute_sum(browser):
    global driver
    driver = launchBrowser(browser)
    # insert values
    field_one = driver.find_element_by_accessibility_id("TextField1")
    field_one.send_keys("12")

    field_two = driver.find_elements_by_class_name("UIATextField")[1]
    field_two.send_keys("8")

    # trigger computation by using the button
    driver.find_element_by_accessibility_id("ComputeSumButton").click();

    # is sum equal?
    sum = driver.find_element_by_class_name("UIAStaticText").text;
    assert int(sum) == 20, "ERROR MESSAGE"

