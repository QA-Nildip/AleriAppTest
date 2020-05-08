# import time
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
#
# service = Service(r'C:\Users\Nildip\PycharmProjects\AleriAppTest\drivers\chrome\chromedriver.exe')
# service.start()
# driver = webdriver.Remote(service.service_url)
# driver.get('http://aleri.ca');
# time.sleep(5) # Let the user actually see something!
# driver.quit()


from selenium import webdriver


#@pytest.fixture(scope="class")
def setup():
    print("initiating chrome driver")
    driver = webdriver.Chrome(r'C:\Users\Nildip\PycharmProjects\AleriAppTest\drivers\chrome\chromedriver.exe') #if not added in PATH
    #driver.get("http://seleniumeasy.com/test")
    #driver.maximize_window()
    driver.close()

setup()