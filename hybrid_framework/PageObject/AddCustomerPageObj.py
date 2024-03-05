from time import sleep


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait



class AddCustomer:
    xpath_customer_menu="//ul[@role='menu']/li/a/p[contains(text(),'Customers')]"
    xpath_customer_option = "//ul[@role='menu']/li/ul/li/a/p[contains(text(),'Customers')]"
    xpath_add_new="//a[@class='btn btn-primary']"
    id_Email="Email"
    id_Password="Password"
    id_Firstname="FirstName"
    id_Lastname="LastName"
    gender = "Female"
    xpath_gender = f"//input[@name='Gender']/following-sibling::label[contains(text(),'{gender}')]"# female or male
    id_dob = "DateOfBirth"
    id_company="Company"
    id_tax="IsTaxExempt"
    xpath_newsletter = "//input[@aria-labelledby='SelectedNewsletterSubscriptionStoreIds_label']"
    xpath_customerrole = "//input[@aria-labelledby='SelectedCustomerRoleIds_label']"
    xpath_delete_register_role="//span[text()='Registered']/following-sibling::span"
    id_select_vendo='VendorId'
    id_active='Active'
    id_admin_comment='AdminComment'
    xpath_save = "//button[@name='save']"
    xpath_alert="//div[@class='alert alert-success alert-dismissable']"
    #xpath_validation_error = "//li[contains(text(),'The customer cannot be in both 'Guests' and 'Registered' customer roles')]"
    xpath_validation_error="//li[contains(text(),'Email is already registered')]"


    def __init__(self, driver):
        self.driver = driver
        self.wait_obj = WebDriverWait(driver, 10)

    def NavigatetoAddCustomer(self):
        sleep(2)
        self.driver.find_element(By.XPATH, self.xpath_customer_menu).click()
        sleep(2)
        self.driver.find_element(By.XPATH, self.xpath_customer_option).click()
        self.driver.find_element(By.XPATH, self.xpath_add_new).click()

    def SetCustomerEmail(self, email):
        self.driver.find_element(By.ID, self.id_Email).send_keys(email)

    def SetCustomerPassword(self, pswd):
        self.driver.find_element(By.ID, self.id_Password).send_keys(pswd)

    def SetCustomerFirstName(self, name):
        self.driver.find_element(By.ID, self.id_Firstname).send_keys(name)

    def SetCustomerLastName(self, name):
        self.driver.find_element(By.ID, self.id_Lastname).send_keys(name)

    def SetCustomerGender(self, gender):
        self.gender=gender
        self.driver.find_element(By.XPATH, self.xpath_gender).click()

    def SetCustomerDOB(self, dob):
        self.driver.find_element(By.ID, self.id_dob).send_keys(dob)

    def SetCustomerCompany(self, company):
        self.driver.find_element(By.ID, self.id_company).send_keys(company)

    def SetCustomerTax(self, tax):
        if tax=="yes":
            self.driver.find_element(By.ID, self.id_tax).click()

    def SetCustomerNewsletter(self, newsletter):
        self.driver.find_element(By.XPATH, self.xpath_newsletter).click()
        sleep(3)
        self.driver.find_element(By.XPATH, f"//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[text()='{newsletter}']").click()

    def SetCustomerRole(self, role):
        if role=="Guests":
            sleep(2)
            self.driver.find_element(By.XPATH, self.xpath_delete_register_role).click()
            self.driver.find_element(By.XPATH,self.xpath_customerrole).click()
            sleep(3)
            self.driver.find_element(By.XPATH, f"//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'{role}')]").click()
        elif role=="Registered":
            pass
        else:
            self.driver.find_element(By.XPATH, self.xpath_customerrole).click()
            sleep(3)
            self.driver.find_element(By.XPATH, f"//ul[@id='SelectedCustomerRoleIds_listbox']/li[contains(text(),'{role}')]").click()



    def SetCustomerVendor(self, vendor):
        drp_down_obj = Select(self.driver.find_element(By.ID, self.id_select_vendo))
        sleep(2)
        drp_down_obj.select_by_visible_text(vendor)

    def SetCustomerActive(self, status):
        if status=="yes":
            self.driver.find_element(By.ID, self.id_active).click()

    def SetAdminContent(self):
        msg="this is admin content"
        self.driver.find_element(By.ID, self.id_admin_comment).send_keys(msg)

    def ClickSave(self):
        self.driver.find_element(By.XPATH, self.xpath_save).click()

    def Verify_Alert(self):
        #return ("The new customer has been added successfully." in
        self.driver.find_element(By.XPATH, self.xpath_alert).text

    def Validation_errors(self):
        self.driver.find_element(By.XPATH,self.xpath_validation_error)

