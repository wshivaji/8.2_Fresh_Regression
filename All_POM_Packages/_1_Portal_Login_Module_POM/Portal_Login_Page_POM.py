import time
from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait

from All_Config_Packages._1_Portal_Login_Module_Config_Files.Portal_Login_Page_Read_INI import Portal_login_page_read_ini
from Base_Package.Login_Logout_Ops import login
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from selenium.webdriver.support import expected_conditions as EC


class Portal_Login_Page_Pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    def wait_for_element_to_appear(self, element_list, xpath):
        count = 0
        if len(element_list) == 0:
            while len(element_list) == 0 or count == 10:
                element_list = self.d.find_elements(By.XPATH, xpath)
                time.sleep(web_driver.one_second)
                if len(element_list) > 0:
                    self.logger.info("element is visible...")
                    return element_list[0]
                else:
                    self.logger.info("waiting for element...")
                count += 1
                self.logger.info(f"wait count: {count}")
        else:
            self.logger.info(f"element length: {len(element_list)}")
            return element_list[0]

    def open_portal_url_and_verify_expected_url_is_visible_verify_expected_page_title_is_visible_and_verify_face_first_logo_is_visible(self):

        try:
            self.logger.info("********** TC_Portal_Login_01 started ********")
            self.logger.info("open_portal_url_and_verify_expected_url_is_visible_verify_expected_page_title_is_visible_and_verify_face_first_logo_is_visible")
            print(f"open_portal_url_and_verify_expected_url_is_visible_verify_expected_page_title_is_visible_and_verify_face_first_logo_is_visible")
            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            actual_url = self.d.current_url
            self.logger.info(f"actual url: {actual_url}")
            expected_url = Portal_login_page_read_ini().get_portal_url()
            self.logger.info(f"expected Portal url: {expected_url}")
            time.sleep(web_driver.one_second)
            if actual_url == expected_url:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_title = self.d.title
            self.logger.info(f"actual title: {actual_title}")
            time.sleep(web_driver.one_second)
            expected_title = Portal_login_page_read_ini().get_portal_title()
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)

            if self.explicit_wait(10, "XPATH", Portal_login_page_read_ini().get_face_first_company_logo_by_xpath(), self.d). \
                    is_displayed():
                self.logger.info(f"logo image is visible: ")
                self.status.append(True)
            else:
                self.logger.error(f"logo image is not visible: ")
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_01.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_01.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_01_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_01_exception.png")
            self.logger.error(f"TC_Portal_Login_01 got exception as: {ex}")

    def verify_username_textbox_is_visible_and_clickable_username_label_on_it_is_visible(self):
        try:
            self.logger.info("********** TC_Portal_Login_02 started ********")
            self.logger.info("verify_username_textbox_is_visible_and_clickable_username_label_on_it_is_visible")
            print("verify_username_textbox_is_visible_and_clickable_username_label_on_it_is_visible")
            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            username_textbox = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                   get_portal_login_username_textbox_by_xpath())
            time.sleep(web_driver.one_second)
            if username_textbox.is_displayed():
                self.logger.info("Username text box is visible.....")
                self.status.append(True)
            else:
                self.status.append(False)
            if username_textbox.is_enabled():
                self.logger.info("Username text box is clickable.....")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_username_label = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                        get_portal_login_username_textbox_by_xpath()). \
                get_attribute("placeholder")
            self.logger.info(f"actual username label: {actual_username_label}")
            expected_username_label = Portal_login_page_read_ini().get_portal_username_label_on_username_textbox()
            self.logger.info(f"expected label is : {expected_username_label}")
            time.sleep(web_driver.one_second)
            if actual_username_label == expected_username_label:
                self.status.append(True)
            else:
                self.status.append(False)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_02.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_02.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_02_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_02_exception.png")
            self.logger.error(f"TC_Portal_Login_02 got an exception as: {ex}")

    def verify_password_textbox_is_visible_and_clickable_password_label_on_it_is_visible(self):
        try:
            self.logger.info("********** TC_Portal_Login_03 started ********")
            self.logger.info(f"verify_password_textbox_is_visible_and_clickable_password_label_on_it_is_visible")
            print(f"verify_password_textbox_is_visible_and_clickable_password_label_on_it_is_visible")
            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()

            password_textbox = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                   get_portal_login_password_textbox_by_xpath())
            time.sleep(web_driver.one_second)
            if password_textbox.is_displayed():
                self.logger.info("Password textbox is visible.....")
                self.status.append(True)
            else:
                self.status.append(False)
            if password_textbox.is_enabled():
                self.logger.info("Password textbox is clickable.....")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_password_label = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                        get_portal_login_password_textbox_by_xpath()). \
                get_attribute("placeholder")
            self.logger.info(f"actual password label: {actual_password_label}")
            expected_password_label = Portal_login_page_read_ini().get_portal_password_label_on_password_textbox()
            self.logger.info(f"expected password label: {expected_password_label}")
            time.sleep(web_driver.one_second)
            if actual_password_label == expected_password_label:
                self.status.append(True)
            else:
                self.status.append(False)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_03.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_03.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_03_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_03_exception.png")
            self.logger.error(f"TC_Portal_Login_03 got an exception as: {ex}")

    def verify_cloud_login_button_is_visible_and_clickable_cloud_login_text_on_it_is_visible_click_on_cloud_login_and_verify_missing_username_msg_is_visible(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_04 started ********")
            self.logger.info("verify_cloud_login_button_is_visible_and_clickable_cloud_login_text_on_it_is_visible_click_on_cloud_login_and_verify_missing_username_msg_is_visible")
            print("verify_cloud_login_button_is_visible_and_clickable_cloud_login_text_on_it_is_visible_click_on_cloud_login_and_verify_missing_username_msg_is_visible")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            cloud_login_button = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            if cloud_login_button.is_displayed():
                self.logger.info("Cloud Login button is visible.....")
                self.status.append(True)
            else:
                self.status.append(False)
            if cloud_login_button.is_enabled():
                self.logger.info("Cloud Login button is clickable.....")
                self.status.append(True)
            else:
                self.status.append(False)
            # actual_cloud_text_on_button = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_cloud_text_on_cloud_login_button_by_xpath()).text
            # self.logger.info(f"actual cloud text: {actual_cloud_text_on_button}")
            # expected_cloud_text_on_button = Portal_login_page_read_ini().get_expected_cloud_text_on_button()
            # self.logger.info(f"expected text: {expected_cloud_text_on_button}")
            # if actual_cloud_text_on_button == expected_cloud_text_on_button:
            #     self.status.append(True)
            # else:
            #     self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_login_text_on_button = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                              get_login_text_on_cloud_login_button_by_xpath()).text
            self.logger.info(f"actual login text: {actual_login_text_on_button}")
            expected_login_text_on_button = Portal_login_page_read_ini().get_expected_login_text_on_button()
            self.logger.info(f"expected login text: {expected_login_text_on_button}")
            if actual_login_text_on_button == expected_login_text_on_button:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath()).click()
            self.logger.info("clicked on CLOUD LOGIN button.....")
            time.sleep(web_driver.one_second)
            missing_username_text_on_alert = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_missing_username_text_on_error_alert_by_xpath())
            if missing_username_text_on_alert.is_displayed():
                self.logger.info("Missing username message is visible.....")
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_close_missing_username_alert_by_xpath()).click()
                self.status.append(True)
            else:
                self.status.append(False)
            # logout().logout_from_core()

            self.logger.info(f"status: {self.status}")

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_04.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_04.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_04_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_04_exception.png")
            self.logger.error(f"TC_Portal_Login_04 got an exception as: {ex}")

    def verify_events_button_is_visible_and_clickable_text_and_exclamatory_icon_on_it_both_are_visible_click_on_events_and_verify_missing_username_msg_is_visible(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_05 started ********")
            self.logger.info("verify_events_button_is_visible_and_clickable_text_and_exclamatory_icon_on_it_both_are_visible_click_on_events_and_verify_missing_username_msg_is_visible")
            print("verify_events_button_is_visible_and_clickable_text_and_exclamatory_icon_on_it_both_are_visible_click_on_events_and_verify_missing_username_msg_is_visible")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events_button = self.explicit_wait(10, "XPATH", Portal_login_page_read_ini()
                                               .get_events_button_on_portal_by_xpath(), self.d)
            if events_button.is_displayed():
                self.logger.info("Events button is visible.....")
                self.status.append(True)
            else:
                self.status.append(False)
            if events_button.is_enabled():
                self.logger.info("Events button is clickable.....")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text_on_events_button = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                               get_events_text_on_events_button_by_xpath()).text
            self.logger.info(f"actual text on events button: {actual_text_on_events_button}")
            expected_text_on_events_button = Portal_login_page_read_ini().get_expected_text_events_on_button()
            self.logger.info(f"expected text on Events button: {expected_text_on_events_button}")
            if actual_text_on_events_button == expected_text_on_events_button:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_events_button_on_portal_by_xpath()).click()
            self.logger.info("Events button is clicked....")
            time.sleep(web_driver.one_second)
            missing_username_text_on_alert = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                                 get_missing_username_text_on_error_alert_by_xpath())
            if missing_username_text_on_alert.is_displayed():
                self.logger.info("Missing Username message is visible.....")
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                    get_close_missing_username_alert_by_xpath()).click()
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            exclamatory_icon = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                   get_exclamation_mark_icon_on_events_button_by_xpath())
            if exclamatory_icon.is_displayed():
                self.logger.info("Exclamatory icon on button is visible.....")
                self.status.append(True)
            else:
                self.status.append(False)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_05.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_05.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_05_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_05_exception.png")
            self.logger.error(f"TC_Portal_Login_05 got an exception as: {ex}")

    def verify_identify_enroll_button_is_visible_and_clickable_text_and_camera_icon_on_it_both_are_visible_click_on_identify_enroll_and_verify_missing_username_mgs_is_visible(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_06 started ********")
            self.logger.info("verify_identify_enroll_button_is_visible_and_clickable_text_and_camera_icon_on_it_both_are_visible_click_on_identify_enroll_and_verify_missing_username_mgs_is_visible")
            print("verify_identify_enroll_button_is_visible_and_clickable_text_and_camera_icon_on_it_both_are_visible_click_on_identify_enroll_and_verify_missing_username_mgs_is_visible")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            identify_enroll_button = self.explicit_wait(10, "XPATH", Portal_login_page_read_ini().
                                                         get_identify_enroll_button_by_xpath(), self.d)
            if identify_enroll_button.is_displayed():
                self.logger.info("Identify & Enroll button is visible.....")
                self.status.append(True)
            else:
                self.status.append(False)
            if identify_enroll_button.is_enabled():
                self.logger.info("Identify & Enroll button is clickable.....")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text_on_identify_enroll_button = self.d.find_element(
                By.XPATH, Portal_login_page_read_ini().get_identify_enroll_text_on_identify_enroll_button_by_xpath()). \
                text
            self.logger.info(f"actual text on identify enroll button: {actual_text_on_identify_enroll_button}")
            expected_text_on_identify_enroll_button = Portal_login_page_read_ini(). \
                get_expected_text_on_identify_enroll_button()
            self.logger.info(f"expected text on identify enroll button: {expected_text_on_identify_enroll_button}")
            if actual_text_on_identify_enroll_button == expected_text_on_identify_enroll_button:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            camera_icon = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                              get_camera_icon_on_identify_enroll_button_by_xpath())
            if camera_icon.is_displayed():
                self.logger.info("Camera icon on Identify & Enroll button is visible.....")
                self.status.append(True)
            else:
                self.status.append(False)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_identify_enroll_button_by_xpath()).click()
            self.logger.info("Identify & Enroll button is clicked.....")
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            missing_username_text_on_alert = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                                 get_missing_username_text_on_error_alert_by_xpath())
            if missing_username_text_on_alert.is_displayed():
                self.logger.info("Missing Username message is visible.....")
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                    get_close_missing_username_alert_by_xpath()).click()
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            # logout().logout_from_core()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_06.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_06.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_06_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_06_exception.png")
            self.logger.error(f"TC_Portal_Login_06 got an exception as: {ex}")

    def verify_users_button_is_visible_and_clickable_text_and_male_icon_on_it_both_are_visible_click_on_users_and_verify_missing_username_msg_is_visible(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_07 started ********")
            self.logger.info("verify_users_button_is_visible_and_clickable_text_and_male_icon_on_it_both_are_visible_click_on_users_and_verify_missing_username_msg_is_visible")
            print("verify_users_button_is_visible_and_clickable_text_and_male_icon_on_it_both_are_visible_click_on_users_and_verify_missing_username_msg_is_visible")
            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            users_button = self.explicit_wait(10, "XPATH", Portal_login_page_read_ini()
                                              .get_users_button_by_xpath(), self.d)
            if users_button.is_displayed():
                self.logger.info("Users button is visible.....")
                self.status.append(True)
            else:
                self.status.append(False)
            if users_button.is_enabled():
                self.logger.info("Users button is clickable.....")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text_on_users_button = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                              get_users_text_on_users_button_by_xpath()).text
            self.logger.info(f"actual text on users button: {actual_text_on_users_button}")
            expected_text_on_users_button = Portal_login_page_read_ini().get_expected_text_on_users_button()
            self.logger.info(f"expected text on users button: {expected_text_on_users_button}")
            if actual_text_on_users_button == expected_text_on_users_button:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_male_icon_on_users_button_by_xpath()). \
                    is_displayed():
                self.logger.info("Male icon on Users button is visible.....")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_users_button_by_xpath()).click()
            self.logger.info("Users button is clicked...")
            time.sleep(web_driver.one_second)
            missing_username_text_on_alert = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                                 get_missing_username_text_on_error_alert_by_xpath())
            if missing_username_text_on_alert.is_displayed():
                self.logger.info("Missing Username message is visible.....")
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                    get_close_missing_username_alert_by_xpath()).click()
                self.status.append(True)
            else:
                self.status.append(False)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_07.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_07.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_07_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_07_exception.png")
            self.logger.error(f"TC_Portal_Login_07 got an exception as: {ex}")

    def verify_account_button_is_visible_and_clickable_text_and_lock_icon_on_it_both_are_visible_click_on_account_button_and_verify_missing_username_msg_is_visible(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_08 started ********")
            self.logger.info("verify_account_button_is_visible_and_clickable_text_and_lock_icon_on_it_both_are_visible_click_on_account_button_and_verify_missing_username_msg_is_visible")
            print("verify_account_button_is_visible_and_clickable_text_and_lock_icon_on_it_both_are_visible_click_on_account_button_and_verify_missing_username_msg_is_visible")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            accounts_button = self.explicit_wait(10, "XPATH", Portal_login_page_read_ini()
                                                 .get_account_button_by_xpath(), self.d)
            if accounts_button.is_displayed():
                self.logger.info("Account button is visible.....")
                self.status.append(True)
            else:
                self.status.append(False)
            if accounts_button.is_enabled():
                self.logger.info("Account button is clickable.....")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_account_button = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                                get_account_text_on_account_button_by_xpath()).text
            self.logger.info(f"actual text on account button: {actual_text_on_account_button}")
            expected_text_on_account_button = Portal_login_page_read_ini().get_expected_text_on_account_button()
            self.logger.info(f"expected text on account button: {expected_text_on_account_button}")
            time.sleep(web_driver.one_second)
            if actual_text_on_account_button == expected_text_on_account_button:
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_lock_icon_on_account_button_by_xpath()). \
                    is_displayed():
                self.logger.info("Lock icon on Account button is visible.....")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_account_button_by_xpath()).click()
            self.logger.info("Account button is clicked...")
            time.sleep(web_driver.one_second)

            missing_username_text_on_alert = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                                 get_missing_username_text_on_error_alert_by_xpath())
            if missing_username_text_on_alert.is_displayed():
                self.logger.info("Missing Username message is visible.....")
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                    get_close_missing_username_alert_by_xpath()).click()
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_08.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_08.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_08_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_08_exception.png")
            self.logger.error(f"TC_Portal_Login_08 got an exception as: {ex}")

    def verify_switch_language_button_is_visible_and_clickable_text_on_it_is_visible_click_on_switch_language_and_verify_box_is_visible_click_cancel_button_on_dialog_box(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_09 started ********")
            print("verify_switch_language_button_is_visible_and_clickable_text_on_it_is_visible_click_on_switch_language_and_verify_box_is_visible_click_cancel_button_on_dialog_box")
            self.logger.info("verify_switch_language_button_is_visible_and_clickable_text_on_it_is_visible_click_on_switch_language_and_verify_box_is_visible_click_cancel_button_on_dialog_box")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            switch_language_button = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                         get_switch_language_button_by_xpath())
            if switch_language_button.is_displayed():
                self.logger.info("Switch Language button is visible.....")
                self.status.append(True)
            else:
                self.status.append(False)
            if switch_language_button.is_enabled():
                self.logger.info("Switch Language button is clickable.....")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text_on_switch_language_button = self.d.find_element(
                By.XPATH,
                Portal_login_page_read_ini().get_switch_language_text_on_switch_language_button_by_xpath()).text
            self.logger.info(f"actual text on switch language button: {actual_text_on_switch_language_button}")
            expected_text_on_switch_language_button = Portal_login_page_read_ini(). \
                get_expected_text_on_switch_language_button()
            self.logger.info(f"expected text on switch language button: {expected_text_on_switch_language_button}")
            if actual_text_on_switch_language_button == expected_text_on_switch_language_button:
                self.status.append(True)
            else:
                self.status.append(False)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_switch_language_button_by_xpath()).click()
            self.logger.info("SWITCH LANGUAGE button is clicked...")
            self.explicit_wait(10, "XPATH", Portal_login_page_read_ini().get_switch_language_dialog_box_heading_by_xpath(), self.d)
            actual_heading_on_switch_language_dialog_box = self.d.find_element(
                By.XPATH, Portal_login_page_read_ini().get_switch_language_dialog_box_heading_by_xpath()).text
            self.logger.info(
                f"actual heading on switch language dialog box: {actual_heading_on_switch_language_dialog_box}")
            expected_heading_on_switch_language_dialog_box = Portal_login_page_read_ini(). \
                get_expected_heading_of_switch_language_dialog_box()
            self.logger.info(f"expected heading on switch language dialog box: {expected_heading_on_switch_language_dialog_box}")
            time.sleep(web_driver.one_second)
            if actual_heading_on_switch_language_dialog_box == expected_heading_on_switch_language_dialog_box:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                get_cancel_button_on_switch_language_dialog_box_by_xpath()).click()
            self.logger.info("Cancel button on switch language dialog box is clicked....")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_09.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_09.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_09_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_09_exception.png")
            self.logger.error(f"TC_Portal_Login_09 got an exception as: {ex}")

    def verify_user_login_with_valid_credentials_and_click_on_cloud_login_and_verify_it_is_navigating_to_cloud_menu_panel(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_10 started ********")
            self.logger.info("verify_user_login_with_valid_credentials_and_click_on_cloud_login_and_verify_it_is_navigating_to_cloud_menu_panel")
            print("verify_user_login_with_valid_credentials_and_click_on_cloud_login_and_verify_it_is_navigating_to_cloud_menu_panel")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)

            self.status.clear()
            time.sleep(web_driver.one_second)
            username_textbox = self.explicit_wait(10, "XPATH", Portal_login_page_read_ini()
                                                  .get_portal_login_username_textbox_by_xpath(), self.d)
            username_textbox.clear()
            time.sleep(web_driver.one_second)
            username_textbox.send_keys(Portal_login_page_read_ini().get_valid_login_username())
            self.logger.info(f"username entered: {Portal_login_page_read_ini().get_valid_login_username()}")
            time.sleep(web_driver.one_second)
            password_textbox = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                   get_portal_login_password_textbox_by_xpath())
            password_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_password())
            self.logger.info(f"password entered: {Portal_login_page_read_ini().get_portal_login_password()}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath()). \
                click()
            self.logger.info("Clicked on CLOUD LOGIN button....")
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.one_second)

            login().accept_terms_and_conditions_for_login_for_new_user()
            if self.explicit_wait(10, "XPATH", Portal_login_page_read_ini().get_cloud_menu_on_dashboard_by_xpath(), self.d).is_displayed():
                self.logger.info("Login successful...")
                self.status.append(True)
            else:
                self.logger.error("user is not able to Login....")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath()).click()
            time.sleep(web_driver.one_second)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_10.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_10.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_10_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_10_exception.png")
            self.logger.error(f"TC_Portal_Login_10 got an exception as: {ex}")

    def verify_user_login_with_valid_credentials_and_click_on_events_button_and_verify_it_is_navigating_to_events_panel(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_11 started ********")
            self.logger.info("verify_user_login_with_valid_credentials_and_click_on_events_button_and_verify_it_is_navigating_to_events_panel")
            print("verify_user_login_with_valid_credentials_and_click_on_events_button_and_verify_it_is_navigating_to_events_panel")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            username_textbox = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                   get_portal_login_username_textbox_by_xpath())
            username_textbox.clear()
            time.sleep(web_driver.one_second)
            username_textbox.send_keys(Portal_login_page_read_ini().get_valid_login_username())
            self.logger.info(f"username entered: {Portal_login_page_read_ini().get_valid_login_username()}")
            time.sleep(web_driver.one_second)
            password_textbox = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                   get_portal_login_password_textbox_by_xpath())
            password_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_password())
            self.logger.info(f"password entered: {Portal_login_page_read_ini().get_portal_login_password()}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_events_button_on_portal_by_xpath()).click()
            self.logger.info("Clicked on Events button....")
            time.sleep(web_driver.one_second)
            actual = self.explicit_wait(10, "XPATH", Portal_login_page_read_ini().get_events_heading_on_events_panel_by_xpath(), self.d)
            actual_txt = actual.text
            self.logger.info(f"actual heading on events panel: {actual_txt}")
            expected_heading = Portal_login_page_read_ini().get_expected_text_events_on_button()
            self.logger.info(f"expected heading : {expected_heading}")
            if actual_txt == expected_heading:
                self.logger.info("Login to Events panel success..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath()).click()
            time.sleep(web_driver.two_second)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_11.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_11.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_11_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_11_exception.png")
            self.logger.error(f"TC_Portal_Login_11 got an exception as: {ex}")

    def verify_user_login_with_valid_credentials_and_click_on_identify_enroll_button_and_verify_it_is_navigating_to_identify_enroll_panel(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_12 started ********")
            self.logger.info("verify_user_login_with_valid_credentials_and_click_on_identify_enroll_button_and_verify_it_is_navigating_to_identify_enroll_panel")
            print("verify_user_login_with_valid_credentials_and_click_on_identify_enroll_button_and_verify_it_is_navigating_to_identify_enroll_panel")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            username_textbox = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                   get_portal_login_username_textbox_by_xpath())
            username_textbox.clear()
            username_textbox.send_keys(Portal_login_page_read_ini().get_valid_login_username())
            self.logger.info(f"username entered: {Portal_login_page_read_ini().get_valid_login_username()}")
            time.sleep(web_driver.one_second)
            password_textbox = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                   get_portal_login_password_textbox_by_xpath())
            password_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_password())
            self.logger.info(f"password entered: {Portal_login_page_read_ini().get_portal_login_password()}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_identify_enroll_button_by_xpath()).click()
            self.logger.info("Clicked on Identify & Enroll button....")
            time.sleep(web_driver.one_second)

            actual_heading = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_identify_enroll_panel_heading_by_xpath())
            actual_heading = self.wait_for_element_to_appear(actual_heading, Portal_login_page_read_ini().get_identify_enroll_panel_heading_by_xpath())
            self.logger.info(f"actual heading on Identify & Enroll panel: {actual_heading.text}")
            expected_heading = Portal_login_page_read_ini().get_expected_text_on_identify_enroll_button()
            self.logger.info(f"expected heading on Identify & Enroll Panel: {expected_heading}")
            if actual_heading.text == expected_heading:
                self.logger.info("Login to Identify & Enroll panel success..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath()).click()
            time.sleep(web_driver.one_second)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_12.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_12.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_12_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_12_exception.png")
            self.logger.error(f"TC_Portal_Login_12 got an exception as: {ex}")

    def verify_user_login_with_valid_credentials_and_click_on_users_button_and_verify_it_is_navigating_to_users_panel(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_13 started ********")
            self.logger.info("verify_user_login_with_valid_credentials_and_click_on_users_button_and_verify_it_is_navigating_to_users_panel")
            print("verify_user_login_with_valid_credentials_and_click_on_users_button_and_verify_it_is_navigating_to_users_panel")
            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            username_textbox = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                   get_portal_login_username_textbox_by_xpath())
            username_textbox.clear()
            username_textbox.send_keys(Portal_login_page_read_ini().get_valid_login_username())
            self.logger.info(f"username entered: {Portal_login_page_read_ini().get_valid_login_username()}")
            time.sleep(web_driver.one_second)
            password_textbox = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                   get_portal_login_password_textbox_by_xpath())
            password_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_password())
            self.logger.info(f"password entered: {Portal_login_page_read_ini().get_portal_login_password()}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_users_button_by_xpath()).click()
            self.logger.info("Clicked on Users button....")
            time.sleep(web_driver.one_second)
            actual_heading = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_users_heading_on_panel_by_xpath())
            actual_heading = self.wait_for_element_to_appear(actual_heading, Portal_login_page_read_ini().get_users_heading_on_panel_by_xpath())
            self.logger.info(f"actual heading on Users panel: {actual_heading.text}")
            expected_heading = Portal_login_page_read_ini().get_expected_text_on_users_button()
            self.logger.info(f"expected heading on Users panel: {expected_heading}")
            if actual_heading.text == expected_heading:
                self.logger.info("Login to Users panel success..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath()).click()
            time.sleep(web_driver.one_second)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_13.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_13.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_13_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_13_exception.png")
            self.logger.error(f"TC_Portal_Login_13 got an exception as: {ex}")

    def verify_user_login_with_valid_credentials_and_click_on_account_and_verify_it_is_navigating_to_account_panel(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_14 started ********")
            self.logger.info("verify_user_login_with_valid_credentials_and_click_on_account_and_verify_it_is_navigating_to_account_panel")
            print("verify_user_login_with_valid_credentials_and_click_on_account_and_verify_it_is_navigating_to_account_panel")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            username_textbox = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                   get_portal_login_username_textbox_by_xpath())
            username_textbox.clear()
            username_textbox.send_keys(Portal_login_page_read_ini().get_valid_login_username())
            self.logger.info(f"username entered: {Portal_login_page_read_ini().get_valid_login_username()}")
            time.sleep(web_driver.one_second)
            password_textbox = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                   get_portal_login_password_textbox_by_xpath())
            password_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_password())
            self.logger.info(f"password entered: {Portal_login_page_read_ini().get_portal_login_password()}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_account_button_by_xpath()).click()
            self.logger.info("Clicked on Account button....")
            time.sleep(web_driver.one_second)
            actual_heading = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_account_heading_on_account_panel_by_xpath())
            actual_heading = self.wait_for_element_to_appear(actual_heading, Portal_login_page_read_ini().get_account_heading_on_account_panel_by_xpath())
            self.logger.info(f"actual heading on Account panel: {actual_heading.text}")
            expected_heading = Portal_login_page_read_ini().get_expected_text_on_account_button()
            self.logger.info(f"expected heading on Account panel: {expected_heading}")
            if actual_heading.text == expected_heading:
                self.logger.info("Login to Account panel success..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            # logout().logout_from_core()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_14.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_14.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_14_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_14_exception.png")
            self.logger.error(f"TC_Portal_Login_14 got an exception as: {ex}")

    def click_on_switch_language_and_verify_switch_language_text_is_visible_english_spanish_arabic_portuguese_text_is_visible_verify_cancel_button_is_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_Portal_Login_15 started ********")
            self.logger.info("click_on_switch_language_and_verify_switch_language_text_is_visible_english_spanish_arabic_portuguese_text_is_visible_verify_cancel_button_is_visible_and_clickable")
            print("click_on_switch_language_and_verify_switch_language_text_is_visible_english_spanish_arabic_portuguese_text_is_visible_verify_cancel_button_is_visible_and_clickable")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_switch_language_button_by_xpath()).click()
            self.logger.info("Clicked on Switch Language button...")
            time.sleep(web_driver.one_second)
            actual_heading = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_switch_language_dialog_box_heading_by_xpath()).text
            self.logger.info(f"actual heading on switch language dialog box: {actual_heading}")
            expected_heading = Portal_login_page_read_ini().get_expected_heading_of_switch_language_dialog_box()
            self.logger.info(f"expected heading on switch language dialog box: {expected_heading}")
            if actual_heading == expected_heading:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_english = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_english_language_on_dialog_box_by_xpath())
            actual_english = self.wait_for_element_to_appear(actual_english, Portal_login_page_read_ini().get_english_language_on_dialog_box_by_xpath())
            self.logger.info(f"actual text: {actual_english.text}")
            expected_text_english = Portal_login_page_read_ini().get_english_language()
            self.logger.info(f"expected text: {expected_text_english}")
            if actual_english.text == expected_text_english:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_spanish = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_spanish_language_on_dialog_box_by_xpath()).text
            self.logger.info(f"actual text: {actual_spanish}")
            self.logger.info(f"expected text: {Portal_login_page_read_ini().get_spanish_language()}")
            if actual_spanish == Portal_login_page_read_ini().get_spanish_language():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_arabic = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_arabic_language_on_dialog_box_by_xpath()).text
            self.logger.info(f"actual text: {actual_arabic}")
            expected_arabic = Portal_login_page_read_ini().get_arabic_language()
            self.logger.info(f"expected text: {expected_arabic}")
            if actual_arabic == expected_arabic:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_portuguese = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_portuguese_language_on_dialog_box_by_xpath()).text
            self.logger.info(f"actual text: {actual_portuguese}")
            expected_portuguese = Portal_login_page_read_ini().get_portuguese_language()
            self.logger.info(f"expected text: {expected_portuguese}")
            if actual_portuguese == expected_portuguese:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            cancel_button = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_cancel_button_on_switch_language_dialog_box_by_xpath())
            if cancel_button.is_displayed():
                self.logger.info("Cancel button on Switch Language dialog box is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if cancel_button.is_enabled():
                self.logger.info("Cancel button on Switch Language dialog box is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text_on_cancel_button = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_cancel_button_on_switch_language_dialog_box_by_xpath()).text
            self.logger.info(f"actual text on cancel button: {actual_text_on_cancel_button}")
            expected_text_on_cancel_button = Portal_login_page_read_ini().get_expected_text_on_cancel_button()
            self.logger.info(f"expected text on cancel button: {expected_text_on_cancel_button}")
            time.sleep(web_driver.one_second)
            if actual_text_on_cancel_button == expected_text_on_cancel_button:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_cancel_button_on_switch_language_dialog_box_by_xpath()).click()
            self.logger.info("Clicked on Cancel button on Switch Language dialog box...")
            self.logger.info(f"status: {self.status}")
            # logout().logout_from_core()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_15.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_15.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_15_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_15_exception.png")
            self.logger.error(f"TC_Portal_Login_15 got an exception as: {ex}")

    def verify_radio_button_before_english_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_english_language(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_19 started ********")
            self.logger.info("verify_radio_button_before_english_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_english_language")
            print("verify_radio_button_before_english_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_english_language")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_switch_language_button_by_xpath()).click()
            self.logger.info("Clicked on Switch Language button...")
            time.sleep(web_driver.one_second)
            english_radio_button = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_english_radio_button_by_xpath())
            if english_radio_button.is_displayed():
                self.logger.info("English radio button is visible...")
                self.status.append(True)
            else:
                self.logger.error("English radio button is not visible...")
                self.status.append(False)
            if english_radio_button.is_enabled():
                self.logger.info("English radio button is clickable...")
                self.status.append(True)
            else:
                self.logger.error("English radio button is not clickable...")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_english_radio_button_by_xpath()).click()
            self.logger.info("Clicked on English radio button...")
            time.sleep(web_driver.one_second)

            actual_text_on_switch_language_button = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_switch_language_text_on_switch_language_button_by_xpath())
            actual_text_on_switch_language_button = self.wait_for_element_to_appear(actual_text_on_switch_language_button, Portal_login_page_read_ini().get_switch_language_text_on_switch_language_button_by_xpath())
            self.logger.info(f"actual text on switch language button: {actual_text_on_switch_language_button.text}")
            expected_text_on_switch_language_button = Portal_login_page_read_ini().get_expected_text_on_switch_language_button()
            self.logger.info(f"expected text: {expected_text_on_switch_language_button}")
            if actual_text_on_switch_language_button.text == expected_text_on_switch_language_button:
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            # logout().logout_from_core()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_19.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_19.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_19_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_19_exception.png")
            self.logger.error(f"TC_Portal_Login_19 got an exception as: {ex}")

    def verify_radio_button_before_portuguese_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_portuguese_language(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_16 started ********")
            self.logger.info("verify_radio_button_before_portuguese_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_portuguese_language")
            print("verify_radio_button_before_portuguese_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_portuguese_language")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_switch_language_button_by_xpath()).click()
            self.logger.info("Clicked on Switch Language button...")
            time.sleep(web_driver.one_second)
            portuguese_radio_button = self.d.find_element(By.XPATH, Portal_login_page_read_ini().
                                                          get_portuguese_radio_button_by_xpath())
            if portuguese_radio_button.is_displayed():
                self.logger.info("Portuguese radio button is visible...")
                self.status.append(True)
            else:
                self.logger.error("Portuguese radio button is not visible...")
                self.status.append(False)
            if portuguese_radio_button.is_enabled():
                self.logger.info("Portuguese radio button is clickable...")
                self.status.append(True)
            else:
                self.logger.error("Portuguese radio button is not clickable...")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_portuguese_radio_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on Portuguese radio button...")
            time.sleep(web_driver.one_second)
            actual_text_on_switch_language_button = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_switch_language_text_on_switch_language_button_by_xpath())
            actual_text_on_switch_language_button = self.wait_for_element_to_appear(actual_text_on_switch_language_button, Portal_login_page_read_ini().get_switch_language_text_on_switch_language_button_by_xpath())
            self.logger.info(f"actual text on switch language button: {actual_text_on_switch_language_button.text}")
            expected_text_on_switch_language_button = Portal_login_page_read_ini().get_expected_switch_language_text_in_portuguese()
            self.logger.info(f"expected text on switch language button: {expected_text_on_switch_language_button}")
            if actual_text_on_switch_language_button.text == expected_text_on_switch_language_button:
                self.status.append(True)
            else:
                self.status.append(False)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_16.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_16.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_16_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_16_exception.png")
            self.logger.error(f"TC_Portal_Login_16 got an exception as: {ex}")

    def verify_radio_button_before_arabic_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_arabic_language(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_18 started ********")
            self.logger.info("verify_radio_button_before_arabic_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_arabic_language")
            print("verify_radio_button_before_arabic_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_arabic_language")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_switch_language_button_by_xpath()).click()
            self.logger.info("Clicked on Switch Language button...")
            time.sleep(web_driver.one_second)
            arabic_radio_button = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_arabic_radio_button_by_xpath())
            if arabic_radio_button.is_displayed():
                self.logger.info("Arabic radio button is visible...")
                self.status.append(True)
            else:
                self.logger.error("Arabic radio button is not visible...")
                self.status.append(False)
            if arabic_radio_button.is_enabled():
                self.logger.info("Arabic radio button is clickable...")
                self.status.append(True)
            else:
                self.logger.error("Arabic radio button is not clickable...")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_arabic_radio_button_by_xpath()).click()
            self.logger.info("Clicked on Arabic radio button...")
            time.sleep(web_driver.one_second)
            actual_text_on_switch_language_button = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_switch_language_text_on_switch_language_button_by_xpath())
            actual_text_on_switch_language_button = self.wait_for_element_to_appear(actual_text_on_switch_language_button, Portal_login_page_read_ini().get_switch_language_text_on_switch_language_button_by_xpath())
            self.logger.info(f"actual text on switch language button: {actual_text_on_switch_language_button.text}")
            expected_text = Portal_login_page_read_ini().get_expected_switch_language_text_in_arabic()
            self.logger.info(f"expected text on switch language button: {expected_text}")
            if actual_text_on_switch_language_button.text == "":
                self.status.append(False)
            else:
                self.status.append(True)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_switch_language_button_by_xpath()).click()
            self.explicit_wait(10, "XPATH", Portal_login_page_read_ini().get_english_radio_button_by_xpath(), self.d).click()
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_18.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_18.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_18_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_18_exception.png")
            self.logger.error(f"TC_Portal_Login_18 got an exception as: {ex}")

    def verify_radio_button_before_spanish_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_spanish_language(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_17 started ********")
            self.logger.info("verify_radio_button_before_spanish_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_spanish_language")
            print("verify_radio_button_before_spanish_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_spanish_language")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_switch_language_button_by_xpath()).click()
            self.logger.info("Clicked on Switch Language button...")
            time.sleep(web_driver.one_second)
            spanish_radio_button = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_spanish_radio_button_by_xpath())
            if spanish_radio_button.is_displayed():
                self.logger.info("Spanish radio button is visible...")
                self.status.append(True)
            else:
                self.logger.error("Spanish radio button is not visible...")
                self.status.append(False)
            if spanish_radio_button.is_enabled():
                self.logger.info("Spanish radio button is clickable...")
                self.status.append(True)
            else:
                self.logger.error("Spanish radio button is not clickable...")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_spanish_radio_button_by_xpath()).click()
            self.logger.info("Clicked on Spanish radio button...")
            time.sleep(web_driver.one_second)
            actual_text_on_switch_language_button = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_switch_language_text_on_switch_language_button_by_xpath())
            actual_text_on_switch_language_button = self.wait_for_element_to_appear(actual_text_on_switch_language_button, Portal_login_page_read_ini().get_switch_language_text_on_switch_language_button_by_xpath())
            self.logger.info(f"actual text on switch language button: {actual_text_on_switch_language_button.text}")
            expected_text_on_switch_language_button = Portal_login_page_read_ini().get_expected_switch_language_text_in_spanish()
            self.logger.info(f"expected text on switch language button: {expected_text_on_switch_language_button}")
            if actual_text_on_switch_language_button.text == expected_text_on_switch_language_button:
                self.status.append(True)
            else:
                self.status.append(False)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_17.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_17.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_17_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_17_exception.png")
            self.logger.error(f"TC_Portal_Login_17 got an exception as: {ex}")

    def verify_face_first_copy_rights_is_visible_and_clickable_click_on_copyrights_and_verify_versions_of_webapi_and_server_both_are_visible_verify_latest_version_of_webapi_and_server_is_appeared(self):
        try:
            self.logger.info("********** TC_Portal_Login_20 started ********")
            self.logger.info("verify_face_first_copy_rights_is_visible_and_clickable_click_on_copyrights_and_verify_versions_of_webapi_and_server_both_are_visible_verify_latest_version_of_webapi_and_server_is_appeared")
            print("verify_face_first_copy_rights_is_visible_and_clickable_click_on_copyrights_and_verify_versions_of_webapi_and_server_both_are_visible_verify_latest_version_of_webapi_and_server_is_appeared")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            # face_first_copyright = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_face_first_copyright_text_by_xpath())
            face_first_copyright = web_driver.explicit_wait(self, 5, "XPATH", Portal_login_page_read_ini().get_face_first_copyright_text_by_xpath(), self.d)
            if face_first_copyright.is_displayed():
                self.logger.info("FaceFirst Copyright is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if face_first_copyright.is_enabled():
                self.logger.info("FaceFirst Copyright is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_copyright_text = face_first_copyright.text
            self.logger.info(f"actual copyright text: {actual_copyright_text[7:]}")
            print(f"actual copyright text: {actual_copyright_text[7:]}")
            expected_copyright_text = Portal_login_page_read_ini().get_expected_copyright_text()
            self.logger.info(f"expected copyright text: {expected_copyright_text}")

            if expected_copyright_text != actual_copyright_text[7:]:
                self.status.append(False)
            else:
                self.status.append(True)
            self.logger.info(f"status: {self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_face_first_copyright_text_by_xpath()).click()
            time.sleep(web_driver.one_second)
            wait = WebDriverWait(self.d, 10)
            popover = wait.until(EC.visibility_of_element_located((By.ID, "versionInformation")))
            copyright_on_display_version_info = popover.find_element(By.XPATH, '//span[@ng-bind="\'TEXT-FACEFIRST-COPYRIGHT\' | i18n"]')
            print(copyright_on_display_version_info.text)
            # copyright_on_display_version_info = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_copyright_on_display_version_page())
            # copyright_on_display_version_info = self.explicit_wait(5, "XPATH", Portal_login_page_read_ini().get_copyright_on_display_version_page(), self.d)
            # copyright_on_display_version_info = self.wait_for_element_to_appear(copyright_on_display_version_info, Portal_login_page_read_ini().get_copyright_on_display_version_page())
            self.logger.info(f"popover visible: {popover.is_displayed()}")
            self.logger.info(f"copyrights text: {copyright_on_display_version_info.text}")
            if actual_copyright_text[7:] == copyright_on_display_version_info.text:
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            # actual_webapi_text_on_version_info = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_WebAPI_text_on_version_info_by_xpath())
            actual_webapi_text_on_version_info = popover.find_element(By.XPATH, Portal_login_page_read_ini().get_WebAPI_text_on_version_info_by_xpath())
            # actual_webapi_text_on_version_info = self.wait_for_element_to_appear(actual_webapi_text_on_version_info, Portal_login_page_read_ini().get_WebAPI_text_on_version_info_by_xpath())
            expected_webapi_text_on_version_info = Portal_login_page_read_ini().get_expected_webapi_text_on_version_info()
            self.logger.info(f"actual webapi text: {actual_webapi_text_on_version_info.text}")
            self.logger.info(f"actual webapi text: {expected_webapi_text_on_version_info}")
            if actual_webapi_text_on_version_info.text == expected_webapi_text_on_version_info:
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            time.sleep(web_driver.one_second)
            # actual_webapi_version_number = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_webapi_version_info_by_xpath()).text
            actual_webapi_version_number = popover.find_element(By.XPATH, Portal_login_page_read_ini().get_webapi_version_info_by_xpath())
            self.logger.info(f"actual webapi version: {actual_webapi_text_on_version_info.text} v{actual_webapi_version_number.text}")
            expected_webapi_version_number = Portal_login_page_read_ini().get_expected_webapi_version_number()
            self.logger.info(f"expected webapi version: {expected_webapi_text_on_version_info} v{expected_webapi_version_number}")
            if actual_webapi_version_number.text == expected_webapi_version_number:
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            time.sleep(web_driver.one_second)
            # actual_server_text_on_version_info = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_Server_text_on_version_info_by_xpath()).text
            actual_server_text_on_version_info = popover.find_element(By.XPATH, Portal_login_page_read_ini().get_Server_text_on_version_info_by_xpath())
            expected_server_text_on_version_info = Portal_login_page_read_ini().get_expected_server_text_on_version_info()
            self.logger.info(f"actual_server_text_on_version_info: {actual_server_text_on_version_info.text}")
            self.logger.info(f"expected_server_text_on_version_info: {expected_server_text_on_version_info}")
            if actual_server_text_on_version_info.text == expected_server_text_on_version_info:
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            time.sleep(web_driver.one_second)
            # actual_portal_version_number = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_version_number_by_xpath()).text
            actual_portal_version_number = popover.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_version_number_by_xpath())
            self.logger.info(f"actual portal version: {actual_server_text_on_version_info.text} v{actual_portal_version_number.text}")
            expected_portal_version_number = Portal_login_page_read_ini().get_expected_portal_version_number()
            self.logger.info(f"expected portal number: {expected_server_text_on_version_info} v{expected_portal_version_number}")
            if actual_portal_version_number.text == expected_portal_version_number:
                self.status.append(True)
            else:
                self.status.append(False)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_close_button_on_version_info_by_xpath()).click()
            time.sleep(web_driver.one_second)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            print(self.status)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_20.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_20.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_20_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_20_exception.png")
            self.logger.error(f"TC_Portal_Login_20 got an exception as: {ex}")

    def on_version_info_verify_close_button_is_visible_and_clickable_text_on_it_is_visible_click_on_close_button_and_verify_version_info_closed(
            self):
        try:
            self.logger.info("********** TC_Portal_Login_21 started ********")
            self.logger.info("on_version_info_verify_close_button_is_visible_and_clickable_text_on_it_is_visible_click_on_close_button_and_verify_version_info_closed")
            print("on_version_info_verify_close_button_is_visible_and_clickable_text_on_it_is_visible_click_on_close_button_and_verify_version_info_closed")
            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_face_first_copyright_text_by_xpath()).click()
            time.sleep(web_driver.one_second)
            close_button = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_close_button_on_version_info_by_xpath())
            if close_button.is_displayed():
                self.logger.info("Close button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if close_button.is_enabled():
                self.logger.info("Close button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text_on_close_button = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_close_button_on_version_info_by_xpath()).text
            self.logger.info(f"actual text on close button: {actual_text_on_close_button}")
            expected_text_on_close_button_on_version_info = Portal_login_page_read_ini().get_expected_text_on_close_button_on_version_info()
            self.logger.info(f"expected text on close button: {expected_text_on_close_button_on_version_info}")
            time.sleep(web_driver.one_second)
            if actual_text_on_close_button == expected_text_on_close_button_on_version_info:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_close_button_on_version_info_by_xpath()).click()
            self.logger.info("Clicked on Close button....")
            time.sleep(web_driver.one_second)
            if self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_copyright_on_display_version_page()). \
                    is_displayed():
                self.status.append(False)
            else:
                self.logger.info("Version info is closed...")
                self.status.append(True)
            time.sleep(web_driver.one_second)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.info(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_21.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_21.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_21_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_21_exception.png")
            self.logger.error(f"TC_Portal_Login_21 got an exception as: {ex}")

    def verify_user_login_with_valid_username_and_valid_password_verify_message_warning(self):
        try:
            self.logger.info("********** TC_Portal_Login_22 started ********")
            self.logger.info("verify_user_login_with_valid_username_and_valid_password_verify_message_warning")
            print("verify_user_login_with_valid_username_and_valid_password_verify_message_warning")
            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            username_txtbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            # username_txtbox = self.wait_for_element_to_appear(username_txtbox, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_txtbox = self.explicit_wait(5, "XPATH", Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath(), self.d)
            username_txtbox.clear()
            time.sleep(web_driver.one_second)
            username_txtbox.send_keys(Portal_login_page_read_ini().get_valid_login_username())
            self.logger.info(f"Entered username as: {Portal_login_page_read_ini().get_valid_login_username()}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath()).send_keys(Portal_login_page_read_ini().get_portal_login_password())
            self.logger.info(f"Entered password as: {Portal_login_page_read_ini().get_portal_login_password()}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath()).click()
            time.sleep(web_driver.two_second)
            dashboard_menu = self.explicit_wait(10, "XPATH", Portal_login_page_read_ini().get_dashboard_menu_by_xpath(), self.d)
            if dashboard_menu.is_displayed():
                self.logger.info(f"dashboard menu is displayed:{dashboard_menu.is_displayed()}")
                self.logger.info("Logged in success...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            logout_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
            logout_btn = self.wait_for_element_to_appear(logout_btn, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
            logout_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            # logout().logout_from_core()
            if False in self.status:
                self.logger.info(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_22.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_22.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_22_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_22_exception.png")
            self.logger.error(f"TC_Portal_Login_22 got an exception as: {ex}")

    def verify_user_login_with_valid_user_name_and_incorrect_password_verify_message_warning(self):
        try:
            self.logger.info("********** TC_Portal_Login_23 started ********")
            self.logger.info("verify_user_login_with_valid_user_name_and_incorrect_password_verify_message_warning")
            print("verify_user_login_with_valid_user_name_and_incorrect_password_verify_message_warning")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            username_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox = self.wait_for_element_to_appear(username_textbox, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox.clear()
            time.sleep(web_driver.one_second)
            username_textbox.send_keys(Portal_login_page_read_ini().get_valid_login_username())
            time.sleep(web_driver.one_second)

            self.logger.info(f"Entered username as: {Portal_login_page_read_ini().get_valid_login_username()}")
            password_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox = self.wait_for_element_to_appear(password_textbox, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox.clear()
            time.sleep(web_driver.one_second)
            password_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_invalid_password())
            self.logger.info(f"Entered password as: {Portal_login_page_read_ini().get_portal_login_invalid_password()}")
            time.sleep(web_driver.one_second)
            login_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn = self.wait_for_element_to_appear(login_btn, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn.click()
            time.sleep(web_driver.one_second)

            actual_error_invalid_password = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_invalid_password_text_on_alert_by_xpath())
            actual_error_invalid_password = self.wait_for_element_to_appear(actual_error_invalid_password, Portal_login_page_read_ini().get_invalid_password_text_on_alert_by_xpath())

            self.logger.info(f"actual invalid password error: {actual_error_invalid_password.text}")
            expected_error_invalid_password = Portal_login_page_read_ini().get_expected_invalid_password_error_text()
            expected_password_not_matching = Portal_login_page_read_ini().get_expected_password_not_match()
            self.logger.info(f"expected error: {expected_error_invalid_password}")
            if expected_error_invalid_password in actual_error_invalid_password.text or expected_password_not_matching in actual_error_invalid_password.text:
                self.status.append(True)
            else:
                logout_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn = self.wait_for_element_to_appear(logout_btn, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn.click()
                time.sleep(web_driver.one_second)
                self.status.append(False)
            invalid_login_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_close_invalid_password_alert_by_xpath())
            invalid_login_btn = self.wait_for_element_to_appear(invalid_login_btn, Portal_login_page_read_ini().get_close_invalid_password_alert_by_xpath())
            if invalid_login_btn.is_displayed():
                invalid_login_btn.click()
            self.logger.info(f"status: {self.status}")
            # logout().logout_from_core()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_23.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_23.png")
                time.sleep(web_driver.one_second)
                # logout().logout_from_core()
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath()).click()
                time.sleep(web_driver.one_second)
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_23_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_23_exception.png")
            self.logger.error(f"TC_Portal_Login_23 got an exception as: {ex}")

    def verify_user_login_with_invalid_username_and_valid_password_verify_message_warning(self):
        try:
            self.logger.info("********** TC_Portal_Login_24 started ********")
            self.logger.info("verify_user_login_with_invalid_username_and_valid_password_verify_message_warning")
            print("verify_user_login_with_invalid_username_and_valid_password_verify_message_warning")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            username_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox = self.wait_for_element_to_appear(username_textbox, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox.clear()
            time.sleep(web_driver.one_second)
            username_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_invalid_username())

            self.logger.info(f"Entered username as: {Portal_login_page_read_ini().get_portal_login_invalid_username()}")
            password_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox = self.wait_for_element_to_appear(password_textbox, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox.clear()
            time.sleep(web_driver.one_second)
            password_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_password())
            time.sleep(web_driver.one_second)
            self.logger.info(f"Entered password as: {Portal_login_page_read_ini().get_portal_login_password()}")
            login_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn = self.wait_for_element_to_appear(login_btn, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn.click()
            time.sleep(web_driver.one_second)

            actual_invalid_username_error_msg = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_invalid_username_text_on_alert_by_xpath())
            actual_invalid_username_error_msg = self.wait_for_element_to_appear(actual_invalid_username_error_msg, Portal_login_page_read_ini().get_invalid_username_text_on_alert_by_xpath())
            time.sleep(web_driver.one_second)
            self.logger.info(f"actual invalid username error: {actual_invalid_username_error_msg.text}")
            username = Portal_login_page_read_ini().get_portal_login_invalid_username()
            error_msg = Portal_login_page_read_ini().get_expected_invalid_username_error_text()
            expected_error_invalid_username = error_msg + " '" + username + "'"
            self.logger.info(f"expected error: {expected_error_invalid_username}")
            if expected_error_invalid_username in actual_invalid_username_error_msg.text:
                self.status.append(True)
            else:
                time.sleep(web_driver.one_second)
                login_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                login_btn = self.wait_for_element_to_appear(login_btn, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                login_btn.click()
                time.sleep(web_driver.one_second)
                self.status.append(False)
            time.sleep(web_driver.one_second)
            invalid_username = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_close_invalid_username_alert_by_xpath())
            invalid_username = self.wait_for_element_to_appear(invalid_username, Portal_login_page_read_ini().get_close_invalid_username_alert_by_xpath())
            invalid_username.click()
            time.sleep(web_driver.one_second)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_24.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_24.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_24_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_24_exception.png")
            self.logger.error(f"TC_Portal_Login_24 got an exception as: {ex}")

    def verify_user_login_with_invalid_username_and_invalid_password_verify_message_warning(self):
        try:
            self.logger.info("********** TC_Portal_Login_25 started ********")
            self.logger.info("verify_user_login_with_invalid_username_and_invalid_password_verify_message_warning")
            print("verify_user_login_with_invalid_username_and_invalid_password_verify_message_warning")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            username_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox = self.wait_for_element_to_appear(username_textbox, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox.clear()
            time.sleep(web_driver.one_second)
            username_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_invalid_username())
            time.sleep(web_driver.one_second)
            self.logger.info(f"Entered username as: {Portal_login_page_read_ini().get_portal_login_invalid_username()}")
            time.sleep(web_driver.one_second)
            password_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox = self.wait_for_element_to_appear(password_textbox, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox.clear()
            time.sleep(web_driver.one_second)
            password_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_invalid_password())
            self.logger.info(f"Entered password as: {Portal_login_page_read_ini().get_portal_login_invalid_password()}")
            time.sleep(web_driver.one_second)
            login_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn = self.wait_for_element_to_appear(login_btn, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn.click()

            time.sleep(web_driver.one_second)
            actual_invalid_username_error_msg = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_invalid_username_text_on_alert_by_xpath())
            actual_invalid_username_error_msg = self.wait_for_element_to_appear(actual_invalid_username_error_msg, Portal_login_page_read_ini().get_invalid_username_text_on_alert_by_xpath())
            self.logger.info(f"actual invalid username error: {actual_invalid_username_error_msg.text}")
            username = Portal_login_page_read_ini().get_portal_login_invalid_username()
            error_msg = Portal_login_page_read_ini().get_expected_invalid_username_error_text()
            expected_error_invalid_username = error_msg + " '" + username + "'"
            self.logger.info(f"expected error: {expected_error_invalid_username}")
            time.sleep(web_driver.one_second)
            if expected_error_invalid_username in actual_invalid_username_error_msg.text:
                self.status.append(True)
            else:
                logout_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn = self.wait_for_element_to_appear(logout_btn, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn.click()
                time.sleep(web_driver.one_second)
                self.status.append(False)
            time.sleep(web_driver.one_second)
            invalid_username = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_close_invalid_username_alert_by_xpath())
            invalid_username = self.wait_for_element_to_appear(invalid_username, Portal_login_page_read_ini().get_close_invalid_username_alert_by_xpath())
            invalid_username.click()
            time.sleep(web_driver.one_second)
            # logout().logout_from_core()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_25.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_25.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_25_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_25_exception.png")
            self.logger.error(f"TC_Portal_Login_25 got an exception as: {ex}")

    def verify_user_login_missing_username_and_entering_password_verify_message_warning(self):
        try:
            self.logger.info("********** TC_Portal_Login_26 started ********")
            self.logger.info("verify_user_login_missing_username_and_entering_password_verify_message_warning")
            print("verify_user_login_missing_username_and_entering_password_verify_message_warning")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            username_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox = self.wait_for_element_to_appear(username_textbox, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox.clear()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Entered username as: null")
            time.sleep(web_driver.one_second)

            password_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox = self.wait_for_element_to_appear(password_textbox, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox.clear()
            time.sleep(web_driver.one_second)
            password_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_password())
            self.logger.info(f"Entered password as: {Portal_login_page_read_ini().get_portal_login_password()}")
            time.sleep(web_driver.one_second)
            login_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn = self.wait_for_element_to_appear(login_btn, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn.click()

            time.sleep(web_driver.one_second)
            actual_error_msg = self.d.find_elements(By.XPATH, Portal_login_page_read_ini(). get_missing_username_text_on_error_alert_by_xpath())
            actual_error_msg = self.wait_for_element_to_appear(actual_error_msg, Portal_login_page_read_ini(). get_missing_username_text_on_error_alert_by_xpath())

            self.logger.info(f"actual missing username error: {actual_error_msg.text}")
            expected_error_msg = Portal_login_page_read_ini().get_expected_missing_username_error_text()
            self.logger.info(f"expected missing username error: {expected_error_msg}")
            if expected_error_msg in actual_error_msg.text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            username_alert = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_close_missing_username_alert_by_xpath())
            username_alert = self.wait_for_element_to_appear(username_alert, Portal_login_page_read_ini().get_close_missing_username_alert_by_xpath())
            username_alert.click()
            time.sleep(web_driver.one_second)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_26.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_26.png")
                logout_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn = self.wait_for_element_to_appear(logout_btn, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn.click()
                time.sleep(web_driver.one_second)
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_26_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_26_exception.png")
            self.logger.error(f"TC_Portal_Login_26 got an exception as: {ex}")

    def verify_user_login_with_username_without_entering_password_verify_message_warning(self):
        try:
            self.logger.info("********** TC_Portal_Login_27 started ********")
            self.logger.info("verify_user_login_with_username_without_entering_password_verify_message_warning")
            print("verify_user_login_with_username_without_entering_password_verify_message_warning")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            username_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox = self.wait_for_element_to_appear(username_textbox, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox.clear()
            time.sleep(web_driver.one_second)
            username_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_username())

            self.logger.info(f"Entered username as: {Portal_login_page_read_ini().get_portal_login_username()}")
            password_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox = self.wait_for_element_to_appear(password_textbox, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox.clear()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Entered password as: null")
            time.sleep(web_driver.one_second)

            login_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn = self.wait_for_element_to_appear(login_btn, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn.click()

            time.sleep(web_driver.one_second)
            actual_missing_password_err = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_missing_password_text_on_error_alert_by_xpath())
            actual_missing_password_err = self.wait_for_element_to_appear(actual_missing_password_err, Portal_login_page_read_ini().get_missing_password_text_on_error_alert_by_xpath())
            self.logger.info(f"actual_missing_password: {actual_missing_password_err.text}")
            expected_missing_password_error = Portal_login_page_read_ini().get_expected_missing_password_error_text()
            self.logger.info(f"expected_missing_password: {expected_missing_password_error}")
            time.sleep(web_driver.one_second)
            if expected_missing_password_error in actual_missing_password_err.text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            password_missing_alert = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_close_missing_password_alert_by_xpath())
            password_missing_alert = self.wait_for_element_to_appear(password_missing_alert, Portal_login_page_read_ini().get_close_missing_password_alert_by_xpath())
            password_missing_alert.click()
            time.sleep(web_driver.one_second)
            # logout().logout_from_core()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_27.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_27.png")
                logout_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn = self.wait_for_element_to_appear(logout_btn, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn.click()
                time.sleep(web_driver.one_second)
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_27_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_27_exception.png")
            self.logger.error(f"TC_Portal_Login_27 got an exception as: {ex}")

    def verify_user_login_without_username_and_without_password_verify_message_warning(self):
        try:
            self.logger.info("********** TC_Portal_Login_28 started ********")
            self.logger.info("verify_user_login_without_username_and_without_password_verify_message_warning")
            print("verify_user_login_without_username_and_without_password_verify_message_warning")

            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            username_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox = self.wait_for_element_to_appear(username_textbox, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox.clear()

            self.logger.info(f"Entered username as: null")
            time.sleep(web_driver.one_second)
            password_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox = self.wait_for_element_to_appear(password_textbox, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox.clear()

            self.logger.info(f"Entered password as: null")
            time.sleep(web_driver.one_second)
            login_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn = self.wait_for_element_to_appear(login_btn, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn.click()
            time.sleep(web_driver.one_second)
            actual_error_msg = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_missing_username_text_on_error_alert_by_xpath())
            actual_error_msg = self.wait_for_element_to_appear(actual_error_msg, Portal_login_page_read_ini().get_missing_username_text_on_error_alert_by_xpath())
            self.logger.info(f"actual error message: {actual_error_msg.text}")
            expected_error_msg = Portal_login_page_read_ini().get_expected_missing_username_error_text()
            self.logger.info(f"expected error message: {expected_error_msg}")
            time.sleep(web_driver.one_second)
            if expected_error_msg in actual_error_msg.text:
                self.status.append(True)
            else:
                logout_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn = self.wait_for_element_to_appear(logout_btn, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn.click()
                time.sleep(web_driver.one_second)
                self.status.append(False)
            time.sleep(web_driver.one_second)
            missing_username_alert = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_close_missing_username_alert_by_xpath())
            missing_username_alert = self.wait_for_element_to_appear(missing_username_alert, Portal_login_page_read_ini().get_close_missing_username_alert_by_xpath())
            missing_username_alert.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_28.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_28.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_28_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_28_exception.png")
            self.logger.error(f"TC_Portal_Login_28 got an exception as: {ex}")

    def verify_user_login_with_invalid_user_user_that_is_not_present_in_system_verify_message_warning(self):
        try:
            self.logger.info("********** TC_Portal_Login_29 started ********")
            self.logger.info("verify_user_login_with_invalid_user_user_that_is_not_present_in_system_verify_message_warning")
            print("verify_user_login_with_invalid_user_user_that_is_not_present_in_system_verify_message_warning")
            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            username_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox = self.wait_for_element_to_appear(username_textbox, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox.clear()

            time.sleep(web_driver.one_second)
            username_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_invalid_username())

            self.logger.info(f"Entered username as: {Portal_login_page_read_ini().get_portal_login_invalid_username()}")
            time.sleep(web_driver.one_second)
            password_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox = self.wait_for_element_to_appear(password_textbox, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox.clear()
            time.sleep(web_driver.one_second)
            password_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_invalid_password())

            self.logger.info(f"Entered password as: {Portal_login_page_read_ini().get_portal_login_invalid_password()}")
            time.sleep(web_driver.one_second)
            login_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn = self.wait_for_element_to_appear(login_btn, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn.click()
            time.sleep(web_driver.one_second)
            actual_invalid_username_error_msg = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_invalid_username_text_on_alert_by_xpath())
            actual_invalid_username_error_msg = self.wait_for_element_to_appear(actual_invalid_username_error_msg, Portal_login_page_read_ini().get_invalid_username_text_on_alert_by_xpath())

            self.logger.info(f"actual invalid username error: {actual_invalid_username_error_msg.text}")
            username = Portal_login_page_read_ini().get_portal_login_invalid_username()
            error_msg = Portal_login_page_read_ini().get_expected_invalid_username_error_text()
            expected_error_invalid_username = error_msg + " '" + username + "'"
            self.logger.info(f"expected invalid username error: {expected_error_invalid_username}")
            if expected_error_invalid_username in actual_invalid_username_error_msg.text:
                self.status.append(True)
            else:

                self.status.append(False)
            time.sleep(web_driver.one_second)
            invalid_username_alert = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_close_invalid_username_alert_by_xpath())
            invalid_username_alert = self.wait_for_element_to_appear(invalid_username_alert, Portal_login_page_read_ini().get_close_invalid_username_alert_by_xpath())
            invalid_username_alert.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_29.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_29.png")
                logout_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn = self.wait_for_element_to_appear(logout_btn, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn.click()
                time.sleep(web_driver.one_second)
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_29_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_29_exception.png")
            self.logger.error(f"TC_Portal_Login_29 got an exception as: {ex}")

    def verify_user_account_blocked_for_30_min_if_user_enter_wrong_password_for_6_times_verify_message_warning(self):
        try:
            self.logger.info("********** TC_Portal_Login_30 started ********")
            self.logger.info("verify_user_account_blocked_for_30_min_if_user_enter_wrong_password_for_6_times_verify_message_warning")
            print("verify_user_account_blocked_for_30_min_if_user_enter_wrong_password_for_6_times_verify_message_warning")
            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            for x in range(7):
                time.sleep(web_driver.one_second)
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath()).clear()
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath()).send_keys(Portal_login_page_read_ini().get_portal_login_username())
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath()).send_keys(Portal_login_page_read_ini().get_portal_login_invalid_password())
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath()).click()
                time.sleep(web_driver.one_second)
                self.logger.info(f"Wrong password entered count: {x}")
            time.sleep(web_driver.one_second)
            actual_account_blocked_msg = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_invalid_password_text_on_alert_by_xpath()).text
            self.logger.info(f"actual account blocked message: {actual_account_blocked_msg}")
            expected_account_blocked_msg = Portal_login_page_read_ini().get_account_blocked_message_after_entering_invalid_password_six_times()
            self.logger.info(f"expected message: {expected_account_blocked_msg}")
            time.sleep(web_driver.one_second)
            if expected_account_blocked_msg in actual_account_blocked_msg:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_close_invalid_password_alert_by_xpath()).click()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_30.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_30.png")
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath()).click()
                time.sleep(web_driver.one_second)
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_30_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_30_exception.png")
            self.logger.error(f"TC_Portal_Login_30 got an exception as: {ex}")

    def verify_user_account_unblocked_after_30_min_if_wrong_password_for_6_times(self):
        try:
            self.logger.info("********** TC_Portal_Login_31 started ********")
            self.logger.info("verify_user_account_unblocked_after_30_min_if_wrong_password_for_6_times")
            print("verify_user_account_unblocked_after_30_min_if_wrong_password_for_6_times")
            
            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            self.status.clear()
            username = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username.clear()
            time.sleep(web_driver.one_second)
            username.send_keys(Portal_login_page_read_ini().get_portal_login_username())
            self.logger.info(f"Entered username which is blocked before 30min.: {Portal_login_page_read_ini().get_portal_login_username()}")
            password = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password.clear()
            time.sleep(web_driver.one_second)
            password.send_keys(Portal_login_page_read_ini().get_portal_login_password())
            self.logger.info(f"Entered password for above user: {Portal_login_page_read_ini().get_portal_login_password()}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath()).click()
            actual_account_blocked_msg = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_invalid_password_text_on_alert_by_xpath())
            time.sleep(web_driver.one_second)
            if actual_account_blocked_msg.is_displayed():
                self.status.append(False)
                self.logger.info("account blocked !!!!")
            else:
                self.status.append(True)
                self.logger.info("Login successful !!!")
                self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath()).click()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_31.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_31.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_31_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_31_exception.png")
            self.logger.error(f"TC_Portal_Login_31 got an exception as: {ex}")

    def Verify_user_login_whose_user_role_is_disabled_verify_error_messages(self):
        try:
            self.logger.info("*********TC_030****** started")
            self.load_portal_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.one_second)
            username_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox = self.wait_for_element_to_appear(username_textbox, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            username_textbox.clear()
            time.sleep(web_driver.one_second)
            username_textbox.send_keys(Portal_login_page_read_ini().diabled_username())

            self.logger.info(f"Entered username as: {Portal_login_page_read_ini().get_portal_login_username()}")
            time.sleep(web_driver.one_second)
            password_textbox = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox = self.wait_for_element_to_appear(password_textbox, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath())
            password_textbox.send_keys(Portal_login_page_read_ini().get_portal_login_password())
            self.logger.info(f"Entered password as: {Portal_login_page_read_ini().get_portal_login_password()}")
            time.sleep(web_driver.one_second)

            login_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn = self.wait_for_element_to_appear(login_btn, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            login_btn.click()
            time.sleep(web_driver.two_second)
            user_disabled_message = self.d.find_element(By.XPATH, Portal_login_page_read_ini().disabled_error_message())
            if user_disabled_message.is_displayed():
                self.logger.info("disabled error message is visible")
                self.status.append(True)
            else:
                self.logger.info("disabled error message is not visible")
                self.status.append(False)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_33.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_33.png")
                logout_btn = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn = self.wait_for_element_to_appear(logout_btn, Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
                logout_btn.click()
                time.sleep(web_driver.one_second)
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Portal_Login_33_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Portal_Login_33_exception.png")
            self.logger.error(f"TC_Portal_Login_31 got an exception as: {ex}")

    def verify_facefirst_logo_visible_and_its_dimentions_are_as_expected(self):
        try:
            self.logger.info("******TC_031****** started")
            self.load_portal_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.one_second)
            # to get dimensions of facefirst logo
            actual_dimensions_of_logo = self.d.find_elements(By.XPATH, Portal_login_page_read_ini().get_face_first_company_logo_by_xpath())
            actual_dimensions_of_logo = self.wait_for_element_to_appear(actual_dimensions_of_logo, Portal_login_page_read_ini().get_face_first_company_logo_by_xpath())
            self.logger.info(f"logo size: {actual_dimensions_of_logo.size}")
            print(actual_dimensions_of_logo.size)

            # reading Expected dimensions of logo
            Expected_dimensions_of_logo = Portal_login_page_read_ini().Expected_dimensions_of_logo()
            print(Expected_dimensions_of_logo)
            self.logger.info(f"expected: {Expected_dimensions_of_logo}")

            # verifying expected dimensions and actual dimensions
            if str(actual_dimensions_of_logo.size) == str(Expected_dimensions_of_logo):
                self.logger.info("actual dimensions and expected dimensions are equal")
                self.status.append(True)
            else:
                self.logger.info("actual and expected dimensions are not equal")
                self.status.append(False)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_portal_login_031_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_portal_login_031_failed.png")

                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_portal_login_031_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_portal_login_034.png")
            self.logger.error(f"TC_portal_login_034 got exception as: {ex} ")

    def verify_facefirst_login_page_background_colors_blue_white_and_black_visible_as_expected(self):
        try:
            self.logger.info("********TC_032 started********")
            self.load_portal_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.one_second)
            # verifying background colour blue
            # HEX_COLOUR = Color.from_string('#135795')
            # print(HEX_COLOUR)

            blue_background_colour = Color.from_string(self.d.find_element(By.ID, 'login-screen').value_of_css_property('background-color'))
            print(blue_background_colour)
            # blue_colour_button = Color.from_string(self.d.find_element(By.ID, 'login-screen').value_of_css_property('color'))
            # print(blue_colour_button)
            time.sleep(web_driver.one_second)
            if blue_background_colour.rgba == Portal_login_page_read_ini().Blue_color_rgba():
                self.logger.info("blue colour rgba value is visible")
                self.status.append(True)
            else:
                self.logger.info("blue color rgba value is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            white_background_colour = Color.from_string(self.d.find_element(By.ID, 'center-login-strip').value_of_css_property('background-color'))
            print(white_background_colour)
            if white_background_colour.rgba == Portal_login_page_read_ini().white_color_rgba():
                self.logger.info("white colour rgba value is visible")
                self.status.append(True)
            else:
                self.logger.info("white color rgba value is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            black_background_colour = Color.from_string(self.d.find_element(By.ID, 'login-link').value_of_css_property('background-color'))
            print(black_background_colour)
            time.sleep(web_driver.one_second)
            if black_background_colour.rgba == Portal_login_page_read_ini().black_color_rgba():
                self.logger.info("black colour rgba is visible")
                self.status.append(True)
            else:
                self.logger.info("black colour rgba is not visible")
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_portal_login_035.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_portal_login_035.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_portal_login_035.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_portal_login_035.png")
            self.logger.error(f"TC_portal_login_035 got exception as: {ex} ")

    def verify_facefirst_login_page_font_type(self):
        try:
            self.logger.info("********TC_036******** started")
            self.load_portal_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.one_second)
            font_type = self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_events_button_on_portal_by_xpath()).value_of_css_property("font-family")
            print(font_type)
            print(Portal_login_page_read_ini().font_type())
            if Portal_login_page_read_ini().font_type() in font_type:
                self.logger.info("font-type is visible")
                self.status.append(True)
            else:
                self.logger.info("font-type is not visible")
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_portal_login_036.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_portal_login_036.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_portal_login_036.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_portal_login_036.png")
            self.logger.error(f"TC_portal_login_036 got exception as: {ex} ")
    '''
    def verify_unsuccessful_login_with_multiple_browsers_account_should_be_blocked_for_6_onsicutive_login_attempts_with_invalid_password(self):
        try:

            self.logger.info("*****TC_038******** started")
            status = []
            login_url_obj = Base_Package.Login_Logout_Ops.login()

            edge_driver = selenium.webdriver.Edge()
            time.sleep(web_driver.one_second)
            firefox_driver = selenium.webdriver.Firefox()
            time.sleep(web_driver.one_second)
            print(login_url_obj.cloud_url)
            edge_driver.get(login_url_obj.cloud_url)
            time.sleep(web_driver.one_second)
            username = edge_driver.find_element(By.XPATH,Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            time.sleep(web_driver.one_second)
            password = edge_driver.find_element(By.XPATH,Portal_login_page_read_ini().get_portal_password_label_on_password_textbox())
            time.sleep(web_driver.one_second)
            login_btn = edge_driver.find_element(By.XPATH,Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            time.sleep(web_driver.one_second)
            username.send_keys(Portal_login_page_read_ini().get_portal_login_invalid_username())
            time.sleep(web_driver.one_second)
            password.send_keys(Portal_login_page_read_ini().get_portal_login_invalid_password())
            time.sleep(web_driver.one_second)
            login_btn.click()
            time.sleep(web_driver.one_second)
            cloud_menu = edge_driver.find_elements(Portal_login_page_read_ini().get_cloud_menu_on_dashboard_by_xpath())
            time.sleep(web_driver.one_second)
            if len(cloud_menu) > 0:
                status.append(True)
            else:
                status.append(False)
            logout_btn = edge_driver.find_element(By.XPATH,Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
            time.sleep(web_driver.one_second)
            logout_btn.click()
            edge_driver.close()

            firefox_driver.get(login_url_obj.cloud_url)
            time.sleep(web_driver.one_second)

            username = firefox_driver.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath())
            time.sleep(web_driver.one_second)
            password = firefox_driver.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_password_label_on_password_textbox())
            time.sleep(web_driver.one_second)
            login_btn = firefox_driver.find_element(By.XPATH,
                                                 Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath())
            time.sleep(web_driver.one_second)
            username.send_keys(Portal_login_page_read_ini().get_portal_login_invalid_username())
            time.sleep(web_driver.one_second)
            password.send_keys(Portal_login_page_read_ini().get_portal_login_invalid_password())
            time.sleep(web_driver.one_second)
            login_btn.click()
            time.sleep(web_driver.one_second)
            cloud_menu = edge_driver.find_elements(Portal_login_page_read_ini().get_cloud_menu_on_dashboard_by_xpath())
            time.sleep(web_driver.one_second)
            if len(cloud_menu) > 0:
                status.append(True)
            else:
                status.append(False)
            logout_btn = edge_driver.find_element(By.XPATH,
                                                  Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath())
            time.sleep(web_driver.one_second)
            logout_btn.click()
            time.sleep(web_driver.one_second)
            edge_driver.close()
        except Exception as ex:
            print(ex.args)
    '''
    def verify_unsuccessful_login_with_multiple_browsers_account_should_be_blocked_for_6_consicutive_login_attempts_with_invalid_password(self):
        try:
            self.d_edge = webdriver.Edge()
            self.d_edge.get(Portal_login_page_read_ini().get_portal_url())
            time.sleep(5)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath()).clear()
            time.sleep(web_driver.three_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath()).send_keys(Portal_login_page_read_ini().diabled_username())
            self.logger.info(f"Entered username as: {Portal_login_page_read_ini().get_portal_login_username()}")
            time.sleep(web_driver.three_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath()).send_keys(Portal_login_page_read_ini().get_portal_login_password())
            self.logger.info(f"Entered password as: {Portal_login_page_read_ini().get_portal_login_password()}")
            time.sleep(web_driver.three_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath()).click()
            time.sleep(web_driver.three_second)
            self.d_firefox = webdriver.Firefox()
            self.d_firefox.get(Portal_login_page_read_ini().get_portal_url())
            time.sleep(10)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath()).clear()
            time.sleep(web_driver.three_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath()).send_keys(Portal_login_page_read_ini().diabled_username())
            self.logger.info(f"Entered username as: {Portal_login_page_read_ini().get_portal_login_username()}")
            time.sleep(web_driver.three_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath()).send_keys(Portal_login_page_read_ini().get_portal_login_password())
            self.logger.info(f"Entered password as: {Portal_login_page_read_ini().get_portal_login_password()}")
            time.sleep(web_driver.three_second)
            self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath()).click()
            time.sleep(web_driver.three_second)

        except Exception as ex:
            print(ex)

    def load_portal_login_page_if_not_loaded(self):
        try:
            # self.logger.info(f"url: {self.d.current_url}")
            if self.d.title == Portal_login_page_read_ini().get_portal_title():
                pass
            else:
                self.d.get(Portal_login_page_read_ini().get_portal_url())
                self.d.maximize_window()
                # time.sleep(web_driver.two_second)
                # self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_advance_btn_by_xpath()).click()
                # self.logger.info("clicked on advance")
                # time.sleep(web_driver.one_second)
                # self.logger.info(f"proceed link xpath: {Portal_login_page_read_ini().get_proceed_link_by_xpath()}")
                # self.d.find_element(By.XPATH, Portal_login_page_read_ini().get_proceed_link_by_xpath()).click()
                # self.logger.info("clicked on proceed link")
                time.sleep(web_driver.one_second)
                for i in range(4):
                    pyautogui.hotkey('ctrl', '-')
                    time.sleep(0.5)

        except Exception as ex:
            self.logger.error(ex)

