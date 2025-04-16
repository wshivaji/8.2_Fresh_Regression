import random
import time
from pathlib import Path
from selenium.webdriver.support.select import Select
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from selenium.webdriver.common.by import By
from All_Config_Packages._3_User_Roles_Module_Config_Files.User_Roles_Read_Ini import user_roles_read_ini
from All_Config_Packages._6_Notification_Groups_Module_Config_Files.Notification_Groups_Read_INI import \
    Read_Notification_Groups_Components
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import \
    Portal_Menu_Module_read_ini
from Base_Package.Login_Logout_Ops import login, logout


def select_options_value(web_element, value):
    """
    handles drop-down using value
    :param web_element:
    :param value: provide the value present in the value attribute
    :return:
    """
    select = Select(web_element)
    select.select_by_value(value)
    time.sleep(web_driver.one_second)
    

def select_options_visible_text(web_element, visible_text):
    """
    handles a drop-down using visible text
    :param web_element:
    :param visible_text: provide the visible text of the web element
    :return:
    """
    select = Select(web_element)
    select.select_by_visible_text(visible_text)
    time.sleep(web_driver.one_second)


def generate_random_number():
    return random.randint(1, 1000)


class Notification_Groups_Module_pom(web_driver, web_logger):
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

    def close_notification_group_module(self):
        try:
            cloud_menu_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().get_CLOUD_MENU_button_by_xpath())
            cloud_menu_button.click()
            time.sleep(web_driver.one_second)
            close_all_panels_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().
                                                          get_close_all_panels_menu_by_xpath())
            if close_all_panels_button.is_displayed():
                close_all_panels_button.click()
                time.sleep(web_driver.one_second)
            else:
                pass
        except Exception as ex:
            print(ex)

    def Verify_Notification_Groups_submenu_is_visible_and_enabled_in_cloud_menu(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                          .notification_groups_button_by_xpath(), self.d)
            if notification_groups_btn.is_displayed():
                self.logger.info("notification groups btn is displayed")
                status.append(True)
            else:
                self.logger.info("notification groups btn is not displayed")
                status.append(False)

            self.logger.info(f"status: {status}")

            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_001_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_001_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_001_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_001_exception.png")
            self.logger.error(f"test_TC_NG_001 got exception as: {ex.args}")
            return False

    def Verify_user_click_on_Notification_Groups_menu_Notification_Groups_panel_is_displayed(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH",Read_Notification_Groups_Components()
                                                          .notification_groups_button_by_xpath(), self.d)
            notification_groups_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                          .notification_groups_button_by_xpath())
            notification_groups_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("notification groups btn is clicked")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().notification_groups_title_by_xpath(),
                               self.d)
            validate_notification_panel = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().notification_groups_title_by_xpath())
            self.logger.info("notification groups panel is open")
            if validate_notification_panel.is_displayed():
                self.logger.info("notification groups title is displayed")
                status.append(True)
            else:
                self.logger.info("notification groups title is not displayed")
                status.append(False)

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_002_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_002_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_002_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_002_exception.png")
            self.logger.error(f"test_TC_NG_002 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Notification_Groups_title_is_visible_on_Notification_Groups_panel(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            time.sleep(web_driver.two_second)
            validate_notification_title_panel = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                                   .notification_groups_title_by_xpath(), self.d)
            status.append(validate_notification_title_panel.text.lower() == Read_Notification_Groups_Components()
                          .notification_group_title_validation_text().lower())
            self.logger.info(f"Expected Title :"
                             f" {Read_Notification_Groups_Components().notification_group_title_validation_text().lower()}")
            self.logger.info(f"Actual Title : {validate_notification_title_panel.text.lower()}")
            status.append(validate_notification_title_panel.is_displayed())
            self.logger.info(f"NG panel title is visible: {validate_notification_title_panel.is_displayed()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_003_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_003_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_003_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_003_exception.png")
            self.logger.error(f"test_TC_NG_003 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Action_button_is_visible_and_clickable(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                          .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            status.append(action_btn.is_displayed())
            self.logger.info(f"Action btn is visible : {action_btn.is_displayed()}")
            status.append(action_btn.is_enabled())
            self.logger.info(f"Action btn is enabled : {action_btn.is_enabled()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_004_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_004_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_004_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_004_exception.png")
            self.logger.error(f"test_TC_NG_004 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Action_button_has_dropdown_list(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                               .notification_groups_button_by_xpath(),self.d)
            time.sleep(web_driver.one_second)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                               .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("action dropdown is clicked")
            refresh = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                         .refresh_button_by_xpath(), self.d)
            create_notification = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().
                                                      create_notification_group_btn_by_xpath())
            status.append(refresh.is_displayed())
            self.logger.info(f"refresh option is displayed : {refresh.is_displayed()}")
            status.append(create_notification.is_displayed())
            self.logger.info(f"create notification option is displayed : {create_notification.is_displayed()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_005_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_005_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_005_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_005_exception.png")
            self.logger.error(f"test_TC_NG_005 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Action_dropdown_consist_Create_Notification_Group_button_is_visible_and_clickable(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                                          notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                             action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("action dropdown is clicked")
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(), self.d)

            status.append(create_notification.is_displayed())
            self.logger.info(f"create notification option is visible : {create_notification.is_displayed()}")
            status.append(create_notification.is_enabled())
            self.logger.info(f"create notification option is visible : {create_notification.is_enabled()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_006_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_006_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_006_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_006_exception.png")
            self.logger.error(f"test_TC_NG_006 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Action_dropdown_consist_Delete_Selected_Notification_Groups_From_System_button_is_visible_and_clickable(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            notification_groups_btn.click()
            time.sleep(web_driver.one_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            delete_selected_notification_groups = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                                      .delete_selected_notification_groups())
            if delete_selected_notification_groups.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            if delete_selected_notification_groups.is_enabled():
                self.status.append(True)
            else:
                self.status.append(False)
            # delete_selected_notification_groups.click()
            #
            # a = self.d.switch_to.alert
            # ac = a.text
            # a.accept()
            # ex = "There are no alerts selected for deletion."
            # self.logger.info(f"expected: {ex}")
            # self.logger.info(f"actual: {ac}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_007_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_007_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_007_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_007_exception.png")
            self.logger.error(f"test_TC_NG_007 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Action_dropdown_consist_Refresh_button_is_visible_and_clickable(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                                          notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                             action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("action dropdown is clicked")
            refresh_button = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                .refresh_button_by_xpath(), self.d)
            status.append(refresh_button.is_displayed())
            self.logger.info(f"refresh option is visible : {refresh_button.is_displayed()}")
            status.append(refresh_button.is_enabled())
            self.logger.info(f"refresh option is clickable : {refresh_button.is_enabled()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_008_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_008_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_008_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_008_exception.png")
            self.logger.error(f"test_TC_NG_008 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_user_click_on_Create_Notification_Group_Notification_Group_Details_panel_should_be_visible(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                                          notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                             action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("action dropdown is clicked")
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification option is clicked")
            create_notification_details_title = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                                   .notification_group_details_by_xpath(), self.d)
            self.logger.info(f"Expected message :"
                             f" {Read_Notification_Groups_Components().notification_groups_details_validation_text().lower()}")
            self.logger.info(f"Actual message : {create_notification_details_title.text.lower()}")
            t = Read_Notification_Groups_Components().notification_groups_details_validation_text().lower() == \
                create_notification_details_title.text.lower()
            status.append(t)
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_009_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_009_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_009_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_009_exception.png")
            self.logger.error(f"test_TC_NG_009 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_user_click_on_Create_Notification_Group_pop_up_panel_title_is_Notification_Group_Details(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                                          notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                             action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("action dropdown is clicked")
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification option is clicked")
            create_notification_details_sub_title = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                                        .notification_group_details_sub_title_by_xpath(), self.d)
            self.logger.info(f"Expected msg : "
                             f"{Read_Notification_Groups_Components().notification_group_details_sub_title_validation_text().lower()}")
            self.logger.info(f"Actual msg : {create_notification_details_sub_title.text.lower()}")
            t = Read_Notification_Groups_Components().notification_group_details_sub_title_validation_text().lower() == \
                create_notification_details_sub_title.text.lower()
            status.append(t)
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_010_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_010_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_010_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_010_exception.png")
            self.logger.error(f"test_TC_NG_010 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Notification_Group_Cancel_button_is_visible_and_clickable(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                                          notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                             action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("action dropdown is clicked")
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification option is clicked")
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                                    .notification_group_details_by_xpath(), self.d)
            cancel_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                .cancel_button_by_xpath())
            status.append(cancel_button.is_displayed())
            self.logger.info(f"cancel btn is visible: {cancel_button.is_displayed()}")
            status.append(cancel_button.is_enabled())
            self.logger.info(f"cancel btn is clickable: {cancel_button.is_enabled()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_011_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_011_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_011_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_011_exception.png")
            self.logger.error(f"test_TC_NG_011 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Notification_Group_Save_button_is_visible_and_clickable(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                               .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("action dropdown is clicked")
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification option is clicked")
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                                    .notification_group_details_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            status.append(save_button.is_displayed())
            self.logger.info(f"cancel btn is visible: {save_button.is_displayed()}")
            status.append(save_button.is_enabled())
            self.logger.info(f"cancel btn is visible: {save_button.is_enabled()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_012_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_012_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_012_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_012_exception.png")
            self.logger.error(f"test_TC_NG_012 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Notification_Group_NOTIFICATION_GROUP_DETAILS_sub_title_is_visible(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("Notification groups btn is clicked")
            time.sleep(web_driver.one_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Create Notification option is clicked")
            time.sleep(web_driver.one_second)
            create_notification_details_title = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                                    .notification_group_details_by_xpath(), self.d)

            t = Read_Notification_Groups_Components().notification_groups_details_validation_text().lower() == \
                create_notification_details_title.text.lower()
            self.logger.info(f"Ex Title: {Read_Notification_Groups_Components().notification_groups_details_validation_text().lower()}")
            self.logger.info(f"Ac Title: {create_notification_details_title.text.lower()}")
            time.sleep(web_driver.one_second)
            sub_title = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .notification_group_details_sub_title_by_xpath(), self.d)
            status.append(sub_title.is_displayed())
            self.logger.info(f"Subtitle is visible: {sub_title.is_displayed()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_013_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_013_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_013_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_013_exception.png")
            self.logger.error(f"test_TC_NG_013 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Name_text_and_Name_textbox_field_is_visible_and_clickable(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("action dropdown is clicked")
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification option is clicked")
            time.sleep(web_driver.one_second)
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)

            status.append(name_field.is_displayed())
            self.logger.info(f"name field is visible : {name_field.is_displayed()}")
            status.append(name_field.is_enabled())
            self.logger.info(f"name field is enabled : {name_field.is_enabled()}")
            # status.append(name_field.send_keys(Read_Notification_Groups_Components().name_field_data()))
            #
            # save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            # status.append(save_button.is_displayed())
            # time.sleep(web_driver.three_second)
            # status.append(save_button.is_enabled())
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_014_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_014_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_014_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_014_exception.png")
            self.logger.error(f"test_TC_NG_014 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Description_text_and_Description_text_box_field_is_visible_and_clickable(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            self.logger.info("create notification option is clicked")
            time.sleep(web_driver.one_second)
            description_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                   .description_field_by_xpath(), self.d)

            status.append(description_field.is_displayed())
            self.logger.info(f"description field is visible: {description_field.is_displayed()}")
            status.append(description_field.is_enabled())
            self.logger.info(f"description field is enabled: {description_field.is_enabled()}")
            # save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            # status.append(save_button.is_displayed())
            #
            # status.append(save_button.is_enabled())
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_015_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_015_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_015_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_015_exception.png")
            self.logger.error(f"test_TC_NG_015 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_validation_message_Missing_required_parameter_is_populated_when_user_click_on_save_button_with_the_blank(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("action dropdown is clicked")
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            self.logger.info("create Notification option is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().description_field_by_xpath(), self.d)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("save btn is clicked without filling any details")
            time.sleep(web_driver.one_second)
            error_message = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                               .error_message_by_xpath(), self.d)
            status.append(error_message.is_displayed())
            self.logger.info(f"error message is visible: {error_message.is_displayed()}")
            alert_groups = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_group_list_by_xpath())
            checkbox = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_checkbox_by_xpath())
            for i in range(len(alert_groups)):
                if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                    checkbox[i].click()
                    self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                       .action_dropdown_button_by_xpath(), self.d).click()
                    time.sleep(web_driver.one_second)
                    self.explicit_wait(10, "XPATH",
                                       Read_Notification_Groups_Components().delete_selected_notification_groups(),
                                       self.d).click()
                    time.sleep(web_driver.one_second)
                    self.explicit_wait(10, "XPATH",
                                       Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath(),
                                       self.d).click()
            self.logger.info(f"status: {status}")

            if False in status:
                self.logger.info("Expected Error message but No error message is displayed...")
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_016_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_016_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_016_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_016_exception.png")
            self.logger.error(f"test_TC_NG_016 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_user_fills_the_Name_text_box_with_data_and_click_on_Save_button_then_validation_message_Success_the_alert_below_has_been_created_should_populate(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                          .notification_groups_button_by_xpath(),
                               self.d)
            notification_groups_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                          .notification_groups_button_by_xpath())
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            time.sleep(web_driver.one_second)
            self.logger.info("notification groups panel is open")
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                             action_dropdown_button_by_xpath(),
                               self.d)
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(),
                               self.d)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            self.logger.info("create notification option is clicked")
            time.sleep(web_driver.one_second)
            self.logger.info("create notification panel is open")
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(),
                               self.d)
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("notification details is filled and save btn is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                   .success_message_by_xpath(),
                               self.d)
            success_msg_text = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                   .success_message_by_xpath())
            self.logger.info(f"Expected message : {Read_Notification_Groups_Components().success_message_validation_text()}")
            self.logger.info(f"Actual message : {success_msg_text.text}")
            self.logger.info(f"expected message == Actual message "
                             f": {Read_Notification_Groups_Components().success_message_validation_text() == success_msg_text.text}")
            status.append(Read_Notification_Groups_Components().success_message_validation_text() ==
                          success_msg_text.text)
            # success_msg_text.is_displayed()
            alert_groups = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_group_list_by_xpath())
            checkbox = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_checkbox_by_xpath())
            try:
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .action_dropdown_button_by_xpath(), self.d).click()
                        time.sleep(web_driver.one_second)

                        self.explicit_wait(10, "XPATH",
                                           Read_Notification_Groups_Components().delete_selected_notification_groups(),
                                           self.d).click()
                        time.sleep(web_driver.one_second)
                        self.explicit_wait(10, "XPATH",
                                           Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath(),
                                           self.d).click()
            except Exception as ex:
                print("delete NG")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_017_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_017_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            print(ex)
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_017_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_017_exception.png")
            self.logger.error(f"test_TC_NG_017 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_user_fill_the_name_text_box_with_data_and_click_Save_button_then_below_fields_Users_Enrollment_Groups_Events_should_be_activated(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().notification_groups_title_by_xpath(),
                               self.d)
            alert_groups = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_group_list_by_xpath())
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_checkbox_by_xpath())
            for i in range(len(alert_groups)):
                print(alert_groups[i].text)
                if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                    checkbox[i].click()
                    time.sleep(web_driver.one_second)
                    self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                       .action_dropdown_button_by_xpath(), self.d).click()
                    time.sleep(web_driver.one_second)

                    self.explicit_wait(10, "XPATH",
                                       Read_Notification_Groups_Components().delete_selected_notification_groups(),
                                       self.d).click()
                    time.sleep(web_driver.one_second)
                    self.explicit_wait(10, "XPATH",
                                       Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath(),
                                       self.d).click()
            time.sleep(web_driver.one_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("action dropdown is clicked")
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            self.logger.info("create notification option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("notification groups details is filled and save btn is clicked")
            user_text = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .user_button_by_xpath(), self.d)
            status.append(user_text.is_displayed())
            self.logger.info(f"users btn is visible : {user_text.is_displayed()}")
            enrollment_groups_text = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                         .enrollment_group_btn_by_xpath())
            status.append(enrollment_groups_text.is_displayed())
            self.logger.info(f"enrollment groups btn is visible : {enrollment_groups_text.is_displayed()}")
            events_text = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().event_button_by_xpath())
            status.append(events_text.is_displayed())
            self.logger.info(f"events btn is visible : {events_text.is_displayed()}")
            # alert_groups = self.d.find_elements(By.XPATH,
            #                                     Read_Notification_Groups_Components().alert_group_list_by_xpath())
            # checkbox = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_checkbox_by_xpath())
            # for i in range(len(alert_groups)):
            #     if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
            #         checkbox[i].click()
            #
            # self.d.find_element(By.XPATH,
            #                     Read_Notification_Groups_Components().action_dropdown_button_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            # self.d.find_element(By.XPATH,
            #                     Read_Notification_Groups_Components().delete_selected_notification_groups()).click()
            # time.sleep(web_driver.one_second)
            # self.d.find_element(By.XPATH, Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath()).click()
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_018_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_018_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_018_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_018_exception.png")
            self.logger.error(f"test_TC_NG_018 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Notification_Group_Details_panel_while_creating_Notification_Group_below_Users_Enrollment_Groups_Events_should_be_in_disable_mode(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("action dropdown is clicked")
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification option is clicked")
            save_button = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                             .save_button_by_xpath(), self.d)
            save_button.click()
            time.sleep(web_driver.one_second)
            user_text = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().user_button_by_xpath())
            status.append(not user_text.is_enabled())
            self.logger.info(f"users btn is disabled : {not user_text.is_enabled()}")
            enrollment_groups_text = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                         .enrollment_group_btn_by_xpath())
            status.append(not enrollment_groups_text.is_enabled())
            self.logger.info(f"enrollment groups btn is disabled : {not enrollment_groups_text.is_enabled()}")
            events_text = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().event_button_by_xpath())
            status.append(not events_text.is_enabled())
            self.logger.info(f"Events btn is disabled: {not events_text.is_enabled()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_019_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_019_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_019_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_019_exception.png")
            self.logger.error(f"test_TC_NG_019 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_user_click_on_Delete_Groups_From_System_option_without_selecting_the_check_box_it_should_display_a_popup_message(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                          .notification_groups_button_by_xpath())
            time.sleep(web_driver.one_second)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            delete_notification = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                      .delete_selected_option_by_xpath())
            status.append(delete_notification.click())
            time.sleep(web_driver.one_second)
            status.append(self.d.switch_to.alert.accept())
            # status.append(delete_notification.is_displayed())
            # status.append(delete_notification.is_enabled())
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_020_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_020_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_020_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_020_exception.png")
            self.logger.error(f"test_TC_NG_020 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_user_click_on_Refresh_button_Notification_Group_page_should_get_refreshed(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                          .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("action dropdown is clicked")
            refresh_button = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                .refresh_button_by_xpath(), self.d)
            try:
                refresh_button.click()
                time.sleep(web_driver.one_second)
                self.logger.info("refresh option is clicked")
                self.logger.info("panel is refreshed")
                status.append(True)
            except Exception as ex:
                self.logger.info("panel didn't refresh")
                status.append(False)

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_021_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_021_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_021_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_021_exception.png")
            self.logger.error(f"test_TC_NG_021 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_SELECT_ALL_check_box_is_visible_and_clickable(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                          .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            time.sleep(web_driver.one_second)
            select_all_text = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                 .select_all_by_xpath(), self.d)
            status.append(select_all_text.is_displayed())
            self.logger.info(f"select all is visible: {select_all_text.is_displayed()}")
            checkbox_text = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().checkbox_by_xpath())
            status.append(checkbox_text.is_enabled())
            self.logger.info(f"select all checkbox is clickable: {checkbox_text.is_enabled()}")
            checkbox_text.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_022_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_022_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_022_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_022_exception.png")
            self.logger.error(f"test_TC_NG_022 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_user_clicks_on_SELECT_ALL_check_box_all_the_below_check_boxes_should_get_selected(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                          .notification_groups_button_by_xpath(), self.d)

            # notification_groups_btn.click()
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("Clicked on notification_groups_btn")
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                               .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            checkbox = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                               .select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.two_second)
            check_list = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().check_box_list_by_xpath())
            for ele in check_list:
                if "checked" not in ele.get_attribute("class"):
                    status.append(False)
                else:
                    status.append(True)
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_023_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_023_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_023_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_023_exception.png")
            self.logger.error(f"test_TC_NG_023 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_user_clicks_on_SELECT_ALL_uncheck_box_all_the_below_check_boxes_should_get_unselected(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                          .notification_groups_button_by_xpath())

            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("Clicked on notification_groups_btn")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                               .action_dropdown_button_by_xpath(), self.d)
            checkbox = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.two_second)
            checkbox = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().select_checkbox_by_xpath())
            self.d.execute_script("arguments[0].click();", checkbox)
            time.sleep(web_driver.two_second)
            check_list = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().check_box_list_by_xpath())
            for ele in check_list:
                if "checked" in ele.get_attribute("class"):
                    status.append(False)
                else:
                    status.append(True)
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_024_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_024_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_024_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_024_exception.png")
            self.logger.error(f"test_TC_NG_024 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            time.sleep(web_driver.one_second)

    def Verify_user_fills_the_Name_text_box_with_any_data_and_click_on_Save_button_then_validation_message_Success_the_alert_below_has_been_created_should_populate(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                          .notification_groups_button_by_xpath(),
                               self.d)
            notification_groups_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                          .notification_groups_button_by_xpath())
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().action_dropdown_button_by_xpath()).click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().delete_selected_notification_groups()).click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath()).click()
            except Exception as ex:
                print("NG deleted")

            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                             action_dropdown_button_by_xpath(),
                               self.d)
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(),
                               self.d)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            self.logger.info("create notification option is clicked")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(),
                               self.d)
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("notification details is filled and save btn is clicked")
            time.sleep(web_driver.two_second)
            success_msg_text = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                   .success_message_by_xpath(),
                               self.d)
            status.append(Read_Notification_Groups_Components().success_message_validation_text() ==
                          success_msg_text.text)
            self.logger.info(f"actual msg: {success_msg_text.text}")
            self.logger.info(f"expected msg: {Read_Notification_Groups_Components().success_message_validation_text()}")
            self.logger.info(f"expected message == Actual message "
                             f": {Read_Notification_Groups_Components().success_message_validation_text() == success_msg_text.text}")
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().action_dropdown_button_by_xpath()).click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().delete_selected_notification_groups()).click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath()).click()
            except Exception as ex:
                print("NG deleted")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_025_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_025_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_025_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_025_exception.png")
            self.logger.error(f"test_TC_NG_025 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Users_button_is_activated_and_clickable(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().description_field_data())
            time.sleep(web_driver.one_second)
            description_field.is_displayed()

            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("notification details if filled and save btn is clicked")
            users_text = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                             .user_button_by_xpath(), self.d)
            status.append(users_text.is_displayed())
            self.logger.info(f"In notification details panel, users btn is visible: {users_text.is_displayed()}")
            self.logger.info(f"status: {status}")

            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_026_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_026_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_026_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_026_exception.png")
            self.logger.error(f"test_TC_NG_026 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Enrollment_Groups_button_is_activated_and_clickable(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().description_field_data())
            time.sleep(web_driver.one_second)
            description_field.is_displayed()

            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("notification details if filled and save btn is clicked")
            enrollment_grp_text = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                     .enrollment_group_btn_by_xpath(), self.d)
            status.append(enrollment_grp_text.is_displayed())
            self.logger.info(f"In Notification details, EG btn is visible : {enrollment_grp_text.is_displayed()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_027_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_027_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_027_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_027_exception.png")
            self.logger.error(f"test_TC_NG_027 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Events_button_is_activated_and_clickable(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().description_field_data())
            time.sleep(web_driver.one_second)
            description_field.is_displayed()

            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("notification details if filled and save btn is clicked")
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                               .enrollment_group_btn_by_xpath(), self.d)
            events_text = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                              .event_button_by_xpath())
            status.append(events_text.is_displayed())
            self.logger.info(f"In Notification details, Events btn is visible : {events_text.is_displayed()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_028_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_028_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_028_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_028_exception.png")
            self.logger.error(f"test_TC_NG_028 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_user_click_on_Users_then_Users_panel_should_open(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                                          notification_groups_button_by_xpath(),
                               self.d)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                             action_dropdown_button_by_xpath(),
                               self.d)
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                    .create_notification_group_btn_by_xpath(),
                               self.d)
            create_enrollment = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .create_notification_group_btn_by_xpath())
            create_enrollment.click()
            self.logger.info("create notification option is clicked")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(),
                               self.d)
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().description_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Notification details is filled and save btn is clicked")
            time.sleep(web_driver.two_second)
            users_text = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                             .user_button_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", users_text)
            self.logger.info("user btn is clicked in notification details panel")
            time.sleep(web_driver.one_second)
            users_text = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .notification_groups_title_by_xpath(), self.d)

            status.append(users_text.is_displayed())
            self.logger.info(f"users panel is visible : {users_text.is_displayed()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_029_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_029_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_029_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_029_exception.png")
            self.logger.error(f"test_TC_NG_029 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_user_click_on_Enrollment_Groups_then_Enrollment_Groups_panel_should_open(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                                          notification_groups_button_by_xpath(),
                               self.d)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                             action_dropdown_button_by_xpath(),
                               self.d)
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                    .create_notification_group_btn_by_xpath(),
                               self.d)
            create_enrollment = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .create_notification_group_btn_by_xpath())
            create_enrollment.click()
            self.logger.info("create notification option is clicked")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(),
                               self.d)
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().description_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("notification details is filled and save btn is clicked")
            time.sleep(web_driver.two_second)
            enrollment_groups_text = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .enrollment_group_btn_by_xpath(),
                               self.d)

            self.d.execute_script("arguments[0].click();", enrollment_groups_text)
            self.logger.info("Enrollment Group btn clicked on notification details panel")
            time.sleep(web_driver.one_second)
            enrollment_in_text = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().notification_groups_title_by_xpath(),
                               self.d)

            status.append(enrollment_in_text.is_displayed())
            self.logger.info(f"Enrollment panel is displayed : {enrollment_in_text.is_displayed()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_030_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_030_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_030_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_030_exception.png")
            self.logger.error(f"test_TC_NG_030 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_user_click_on_Events_then_Events_panel_should_open(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                                          notification_groups_button_by_xpath(),
                               self.d)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                             action_dropdown_button_by_xpath(),
                               self.d)
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(),
                               self.d)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            self.logger.info("create notification option is clicked")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(),
                               self.d)
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().description_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("notification details is filled and save btn is clicked")
            time.sleep(web_driver.two_second)
            events_text = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                              .event_button_by_xpath(),
                               self.d)

            self.d.execute_script("arguments[0].click();", events_text)
            self.logger.info("events btn is clicked on notification groups details panel")
            time.sleep(web_driver.one_second)
            events_text = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                             .notification_groups_title_by_xpath(), self.d)

            status.append(events_text.is_displayed())
            self.logger.info(f"Events panel is displayed: {events_text.is_displayed()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_031_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_031_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_031_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_031_exception.png")
            self.logger.error(f"test_TC_NG_031 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Notification_Group_Details_Action_button_is_visible_and_clickable(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().notification_groups_title_by_xpath(),
                               self.d)
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().action_dropdown_button_by_xpath()).click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().delete_selected_notification_groups()).click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath()).click()
            except Exception as ex:
                print("NG deleted")

            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("notification details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            action_btn_dropdown = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                     .notification_groups_details_action_dropdown_button_by_xpath(), self.d)

            status.append(action_btn_dropdown.is_enabled())
            self.logger.info(f"In NG details panel, Action is visible: {action_btn_dropdown.is_enabled()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_032_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_032_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            print(ex)
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_032_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_032_exception.png")
            self.logger.error(f"test_TC_NG_032 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Notification_Group_Details_Action_dropdown_has_Edit_button_is_visible_and_clickable(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().notification_groups_title_by_xpath(),
                               self.d)
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .action_dropdown_button_by_xpath(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .delete_selected_notification_groups(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH",
                                           Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath(),
                                           self.d).click()
            except Exception as ex:
                print("NG deleted")

            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("action dropdown is clicked")
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("notification details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().success_message_by_xpath(), self.d)
            action_btn_dropdown = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                     .notification_groups_details_action_dropdown_button_by_xpath())

            action_btn_dropdown.click()
            self.logger.info("notification details, Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            edit_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                          .edit_button_by_xpath(), self.d)
            status.append(edit_btn.is_enabled())
            self.logger.info(f"edit btn is visible: {edit_btn.is_enabled()}")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_033_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_033_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_033_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_033_exception.png")
            self.logger.error(f"test_TC_NG_033 got exception as: {ex.args}")
            return False
        # finally:
        #     self.close_all_panel_one_by_one()

    def Verify_Notification_Groups_Functionality_without_filling_any_data_it_should_displayed_Missing_required_parameter_message(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                     .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            self.logger.info("create notification option is clicked")
            save_button = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                             .save_button_by_xpath(), self.d)
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("notification details are filled with some data missing and save btn is clicked")
            time.sleep(web_driver.one_second)
            status.append(self.validate_error_msg())
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.info(f"expected error message: 'Missing required field' actual: No message displayed")
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_034_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_034_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_034_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_034_exception.png")
            self.logger.error(f"test_TC_NG_034 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Notification_Groups_Functionality_by_filling_Description_data_it_should_displayed_Missing_required_parameter_message(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)

            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                               .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                             action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("action dropdown is clicked")
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification option is clicked")
            description_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                    .description_field_by_xpath(), self.d)
            # description_field.sendkeys("notification Group")
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            self.logger.info("notification details are filled with some data missing and save btn is clicked")
            save_button.click()
            time.sleep(web_driver.one_second)
            status.append(self.validate_error_msg())
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.info(f"expected error message: 'Missing required field' actual: No message displayed")
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_035_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_035_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_035_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_035_exception.png")
            self.logger.error(f"test_TC_NG_035 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Notification_Groups_Functionality_by_filling_Name_data_it_should_displayed_Success_the_alert_below_has_been_created_message(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().notification_groups_button_by_xpath(),
                               self.d)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .action_dropdown_button_by_xpath(), self.d).click()
                        time.sleep(web_driver.one_second)
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .delete_selected_notification_groups(), self.d).click()
                        time.sleep(web_driver.one_second)
                        self.explicit_wait(10, "XPATH",
                                           Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath(),
                                           self.d).click()
            except Exception as ex:
                print("NG deleted")

            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().action_dropdown_button_by_xpath(),
                               self.d)
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(),
                               self.d)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()

            self.logger.info("create notification option is clicked")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(),
                               self.d)
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("notification details is filled and save btn is clicked")
            time.sleep(web_driver.two_second)
            status.append(self.validate_successful_message())
            action_btn_dropdown = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                      .notification_groups_details_action_dropdown_button_by_xpath())

            status.append(action_btn_dropdown.is_enabled())
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .action_dropdown_button_by_xpath(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .delete_selected_notification_groups(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH",
                                           Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath(),
                                           self.d).click()
            except Exception as ex:
                print("NG deleted")

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_036_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_036_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_036_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_036_exception.png")
            self.logger.error(f"test_TC_NG_036 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_Notification_Groups_Functionality_by_filling_Name_and_Description_data_it_should_displayed_Success_the_alert_below_has_been_created_message(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                               .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification_groups_btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .action_dropdown_button_by_xpath(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .delete_selected_notification_groups(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH",
                                           Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath(),
                                           self.d).click()
            except Exception as ex:
                print("NG deleted")

            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                               .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .name_field_by_xpath(), self.d)
            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().description_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("notification details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            status.append(self.validate_successful_message())
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .action_dropdown_button_by_xpath(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .delete_selected_notification_groups(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH",
                                           Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath(),
                                           self.d).click()
            except Exception as ex:
                print("NG deleted")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_037_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_037_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_037_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_037_exception.png")
            self.logger.error(f"test_TC_NG_037 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_that_when_user_click_on_action_button_dropdown_and_click_on_edit_button_then_Name_and_Description_field_should_appear(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH",Read_Notification_Groups_Components()
                               .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            time.sleep(web_driver.one_second)
            self.logger.info("notification groups btn is clicked")
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().notification_groups_title_by_xpath(),
                               self.d)
            alert_groups = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_group_list_by_xpath())
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_checkbox_by_xpath())
            time.sleep(web_driver.one_second)
            for i in range(len(alert_groups)):
                print(alert_groups[i].text)
                if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                    checkbox[i].click()
                    self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                       .action_dropdown_button_by_xpath(), self.d).click()
                    time.sleep(web_driver.one_second)

                    self.explicit_wait(10, "XPATH",
                                       Read_Notification_Groups_Components().delete_selected_notification_groups(),
                                       self.d).click()
                    time.sleep(web_driver.one_second)
                    self.explicit_wait(10, "XPATH",
                                       Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath(),
                                       self.d).click()
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                     .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .name_field_by_xpath(), self.d)
            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().description_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Notification details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .new_second_action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Notification details, Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            edit_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                          .edit_button_by_xpath(), self.d)
            edit_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("edit btn is clicked")
            if name_field.is_displayed():
                self.logger.info("name field is displayed")
                status.append(True)
            else:
                self.logger.info("name field is not displayed")
                status.append(False)
            if description_field.is_displayed():
                self.logger.info("Description field is displayed")
                status.append(True)
            else:
                self.logger.info("Description field is not displayed")
                status.append(False)
            time.sleep(web_driver.one_second)

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_038_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_038_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_038_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_038_exception.png")
            self.logger.error(f"test_TC_NG_038 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_that_user_can_edit_update_Name_field_and_Description_field(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                                          notification_groups_button_by_xpath(),
                               self.d)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            time.sleep(web_driver.two_second)
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .action_dropdown_button_by_xpath(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .delete_selected_notification_groups(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH",
                                           Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath(),
                                           self.d).click()
            except Exception as ex:
                print("NG deleted")

            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().
                                             action_dropdown_button_by_xpath(),
                               self.d)
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(),
                               self.d)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            self.logger.info("create notification option is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(),
                               self.d)
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)
            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().description_field_data())
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Notification details is filled and save btn is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                    .new_second_action_dropdown_button_by_xpath(),
                               self.d)
            second_action_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .new_second_action_dropdown_button_by_xpath())
            second_action_btn.click()
            self.logger.info("Notification group details, action dropdown is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().edit_button_by_xpath(),
                               self.d)
            edit_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().edit_button_by_xpath())
            status.append(edit_btn.is_enabled())
            edit_btn.click()
            self.logger.info("edit option is clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(),
                               self.d)
            new_name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)
            new_name_field.clear()
            time.sleep(web_driver.one_second)
            new_name_field.send_keys(Read_Notification_Groups_Components().new_name_field_data())
            time.sleep(web_driver.one_second)
            new_description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                        .description_field_by_xpath())
            new_description_field.clear()
            time.sleep(web_driver.one_second)
            new_description_field.send_keys(Read_Notification_Groups_Components().description_field_new_data())
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            save_button.click()
            self.logger.info("Notification details is modified and save btn is clicked")
            time.sleep(web_driver.two_second)
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for groups in alert_groups:
                    print(f"{groups.text}")
                print(f"new_name: {Read_Notification_Groups_Components().new_name_field_data()}")
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().new_name_field_data():
                        print(f"new_name: {Read_Notification_Groups_Components().new_name_field_data()}")
                        checkbox[i].click()
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .action_dropdown_button_by_xpath(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .delete_selected_notification_groups(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH",
                                           Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath(),
                                           self.d).click()
            except Exception as ex:
                print("NG deleted")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_039_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_039_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_039_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_039_exception.png")
            self.logger.error(f"test_TC_NG_039 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_that_user_click_on_Cancel_button_then_Name_field_and_Description_field_should_disappear(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().action_dropdown_button_by_xpath()).click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().delete_selected_notification_groups()).click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath()).click()
            except Exception as ex:
                print("NG deleted")
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            self.logger.info("create notification option is clicked")
            time.sleep(web_driver.one_second)
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)
            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())

            description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().description_field_data())

            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Notification details is modified and save btn is clicked")
            second_action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                   .new_second_action_dropdown_button_by_xpath(), self.d)
            second_action_btn.click()
            self.logger.info("In Notification details panel, Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            edit_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                          .edit_button_by_xpath(), self.d)
            edit_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("edit option is clicked")
            cancel_button = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                               .cancel_button_by_xpath(), self.d)
            status.append(cancel_button.is_enabled())
            cancel_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("cancel btn is clicked")
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().action_dropdown_button_by_xpath()).click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().delete_selected_notification_groups()).click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath()).click()
            except Exception as ex:
                print("NG deleted")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_040_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_040_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_040_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_040_exception.png")
            self.logger.error(f"test_TC_NG_040 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def click_on_edit_button_then_name_and_description_field_should_appear(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            alert_groups = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_group_list_by_xpath())
            checkbox = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_checkbox_by_xpath())
            for i in range(len(alert_groups)):
                if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                    checkbox[i].click()
                    time.sleep(web_driver.one_second)
                    self.d.find_element(By.XPATH,
                                        Read_Notification_Groups_Components().action_dropdown_button_by_xpath()).click()
                    time.sleep(web_driver.one_second)
                    self.d.find_element(By.XPATH,
                                        Read_Notification_Groups_Components().delete_selected_notification_groups()).click()
                    time.sleep(web_driver.one_second)
                    self.d.find_element(By.XPATH,
                                        Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath()).click()
            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)
            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                              .description_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            action_btn_dropdown = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                      .notification_groups_details_action_dropdown_button_by_xpath())

            status.append(action_btn_dropdown.is_enabled())
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_0_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_0_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_0_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_0_exception.png")
            self.logger.error(f"test_TC_NG_0 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_users_should_be_created_from_Notification_Group_module(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification groups btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .action_dropdown_button_by_xpath(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .delete_selected_notification_groups(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH",
                                           Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath(),
                                           self.d).click()
            except Exception as ex:
                print("NG deleted")

            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            self.logger.info("create enotification option is clicked")
            time.sleep(web_driver.one_second)
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .name_field_by_xpath(), self.d)
            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().description_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Notification details is filled and save btn is clicked")
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().success_message_by_xpath(), self.d)
            users_text = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                             .user_button_by_xpath())
            users_text.click()
            self.logger.info("In notification details panel, users btn is clicked")
            third_action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                  .third_action_dropdown_button_by_xpath(), self.d)
            third_action_btn.click()
            self.logger.info("Users Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_user = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                             .create_users_by_xpath(), self.d)
            create_user.click()
            self.logger.info("Create user option is clicked")
            ex_username = Read_Notification_Groups_Components().user_name_input_data() + str(generate_random_number())
            self.enter_user_name(ex_username)
            time.sleep(web_driver.one_second)
            self.enter_first_name(Read_Notification_Groups_Components().first_name_input_data())
            time.sleep(web_driver.one_second)
            self.enter_last_name(Read_Notification_Groups_Components().last_name_input_data())
            # self.select_user_role(Read_Notification_Groups_Components().user_role_input_data())
            time.sleep(web_driver.one_second)
            user_role_ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().user_role_options_by_xpath())
            user_role_ele.click()
            time.sleep(web_driver.one_second)
            # sel = Select(self.d.find_element(By.XPATH, Read_Notification_Groups_Components().user_role_options_by_xpath()))
            # sel.select_by_visible_text(Read_Notification_Groups_Components().user_role_input_data())
            role_options_inside_dropdown = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components()
                                                                .get_role_option_in_user_role_dropdown_by_xpath())

            for role in role_options_inside_dropdown:
                if role.text == user_roles_read_ini().get_so_user_role():
                    role.click()
            self.enter_password(Read_Notification_Groups_Components().password_data_input())
            time.sleep(web_driver.one_second)
            self.select_region(Read_Notification_Groups_Components().region_data_input())
            time.sleep(web_driver.one_second)
            # region_ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().region_by_xpath())
            # region_ele.click()
            # time.sleep(web_driver.two_second)
            # region_list_by_xpath = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
            #                                            .region_list_by_xpath())
            # region_list_by_xpath.click()
            email = f"{ex_username}@facefirst.com"
            self.user_email_by_xpath(email)
            # self.user_email_by_xpath(Read_Notification_Groups_Components().email_input_data())
            self.select_time_zone(Read_Notification_Groups_Components().time_zone_input_data())
            time.sleep(web_driver.two_second)
            second_save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                     .second_save_button_by_xpath())
            second_save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Users details is filled and save btn is clicked")

            filter_button = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                               .users_filter_button_by_xpath(), self.d)
            filter_button.click()
            self.logger.info("Users details is filled and save btn is clicked")
            time.sleep(web_driver.three_second)
            unlinked_users = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                .user_filter_drp_dwn_button_by_xpath(), self.d)
            unlinked_users.click()
            self.logger.info("Users filter dropdown is clicked")
            time.sleep(web_driver.two_second)
            users_search_box = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                   .users_search_box_by_xpath())
            users_search_box.send_keys(ex_username)
            self.logger.info(f"Enter {ex_username} in users search box")
            time.sleep(web_driver.two_second)

            select_check_box = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                   .users_select_check_box_by_xpath())
            select_check_box.click()
            self.logger.info(f"select the checkbox for user : {ex_username}")
            time.sleep(web_driver.one_second)
            third_action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                   .third_action_dropdown_button_by_xpath(), self.d)
            third_action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.one_second)
            add_users = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .add_users_by_xpath(), self.d)
            add_users.click()
            self.logger.info("add user option is clicked")
            time.sleep(web_driver.two_second)
            users_text = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .user_button_by_xpath(), self.d)
            users_text.click()
            self.logger.info("click on users btn in notification details panel")
            time.sleep(web_driver.two_second)
            register_user = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                               .register_username_by_xpath(), self.d)
            ac_register_user_name = register_user.text
            self.logger.info(f"Expected user name: {ex_username}")
            self.logger.info(f"Actual user name: {ac_register_user_name}")
            if ex_username == ac_register_user_name:
                status.append(True)
            else:
                status.append(False)
            self.logger.info(f"status: {status}")

            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_041_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_041_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            print(ex)
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_041_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_041_exception.png")
            self.logger.error(f"test_TC_NG_041 got exception as: {ex.args}")
            return False
        # finally:
            # self.close_notification_group_module()

    def verify_that_enrollment_groups_should_be_created_from_notification_group_module(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            self.logger.info("notification btn is clicked")
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().action_dropdown_button_by_xpath()).click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().delete_selected_notification_groups()).click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath()).click()
            except Exception as ex:
                print("NG deleted")

            action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            self.logger.info("create notification option is clicked")
            time.sleep(web_driver.one_second)
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .name_field_by_xpath(), self.d)
            name_field.send_keys(Read_Notification_Groups_Components().name_field_data())
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().description_field_data())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Notification details is filled and save btn is clicked")
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().success_message_by_xpath(), self.d)
            enrollment_groups_text = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                         .enrollment_group_btn_by_xpath())

            enrollment_groups_text.click()
            self.logger.info("In Notification groups details panel, Enrollment groups btn is clicked")
            time.sleep(web_driver.two_second)
            third_action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                   .third_action_dropdown_button_by_xpath(), self.d)
            third_action_btn.click()
            self.logger.info("In enrollment Group panel, Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_enrolmment_grp = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                        .create_enrollment_group_by_xpath(), self.d)
            create_enrolmment_grp.click()
            self.logger.info("Create enrollment group option is clicked")
            ex_ntf_group = Read_Notification_Groups_Components().name_field_data() + str(generate_random_number())
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                             .name_field_by_xpath_enrolment(), self.d)

            name_field.send_keys(ex_ntf_group)

            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                              .second_save_button_by_xpath())
            save_button.click()
            self.logger.info("Enrollment details is filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            filter_button = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                               .users_filter_button_by_xpath(), self.d)
            filter_button.click()
            self.logger.info("Filter Dropdown is clicked")
            time.sleep(web_driver.one_second)
            unlinked_enrollment_grp = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                          .unlinked_enrollment_group_by_xpath(), self.d)
            unlinked_enrollment_grp.click()
            self.logger.info("Unlink option is clicked")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Read_Notification_Groups_Components().enrollment_name(ex_ntf_group)).click()
            third_action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                   .third_action_dropdown_button_by_xpath(), self.d)
            third_action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            add_alert_to_user = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                   .add_alert_to_groups(), self.d)
            add_alert_to_user.click()
            self.logger.info("Add alert to group option is clicked")
            time.sleep(web_driver.two_second)
            registered_enrollment_groups = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                               .registered_enrollment_groups(), self.d)
            ac_text_enrollment_user = registered_enrollment_groups.text
            self.logger.info(f"Expected EG: {registered_enrollment_groups.text}")
            self.logger.info(f"Actual EG: {ac_text_enrollment_user}")
            if ex_ntf_group == ac_text_enrollment_user:
                status.append(True)
            else:
                status.append(False)
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_042_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_042_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_042_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_042_exception.png")
            self.logger.error(f"test_TC_NG_042 got exception as: {ex.args}")
            return False
        finally:
            self.close_notification_group_module()

    def verify_that_events_should_be_created_from_notification_group_module(self):
        try:
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                         .notification_groups_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", notification_groups_btn)
            time.sleep(web_driver.one_second)
            self.logger.info("notification groups btn is clicked")
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .action_dropdown_button_by_xpath(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .delete_selected_notification_groups(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH",
                                           Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath(),
                                           self.d).click()
            except Exception as ex:
                print("NG deleted")

            action_btn = self.explicit_wait(10, "XPATH",Read_Notification_Groups_Components()
                               .action_dropdown_button_by_xpath(), self.d)
            action_btn.click()
            self.logger.info("Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            create_notification = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                      .create_notification_group_btn_by_xpath(), self.d)
            create_notification.click()
            time.sleep(web_driver.one_second)
            self.logger.info("create notification option is clicked")
            name_field = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                            .name_field_by_xpath(), self.d)

            name_field.send_keys(Read_Notification_Groups_Components().name_field_data()+ str(generate_random_number()))
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                    .description_field_by_xpath())
            description_field.send_keys(Read_Notification_Groups_Components().description_field_data())
            description_field.is_displayed()
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
            save_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Notification details is filled and save btn is clicked")
            self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().success_message_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            events_text = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                              .event_button_by_xpath())
            # events_text.click()
            self.d.execute_script("arguments[0].click();", events_text)
            self.logger.info("In Notification details panel, events btn is clicked")
            events_action_btn = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                    .events_action_dropdown_button_by_xpath(), self.d)
            events_action_btn.click()
            self.logger.info("In Events panel, Action dropdown is clicked")
            time.sleep(web_driver.one_second)
            events_refresh_button = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                                       .events_refresh_button_by_xpath(), self.d)
            status.append(events_refresh_button.is_displayed())
            self.logger.info(f"refresh option is visible : {events_refresh_button.is_displayed()}")
            status.append(events_refresh_button.is_enabled())
            self.logger.info(f"refresh option is enabled : {events_refresh_button.is_enabled()}")
            events_refresh_button.click()
            time.sleep(web_driver.three_second)
            try:
                alert_groups = self.d.find_elements(By.XPATH,
                                                    Read_Notification_Groups_Components().alert_group_list_by_xpath())
                checkbox = self.d.find_elements(By.XPATH,
                                                Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                for i in range(len(alert_groups)):
                    if alert_groups[i].text == Read_Notification_Groups_Components().name_field_data():
                        checkbox[i].click()
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .action_dropdown_button_by_xpath(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                           .delete_selected_notification_groups(), self.d).click()
                        time.sleep(web_driver.two_second)
                        self.explicit_wait(10, "XPATH",
                                           Read_Notification_Groups_Components().delete_popup_yes_btn_by_xpath(),
                                           self.d).click()
            except Exception as ex:
                print("NG deleted")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_043_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_043_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_NG_043_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NG_043_exception.png")
            self.logger.error(f"test_TC_NG_043 got exception as: {ex.args}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    ################################# Resuable Methods #############################################

    # def click_on_logout_button(self):
    #     try:
    #         time.sleep(web_driver.one_second)
    #         logout_button = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_logout_button_on_portal_by_xpath())
    #         while not logout_button.is_displayed():
    #             time.sleep(web_driver.one_second)
    #         time.sleep(web_driver.one_second)
    #         try:
    #             self.d.execute_script("arguments[0].click();", logout_button)
    #         except Exception as ex:
    #             logout_button.click()
    #         time.sleep(web_driver.one_second)
    #         self.d.delete_cookie()
    #     except Exception as ex:
    #         msg = str(ex)
    #         if msg.__contains__('not clickable at point'):
    #             print("Exception crated: ", ex, " #returning false# ")
    #             self.d.save_screenshot(
    #                 f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_logout_pg_03.png")
    #             return False

    def enter_name(self, name):
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().name_field_by_xpath())
        ele.send_keys(name)
        time.sleep(web_driver.one_second)

    def enter_description(self, description):
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().description_field_by_xpath())
        ele.send_keys(description)
        time.sleep(web_driver.one_second)

    def validate_error_msg(self):
        time.sleep(web_driver.one_second)
        self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().validation_error_message_by_xpath(),
                           self.d)
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().validation_error_message_by_xpath()).text
        self.logger.info(f"actual msg: {ele}")
        self.logger.info(f"expected msg: {Read_Notification_Groups_Components().validation_error_message_validation_text()}")
        time.sleep(web_driver.one_second)
        return ele == Read_Notification_Groups_Components().validation_error_message_validation_text()

    def close_all_panel_one_by_one(self):
        time.sleep(web_driver.one_second)
        close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
        if len(close_panel) > 0:
            for i in range(len(close_panel)):
                close_panel[i].click()
                alerts_list = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().user_close_panel_and_discard_changes())
                if len(alerts_list) > 0:
                    if self.d.find_element(By.XPATH, Read_Notification_Groups_Components().user_close_panel_and_discard_changes()).is_displayed():
                        self.d.find_element(By.XPATH, Read_Notification_Groups_Components().user_close_panel_and_discard_changes()).click()
                    else:
                        pass
                time.sleep(web_driver.one_second)
        return True

    def close_all_panel_one_by_one_no_popup(self):
        try:
            time.sleep(web_driver.one_second)
            close_panel_list = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())                                                    
            for i in close_panel_list:
                i.click()
                time.sleep(web_driver.one_second)
            return True

        except Exception as ex:
            self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\close_all_panel_failed_pg_03.png")
            return False

    # ############################################################################

    def click_on_save_btn(self):
        """
        clicks on save button
        """
        save = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
        save.click()
        time.sleep(web_driver.one_second)

    def enter_user_name(self, user_name):
        """
        fills user name field
        :param user_name:
        """
        user_name_txt_bx = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components()
                                              .user_name_by_xpath(), self.d)
        user_name_txt_bx.send_keys(user_name)
        time.sleep(web_driver.one_second)


    def enter_first_name(self, first_name):
        """
        fills first name field
        :param first_name:
        """
        first_name_txt_bx = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().first_name_by_xpath())
        first_name_txt_bx.send_keys(first_name)
        time.sleep(web_driver.one_second)

    def enter_last_name(self, last_name):
        """
        fills last name field
        :param last_name:
        """
        last_name_txt_bx = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().last_name_by_xpath())
        last_name_txt_bx.send_keys(last_name)
        time.sleep(web_driver.one_second)

    def select_user_role(self, role_data_text):
        """
        handles user role drop down using visible text of the element
        :param role_data_text:
        :return:
        """
        user_role_ele = self.d.find_element(By.XPATH,
                                            Read_Notification_Groups_Components().user_role_options_by_xpath())
        sel = Select(user_role_ele)
        sel.select_by_visible_text(role_data_text)
        time.sleep(web_driver.one_second)

    def enter_password(self, password):
        """
        fills password field
        :param password:
        :return:
        """
        new_password = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().new_password_by_xpath())
        confirm_password = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                               .confirm_password_by_xpath())
        new_password.send_keys(password)
        confirm_password.send_keys(password)
        time.sleep(web_driver.one_second)

    def select_options_visible_text(web_element, visible_text):
        """
        handles a drop-down using visible text
        :param web_element:
        :param visible_text: provide the visible text of the web element
        :return:
        """
        select = Select(web_element)
        select.select_by_visible_text(visible_text)
        time.sleep(web_driver.one_second)

    def enter_mis_match_password(self, password, confirm_password):
        """
        fills password field
        :param password:
        :param confirm_password:
        :return:
        """
        new_password = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().new_password_by_xpath())
        conf_password = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().confirm_password_by_xpath())
        new_password.send_keys(password)
        time.sleep(web_driver.one_second)
        conf_password.send_keys(confirm_password)
        time.sleep(web_driver.one_second)

    def enter_title(self, title):
        title_ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().title_by_xpath())
        title_ele.send_keys(title)
        time.sleep(web_driver.one_second)

    def enter_department(self, department):
        department_ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().department_by_xpath())
        department_ele.send_keys(department)
        time.sleep(web_driver.one_second)

    def validate_required_user_role_is_selected(self, required_option):
        """
        validate the user role provided is selected.
        :param required_option:
        """
        user_role_ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().user_role_by_xpath())
        select = Select(user_role_ele)
        time.sleep(web_driver.one_second)
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
        region_ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().region_by_xpath())
        region_ele.click()
        time.sleep(web_driver.two_second)
        region_text_list = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().region_list_by_xpath())
        expected_region_text = region_text
        try:
            for i in range(len(region_text_list) + 1):
                actual_zone_text = region_text_list.__getitem__(i).text
                print(actual_zone_text)
                print(expected_region_text)
                if expected_region_text.upper() in actual_zone_text.upper():
                    region_text_list.__getitem__(i).click()
                    break
            save = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().region_save_btn_by_xpath())
            self.d.execute_script("arguments[0].click();", save)
        except Exception as ex:
            str(ex)

    def validate_region(self, region_text):
        """
        validate the selected region is correct
        :param region_text:
        :return:
        """
        region_output = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().region_selected_by_xpath())
        time.sleep(web_driver.one_second)
        return region_output.text.lower() in str(region_text).lower()

    def select_time_zone(self, use_value):
        """
        selects time zone using the value of the element
        :param use_value:
        :return:
        """
        time_zone = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().time_zone_by_xpath())
        select_options_value(time_zone, use_value)
        time.sleep(web_driver.one_second)

    def user_email_by_xpath(self, email):
        """
        fills email field
        :param email:
        """
        email_txt_bx = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().user_email_by_xpath())
        email_txt_bx.send_keys(email)
        time.sleep(web_driver.one_second)

    def enter_alert_email(self, alert_email):
        """
        fills email field
        :param alert_email:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().alert_email_by_xpath())
        ele.send_keys(alert_email)
        time.sleep(web_driver.one_second)

    def enter_alert_phone_no(self, alert_phone_no):
        """
        fills email field
        :param alert_phone_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().alert_phone_number_by_xpath())
        ele.send_keys(alert_phone_no)
        time.sleep(web_driver.one_second)

    def enter_address(self, address):
        """
        fills email field
        :param address:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().address_by_xpath())
        ele.send_keys(address)
        time.sleep(web_driver.one_second)

    def enter_city(self, city):
        """
        fills email field
        :param city:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().city_by_xpath())
        ele.send_keys(city)
        time.sleep(web_driver.one_second)

    def enter_state(self, state):
        """
        fills email field
        :param state:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().state_by_xpath())
        ele.send_keys(state)
        time.sleep(web_driver.one_second)

    def enter_postal_code(self, postal_code):
        """
        fills email field
        :param postal_code:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().postal_code_by_xpath())
        ele.send_keys(postal_code)
        time.sleep(web_driver.one_second)

    def enter_home_ph_no(self, home_ph_no):
        """
        fills email field
        :param home_ph_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().home_phone_number_by_xpath())
        ele.send_keys(home_ph_no)
        time.sleep(web_driver.one_second)

    def enter_work_ph_no(self, work_ph_no):
        """
        fills email field
        :param work_ph_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().work_phone_number_by_xpath())
        ele.send_keys(work_ph_no)
        time.sleep(web_driver.one_second)

    def enter_fax_ph_no(self, fax_ph_no):
        """
        fills email field
        :param fax_ph_no:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().fax_phone_number_by_xpath())
        ele.send_keys(fax_ph_no)
        time.sleep(web_driver.one_second)

    def enter_phone_type(self, phone_type):
        """
        fills email field
        :param phone_type:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().phone_type_by_xpath())
        ele.send_keys(phone_type)
        time.sleep(web_driver.one_second)

    def enter_address2(self, address2):
        """
        fills email field
        :param address2:
        """
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().address2_by_xpath())
        ele.send_keys(address2)
        time.sleep(web_driver.one_second)

    def select_phone_provider(self, phone_provider):
        ph_prov_bx = self.d.find_element(By.XPATH,
                                         Read_Notification_Groups_Components().phone_provider_drop_dwn_by_xpath())
        select = Select(ph_prov_bx)
        select.select_by_visible_text(phone_provider)
        time.sleep(web_driver.one_second)

    def validate_required_time_zone_is_selected(self, required_option):
        """
        checks if the required time zone is selected
        :param required_option:
        """
        time_zone_ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().time_zone_by_xpath())
        select = Select(time_zone_ele)
        selected_option = select.first_selected_option
        selected_value = selected_option.get_attribute("value")
        time.sleep(web_driver.one_second)
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
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().error_message_by_xpath())
        msg_validation = ele.text
        ac_result.append(msg_validation == Read_Notification_Groups_Components().error_msg_validation_text())
        ac_result.append(ele.is_displayed())
        time.sleep(web_driver.one_second)
        if ex_result == ac_result:
            return True
        else:
            return False

    def validate_successful_message(self):
        """
        checks if the error message "Success! A user has been created." is displayed.
        """
        ex_result = [True, True]
        ac_result = []
        ele = self.explicit_wait(10, "XPATH", Read_Notification_Groups_Components().success_message_by_xpath(), self.d)
        msg_validation = ele.text
        self.logger.info(f"actual success msg: {msg_validation}")
        ac_result.append(msg_validation == Read_Notification_Groups_Components().success_message_validation_text())
        self.logger.info(f"expected msg: {Read_Notification_Groups_Components().success_message_validation_text()}")
        ac_result.append(ele.is_displayed())
        time.sleep(web_driver.one_second)
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
        ele = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().success_message_by_xpath())
        msg_validation = ele.text
        ac_result.append(msg_validation == Read_Notification_Groups_Components().success_msg_validation_text())
        ac_result.append(ele.is_displayed())
        search_box = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().search_box_by_xpath())
        search_box.send_keys(user_name)
        time.sleep(web_driver.one_second)
        user = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().users_list_board_username_by_xpath())
        ac_result.append(user_name == user.text)

        if ex_result == ac_result:
            return True
        else:
            return False

    def time_zone_by_xpath(self):
        try:
            time_zone_by_xpath = self.config.get("LOCATORS", "time_zone_by_xpath")
            time.sleep(web_driver.one_second)
            return time_zone_by_xpath
        except Exception as ex:
            print(ex)
