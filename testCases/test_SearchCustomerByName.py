import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator

class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationBaseUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGenerator.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_searchcustomerbyName(self,setup):
        self.logger.info("********** Test_SearchCustomerByName_004 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.Login()
        self.logger.info("********** Login Successful **********")
        self.logger.info("********** Starting Search Customer By Name **********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomersMenu()
        time.sleep(3)
        self.addcust.clickonCustomersMenuItem()
        self.logger.info("********** Searching Customer By Name **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("********** Test_SearchCustomerByName_005 Finished **********")
        self.driver.close()

