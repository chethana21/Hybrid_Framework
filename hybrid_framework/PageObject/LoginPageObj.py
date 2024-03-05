# locators(var) and action(method)
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Login:
    id_email="Email"
    id_password="Password"
    xpath_checkbox="//input[@type='checkbox']"
    xpath_login="//button[@type='submit']"
    xpath_logout="//a[contains(text(),'Logout')]"
    xpath_profile_name = "//ul[@class='navbar-nav ml-auto pl-2']/li[2]/a"

    def __init__(self, driver):
        self.driver = driver
        self.wait_obj = WebDriverWait(driver, 10)

    def ClickCheckbox(self):
        self.wait_obj.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.ID, "cf-chl-widget-ke4bs")))
        self.driver.find_element(By.XPATH, self.xpath_checkbox).click()

    def SetEmail(self, email):
        self.driver.find_element(By.ID, self.id_email).clear()
        self.driver.find_element(By.ID, self.id_email).send_keys(email)

    def SetPassword(self, pswd):
        self.driver.find_element(By.ID, self.id_password).clear()
        self.driver.find_element(By.ID, self.id_password).send_keys(pswd)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.xpath_login).click()

    def ClickLogOut(self):
        sleep(2)
        self.driver.find_element(By.XPATH, self.xpath_logout).click()

    def VerifyLogin(self):
        try:
            self.wait_obj.until(expected_conditions.presence_of_element_located((By.XPATH, self.xpath_profile_name)))
            return self.driver.find_element(By.XPATH, self.xpath_profile_name).text
        except:
            return False