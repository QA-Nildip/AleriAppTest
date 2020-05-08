__author__ = 'Nildip Patel'

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver_init(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome("C://Users//Nildip//PycharmProjects//AleriAppTest//drivers//chrome//chromedriver.exe") #if not added in PATH
    request.cls.driver = driver
    yield driver
    driver.close()



# @pytest.fixture(autouse="true")#scope='session')
# def driver_init():
#     print("Setting up web driver")
#     # binary = FirefoxBinary(r'C:\\Program Files\\Mozilla Firefox\\firefox.exe')
#     # driver = webdriver.Firefox(firefox_binary=binary,
#     #                            executable_path=r'C:\Users\Nildip\PycharmProjects\AleriAppTest\drivers\firefox\geckodriver.exe')
#     service = Service(r'C:\Users\Nildip\PycharmProjects\AleriAppTest\drivers\chrome\chromedriver.exe')
#     service.start()
#     driver = webdriver.Remote(service.service_url)
#     # driver.maximize_window()
#     driver.get("https://aleri.ca")
#     yield driver
#     print("Tearing down")
#     driver.close()
#     driver.quit()