# print(Portal_Login_Page_Pom().open_portal_url_and_verify_expected_url_is_visible_verify_expected_page_title_is_visible_and_verify_face_first_logo_is_visible())
# print(Portal_Login_Page_Pom().verify_username_textbox_is_visible_and_clickable_username_label_on_it_is_visible())
# print(Portal_Login_Page_Pom().verify_password_textbox_is_visible_and_clickable_password_label_on_it_is_visible())
# print(Portal_Login_Page_Pom().verify_cloud_login_button_is_visible_and_clickable_cloud_login_text_on_it_is_visible_click_on_cloud_login_and_verify_missing_username_msg_is_visible())
# print(Portal_Login_Page_Pom().verify_events_button_is_visible_and_clickable_text_and_exclamatory_icon_on_it_both_are_visible_click_on_events_and_verify_missing_username_msg_is_visible())
# print(Portal_Login_Page_Pom().verify_identify_enroll_button_is_visible_and_clickable_text_and_camera_icon_on_it_both_are_visible_click_on_identify_enroll_and_verify_missing_username_mgs_is_visible())
# print(Portal_Login_Page_Pom().verify_users_button_is_visible_and_clickable_text_and_male_icon_on_it_both_are_visible_click_on_users_and_verify_missing_username_msg_is_visible())
# print(Portal_Login_Page_Pom().verify_account_button_is_visible_and_clickable_text_and_lock_icon_on_it_both_are_visible_click_on_account_button_and_verify_missing_username_msg_is_visible())
# print(Portal_Login_Page_Pom().verify_switch_language_button_is_visible_and_clickable_text_on_it_is_visible_click_on_switch_language_and_verify_box_is_visible_click_cancel_button_on_dialog_box())
# print(Portal_Login_Page_Pom().verify_face_first_copy_rights_is_visible_and_clickable_click_on_copyrights_and_verify_versions_of_webapi_and_server_both_are_visible_verify_latest_version_of_webapi_and_server_is_appeared())
# print(Portal_Login_Page_Pom().verify_user_login_with_valid_credentials_and_click_on_cloud_login_and_verify_it_is_navigating_to_cloud_menu_panel())
# print(Portal_Login_Page_Pom().verify_user_login_with_valid_credentials_and_click_on_events_button_and_verify_it_is_navigating_to_events_panel())
# print(Portal_Login_Page_Pom().verify_user_login_with_valid_credentials_and_click_on_identify_enroll_button_and_verify_it_is_navigating_to_identify_enroll_panel())
# print(Portal_Login_Page_Pom().verify_user_login_with_valid_credentials_and_click_on_users_button_and_verify_it_is_navigating_to_users_panel())
# print(Portal_Login_Page_Pom().verify_user_login_with_valid_credentials_and_click_on_account_and_verify_it_is_navigating_to_account_panel())
# print(Portal_Login_Page_Pom().click_on_switch_language_and_verify_switch_language_text_is_visible_english_spanish_arabic_portuguese_text_is_visible_verify_cancel_button_is_visible_and_clickable())
# print(Portal_Login_Page_Pom().verify_radio_button_before_english_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_english_language())
# print(Portal_Login_Page_Pom().verify_radio_button_before_spanish_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_spanish_language())
# print(Portal_Login_Page_Pom().verify_radio_button_before_arabic_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_arabic_language())
# print(Portal_Login_Page_Pom().verify_radio_button_before_portuguese_is_visible_and_clickable_click_on_radio_button_and_verify_text_is_visible_in_portuguese_language())
# print(Portal_Login_Page_Pom().on_version_info_verify_close_button_is_visible_and_clickable_text_on_it_is_visible_click_on_close_button_and_verify_version_info_closed())
# print(Portal_Login_Page_Pom().verify_user_login_with_valid_username_and_valid_password_verify_message_warning())
# print(Portal_Login_Page_Pom().verify_user_login_with_valid_user_name_and_incorrect_password_verify_message_warning())
# print(Portal_Login_Page_Pom().verify_user_login_with_invalid_username_and_valid_password_verify_message_warning())
# print(Portal_Login_Page_Pom().verify_user_login_with_invalid_username_and_invalid_password_verify_message_warning())
# print(Portal_Login_Page_Pom().verify_user_login_missing_username_and_entering_password_verify_message_warning())
# print(Portal_Login_Page_Pom().verify_user_login_with_username_without_entering_password_verify_message_warning())
# print(Portal_Login_Page_Pom().verify_user_login_without_username_and_without_password_verify_message_warning())
# print(Portal_Login_Page_Pom().verify_user_login_with_invalid_user_user_that_is_not_present_in_system_verify_message_warning())
# print(Portal_Login_Page_Pom().verify_user_account_blocked_for_30_min_if_user_enter_wrong_password_for_6_times_verify_message_warning())
# print(Portal_Login_Page_Pom().verify_user_account_unblocked_after_30_min_if_wrong_password_for_6_times())
