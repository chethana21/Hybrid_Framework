import sys
from time import sleep

import pytest

# from hybrid_framework.PageObject.LoginPageObj import Login
# from hybrid_framework.TestData.Test_data import login_data_py
# from hybrid_framework.Utility.CustomLogger import custom_log
# from hybrid_framework.Utility.xl_utility import *
# from hybrid_framework.Utility.xmlUtility import *
from PageObject.LoginPageObj import Login
from TestData.Test_data import login_data_py
from Utility.CustomLogger import custom_log
from Utility.xl_utility import *
from Utility.xmlUtility import *

class Test_Login_DDT:
    log=custom_log()
    ###################################
    # excel
    ################################33
    # xlpath = r".\TestData\LoginData.xlsx"
    # sheet = "Sheet1"
    # # print(GetRow(xlpath, sheet))
    # # print(GetCol(xlpath, sheet))
    # login_data=[]
    # for r in range(2, GetRow(xlpath, sheet)+1):
    #     temp_list=[]
    #     for c in range(1, GetCol(xlpath, sheet)+1):
    #         temp_list.append(ReadCell(xlpath, sheet,r,c))
    #     login_data.append(tuple(temp_list))
    # print(login_data) #[('admin@yourstore.com', 'admin', 'Pass'), ('admin@yourstore.com', 'adm', 'Fail'), ('adm@yourstore.com', 'admin', 'Fail'), ('adm@yourstore.com', 'adm', 'Fail'
    # )]
    ###################################
    # xml
    ################################33
    xml_file=r".\TestData\test_data_xml.xml"
    login_data_xml=[]
    data_dict = load_test_data(xml_file)
    for k, v in data_dict["login_data"].items():
        print(k)
        print("**************")
        login_data_xml.append(tuple(v.values()))

    print(login_data_xml)
    # @pytest.mark.parametrize("email, password, expect",login_data_py)# for pyfile
    # @pytest.mark.parametrize("email, password, expect",login_data)#for excel
    @pytest.mark.parametrize("email, password, expect",login_data_xml)#for xml
    def test_verify_login_ddt(self, setup, email, password, expect):
        driver = setup
        self.log.info("Launching browser")
        login_obj = Login(driver)
        # login_obj.ClickCheckbox()
        login_obj.SetEmail(email)
        login_obj.SetPassword(password)
        login_obj.ClickLogin()
        self.log.info("Successfully login to the Dashbord...")
        profile = login_obj.VerifyLogin()
        if profile == "John Smith" and expect=="Pass":
            login_obj.ClickLogOut()
            self.log.info("TC::test_verify_login=PASSED")
            assert True
        elif profile != "John Smith" and expect=="Fail":
            self.log.info("TC::test_verify_login=PASSED")
            assert True
        else:
            self.log.error("TC::test_verify_login=FAILED")
            driver.save_screenshot(r".\ScreenShot\test_verify_login.png")
            assert False