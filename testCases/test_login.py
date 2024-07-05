import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator

class Test_001_Login:
    baseURL= ReadConfig.getApplicationBaseUrl()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    logger = LogGenerator.loggen()

    @pytest.mark.regression
    def test_login_page_title(self,setup):
        self.logger.info("*************** Test_001_Login ***************")
        self.logger.info("*************** Verifying login page title ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        # Validations
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("*************** Test is passed ***************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login_page_title.png")
            self.driver.close()
            self.logger.error("*************** Test is failed ***************")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_home_page_title(self,setup):
        self.logger.info("*************** test_home_page_title ***************")
        self.logger.info("*************** Verifying home page title ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.Login()
        act_title = self.driver.title

        # Validations
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("*************** test_home_page_title is passed ***************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_home_page_title.png")
            self.driver.close()
            self.logger.error("*************** test_home_page_title is failed ***************")
            assert False




