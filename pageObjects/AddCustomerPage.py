import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select

class AddCustomer():
    lnkcustomers_menu_xpath = "//a[@href='#']/p[contains(text(),'Customers')]"
    lnkcustomers_menuitem_xpath ="//p[contains(text(),'Customers')]/../../a[@href='/Admin/Customer/List']"
    btnAddNew_xpath = "//a[@href='/Admin/Customer/Create']"
    txtEmail_xpath ="//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstname_xpath ="//input[@id='FirstName']"
    txtLastname_xpath ="//input[@id='LastName']"
    rdmale_xpath="//input[@id='Gender_Male']"
    rdfemale_xpath = "//input[@id='Gender_Female']"
    txtdob_xpath ="//input[@id='DateOfBirth']"
    txtcompany_xpath ="//input[@id='Company']"
    txtAdminComment_xpath ="//textarea[@id='AdminComment']"
    btnsave_xpath = "//button[@name='save']"
    drpVendor_xpath = "//select[@id='VendorId']"
    selectcustomerrole_xpath = "//select[@id='SelectedCustomerRoleIds']"
    lstitemsRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemsGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemsVendors_xpath = "//li[contains(text(),'Vendors')]"
    lstitemsAdministrators_xpath = "//li[contains(text(),'Administrators')]"

    def __init__(self,driver):
        self.driver = driver

    def clickonCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkcustomers_menu_xpath).click()

    def clickonCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkcustomers_menuitem_xpath).click()

    def clickonAddnew(self):
        self.driver.find_element(By.XPATH,self.btnAddNew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.selectcustomerrole_xpath).send_keys(role)

    def setManagerOfVendors(self):
        self.driver.find_element(By.XPATH,self.drpVendor_xpath).send_keys()

    def setGender(self,gender):
        self.driver.find_element(By.XPATH,self.rdmale_xpath).send_keys(gender)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.txtFirstname_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txtLastname_xpath).send_keys(lname)

    def setDob(self,dob):
        self.driver.find_element(By.XPATH,self.txtdob_xpath).send_keys(dob)

    def setCompanyname(self,companyName):
        self.driver.find_element(By.XPATH,self.txtcompany_xpath).send_keys(companyName)

    def setAdminContent(self,admincontent):
        self.driver.find_element(By.XPATH,self.txtAdminComment_xpath).send_keys(admincontent)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnsave_xpath).click()




