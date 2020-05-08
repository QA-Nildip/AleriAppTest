# __author__ = 'Nildip Patel'

import pytest


@pytest.mark.usefixtures("driver_init")
class TestExampleOne:

    def test_title(self):
        """
        Verify title of page
        :return: None
        """
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

