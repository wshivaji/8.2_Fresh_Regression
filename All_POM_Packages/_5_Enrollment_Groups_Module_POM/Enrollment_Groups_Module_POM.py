from All_Config_Packages._5_Enrollment_Groups_Config_Files.Enrollment_Groups_Read_INI import Read_Enrollment_Groups_Components
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from All_Config_Packages._0_login_logout_config_file.login_logout_read_ini import LoginLogout_Read_ini
# from pathlib import Path
from selenium.webdriver import ActionChains
from Base_Package.Login_Logout_Ops import login, logout
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
import time
import random


def generate_random_number():
    return random.randint(1, 1000)


class Enrollments_Groups_Module_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()

    def load_portal_login_page_if_not_loaded(self):
        try:
            if self.d.title != None and self.d.title == LoginLogout_Read_ini().get_portal_title():
                self.logger.info("title is not none or matching")
                pass
            else:
                self.logger.info(" no url ")
                self.d.get(LoginLogout_Read_ini().get_portal_url())
                self.d.maximize_window()
                time.sleep(web_driver.two_second)
            return self.d
        except Exception as ex:
            self.logger.error(ex)

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

    def verify_user_able_to_click_on_enrollment_groups_in_cloud_menu(self):
        try:
            self.logger.info("***************** test_TC_EG_001 *****************")
            # # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().enrollment_groups_button_by_xpath(), self.d)
            enrollment_groups_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enrollment_groups_button_by_xpath())
            time.sleep(web_driver.one_second)
            self.logger.info(f"enrollment_groups_btn is_displayed :{enrollment_groups_btn.is_displayed()}")
            if enrollment_groups_btn.is_displayed():
                self.logger.info(f"Status : {True}")
                return True
            else:
                self.logger.info(f"Status : {False}")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_001_failed.png")
                return False
        except Exception as ex:

            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_001_exception.png")
            self.logger.info(f"verify_user_able_to_click_on_enrollment_groups_in_cloud_menu_failed: {ex}")
            return False
        # finally:
        #     self.close_all_panel_one_by_one_no_popup()

    def verify_user_click_on_enrollment_groups_enrollment_groups_panel_is_displayed(self):
        try:
            self.logger.info("*********************** test_TC_EG_002 ********************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().enrollment_groups_button_by_xpath(),
                               self.d)
            enrollment_groups_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enrollment_groups_button_by_xpath())
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            validate_enrollment_panel = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enrollment_groups_button_by_xpath())
            self.logger.info(f"validate_enrollment_panel is_displayed :{validate_enrollment_panel.is_displayed()}")
            time.sleep(web_driver.one_second)
            if validate_enrollment_panel.is_displayed():
                self.logger.info(f"Status : {True}")
                return True
            else:
                self.logger.info(f"Status : {False}")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_002_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_002_exception.png")
            self.logger.info(f"Verify_user_click_on_Enrollment_Groups_Enrollment_Groups_panel_is_displayed_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_enrollment_groups_title_is_visible_on_enrollment_group_panel(self):
        try:
            self.logger.info("******************** test_TC_EG_003 ********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            time.sleep(web_driver.one_second)
            validate_enrollment_title_panel = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                                 .enrollment_groups_title_by_xpath(), self.d)
            self.logger.info(
                f"Expected enrollment title panel :{Read_Enrollment_Groups_Components().enrollment_group_title_validation_text()}")
            self.logger.info(f"Actual enrollment title panel : {validate_enrollment_title_panel.text}")
            status.append(validate_enrollment_title_panel.text.lower() == Read_Enrollment_Groups_Components().enrollment_group_title_validation_text().lower())
            status.append(validate_enrollment_title_panel.is_displayed())
            self.logger.info(f"validate_enrollment_title_panel is_displayed :{validate_enrollment_title_panel.is_displayed()}")
            self.logger.info(f"Status : {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_003_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_003_exception.png")
            self.logger.info(f"Verify_user_click_on_Enrollment_Groups_Enrollment_Groups_panel_is_displayed_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_action_button_is_visible_and_clickable(self):
        try:
            self.logger.info("*********************** test_TC_EG_004 ********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            status.append(action_btn.is_displayed())
            self.logger.info(f"Action dropdown is visible : {action_btn.is_displayed()}")
            status.append(action_btn.is_enabled())
            self.logger.info(f"Action dropdown is clickable : {action_btn.is_enabled()}")
            self.logger.info(f"Status is : {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_004_failed.png")
                return False
            else:
                return True
        except Exception as ex:

            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_004_exception.png")
            self.logger.info(f"verify_action_button_is_visible_and_clickable_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_action_button_has_dropdown_list(self):
        try:
            self.logger.info("****************** test_TC_EG_005 **********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().enrollment_groups_button_by_xpath(),
                               self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("Enrollment Groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().refresh_button_by_xpath(),
                               self.d)
            refresh = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().refresh_button_by_xpath())
            create_enrollment = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().create_enrollment_group_button_by_xpath())
            time.sleep(web_driver.one_second)
            status.append(refresh.is_displayed())
            self.logger.info(f"Refresh option is displayed : {refresh.is_displayed()}")
            status.append(create_enrollment.is_displayed())
            self.logger.info(f"create enrollment option is displayed : {create_enrollment.is_displayed()}")
            self.logger.info(f"Status : {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_005_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_005_exception.png")
            self.logger.info(f"verify_action_button_has_dropdown_list_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_action_dropdown_consist_create_enrollment_group_button_is_visible_and_clickable(self):
        try:
            self.logger.info("****************** test_TC_EG_006 **********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .create_enrollment_group_button_by_xpath(), self.d)

            status.append(create_enrollment.is_displayed())
            self.logger.info(f"create enrollment option is visible : {create_enrollment.is_displayed()}")
            status.append(create_enrollment.is_enabled())
            self.logger.info(f"create enrollment option is clickable : {create_enrollment.is_enabled()}")
            self.logger.info(f"Status is : {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_006_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_006_exception.png")
            self.logger.info(f"verify_action_dropdown_consist_create_enrollment_group_button_is_visible_and_clickable: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_action_dropdown_consist_refresh_button_is_visible_and_clickable(self):
        try:
            self.logger.info("***************** test_TC_EG_007 **********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            refresh_button = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().refresh_button_by_xpath(),
                               self.d)
            status.append(refresh_button.is_displayed())
            self.logger.info(f"refresh option is visible : {refresh_button.is_displayed()}")
            status.append(refresh_button.is_enabled())
            self.logger.info(f"refresh option is clickable : {refresh_button.is_enabled()}")
            self.logger.info(f"Status is : {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_007_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_007_Exception.png")
            self.logger.info(f"verify_action_dropdown_consist_refresh_button_is_visible_and_clickable: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_user_click_on_create_enrollment_group_enrollment_group_details_panel_should_be_visible(self):
        try:
            self.logger.info("******************** test_TC_EG_008 ******************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create enrollment groups option is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment_details_title = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                                 .enrollment_group_details_by_xpath(), self.d)
            t = Read_Enrollment_Groups_Components().enrollment_groups_details_validation_text().lower() == create_enrollment_details_title.text.lower()
            status.append(t)
            self.logger.info(f"Expected is : {Read_Enrollment_Groups_Components().enrollment_groups_details_validation_text().lower()}")
            self.logger.info(f"Actual is : {create_enrollment_details_title.text.lower()}")
            self.logger.info(f"Status is : {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_008_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_008_Exception.png")
            self.logger.info(f"verify_user_click_on_create_enrollment_group_enrollment_group_details_panel_should_be_visible: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_enrollment_group_cancel_button_is_visible_and_clickable(self):
        try:
            self.logger.info("******************* test_TC_EG_010 ******************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)

            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)

            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(),  self.d)
            action_btn.click()
            self.logger.info("Clicked on Action dropdown")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Clicked on create enrollment")
            time.sleep(web_driver.two_second)
            create_enrollment_details_title = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                                 .enrollment_group_details_by_xpath(), self.d)

            t = Read_Enrollment_Groups_Components().enrollment_groups_details_validation_text().lower() == create_enrollment_details_title.text.lower()
            status.append(t)

            cancel_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().cancel_button_by_xpath())
            status.append(cancel_button.is_displayed())
            self.logger.info(f"cancel_button is visible : {cancel_button.is_displayed()}")
            status.append(cancel_button.is_enabled())
            self.logger.info(f"cancel_button is clickable : {cancel_button.is_enabled()}")
            self.logger.info(f"Status : {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_010_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_010_Exception.png")
            self.logger.info(f"verify_enrollment_group_cancel_button_is_visible_and_clickable_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_enrollment_group_save_button_is_visible_and_clickable(self):
        try:
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().action_dropdown_button_by_xpath(),
                               self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("create_enrollment option is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment_details_title = self.explicit_wait(10, "XPATH",  Read_Enrollment_Groups_Components().enrollment_group_details_by_xpath(), self.d)

            t = Read_Enrollment_Groups_Components().enrollment_groups_details_validation_text().lower() == create_enrollment_details_title.text.lower()
            status.append(t)

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            status.append(save_button.is_displayed())
            self.logger.info(f"save_button is visible : {save_button.is_enabled()}")
            status.append(save_button.is_enabled())
            self.logger.info(f"save_button is clickable : {save_button.is_enabled()}")
            self.logger.info(f"Status : {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_011_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_011_Exception.png")
            self.logger.info(f"verify_enrollment_group_save_button_is_visible_and_clickable_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_user_click_on_create_enrollment_group_pop_up_panel_sub_title_is_enrollment_group_details(self):
        try:
            self.logger.info("************************* test_TC_EG_009 ********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().enrollment_groups_button_by_xpath(),
                               self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().action_dropdown_button_by_xpath(),
                               self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().create_enrollment_group_button_by_xpath(),
                               self.d)
            create_enrollment.click()
            self.logger.info("Create Enrollment Groups option is clicked")
            create_enrollment_details_sub_title = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                                     .enrollment_group_details_sub_title_by_xpath(), self.d)
            self.logger.info(f"Expected EG details sub title : {Read_Enrollment_Groups_Components().enrollment_group_details_sub_title_validation_text()}")
            self.logger.info(f"Actual EG details sub title : {create_enrollment_details_sub_title.text}")
            t = Read_Enrollment_Groups_Components().enrollment_group_details_sub_title_validation_text().lower() == create_enrollment_details_sub_title.text.lower()
            status.append(t)
            self.logger.info(f"Status is : {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_009_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_009_Exception.png")
            self.logger.info(f"verify_user_click_on_create_enrollment_group_pop_up_panel_sub_title_is_enrollment_group_details: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_name_text_box_field_is_visible_and_user_able_to_enter_name(self):
        try:
            self.logger.info("******************* test_TC_EG_012 *********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"Enrollment Groups Btn visible: {enrollment_groups_btn.is_displayed()}")
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.one_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"Action Btn visible: {action_btn.is_displayed()}")
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .create_enrollment_group_button_by_xpath(), self.d)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"Create Enrollment visible: {create_enrollment.is_displayed()}")
            create_enrollment.click()
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"Name field visible: {name_field.is_displayed()}")
            status.append(name_field.is_displayed())
            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            # status.append()

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"save btn visible: {save_button.is_displayed()}")
            status.append(save_button.is_displayed())
            time.sleep(web_driver.two_second)
            status.append(save_button.is_enabled())
            self.logger.info(f"save_button is clickable : {save_button.is_enabled()}")
            self.logger.info(f"status: {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_012_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_012_exception.png")
            self.logger.info(f"verify_name_text_box_field_is_visible_and_user_able_to_enter_name_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_description_text_box_field_is_visible_and_user_able_to_enter_description(self):
        try:
            self.logger.info("************************ test_TC_EG_013 *********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            action_btn = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().action_dropdown_button_by_xpath(),
                               self.d)
            action_btn.click()
            self.logger.info("Clicked on Action Dropdown")
            time.sleep(web_driver.two_second)

            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("clicked on create_enrollment option")
            time.sleep(web_driver.two_second)
            description_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .description_field_by_xpath(), self.d)

            description_field.is_displayed()
            try:
                description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
                web_driver.implicit_wait(self, web_driver.one_second, self.d)
            except Exception as ex:
                status.append(False)
                self.logger.info(f"{ex}")
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            status.append(save_button.is_displayed())
            status.append(save_button.is_enabled())
            self.logger.info(f"status {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_013_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_013_Exception.png")
            self.logger.info(f"verify_description_text_box_field_is_visible_and_user_able_to_enter_description: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_face_threshold_text_box_field_is_visible_and_user_able_to_enter_face_threshold(self):
        try:
            self.logger.info("******************** test_TC_EG_014 ***********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .enrollment_groups_button_by_xpath(), self.d)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("clicked on Action dropdown")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("clicked on create enrollment group option")
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            face_threshold_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .face_threshold_field_by_xpath(), self.d)
            face_threshold_field.clear()
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            status.append(face_threshold_field.is_displayed())
            self.logger.info(f"face_threshold_field is visible : {face_threshold_field.is_displayed()}")
            face_threshold_field.send_keys(Read_Enrollment_Groups_Components().face_threshold_field_data())
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            status.append(save_button.is_displayed())
            status.append(save_button.is_enabled())
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"status: {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_014_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_014_Exception.png")
            self.logger.info(f"verify_face_threshold_text_box_field_is_visible_and_user_able_to_enter_face_threshold: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_masked_face_threshold_text_box_field_is_visible_user_able_to_enter_masked_face_threshold(self):
        try:
            self.logger.info("******************* test_TC_EG_016 ****************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("clicked on Action dropdown")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("clicked on create enrollment groups option")
            time.sleep(web_driver.two_second)
            masked_face_threshold_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .masked_face_threshold_field_by_xpath(), self.d)
            masked_face_threshold_field.clear()

            status.append(masked_face_threshold_field.is_displayed())
            self.logger.info(f"masked_face_threshold_field is visible : {masked_face_threshold_field.is_displayed()}")
            masked_face_threshold_field.send_keys(Read_Enrollment_Groups_Components().masked_face_threshold_data())

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            status.append(save_button.is_displayed())
            save_button.is_enabled()
            self.logger.info(f"Status : {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_016_failed.png")
                return False
            else:
                return True

        except Exception as ex:

            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_016_exception.png")
            self.logger.info(f"verify_masked_face_threshold_text_box_field_is_visible_user_able_to_enter_masked_face_threshold: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            logout().logout_from_core(self.d)
            time.sleep(web_driver.one_second)

    def verify_serious_offender_dropdown_is_visible_user_able_to_select_from_the_dropdown(self):
        try:
            self.logger.info("**************** test_TC_EG_017 ****************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH",Read_Enrollment_Groups_Components()
                               .enrollment_groups_button_by_xpath(),self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create enrollment groups option is clicked")
            time.sleep(web_driver.one_second)
            dp_dwn_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .serious_offender_drop_down_by_xpath(), self.d)
            select = Select(dp_dwn_btn)
            options = select.options
            time.sleep(web_driver.one_second)
            for option in options:
                value = option.get_attribute("value")
                select.select_by_visible_text(value)
                time.sleep(web_driver.two_second)
                if not value == select.first_selected_option.text:
                    status.append(False)
            self.logger.info(f"Status is : {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_017_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_017_Exception.png")
            self.logger.info(f"verify_serious_offender_dropdown_is_visible_user_able_to_select_from_the_dropdown: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_suppress_duplicate_events_dropdown_is_visible_user_able_to_select_from_the_dropdown(self):
        try:
            self.logger.info("********************* test_TC_EG_018 ********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(),self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .create_enrollment_group_button_by_xpath(),self.d)
            create_enrollment.click()
            self.logger.info("Create enrollment groups option is clicked")
            time.sleep(web_driver.one_second)
            dp_dwn_btn = self.explicit_wait(10, "XPATH",Read_Enrollment_Groups_Components()
                                            .supress_duplicate_events_by_xpath(),self.d)
            # dp_dwn_btn.click()

            select = Select(dp_dwn_btn)
            options = select.options
            time.sleep(web_driver.one_second)
            print(options)
            for option in options:
                value = option.get_attribute("text")
                select.select_by_visible_text(value)
                time.sleep(web_driver.two_second)
                if not value == select.first_selected_option.text:
                    status.append(False)
            self.logger.info(f"Status is : {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_018_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_018_Exception.png")
            self.logger.info(f"verify_suppress_duplicate_events_dropdown_is_visible_user_able_to_select_from_the_dropdown: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_validation_error_message(self):
        try:
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enrollment_groups_button_by_xpath())
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().action_dropdown_button_by_xpath())
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().create_enrollment_group_button_by_xpath())
            create_enrollment.click()
            time.sleep(web_driver.one_second)
            create_enrollment_details_title = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enrollment_group_details_by_xpath())

            t = Read_Enrollment_Groups_Components().enrollment_groups_details_validation_text().lower() == create_enrollment_details_title.text.lower()
            status.append(t)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())

            save_button.click()
            time.sleep(web_driver.one_second)
            error_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().validation_error_message_by_xpath())
            status.append(error_message.is_displayed())
            print(status)
            if False in status:
                self.d.save_screenshot( f"{self.screenshots_path}\\test_verify_validation_error_message_EG_Module.png")
                return False
            else:
                return True

        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(verify_validation_error_message.png")
            self.logger.info(f"verify_validation_error_message: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_creating_enrollment_group_below_enrollments_notification_groups_events_should_be_disable_mode(self):
        try:
            self.logger.info("****************** test_TC_EG_020 ******************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH",Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(),self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH",Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create enrollment groups option is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment_details_title = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                                 .enrollment_group_details_by_xpath(), self.d)

            time.sleep(web_driver.one_second)
            enrollment_btn_text = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enrollment_button_by_xpath())
            status.append(not enrollment_btn_text.is_enabled())
            self.logger.info(f"enrollment btn is disabled : {not enrollment_btn_text.is_enabled()}")

            notification_btn_text = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().notification_groups_button_by_xpath())
            status.append(not notification_btn_text.is_enabled())
            self.logger.info(f"Notification groups button is disabled : {not notification_btn_text.is_enabled()}")

            events_btn_text = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().events_button_by_xpath())
            status.append(not events_btn_text.is_enabled())
            self.logger.info(f"Events btn is disabled : {not events_btn_text.is_enabled()}")
            time.sleep(web_driver.two_second)
            self.logger.info(f"Status is : {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_020_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_020_Exception.png")
            self.logger.info(f"verify_creating_enrollment_group_below_enrollments_notification_groups_events_should_be_disable_mode: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_user_click_on_delete_groups_from_system_option_unselecting_check_box_a_popup_msg_is_appeared(self):
        try:
            self.logger.info("****************** test_TC_EG_021 ******************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().enrollment_groups_button_by_xpath(),
                               self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("Enrollment Groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().action_dropdown_button_by_xpath(),
                               self.d)
            action_btn.click()
            self.logger.info("Action Dropdown is clicked")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().delete_button_by_xpath(),
                               self.d)
            delete_enrollment = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().delete_button_by_xpath())
            status.append(delete_enrollment.is_displayed())
            self.logger.info(f"Delete Enrollment option is visible : {delete_enrollment.is_displayed()}")
            status.append(delete_enrollment.is_enabled())
            self.logger.info(f"Delete Enrollment option is clickable : {delete_enrollment.is_enabled()}")
            self.logger.info(f"Status : {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_021_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_021_exception.png")
            self.logger.info(f"verify_user_click_on_delete_groups_from_system_option_unselecting_check_box_a_popup_msg_is_appeared: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_select_all_check_box_is_visible(self):
        try:
            self.logger.info("**************** test_TC_EG_022 ********************")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .enrollment_groups_title_by_xpath(), self.d)
            checkbox_text = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().checkbox_text_by_xpath())

            status.append(checkbox_text.is_displayed())
            self.logger.info(f"Checkbox is displayed : {checkbox_text.is_displayed()}")
            self.logger.info(f"status is : {status}")
            time.sleep(web_driver.two_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_022_failed.png")
                return False
            else:
                return True

        except Exception as ex:

            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_022_Exception.png")
            self.logger.info(f"verify_select_all_check_box_is_visible_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_user_clicks_on_select_all_check_box_all_the_below_check_boxes_should_get_selected(self):
        try:
            self.logger.info("****************** test_TC_EG_023 *****************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH",Read_Enrollment_Groups_Components()
                               .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            checkbox = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.two_second)
            check_list = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().check_box_list_by_xpath())
            for ele in check_list:
                if "checked" not in ele.get_attribute("class"):
                    status.append(False)
            self.logger.info(f"Status is : {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_023_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_023_exception.png")
            self.logger.info(f"verify_user_clicks_on_select_all_check_box_all_the_below_check_boxes_should_get_selected: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_user_clicks_on_select_all_uncheck_box_all_the_below_check_boxes_should_get_unselected(self):
        try:
            self.logger.info("****************** test_TC_EG_024 ********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            checkbox = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.two_second)
            checkbox = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().select_checkbox_by_xpath())
            self.d.execute_script("arguments[0].click();", checkbox)
            time.sleep(web_driver.two_second)
            check_list = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().check_box_list_by_xpath())
            for ele in check_list:
                if "checked" in ele.get_attribute("class"):
                    status.append(False)
            print(status)
            self.logger.info(f"Status is : {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_024_failed.png")
                return False
            else:
                return True
        except Exception as ex:

            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_024_exception.png")
            self.logger.info(f"verify_user_clicks_on_select_all_uncheck_box_all_the_below_check_boxes_should_get_unselected: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_user_fill_the_name_text_box_with_data_click_save_button_then_below_fields_should_be_activated(self):
        try:
            self.logger.info("******************** test_TC_EG_026 *********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"login done...")
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"enrollment group btn visible: {enrollment_groups_btn.is_displayed()}")
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment group btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"action btn visible: {action_btn.is_displayed()}")
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .create_enrollment_group_button_by_xpath(), self.d)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"create enrollment btn visible {create_enrollment.is_displayed()}")
            create_enrollment.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create enrollment option is clicked")
            name_field = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().name_field_by_xpath(),
                               self.d)
            self.logger.info(f"name field visible: {name_field.is_displayed()}")
            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"save btn visible: {save_button.is_displayed()}")
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Enrollment details is filled and save btn is clicked")
            enrollments_text = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().enrollment_button_by_xpath(),
                               self.d)
            self.logger.info(f"enrollment text visible: {enrollments_text.is_displayed()} ")
            status.append(enrollments_text.is_displayed())
            notification_groups_text = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().notification_groups_button_by_xpath(),
                               self.d)
            self.logger.info(f"notification groups text visible: {notification_groups_text.is_displayed()}")
            status.append(notification_groups_text.is_displayed())

            events_text = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().events_button_by_xpath())
            self.logger.info(f"event text visible: {events_text.is_displayed()}")
            status.append(events_text.is_displayed())
            self.logger.info(f"Status: {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_026_failed.png")
                return False
            else:
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_026_exception.png")
            self.logger.info(f"verify_user_fill_the_name_text_box_with_data_click_save_button_then_below_fields_should_be_activated: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()
            time.sleep(web_driver.one_second)

    def verify_success_validation_message(self):
        try:
            self.logger.info("********************* test_TC_EG_025 ******************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().enrollment_groups_button_by_xpath(),
                               self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.one_second)
            action_btn = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().action_dropdown_button_by_xpath(),
                               self.d)
            action_btn.click()
            self.logger.info("Action Dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().create_enrollment_group_button_by_xpath(),
                               self.d)
            create_enrollment.click()
            self.logger.info("create enrollment option is clicked")
            time.sleep(web_driver.one_second)
            name_field = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().name_field_by_xpath(),
                               self.d)
            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH",Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_msg_text = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                   .success_message_by_xpath())
            status.append(Read_Enrollment_Groups_Components().success_message_validation_text() == success_msg_text.text)
            self.logger.info(f"expected msg is : {Read_Enrollment_Groups_Components().success_message_validation_text()}")
            self.logger.info(f"actual msg is : {success_msg_text.text}")
            self.logger.info(f"status {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_025_failed.png")

                return False
            else:
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_025_exception.png")
            self.logger.info(f"verify_success_validation_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def verify_enrollments_button_is_activated_and_clickable(self):
        try:
            self.logger.info("******************** test_TC_EG_028 *******************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create enrollment groups option is clicked")
            time.sleep(web_driver.one_second)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Enrollment groups details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            enrollments_text = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                  .enrollment_button_by_xpath(), self.d)
            status.append(enrollments_text.is_displayed())
            self.logger.info(f"Enrollment btn is visible: {enrollments_text.is_displayed()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_028_failed.png")
                return False
            else:
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
        except Exception as ex:

            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_028_exception.png")
            self.logger.info(f"verify_enrollments_button_is_activated_and_clickable_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def verify_notification_groups_button_is_activated_and_clickable(self):
        try:
            self.logger.info("****************** test_TC_EG_029 *********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create enrollment groups option is clicked")
            time.sleep(web_driver.one_second)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Enrollment groups details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            notification_groups_text = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                          .notification_groups_button_by_xpath(), self.d)
            status.append(notification_groups_text.is_displayed())
            self.logger.info(f"notification groups btn is visible: {notification_groups_text.is_displayed()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_029_failed.png")
                return False
            else:
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
        except Exception as ex:

            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_029_Exception.png")
            self.logger.info(f"verify_notification_groups_button_is_activated_and_clickable_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def verify_events_button_is_activated_and_clickable(self):
        try:
            self.logger.info("****************** test_TC_EG_030 ******************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create enrollment groups option is clicked")
            time.sleep(web_driver.one_second)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Enrollment groups details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            events_text = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                             .events_button_by_xpath(), self.d)
            status.append(events_text.is_displayed())
            self.logger.info(f"Events btn is visible: {events_text.is_displayed()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_030_failed.png")
                return False
            else:
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_030_exception.png")
            self.logger.info(f"verify_events_button_is_activated_and_clickable_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def verify_user_click_on_enrollments_then_linked_enrollments_should_open(self):
        try:
            self.logger.info("***************** test_TC_EG_031 **************************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create enrollment groups option is clicked")
            time.sleep(web_driver.one_second)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Enrollment groups details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .enrollment_button_by_xpath(), self.d)
            enrollments_text = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                   .enrollment_button_by_xpath())
            # enrollments_text.click()
            self.d.execute_script("arguments[0].click();", enrollments_text)
            self.logger.info("Enrollment btn is clicked")
            time.sleep(web_driver.one_second)
            enrollment_in_text = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .enrollment_in_text_title_by_xpath(), self.d)

            status.append(enrollment_in_text.is_displayed())
            self.logger.info(f"Enrollment panel title is visible: {enrollment_in_text.is_displayed()}")
            self.logger.info(f"status: {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_031_failed.png")
                return False
            else:
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_031_Exception.png")
            self.logger.info(f"verify_user_click_on_enrollments_then_linked_enrollments_should_open_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def verify_user_click_on_notification_groups_then_linked_notification_groups_should_open(self):
        try:
            self.logger.info("******************** test_TC_EG_032 ***********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create enrollment groups option is clicked")
            time.sleep(web_driver.one_second)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Enrollment groups details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            notification_grp_text = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .notification_groups_button_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", notification_grp_text)
            self.logger.info("Notification groups btn is clicked")
            time.sleep(web_driver.two_second)
            notification_grp_text = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .notification_groups_title_by_xpath(), self.d)

            status.append(notification_grp_text.is_displayed())
            self.logger.info(f"Notification group title is visible: {notification_grp_text.is_displayed()}")
            self.logger.info(f"status: {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_032_failed.png")
                return False
            else:
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
        except Exception as ex:

            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_032_exception.png")
            self.logger.info(f"verify_user_click_on_notification_groups_then_linked_notification_groups_should_open_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def verify_user_click_on_events_then_linked_events_should_open(self):
        try:
            self.logger.info("*********************  test_TC_EG_033  ********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                                        enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                             action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create enrollment groups option is clicked")
            time.sleep(web_driver.one_second)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Enrollment groups details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .notification_groups_button_by_xpath(), self.d)
            events_text = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().events_button_by_xpath())

            self.d.execute_script("arguments[0].click();", events_text)
            self.logger.info("Events btn is clicked")
            time.sleep(web_driver.two_second)
            events_text = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                             .events_title_by_xpath(), self.d)
            print(events_text.text)
            status.append(events_text.is_displayed())
            self.logger.info(f"Events panel title is visible: {events_text.is_displayed()}")
            self.logger.info(f"status: {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_033_failed.png")
                return False
            else:
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_033_Exception.png")
            self.logger.info(f"verify_user_click_on_events_then_linked_events_should_open_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def verify_enrollment_group_details_action_dropdown_button_is_visible_and_clickable(self):
        try:
            self.logger.info("******************** test_TC_EG_034 *********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(),self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create enrollment groups option is clicked")
            time.sleep(web_driver.one_second)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Enrollment groups details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            action_btn_dropdown = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                     .enrollment_groups_details_action_dropdown_button_by_xpath(),
                                                     self.d)
            status.append(action_btn_dropdown.is_displayed())
            self.logger.info(f"EG details panel, Action is visible: {action_btn_dropdown.is_displayed()}")
            status.append(action_btn_dropdown.is_enabled())
            self.logger.info(f"EG details panel, Action is clickable: {action_btn_dropdown.is_enabled()}")
            self.logger.info(f"status: {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_034_failed.png")
                return False
            else:
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_034_Exception.png")
            self.logger.info(f"verify_enrollment_group_details_action_dropdown_button_is_visible_and_clickable_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def verify_enrollment_group_details_action_dropdown_has_edit_button_is_visible_and_clickable(self):
        try:
            self.logger.info("*********************** test_TC_EG_035 **********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH",Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                             action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)

            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(),
                               self.d)
            create_enrollment.click()
            self.logger.info("Create Enrollment Group option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().name_field_by_xpath(),
                               self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Enrollment group details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            action_btn_dropdown = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                     .enrollment_groups_details_action_dropdown_button_by_xpath(), self.d)
            action_btn_dropdown.click()
            self.logger.info("In Enrollment group details panel, edit dropdown is clicked")
            time.sleep(web_driver.two_second)
            edit_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().edit_button_by_xpath())
            status.append(edit_btn.is_displayed())
            self.logger.info(f"edit btn visible : {edit_btn.is_displayed()}")
            self.logger.info(f"status: {status}")
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_035_failed.png")
                return False
            else:
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_035_Exception.png")
            self.logger.info(f"verify_enrollment_group_details_action_dropdown_has_edit_button_is_visible_and_clickable_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def verify_user_unsaving_enrollment_group_details_panel_below_buttons_should_be_disable_mode(self):
        try:
            self.logger.info("***************** test_TC_EG_027 ***********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH",Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(),self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"enrollment group btn visible: {enrollment_groups_btn.is_displayed()}")
            self.logger.info(f"enrollment group btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)

            self.logger.info(f"action btn visible: {action_btn.is_displayed()}")
            action_btn.click()
            self.logger.info(f"Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .create_enrollment_group_button_by_xpath(), self.d)
            self.logger.info(f"create enrollment btn visible: {create_enrollment.is_displayed()}")
            create_enrollment.click()
            self.logger.info(f"Create Enrollment option is clicked")
            time.sleep(web_driver.one_second)
            # self.logger.info(f"enrollment group btn visible: {enrollment_groups_btn.is_displayed()}")

            create_enrollment_details_title = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                                 .enrollment_group_details_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            self.logger.info(f"create enrollment details visible: {create_enrollment_details_title.is_displayed()}")
            status.append(Read_Enrollment_Groups_Components().enrollment_groups_details_validation_text().lower() == create_enrollment_details_title.text.lower())
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"save btn visible: {save_button.is_displayed()}")
            # save_button.click()
            time.sleep(web_driver.one_second)
            enrollment_btn_text = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enrollment_button_by_xpath())
            status.append(not enrollment_btn_text.is_enabled())
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"enrollment_btn_text is not enabled: {not enrollment_btn_text.is_enabled()}")
            time.sleep(web_driver.one_second)

            notification_btn_text = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().notification_groups_button_by_xpath())
            status.append(not notification_btn_text.is_enabled())
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"notification_btn_text is not enabled: {not notification_btn_text.is_enabled()}")
            time.sleep(web_driver.one_second)

            events_btn_text = self.d.find_element(By.XPATH,
                                                  Read_Enrollment_Groups_Components().events_button_by_xpath())
            status.append(not events_btn_text.is_enabled())
            self.logger.info(f"events_btn_text is not enabled: {not events_btn_text.is_enabled()}")
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_027_failed.png")
                return False
            else:
                # self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
        except Exception as ex:

            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_027_Exception.png")
            self.logger.info(f"verify_user_unsaving_enrollment_group_details_panel_below_buttons_should_be_disable_mode_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def verify_user_can_delete_any_enrollment_groups(self):
        try:
            self.logger.info("*********************** test_TC_EG_036 *******************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                                        enrollment_groups_button_by_xpath(),
                               self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                             action_dropdown_button_by_xpath(),
                               self.d)
            action_btn.click()
            self.logger.info("Action Dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(),
                               self.d)
            create_enrollment.click()
            self.logger.info("Create Enrollment option is clicked")
            group_name = Read_Enrollment_Groups_Components().name_field_data() + str(generate_random_number())
            print(group_name)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().name_field_by_xpath(),
                               self.d)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(group_name)

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            self.delete_enrollment_group(group_name)
            time.sleep(web_driver.two_second)
            if self.check_if_the_group_is_deleted(group_name):
                self.logger.info(f"status: {True}")
                return True
            else:
                self.logger.info(f"status: {False}")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_036_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_036_Exception.png")
            self.logger.info(f"verify_user_can_delete_any_enrollment_groups_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def without_filling_any_data_it_should_displayed_error_message(self):
        try:
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            status.append(self.validate_error_msg())
            if False in status:
                # self.d.save_screenshot(f"{self.screenshots_path}(without_filling_any_data_it_should_displayed_error_message_failed.png")
                return False
            else:
                # self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return False

        except Exception as ex:
            # self.d.save_screenshot(f"{self.screenshots_path}(without_filling_any_data_it_should_displayed_error_message_failed.png")
            self.logger.info(f"without_filling_any_data_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_suppress_duplicate_events_data_it_should_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            suppress_duplicate = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(suppress_duplicate)

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                # self.d.save_screenshot(
                #     f"{self.screenshots_path}(filling_suppress_duplicate_events_data"
                #     f"_it_should_displayed_error_message_failed.png")
                return False

        except Exception as ex:

            # self.d.save_screenshot(
                # f"{self.screenshots_path}(filling_suppress_duplicate_events_data"
                # f"_it_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_suppress_duplicate_events_data_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_serious_offender_data_it_should_displayed_error_message(self):

        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                # self.d.save_screenshot(
                #     f"{self.screenshots_path}(filling_serious_offender_data_"
                #     f"it_should_displayed_error_message_failed.png")
                return False

        except Exception as ex:

            # self.d.save_screenshot(
            #     f"{self.screenshots_path}(filling_serious_offender_data_it_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_serious_offender_data_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_serious_offender_suppress_duplicate_events_data_it_should_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)

            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                # self.d.save_screenshot(
                #     f"{self.screenshots_path}(filling_serious_offender_suppress_duplicate_events_"
                #     f"data_it_should_displayed_error_message_failed.png")
                return False

        except Exception as ex:

            # self.d.save_screenshot(
            #     f"{self.screenshots_path}(filling_serious_offender_suppress_duplicate_events_"
            #     f"data_it_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_serious_offender_suppress_duplicate_events_data_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_masked_face_threshold_data_it_should_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()

            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                # self.d.save_screenshot(
                #     f"{self.screenshots_path}(filling_masked_face_threshold_data"
                #     f"_it_should_displayed_error_message_failed.png")
                return False

        except Exception as ex:

            # self.d.save_screenshot(
            #     f"{self.screenshots_path}(filling_masked_face_threshold_data"
            #     f"_it_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_masked_face_threshold_data_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_masked_face_threshold_suppress_duplicate_events_data_it_should_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.one_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.one_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                # self.d.save_screenshot(
                #     f"{self.screenshots_path}(filling_masked_face_threshold_data_"
                #     f"it_should_displayed_error_message_failed.png")
                return False

        except Exception as ex:

            # self.d.save_screenshot(
            #     f"{self.screenshots_path}(filling_masked_face_threshold_data_"
            #     f"it_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_masked_face_threshold_data_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_masked_face_threshold_serious_offender_data_it_should_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.one_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.one_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                # self.d.save_screenshot(
                #     f"{self.screenshots_path}(filling_masked_face_threshold_serious_offender_suppress"
                #     f"_duplicate_events_should_displayed_error_message_failed.png")
                return False

        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(filling_masked_face_threshold_serious_offender_suppress"
                f"_duplicate_events_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_masked_face_threshold_serious_offender_data_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_masked_face_threshold_serious_offender_suppress_duplicate_events_should_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            masked_face_threshold.clear()
            time.sleep(web_driver.one_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.one_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.one_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                # self.d.save_screenshot(
                #     f"{self.screenshots_path}(filling_masked_face_threshold_serious_offender_suppress"
                #     f"_duplicate_events_should_displayed_error_message_failed.png")
                return False

        except Exception as ex:

            # self.d.save_screenshot(
            #     f"{self.screenshots_path}(filling_masked_face_threshold_serious_offender_suppress"
            #     f"_duplicate_events_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_masked_face_threshold_serious_offender_suppress_duplicate_events_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_face_threshold_it_should_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)

            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())
            face_threshold_field.clear()
            time.sleep(web_driver.one_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                # self.d.save_screenshot(
                #     f"{self.screenshots_path}(filling_serious_offender_data_it_"
                #     f"should_displayed_error_message_failed.png")
                return False

        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(filling_serious_offender_data_it_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_serious_offender_data_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_face_threshold_suppress_duplicate_events_data_it_should_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())
            face_threshold_field.clear()
            time.sleep(web_driver.one_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.one_second)
            suppress_duplicate = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(suppress_duplicate)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(filling_suppress_duplicate_events_"
                    f"data_it_should_displayed_error_message_failed.png")

        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(filling_suppress_duplicate_events_"
                f"data_it_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_suppress_duplicate_events_data_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_face_threshold_serious_offender_data_it_should_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            time.sleep(web_driver.one_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.one_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                # self.d.save_screenshot(
                #     f"{self.screenshots_path}(filling_serious_offender_data_it_should_displayed"
                #     f"_error_message_failed.png")
                return False

        except Exception as ex:

            # self.d.save_screenshot(
            #     f"{self.screenshots_path}(filling_serious_offender_data_it_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_serious_offender_data_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_face_threshold_serious_offender_suppress_duplicate_events_it_should_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())
            face_threshold_field.clear()
            time.sleep(web_driver.one_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.one_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.one_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(filling_face_threshold_serious_offender_suppress_"
                    f"duplicate_events_it_should_displayed_error_message_failed.png")
                return False

        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(filling_face_threshold_serious_offender_suppress_"
                f"duplicate_events_it_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_face_threshold_serious_offender_suppress_duplicate_events_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_face_threshold_masked_face_threshold_it_should_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())
            face_threshold_field.clear()
            time.sleep(web_driver.one_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.one_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.one_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(filling_face_threshold_masked_face_"
                    f"threshold_it_should_displayed_error_message_failed.png")
                return False

        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(filling_face_threshold_masked_face_"
                f"threshold_it_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_face_threshold_masked_face_threshold_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_face_threshold_masked_face_threshold_suppress_duplicate_events_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            time.sleep(web_driver.one_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.one_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.one_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.one_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}(filling_face_threshold_masked_face_threshold_suppress_duplicate_events_displayed_error_message_failed.png")
                return False

        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(filling_face_threshold_masked_face_threshold_"
                f"suppress_duplicate_events_displayed_error_message_failed.png")
            self.logger.info(f"filling_face_threshold_masked_face_threshold_suppress_duplicate_events_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_face_threshold_masked_face_threshold_serious_offender_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            time.sleep(web_driver.one_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.one_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.one_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.one_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(filling_face_threshold_masked_face_threshold"
                    f"_serious_offender_displayed_error_message_failed.png")
                return False

        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(filling_face_threshold_masked_face_threshold"
                f"_serious_offender_displayed_error_message_failed.png")
            self.logger.info(f"filling_face_threshold_masked_face_threshold_serious_offender_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_face_threshold_masked_face_threshold_serious_offender_suppress_duplicate_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            time.sleep(web_driver.one_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.one_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.one_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.one_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.one_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(filling_face_threshold_masked_face_threshold_"
                    f"serious_offender_suppress_duplicate_error_message_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(filling_face_threshold_masked_face_threshold_serious_offender_suppress_duplicate_error_message_failed.png")
            self.logger.info(f"filling_face_threshold_masked_face_threshold_serious_offender_suppress_duplicate_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_description_data_it_should_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(filling_description_data_it_should_displayed_error_message_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(filling_description_data_it_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_description_data_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_description_suppress_duplicate_events_data_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())

            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.one_second)

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(filling_description_suppress_duplicate_"
                    f"events_data_displayed_error_message_failed.png")
                return False

        except Exception as ex:

            self.d.save_screenshot(
                f"{self.screenshots_path}(filling_description_suppress_duplicate_"
                f"events_data_displayed_error_message_failed.png")
            self.logger.info(f"filling_description_suppress_duplicate_events_data_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_description_serious_offender_data_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            time.sleep(web_driver.one_second)
            masked_face_threshold.clear()
            time.sleep(web_driver.one_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.one_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(filling_description_serious_offender_data_displayed"
                    f"_error_message_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(filling_description_serious_offender_data_displayed_error_message_failed.png")
            self.logger.info(f"filling_description_serious_offender_data_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_description_serious_offender_suppress_duplicate_events_displayed_error_message(self):

        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())

            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.one_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(filling_description_serious_offender_"
                    f"suppress_duplicate_events_displayed_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(filling_description_serious_offender_suppress_duplicate_events_displayed_error_message_failed.png")
            self.logger.info(f"filling_description_serious_offender_suppress_duplicate_events_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_description_masked_face_threshold_displayed_error_message(self):

        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.one_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.one_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.two_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(filling_description_masked_face_threshold_"
                    f"displayed_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(filling_description_masked_face_threshold_displayed_error_message_failed.png")
            self.logger.info(f"filling_description_masked_face_threshold_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_description_masked_face_threshold_suppress_duplicate_events_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.one_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            masked_face_threshold.clear()
            time.sleep(web_driver.one_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.one_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}(filling_description_masked_face_threshold_suppress_duplicate_events_displayed_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(filling_description_masked_face_threshold_suppress_duplicate_events_displayed_error_message_failed.png")
            self.logger.info(f"filling_description_masked_face_threshold_suppress_duplicate_events_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_description_masked_face_threshold_serious_offender_display_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}(filling_description_masked_face_threshold_suppress_duplicate_events_displayed_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(filling_description_masked_face_threshold_suppress_duplicate_events_displayed_error_message_failed.png")
            self.logger.info(f"filling_description_masked_face_threshold_serious_offender_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def fill_description_masked_face_threshold_serious_offender_suppress_duplicate_event_display_error_mge(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}(filling_description_masked_face_threshold_serious_offender_suppress_duplicate_events_error_message.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(filling_description_masked_face_threshold_serious_offender_suppress_duplicate_events_error_message.png")
            self.logger.info(f"fill_description_masked_face_threshold_serious_offender_suppress_duplicate_event_display_error_mge_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_description_masked_face_threshold_serious_offender_suppress_duplicate_events_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}(filling_description_masked_face_threshold_serious_offender_suppress_duplicate_events_error_message.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(filling_description_masked_face_threshold_serious_offender_suppress_duplicate_events_error_message.png")
            self.logger.info(f"filling_description_masked_face_threshold_serious_offender_suppress_duplicate_events_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_description_masked_face_threshold_serious_offender_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}(filling_description_data_it_should_displayed_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(filling_description_data_it_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_description_data_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_description_face_threshold_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}(filling_description_data_it_should_displayed_error_message_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(filling_description_data_it_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_description_data_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_description_face_threshold_suppress_duplicate_events_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}(filling_description_face_threshold_suppress_duplicate_events_displayed_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(filling_description_face_threshold_suppress_duplicate_events_displayed_error_message_failed.png")
            self.logger.info(f"filling_description_face_threshold_suppress_duplicate_events_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def description_masked_face_threshold_serious_offender_supress_duplicate_events_display_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(description_masked_face_threshold_serious_offender_"
                    f"supress_duplicate_events_display_error_message_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(description_masked_face_threshold_serious_offender_supress_duplicate_events_display_error_message_failed.png")
            self.logger.info(f"description_masked_face_threshold_serious_offender_supress_duplicate_events_display_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def fill_description_face_threshold_serious_offender_suppress_duplicate_events_displayed_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(fill_description_face_threshold_serious_offender_"
                    f"suppress_duplicate_events_displayed_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(fill_description_face_threshold_serious_offender_suppress_duplicate_events_displayed_error_message_failed.png")
            self.logger.info(f"fill_description_face_threshold_serious_offender_suppress_duplicate_events_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_description_face_threshold_masked_face_threshold_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}(filling_description_data_it_should_displayed_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(filling_description_data_it_should_displayed_error_message_failed.png")
            self.logger.info(f"filling_description_data_it_should_displayed_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_description_face_threshold_masked_face_threshold_suppress_duplicate_events_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())
            time.sleep(web_driver.two_second)
            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}(filling_description_face_threshold_masked_face_threshold_"
                    f"suppress_duplicate_events_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(filling_description_face_threshold_masked_face_threshold_suppress_duplicate_events_error_message_failed.png")
            self.logger.info(f"filling_description_face_threshold_masked_face_threshold_suppress_duplicate_events_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_description_face_threshold_masked_face_threshold_serious_offender_error_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}(filling_description_face_threshold_masked_face_threshold_serious_offender_error_message_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(filling_description_face_threshold_masked_face_threshold_serious_offender_error_message_failed.png")
            self.logger.info(f"filling_description_face_threshold_masked_face_threshold_serious_offender_error_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def description_face_threshold_masked_face_threshold_serious_offender_suppress_duplicate_events_error_msg(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            if self.validate_error_msg():
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}(description_face_threshold_masked_face_threshold_serious_offender_suppress_duplicate_events_error_msg_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}(description_face_threshold_masked_face_threshold_serious_offender_suppress_duplicate_events_error_msg_failed.png")
            self.logger.info(f"description_face_threshold_masked_face_threshold_serious_offender_suppress_duplicate_events_error_msg_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_data_it_should_displayed_success_message(self):
        try:
            self.logger.info("****************** test_TC_EG_070 ***********************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .enrollment_groups_title_by_xpath(), self.d)
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action Dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create Enrollment Groups option is clicked")
            time.sleep(web_driver.one_second)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            time.sleep(web_driver.two_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(), self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            print("success message: ", success_message)
            print("success message: ", ex_success_msg)
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            time.sleep(web_driver.two_second)
            if ex_success_msg.lower() == success_message.lower():
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.logger.info(f"status: {False}")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_070_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_070_exception.png")
            self.logger.info(f"filling_name_data_it_should_displayed_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_suppress_duplicate_events_data_success_message(self):
        try:
            self.logger.info("********************** test_TC_EG_071 **********************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                             action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action Dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .success_message_by_xpath(), self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            time.sleep(web_driver.two_second)
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.logger.info(f"status: {False}")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_071_failed.png")
            return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_071_Exception.png")
            self.logger.info(f"filling_name_suppress_duplicate_events_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_serious_offender_data_success_message(self):
        try:
            self.logger.info(f"***** test_TC_EG_078 *****")
            self.logger.info("****************** test_TC_EG_072 ********************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                                        enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                             action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action Dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)
            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath(), self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.logger.info(f"status: {False}")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_072_failed.png")
            return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_072_Exception.png")
            self.logger.info(f"filling_name_serious_offender_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_serious_offender_suppress_duplicate_events_data_success_message(self):
        try:
            self.logger.info("***************** test_TC_EG_073 *********************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                                        enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action Dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath(), self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"ex msg : {ex_success_msg}")
            self.logger.info(f"ac msg : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_073_failed.png")
            return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_073_Exception.png")
            self.logger.info(f"notes_with_no_filter_combination: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_masked_face_threshold_data_success_message(self):
        try:
            self.logger.info("********************* test_TC_EG_074 ****************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                                        enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                             action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action Dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create Enrollment Groups option is clicked")
            time.sleep(web_driver.one_second)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            masked_face_threshold.clear()
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.two_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .success_message_by_xpath(), self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            time.sleep(web_driver.two_second)
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_074_failed.png")
            return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_074_Exception.png")
            self.logger.info(f"filling_name_masked_face_threshold_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_masked_face_threshold_suppress_duplicate_events_success_message(self):
        try:
            self.logger.info("**************** test_TC_EG_075 **********************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                             action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action Dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .success_message_by_xpath(), self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}(\\filling_name_masked_face_threshold_data_success_message_failed.png")
            return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_075_exception.png")
            self.logger.info(f"filling_name_masked_face_threshold_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_masked_face_threshold_serious_offender_success_message(self):
        try:
            self.logger.info("***************** test_TC_EG_076 **********************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action Dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .success_message_by_xpath(), self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_076_failed.png")
            return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_076_exception.png")
            self.logger.info(f"filling_name_masked_face_threshold_serious_offender_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_masked_face_threshold_serious_offender_suppress_duplicate_events_success_message(self):
        try:
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action Dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                               .success_message_by_xpath(), self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            time.sleep(web_driver.two_second)
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_077_failed.png")
            return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_077_Exception.png")
            self.logger.info(f"filling_name_masked_face_threshold_serious_offender_suppress_duplicate_events_success_message: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_face_threshold_data_success_message(self):
        try:
            self.logger.info("********************* test_TC_EG_079 ******************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            self.logger.info("Action Dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_079_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_079_Exception.png")
            self.logger.info(f"filling_name_face_threshold_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_face_threshold_serious_offender_data_success_message(self):
        try:
            self.logger.info("**************** test_TC_EG_080 ******************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())

            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_080_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_080_Exception.png")
            self.logger.info(f"filling_name_face_threshold_serious_offender_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_face_threshold_serious_offender_suppress_duplicate_events_data_success_message(self):
        try:
            self.logger.info("******************* test_TC_EG_081 ****************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_081_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_081_Exception.png")
            self.logger.info(f"filling_name_face_threshold_serious_offender_suppress_duplicate_events_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_face_threshold_masked_face_threshold_data_success_message(self):
        try:
            self.logger.info("****************** test_TC_EG_082 *******************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_082_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_082_Exception.png")
            self.logger.info(f"filling_name_face_threshold_masked_face_threshold_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_face_threshold_masked_face_threshold_suppress_duplicate_events_data_success_message(self):
        try:
            self.logger.info("************************ test_TC_EG_083 *********************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())

            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())
            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_083_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_083_Exception.png")
            self.logger.info(f"filling_name_face_threshold_masked_face_threshold_suppress_duplicate_events_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_face_threshold_masked_face_threshold_serious_offender_data_success_message(self):
        try:
            self.logger.info("******************* test_TC_EG_084 ****************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())
            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_084_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_084_exception.png")
            self.logger.info(f"filling_name_face_threshold_masked_face_threshold_serious_offender_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def fill_name_face_masked_face_threshold_serious_offender_suppress_duplicate_events_data_success_msg(self):
        try:
            self.logger.info("****************** test_TC_EG_085 *****************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())
            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_085_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_085_exception.png")
            self.logger.info(f"fill_name_face_masked_face_threshold_serious_offender_suppress_duplicate_events_data_success_msg_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_description_data_success_message(self):
        try:
            self.logger.info("********************* test_TC_EG_086 ****************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_086_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_086_exception.png")
            self.logger.info(f"filling_name_description_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_description_suppress_duplicate_events_data_success_message(self):
        try:
            self.logger.info("****************** test_TC_EG_087 ******************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_087_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_087_Exception.png")
            self.logger.info(f"filling_name_description_suppress_duplicate_events_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_description_serious_offender_data_success_message(self):
        try:
            self.logger.info("****************** test_TC_EG_088 ******************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_088_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_088_Exception.png")
            self.logger.info(f"filling_name_description_serious_offender_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_description_serious_offender_suppress_duplicate_events_data_success_message(self):
        try:
            self.logger.info("**************** test_TC_EG_089 *********************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_089_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_089_Exception.png")
            self.logger.info(f"filling_name_description_serious_offender_suppress_duplicate_events_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_description_masked_face_threshold_data_success_message(self):
        try:
            self.logger.info("**************** test_TC_EG_090 ***************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_090_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_090_Exception.png")
            self.logger.info(f"filling_name_description_masked_face_threshold_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_description_masked_face_threshold_suppress_duplicate_events_data_success_message(self):
        try:
            self.logger.info("**************** test_TC_EG_091 **********************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            self.logger.info("Action dropdown is clicked")
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_091_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_091_Exception.png")
            self.logger.info(f"filling_name_description_masked_face_threshold_suppress_duplicate_events_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def fill_name_description_masked_face_threshold_serious_offender_events_data_success_msg(self):
        try:
            self.logger.info("***************** test_TC_EG_092 *****************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_092_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_092_exception.png")
            self.logger.info(f"fill_name_description_masked_face_threshold_serious_offender_events_data_success_msg_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def name_description_masked_face_threshold_serious_offender_suppress_duplicate_events_data_success_msg(self):
        try:
            self.logger.info("***************** test_TC_EG_093 ***************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_093_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_093_exception.png")
            self.logger.info(f"name_description_masked_face_threshold_serious_offender_suppress_duplicate_events_data_success_msg_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_description_face_threshold_data_success_message(self):
        try:
            self.logger.info("************* test_TC_EG_094 ****************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())
            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_094_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_094_Exception.png")
            self.logger.info(f"filling_name_description_face_threshold_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_description_face_threshold_suppress_duplicate_events_data_success_message(self):
        try:
            self.logger.info("********************** test_TC_EG_095 ***********************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())
            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)

            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_095_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_095_Exception.png")
            self.logger.info(f"filling_name_description_face_threshold_suppress_duplicate_events_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_description_face_threshold_serious_offender_events_data_success_message(self):
        try:
            self.logger.info("***************** test_TC_EG_096 *******************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())
            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_096_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_096_Exception.png")
            self.logger.info(f"filling_name_description_face_threshold_serious_offender_events_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def name_description_face_threshold_serious_offender_events_suppress_duplicate_events_data_success_msg(self):
        try:
            self.logger.info("****************** test_TC_EG_097 ***********************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.two_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_097_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_097_Exception.png")
            self.logger.info(f"name_description_face_threshold_serious_offender_events_suppress_duplicate_events_data_success_msg_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def filling_name_description_face_threshold_masked_face_threshold_data_success_message(self):
        try:
            self.logger.info("***************** test_TC_EG_098 *****************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())
            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)

            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_098_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_098_Exception.png")
            self.logger.info(f"filling_name_description_face_threshold_masked_face_threshold_data_success_message_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def name_description_face_threshold_masked_face_threshold_suppress_duplicate_events_data_success_msg(self):
        try:
            self.logger.info("******************** test_TC_EG_099 *******************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.two_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())

            face_threshold_field.clear()
            time.sleep(web_driver.two_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)
            time.sleep(web_driver.two_second)
            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())

            masked_face_threshold.clear()
            time.sleep(web_driver.two_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)

            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)

            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_099_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_099_failed.png")
            self.logger.info(f"name_description_face_threshold_masked_face_threshold_suppress_duplicate_events_data_success_msg_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def name_description_face_masked_face_threshold_serious_offender_data_success(self):
        try:
            self.logger.info("****************** test_TC_EG_0100 **********************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(), self.d)
            create_enrollment.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Create Enrollment Groups option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.one_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())
            face_threshold_field.clear()
            time.sleep(web_driver.one_second)
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)

            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            masked_face_threshold.clear()
            time.sleep(web_driver.one_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)
            time.sleep(web_driver.one_second)
            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.one_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected msg is : {ex_success_msg}")
            self.logger.info(f"actual msg is : {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_0100_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_0100_Exception.png")
            self.logger.info(f"name_description_face_masked_face_threshold_serious_offender_data_success_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def name_description_face_masked_face_threshold_serious_offender_suppress_duplicate_events_data_success(self):
        try:
            self.logger.info("******************** test_TC_EG_0101 *******************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                                        enrollment_groups_button_by_xpath(), self.d)
            self.logger.info(f"enrollment groups btn visible: {enrollment_groups_btn.is_displayed()}")
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info(f"enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                             action_dropdown_button_by_xpath(),
                               self.d)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            time.sleep(web_driver.two_second)
            self.logger.info(f"action btn visible: {action_btn.is_displayed()}")
            action_btn.click()
            self.logger.info(f"Action Dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_enrollment = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                    .create_enrollment_group_button_by_xpath(),
                               self.d)
            self.logger.info(f"create enrollment btn visible: {create_enrollment.is_displayed()}")
            create_enrollment.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Create Enrollment option is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().name_field_by_xpath(),
                               self.d)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"name field visible: {name_field.is_displayed()}")
            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                    .description_field_by_xpath())
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"description field visible: {description_field.is_displayed()}")
            description_field.send_keys(Read_Enrollment_Groups_Components().description_field_data())
            time.sleep(web_driver.one_second)
            face_threshold_field = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().
                                                       face_threshold_field_by_xpath())
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"face threshold visible: {face_threshold_field.is_displayed()}")
            face_threshold_field.clear()
            face_threshold_field = Read_Enrollment_Groups_Components().face_threshold_field_data()
            self.enter_face_thresh_hold(face_threshold_field)

            masked_face_threshold = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                        .masked_face_threshold_field_by_xpath())
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"masked face threshold visible: {masked_face_threshold.is_displayed()}")
            masked_face_threshold.clear()
            time.sleep(web_driver.one_second)
            masked_face_threshold_data = Read_Enrollment_Groups_Components().masked_face_threshold_data()
            self.enter_mask_face_thresh_hold(masked_face_threshold_data)

            serious_offender = Read_Enrollment_Groups_Components().serious_offender_input_data()
            self.select_serious_offender(serious_offender)
            time.sleep(web_driver.one_second)
            supress_duplicate_events = Read_Enrollment_Groups_Components().supress_duplicate_events_input_data()
            self.select_suppress_duplicate_events(supress_duplicate_events)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info(f"save btn visible: {save_button.is_displayed()}")
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            ex_success_msg = Read_Enrollment_Groups_Components().success_message_validation_text()
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().success_message_by_xpath(),self.d)
            success_message = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components()
                                                  .success_message_by_xpath()).text
            self.logger.info(f"expected: {ex_success_msg}")
            self.logger.info(f"actual: {success_message}")
            if ex_success_msg == success_message:
                self.logger.info(f"status: {True}")
                self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.logger.info(f"status: {False}")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_0101_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_0101_exception.png")
            self.logger.info(f"name_description_face_masked_face_threshold_serious_offender_suppress_duplicate_events_data_success_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def verify_that_enrollment_should_be_add_from_enrollment_group_module_end_to_end(self):
        try:
            self.logger.info("**************** test_TC_EG_0102 ****************")
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().enrollment_groups_button_by_xpath(),
                               self.d)
            enrollment_groups_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enrollment_groups_button_by_xpath())
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"enrollment group btn visible: {enrollment_groups_btn.is_displayed()}")
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().action_dropdown_button_by_xpath(),
                               self.d)
            action_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().action_dropdown_button_by_xpath())
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"action btn visible: {action_btn.is_displayed()}")
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().create_enrollment_group_button_by_xpath(),
                               self.d)
            create_enrollment = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().create_enrollment_group_button_by_xpath())
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"create enrollment btn visible: {create_enrollment.is_displayed()}")
            create_enrollment.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Create enrollment groups option is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().name_field_by_xpath(),
                               self.d)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"name field visible: {name_field.is_displayed()}")
            name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data()+str(generate_random_number()))
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"save btn visible: {save_button.is_displayed()}")
            save_button.click()
            self.logger.info("Enrollment groups details is filled and save btn is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().enrollment_button_by_xpath(),
                               self.d)
            enrollment_btn_text = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enrollment_button_by_xpath())
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"enrollment btn text visible: {enrollment_btn_text.is_displayed()}")
            enrollment_btn_text.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"enrollment btn is clicked")
            self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().enroll_filter_button_by_xpath(),
                               self.d)
            time.sleep(web_driver.one_second)
            filter_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enroll_filter_button_by_xpath())
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"filer btn visible: {filter_button.is_displayed()}")
            filter_button.click()
            self.logger.info(f"filter dropdown is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().unlinked_enrollments_by_xpath(),
                               self.d)
            unlinked_enroll = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().unlinked_enrollments_by_xpath())
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"unlinked enrollment btn visible: {unlinked_enroll.is_displayed()}")
            unlinked_enroll.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Unlinked enrollment option is clicked")
            time.sleep(web_driver.two_second)
            enroll_check_box = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enroll_check_box())
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"enroll checkbox visible: {enroll_check_box.is_displayed()}")
            enroll_check_box.click()
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().third_action_dropdown_button_by_xpath(),
                               self.d)
            third_action_btn = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().third_action_dropdown_button_by_xpath())
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"action btn visible: {third_action_btn.is_displayed()}")
            third_action_btn.click()
            self.logger.info(f"action dropdown is clicked")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().add_users_to_groups(),
                               self.d)
            add_users_to_groups = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().add_users_to_groups())
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"add user to group visible: {add_users_to_groups.is_displayed()}")
            add_users_to_groups.click()
            self.logger.info(f"add user to group option is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().enrollment_button_by_xpath(),
                               self.d)
            enrollment_btn_text = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enrollment_button_by_xpath())
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"enrollment btn text visible: {enrollment_btn_text.is_displayed()}")
            enrollment_btn_text.click()
            time.sleep(web_driver.one_second)

            ac_added_enrollment = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().added_enrollment_to_enrollment_groups_by_xpath())
            ac_text = ac_added_enrollment.text
            ex_text = Read_Enrollment_Groups_Components().added_enrollment_to_enrollment_groups_text()
            self.logger.info(f"actual: {ac_text}")
            self.logger.info(f"expected: {ex_text}")
            if ac_added_enrollment.is_displayed():
                self.logger.info(f"status: {True}")
                # self.delete_enrollment_group(Read_Enrollment_Groups_Components().name_field_data())
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_0102_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_0102_exception.png")
            self.logger.info(f"verify_that_enrollment_should_be_add_from_enrollment_group_module_end_to_end_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def verify_that_notification_group_should_be_created_from_enrollment_group_module_end_to_end(self):
        try:
            self.logger.info("******************* test_TC_EG_0103 *******************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().enrollment_groups_button_by_xpath(), self.d)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"enrollment groups btn text visible: {enrollment_groups_btn.is_displayed()}")
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info(f"enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().action_dropdown_button_by_xpath(),
                               self.d)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"action btn  visible: {action_btn.is_displayed()}")
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().create_enrollment_group_button_by_xpath(),
                               self.d)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"create enrollment visible: {create_enrollment.is_displayed()}")
            create_enrollment.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Create Enrollment btn is clicked")
            random_number = random.randint(1, 1000)
            name_field = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().name_field_by_xpath(),
                               self.d)

            name_value = Read_Enrollment_Groups_Components().name_field_data()
            name_value_ran = name_value+str(random_number)
            name_field.send_keys(name_value_ran)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"save btn text visible: {save_button.is_displayed()}")

            save_button.click()
            self.logger.info(f"Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.two_second)
            notification_group_in_enrollment_group = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().notification_group_in_enrollment_group(),
                               self.d)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"notification group in enrollment group visible: {notification_group_in_enrollment_group.is_displayed()}")

            notification_group_in_enrollment_group.click()
            time.sleep(web_driver.one_second)
            third_action_btn = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().third_action_dropdown_button_by_xpath(),
                               self.d)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"third action btn visible: {third_action_btn.is_displayed()}")
            third_action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"In notification groups panel, action dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_notification = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().create_notification_group_btn_by_xpath(),
                               self.d)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"create notification visible: {create_notification.is_displayed()}")
            self.d.execute_script("arguments[0].click();", create_notification)
            self.logger.info("create notification groups option is clicked")
            second_name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                   .second_name_by_xpath(), self.d)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"second name field visible: {second_name_field.is_displayed()}")
            second_name_value = Read_Enrollment_Groups_Components().name_field_data()
            second_name_value_ran = second_name_value + str(random_number)
            second_name_field.send_keys(second_name_value_ran)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().second_save_button_by_xpath())
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"save btn visible: {save_button.is_displayed()}")
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Notification details is filled and save btn is clicked")
            filter_button = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().enroll_filter_button_by_xpath(),
                               self.d)
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"filter btn visible: {filter_button.is_displayed()}")
            filter_button.click()
            self.logger.info("Filter dropdown is clicked")
            time.sleep(web_driver.two_second)
            unlinked_notification_group = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().unlinked_notification_groups(),
                               self.d)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"unlinked notification group visible: {unlinked_notification_group.is_displayed()}")
            unlinked_notification_group.click()
            self.logger.info("Unlinked option is clicked")
            time.sleep(web_driver.two_second)
            filter_notification_search_by_xpath = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().filter_notification_search_by_xpath(),
                               self.d)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"filter notification search  visible: {filter_notification_search_by_xpath.is_displayed()}")
            filter_notification_search_by_xpath.send_keys(second_name_value_ran)
            self.logger.info(f"Enter the NG user name in search box")
            time.sleep(web_driver.two_second)

            ng_select_all_check_box = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().eg_select_check_box_by_xpath())
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"select all check box visible: {ng_select_all_check_box.is_displayed()}")
            ng_select_all_check_box.click()
            time.sleep(web_driver.two_second)
            third_action_btn = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().third_action_dropdown_button_by_xpath(),
                               self.d)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"third action btn visible: {third_action_btn.is_displayed()}")
            third_action_btn.click()
            self.logger.info("third Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            ng_adding_eg_by_xpath = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().ng_adding_eg_by_xpath(),
                               self.d)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"ng adding by eg visible: {ng_adding_eg_by_xpath.is_displayed()}")
            ng_adding_eg_by_xpath.click()
            time.sleep(web_driver.one_second)
            self.logger.info(" Add NG to EG option is clicked")
            time.sleep(web_driver.one_second)

            eg_click = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().enrollment_group_btn_by_xpath())
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info(f"eg visible: {eg_click.is_displayed()}")
            eg_click.click()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components().created_ng_by_xpath(),
                               self.d)
            created_ng = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().created_ng_by_xpath())
            ac_created_ng = created_ng.text
            ex_created_ng = Read_Enrollment_Groups_Components().created_ng_validation_text()+str(random_number)

            created_eg = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().created_eg_by_xpath())
            ac_created_eg = created_eg.text
            ex_created_eg = Read_Enrollment_Groups_Components().created_ng_validation_text()+str(random_number)
            status.append(ac_created_ng == ex_created_ng)
            status.append(ac_created_eg == ex_created_eg)
            self.logger.info(f"ex created ng is : {ex_created_ng}")
            self.logger.info(f"ac created ng is : {ac_created_ng}")
            self.logger.info(f"ex created eg is : {ex_created_eg}")
            self.logger.info(f"ac created eg is : {ac_created_eg}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_0103_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_0103_exception.png")
            self.logger.info(f"verify_that_notification_group_should_be_created_from_enrollment_group_module_end_to_end_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one_no_popup()

    def verify_that_events_should_be_created_from_enrollment_group_module_end_to_end(self):
        try:
            self.logger.info("*********************** test_TC_EG_0104 *********************")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            enrollment_groups_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .enrollment_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", enrollment_groups_btn)
            self.logger.info("enrollment groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                                       .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrollment = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components()
                               .create_enrollment_group_button_by_xpath(),
                               self.d)
            create_enrollment.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Create enrollment option is clicked")
            random_number = random.randint(1, 1000)
            name_field = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                            .name_field_by_xpath(), self.d)
            name_value = Read_Enrollment_Groups_Components().name_field_data()
            name_value_ran = name_value + str(random_number)
            # name_field.send_keys(Read_Enrollment_Groups_Components().name_field_data())
            name_field.send_keys(name_value_ran)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().save_button_by_xpath())
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.two_second)
            events_text = self.explicit_wait(10, "XPATH",
                               Read_Enrollment_Groups_Components()
                               .event_button_by_xpath(),
                               self.d)
            events_text.click()
            time.sleep(web_driver.one_second)
            self.logger.info("In Enrollment details panel, events btn is clicked")
            time.sleep(web_driver.two_second)
            events_action_btn = self.explicit_wait(10, "XPATH",Read_Enrollment_Groups_Components().events_action_dropdown_button_by_xpath(),
                               self.d)
            events_action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            events_refresh_button = self.explicit_wait(10, "XPATH",Read_Enrollment_Groups_Components().events_refresh_button_by_xpath(),
                               self.d)
            status.append(events_refresh_button.is_displayed())
            self.logger.info(f"events refresh option is visible : {events_refresh_button.is_displayed()}")
            status.append(events_refresh_button.is_enabled())
            self.logger.info(f"events refresh option is clickable : {events_refresh_button.is_enabled()}")
            events_refresh_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Status is : {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_0104_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EG_0104_Exception.png")
            self.logger.info(f"verify_events_groups_button_is_activated_and_clickable_failed: {ex}")
            return False
        finally:
            self.click_on_logout_button()

    ################################# Re-usable Methods #############################################

    def click_on_logout_button(self):
        try:
            time.sleep(web_driver.two_second)
            logout_button = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().logout_btn_by_xpath())
            count = 0
            while not logout_button.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for logout btn, count: {count}")
            time.sleep(web_driver.two_second)
            try:
                self.d.execute_script("arguments[0].click();", logout_button)
            except Exception as ex:
                logout_button.click()
                self.logger.info(f"{ex}")
            time.sleep(web_driver.one_second)
            self.d.delete_cookie()
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")

    def delete_enrollment_group(self, group_name):
        action = ActionChains(self.d)
        time.sleep(web_driver.two_second)
        check_bx = self.d \
            .find_element(By.XPATH, Read_Enrollment_Groups_Components().enrollment_group_name_delete(group_name))
        # action.scroll_to_element(check_bx).perform()
        # time.sleep(web_driver.two_second)
        check_bx.click()
        # self.d.execute_script("arguments[0].click();", check_bx)
        time.sleep(web_driver.two_second)
        action_btn = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().
                                         action_dropdown_button_by_xpath(), self.d)
        time.sleep(web_driver.two_second)
        action_btn.click()
        time.sleep(web_driver.two_second)
        delete = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().delete_button_by_xpath(), self.d)
        delete.click()
        time.sleep(web_driver.two_second)
        confirm = self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components()
                                     .delete_popup_yes_btn_by_xpath(), self.d)
        self.d.execute_script("arguments[0].click();", confirm)

    def check_if_the_group_is_deleted(self, group_name):
        group_names = []
        list_ele = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().enrollment_group_list_by_xpath())
        for e in list_ele:
            group_names.append(e.text)
        return group_name not in group_names

    def enter_name(self, name):
        ele = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().name_field_by_xpath())
        ele.send_keys(name)
        time.sleep(web_driver.one_second)

    def enter_description(self, description):
        ele = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().description_field_by_xpath())
        ele.send_keys(description)
        time.sleep(web_driver.one_second)

    def enter_face_thresh_hold(self, face_thresh_hold):
        ele = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().face_threshold_field_by_xpath())
        ele.send_keys(face_thresh_hold)
        time.sleep(web_driver.one_second)

    def enter_mask_face_thresh_hold(self, mask_face_thresh_hold):
        ele = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().masked_face_threshold_field_by_xpath())
        ele.send_keys(mask_face_thresh_hold)
        time.sleep(web_driver.one_second)

    def select_serious_offender(self, serious_offender):
        ele = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().serious_offender_drop_down_by_xpath())
        select = Select(ele)
        select.select_by_visible_text(serious_offender)
        time.sleep(web_driver.one_second)

    def select_suppress_duplicate_events(self, supress_duplicate_events):
        ele = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().supress_duplicate_events_by_xpath())
        select = Select(ele)
        select.select_by_value(supress_duplicate_events)
        time.sleep(web_driver.one_second)

    def validate_error_msg(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().validation_error_message_by_xpath()).text
        return ele == Read_Enrollment_Groups_Components().validation_error_message_validation_text()

    def close_all_panel_one_by_one_no_popup(self):
        try:
            self.logger.info("Closing all panels one by one with no pop up")
            close_panel_list = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().close_all_panel_one_by_one())
            for i in close_panel_list:
                i.click()
                # time.sleep(web_driver.one_second)
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            # self.explicit_wait(10, "XPATH", Read_Enrollment_Groups_Components().close_panel_and_discard_changes(),
            #                    self.d)
            close_panel_and_discard_changes = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().close_panel_and_discard_changes())
            if len(close_panel_and_discard_changes) > 0:
                self.logger.info(f"close panel and discard changes is displayed")
                close_panel_and_discard_changes[0].click()
            else:
                pass
            self.logger.info(f"************************** END ****************************")
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.info(f"{ex}")

    def close_all_panel_one_by_one(self):
        try:
            # close_panel_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().close_all_panel_one_by_one())
            time.sleep(web_driver.one_second)
            cloud_menu = self.d.find_element(By.XPATH, Read_Enrollment_Groups_Components().cloud_menu_by_xpath())
            cloud_menu.click()
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            close_all_panels_menu = self.d.find_elements(By.XPATH, Read_Enrollment_Groups_Components().close_all_panels_btn_by_xpath())
            time.sleep(web_driver.one_second)
            # web_driver.implicit_wait(self, web_driver.one_second, self.d)
            # web_driver.explicit_wait(self, web_driver.one_second, close_all_panels_menu, self.d)
            if len(close_all_panels_menu) > 0:
                close_all_panels_menu[0].click()
                time.sleep(web_driver.one_second)
                self.d.switch_to.alert.accept()
            else:
                pass
            time.sleep(web_driver.one_second)
            # for si in close_panel_list:
            #     i.click()
            #     warning_msg_list = self.d.find_elements(By.XPATH,
            #                                             Read_Identify_and_Enroll_Components().get_pop_up_msg_person_not_registered_by_xpath())
            #     if len(warning_msg_list) > 0:
            #         close_btn_list = self.d.find_elements(By.XPATH,
            #                                               Read_Identify_and_Enroll_Components().get_close_and_cancel_enrollment_btn_by_xpath())
            #         if len(close_btn_list) > 0:
            #             close_btn_list[0].click()
            #         else:
            #             pass
            #     else:
            #         pass
            #     time.sleep(web_driver.one_second)

        except Exception as ex:
            self.logger.error(f"Close all panel one by one exception: {ex}")
