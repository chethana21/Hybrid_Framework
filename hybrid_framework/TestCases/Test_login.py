from time import sleep
from PageObject.LoginPageObj import Login
from Utility.CustomLogger import custom_log
from Utility.ReadIni import ReadProperty

class Test_Login_Functionality:
    log=custom_log()
    def test_verfiy_title(self, setup):
        driver = setup
        self.log.info("Launching browser")
        if driver.title == "Your store. Login":
            self.log.info("TC::test_verfiy_title=PASSED")
            assert True
        else:
            self.log.error("TC::test_verfiy_title=FAILED")
            driver.save_screenshot(r".\ScreenShot\test_verfiy_title.png")
            assert False

    def test_verify_login(self, setup):
        driver = setup
        self.log.info("Launching browser")
        login_obj = Login(driver)
        # login_obj.ClickCheckbox()
        login_obj.SetEmail(ReadProperty.GetUser())
        login_obj.SetPassword(ReadProperty.GetPassword())
        login_obj.ClickLogin()
        self.log.info("Successfully login to the Dashbord...")
        profile = login_obj.VerifyLogin()
        if profile == "John Smith":
            login_obj.ClickLogOut()
            self.log.info("TC::test_verify_login=PASSED")
            assert True
        else:
            self.log.error("TC::test_verify_login=FAILED")
            driver.save_screenshot(r".\ScreenShot\test_verify_login.png")
            assert False



