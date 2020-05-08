# __author__ = 'Nildip Patel'

import allure
import pytest


#@allure.step
@allure.feature('Test - Auomation Framework in Python')
@allure.story('story1')
@pytest.mark.usefixtures("driver_init")
class TestExampleOne:

    @allure.title("This test has a custom title")
    def test_title(self):
        """
        Verify title of page
        :return: None
        """
        allure.attach('A text attacment in module scope fixture', 'blah blah blah', allure.attachment_type.TEXT)
        self.driver.get("https://aleri.ca/")
        assert self.driver.title == "Aleri"

@pytest.mark.usefixtures("driver_init")
class TestExampletwo:

    def test_title1(self):
        """
        Verify title of page
        :return: None
        """
        self.driver.get("https://aleri.ca/")
        assert self.driver.title == "Aleri"

