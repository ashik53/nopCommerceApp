import time
from typing import List, Any
import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_ddt_Login:

    logger= LogGen.log_gen()
    baseURL = ReadConfig.get_application_url()
    path = "..//TestData/LoginData.xlsx"

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("**********  Test_002_ddt_Login ********")
        self.logger.info("**********  Verifying the login test ********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of Rows in a excel sheet: ",self.rows)

        lst_status =[]

        #loop through the excel sheet
        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, "Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)


            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            actual_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if actual_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("******* Passed ******")
                    self.lp.clickLogout()
                    lst_status.append("Pass" )
                elif self.exp == "Fail":
                    self.logger.info("******* Failed ******")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif actual_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("******* Failed ******")
                    lst_status.append("Fail" )
                elif self.exp == "Fail":
                    self.logger.info("******* Passed ******")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info('******** Login DDT test passed *************')
            self.driver.close()
            assert True
        else:
            self.logger.info('******** Login DDT test failed *************')
            self.driver.close()
            assert False

        self.logger.info("********* End of Login DDT Test **************")
        self.logger.info("********* Completed Test_002_ddt_Login **************")





























