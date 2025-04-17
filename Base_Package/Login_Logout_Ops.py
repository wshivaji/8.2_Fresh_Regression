import time
import pyautogui
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from pathlib import Path
import configparser
from selenium.webdriver.common.by import By
from All_Config_Packages._1_Portal_Login_Module_Config_Files.Portal_Login_Page_Read_INI import \
    Portal_login_page_read_ini


class login(web_driver, web_logger):
    # d = web_driver.d()
    # logger = web_logger.logger_obj()

    def __init__(self):

        self.file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\0_Login_Logout_Data\\Data_From_INI\\login_logout.ini"
        self.common_test_data_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
        self.common_test_data_config = configparser.RawConfigParser()
        self.common_test_data_config.read(self.common_test_data_ini_file_path)
        print(f"INI Data File Path: {self.file_path}")
        self.config = configparser.RawConfigParser()
        self.config.read(self.file_path)
        self.cloud_url = self.common_test_data_config.get("Login_Logout_Data", "cloud_login_url")
        print(f"cloud url: {self.cloud_url}")
        self.d = None
        self.logger = web_logger.logger_obj()

    def login_to_localhost_if_not_done(self, d):
        try:
            self.d = d
            current_url = self.d.current_url

            if current_url is None or current_url == self.cloud_url:
                self.logger.info("url is not open")
                self.d.get(self.cloud_url)
                self.logger.info("opening localhost portal login")
                self.logger.info("logging in to localhost")
                username_textbox = self.d.find_element(By.XPATH, self.config.get("login_page_locators",
                                                                                 "username_textbox_by_xpath"))
                password_textbox = self.d.find_element(By.XPATH, self.config.get("login_page_locators",
                                                                                 "password_textbox_by_xpath"))
                login_btn = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "login_link_by_xpath"))
                # username_textbox.send_keys(self.config.get("user_info", "username"))
                # password_textbox.send_keys(self.config.get("user_info", "password"))
                login_btn.click()
                return self.d
            else:
                self.logger.info("Portal already logged in")

        except Exception as ex:
            self.logger.info(f"exception: {ex.args}")
            print(f"{ex.args}")

    def login_to_cloud_if_not_done(self, d):
        try:
            self.d = d
            time.sleep(web_driver.one_second)
            if self.d.current_url == Portal_login_page_read_ini().get_portal_url():
                self.logger.info(f"page url: {self.d.current_url}")
                pass
            else:
                self.d.get(Portal_login_page_read_ini().get_portal_url())
                self.d.maximize_window()
                time.sleep(web_driver.two_second)
                # self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_advance_btn_by_xpath()).click()
                # self.logger.info("clicked on advance")
                # time.sleep(web_driver.one_second)
                # self.logger.info(f"proceed link xpath: {Portal_login_page_read_ini().get_proceed_link_by_xpath()}")
                # self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_proceed_link_by_xpath()).click()
                # self.logger.info("clicked on proceed link")
                # time.sleep(web_driver.one_second)
                time.sleep(web_driver.one_second)
                for i in range(4):
                    pyautogui.hotkey('ctrl', '-')
                    time.sleep(0.5)

            # login_logo = self.d.find_element(By.XPATH, "//img[@id='login-logo']").is_displayed()
            # if not login_logo.is_displayed():
            #     self.d.get(Portal_login_page_read_ini().get_portal_url())

            login_btn = self.d.find_elements(By.XPATH, self.config.get("login_page_locators", "login_link_by_xpath"))
            current_url = self.d.current_url
            self.logger.info(f"current url: {current_url}")

            if current_url is None or len(login_btn) > 0:
                print("current url", current_url)
                self.logger.info("url is not open")
                self.d.get(self.cloud_url)
                self.d.maximize_window()
                self.logger.info("opening localhost portal login")
                self.logger.info("logging in to core")
                self.implicit_wait(web_driver.one_second, self.d)
                print(f"portal login page title: {self.d.title}")
                # username_textbox = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "username_textbox_by_xpath"))
                username_textbox = web_driver.explicit_wait(self, 10, "XPATH", self.config.get("login_page_locators", "username_textbox_by_xpath"), self.d)
                password_textbox = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "password_textbox_by_xpath"))
                login_btn = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "login_link_by_xpath"))
                self.implicit_wait(web_driver.one_second, self.d)
                # self.logger.info(f"username: {username_textbox}")
                # self.logger.info(f"password: {password_textbox}")
                if username_textbox != None:
                    if username_textbox.text == "":
                        username_textbox.send_keys(self.config.get("user_info", "username"))
                        time.sleep(web_driver.one_second)
                self.implicit_wait(web_driver.one_second, self.d)
                if password_textbox != None:
                    if password_textbox.text == "":
                        password_textbox.send_keys(self.config.get("user_info", "password"))
                        time.sleep(web_driver.one_second)
                self.implicit_wait(web_driver.one_second, self.d)
                login_btn.click()
                self.implicit_wait(web_driver.one_second, self.d)
                # logout_btn = self.d.find_element(By.XPATH, self.config.get("logout_locators", "logout_btn_by_xpath"))
                logout_btn = web_driver.explicit_wait(self, 10, "XPATH", self.config.get("logout_locators", "logout_btn_by_xpath"), self.d)

                time.sleep(web_driver.two_second)
                if logout_btn.is_displayed():
                    self.logger.info("login success..")
                else:
                    self.logger.info("login unsuccessful.. please check code.")
                    self.d.save_screenshot(f"{web_driver.screenshots_path}\\login_failed.png")
                time.sleep(web_driver.two_second)
            else:
                print("portal logged in")
                self.logger.info("Portal already logged in")
                time.sleep(web_driver.two_second)

            return self.d
        except Exception as ex:
            self.logger.info(f"exception: {ex.args}")
            self.d.save_screenshot(f"{web_driver.screenshots_path}\\login_exception.png")
            print(f"{ex.args}")

    def login_to_cloud_if_not_done_2fa(self, d):
        try:
            self.d = d
            time.sleep(web_driver.one_second)
            if self.d.current_url == Portal_login_page_read_ini().get_portal_url():
                self.logger.info(f"page url: {self.d.current_url}")
                pass
            else:
                self.d.get(Portal_login_page_read_ini().get_portal_url())
                self.d.maximize_window()
                time.sleep(web_driver.two_second)
                # self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_advance_btn_by_xpath()).click()
                # self.logger.info("clicked on advance")
                # time.sleep(web_driver.one_second)
                # self.logger.info(f"proceed link xpath: {Portal_login_page_read_ini().get_proceed_link_by_xpath()}")
                # self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_proceed_link_by_xpath()).click()
                # self.logger.info("clicked on proceed link")
                # time.sleep(web_driver.one_second)
                time.sleep(web_driver.one_second)
                for i in range(4):
                    pyautogui.hotkey('ctrl', '-')
                    time.sleep(0.5)

            # login_logo = self.d.find_element(By.XPATH, "//img[@id='login-logo']").is_displayed()
            # if not login_logo.is_displayed():
            #     self.d.get(Portal_login_page_read_ini().get_portal_url())

            login_btn = self.d.find_elements(By.XPATH, self.config.get("login_page_locators", "login_link_by_xpath"))
            current_url = self.d.current_url
            self.logger.info(f"current url: {current_url}")

            if current_url is None or len(login_btn) > 0:
                print("current url", current_url)
                self.logger.info("url is not open")
                self.d.get(self.cloud_url)
                self.d.maximize_window()
                self.logger.info("opening localhost portal login")
                self.logger.info("logging in to core")
                self.implicit_wait(web_driver.one_second, self.d)
                print(f"portal login page title: {self.d.title}")
                # username_textbox = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "username_textbox_by_xpath"))
                username_textbox = web_driver.explicit_wait(self, 10, "XPATH", self.config.get("login_page_locators", "username_textbox_by_xpath"), self.d)
                password_textbox = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "password_textbox_by_xpath"))
                login_btn = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "login_link_by_xpath"))
                self.implicit_wait(web_driver.one_second, self.d)
                # self.logger.info(f"username: {username_textbox}")
                # self.logger.info(f"password: {password_textbox}")
                if username_textbox != None:
                    if username_textbox.text == "":
                        username_textbox.send_keys(self.config.get("user_info", "2fa_username"))
                        time.sleep(web_driver.one_second)
                self.implicit_wait(web_driver.one_second, self.d)
                if password_textbox != None:
                    if password_textbox.text == "":
                        password_textbox.send_keys(self.config.get("user_info", "password"))
                        time.sleep(web_driver.one_second)
                self.implicit_wait(web_driver.one_second, self.d)
                login_btn.click()
                self.implicit_wait(web_driver.one_second, self.d)
                # logout_btn = self.d.find_element(By.XPATH, self.config.get("logout_locators", "logout_btn_by_xpath"))
                logout_btn = web_driver.explicit_wait(self, 10, "XPATH", self.config.get("logout_locators", "logout_btn_by_xpath"), self.d)

                time.sleep(web_driver.two_second)
                if logout_btn.is_displayed():
                    self.logger.info("login success..")
                else:
                    self.logger.info("login unsuccessful.. please check code.")
                    self.d.save_screenshot(f"{web_driver.screenshots_path}\\login_failed.png")
                time.sleep(web_driver.two_second)
            else:
                print("portal logged in")
                self.logger.info("Portal already logged in")
                time.sleep(web_driver.two_second)
            return self.d
        except Exception as ex:
            self.logger.info(f"exception: {ex.args}")
            self.d.save_screenshot(f"{web_driver.screenshots_path}\\login_exception.png")
            print(f"{ex.args}")

    def login_to_cloud_if_not_done_with_edge_user(self, d):
        try:
            self.d = d
            time.sleep(web_driver.one_second)
            if self.d.current_url == Portal_login_page_read_ini().get_portal_url():
                self.logger.info(f"page url: {self.d.current_url}")
                pass
            else:
                self.d.get(Portal_login_page_read_ini().get_portal_url())
                self.d.maximize_window()
                time.sleep(web_driver.one_second)
                self.d.execute_script("document.body.style.zoom = '70%'")
                # for i in range(4):
                #     pyautogui.hotkey('ctrl', '-')
                #     time.sleep(0.5)

            current_url = self.d.current_url
            login_btn = self.d.find_elements(By.XPATH, self.config.get("login_page_locators", "login_link_by_xpath"))
            self.logger.info(f"current url: {current_url}")

            if current_url is None or len(login_btn) > 0:
                print("current url", current_url)
                self.logger.info("url is not open")
                self.d.get(self.cloud_url)
                self.d.maximize_window()

                self.logger.info("opening localhost portal login")
                self.logger.info("logging in to core")
                self.implicit_wait(web_driver.one_second, self.d)
                print(f"portal login page title: {self.d.title}")
                # username_textbox = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "username_textbox_by_xpath"))
                username_textbox = web_driver.explicit_wait(self, 10, "XPATH", self.config.get("login_page_locators", "username_textbox_by_xpath"), self.d)
                password_textbox = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "password_textbox_by_xpath"))
                login_btn = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "login_link_by_xpath"))
                self.implicit_wait(web_driver.one_second, self.d)
                if username_textbox.text == "":
                    username_textbox.send_keys(self.config.get("user_info", "edge_username"))
                self.implicit_wait(web_driver.one_second, self.d)
                if password_textbox.text == "":
                    password_textbox.send_keys(self.config.get("user_info", "password"))
                self.implicit_wait(web_driver.one_second, self.d)
                login_btn.click()
                self.implicit_wait(web_driver.one_second, self.d)
                # logout_btn = self.d.find_element(By.XPATH, self.config.get("logout_locators", "logout_btn_by_xpath"))
                logout_btn = web_driver.explicit_wait(self, 10, "XPATH", self.config.get("logout_locators", "logout_btn_by_xpath"), self.d)

                time.sleep(web_driver.two_second)
                if logout_btn.is_displayed():
                    self.logger.info("login success..")
                else:
                    self.logger.info("login unsuccessful.. please check code.")
                    self.d.save_screenshot(f"{web_driver.screenshots_path}\\login_failed.png")
                time.sleep(web_driver.two_second)
            else:
                print("portal logged in")
                self.logger.info("Portal already logged in")
                time.sleep(web_driver.two_second)
            return self.d
        except Exception as ex:
            self.logger.info(f"exception: {ex.args}")
            self.d.save_screenshot(f"{web_driver.screenshots_path}\\login_exception.png")
            print(f"{ex.args}")

    def login_action(self):
        # username_textbox = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "username_textbox_by_xpath"))
        username_textbox = web_driver.explicit_wait(self, 10, "XPATH", self.config.get("login_page_locators", "username_textbox_by_xpath"), self.d)
        password_textbox = self.d.find_element(By.XPATH,
                                               self.config.get("login_page_locators", "password_textbox_by_xpath"))
        login_btn = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "login_link_by_xpath"))
        self.implicit_wait(web_driver.one_second, self.d)
        if username_textbox.text == "":
            username_textbox.send_keys(self.config.get("user_info", "username"))
        self.implicit_wait(web_driver.one_second, self.d)
        if password_textbox.text == "":
            password_textbox.send_keys(self.config.get("user_info", "password"))
        self.implicit_wait(web_driver.one_second, self.d)
        login_btn.click()
        self.implicit_wait(web_driver.one_second, self.d)
        # logout_btn = self.d.find_element(By.XPATH, self.config.get("logout_locators", "logout_btn_by_xpath"))
        logout_btn = web_driver.explicit_wait(self, 10, "XPATH", self.config.get("logout_locators", "logout_btn_by_xpath"), self.d)
        time.sleep(web_driver.one_second)
        if logout_btn.is_displayed():
            self.logger.info("login success..")
        else:
            self.logger.info("login unsuccessful.. please check code.")
            self.d.save_screenshot(f"{web_driver.screenshots_path}\\login_failed.png")
        time.sleep(web_driver.two_second)

    def login_to_facecirst_portal_if_not_done(self, d):
        try:
            self.d = d
            time.sleep(web_driver.one_second)
            # print(f"current url: {self.d.current_url}")
            # print(f"expected url: {Portal_login_page_read_ini().get_portal_url()}")
            logout_btn = cloud_menu_btn = None
            try:
                # self.d.refresh()
                logout_btn = web_driver.explicit_wait(self, 3, "XPATH", self.config.get("logout_locators", "logout_btn_by_xpath"), self.d)
                cloud_menu_btn = web_driver.explicit_wait(self, 5, "XPATH", self.config.get("logout_locators", "cloud_or_local_menu_by_xpath"), self.d)
            except Exception as ex:
                print(ex.args)
            if cloud_menu_btn:
                print(f"logout btn visible: {cloud_menu_btn.is_displayed()}")
            else:
                if self.d.current_url == Portal_login_page_read_ini().get_portal_url():
                    print(f"page url: {self.d.current_url}")
                else:
                    self.d.get(Portal_login_page_read_ini().get_portal_url())
                    self.d.maximize_window()
                    time.sleep(web_driver.two_second)
                    # self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_advance_btn_by_xpath()).click()
                    # self.logger.info("clicked on advance")
                    # time.sleep(web_driver.one_second)
                    # self.logger.info(f"proceed link xpath: {Portal_login_page_read_ini().get_proceed_link_by_xpath()}")
                    # self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_proceed_link_by_xpath()).click()
                    # self.logger.info("clicked on proceed link")
                    # time.sleep(web_driver.one_second)
                    time.sleep(web_driver.one_second)
                    for i in range(4):
                        pyautogui.hotkey('ctrl', '-')
                        time.sleep(0.5)
                    username_textbox = web_driver.explicit_wait(self, 10, "XPATH", self.config.get("login_page_locators",
                                                                                                   "username_textbox_by_xpath"),
                                                                self.d)
                    password_textbox = self.d.find_element(By.XPATH,
                                                           self.config.get("login_page_locators",
                                                                           "password_textbox_by_xpath"))
                    login_btn = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "login_link_by_xpath"))
                    self.implicit_wait(web_driver.one_second, self.d)
                    if username_textbox.text == "":
                        username_textbox.send_keys(self.config.get("user_info", "username"))
                    self.implicit_wait(web_driver.one_second, self.d)
                    if password_textbox.text == "":
                        password_textbox.send_keys(self.config.get("user_info", "password"))
                    self.implicit_wait(web_driver.one_second, self.d)
                    login_btn.click()
                    self.implicit_wait(web_driver.one_second, self.d)
                    # logout_btn = self.d.find_element(By.XPATH, self.config.get("logout_locators", "logout_btn_by_xpath"))
                    logout_btn = web_driver.explicit_wait(self, 10, "XPATH", self.config.get("logout_locators", "logout_btn_by_xpath"), self.d)
                    time.sleep(web_driver.one_second)
                    if logout_btn.is_displayed():
                        self.logger.info("login success..")
                    else:
                        self.logger.info("login unsuccessful.. please check code.")
                        self.d.save_screenshot(f"{web_driver.screenshots_path}\\login_failed.png")
                    time.sleep(web_driver.two_second)

            return self.d
        except Exception as ex:
            self.logger.info(f"exception: {ex.args}")
            self.logger.info(f"exception message: {ex}")
            self.d.save_screenshot(f"{web_driver.screenshots_path}\\login_exception.png")
            print(f"{ex.args}")

    def login_to_cloud_if_not_done_with_user_credentials(self, d, username, password):
        try:
            self.d = d
            time.sleep(web_driver.one_second)
            if self.d.current_url == Portal_login_page_read_ini().get_portal_url():
                self.logger.info(f"page url: {self.d.current_url}")
                pass
            else:
                self.d.get(Portal_login_page_read_ini().get_portal_url())
                self.d.maximize_window()
                time.sleep(web_driver.two_second)
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_advance_btn_by_xpath()).click()
                self.logger.info("clicked on advance")
                time.sleep(web_driver.one_second)
                self.logger.info(f"proceed link xpath: {Portal_login_page_read_ini().get_proceed_link_by_xpath()}")
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_proceed_link_by_xpath()).click()
                self.logger.info("clicked on proceed link")
                time.sleep(web_driver.one_second)
                time.sleep(web_driver.one_second)
                for i in range(4):
                    pyautogui.hotkey('ctrl', '-')
                    time.sleep(0.5)
            login_btn = self.d.find_elements(By.XPATH, self.config.get("login_page_locators", "login_link_by_xpath"))
            current_url = self.d.current_url
            self.logger.info(f"current url: {current_url}")

            if current_url is None or len(login_btn) > 0:
                print("current url", current_url)
                self.logger.info("url is not open")
                self.d.get(self.cloud_url)
                self.d.maximize_window()
                self.logger.info("opening localhost portal login")
                self.logger.info("logging in to core")
                self.implicit_wait(web_driver.one_second, self.d)
                print(f"portal login page title: {self.d.title}")
                # username_textbox = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "username_textbox_by_xpath"))
                username_textbox = web_driver.explicit_wait(self, 10, "XPATH", self.config.get("login_page_locators", "username_textbox_by_xpath"), self.d)
                password_textbox = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "password_textbox_by_xpath"))
                login_btn = self.d.find_element(By.XPATH, self.config.get("login_page_locators", "login_link_by_xpath"))
                self.implicit_wait(web_driver.one_second, self.d)
                # self.logger.info(f"username: {username_textbox}")
                # self.logger.info(f"password: {password_textbox}")
                if username_textbox != None:
                    if username_textbox.text == "":
                        # username_textbox.send_keys(self.config.get("user_info", "username"))
                        username_textbox.send_keys(username)
                        time.sleep(web_driver.one_second)
                self.implicit_wait(web_driver.one_second, self.d)
                if password_textbox != None:
                    if password_textbox.text == "":
                        # password_textbox.send_keys(self.config.get("user_info", "password"))
                        password_textbox.send_keys(password)
                        time.sleep(web_driver.one_second)
                self.implicit_wait(web_driver.one_second, self.d)
                login_btn.click()
                self.implicit_wait(web_driver.one_second, self.d)
                # logout_btn = self.d.find_element(By.XPATH, self.config.get("logout_locators", "logout_btn_by_xpath"))
                logout_btn = web_driver.explicit_wait(self, 10, "XPATH", self.config.get("logout_locators", "logout_btn_by_xpath"), self.d)

                time.sleep(web_driver.two_second)
                if logout_btn.is_displayed():
                    self.logger.info("login success..")
                else:
                    self.logger.info("login unsuccessful.. please check code.")
                    self.d.save_screenshot(f"{web_driver.screenshots_path}\\login_failed.png")
                time.sleep(web_driver.two_second)
            else:
                print("portal logged in")
                self.logger.info("Portal already logged in")
                time.sleep(web_driver.two_second)
            return self.d
        except Exception as ex:
            self.logger.info(f"exception: {ex.args}")
            self.d.save_screenshot(f"{web_driver.screenshots_path}\\login_exception.png")
            print(f"{ex.args}")

    def accept_terms_and_conditions_for_login_for_new_user(self):
        try:
            agree_and_continue_btn = self.d.find_element(By.XPATH, Portal_login_page_read_ini().accept_user_policy())
            agree_and_continue_btn.click()
            # agree_and_continue_btn = self.explicit_wait(10, "XPATH", "//body/div[@id=\"login-screen\"]//div[@class=\"ng-modal\"]/div[@class=\"ng-modal-dialog\"]/div/div/div[@class=\"modal-button-container fltlft posrel clrbth\"]/button[@ng-click=\"handleAUPModalAgree()\"]", self.d)
            self.logger.info(f"agree and continue btn visible: {agree_and_continue_btn.is_displayed()}")
            # if agree_and_continue_btn.is_displayed():
            #     agree_and_continue_btn.click()
            #     time.sleep(web_driver.one_second)
            #     self.logger.info(f"agree and continue btn clicked.")
            # else:
            #     self.logger.info(f"agree and continue btn not visible")
        except Exception as ex:
            self.logger.info(f"except: {ex.args}")

    def login_with_persona_user(self, d, user):
        try:
            self.d = d
            time.sleep(web_driver.one_second)
            if self.d.current_url == Portal_login_page_read_ini().get_portal_url():
                self.logger.info(f"page url: {self.d.current_url}")
                pass
            else:
                self.d.get(Portal_login_page_read_ini().get_portal_url())
                self.d.maximize_window()
                time.sleep(web_driver.one_second)

                for i in range(5):
                    pyautogui.hotkey('ctrl', '-')
                    time.sleep(0.5)

            login_btn = self.d.find_elements(By.XPATH, self.config.get("login_page_locators", "login_link_by_xpath"))
            current_url = self.d.current_url
            self.logger.info(f"current url: {current_url}")

            if current_url is None or len(login_btn) > 0:
                print("current url", current_url)
                self.logger.info("url is not open")
                self.d.get(self.cloud_url)
                self.d.maximize_window()
                self.logger.info("opening localhost portal login")
                self.logger.info("logging in to core")
                self.implicit_wait(web_driver.one_second, self.d)
                print(f"portal login page title: {self.d.title}")
                username_textbox = web_driver.explicit_wait(self, 10, "XPATH",
                                                            self.config.get("login_page_locators",
                                                                            "username_textbox_by_xpath"), self.d)
                password_textbox = self.d.find_element(By.XPATH, self.config.get("login_page_locators",
                                                                                 "password_textbox_by_xpath"))
                login_btn = self.d.find_element(By.XPATH,
                                                self.config.get("login_page_locators", "login_link_by_xpath"))
                self.implicit_wait(web_driver.one_second, self.d)
                if username_textbox != None:
                    if username_textbox.text == "":
                        username_textbox.send_keys(user)
                        time.sleep(web_driver.one_second)
                self.implicit_wait(web_driver.one_second, self.d)
                if password_textbox != None:
                    if password_textbox.text == "":
                        password_textbox.send_keys(self.config.get("user_info", "password"))
                        time.sleep(web_driver.one_second)
                self.implicit_wait(web_driver.one_second, self.d)
                login_btn.click()
                self.implicit_wait(web_driver.one_second, self.d)

                # login().accept_terms_and_conditions_for_login_for_new_user(self.d)
                # logout_btn = web_driver.explicit_wait(self, 10, "XPATH",
                #                                       self.config.get("logout_locators", "logout_btn_by_xpath"),
                #                                       self.d)
                #
                # time.sleep(web_driver.two_second)
                # if logout_btn.is_displayed():
                #     self.logger.info(f"******* Login with {user} user success *********")
                # else:
                #     self.logger.info("login unsuccessful.. please check code.")
                #     self.d.save_screenshot(f"{web_driver.screenshots_path}\\login_failed.png")
                # time.sleep(web_driver.two_second)
            # else:
            #     print("portal logged in")
            #     logout_btn = web_driver.explicit_wait(self, 10, "XPATH",
            #                                           self.config.get("logout_locators", "logout_btn_by_xpath"), self.d)
            #     time.sleep(web_driver.one_second)
            #     if logout_btn.is_displayed():
            #         self.logger.info("Someone already logged in..")
            #         logout_btn.click()
            #     else:
            #         self.logger.info("Unable to click logout")
            #     time.sleep(web_driver.two_second)
            return self.d
        except Exception as ex:
            self.logger.info(f"exception: {ex.args}")
            self.d.save_screenshot(f"{web_driver.screenshots_path}\\login_exception.png")
            print(f"{ex.args}")

