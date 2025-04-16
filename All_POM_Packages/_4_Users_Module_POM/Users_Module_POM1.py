import random
import time
from pathlib import Path

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from All_Config_Packages._4_Users_Module_Config_Files.Users_Read_INI import Read_Users_Components
from All_Config_Packages._4_Users_Module_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
# from All_Config_Packages._0_login_logout_config_File.login_logout_Read_INI import Login_logout_Read_ini
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login,logout,web_logger

driver = web_driver.d
action = ActionChains(driver)



def move_to_element(web_element):
    """
    moves the mouse cursor to a particular element
    :param web_element:
    :return:
    """
    action.move_to_element(web_element).perform()


def scroll_to_element(web_element):
    """
    scrolls the scrollbar to the particular element
    :param web_element:
    :return:
    """
    action.scroll_to_element(web_element).perform()


def javascript_executor_click(web_element):
    """
    click on a web element
    :param web_element:
    :return:
    """
    driver.execute_script("arguments[0].click();", web_element)


def select_options_visible_text(web_element, visible_text):
    """
    handles a drop-down using visible text
    :param web_element:
    :param visible_text: provide the visible text of the web element
    :return:
    """
    select = Select(web_element)
    select.select_by_visible_text(visible_text)


def select_options_value(web_element, value):
    """
    handles drop-down using value
    :param web_element:
    :param value: provide the value present in the value attribute
    :return:
    """
    select = Select(web_element)
    select.select_by_value(value)


def generate_random_number():
    return random.randint(1, 10000)


