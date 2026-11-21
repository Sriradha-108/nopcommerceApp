import pytest
from selenium import webdriver
from pageObjects.loginPage import loginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//testData//LoginData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************ Test_002_DDT_Login *****************")
        self.logger.info("************** Verifying Login DDT test ************* ")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp=loginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows i a Excel:", self.rows)

        list_status = []   # empty list variable

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("**** failed ****")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    list_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("**** Login DDT test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT test failed ****")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")
