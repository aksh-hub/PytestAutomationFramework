import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import moment

from pages.loginPage import LoginPage
from pages.homePage import HomePage

from datetime import date
from datetime import  datetime

from utils import utils

@pytest.mark.usefixtures("test_setup")
class TestLogin():
    #Add pytest fixture to test_setup
    #@pytest.fixture(scope="session") #When No class created
    # @pytest.fixture(scope="class")
    # def test_setup(self):
    #     global driver
    #     driver = webdriver.Chrome()
    #     driver.implicitly_wait(5)
    #     driver.maximize_window()
    #
    #     yield  # tear down methods
    #     driver.close()
    #     driver.quit()
    #
    #     print("***** Test Completed ******")

    #Add test_setup & tear down method to test_login method
    #def test_login(self,test_setup):
    def test_login(self):
        driver=self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enterUName(utils.UserName)
        login.enterPwd(utils.Password)
        login.clickLoginBtn()


    #Add test_setup & tear down method to test_logout method
    #def test_logout(self,test_setup):
    def test_logout(self):
        try:
            driver = self.driver
            home = HomePage(driver)
            home.clickWelcome()
            home.clickLogout()

            x= driver.title
            assert x=="Orange"

            print(driver.title)

        except AssertionError as error:
            print("assertion error occured")
            print(error)
            #currentTime=moment.now().strftime("%H:%M:%S_%d-%m-%Y")
            currentTime = datetime.now().strftime("%H:%M:%S_%d-%m-%Y")

            #screenShotName="screenshot"+currentTime
            testName = utils.whoami()
            screenShotName =testName+"_"+currentTime
            print(currentTime)
            allure.attach(self.driver.get_screenshot_as_png(),name=screenShotName,attachement_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_png("C:/Users/ashetti/PycharmProjects/AutomationFrameworkBuilding_1/screenshots"+screenShotName+".png")
            raise
        except:
            print("There was an exception")
            raise
        else:
            print("No exception occured")

        finally:
            print("This block will always execute|Close DB")
