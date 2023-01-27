import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
@pytest.fixture
def setup(browser):
    #print("hi")
    if browser == "chrome":
        servobj=Service(r"C:\Users\kirthiga\OneDrive\Desktop\webdriver\chromedriver_win32(1)\chromedriver.exe")
        driver=webdriver.Chrome(service=servobj)
        return driver
    
    elif browser == "edge":
        servobj=Service(r"C:\Users\kirthiga\OneDrive\Desktop\webdriver\edgedriver_win64\msedgedriver.exe")
        driver=webdriver.Edge(service=servobj)
        return driver 

def pytest_addoption(parser): #this ll get value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

#####Pytest HTML Report
######hook for Adding Environment for HTML report
def pytest_configure(config):
    config._metadata['project Name']="Automation Testing-Inuvest Technologies"
    config._metadata['Module Name']="Login-SignUp"
    config._metadata['Tester']="Kirthiga"
######hook for Deleting Environment for HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
