import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    logger= LogGen.log_gen()
    baseURL = ReadConfig.get_application_url()
    userName = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()


    @pytest.mark.regression
    def test_homePageTitle(self, setup):

        self.logger.info("**********  Test_001_Login  ********")
        self.logger.info("**********  Verifying Home Page Title  ********")

        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "Your store. Login123":
            assert True
            self.driver.close()
            self.logger.info("**********  Home Page Title test case passed ********")
        else:
            self.driver.save_screenshot("D:\\Python_Selenium\\nopCommerceApp\\Screenshots\\" +"test_homePageTitle_FAILED.png")
            self.logger.error("**********  Home Page Title test case failed ********")
            assert False
            self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("**********  Verifying the login test ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**********  Login test is passed  ********")
        else:
            self.driver.save_screenshot("D:\\Python_Selenium\\nopCommerceApp\\Screenshots\\" + "test_login_FAILED.png")
            assert False
            self.driver.close()
            self.logger.error("**********  Login test is failed  ********")