class logout(web_driver, web_logger):
    def __init__(self):
        self.file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\0_Login_Logout_Data\\Data_From_INI\\login_logout.ini"
        print(f"INI Data File Path: {self.file_path}")
        self.config = configparser.RawConfigParser()
        self.config.read(self.file_path)
        self.local_url = self.config.get("login_urls", "local_login_url")
        self.cloud_url = self.config.get("login_urls", "cloud_login_url")
        # print(f"local url: {self.local_url}")
        # print(f"cloud url: {self.cloud_url}")
        self.d = web_driver.d()
        self.logger = web_logger.logger_obj()

    def logout_from_core(self, d):
        try:
            self.d = d
            time.sleep(web_driver.one_second)
            current_url = self.d.current_url
            if current_url == self.config.get("login_urls", "cloud_login_url"):
                self.logger.info(f"current url: {current_url}")
                self.logger.info(f"actual url: {self.config.get('login_urls', 'cloud_login_url')}")
                # cloud_menu_btn = self.d.find_element(By.XPATH, self.config.get("logout_locators", "cloud_or_local_menu_by_xpath"))
                cloud_menu_btn = web_driver.explicit_wait(self, 10, "XPATH", self.config.get("logout_locators", "cloud_or_local_menu_by_xpath"), self.d)
                cloud_menu_btn.click()
                close_all_submenu_list = self.d.find_elements(By.XPATH, self.config.get("logout_locators", "close_all_panels_menu_by_xpath"))
                full_dashboard = self.d.find_element(By.XPATH, self.config.get("logout_locators",
                                                                                        "full_dashboard_by_xpath"))
                self.logger.info(f"close all btn object count: {len(close_all_submenu_list)}")
                if len(close_all_submenu_list) > 0:
                    close_all_submenu_list[0].click()
                else:
                    # logout_btn = self.d.find_element(By.XPATH, self.config.get("logout_locators", "logout_btn_by_xpath"))
                    logout_btn = web_driver.explicit_wait(self, 10, "XPATH", self.config.get("logout_locators", "logout_btn_by_xpath"), self.d)
                    logout_btn.click()
                if not full_dashboard.is_displayed():
                    time.sleep(web_driver.one_second)
                    logout_btn = self.d.find_element(By.XPATH,
                                                     self.config.get("logout_locators", "logout_btn_by_xpath"))
                    logout_btn.click()
            else:
                print(f"wrong url detected: {current_url}")
                self.logger.info(f"wrong url detected: {current_url}")
                self.d.save_screenshot(f"{web_driver.screenshots_path}\\logout_failed.png")
        except Exception as ex:
            self.logger.info(f"logout exception: {ex.args}")
            self.d.save_screenshot(f"{web_driver.screenshots_path}\\logout_exception.png")
            print(ex.args)


# login().login_to_localhost_if_not_done()
# login().login_to_cloud_if_not_done()
# login().logout_from_core()
