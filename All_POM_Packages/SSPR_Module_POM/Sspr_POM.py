import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login
from All_Config_Packages._21_SSPR_Config_Fiels.Sspr_Read_INI import sspr_read_ini

class SSPR_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    def open_portal_login_page_enter_username_password_and_click_on_login_btn_verify_password_reset_pop_up_displayed(self):
        try:
            self.logger.info("********************************** TC_SSPR_02 Started *******************************")
            self.status.clear()
            self.open_portal_url_if_not_open()
            self.enter_username_password_and_click_on_login()
            self.verify_password_change_pop_up_is_displayed()
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_SSPR_02 end  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SSPR_02_failed.png")
                return False
            else:
                self.d.refresh()
                return True
        except Exception as ex:
            self.logger.info(f"open_portal_login_page_enter_username_password_and_click_on_login_btn_verify_password_reset_pop_up_displayed ex: {ex.args}")
            self.logger.info(f"ex: {type(ex).__name__}")
            self.d.refresh()

    def verify_password_length_should_not_accept_less_than_8(self):
        try:
            self.logger.info("********************************** TC_SSPR_08 Started *******************************")
            self.status.clear()
            self.open_portal_url_if_not_open()
            self.enter_username_password_and_click_on_login()
            password = "abcd123"
            self.enter_new_password(password)
            time.sleep(web_driver.one_second)
            self.enter_confirm_password(password)
            time.sleep(web_driver.one_second)
            self.click_on_submit_btn()
            time.sleep(web_driver.one_second)
            # self.click_on_login_link()
            self.verify_error_message()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_SSPR_08 end  **************")
            time.sleep(web_driver.one_second)
            if self.status is None:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SSPR_08_failed.png")
                return False
            else:
                if False in self.status:
                    self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SSPR_08_failed.png")
                    return False
                else:
                    time.sleep(web_driver.one_second)
                    self.d.refresh()
                    return True
        except Exception as ex:
            self.logger.info(f"verify password length should not accept less than 8  ex: {ex.args}")
            self.d.refresh()

    def verify_password_combination_alphabets_capital_small_digits_and_symbol_accepted_successfully(self):
        try:
            self.logger.info("********************************** TC_SSPR_09 Started *******************************")
            self.status.clear()
            self.open_portal_url_if_not_open()
            time.sleep(web_driver.one_second)
            self.enter_username_password_and_click_on_login()
            time.sleep(web_driver.one_second)
            password = sspr_read_ini().get_new_password()
            self.enter_new_password(password)
            time.sleep(web_driver.one_second)
            self.enter_confirm_password(password)
            time.sleep(web_driver.one_second)
            self.click_on_submit_btn()
            time.sleep(web_driver.one_second)
            # self.click_on_login_link()
            self.verify_successful_login_post_password_change()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_SSPR_09 end  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_SSPR_09_failed.png")
                return False
            else:
                time.sleep(web_driver.one_second)
                self.d.refresh()
                return True
        except Exception as ex:
            self.logger.info(f"verify_password_combination_alphabets_capital_small_digits_and_symbol_accepted_successfully ex: {ex.args}")
            self.logger.info(f"ex: {type(ex).__name__}")
            self.d.refresh()


    # **************************** User Methods ****************************************

    def verify_successful_login_post_password_change(self):
        try:
            success_msg = self.explicit_wait(10, "XPATH",
                                         sspr_read_ini().password_change_success_message_by_xpath(),
                                         self.d)
            self.logger.info(f"error msg displayed : {success_msg.is_displayed()}")
            if success_msg.is_displayed():
                self.logger.info(f"error msg: {success_msg.text}")
                self.status.append(True)
            else:
                self.status.append(False)
        except Exception as ex:
            self.logger.info(f"verify_successful_login_post_password_change ex: {ex.args}")
            self.status.append(False)
            self.d.refresh()

    def verify_error_message(self):
        try:
            err_msg = self.explicit_wait(10, "XPATH", sspr_read_ini().password_must_contain_8to20_characters_error_msg_by_xpath(), self.d)
            self.logger.info(f"error msg displayed : {err_msg.is_displayed()}")
            if err_msg.is_displayed():
                self.logger.info(f"error msg: {err_msg.text}")
                self.status.append(True)
            else:
                self.status.append(False)

        except Exception as ex:
            self.logger.info(f"verify_error_message {ex.args}")
            self.status.append(False)
            self.d.refresh()

    def click_on_submit_btn(self):
        try:
            submit_btn = self.explicit_wait(5, "XPATH", sspr_read_ini().submit_btn_on_popup_by_xpath(),
                                                       self.d)
            self.logger.info(f"new password text box is visible: {submit_btn.is_displayed()}")
            if submit_btn.is_displayed():
                submit_btn.click()
        except Exception as ex:
            self.logger.info(f"click_on_submit_btn {ex.args}")

    def enter_new_password(self, password):
        try:
            new_password_text_box = self.explicit_wait(5, "XPATH", sspr_read_ini().new_password_textbox_by_xpath(), self.d)
            self.logger.info(f"new password text box is visible: {new_password_text_box.is_displayed()}")
            if new_password_text_box.is_displayed():
                new_password_text_box.send_keys(password)
        except Exception as ex:
            self.logger.info(f"enter_new_password {ex.args}")

    def enter_confirm_password(self, password):
        try:
            confirm_password_text_box = self.explicit_wait(5, "XPATH", sspr_read_ini().confirm_password_text_box_by_xpath(),
                                                       self.d)
            self.logger.info(f"new password text box is visible: {confirm_password_text_box.is_displayed()}")
            if confirm_password_text_box.is_displayed():
                confirm_password_text_box.send_keys(password)
        except Exception as ex:
            self.logger.info(f"enter_confirm_password ex: {ex.args}")

    def verify_password_change_pop_up_is_displayed(self):
        try:
            self.explicit_wait(5, "XPATH", sspr_read_ini().change_password_popup_by_xpath(), self.d)
            password_change_pop_up = self.d.find_elements(By.XPATH, sspr_read_ini().change_password_popup_by_xpath())
            if len(password_change_pop_up) > 0:
                if password_change_pop_up[0].is_displayed():
                    self.logger.info(f"password change pop up is visible: {password_change_pop_up[0].is_displayed()}")
                    self.status.append(True)
                else:
                    self.logger.info(f"password change pop up is not visible")
                    self.status.append(False)
            else:
                self.logger.info("password change pop up not displayed or not found")

        except Exception as ex:
            self.logger.info(f"verify_password_change_pop_up_is_displayed ex: {ex.args}")

    def enter_username_password_and_click_on_login(self):
        try:
            username = sspr_read_ini().get_username()
            password = sspr_read_ini().get_password()
            username_text_box = self.explicit_wait(5, "XPATH", sspr_read_ini().get_username_text_box_by_xpath(), self.d)
            password_text_box = self.explicit_wait(5, "XPATH", sspr_read_ini().password_textbox_by_xpath(), self.d)
            login_link = self.explicit_wait(5, "XPATH", sspr_read_ini().login_link_by_xpath(), self.d)

            if username_text_box.is_displayed():
                username_text_box.click()
                username_text_box.clear()
                username_text_box.send_keys(username)
                self.logger.info(f"username entered")
            if password_text_box.is_displayed():
                password_text_box.click()
                password_text_box.clear()
                password_text_box.send_keys(password)
                self.logger.info(f"password entered")
            if login_link.is_displayed():
                self.logger.info(f"login link is visible.")
                login_link.click()
        except Exception as ex:
            self.logger.info(f"enter_username_password_and_click_on_login ex: {ex.args}")

    def open_portal_url_if_not_open(self):
        try:
            cloud_url = sspr_read_ini().get_cloud_url()
            self.logger.info(f"cloud url: {cloud_url}")
            if self.d.current_url == cloud_url:
                username_text_box = self.d.find_elements(By.XPATH, sspr_read_ini().get_username_text_box_by_xpath())
                if len(username_text_box) > 0:
                    if username_text_box[0].is_displayed():
                        self.logger.info(f"username textbox is visible.")
                else:
                    self.logger.info("username textbox not visible")
                    logout_btn = self.d.find_elements(By.XPATH, sspr_read_ini().logout_btn_by_xpath())
                    if len(logout_btn) > 0:
                        if logout_btn[0].is_displayed():
                            logout_btn[0].click()
                    else:
                        self.logger.info("Logout btn is not visible.")

            else:
                self.d.get(cloud_url)
                self.d.maximize_window()

        except Exception as ex:
            self.logger.info(f"open_portal_url_if_not_open ex: {ex.args}")

