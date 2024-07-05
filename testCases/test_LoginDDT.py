import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator
from utilities.ExcelUtils import XLUtils

class Test_001_Login_DDT:
    baseURL= ReadConfig.getApplicationBaseUrl()
    path = ".\\TestData\\LoginData.xlsx"
    logger = LogGenerator.loggen()

    @pytest.mark.regression
    def test_home_page_title_DDT(self,setup):
        self.logger.info("*************** test_home_page_title_DDT started ***************")
        self.logger.info("*************** Verifying home page title ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in excel", self.rows)
        lst_status = []
        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.Login()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("Passed")
                    self.lp.Logout()
                    lst_status.append("Pass")
                elif self.exp == "fail":
                    self.logger.info("Failed")
                    self.lp.Logout()
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp == "Pass":
                    self.logger.info("Failed")
                    lst_status.append("Fail")
                elif self.exp == "fail":
                    self.logger.info("Passed")
                    lst_status.append("Pass")
        if 'Fail' not in lst_status:
            self.logger.info("test_home_page_title_DDT is passed")
            assert True
        else:
            self.logger.info("test_home_page_title_DDT is failed")
            assert False
        self.logger.info("*************** test_home_page_title_DDT Ended ***************")
        self.logger.info("*************** Completed Verifying home page title test ***************")













