from selenium.webdriver.common.by import By

class LoginPage:
    textbox_email_id="Email"
    textbox_password_id = "Password"
    button_login_xpath="//button[text()='Log in']"
    button_logout_xpath = "//a[text()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID,self.textbox_email_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def Login(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def Logout(self):
        self.driver.find_element(By.XPATH,self.button_logout_xpath).click()
