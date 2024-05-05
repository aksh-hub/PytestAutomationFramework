from selenium.webdriver.common.by import By
import time
class HomePage():
    def __init__(self,driver):
        self.driver = driver
        self.acnt_byCSS = "p[class*='userdropdown']"
        self.logout_byLinkTxt = "Logout"


    def clickWelcome(self):
        self.driver.find_element(By.CSS_SELECTOR,self.acnt_byCSS).click()
        time.sleep(3)


    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_byLinkTxt).click()
        time.sleep(2)
