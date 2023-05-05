import pytest as pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.Configreader import readConfig
@pytest.fixture(params=["chrome"],scope="function")
def get_browser(request):

    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
    # if request.param == "firefox":
    #     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = driver
    driver.get(readConfig("basic info","testsiteurl"))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()