import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Base_Package.Web_Logger import web_logger


class web_driver:
    logger = web_logger.logger_obj()
    _d = None
    one_second = 1
    two_second = 2
    three_second = 3
    screenshots_path = f"{Path(__file__).parent.parent}\\Reports\\Screenshots"

    @classmethod
    def d(cls):
        if cls._d is None:
            print("creating new Driver object")
            cls._d = cls.driver_init()
            return cls._d
        else:
            return cls._d

    @staticmethod
    def driver_init():
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            d = webdriver.Chrome(options=chrome_options)
            # d_edge = webdriver.Edge()
            # d_firefox = webdriver.Firefox()
            return d
        except Exception as ex:
            print("init constructor in base class has an err: ", ex)

    def implicit_wait(self, seconds, driver):
        driver.implicitly_wait(seconds)

    """set Explicit wait function to be used by all the web elements where ever it is needed"""

    def explicit_wait(self, seconds, locator_type, locator, driver):
        try:
            self.logger.info(f"entered explicit wait for {seconds}")
            self.logger.info(f"looking for locator: {locator} ")
            element = None
            if locator_type == "NAME":
                element = WebDriverWait(driver, seconds).until(EC.visibility_of_element_located((By.NAME, locator)))
            if locator_type == "ID":
                element = WebDriverWait(driver, seconds).until(EC.visibility_of_element_located((By.ID, locator)))
            if locator_type == "XPATH":
                element = WebDriverWait(driver, seconds).until(EC.visibility_of_element_located((By.XPATH, locator)))
            self.logger.info(f"exiting explicit wait..")
            return element
        except Exception as ex:
            print(f"element not found: {locator}")
            self.logger.info(f"element not found: {locator}")
            # self.logger.info(f"ex: {ex.args}")

    def explicit_wait_for_element_not_interactable(self, seconds, locator_type, locator, driver):
        try:
            self.logger.info(f"entered explicit wait for {seconds}")
            element = None
            if locator_type == "ID":
                element = WebDriverWait(driver, seconds).until(EC.element_to_be_clickable((By.ID, locator)))
            if locator_type == "XPATH":
                element = WebDriverWait(driver, seconds).until(EC.element_to_be_clickable((By.XPATH, locator)))
            self.logger.info(f"exiting explicit wait..")
            return element
        except Exception as ex:
            print(f"element not found: {locator}")
            self.logger.info(f"element not found: {locator}")
            # self.logger.info(f"ex: {ex.args}")


    def explicit_wait_for_stale_element(self, seconds, locator_type, locator, driver):
        try:
            self.logger.info(f"entered explicit wait for {seconds}")
            element = None
            if locator_type == "ID":
                element = WebDriverWait(driver, seconds).until(EC.element_to_be_clickable((By.ID, locator)))
            if locator_type == "XPATH":
                element = WebDriverWait(driver, seconds).until(EC.element_to_be_clickable((By.XPATH, locator)))
            self.logger.info(f"exiting explicit wait..")
            return element
        except Exception as ex:
            print(f"element not found: {locator}")
            self.logger.info(f"element not found: {locator}")
            # self.logger.info(f"ex: {ex.args}")

    @staticmethod
    @pytest.fixture(scope="function")
    def setup_method(self):
        try:
            print("\nsetup start")
            print("setup function exe")
            d = webdriver.d
            d.maximize_window()
            d.set_page_load_timeout(50)
            d.set_script_timeout(30)
            d.implicitly_wait(30)
            print("\nsetup end")
        except Exception as ex:
            print("\nException in Test_Deployment_Manager_Test_Cases/setup_method: ", ex)
