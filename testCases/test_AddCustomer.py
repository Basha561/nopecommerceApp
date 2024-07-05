import time

import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator
import string
import random
class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationBaseUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self,setup):
        self.logger.info("********** Test_003_AddCustomerPage **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.Login()
        self.logger.info("********** Login Successful **********")
        self.logger.info("********** Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomersMenu()
        self.addcust.clickonCustomersMenuItem()
        self.addcust.clickonAddnew()
        self.logger.info("********** Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        #self.addcust.setCustomerRoles("Guests")
        #self.addcust.setManagerOfVendors("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("TestSharp")
        self.addcust.setLastName("Academy")
        self.addcust.setDob("06/06/1991")
        self.addcust.setCompanyname("TestSharp Academy")
        self.addcust.setAdminContent("This is for testing......")
        self.addcust.clickOnSave()
        self.logger.info("********** Saving customer info **********")
        self.logger.info("********** Add customer validation started **********")
        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            self.logger.info("********** Add customer test passed **********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_addcustomer.png")
            self.logger.info("********** Add customer test failed **********")
            assert False
        self.driver.close()
        self.logger.info("********** Ending Home Page Title Test **********")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return  ''.join(random.choice(chars) for x in range(size))






