import pytest
from selenium import webdriver


#from hybrid_framework.Utility.ReadIni import ReadProperty
from Utility.ReadIni import ReadProperty

@pytest.fixture()
def setup(request):
    if request.config.getoption("--browser")=="chrome":
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"C:\Users\Dhipak\OneDrive\Desktop\Drivers\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif request.config.getoption("--browser")=="edge":
        from selenium.webdriver.edge.service import Service
        service_obj = Service(r"C:\Users\Dhipak\OneDrive\Desktop\Drivers\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    elif request.config.getoption("--browser")=="ff":
        # from selenium.webdriver.firefox.service import Service
        # service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
        driver = webdriver.Firefox()
    else:
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"C:\Users\Dhipak\OneDrive\Desktop\Drivers\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    driver.get(ReadProperty.GetBaseURL())
    yield driver
    driver.quit()

def pytest_addoption(parser):  # this will get the values from CLI/hooks
    parser.addoption("--browser")