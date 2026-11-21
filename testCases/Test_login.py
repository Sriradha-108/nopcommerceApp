import pytest
from selenium import webdriver
from pageObjects.loginPage import loginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):

        self.logger.info("**************** Test_001_Login ************ ")
        self.logger.info("************** Verifying Home Page Title************* ")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************** Home page title test is passed ************* ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************** Home page title test is failed ************* ")
            assert False

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("************** Verifying Login Test************* ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=loginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        # self.driver.close()
        if act_title=="Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("************** Login page title test is passed ************* ")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots" + "test_login.png")
            self.driver.close()
            self.logger.error("************** Login page title test is failed ************* ")
            assert False