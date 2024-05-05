from selenium.webdriver.common.by import By
class LoginPage():
    def __init__(self,driver):
        self.driver = driver

        self.txt_Uname_byName = "username"
        self.txt_Pwd_byName = "password"
        self.btn_Login_byCSS = "button[class*='orangehrm-login']"
        self.drpDwn_UserAccount_byCSS = "p[class*='userdropdown']"
        self.lnk_Logout_byLinkTxt = "Logout"

    def enterUName(self,uname):
        self.driver.find_element(By.NAME, self.txt_Uname_byName).clear()
        self.driver.find_element(By.NAME, self.txt_Uname_byName).send_keys(uname)

    def enterPwd(self,pwd):
        self.driver.find_element(By.NAME, self.txt_Pwd_byName).clear()
        self.driver.find_element(By.NAME, self.txt_Pwd_byName).send_keys(pwd)

    def clickLoginBtn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_Login_byCSS).click()
