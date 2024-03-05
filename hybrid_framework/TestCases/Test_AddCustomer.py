from time import sleep

import pytest

from PageObject.LoginPageObj import Login
from PageObject.AddCustomerPageObj import AddCustomer
from Utility.CustomLogger import custom_log
# from Utility.ReadIni import ReadProperty
# from TestData.Test_data import login_data_py
# from Utility.xl_utility import *
from Utility.xmlUtility import *

class Test_Add_Customer_Functionality:

    log = custom_log()
    xml_file = r".\TestData\customer_page.xml"
    login_data_xml = []
    data_dict = load_test_data(xml_file)
    for k, v in data_dict["add_customer_page"].items():
        print(k)
        print("**************")
        login_data_xml.append(tuple(v.values()))

    @pytest.mark.parametrize(
        "user, password, email, newpassword, firstname,lastname, Gender, dateofbirth, companyname,taxexempt,newsletter,customerroles,Managerofvendor,active, expect",
        login_data_xml)  # for xml
    def test_verify_add_new(self, setup, user, password, email, newpassword, firstname,lastname, Gender, dateofbirth, companyname,taxexempt,newsletter,customerroles,Managerofvendor,active, expect):
        driver = setup

        self.log.info("Launching browser")
        login_obj = Login(driver)
    # login_obj.ClickCheckbox()
        login_obj.SetEmail(user)
        login_obj.SetPassword(password)
        login_obj.ClickLogin()
        self.log.info("Successfully login to the Dashbord...")
        ac_obj = AddCustomer(driver)
        ac_obj.NavigatetoAddCustomer()
        ac_obj.SetCustomerEmail(email)
        ac_obj.SetCustomerPassword(newpassword)
        ac_obj.SetCustomerFirstName(firstname)
        ac_obj.SetCustomerLastName(lastname)
        ac_obj.SetCustomerGender(Gender)
        ac_obj.SetCustomerDOB(dateofbirth)
        ac_obj.SetCustomerCompany(companyname)
        ac_obj.SetCustomerTax(taxexempt)
        ac_obj.SetCustomerNewsletter(newsletter)
        ac_obj.SetCustomerRole(customerroles)
        ac_obj.SetCustomerVendor(Managerofvendor)
        ac_obj.SetCustomerActive(active)
        ac_obj.SetAdminContent()
        ac_obj.ClickSave()
        sleep(5)
       # status = ac_obj.Verify_Alert()
        #self.log.info("Successful Created the customer")
        sleep(5)
        if ac_obj.Verify_Alert() == "The new customer has been added successfully.":
            login_obj.ClickLogOut()
            self.log.info("TC::test_verify_add_new=PASSED")
            assert True
        elif ac_obj.Validation_errors() == "Email is already registered":
        #elif ac_obj.Validation_errors() == "The customer cannot be in both 'Guests' and 'Registered' customer roles":
            driver.save_screenshot(r".\ScreenShot\test_verify_add_new_customer_.png")
            self.log.error("TC::test_verify_add_new=FAILED")
        # elif == "Valid Email is required for customer to be in 'Registered' role"
        # elif == "Please enter a valid email address.""
        else:
            self.log.error("TC::test_verify_add_new=FAILED")
            driver.save_screenshot(r".\ScreenShot\test_verify_add_new_customer.png")
            assert False

# from hybrid_framework.PageObject.LoginPageObj import Login
# from hybrid_framework.PageObject.AddCustomerPageObj import AddCustomer
# from hybrid_framework.Utility.CustomLogger import custom_log
# from hybrid_framework.Utility.ReadIni import ReadProperty
# class Test_Add_Customer_Functionality:
#     log=custom_log()
#     def test_verify_add_new(self, setup):
#         driver = setup
#         self.log.info("Launching browser")
#         login_obj = Login(driver)
#         login_obj.SetEmail(ReadProperty.GetUser())
#         login_obj.SetPassword(ReadProperty.GetPassword())
#         login_obj.ClickLogin()
#         self.log.info("Successfully login to the Dashbord...")
#         ac_obj = AddCustomer(driver)
#         ac_obj.NavigatetoAddCustomer()
#         ac_obj.SetCustomerEmail("xyz.gamil.com")
#         ac_obj.SetCustomerPassword("123456")
#         ac_obj.SetCustomerFirstName("sam")
#         ac_obj.SetCustomerLastName("pooja")
#         ac_obj.SetCustomerGender("Male")
#         ac_obj.SetCustomerDOB("3/2/2024")
#         ac_obj.SetCustomerCompany("xyz company")
#         ac_obj.SetCustomerTax("yes")
#         ac_obj.SetCustomerNewsletter("Your store name")
#         ac_obj.SetCustomerRole("Guests")
#         ac_obj.SetCustomerVendor("Vendor 1")
#         ac_obj.SetCustomerActive("yes")
#         ac_obj.SetAdminContent()
#         ac_obj.ClickSave()