class Users_Module_pom(web_driver,web_logger):

    d = web_driver.d
    log = web_logger.logger_obj()
    screenshots_path = f"{Path(__file__).parent.parent.parent}\\Reports\\Screenshots\\"

    def wait_for_element_to_appear(self, element_list, xpath):
        count = 0
        if len(element_list) == 0:
            while len(element_list) == 0 or count == 10:
                element_list = self.d.find_elements(By.XPATH, xpath)
                time.sleep(web_driver.one_second)
                if len(element_list) > 0:
                    self.log.info("element is visible...")
                    return element_list[0]
                else:
                    self.log.info("waiting for element...")
                count += 1
                self.log.info(f"wait count: {count}")
        else:
            self.log.info(f"element length: {len(element_list)}")
            return element_list[0]

    def login(self):
        if self.d.title == "" or self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())\
                .is_displayed():
            self.login_before()

    def login_before(self):

        try:
            self.d.get(Read_Portal_Menu_Components().get_url())
            time.sleep(web_driver.one_second)
            username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            if not username.is_displayed():
                self.d.get(Read_Portal_Menu_Components().get_url())
            time.sleep(web_driver.one_second)
            username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            username.send_keys(Read_Portal_Menu_Components().get_username())
            password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
            password.send_keys(Read_Portal_Menu_Components().get_password())
            login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
            javascript_executor_click(login_btn)
            time.sleep(web_driver.one_second)

        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}login_failed_for_users_menu_failed.png")
            self.log.info(f"login_before_failed: {ex}")
            return False

    def verify_user_able_to_view_the_user_on_cloud_menu(self):
        try:
            ex_result = [True, True]
            ac_result = []
            login().login_to_cloud_if_not_done()
            time.sleep(web_driver.one_second)
            users_menu = self.d.find_element(By.XPATH, Read_Users_Components().users_cloud_menu_by_xpath())
            ac_result.append(users_menu.is_displayed())
            time.sleep(web_driver.one_second)
            exp = Read_Users_Components().users_cloud_menu_validation_text()
            act = users_menu.text
            self.log.info(f"Text Expected : {exp}")
            self.log.info(f"Text Displayed : {act}")
            time.sleep(web_driver.one_second)
            ac_result.append(users_menu.text == Read_Users_Components().users_cloud_menu_validation_text())
            if ex_result == ac_result:
                time.sleep(web_driver.one_second)
                return True
            else:
                time.sleep(web_driver.one_second)
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_001_failed.png")
                return False
        except Exception as ex:
            time.sleep(web_driver.one_second)
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_001_exception.png")
            self.log.info(f"test_TC_US_001_exception: {ex}")
            return False
        finally:
            logout().logout_from_core()

    def verify_user_opens_user_then_users_panel_should_display(self):
        try:
            ex_result = [True, True]
            ac_result = []
            login().login_to_cloud_if_not_done()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            users_panel = self.d.find_element(By.XPATH, Read_Users_Components().users_panel_title_by_xpath())
            ac_result.append(users_panel.is_displayed())
            ac_result.append(users_panel.text == Read_Users_Components().users_panel_title_validation_text())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_002_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_002_exception.png")
            self.log.info(f"test_TC_US_002_exception: {ex}")
            return False
        finally:
               logout().logout_from_core()

    def verify_user_able_to_see_and_open_action_dropdown(self):
        try:
            ex_result = [True, True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            action_btn = self.d.find_element(By.XPATH, Read_Users_Components().action_dropdown_by_xpath())
            ac_result.append(action_btn.text == Read_Users_Components().action_dropdown_validation_text())
            ac_result.append(action_btn.is_displayed())
            ac_result.append(action_btn.is_enabled())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_003_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_003_exception.png")
            self.log.info(f"test_TC_US_003_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_users_able_to_see_refresh(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            action_btn = self.d.find_element(By.XPATH, Read_Users_Components().action_dropdown_by_xpath())
            action_btn.click()
            refresh = self.d.find_element(By.XPATH, Read_Users_Components().refresh_by_xpath())
            ac_result.append(refresh.text == Read_Users_Components().refresh_validation_text())
            ac_result.append(refresh.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_004_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_004_exception.png")
            self.log.info(f"test_TC_US_004_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_create_user(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            action_btn = self.d.find_element(By.XPATH, Read_Users_Components().action_dropdown_by_xpath())
            action_btn.click()
            create_user = self.d.find_element(By.XPATH, Read_Users_Components().create_user_by_xpath())
            ac_result.append(create_user.text == Read_Users_Components().create_user_validation_text())
            ac_result.append(create_user.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_005_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_005_exception.png")
            self.log.info(f"test_TC_US_005_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_delete_selected_user(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_btn()
            delete_user = self.d.find_element(By.XPATH, Read_Users_Components().delete_selected_user_by_xpath())
            ac_result.append(delete_user.text == Read_Users_Components().delete_selected_user_validation_text())
            ac_result.append(delete_user.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_006_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_006_exception.png")
            self.log.info(f"test_TC_US_006_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_clicks_refresh_then_it_should_refresh_the_users_list(self):
        try:
            ex_result = [True, True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            refresh = self.d.find_element(By.XPATH, Read_Users_Components().refresh_by_xpath())
            ac_result.append(refresh.is_enabled())
            try:
                self.click_on_action_refresh_option()
                ac_result.append(True)
            except Exception as e:
                ac_result.append(False)
                self.log.info(e)
            updating_indicator = self.d.find_element(By.XPATH, Read_Users_Components().updating_indicator_by_xpath())
            ac_result.append(updating_indicator.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_007_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_007_exception.png")
            self.log.info(f"test_TC_US_007_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_clicks_create_user_user_panel_should_be_displayed(self):
        try:
            ex_result = [True, True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            create_user = self.d.find_element(By.XPATH, Read_Users_Components().create_user_by_xpath())
            ac_result.append(create_user.is_enabled())
            self.click_on_action_create_user_option()
            user_panel_title = self.d.find_element(By.XPATH, Read_Users_Components().users_panel_title_by_xpath())
            ac_result.append(user_panel_title.text == Read_Users_Components().users_panel_title_validation_text())
            ac_result.append(user_panel_title.is_displayed())
            time.sleep(web_driver.one_second)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_008_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_008_exception.png")
            self.log.info(f"test_TC_US_008_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_title_new_user_details_face_first_is_visible(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            user_panel_header = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_header_by_xpath())
            ac_result.append(user_panel_header.text == Read_Users_Components().user_panel_header_validation_text())
            ac_result.append(user_panel_header.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_009_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_009_exception.png")
            self.log.info(f"test_TC_US_009_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_cancel_and_save_button_is_present(self):
        try:
            ex_result = [True, True, True, True, True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
            save = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_save_button_by_xpath())
            ac_result.append(cancel.text == Read_Users_Components().user_panel_cancel_btn_validation_text())
            ac_result.append(save.text == Read_Users_Components().user_panel_save_btn_validation_text())
            ac_result.append(cancel.is_displayed())
            ac_result.append(save.is_displayed())
            ac_result.append(cancel.is_enabled())
            ac_result.append(save.is_enabled())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_010_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_010_exception.png")
            self.log.info(f"test_TC_US_010_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_username_required_text_for_username(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            user_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().user_name_by_xpath())
            user_name_txt_bx.clear()
            error_msg = self.d.find_element(By.XPATH, Read_Users_Components().user_name_error_msg_by_xpath())
            ac_result.append(error_msg.text == Read_Users_Components().user_name_error_msg_validation_text())
            ac_result.append(error_msg.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_011_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_011_exception.png")
            self.log.info(f"test_TC_US_011_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_user_role_required_text_for_user_role(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            error_msg = self.d.find_element(By.XPATH, Read_Users_Components().user_role_error_msg())
            ac_result.append(error_msg.text == Read_Users_Components().user_role_error_msg_validation_text())
            ac_result.append(error_msg.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_012_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_012_exception.png")
            self.log.info(f"test_TC_US_012_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_password_required_and_confirm_password_required_text_for_password(self):
        try:
            ex_result = [True, True, True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            new_password = self.d.find_element(By.XPATH, Read_Users_Components().new_password_by_xpath())
            new_password.clear()
            error_msg = self.d.find_element(By.XPATH, Read_Users_Components().new_password_error_msg_by_xpath())
            ac_result.append(error_msg.text == Read_Users_Components().new_password_error_msg_validation_text())
            ac_result.append(error_msg.is_displayed())
            error_msg = self.d.find_element(By.XPATH, Read_Users_Components().confirm_password_error_msg_by_xpath())
            ac_result.append(error_msg.text == Read_Users_Components().confirm_password_error_msg_validation_text())
            ac_result.append(error_msg.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_013_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_013_exception.png")
            self.log.info(f"test_TC_US_013_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_region_required_text_for_region(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            error_msg = self.d.find_element(By.XPATH, Read_Users_Components().region_error_msg_by_xpath())
            ac_result.append(error_msg.text == Read_Users_Components().region_error_msg_validation_text())
            ac_result.append(error_msg.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_014_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_014_exception.png")
            self.log.info(f"test_TC_US_014_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_email_required_text_for_email(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            error_msg = self.d.find_element(By.XPATH, Read_Users_Components().email_error_msg_by_xpath())
            scroll_to_element(error_msg)
            ac_result.append(error_msg.text == Read_Users_Components().email_error_msg_validation_text())
            ac_result.append(error_msg.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_015_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_015_exception.png")
            self.log.info(f"test_TC_US_015_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_timezone_required_text_for_timezone(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            error_msg = self.d.find_element(By.XPATH, Read_Users_Components().time_zone_error_msg_by_xpath())
            scroll_to_element(error_msg)
            ac_result.append(error_msg.text == Read_Users_Components().time_zone_error_msg_validation_text())
            ac_result.append(error_msg.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_016_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_016_exception.png")
            self.log.info(f"test_TC_US_016_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_enabled_checkbox_is_selected(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            checkbox = self.d.find_element(By.XPATH, Read_Users_Components().enabled_by_xpath())
            checkbox_value = checkbox.get_attribute("class")
            ac_result.append("checked" in checkbox_value)
            ac_result.append(checkbox.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_017_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_017_exception.png")
            self.log.info(f"test_TC_US_017_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_select_disabled_checkbox(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            checkbox = self.d.find_element(By.XPATH, Read_Users_Components().disabled_by_xpath())
            checkbox.click()
            checkbox_value = checkbox.get_attribute("class")
            ac_result.append("checked" in checkbox_value)
            ac_result.append(checkbox.is_displayed())
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_018_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_018_exception.png")
            self.log.info(f"test_TC_US_018_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_username_textbox_and_fill_username(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().user_name_input_data()
            user_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().user_name_by_xpath())
            ac_result.append(user_name_txt_bx.is_enabled())
            user_name_txt_bx.send_keys(expected)
            actual = user_name_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_019_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_019_exception.png")
            self.log.info(f"test_TC_US_019_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_first_name_textbox_and_fill_first_name(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().first_name_input_data()
            first_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().first_name_by_xpath())
            ac_result.append(first_name_txt_bx.is_enabled())
            first_name_txt_bx.send_keys(expected)
            actual = first_name_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_020_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_020_exception.png")
            self.log.info(f"test_TC_US_020_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_last_name_textbox_and_fill_last_name(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().last_name_input_data()
            last_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().last_name_by_xpath())
            ac_result.append(last_name_txt_bx.is_enabled())
            last_name_txt_bx.send_keys(expected)
            actual = last_name_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_021_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_021_exception.png")
            self.log.info(f"test_TC_US_021_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_user_role_dropdown_is_present_and_choose_the_user_roles(self):
        try:
            result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            user_role = self.d.find_element(By.XPATH, Read_Users_Components().user_role_by_xpath())
            user_role.click()
            time.sleep(web_driver.one_second)
            user_role_ele_with_options_ele = self.d \
                .find_elements(By.XPATH, Read_Users_Components().user_role_options_by_xpath())
            user_role_ele_options = []
            for e in user_role_ele_with_options_ele:
                user_role_ele_options.append(e.text)
            select = Select(user_role)
            for e in user_role_ele_options:
                select.select_by_visible_text(e)
                time.sleep(web_driver.one_second)
                if not e == select.first_selected_option.text:
                    result.append(False)
                else:
                    result.append(True)
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_022_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_022_exception.png")
            self.log.info(f"test_TC_US_022_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_password_textbox_and_fill_password(self):
        try:
            ex_result = [True, True, True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().password_data_input()
            new_password = self.d.find_element(By.XPATH, Read_Users_Components().new_password_by_xpath())
            confirm_password = self.d.find_element(By.XPATH, Read_Users_Components().confirm_password_by_xpath())
            ac_result.append(new_password.is_enabled())
            ac_result.append(confirm_password.is_enabled())
            new_password.send_keys(expected)
            confirm_password.send_keys(expected)
            actual = new_password.get_attribute("value")
            ac_result.append(expected == actual)
            actual = confirm_password.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_023_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_023_exception.png")
            self.log.info(f"test_TC_US_023_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_company_textbox_and_enter_their_company_name(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().company_input_data()
            company_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().company_by_xpath())
            ac_result.append(company_txt_bx.is_enabled())
            company_txt_bx.send_keys(expected)
            actual = company_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_024_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_024_exception.png")
            self.log.info(f"test_TC_US_024_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_title_textbox_and_enter_title(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().title_input_data()
            title_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().title_by_xpath())
            ac_result.append(title_txt_bx.is_enabled())
            title_txt_bx.send_keys(expected)
            actual = title_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_025_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_025_exception.png")
            self.log.info(f"test_TC_US_025_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

    def verify_user_able_to_see_region_popup_and_choose_a_region(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            region = Read_Users_Components().region_data_input()
            self.select_region(region)
            if self.validate_region(region):
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_026_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_026_exception.png")
            self.log.info(f"test_TC_US_026_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_department_textbox_and_enter_their_department_name(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().department_input_data()
            department_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().department_by_xpath())
            ac_result.append(department_txt_bx.is_enabled())
            department_txt_bx.send_keys(expected)
            actual = department_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_027_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_027_exception.png")
            self.log.info(f"test_TC_US_027_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_email_textbox_and_enter_a_valid_email(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().email_input_data()
            email_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().email_by_xpath())
            ac_result.append(email_txt_bx.is_enabled())
            email_txt_bx.send_keys(expected)
            actual = email_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_028_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_028_exception.png")
            self.log.info(f"test_TC_US_028_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_alert_email_and_enter_a_valid_alert_email(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().alert_email_input_data()
            alert_email_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().alert_email_by_xpath())
            ac_result.append(alert_email_txt_bx.is_enabled())
            alert_email_txt_bx.send_keys(expected)
            actual = alert_email_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_029_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_029_exception.png")
            self.log.info(f"test_TC_US_029_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_alert_phone_number_and_enter_a_valid_phone_number(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().alert_phone_no_input_data()
            alert_ph_no_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().alert_phone_number_by_xpath())
            ac_result.append(alert_ph_no_txt_bx.is_enabled())
            alert_ph_no_txt_bx.send_keys(expected)
            actual = alert_ph_no_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_030_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_030_exception.png")
            self.log.info(f"test_TC_US_030_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_timezone_dropdown_and_select_a_timezone(self):
        try:
            result = True
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time_zone = self.d.find_element(By.XPATH, Read_Users_Components().time_zone_by_xpath())
            time_zone.click()
            time_zone_options_ele = self.d.find_elements(By.XPATH, Read_Users_Components().time_zone_options_by_xpath())
            time_zone_options = []
            select = Select(time_zone)
            for ele in time_zone_options_ele:
                value = ele.get_attribute("value")
                time_zone_options.append(value)
                select.select_by_value(value)
                ac = select.first_selected_option.get_attribute("value")
                if not value == ac:
                    result = False
                    break
            if result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_031_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_031_exception.png")
            self.log.info(f"test_TC_US_031_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_address_textbox_and_enter_their_address(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().address_input_data()
            address_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().address_by_xpath())
            ac_result.append(address_txt_bx.is_enabled())
            address_txt_bx.send_keys(expected)
            actual = address_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_032_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_032_exception.png")
            self.log.info(f"test_TC_US_032_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_address_2_textbox_and_enter_their_address(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().address2_input_data()
            address2_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().address2_by_xpath())
            ac_result.append(address2_txt_bx.is_enabled())
            address2_txt_bx.send_keys(expected)
            actual = address2_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_033_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_033_exception.png")
            self.log.info(f"test_TC_US_033_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_city_textbox_and_fill_it(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().city_input_data()
            city_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().city_by_xpath())
            ac_result.append(city_txt_bx.is_enabled())
            city_txt_bx.send_keys(expected)
            actual = city_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_034_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_034_exception.png")
            self.log.info(f"test_TC_US_034_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_state_textbox_and_fill_it(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().state_input_data()
            state_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().state_by_xpath())
            ac_result.append(state_txt_bx.is_enabled())
            state_txt_bx.send_keys(expected)
            actual = state_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_035_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_035_exception.png")
            self.log.info(f"test_TC_US_035_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_postal_code_textbox_and_fill_it(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().postal_code_input_data()
            postal_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().postal_code_by_xpath())
            ac_result.append(postal_txt_bx.is_enabled())
            postal_txt_bx.send_keys(expected)
            actual = postal_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_036_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_036_exception.png")
            self.log.info(f"test_TC_US_036_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_house_phone_number_textbox_and_enter_a_valid_phone_number(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().home_phone_no_input_data()
            ph_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().home_phone_number_by_xpath())
            ac_result.append(ph_txt_bx.is_enabled())
            ph_txt_bx.send_keys(expected)
            actual = ph_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_037_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_037_exception.png")
            self.log.info(f"test_TC_US_037_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_users_able_to_see_work_phone_number_textbox_and_enter_a_valid_work_phone_number(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().work_phone_no_input_data()
            ph_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().work_phone_number_by_xpath())
            ac_result.append(ph_txt_bx.is_enabled())
            ph_txt_bx.send_keys(expected)
            actual = ph_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_038_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_038_exception.png")
            self.log.info(f"test_TC_US_038_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_users_able_to_see_fax_phone_number_textbox_and_fill_it(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().fax_phone_no_input_data()
            ph_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().fax_phone_number_by_xpath())
            ac_result.append(ph_txt_bx.is_enabled())
            ph_txt_bx.send_keys(expected)
            actual = ph_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_039_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_039_exception.png")
            self.log.info(f"test_TC_US_039_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_phone_type_textbox_and_fill_it(self):
        try:
            ex_result = [True, True]
            ac_result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            expected = Read_Users_Components().phone_type_input_data()
            ph_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().phone_type_by_xpath())
            ac_result.append(ph_txt_bx.is_enabled())
            ph_txt_bx.send_keys(expected)
            actual = ph_txt_bx.get_attribute("value")
            ac_result.append(expected == actual)
            if ex_result == ac_result:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_040_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_040_exception.png")
            self.log.info(f"test_TC_US_040_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_phone_provider_dropdown_and_select_the_required_phone_provider(self):
        try:
            status = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            ph_prov_bx = self.d.find_element(By.XPATH, Read_Users_Components().phone_provider_drop_dwn_by_xpath())
            select = Select(ph_prov_bx)
            options = select.options
            self.log.info(options)
            for option in options:
                value = option.get_attribute("text")
                select.select_by_visible_text(value)
                time.sleep(web_driver.one_second)
                if not value == select.first_selected_option.text:
                    status.append(False)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_041_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_041.png")
            self.log.info(f"test_TC_US_041: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_alert_schedule_is_disabled(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            btn = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_btn_by_xpath())
            if not btn.is_enabled():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_042_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_042_exception.png")
            self.log.info(f"test_TC_US_042_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_notification_groups_is_disabled(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            btn = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_btn_by_xpath())
            if not btn.is_enabled():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_043_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_043_exception.png")
            self.log.info(f"test_TC_US_043_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_users_able_to_close_user_panel_on_clicking_cancel_button(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_list_by_xpath())
            panel_count = len(panel_list)
            cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
            cancel.click()
            panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_list_by_xpath())
            new_panel_count = len(panel_list)
            if new_panel_count < panel_count:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_044_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_044_exception.png")
            self.log.info(f"test_TC_US_044_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_users_able_to_close_users_pane(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
            cancel.click()
            close_btn = self.d.find_element(By.XPATH, Read_Users_Components().users_panel_close_panel_btn())
            javascript_executor_click(close_btn)
            users_cloud_menu = self.d. \
                find_element(By.XPATH, Read_Portal_Menu_Components().portal_menu_users_btn_by_xpath())
            if users_cloud_menu.is_displayed():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_045_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_045_exception.png")
            self.log.info(f"test_TC_US_045_exception: {ex}")
            return False

    def verify_user_fills_first_name_and_last_name_then_save_should_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_046_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_046_exception.png")
            self.log.info(f"test_TC_US_046_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_047_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_047_exception.png")
            self.log.info(f"test_TC_US_047_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_048_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_048_exception.png")
            self.log.info(f"test_TC_US_048_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_email_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_049_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_049_exception.png")
            self.log.info(f"test_TC_US_049_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_and_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_050_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_050_exception.png")
            self.log.info(f"test_TC_US_050_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

    def verify_user_fills_first_name_last_name_region_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_051_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_051_exception.png")
            self.log.info(f"test_TC_US_051_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_region_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_052_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_052_exception.png")
            self.log.info(f"test_TC_US_052_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_region_email_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_053_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_053.png")
            self.log.info(f"test_TC_US_053: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_and_password_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_054_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_054_exception.png")
            self.log.info(f"test_TC_US_054_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_mame_last_name_password_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_055_failed.png")
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_055_exception.png")
            self.log.info(f"test_TC_US_055_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_password_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_056_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_056_exception.png")
            self.log.info(f"test_TC_US_056_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_password_email_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_057_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_057.png")
            self.log.info(f"test_TC_US_057_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_password_and_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_058_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_058_exception.png")
            self.log.info(f"test_TC_US_058_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_password_region_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_059_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_059_exception.png")
            self.log.info(f"test_TC_US_059_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_password_region_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_060_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_060_exception.png")
            self.log.info(f"test_TC_US_060_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_last_name_password_region_email_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_061_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_061_exception.png")
            self.log.info(f"test_TC_US_061_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_and_user_role_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_062_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_062_exception.png")
            self.log.info(f"test_TC_US_062_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_063_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_063_exception.png")
            self.log.info(f"test_TC_US_063_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_064_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_064_exception.png")
            self.log.info(f"test_TC_US_064_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_email_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_065_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_065_exception.png")
            self.log.info(f"test_TC_US_065_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_and_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_066_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_066_exception.png")
            self.log.info(f"test_TC_US_066_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_region_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_067_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_067_exception.png")
            self.log.info(f"test_TC_US_067_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_region_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_068_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_068_exception.png")
            self.log.info(f"test_TC_US_068_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_region_email_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_069_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_069_exception.png")
            self.log.info(f"test_TC_US_069_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_and_password_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_070_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_070_exception.png")
            self.log.info(f"test_TC_US_070_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_password_and_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_071_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_071_exception.png")
            self.log.info(f"test_TC_US_071_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_password_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_072_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_072_exception.png")
            self.log.info(f"test_TC_US_072_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_password_email_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_073_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_073_exception.png")
            self.log.info(f"test_TC_US_073_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_password_and_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_074_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_074_exception.png")
            self.log.info(f"test_TC_US_074_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_first_name_last_name_user_role_password_region_time_zone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_075_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_075_exception.png")
            self.log.info(f"test_TC_US_075_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_first_name_last_name_user_role_password_region_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_076_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_076_exception.png")
            self.log.info(f"test_TC_US_076_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_first_name_last_name_user_role_password_region_email_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_077_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_077_exception.png")
            self.log.info(f"test_TC_US_077_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_and_last_name_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_078_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_078_exception.png")
            self.log.info(f"test_TC_US_078_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_and_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_079_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_079_exception.png")
            self.log.info(f"test_TC_US_079_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_080_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_080_exception.png")
            self.log.info(f"test_TC_US_080_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

    def user_fills_username_first_name_last_name_email_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_081_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_081_exception.png")
            self.log.info(f"test_TC_US_081_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_and_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_082_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_082_exception.png")
            self.log.info(f"test_TC_US_082_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_region_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_083_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_083_exception.png")
            self.log.info(f"test_TC_US_083_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_region_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_084_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_084_exception.png")
            self.log.info(f"test_TC_US_084_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_region_email_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_085_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_085_exception.png")
            self.log.info(f"test_TC_US_080_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_and_password_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_086_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_086_exception.png")
            self.log.info(f"test_TC_US_086_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_password_and_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_087_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_087_exception.png")
            self.log.info(f"test_TC_US_087_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_password_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_088_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_088_exception.png")
            self.log.info(f"test_TC_US_088_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_password_email_and_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_089_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_089_exception.png")
            self.log.info(f"test_TC_US_089_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_password_and_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_090_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_090_exception.png")
            self.log.info(f"test_TC_US_090_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_password_region_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_091_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_091_exception.png")
            self.log.info(f"test_TC_US_091_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_password_region_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_092_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_092_exception.png")
            self.log.info(f"test_TC_US_092_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_password_region_email_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_093_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_093_exception.png")
            self.log.info(f"test_TC_US_093_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_and_user_role_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_094_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_094_exception.png")
            self.log.info(f"test_TC_US_094_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_user_role_and_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_095_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_095_exception.png")
            self.log.info(f"test_TC_US_095_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_user_role_and_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_096_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_096_exception.png")
            self.log.info(f"test_TC_US_096_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_user_role_email_and_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_097_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_097_exception.png")
            self.log.info(f"test_TC_US_097_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_user_role_and_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_098_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_098_exception.png")
            self.log.info(f"test_TC_US_098_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_user_role_region_and_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_099_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_099_exception.png")
            self.log.info(f"test_TC_US_099_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_user_role_region_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_100_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_100_exception.png")
            self.log.info(f"test_TC_US_100_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

    def user_fills_username_first_name_last_name_user_role_region_email_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_101_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_101_exception.png")
            self.log.info(f"test_TC_US_101_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_user_role_and_password_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_102_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_102_exception.png")
            self.log.info(f"test_TC_US_102_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_user_role_password_and_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_103_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_103_exception.png")
            self.log.info(f"test_TC_US_103_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_fills_username_first_name_last_name_user_role_password_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_104_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_104_exception.png")
            self.log.info(f"test_TC_US_104_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_lastname_user_role_password_email_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_105_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_105_exception.png")
            self.log.info(f"test_TC_US_105_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_last_name_user_role_password_region_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_106_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_106_exception.png")
            self.log.info(f"test_TC_US_106_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_firstname_lastname_user_role_password_region_timezone_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_107_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_107_exception.png")
            self.log.info(f"test_TC_US_107_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_first_name_lastname_user_role_password_region_email_save_display_error_message(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            self.enter_user_name(Read_Users_Components().user_name_input_data())
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            if self.validate_error_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_108_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_108_exception.png")
            self.log.info(f"test_TC_US_108_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def user_fills_username_firstname_lastname_user_role_password_region_email_timezone_display_success_msg(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)
            if self.validate_successful_message():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_109_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_109_exception.png")
            self.log.info(f"test_TC_US_109_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_create_a_new_user_by_filling_only_mandatory_fields(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)
            self.enter_first_name(Read_Users_Components().first_name_input_data())
            self.enter_last_name(Read_Users_Components().last_name_input_data())
            self.select_user_role(Read_Users_Components().user_role_input_data())
            self.enter_password(Read_Users_Components().password_data_input())
            self.select_region(Read_Users_Components().region_data_input())
            self.enter_email(Read_Users_Components().email_input_data())
            self.select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)
            if self.check_if_user_is_created(user_name=username):
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_110_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_110_exception.png")
            self.log.info(f"test_TC_US_110_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_the_mandatory_details_filled_for_the_newly_created_user(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)
            if self.check_if_users_able_to_see_mandatory_details(username, first_name, last_name,
                                                                 user_role, region, email, time_zone):
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_111_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_111_exception.png")
            self.log.info(f"test_TC_US_111_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_create_a_new_users_by_filling_all_the_fields(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            company = Read_Users_Components().company_input_data()
            self.enter_company(company)

            title = Read_Users_Components().title_input_data()
            self.enter_title(title)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            department = Read_Users_Components().department_input_data()
            self.enter_department(department)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            alert_email = Read_Users_Components().alert_email_input_data()
            self.enter_alert_email(alert_email)

            alert_phone_no = Read_Users_Components().alert_phone_no_input_data()
            self.enter_alert_phone_no(alert_phone_no)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            address = Read_Users_Components().address_input_data()
            self.enter_address(address)

            address2 = Read_Users_Components().address2_input_data()
            self.enter_address2(address2)

            city = Read_Users_Components().city_input_data()
            self.enter_city(city)

            state = Read_Users_Components().state_input_data()
            self.enter_state(state)

            postal_code = Read_Users_Components().postal_code_input_data()
            self.enter_postal_code(postal_code)

            home_ph_no = Read_Users_Components().home_phone_no_input_data()
            self.enter_home_ph_no(home_ph_no)

            work_ph_no = Read_Users_Components().work_phone_no_input_data()
            self.enter_work_ph_no(work_ph_no)

            fax_ph_no = Read_Users_Components().fax_phone_no_input_data()
            self.enter_fax_ph_no(fax_ph_no)

            phone_type = Read_Users_Components().phone_type_input_data()
            self.enter_phone_type(phone_type)

            phone_provider = Read_Users_Components().phone_provider_input_data()
            self.select_phone_provider(phone_provider)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.check_if_user_is_created(user_name=username):
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_112_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_112_exception.png")
            self.log.info(f"test_TC_US_112_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_all_the_details_filled_for_the_newly_created_user(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            company = Read_Users_Components().company_input_data()
            self.enter_company(company)

            title = Read_Users_Components().title_input_data()
            self.enter_title(title)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            department = Read_Users_Components().department_input_data()
            self.enter_department(department)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            alert_email = Read_Users_Components().alert_email_input_data()
            self.enter_alert_email(alert_email)

            alert_phone_no = Read_Users_Components().alert_phone_no_input_data()
            self.enter_alert_phone_no(alert_phone_no)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            address = Read_Users_Components().address_input_data()
            self.enter_address(address)

            address2 = Read_Users_Components().address2_input_data()
            self.enter_address2(address2)

            city = Read_Users_Components().city_input_data()
            self.enter_city(city)

            state = Read_Users_Components().state_input_data()
            self.enter_state(state)

            postal_code = Read_Users_Components().postal_code_input_data()
            self.enter_postal_code(postal_code)

            home_ph_no = Read_Users_Components().home_phone_no_input_data()
            self.enter_home_ph_no(home_ph_no)

            work_ph_no = Read_Users_Components().work_phone_no_input_data()
            self.enter_work_ph_no(work_ph_no)

            fax_ph_no = Read_Users_Components().fax_phone_no_input_data()
            self.enter_fax_ph_no(fax_ph_no)

            phone_type = Read_Users_Components().phone_type_input_data()
            self.enter_phone_type(phone_type)

            phone_provider = Read_Users_Components().phone_provider_input_data()
            self.select_phone_provider(phone_provider)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.check_if_users_able_to_see_all_details(user_name=username):
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_113_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_113_exception.png")
            self.log.info(f"test_TC_US_113_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_if_user_creates_a_new_users_marked_as_enabled_it_should_reflect_as_enabled(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            self.select_disabled()
            self.select_enabled()

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)
            if self.check_if_user_marked_as_enabled():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_114_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_114_exception.png")
            self.log.info(f"test_TC_US_114_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_if_user_creates_a_new_users_marked_as_disabled_it_should_reflect_as_disabled(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            self.select_disabled()

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)
            if self.check_if_user_marked_as_disabled():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_115_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_115_exception.png")
            self.log.info(f"test_TC_US_115_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_the_alert_schedule_is_enabled_after_creating_a_new_user(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)
            if self.check_if_alert_schedule_is_enabled():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_116_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_116_exception.png")
            self.log.info(f"test_TC_US_116_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_open_the_alert_schedule_after_creating_a_new_user(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.verify_user_able_to_open_the_alert_schedule():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_117_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_117_exception.png")
            self.log.info(f"test_TC_US_117_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_the_notification_groups_is_enabled_after_creating_a_new_user(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.check_if_notification_groups_is_enabled():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_118_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_118_exception.png")
            self.log.info(f"test_TC_US_118_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_open_the_notification_groups_after_creating_a_new_user(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.verify_user_able_to_open_the_notification_groups():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_119_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_119_exception.png")
            self.log.info(f"test_TC_US_119_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def user_able_to_see_the_newly_created_users_details_username_firstname_lastname_email_under_users_panel(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if False in self.verify_user_details_under_users_panel():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_120_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_120_exception.png")
            self.log.info(f"test_TC_US_120_exception: {ex}")
            return False
        finally:
            self.close_single_panel()
            self.click_on_logout_button()

    def verify_user_able_to_see_if_the_enabled_is_displayed_for_users_marked_as_enabled_under_users_panel(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.check_users_marked_as_enabled_under_users_panel():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_121_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_121_exception.png")
            self.log.info(f"test_TC_US_121_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_if_the_disabled_is_displayed_for_users_marked_as_disabled_under_users_panel(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            time.sleep(web_driver.one_second)
            self.select_disabled()
            time.sleep(web_driver.one_second)
            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.check_users_marked_as_disabled_under_users_panel():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_122_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_122_exception.png")
            self.log.info(f"test_TC_US_122_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_users_able_to_see_the_notification_groups_icon_for_the_newly_created_user_under_users_panel(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if False in self.check_notification_groups_icon():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_123_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_123_exception.png")
            self.log.info(f"test_TC_US_123_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_for_newly_created_user_the_hover_text_is_visible_for_notification_groups_under_users_panel(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if False in self.check_hover_text_notification_groups_icon():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_124_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_124_exception.png")
            self.log.info(f"test_TC_US_124_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_open_the_notification_groups_for_the_newly_created_user_under_users_panel(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.check_if_notification_groups_can_be_opened():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_125_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_125_exception.png")
            self.log.info(f"test_TC_US_125_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_the_details_icon_for_the_newly_created_user_under_users_panel(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if False in self.check_details_icon():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_126_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_126_exception.png")
            self.log.info(f"test_TC_US_126_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_that_for_the_newly_created_user_the_hover_text_is_visible_for_details_icon_under_users_panel(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if False in self.check_hover_text_details_icon():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_127_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_127_exception.png")
            self.log.info(f"test_TC_US_127_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_open_the_details_for_the_newly_created_user_under_users_panel(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.check_if_details_can_be_opened():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_128_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_128_exception.png")
            self.log.info(f"test_TC_US_128_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_see_the_alert_schedule_icon_for_the_newly_created_user_under_users_panel(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if False in self.check_alert_schedule_icon():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_129_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_129_exception.png")
            self.log.info(f"test_TC_US_129_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_for_the_newly_created_user_the_hover_text_is_visible_for_alert_schedule_under_users_panel(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if False in self.check_hover_text_alert_schedule():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_130_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_130_exception.png")
            self.log.info(f"test_TC_US_130_exception: {ex}")
            return False
        finally:
            self.close_single_panel()
            self.click_on_logout_button()

    def verify_user_able_to_open_the_alert_schedule_for_the_newly_created_user_under_users_panel(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if False in self.check_if_alert_schedule_can_be_opened():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_131_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_131_exception.png")
            self.log.info(f"test_TC_US_131_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_edit_the_details_for_the_newly_created_user_details(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.check_if_users_able_to_edit_details():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_132_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_132_exception.png")
            self.log.info(f"test_TC_US_132_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_able_to_delete_the_newly_created_user(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if False in self.check_if_users_able_to_delete_a_user():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_133_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_133_exception.png")
            self.log.info(f"test_TC_US_133_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_should_not_be_able_to_create_user_which_already_exist(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if False in self.check_users_not_be_able_to_create_user_which_already_exist():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_134_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_134_exception.png")
            self.log.info(f"test_TC_US_134_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_should_not_be_able_to_create_user_if_password_and_confirm_password_does_not_match(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            confirm_passwrd = Read_Users_Components().confirm_password_data_input()
            self.enter_mis_match_password(password, confirm_passwrd)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if False in self.check_if_error_msg_displayed_for_password_mismatch():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_135_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_135_exception.png")
            self.log.info(f"test_TC_US_135_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_cancel_the_user_creation_after_filling_all_the_details(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)

            if self.check_if_users_able_to_cancel():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_136_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_136_exception.png")
            self.log.info(f"test_TC_US_136_exception: {ex}")
            return False
        finally:
            self.close_single_panel()
            self.click_on_logout_button()

    def verify_when_user_close_user_panel_it_should_display_a_warning_popup(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)
            self.d.find_element(By.XPATH, Read_Users_Components().user_close_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            ex_pop_up = self.d.find_element(By.XPATH, Read_Users_Components().close_pop_up_by_xpath()).text.strip()
            ac_pop_up = Read_Users_Components().close_panel_pop_validation_text()
            if ex_pop_up == ac_pop_up:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_137_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_137_exception.png")
            self.log.info(f"test_TC_US_137_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_users_sees_go_back_and_close_panel_and_discard_changes_in_warning_popup(self):
        try:
            result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)
            self.d.find_element(By.XPATH, Read_Users_Components().user_close_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            go_back = self.d.find_element(By.XPATH, Read_Users_Components().close_pop_up_go_back_btn_by_xpath())
            discard = self.d.find_element(By.XPATH, Read_Users_Components().close_panel_and_discard_changes_by_xpath())
            result.append(go_back.is_displayed())
            result.append(go_back.is_enabled())
            result.append(discard.is_displayed())
            result.append(discard.is_enabled())
            go_back.click()
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_138_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_138_exception.png")
            self.log.info(f"test_TC_US_138_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            self.click_on_logout_button()

    def verify_user_lands_on_the_same_panel_on_clicking_go_back(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            ex = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_title_by_xpath()).text
            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)
            self.d.find_element(By.XPATH, Read_Users_Components().user_close_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            go_back = self.d.find_element(By.XPATH, Read_Users_Components().close_pop_up_go_back_btn_by_xpath())
            go_back.click()
            ac = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_title_by_xpath()).text
            if ex == ac:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_139_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_139_exception.png")
            self.log.info(f"test_TC_US_139_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_on_clicking_close_panel_and_discard_changes_user_panel_should_be_closed(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)
            self.d.find_element(By.XPATH, Read_Users_Components().user_close_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            discard = self.d.find_element(By.XPATH, Read_Users_Components().close_panel_and_discard_changes_by_xpath())
            discard.click()
            panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_list_by_xpath())
            new_panel_count = len(panel_list)
            if new_panel_count == 1:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_140_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_140_exception.png")
            self.log.info(f"test_TC_US_140_exception: {ex}")
            return False
        finally:
            self.close_single_panel()
            self.click_on_logout_button()

    def verify_user_is_able_to_open_filter_drop_down_in_notification_group_panel(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.verify_user_able_to_open_the_filter_drop_down():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_141_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_141_exception.png")
            self.log.info(f"test_TC_US_141_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_the_user_is_able_to_open_action_drop_down_in_notification_group_panel(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.verify_user_able_to_open_the_action_drop_down():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_142_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_142_exception.png")
            self.log.info(f"test_TC_US_142_exception: {ex}")
            return False
        finally:
            self.close_single_panel()
            self.click_on_logout_button()

    def verify_user_able_to_assign_the_newly_created_user_to_a_notification_group(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if False in self.verify_user_able_to_assign_user_to_notification_group():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_143_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_143_exception.png")
            self.log.info(f"test_TC_US_143_exception: {ex}")
            return False
        finally:
            self.close_single_panel()
            self.click_on_logout_button()

    def verify_company_input_fields_should_not_accept_special_characters(self):
        try:
            result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            company = Read_Users_Components().company_input_data() + str("@$")
            self.enter_company(company)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)

            company_error = self.d.find_element(By.XPATH, Read_Users_Components().company_error_msg())
            result.append(company_error.is_displayed())
            ex_company_error_txt = Read_Users_Components().company_error_msg_validation_text()
            ac_company_error_txt = company_error.text
            result.append(ex_company_error_txt == ac_company_error_txt)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)
            result.append(self.validate_error_message())
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_144_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_144_exception.png")
            self.log.info(f"test_TC_US_144_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_should_not_be_able_to_create_a_user_if_password_value_is_username_firstname_or_lastname(self):
        try:
            result = []
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            self.enter_password(username)

            company = Read_Users_Components().company_input_data()
            self.enter_company(company)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)

            self.click_on_save_btn()

            # validate with username
            time.sleep(web_driver.one_second)
            req_not_match = self.d.find_element(By.XPATH, Read_Users_Components().password_requirement_un_fn_ln_msg())
            ex_req_not_match = req_not_match.text
            ac_req_not_match = Read_Users_Components().password_requirement_un_fn_ln_msg_validation_text()
            result.append(req_not_match.is_displayed())
            result.append(ex_req_not_match == ac_req_not_match)

            # validate with firstname
            new_password = self.d.find_element(By.XPATH, Read_Users_Components().new_password_by_xpath())
            confirm_password = self.d.find_element(By.XPATH, Read_Users_Components().confirm_password_by_xpath())
            new_password.clear()
            confirm_password.clear()
            time.sleep(web_driver.one_second)
            self.enter_password(first_name)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)
            ex_req_not_match = req_not_match.text
            ac_req_not_match = Read_Users_Components().password_requirement_un_fn_ln_msg_validation_text()
            result.append(req_not_match.is_displayed())
            result.append(ex_req_not_match == ac_req_not_match)

            # validate with lastname
            new_password = self.d.find_element(By.XPATH, Read_Users_Components().new_password_by_xpath())
            confirm_password = self.d.find_element(By.XPATH, Read_Users_Components().confirm_password_by_xpath())
            new_password.clear()
            confirm_password.clear()
            time.sleep(web_driver.one_second)
            self.enter_password(last_name)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)
            ex_req_not_match = req_not_match.text
            ac_req_not_match = Read_Users_Components().password_requirement_un_fn_ln_msg_validation_text()
            result.append(req_not_match.is_displayed())
            result.append(ex_req_not_match == ac_req_not_match)
            time.sleep(web_driver.one_second)

            cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
            cancel.click()
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_145_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_145_exception.png")
            self.log.info(f"test_TC_US_145_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_should_not_be_able_to_create_a_user_if_password_value_is_less_than_8_characters(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_7_character_data()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.verify_password_7_characters():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_146_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_146_exception.png")
            self.log.info(f"test_TC_US_146_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_should_not_be_able_to_create_a_user_if_password_value_is_greater_than_20_characters(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_21_character_data()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.verify_password_21_characters():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_147_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_147_exception.png")
            self.log.info(f"test_TC_US_147_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_should_not_be_able_to_create_a_user_if_password_value_is_only_alphabets(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_only_alphabet_data()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.verify_password_only_alphabets():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_148_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_148_exception.png")
            self.log.info(f"test_TC_US_148_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_should_not_be_able_to_create_a_user_if_password_value_is_only_numbers(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_only_number_data()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.verify_password_only_numeric():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_149_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_149_exception.png")
            self.log.info(f"test_TC_US_149_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_user_should_not_be_able_to_create_a_user_if_password_value_is_only_special_characters(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_only_special_symbol_data()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.verify_password_only_special_character():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_150_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_150_exception.png")
            self.log.info(f"test_TC_US_150_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def Verify_if_password_value_is_only_combination_of_alphabet_in_lower_case_and_number(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_only_alphabet_number_data()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.verify_password_combination_lower_alphabet_and_number():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_151_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_151_exception.png")
            self.log.info(f"test_TC_US_151_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_if_password_value_is_only_combination_of_alphabet_in_lower_case_and_special_characters(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_only_alphabet_special_symbol_data()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.verify_password_combination_lower_alphabet_and_special_character():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_152_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_152_exception.png")
            self.log.info(f"test_TC_US_152_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_if_password_value_is_only_combination_of_number_and_special_characters(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_only_number_special_symbol_data()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

            if self.verify_password_combination_number_and_special_character():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_153_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_153_exception.png")
            self.log.info(f"test_TC_US_153_exception: {ex}")
            return False
        finally:
            self.close_single_panel()
            self.click_on_logout_button()

    def verify_user_on_clicking_alert_schedule_alert_schedule_panel_pops_up_and_the_title_is_visible(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            if False in self.verify_alert_schedule_title():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_154_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_154_exception.png")
            self.log.info(f"test_TC_US_154_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_on_alert_schedule_user_is_able_to_see_the_sub_title_user_alert_schedule(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)

            if False in self.verify_alert_schedule_sub_title():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_155_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_155_exception.png")
            self.log.info(f"test_TC_US_155_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_on_alert_schedule_user_is_able_to_see_schedule_sub_title(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)

            if False in self.verify_schedule_sub_title_is_visible():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_156_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_156_exception.png")
            self.log.info(f"test_TC_US_156_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_on_alert_schedule_settings_text_is_visible(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)

            if False in self.verify_settings_text_is_visible():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_157_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_157_exception.png")
            self.log.info(f"test_TC_US_157_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_on_alert_schedule_settings_details_and_its_values_is_visible(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)

            if False in self.verify_settings_details_and_values_is_visible():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_158_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_158_exception.png")
            self.log.info(f"test_TC_US_158_exception: {ex}")
            return False
        finally:
            self.close_single_panel()
            self.click_on_logout_button()

    def verify_on_alert_schedule_under_schedule_day_and_time_range_is_visible(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)

            if False in self.verify_schedule_day_and_time_range_is_visible():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_159_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_159_exception.png")
            self.log.info(f"test_TC_US_159_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def verify_on_alert_schedule_action_drop_down_is_visible_and_clickable(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)

            if False in self.verify_alert_schedule_action_drop_down():
                self.d.save_screenshot(
                    f"{self.screenshots_path}test_TC_US_160_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}test_TC_US_160_exception.png")
            self.log.info(f"test_TC_US_160_exception: {ex}")
            return False
        finally:
            self.close_single_panel()
    
    def on_alert_schedule_click_on_action_dropdown_verify_option_inside_drop_down_is_visible(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)

            if False in self.verify_action_drop_down_options():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_161_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_161_exception.png")
            self.log.info(f"test_TC_US_161_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def on_alert_schedule_click_on_edit_user_alert_schedule_and_verify_the_panel_should_be_editable(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            self.click_on_alert_schedule_action_option_edit()
            if False in self.verify_panel_is_editable():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_162_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_162_exception.png")
            self.log.info(f"test_TC_US_162_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def on_alert_schedule_verify_save_and_cancel_button_is_visible_and_clickable(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            self.click_on_alert_schedule_action_option_edit()
            if False in self.verify_save_and_cancel():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_163_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_163.png")
            self.log.info(f"test_TC_US_163_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def on_alert_schedule_verify_the_username_is_correct(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            if self.verify_username_is_correct():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_164_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_164_exception.png")
            self.log.info(f"test_TC_US_164_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def on_alert_schedule_verify_the_time_zone_ID_is_correct(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            if self.verify_timezone_id_is_correct():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_165_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_165_exception.png")
            self.log.info(f"test_TC_US_165_exception: {ex}")
            return False
        finally:
            self.close_single_panel()
            self.click_on_logout_button()

    def verify_send_sms_send_mms_send_email_send_in_app_notifications_enable_alerts_Yes_No_button(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            self.click_on_alert_schedule_action_option_edit()
            time.sleep(web_driver.one_second)
            if False in self.verify_settings_yes_or_no_button():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_166_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_166_exception.png")
            self.log.info(f"test_TC_US_166_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def on_alert_schedule_under_schedule_verify_the_day_and_checkbox_are_visible_and_clickable(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            self.click_on_alert_schedule_action_option_edit()
            time.sleep(web_driver.one_second)
            if False in self.verify_day_checkbox():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_167_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_167_exception.png")
            self.log.info(f"test_TC_US_167_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def on_alert_schedule_under_schedule_verify_the_time_range_slider_is_visible(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            self.click_on_alert_schedule_action_option_edit()
            time.sleep(web_driver.one_second)
            if False in self.verify_time_range_slider():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_168_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_168_exception.png")
            self.log.info(f"test_TC_US_168_exception: {ex}")
            return False
        finally:
            self.close_single_panel()
            self.click_on_logout_button()

    def verify_on_marking_the_days_checkbox_the_time_range_slider_is_enabled(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            self.click_on_alert_schedule_action_option_edit()
            time.sleep(web_driver.one_second)
            if False in self.verify_on_marking_the_time_range_slider_is_enabled():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_169_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_169_exception.png")
            self.log.info(f"test_TC_US_169_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def un_mark_the_days_checkbox_and_verify_the_time_range_slider_is_disabled(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            self.click_on_alert_schedule_action_option_edit()
            time.sleep(web_driver.one_second)
            if False in self.verify_on_un_marking_the_time_range_slider_is_disabled():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_170_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_170_exception.png")
            self.log.info(f"test_TC_US_170_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def edit_the_settings_send_sms_toggle_it_either_yes_or_no_save_and_verify_the_changes_are_reflected(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            self.click_on_alert_schedule_action_option_edit()
            time.sleep(web_driver.one_second)
            if False in self.verify_send_sms_toggle_yes_or_no():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_171_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_171_exception.png")
            self.log.info(f"test_TC_US_171_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def edit_the_settings_send_mms_toggle_it_either_yes_or_no_save_and_verify_the_changes_are_reflected(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            self.click_on_alert_schedule_action_option_edit()
            time.sleep(web_driver.one_second)
            if False in self.verify_send_mms_toggle_yes_or_no():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_172_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_172_exception.png")
            self.log.info(f"test_TC_US_172_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def edit_the_settings_send_email_toggle_it_either_yes_or_no_save_and_verify_the_changes_are_reflected(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            self.click_on_alert_schedule_action_option_edit()
            time.sleep(web_driver.one_second)
            if False in self.verify_send_email_toggle_yes_or_no():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_173_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_173_exception.png")
            self.log.info(f"test_TC_US_173_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def edit_the_settings_send_in_app_notifications_toggle_yes_no_save_and_verify_the_changes_are_reflected(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            self.click_on_alert_schedule_action_option_edit()
            time.sleep(web_driver.one_second)
            if False in self.verify_send_in_app_notifications_toggle_yes_or_no():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_174_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_174_exception.png")
            self.log.info(f"test_TC_US_174_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def edit_the_settings_enable_alerts_toggle_it_either_yes_or_no_save_and_verify_the_changes_are_reflected(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            self.click_on_alert_schedule_action_option_edit()
            time.sleep(web_driver.one_second)
            if False in self.verify_enable_alerts_toggle_yes_or_no():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_175_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_175_exception.png")
            self.log.info(f"test_TC_US_175_exception: {ex}")
            return False
        finally:
            self.close_single_panel()

    def on_alert_schedule_panel_verify_close_panel_button_is_visible_and_clickable_hover_text_is_visible(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            if False in self.verify_close_panel_button_is_visible_and_clickable():
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_176_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_176_exception.png")
            self.log.info(f"test_TC_US_176_exception: {ex}")
            return False
        finally:
            self.close_single_panel()
    
    def on_alert_schedule_panel_click_on_close_panel_button_and_verify_alert_schedule_panel_is_closing(self):
        try:
            self.login()
            time.sleep(web_driver.one_second)
            self.click_user_on_cloud_menu()
            self.create_a_user_with_a_constant_username_else_continue(self.is_constant_user_created())
            self.click_on_alert_schedule_icon()
            time.sleep(web_driver.one_second)
            if self.verify_alert_schedule_panel_is_closing():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_177_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_177_exception.png")
            self.log.info(f"test_TC_US_177_exception: {ex}")
            return False
        finally:
            self.close_single_panel()
            self.click_on_logout_button()

    def click_on_logout_button(self):
        try:
            time.sleep(web_driver.one_second)
            logout_button = self.d.find_element(By.XPATH, Read_Users_Components().logout_btn_by_xpath())
            time.sleep(web_driver.one_second)
            logout_button.click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}click_on_logout_button_failed.png")
            self.log.info(f"click_on_logout_button_failed: {ex}")
            return False

    def click_user_on_cloud_menu(self):
        """
        This function clicks on users on the cloud menu
        """
        users = self.d.find_element(By.XPATH, Read_Users_Components().users_cloud_menu_by_xpath())
        users.click()

    def click_on_action_btn(self):
        """
        clicks on action button
        """
        action_btn = self.d.find_element(By.XPATH, Read_Users_Components().action_dropdown_by_xpath())
        action_btn.click()

    def click_on_action_refresh_option(self):
        """
        clicks on refresh
        """
        self.click_on_action_btn()
        time.sleep(web_driver.one_second)
        refresh = self.d.find_element(By.XPATH, Read_Users_Components().refresh_by_xpath())
        refresh.click()

    def click_on_action_create_user_option(self):
        """
        clicks on create user
        """
        self.click_on_action_btn()
        time.sleep(web_driver.one_second)
        create_user = self.d.find_element(By.XPATH, Read_Users_Components().create_user_by_xpath())
        create_user.click()

    def click_on_action_delete_option(self):
        """
        clicks on delete selected user
        """
        self.click_on_action_btn()
        time.sleep(web_driver.one_second)
        delete = self.d.find_element(By.XPATH, Read_Users_Components().delete_selected_user_by_xpath())
        delete.click()
        time.sleep(web_driver.one_second)
        self.d.find_element(By.XPATH, Read_Users_Components().delete_confirmation_yes_by_xpath()).click()

    def click_on_save_btn(self):
        """
        clicks on save button
        """
        save = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_save_button_by_xpath())
        save.click()

    def click_on_cancel_btn(self):
        """
        clicks on cancel button
        """
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()

    def select_enabled(self):
        """
        selects enabled checkbox
        """
        checkbox = self.d.find_element(By.XPATH, Read_Users_Components().enabled_by_xpath())
        checkbox.click()

    def select_disabled(self):
        """
        selects disabled checkbox
        """
        checkbox = self.d.find_element(By.XPATH, Read_Users_Components().disabled_by_xpath())
        checkbox.click()

    def enter_user_name(self, user_name):
        """
        fills username field
        :param user_name:
        """
        user_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().user_name_by_xpath())
        user_name_txt_bx.send_keys(user_name)

    def enter_first_name(self, first_name):
        """
        fills first name field
        :param first_name:
        """
        first_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().first_name_by_xpath())
        first_name_txt_bx.send_keys(first_name)

    def enter_last_name(self, last_name):
        """
        fills last name field
        :param last_name:
        """
        last_name_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().last_name_by_xpath())
        last_name_txt_bx.send_keys(last_name)

    def select_user_role(self, role_data_text):
        """
        handles user role drop down using visible text of the element
        :param role_data_text:
        :return:
        """
        user_role_ele = self.d.find_element(By.XPATH, Read_Users_Components().user_role_by_xpath())
        select_options_visible_text(user_role_ele, role_data_text)

    def enter_password(self, password):
        """
        fills password field
        :param password:
        :return:
        """
        new_password = self.d.find_element(By.XPATH, Read_Users_Components().new_password_by_xpath())
        confirm_password = self.d.find_element(By.XPATH, Read_Users_Components().confirm_password_by_xpath())
        new_password.send_keys(password)
        confirm_password.send_keys(password)

    def enter_mis_match_password(self, password, confirm_password):
        """
        fills password field
        :param password:
        :param confirm_password:
        :return:
        """
        new_password = self.d.find_element(By.XPATH, Read_Users_Components().new_password_by_xpath())
        conf_password = self.d.find_element(By.XPATH, Read_Users_Components().confirm_password_by_xpath())
        new_password.send_keys(password)
        conf_password.send_keys(confirm_password)

    def enter_company(self, company):
        company_ele = self.d.find_element(By.XPATH, Read_Users_Components().company_by_xpath())
        company_ele.send_keys(company)

    def enter_title(self, title):
        title_ele = self.d.find_element(By.XPATH, Read_Users_Components().title_by_xpath())
        title_ele.send_keys(title)

    def enter_department(self, department):
        department_ele = self.d.find_element(By.XPATH, Read_Users_Components().department_by_xpath())
        department_ele.send_keys(department)

    def validate_required_user_role_is_selected(self, required_option):
        """
        validate the user role provided is selected.
        :param required_option:
        """
        user_role_ele = self.d.find_element(By.XPATH, Read_Users_Components().user_role_by_xpath())
        select = Select(user_role_ele)
        if select.first_selected_option.text == required_option:
            return True
        else:
            return False

    def select_region(self, region_text):
        """
        This function is used to handle the region drop-down and select the required options
        :param region_text:
        :return:
        """
        region_ele = self.d.find_element(By.XPATH, Read_Users_Components().region_by_xpath())
        region_ele.click()
        time.sleep(web_driver.one_second)
        region_text_list = self.d.find_elements(By.XPATH, Read_Users_Components().region_list_by_xpath())
        expected_region_text = region_text
        try:
            for i in range(len(region_text_list) + 1):
                actual_zone_text = region_text_list.__getitem__(i).text
                self.log.info(actual_zone_text)
                self.log.info(expected_region_text)
                if expected_region_text.upper() in actual_zone_text.upper():
                    region_text_list.__getitem__(i).click()
                    break
            save = self.d.find_element(By.XPATH, Read_Users_Components().region_save_btn_by_xpath())
            save.click()
            # self.d.execute_script("arguments[0].click();", save)
        except Exception as ex:
            str(ex)

    def validate_region(self, region_text):
        """
        validate the selected region is correct
        :param region_text:
        :return:
        """
        region_output = self.d.find_element(By.XPATH, Read_Users_Components().region_selected_by_xpath())
        return region_output.text.lower() in str(region_text).lower()

    def select_time_zone(self, use_value):
        """
        selects time zone using the value of the element
        :param use_value:
        :return:
        """
        time_zone = self.d.find_element(By.XPATH, Read_Users_Components().time_zone_by_xpath())
        select_options_value(time_zone, use_value)

    def enter_email(self, email):
        """
        fills email field
        :param email:
        """
        email_txt_bx = self.d.find_element(By.XPATH, Read_Users_Components().email_by_xpath())
        email_txt_bx.send_keys(email)

    def enter_alert_email(self, alert_email):
        """
        fills email field
        :param alert_email:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_email_by_xpath())
        ele.send_keys(alert_email)

    def enter_alert_phone_no(self, alert_phone_no):
        """
        fills email field
        :param alert_phone_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_phone_number_by_xpath())
        ele.send_keys(alert_phone_no)

    def enter_address(self, address):
        """
        fills email field
        :param address:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().address_by_xpath())
        ele.send_keys(address)

    def enter_city(self, city):
        """
        fills email field
        :param city:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().city_by_xpath())
        ele.send_keys(city)

    def enter_state(self, state):
        """
        fills email field
        :param state:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().state_by_xpath())
        ele.send_keys(state)

    def enter_postal_code(self, postal_code):
        """
        fills email field
        :param postal_code:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().postal_code_by_xpath())
        ele.send_keys(postal_code)

    def enter_home_ph_no(self, home_ph_no):
        """
        fills email field
        :param home_ph_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().home_phone_number_by_xpath())
        ele.send_keys(home_ph_no)

    def enter_work_ph_no(self, work_ph_no):
        """
        fills email field
        :param work_ph_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().work_phone_number_by_xpath())
        ele.send_keys(work_ph_no)

    def enter_fax_ph_no(self, fax_ph_no):
        """
        fills email field
        :param fax_ph_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().fax_phone_number_by_xpath())
        ele.send_keys(fax_ph_no)

    def enter_phone_type(self, phone_type):
        """
        fills email field
        :param phone_type:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().phone_type_by_xpath())
        ele.send_keys(phone_type)

    def enter_address2(self, address2):
        """
        fills email field
        :param address2:
        """
        ele = self.d.find_element(By.XPATH, Read_Users_Components().address2_by_xpath())
        ele.send_keys(address2)

    def select_phone_provider(self, phone_provider):
        ph_prov_bx = self.d.find_element(By.XPATH, Read_Users_Components().phone_provider_drop_dwn_by_xpath())
        select = Select(ph_prov_bx)
        select.select_by_visible_text(phone_provider)

    def validate_required_time_zone_is_selected(self, required_option):
        """
        checks if the required time zone is selected
        :param required_option:
        """
        time_zone_ele = self.d.find_element(By.XPATH, Read_Users_Components().time_zone_by_xpath())
        select = Select(time_zone_ele)
        selected_option = select.first_selected_option
        selected_value = selected_option.get_attribute("value")
        if selected_value == required_option:
            return True
        else:
            return False

    def validate_error_message(self):
        """
        checks if the error message "PLEASE NOTE: Required Fields Are Incomplete" is displayed.
        """
        ex_result = [True, True]
        ac_result = []
        ele = self.d.find_element(By.XPATH, Read_Users_Components().error_message_by_xpath())
        self.log.info(f"actual: {ele.text}")
        msg_validation = ele.text
        self.log.info(f"msg validation: {msg_validation}")
        ac_result.append(msg_validation == Read_Users_Components().error_msg_validation_text())
        ac_result.append(ele.is_displayed())
        self.log.info(f"status: {ac_result}")
        if ex_result == ac_result:
            self.log.info(f"validation Success: ")
            return True
        else:
            self.log.info(f"validation Failed: ")
            return False

    def validate_successful_message(self):
        """
        checks if the error message "Success! A user has been created." is displayed.
        """
        ex_result = [True, True]
        ac_result = []
        ele = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        msg_validation = ele.text
        ac_result.append(msg_validation == Read_Users_Components().success_msg_validation_text())
        ac_result.append(ele.is_displayed())
        if ex_result == ac_result:
            return True
        else:
            return False

    def check_if_user_is_created(self, user_name):
        """
        checks if the error message "Success! A user has been created." is displayed.
        """
        ex_result = [True, True, True]
        ac_result = []
        ele = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        msg_validation = ele.text
        ac_result.append(msg_validation == Read_Users_Components().success_msg_validation_text())
        ac_result.append(ele.is_displayed())
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(user_name)
        time.sleep(web_driver.one_second)
        user = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_username_by_xpath())
        ac_result.append(user_name == user.text)

        if ex_result == ac_result:
            return True
        else:
            return False

    def check_if_users_able_to_see_mandatory_details(self, ex_user_name, ex_first_name, ex_last_name, ex_user_role,
                                                     ex_region, ex_email, ex_time_zone):
        """
        checks if user details shows mandatory details that has been filled during the user creation process.
        """
        ex_result = [True, True, True, True, True, True, True]
        ac_result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        firstname = self.d.find_element(By.XPATH, Read_Users_Components().user_details_first_name_by_xpath()).text
        lastname = self.d.find_element(By.XPATH, Read_Users_Components().user_details_last_name_by_xpath()).text
        user_role = self.d.find_element(By.XPATH, Read_Users_Components().user_details_user_role_by_xpath()).text
        region = self.d.find_element(By.XPATH, Read_Users_Components().user_details_region_by_xpath()).text
        email = self.d.find_element(By.XPATH, Read_Users_Components().user_details_email_by_xpath()).text
        time_zone = self.d.find_element(By.XPATH, Read_Users_Components().user_details_timezone_by_xpath()).text
        ac_result.append(True if ex_user_name == username else False)
        ac_result.append(True if ex_first_name == firstname else False)
        ac_result.append(True if ex_last_name == lastname else False)
        ac_result.append(True if ex_user_role == user_role.lower() else False)
        ac_result.append(True if region in ex_region else False)
        ac_result.append(True if ex_email == email else False)
        ac_result.append(True if ex_time_zone == time_zone else False)

        if ex_result == ac_result:
            return True
        else:
            return False

    def check_if_users_able_to_see_all_details(self, user_name):
        """
        checks if user details shows all details that has been filled during the user creation process.
        """
        ex_user_name = user_name
        ex_first_name = Read_Users_Components().first_name_input_data().strip()

        ex_last_name = Read_Users_Components().last_name_input_data().strip()

        ex_user_role = Read_Users_Components().user_role_input_data().strip()

        ex_company = Read_Users_Components().company_input_data().strip()

        ex_title = Read_Users_Components().title_input_data().strip()

        ex_region = Read_Users_Components().region_data_input()

        ex_department = Read_Users_Components().department_input_data().strip()

        ex_email = Read_Users_Components().email_input_data().strip()

        ex_alert_email = Read_Users_Components().alert_email_input_data().strip()

        ex_alert_phone_no = Read_Users_Components().alert_phone_no_input_data().strip()

        ex_time_zone = Read_Users_Components().time_zone_input_data().strip()

        ex_address = Read_Users_Components().address_input_data().strip()

        ex_address2 = Read_Users_Components().address2_input_data().strip()

        ex_city = Read_Users_Components().city_input_data().strip()

        ex_state = Read_Users_Components().state_input_data().strip()

        ex_postal_code = Read_Users_Components().postal_code_input_data().strip()

        ex_home_ph_no = Read_Users_Components().home_phone_no_input_data().strip()

        ex_work_ph_no = Read_Users_Components().work_phone_no_input_data().strip()

        ex_fax_ph_no = Read_Users_Components().fax_phone_no_input_data().strip()

        ac_user_name = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text

        ac_first_name = self.d.find_element(By.XPATH, Read_Users_Components().user_details_first_name_by_xpath()).text

        ac_last_name = self.d.find_element(By.XPATH, Read_Users_Components().user_details_last_name_by_xpath()).text

        ac_user_role = self.d.find_element(By.XPATH, Read_Users_Components().user_details_user_role_by_xpath()).text

        ac_company = self.d.find_element(By.XPATH, Read_Users_Components().user_details_company_by_xpath()).text

        ac_title = self.d.find_element(By.XPATH, Read_Users_Components().user_details_title_by_xpath()).text

        ac_region = self.d.find_element(By.XPATH, Read_Users_Components().user_details_region_by_xpath()).text

        ac_department = self.d.find_element(By.XPATH, Read_Users_Components().user_details_department_by_xpath()).text

        ac_email = self.d.find_element(By.XPATH, Read_Users_Components().user_details_email_by_xpath()).text

        ac_alert_email = self.d.find_element(By.XPATH, Read_Users_Components().user_details_alert_email_by_xpath()).text

        ac_alert_phone_no = self.d.find_element(By.XPATH,
                                                Read_Users_Components().user_details_alert_ph_no_by_xpath()).text

        ac_time_zone = self.d.find_element(By.XPATH, Read_Users_Components().user_details_timezone_by_xpath()).text

        ac_address = self.d.find_element(By.XPATH, Read_Users_Components().user_details_address_by_xpath()).text

        ac_address2 = self.d.find_element(By.XPATH, Read_Users_Components().user_details_address2_by_xpath()).text

        ac_city = self.d.find_element(By.XPATH, Read_Users_Components().user_details_city_by_xpath()).text

        ac_state = self.d.find_element(By.XPATH, Read_Users_Components().user_details_state_by_xpath()).text

        ac_postal_code = self.d.find_element(By.XPATH, Read_Users_Components().user_details_postal_code_by_xpath()).text

        ac_home_ph_no = self.d.find_element(By.XPATH, Read_Users_Components().user_details_home_ph_no_by_xpath()).text

        ac_work_ph_no = self.d.find_element(By.XPATH, Read_Users_Components().user_details_work_ph_no_by_xpath()).text

        ac_fax_ph_no = self.d.find_element(By.XPATH, Read_Users_Components().user_details_fax_ph_no_by_xpath()).text

        ac_result = [True if ex_user_name == ac_user_name.strip() else False,
                     True if ex_first_name == ac_first_name.strip() else False,
                     True if ex_last_name == ac_last_name.strip() else False,
                     True if ex_user_role == ac_user_role.strip().lower() else False,
                     True if ex_company == ac_company.strip() else False,
                     True if ex_title == ac_title.strip() else False,
                     True if ac_region in ex_region else False,
                     True if ex_department == ac_department.strip() else False,
                     True if ex_email == ac_email.strip() else False,
                     True if ex_alert_email == ac_alert_email.strip() else False,
                     True if ex_alert_phone_no == ac_alert_phone_no.strip() else False,
                     True if ex_time_zone == ac_time_zone.strip() else False,
                     True if ex_address == ac_address.strip() else False,
                     True if ex_address2 == ac_address2.strip() else False,
                     True if ex_city == ac_city.strip() else False,
                     True if ex_state == ac_state.strip() else False,
                     True if ex_postal_code == ac_postal_code.strip() else False,
                     True if ex_home_ph_no == ac_home_ph_no.strip() else False,
                     True if ex_work_ph_no == ac_work_ph_no.strip() else False,
                     True if ex_fax_ph_no == ac_fax_ph_no.strip() else False]

        if False in ac_result:
            return False
        else:
            return True

    def check_if_user_marked_as_enabled(self):
        """
        checks if user marked as enabled in user panel(User details)
        """
        enabled = self.d.find_element(By.XPATH, Read_Users_Components().user_details_enabled_by_xpath())
        return enabled.is_displayed()

    def check_if_user_marked_as_disabled(self):
        """
        checks if user marked as disabled in user panel(User details)
        """

        disabled = self.d.find_element(By.XPATH, Read_Users_Components().users_details_disabled_by_xpath())
        return disabled.is_displayed()

    def check_if_alert_schedule_is_enabled(self):
        """
        checks if alert schedule is enabled when a new user is created.
        """
        alert_schedule_btn = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_btn_by_xpath())
        return alert_schedule_btn.is_enabled()

    def verify_user_able_to_open_the_alert_schedule(self):
        """
        checks if alert schedule panel pops up.
        """
        exp = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        alert_schedule_btn = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_btn_by_xpath())
        alert_schedule_btn.click()
        alert_panel_text = self.d.find_element(By.XPATH, Read_Users_Components().alert_panel_title_by_xpath()).text
        act = alert_panel_text.replace("(", "").replace(")", "")
        return exp == act

    def check_if_notification_groups_is_enabled(self):
        """
        checks if notification groups is enabled when a new user is created.
        """
        notification_groups_btn = self.d.find_element(By.XPATH,
                                                      Read_Users_Components().notification_groups_btn_by_xpath())
        return notification_groups_btn.is_enabled()

    def verify_user_able_to_open_the_notification_groups(self):
        """
        checks if notification groups panel pops up.
        """
        exp = Read_Users_Components().notification_group_title_validation_text()
        notification_groups_btn = self.d.find_element(By.XPATH,
                                                      Read_Users_Components().notification_groups_btn_by_xpath())
        notification_groups_btn.click()
        act = self.d.find_element(By.XPATH, Read_Users_Components().notification_group_title_by_xpath()).text
        return exp == act

    def verify_user_details_under_users_panel(self):
        """
        check user details under users_panel
        1. username
        2. first name
        3. last name
        4. email
        """
        result = []
        ex_username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        first_name = self.d.find_element(By.XPATH, Read_Users_Components().user_details_first_name_by_xpath()).text
        last_name = self.d.find_element(By.XPATH, Read_Users_Components().user_details_last_name_by_xpath()).text
        ex_first_last_name = first_name + " " + last_name
        ex_email = self.d.find_element(By.XPATH, Read_Users_Components().user_details_email_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(ex_username)
        time.sleep(web_driver.one_second)
        ac_username = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_username_by_xpath()).text
        ac_first_last_name = self.d \
            .find_element(By.XPATH, Read_Users_Components().users_list_board_first_and_last_name_by_xpath()).text
        ac_email = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_email_by_xpath()).text
        result.append(ex_username == ac_username)
        result.append(ex_first_last_name == ac_first_last_name)
        result.append(ex_email == ac_email)
        return result

    def check_users_marked_as_enabled_under_users_panel(self):
        """
        checks if user marked as enabled in Users panel.
        """
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        enabled_list_board = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_enabled_by_xpath())
        return enabled_list_board.is_displayed()

    def check_users_marked_as_disabled_under_users_panel(self):
        """
        checks if user marked as disabled in Users panel.
        """
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        disabled_list_board = self.d.find_element(By.XPATH,
                                                  Read_Users_Components().users_list_board_disabled_by_xpath())
        return disabled_list_board.is_displayed()

    def check_notification_groups_icon(self):
        """
        check notification groups icon is displayed and enabled
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        notification_groups_icon = self.d.find_element(By.XPATH,
                                                       Read_Users_Components().notification_group_icon_by_xpath())
        result.append(notification_groups_icon.is_displayed())
        result.append(notification_groups_icon.is_enabled())
        return result

    def check_hover_text_notification_groups_icon(self):
        """
        checks hover text for notification groups icon is visible
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_group_icon_by_xpath())
        move_to_element(ele)
        time.sleep(web_driver.one_second)
        exp = Read_Users_Components().notification_group_icon_hover_validation_text()
        hover_ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_group_icon_hover_by_xpath())
        result.append(hover_ele.is_displayed())
        act = hover_ele.text.split(":")[0]
        result.append(exp == act)
        return result

    def check_if_notification_groups_can_be_opened(self):
        """
        checks notification groups icon can be opened
        """
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_group_icon_by_xpath())
        ele.click()
        time.sleep(web_driver.one_second)
        title = self.d.find_element(By.XPATH, Read_Users_Components().notification_group_title_by_xpath()).text
        return Read_Users_Components().notification_group_title_validation_text() == title

    def check_details_icon(self):
        """
        check details icon is displayed and enabled
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        details_icon = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_by_xpath())
        result.append(details_icon.is_displayed())
        result.append(details_icon.is_enabled())
        return result

    def check_hover_text_details_icon(self):
        """
        checks hover text for details icon is visible
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        details_icon = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_by_xpath())
        move_to_element(details_icon)
        time.sleep(web_driver.one_second)
        exp = Read_Users_Components().details_icon_hover_validation_text()
        hover_ele = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_hover_by_xpath())
        result.append(hover_ele.is_displayed())
        act = hover_ele.text
        result.append(exp == act)
        return result

    def check_if_details_can_be_opened(self):
        """
        checks details icon can be opened and user panel should pop up
        """
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        ele = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_by_xpath())
        ele.click()
        time.sleep(web_driver.one_second)
        title = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_title_by_xpath()).text
        return Read_Users_Components().user_panel_title_validation_text() == title

    def check_alert_schedule_icon(self):
        """
        check alert schedule icon is displayed and enabled
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        details_icon = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_icon_by_xpath())
        result.append(details_icon.is_displayed())
        result.append(details_icon.is_enabled())
        return result

    def check_hover_text_alert_schedule(self):
        """
        checks hover text for alert schedule icon is visible
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        alert_icon = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_icon_by_xpath())
        move_to_element(alert_icon)
        time.sleep(web_driver.one_second)
        exp = Read_Users_Components().alert_schedule_icon_hover_validation_text()
        hover_ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_icon_hover_by_xpath())
        result.append(hover_ele.is_displayed())
        act = hover_ele.text
        result.append(exp == act)
        return result

    def check_if_alert_schedule_can_be_opened(self):
        """
        checks Alert Schedule icon can be opened and alert panel should pop up.
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_icon_by_xpath())
        ele.click()
        time.sleep(web_driver.one_second)
        exp_title = username
        title = self.d.find_element(By.XPATH, Read_Users_Components().alert_panel_title_by_xpath()).text
        act_title = title.replace("(", "").replace(")", "")
        exp_sub_title = Read_Users_Components().alert_panel_sub_title_validation_text()
        act_sub_title = self.d.find_element(By.XPATH,
                                            Read_Users_Components().alert_panel_sub_title_by_xpath()).text.strip()
        result.append(exp_title == act_title)
        result.append(exp_sub_title == act_sub_title)
        return result

    def check_if_users_able_to_edit_details(self):
        """
        check if users able to edit details.
        """
        time.sleep(web_driver.one_second)
        self.d.find_element(By.XPATH, Read_Users_Components().user_details_action_btn()).click()
        self.d.find_element(By.XPATH, Read_Users_Components().user_details_action_edit_user()).click()
        time.sleep(web_driver.one_second)
        email = self.d.find_element(By.XPATH, Read_Users_Components().email_by_xpath())
        email.clear()
        time.sleep(web_driver.one_second)
        exp_email = Read_Users_Components().update_email_input_data()
        email.send_keys(exp_email)
        self.click_on_save_btn()
        time.sleep(web_driver.one_second)
        act_email = self.d.find_element(By.XPATH, Read_Users_Components().user_details_email_by_xpath()).text
        return exp_email == act_email

    def check_if_users_able_to_delete_a_user(self):
        """
        check if users able to delete a user
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        check_box = self.d.find_element(By.XPATH, Read_Users_Components().users_check_box_by_xpath())
        check_box.click()
        time.sleep(web_driver.one_second)
        self.click_on_action_delete_option()
        time.sleep(web_driver.one_second)
        search_box.send_keys(username)
        time.sleep(web_driver.one_second)
        msg = self.d.find_element(By.XPATH, Read_Users_Components().filter_message_by_xpath())
        result.append(msg.is_displayed())
        result.append(msg.text == Read_Users_Components().filter_msg_validation_text())
        return result

    def check_users_not_be_able_to_create_user_which_already_exist(self):
        """
        check if users not be able to create user which already exist
        """
        result = []
        username = self.d.find_element(By.XPATH, Read_Users_Components().user_details_username_by_xpath()).text

        self.click_on_action_create_user_option()
        time.sleep(web_driver.one_second)

        self.enter_user_name(username)

        first_name = Read_Users_Components().first_name_input_data()
        self.enter_first_name(first_name)

        last_name = Read_Users_Components().last_name_input_data()
        self.enter_last_name(last_name)

        user_role = Read_Users_Components().user_role_input_data()
        self.select_user_role(user_role)

        password = Read_Users_Components().password_data_input()
        self.enter_password(password)

        region = Read_Users_Components().region_data_input()
        self.select_region(region)

        email = Read_Users_Components().email_input_data()
        self.enter_email(email)

        time_zone = Read_Users_Components().time_zone_input_data()
        self.select_time_zone(time_zone)

        time.sleep(web_driver.one_second)
        self.click_on_save_btn()

        time.sleep(web_driver.one_second)
        error_msg = self.d.find_element(By.XPATH, Read_Users_Components().user_name_exists_by_xpath())
        result.append(error_msg.is_displayed())
        result.append(error_msg.text == Read_Users_Components().user_name_exists_validation_text())
        return result

    def check_if_error_msg_displayed_for_password_mismatch(self):
        """
        check if error msg displayed for password mismatch
        """
        result = []
        error_msg = self.d.find_element(By.XPATH, Read_Users_Components().password_mis_match_by_xpath())
        result.append(error_msg.is_displayed())
        result.append(error_msg.text == Read_Users_Components().password_mis_match_validation_text())
        return result

    def check_if_users_able_to_cancel(self):
        """
        check if users able to cancel
        """
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_list_by_xpath())
        new_panel_count = len(panel_list)
        return new_panel_count == 1

    def close_all_panel_one_by_one(self):
        try:
            time.sleep(web_driver.one_second)
            close_panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_one_by_one_list())

            for i in close_panel_list:
                i.click()
                time.sleep(web_driver.one_second)
            while self.d.find_element(By.XPATH, Read_Users_Components().user_close_panel_and_discard_Changes())\
                    .is_displayed():
                ele = self.d.find_element(By.XPATH, Read_Users_Components().user_close_panel_and_discard_Changes())
                javascript_executor_click(ele)
                if self.d.find_element(By.XPATH, Read_Users_Components().face_first_logo()).is_displayed():
                    break
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.click_on_logout_button()
            self.d.save_screenshot(f"{self.screenshots_path}close_all_panel_one_by_one_failed.png")
            self.log.info(f"close_all_panel_one_by_one_failed: {ex}")

    def close_single_panel(self):
        try:
            time.sleep(web_driver.one_second)
            close_panel_list = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_one_by_one_list())
            for i in close_panel_list:
                javascript_executor_click(i)
            time.sleep(web_driver.one_second)
            if self.d.find_element(By.XPATH, Read_Users_Components().close_panel_and_discard_changes_warning_by_xpath()).is_displayed():
                self.d.find_element(By.XPATH, Read_Users_Components().close_panel_and_discard_changes_warning_by_xpath()).click()
            else:
                pass
        except Exception as ex:
            self.click_on_logout_button()
            self.d.save_screenshot(f"{self.screenshots_path}close_all_panel_one_by_one_failed.png")
            self.log.info(f"close_all_panel_one_by_one_failed: {ex}")

    def verify_user_able_to_open_the_filter_drop_down(self):
        """
        checks if filter drop down is enabled
        """
        notification_groups_btn = self.d.find_element(By.XPATH,
                                                      Read_Users_Components().notification_groups_btn_by_xpath())
        notification_groups_btn.click()
        filter_ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_filter_drop_dwn())
        return filter_ele.is_enabled()

    def verify_user_able_to_open_the_action_drop_down(self):
        """
        checks if action drop down is enabled
        """
        notification_groups_btn = self.d.find_element(By.XPATH,
                                                      Read_Users_Components().notification_groups_btn_by_xpath())
        notification_groups_btn.click()

        action_ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_action_drop_dwn())
        return action_ele.is_enabled()

    def verify_user_able_to_assign_user_to_notification_group(self):
        """
        Add user to notification group
        """
        result = []
        time.sleep(web_driver.one_second)
        notification_groups_btn = self.d.find_element(By.XPATH,
                                                      Read_Users_Components().notification_groups_btn_by_xpath())
        notification_groups_btn.click()
        time.sleep(web_driver.one_second)
        action_ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_action_drop_dwn())
        action_ele.click()
        time.sleep(web_driver.one_second)
        create = self.d.find_element(By.XPATH, Read_Users_Components().option_create_notification_group())
        create.click()
        time.sleep(web_driver.one_second)

        name_value = Read_Users_Components().notification_group_name() + str(generate_random_number())
        name_ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_details_name_input())
        name_ele.send_keys(name_value)
        time.sleep(web_driver.one_second)
        save = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_details_save_btn())
        save.click()
        time.sleep(web_driver.one_second)
        close = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_details_close_panel())
        close.click()
        time.sleep(web_driver.one_second)
        filter_ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_filter_drop_dwn())
        filter_ele.click()
        time.sleep(web_driver.one_second)
        unlinked = self.d.find_element(By.XPATH, Read_Users_Components().option_unlinked_notification_groups())
        unlinked.click()
        time.sleep(web_driver.one_second)
        search = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_search_bar())
        search.send_keys(name_value)
        time.sleep(web_driver.one_second)
        check_box = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_select_all_checkbox())
        check_box.click()
        time.sleep(web_driver.one_second)
        action_ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_action_drop_dwn())
        action_ele.click()
        time.sleep(web_driver.one_second)
        add_user = self.d.find_element(By.XPATH, Read_Users_Components().option_add_to_user())
        add_user.click()
        time.sleep(web_driver.one_second)
        close_notification_groups = self.d\
            .find_element(By.XPATH, Read_Users_Components().notification_groups_close_panel())
        close_notification_groups.click()
        time.sleep(web_driver.one_second)
        notification_groups_btn = self.d.find_element(By.XPATH,
                                                      Read_Users_Components().notification_groups_btn_by_xpath())
        notification_groups_btn.click()
        ac_name = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_name_list()).text
        result.append(name_value == ac_name)

        time.sleep(web_driver.one_second)
        check_box = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_select_all_checkbox())
        check_box.click()
        time.sleep(web_driver.one_second)
        action_ele = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_action_drop_dwn())
        action_ele.click()
        time.sleep(web_driver.one_second)
        remove_user = self.d.find_element(By.XPATH, Read_Users_Components().option_remove_from_user())
        remove_user.click()
        time.sleep(web_driver.one_second)
        msg = self.d.find_element(By.XPATH, Read_Users_Components().notification_groups_no_linked_alerts())
        result.append(msg.is_displayed())
        time.sleep(web_driver.one_second)
        close_notification_groups = self.d.find_element(By.XPATH,
                                                        Read_Users_Components().notification_groups_close_panel())
        close_notification_groups.click()
        return result

    def verify_password_7_characters(self):
        ex_msg = Read_Users_Components().password_less_than_8_characters_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        return ex_msg == ac_msg

    def verify_password_21_characters(self):
        ex_msg = Read_Users_Components().password_greater_than_20_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        return ex_msg == ac_msg

    def verify_password_only_alphabets(self):
        ex_msg = Read_Users_Components().password_only_alphabet_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        return ex_msg == ac_msg

    def verify_password_only_numeric(self):
        ex_msg = Read_Users_Components().password_only_numeric_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        return ex_msg == ac_msg

    def verify_password_only_special_character(self):
        ex_msg = Read_Users_Components().password_only_special_symbol_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        return ex_msg == ac_msg

    def verify_password_combination_lower_alphabet_and_number(self):
        ex_msg = Read_Users_Components().password_only_alphanumeric_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        return ex_msg == ac_msg

    def verify_password_combination_lower_alphabet_and_special_character(self):
        ex_msg = Read_Users_Components().password_only_alphabet_sp_symbol_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        return ex_msg == ac_msg

    def verify_password_combination_number_and_special_character(self):
        ex_msg = Read_Users_Components().password_only_number_sp_symbol_validation_txt()
        msg = self.d.find_element(By.XPATH, Read_Users_Components().success_message_by_xpath())
        ac_msg = msg.text
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().user_panel_cancel_button_by_xpath())
        cancel.click()
        return ex_msg == ac_msg

    def verify_alert_schedule_title(self):
        """
        checks alert schedule panel title.
        """
        status = []
        exp = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_username_by_xpath()).text.strip()
        alert_panel_ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_panel_title_by_xpath())
        alert_panel_text = alert_panel_ele.text
        act = alert_panel_text.replace("(", "").replace(")", "")
        status.append(alert_panel_ele.is_displayed())
        status.append(exp == act)
        return status

    def is_constant_user_created(self):
        user_name = Read_Users_Components().constant_user_name()
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(user_name)
        time.sleep(web_driver.one_second)
        filter_msg = self.d.find_element(By.XPATH, Read_Users_Components().filter_message_by_xpath())
        if filter_msg.is_displayed():
            return False
        user = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_username_by_xpath())
        return user_name == user.text

    def click_on_alert_schedule_icon(self):
        alert_schedule = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_icon_by_xpath())
        alert_schedule.click()

    def create_a_user_with_a_constant_username_else_continue(self, is_user_created):
        if not is_user_created:
            self.click_on_action_create_user_option()
            time.sleep(web_driver.one_second)

            username = Read_Users_Components().constant_user_name()
            self.enter_user_name(username)

            first_name = Read_Users_Components().first_name_input_data()
            self.enter_first_name(first_name)

            last_name = Read_Users_Components().last_name_input_data()
            self.enter_last_name(last_name)

            user_role = Read_Users_Components().user_role_input_data()
            self.select_user_role(user_role)

            password = Read_Users_Components().password_data_input()
            self.enter_password(password)

            region = Read_Users_Components().region_data_input()
            self.select_region(region)

            email = Read_Users_Components().email_input_data()
            self.enter_email(email)

            time_zone = Read_Users_Components().time_zone_input_data()
            self.select_time_zone(time_zone)

            time.sleep(web_driver.one_second)
            self.click_on_save_btn()
            time.sleep(web_driver.one_second)

    def verify_alert_schedule_sub_title(self):
        """
        checks alert schedule sub title.
        """
        status = []
        exp = Read_Users_Components().alert_panel_sub_title_validation_text()
        sub_title_ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_panel_sub_title_by_xpath())
        act = sub_title_ele.text.strip()
        # self.log.info(exp, "==", act)
        status.append(sub_title_ele.is_displayed())
        status.append(exp == act)
        return status

    def verify_schedule_sub_title_is_visible(self):
        """
        checks alert schedule sub title 'Schedule'.
        """
        status = []
        exp = Read_Users_Components().alert_schedule_sub_title_schedule_validation_txt()
        sub_title_ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_panel_sub_title_schedule_by_xpath())
        act = sub_title_ele.text.strip()
        # self.log.info(exp, "==", act)
        status.append(sub_title_ele.is_displayed())
        status.append(exp == act)
        return status

    def verify_settings_text_is_visible(self):
        """
        checks 'Schedule' is visible.
        """
        status = []
        exp = Read_Users_Components().alert_schedule_settings_validation_txt()
        settings = self.d.find_element(By.XPATH, Read_Users_Components().alert_panel_settings_by_xpath())
        act = settings.text
        status.append(settings.is_displayed())
        status.append(exp == act)
        return status

    def verify_settings_details_and_values_is_visible(self):
        """
        checks Settings items (Username, Timezone, Timezone ID, Send SMS, Send MMS, Send Email,
        Send In-App Notifications, Enable Alerts) and its values is visible.
        """
        status = []

        # Details
        username_ele = self.d.find_element(By.XPATH, Read_Users_Components().settings_username_by_xpath())
        timezone_ele = self.d.find_element(By.XPATH, Read_Users_Components().settings_timezone_by_xpath())
        timezone_id_ele = self.d.find_element(By.XPATH, Read_Users_Components().settings_timezone_id_by_xpath())
        send_sms_ele = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_sms_by_xpath())
        send_mms_ele = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_mms_by_xpath())
        send_email_ele = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_email_by_xpath())
        send_in_app_ele = self.d.find_element(By.XPATH, Read_Users_Components()
                                              .settings_send_in_app_notifications_by_xpath())
        enable_alerts_ele = self.d.find_element(By.XPATH, Read_Users_Components().settings_enable_alerts_by_xpath())

        # Values
        username_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_username_value_by_xpath())
        timezone_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_timezone_value_by_xpath())
        timezone_id_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_timezone_id_value_by_xpath())
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_sms_value_by_xpath())
        send_mms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_mms_value_by_xpath())
        send_email_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_email_value_by_xpath())
        send_in_app_value = self.d\
            .find_element(By.XPATH, Read_Users_Components().settings_send_in_app_value_notifications_by_xpath())
        enable_alerts_value = self.d.find_element(By.XPATH, Read_Users_Components()
                                                  .settings_enable_alerts_value_by_xpath())

        # Details
        status.append(username_ele.is_displayed())
        status.append(timezone_ele.is_displayed())
        status.append(timezone_id_ele.is_displayed())
        status.append(send_sms_ele.is_displayed())
        status.append(send_mms_ele.is_displayed())
        status.append(send_email_ele.is_displayed())
        status.append(send_in_app_ele.is_displayed())
        status.append(enable_alerts_ele.is_displayed())
        status.append(username_ele.text == Read_Users_Components().settings_username_validation_txt())
        status.append(timezone_ele.text == Read_Users_Components().settings_timezone_validation_txt())
        status.append(timezone_id_ele.text == Read_Users_Components().settings_timezone_id_validation_txt())
        status.append(send_sms_ele.text == Read_Users_Components().settings_send_sms_validation_txt())
        status.append(send_mms_ele.text == Read_Users_Components().settings_send_mms_validation_txt())
        status.append(send_email_ele.text == Read_Users_Components().settings_send_email_validation_txt())
        status.\
            append(send_in_app_ele.text == Read_Users_Components().settings_send_in_app_notifications_validation_txt())
        status.append(enable_alerts_ele.text == Read_Users_Components().settings_enable_alerts_validation_txt())

        # Values
        status.append(username_value.is_displayed())
        status.append(timezone_value.is_displayed())
        status.append(timezone_id_value.is_displayed())
        status.append(send_sms_value.is_displayed())
        status.append(send_mms_value.is_displayed())
        status.append(send_email_value.is_displayed())
        status.append(send_in_app_value.is_displayed())
        status.append(enable_alerts_value.is_displayed())

        return status

    def verify_schedule_day_and_time_range_is_visible(self):
        """
        checks 'Schedule' day and time range.
        """
        status = []

        days_ele = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_day_by_xpath())
        for day in days_ele:
            status.append(day.is_displayed())
            self.log.info(day.is_displayed())
        time_range_ele = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_time_range_by_xpath())
        for ele in time_range_ele:
            status.append(ele.is_displayed())
            self.log.info(ele.is_displayed)
        return status

    def verify_alert_schedule_action_drop_down(self):
        """
        checks action drop down button
        """
        status = []
        action_ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_action_btn_by_xpath())
        status.append(action_ele.is_displayed())
        status.append(action_ele.is_enabled())
        return status

    def verify_action_drop_down_options(self):
        """
        checks action drop down options
        """
        status = []
        action_ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_action_btn_by_xpath())
        action_ele.click()
        time.sleep(web_driver.one_second)
        edit = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_action_option_edit_by_xpath())
        status.append(edit.is_displayed())
        status.append(edit.is_enabled())
        return status

    def click_on_alert_schedule_action_option_edit(self):
        action_ele = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_action_btn_by_xpath())
        action_ele.click()
        time.sleep(web_driver.one_second)
        edit = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_action_option_edit_by_xpath())
        edit.click()

    def verify_panel_is_editable(self):
        """
        checks alert schedule panel is editable
        """
        status = []
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_cancel_btn_by_xpath())
        status.append(save.is_displayed())
        status.append(cancel.is_displayed())
        return status

    def verify_save_and_cancel(self):
        """
        checks save and cancel
        """
        status = []
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        cancel = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_cancel_btn_by_xpath())
        status.append(save.is_displayed())
        status.append(cancel.is_displayed())
        status.append(save.is_enabled())
        status.append(cancel.is_enabled())
        return status

    def verify_username_is_correct(self):
        """
        checks username is correct in alert schedule
        """
        user = self.d.find_element(By.XPATH, Read_Users_Components().users_list_board_username_by_xpath())
        ex_user = user.text
        setting_user = self.d.find_element(By.XPATH, Read_Users_Components().settings_username_value_by_xpath())
        ac_user = setting_user.text
        return ex_user == ac_user

    def verify_timezone_id_is_correct(self):
        """
        checks timezone ID is correct in alert schedule
        """
        details_icon = self.d.find_element(By.XPATH, Read_Users_Components().details_icon_by_xpath())
        details_icon.click()
        time.sleep(web_driver.one_second)
        timezone_ele = self.d.find_element(By.XPATH, Read_Users_Components().user_details_timezone_by_xpath())
        ex_timezone_id = timezone_ele.text
        setting_timezone_id = self.d.find_element(By.XPATH, Read_Users_Components().settings_timezone_value_by_xpath())
        ac_timezone_id = setting_timezone_id.text
        return ex_timezone_id == ac_timezone_id

    def verify_settings_yes_or_no_button(self):
        """
        checks the Send SMS, Send MMS, Send Email, Send In-App Notifications,
         Enable Alerts - Yes/No button is visible and clickable.
        """
        status = []
        send_sms_yes = self.d.find_element(By.XPATH, Read_Users_Components().send_sms_yes_btn_by_xpath())
        send_sms_no = self.d.find_element(By.XPATH, Read_Users_Components().send_sms_no_btn_by_xpath())

        send_mms_yes = self.d.find_element(By.XPATH, Read_Users_Components().send_mms_yes_btn_by_xpath())
        send_mms_no = self.d.find_element(By.XPATH, Read_Users_Components().send_mms_no_btn_by_xpath())

        send_email_yes = self.d.find_element(By.XPATH, Read_Users_Components().send_email_yes_btn_by_xpath())
        send_email_no = self.d.find_element(By.XPATH, Read_Users_Components().send_email_no_btn_by_xpath())

        send_in_app_notification_yes = self.d\
            .find_element(By.XPATH, Read_Users_Components().send_in_app_notification_yes_btn_by_xpath())
        send_in_app_notification_no = self.d\
            .find_element(By.XPATH, Read_Users_Components().send_in_app_notification_no_btn_by_xpath())

        enable_alerts_yes = self.d.find_element(By.XPATH, Read_Users_Components().enable_alerts_yes_btn_by_xpath())
        enable_alerts_no = self.d.find_element(By.XPATH, Read_Users_Components().enable_alerts_no_btn_by_xpath())

        status.append(send_sms_yes.is_displayed())
        status.append(send_sms_yes.is_enabled())
        status.append(send_sms_no.is_displayed())
        status.append(send_sms_no.is_enabled())

        status.append(send_mms_yes.is_displayed())
        status.append(send_mms_yes.is_enabled())
        status.append(send_mms_no.is_displayed())
        status.append(send_mms_no.is_enabled())

        status.append(send_email_yes.is_displayed())
        status.append(send_email_yes.is_enabled())
        status.append(send_email_no.is_displayed())
        status.append(send_email_no.is_enabled())

        status.append(send_in_app_notification_yes.is_displayed())
        status.append(send_in_app_notification_yes.is_enabled())
        status.append(send_in_app_notification_no.is_displayed())
        status.append(send_in_app_notification_no.is_enabled())

        status.append(enable_alerts_yes.is_displayed())
        status.append(enable_alerts_yes.is_enabled())
        status.append(enable_alerts_no.is_displayed())
        status.append(enable_alerts_no.is_enabled())
        return status
        
    def verify_day_checkbox(self):
        """
        checks schedule day checkbox is visible and clickable
        """
        status = []
        checkbox = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_day_checkbox_by_xpath())
        for x in checkbox:
            status.append(x.is_displayed())
            status.append(x.is_enabled())
        return status

    def verify_time_range_slider(self):
        """
        checks schedule day checkbox is visible and clickable
        """
        status = []
        slider = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_time_range_slider_by_xpath())
        for x in slider:
            status.append(x.is_displayed())
        return status

    def verify_on_marking_the_time_range_slider_is_enabled(self):
        """
        checks time slider is enabled after selecting the days checkbox
        """
        status = []
        checkbox = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_day_checkbox_by_xpath())
        modified_path = Read_Users_Components().schedule_day_checkbox_by_xpath()+"/ins"
        checkbox_ins = self.d.find_elements(By.XPATH, modified_path)
        for x in range(len(checkbox)):
            if "checked" not in checkbox[x].get_attribute("class"):
                checkbox_ins[x].click()
                time.sleep(web_driver.one_second)

        slider = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_time_range_slider_by_xpath())
        for y in slider:
            status.append("disabled" not in y.get_attribute("class"))

        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        time_range = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_time_range_by_xpath())
        for z in time_range:
            status.append("Not Enabled" not in z.text)
        return status

    def verify_on_un_marking_the_time_range_slider_is_disabled(self):
        """
        checks time slider is disabled after un-selecting the days checkbox
        """
        status = []
        checkbox = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_day_checkbox_by_xpath())
        modified_path = Read_Users_Components().schedule_day_checkbox_by_xpath()+"/ins"
        checkbox_ins = self.d.find_elements(By.XPATH, modified_path)
        for x in range(len(checkbox)):
            if "checked" in checkbox[x].get_attribute("class"):
                checkbox_ins[x].click()
                time.sleep(web_driver.one_second)

        slider = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_time_range_slider_by_xpath())
        for y in slider:
            status.append("disabled" in y.get_attribute("class"))

        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        time_range = self.d.find_elements(By.XPATH, Read_Users_Components().schedule_time_range_by_xpath())
        for z in time_range:
            status.append("Not Enabled" in z.text)
        return status

    def verify_send_sms_toggle_yes_or_no(self):
        """
        checks if send sms yes or no button is functioning properly
        """
        status = []
        yes_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_sms_yes_btn_by_xpath())
        yes_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_sms_value_by_xpath())
        status.append(send_sms_value.text == "Yes")

        self.click_on_alert_schedule_action_option_edit()
        time.sleep(web_driver.one_second)
        no_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_sms_no_btn_by_xpath())
        no_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_sms_value_by_xpath())

        status.append(send_sms_value.text == "No")
        return status

    def verify_send_mms_toggle_yes_or_no(self):
        """
        checks if send mms yes or no button is functioning properly
        """
        status = []
        yes_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_mms_yes_btn_by_xpath())
        yes_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_mms_value_by_xpath())
        status.append(send_sms_value.text == "Yes")

        self.click_on_alert_schedule_action_option_edit()
        time.sleep(web_driver.one_second)
        no_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_mms_no_btn_by_xpath())
        no_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_mms_value_by_xpath())

        status.append(send_sms_value.text == "No")
        return status

    def verify_send_email_toggle_yes_or_no(self):
        """
        checks if send email yes or no button is functioning properly
        """
        status = []
        yes_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_email_yes_btn_by_xpath())
        yes_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_email_value_by_xpath())
        status.append(send_sms_value.text == "Yes")

        self.click_on_alert_schedule_action_option_edit()
        time.sleep(web_driver.one_second)
        no_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_email_no_btn_by_xpath())
        no_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_send_email_value_by_xpath())

        status.append(send_sms_value.text == "No")
        return status

    def verify_send_in_app_notifications_toggle_yes_or_no(self):
        """
        checks if enable alerts yes or no button is functioning properly
        """
        status = []
        yes_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_in_app_notification_yes_btn_by_xpath())
        yes_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d\
            .find_element(By.XPATH, Read_Users_Components().settings_send_in_app_value_notifications_by_xpath())
        status.append(send_sms_value.text == "Yes")

        self.click_on_alert_schedule_action_option_edit()
        time.sleep(web_driver.one_second)
        no_btn = self.d.find_element(By.XPATH, Read_Users_Components().send_in_app_notification_no_btn_by_xpath())
        no_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d\
            .find_element(By.XPATH, Read_Users_Components().settings_send_in_app_value_notifications_by_xpath())

        status.append(send_sms_value.text == "No")
        return status

    def verify_enable_alerts_toggle_yes_or_no(self):
        """
        checks if enable alerts yes or no button is functioning properly
        """
        status = []
        yes_btn = self.d.find_element(By.XPATH, Read_Users_Components().enable_alerts_yes_btn_by_xpath())
        yes_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_enable_alerts_value_by_xpath())
        status.append(send_sms_value.text == "Yes")

        self.click_on_alert_schedule_action_option_edit()
        time.sleep(web_driver.one_second)
        no_btn = self.d.find_element(By.XPATH, Read_Users_Components().enable_alerts_no_btn_by_xpath())
        no_btn.click()
        save = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)
        send_sms_value = self.d.find_element(By.XPATH, Read_Users_Components().settings_enable_alerts_value_by_xpath())

        status.append(send_sms_value.text == "No")
        return status

    def verify_close_panel_button_is_visible_and_clickable(self):
        status = []
        close_panel = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_close_panel_by_xpath())
        status.append(close_panel.is_displayed())
        status.append(close_panel.is_enabled())
        move_to_element(close_panel)
        time.sleep(web_driver.one_second)
        hover_txt = self.d.find_elements(By.XPATH, Read_Users_Components().close_panel_hover_text_by_xpath())
        for x in hover_txt:
            if x.is_displayed():
                status.append(x.text == Read_Users_Components().close_panel_hover_validation_txt())

        return status

    def verify_alert_schedule_panel_is_closing(self):
        all_panels = self.d.find_elements(By.XPATH, Read_Users_Components().all_open_panel_titles_by_xpath())
        for x in all_panels:
            self.log.info(x.text)
        close_panel = self.d.find_element(By.XPATH, Read_Users_Components().alert_schedule_close_panel_by_xpath())
        close_panel.click()
        time.sleep(web_driver.one_second)
        all_panels = self.d.find_elements(By.XPATH, Read_Users_Components().all_open_panel_titles_by_xpath())

        return len(all_panels) == 1 and all_panels[0].text == \
            Read_Users_Components().users_panel_title_validation_text()
