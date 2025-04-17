import configparser
import time
from pathlib import Path

import numpy as np
import pandas as pd
from selenium.webdriver.support.select import Select

from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from selenium.webdriver.common.by import By
from All_Config_Packages._17_Notifier_Module_Config_Files.Notifier_Read_INI import Notifier_Read_ini
from All_Config_Packages._18_Reporting_Module_Config_Files.Reporting_Read_INI import Reporting_read_ini
from All_Config_Packages._0_login_logout_config_file.login_logout_read_ini import LoginLogout_Read_ini
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import Portal_Menu_Module_read_ini
from All_Config_Packages._6_Notification_Groups_Module_Config_Files.Notification_Groups_Read_INI import Read_Notification_Groups_Components
from Base_Package.Login_Logout_Ops import login, logout
from All_Other_Utility_Packages._3_User_Roles_Module.Read_Excel import Read_excel


class Notifier_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []
    
    def __init__(self):
        self.groups = self.region_name = self.camera1_name = self.camera2_name = self.refresh_rate = \
            self.events_displayed = self.photo_size = self.sound_option = self.group_selected = None
        
        self.notifier_test_data = \
            f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\17_Notifier_Module\\Data_From_Excel\\Notifier_test_data.xlsx"
        self.file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\0_Login_Logout_Data\\Data_From_INI\\login_logout.ini"
        self.config = configparser.RawConfigParser()
        self.config.read(self.file_path)

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

    def load_notifier_module(self):
        try:
            time.sleep(web_driver.one_second)
            notifier_module = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Notifier_menu_by_xpath())
            if notifier_module.is_displayed():
                notifier_module.click()
            else:
                pass
            time.sleep(web_driver.two_second)
        except Exception as ex:
            self.logger.error(ex)

    def close_notifier_module(self):
        try:
            cloud_menu_button = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath())
            cloud_menu_button.click()
            time.sleep(web_driver.one_second)
            close_notifier_btn_on_dashboard = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_close_notifier_button_on_dashboard_menu_by_xpath())
            if close_notifier_btn_on_dashboard.is_displayed():
                close_notifier_btn_on_dashboard.click()
                time.sleep(web_driver.one_second)
            else:
                pass
        except Exception as ex:
            self.logger.error(ex)
            return False

    def get_region_and_group_data(self):
        try:
            df_groups = pd.read_excel(self.notifier_test_data, sheet_name='group_data', names=['Group_Names'])
            df_regions = pd.read_excel(self.notifier_test_data, sheet_name='region_data',
                                       names=['Region_Name', 'Camera1_Name', 'Camera2_Name'])
            df_notifier_setting = pd.read_excel(self.notifier_test_data, sheet_name='notifier_setting', names=['Refresh_Rate', 'Events_Displayed', 'Photo_Size', 'Sound_Option'])
            self.groups = [x for x in df_groups['Group_Names']]
            self.region_name = [x for x in df_regions['Region_Name']]
            self.camera1_name = [y for y in df_regions['Camera1_Name']]
            self.camera2_name = [z for z in df_regions['Camera2_Name']]
            self.refresh_rate = [x for x in df_notifier_setting['Refresh_Rate']]
            self.events_displayed = [y for y in df_notifier_setting['Events_Displayed']]
            self.photo_size = [z for z in df_notifier_setting['Photo_Size']]
            self.sound_option = [xx for xx in df_notifier_setting['Sound_Option']]
            # print(f"groups: {self.groups}" f"length: {len(self.groups)}")
            # print(f"region names: {self.region_name}" f"length: {len(self.region_name)}")
            # print(f"camera1 names: {self.camera1_name}" f"length: {len(self.camera1_name)}")
            # print(f"camera2 names: {self.camera2_name}" f"length: {len(self.camera2_name)}")
            # print(f"regions: {df_regions}")
            # print(f"groups: {df_groups}")

        except Exception as ex:
            self.logger.error(ex)

    def Verify_Notifier_is_visible_and_clickable_in_dashboard_menu_items_click_on_Notifier_and_verify_it_is_navigating_to_notifier_panel(self):
        try:
            self.logger.info("*********** TC_Notifier_001 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            dashboard_items = self.d.find_elements(By.XPATH, Reporting_read_ini().get_dashboard_menu_items_by_xpath())
            for items in dashboard_items:
                if items.text == Notifier_Read_ini().get_notifier():
                    self.status.append(True)
                    self.logger.info("Notifier is visible on dashboard..")
                    break
            else:
                self.logger.error("Notifier is not visible.!!!")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_module_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on Notifier module...")
            actual_panel_heading = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                       get_notifier_panel_heading_by_xpath()).text
            time.sleep(web_driver.one_second)
            if actual_panel_heading == Notifier_Read_ini().get_notifier():
                self.logger.info("Notifier panel is visible..")
                self.status.append(True)
            else:
                self.logger.error("Notifier panel is not visible.!!!")
                self.status.append(False)
            time.sleep(web_driver.one_second)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_001.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_001.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_001_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_001_exception.png")
            self.logger.error(f"TC_Notifier_001 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Click_on_Notifier_and_verify_title_is_visible_CLOUD_MENU_button_is_visible_and_clickable_user_name_is_visible_Logout_button_is_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Notifier_003 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.load_notifier_module()
            actual_panel_heading = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                       get_notifier_panel_heading_by_xpath()).text
            if actual_panel_heading == Notifier_Read_ini().get_notifier():
                self.logger.info("Notifier title is visible..")
                self.status.append(True)
            else:
                self.logger.error("Notifier title is not visible.!!!")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            cloud_menu_button = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath())
            if cloud_menu_button.is_displayed():
                self.logger.info("CLOUD MENU button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if cloud_menu_button.is_enabled():
                self.logger.info("CLOUD MENU button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_username = self.d.find_element(By.XPATH, Notifier_Read_ini().get_user_name_by_xpath()).text
            self.logger.info(f"actual user name: {actual_username}")
            expected_username = LoginLogout_Read_ini().get_username()
            self.logger.info(f"expected user name: {expected_username}")
            if actual_username == expected_username:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            logout_button = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_logout_button_on_portal_by_xpath())
            if logout_button.is_displayed():
                self.logger.info("Logout button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if logout_button.is_enabled():
                self.logger.info("Logout button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_003.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_003.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_003_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_003_exception.png")
            self.logger.error(f"TC_Notifier_003 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Close_Notifier_button_in_dashboard_menu_is_visible_and_clickable_bullhorn_icon_and_text_on_button_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Notifier_004 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.load_notifier_module()

            cloud_menu_button = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath())
            cloud_menu_button.click()
            time.sleep(web_driver.one_second)
            close_notifier_btn_on_dashboard = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_close_notifier_button_on_dashboard_menu_by_xpath())
            if close_notifier_btn_on_dashboard.is_displayed():
                self.logger.info("'Close Notifier' button is visible on dashboard...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if close_notifier_btn_on_dashboard.is_enabled():
                self.logger.info("'Close Notifier' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            bullhorn_icon = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                get_bullhorn_icon_on_close_notifier_btn_by_xpath())
            if bullhorn_icon.is_displayed():
                self.logger.info("Bullhorn icon on 'Close Notifier' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                              get_text_on_close_notifier_btn_on_dashboard_by_xpath()).text
            self.logger.info(f"actual text on Close Notifier button: {actual_text}")
            expected_text = Notifier_Read_ini().get_expected_text_on_close_notifier_button_on_dashboard()
            self.logger.info(f"expected text on close notifier button on dashboard: {expected_text}")
            time.sleep(web_driver.one_second)
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_notifier_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_004.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_004.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_004_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_004_exception.png")
            self.logger.error(f"TC_Notifier_004 got exception as: {ex}")

    def Click_on_Close_Notifier_button_on_dashboard_and_verify_notifier_panel_is_closed(self):
        try:
            self.logger.info("*********** TC_Notifier_005 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.load_notifier_module()
            close_notifier_button_on_notifier_panel = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_close_notifier_button_on_notifier_panel_by_xpath())
            if close_notifier_button_on_notifier_panel.is_displayed():
                self.logger.info("Notifier panel is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            cloud_menu_button = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath())
            cloud_menu_button.click()
            time.sleep(web_driver.one_second)
            close_notifier_btn_on_dashboard = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_close_notifier_button_on_dashboard_menu_by_xpath())
            close_notifier_btn_on_dashboard.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on 'Close Notifier' button...")
            if close_notifier_button_on_notifier_panel.is_displayed():
                self.status.append(False)
            else:
                self.logger.info("Notifier panel is closed..")
                self.status.append(True)
            time.sleep(web_driver.one_second)
            self.close_notifier_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_005.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_005.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_005_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_005_exception.png")
            self.logger.error(f"TC_Notifier_005 got exception as: {ex}")

    def Verify_Enrollment_Group_Selection_button_is_visible_and_clickable_text_and_group_icon_on_button_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Notifier_006 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.load_notifier_module()
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            if enrollment_group_selection_button.is_displayed():
                self.logger.info("Enrollment Group Selection button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if enrollment_group_selection_button.is_enabled():
                self.logger.info("Enrollment Group Selection button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            group_icon = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                             get_group_icon_on_enrollment_group_selection_button_by_xpath())
            if group_icon.is_displayed():
                self.logger.info("Group icon on Enrollment Group Selection button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                              get_text_on_enrollment_group_selection_button_by_xpath()).text
            self.logger.info(f"actual text on button: {actual_text}")
            expected_text = Notifier_Read_ini().get_expected_text_on_enrollment_group_selection_button()
            self.logger.info(f"expected text on button: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_006.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_006.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_006_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_006_exception.png")
            self.logger.error(f"TC_Notifier_006 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Org_Hierarchy_Selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Notifier_007 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.load_notifier_module()
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            if org_hierarchy_selection_button.is_displayed():
                self.logger.info("Org/Hierarchy Selection button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if org_hierarchy_selection_button.is_enabled():
                self.logger.info("Org/Hierarchy Selection button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            dot_circle_icon = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                  get_dot_circle_icon_on_org_hierarchy_selection_button_by_xpath())
            if dot_circle_icon.is_displayed():
                self.logger.info("Dot circle icon on Org/Hierarchy Selection button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                              get_text_on_org_hierarchy_selection_button_by_xpath()).text
            self.logger.info(f"actual text on Org/Hierarchy Selection button: {actual_text}")
            expected_text = Notifier_Read_ini().get_expected_text_on_org_hierarchy_selection_button()
            self.logger.info(f"expected text on Org/Hierarchy Selection button: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_007.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_007.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_007_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_007_exception.png")
            self.logger.error(f"TC_Notifier_007 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_Setting_button_is_visible_and_clickable_text_and_setting_icon_on_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Notifier_008 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.load_notifier_module()
            notifier_setting_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_notifier_setting_button_by_xpath())
            if notifier_setting_button.is_displayed():
                self.logger.info("Notifier Setting button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if notifier_setting_button.is_enabled():
                self.logger.info("Notifier Setting button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            gear_icon = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                            get_gear_icon_on_notifier_setting_button_by_xpath())
            if gear_icon.is_displayed():
                self.logger.info("Gear icon on Notifier Setting button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                              get_text_on_notifier_setting_button_by_xpath()).text
            self.logger.info(f"actual text on Notifier Setting button: {actual_text}")
            expected_text = Notifier_Read_ini().get_expected_text_on_notifier_setting_button()
            self.logger.info(f"expected text on Notifier Setting button: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_008.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_008.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_008_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_008_exception.png")
            self.logger.error(f"TC_Notifier_008 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Close_Notifier_symbol_on_Notifier_panel_is_visible_and_clickable_close_symbol_is_visible_click_on_close_notifier_and_verify_Notifier_panel_is_closing(
            self):
        try:
            self.logger.info("*********** TC_Notifier_009 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.load_notifier_module()
            close_notifier_button_on_notifier_panel = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_close_notifier_button_on_notifier_panel_by_xpath())
            if close_notifier_button_on_notifier_panel.is_displayed():
                self.logger.info("Close notifier button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if close_notifier_button_on_notifier_panel.is_enabled():
                self.logger.info("Close notifier button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)
            close_symbol_on_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                         get_close_symbol_on_close_notifier_button_by_xpath())
            if close_symbol_on_button.is_displayed():
                self.logger.info("Close symbol on close notifier button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            close_notifier_button_on_notifier_panel.click()
            time.sleep(web_driver.one_second)
            notifier_module = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_module_by_xpath())
            if notifier_module.is_displayed():
                self.logger.info("Notifier panel is closed successfully...")
                self.status.append(True)
            else:
                self.logger.info("Notifier panel is not closed...")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_009.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_009.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_009_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_009_exception.png")
            self.logger.error(f"TC_Notifier_009 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Click_on_Enrollment_Group_Selection_button_and_verify_select_a_group_panel_is_visible_heading_on_panel_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Notifier_010 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.load_notifier_module()
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_enrollment_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            dialog_box = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                             get_select_group_dialog_box_in_enrollment_group_selection_by_xpath())
            if dialog_box.is_displayed():
                self.logger.info("'Select a group' dialog box is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_heading = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_heading_on_select_a_group_dialog_box_by_xpath()).text
            self.logger.info(f"actual heading on Enrollment Group Selection dialog box: {actual_heading}")
            expected_heading = Notifier_Read_ini().get_expected_heading_on_select_a_group_dialog_box()
            self.logger.info(f"expected heading on Enrollment Group Selection dialog box: {expected_heading}")
            if actual_heading == expected_heading:
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_010.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_010.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_010_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_010_exception.png")
            self.logger.error(f"TC_Notifier_010 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def In_Group_Selection_dialog_box_verify_filter_group_list_below_textbox_is_visible_and_clickable_group_list_below_textbox_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Notifier_011 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.load_notifier_module()
            close_button_on_group_selection_panel = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().get_close_button_on_group_selection_panel_by_xpath())
            if close_button_on_group_selection_panel.is_displayed():
                pass
            else:
                self.d.find_element(By.XPATH, Notifier_Read_ini().get_enrollment_group_selection_button_by_xpath()). \
                    click()
                time.sleep(web_driver.one_second)
            filter_group_textbox = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                       get_filter_group_list_textbox_by_xpath())
            time.sleep(web_driver.one_second)
            if filter_group_textbox.is_displayed():
                self.logger.info("'filter group list below..' textbox is visible")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if filter_group_textbox.is_enabled():
                self.logger.info("'filter group list below..' textbox is clickable")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_label = filter_group_textbox.get_attribute('placeholder')
            time.sleep(web_driver.one_second)
            self.logger.info(f"actual label on 'filter group list' textbox: {actual_label}")
            expected_label = Notifier_Read_ini().get_expected_label_on_filter_group_list_textbox()
            self.logger.info(f"expected label on 'filter group list' textbox: {expected_label}")
            if actual_label == expected_label:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            group_items = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                               get_group_items_below_filter_group_list_textbox_by_xpath())
            self.logger.info(f"Number of groups below 'filter group list below' textbox: {len(group_items)}")
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_enrollment_groups_module_on_dashboard_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            enrollment_groups = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                     get_group_list_from_enrollment_groups_module_by_xpath())
            self.logger.info(f"Number of groups in Enrollment Groups module: {len(enrollment_groups)}")
            if len(group_items) == len(enrollment_groups):
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            close_panel_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                     get_enrollment_groups_close_panel_button_by_xpath())
            close_panel_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_011.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_011.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_011_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_011_exception.png")
            self.logger.error(f"TC_Notifier_011 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_group_list_radio_buttons_are_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Notifier_012 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.load_notifier_module()
            close_button_on_group_selection_panel = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().get_close_button_on_group_selection_panel_by_xpath())
            if close_button_on_group_selection_panel.is_displayed():
                pass
            else:
                self.d.find_element(By.XPATH, Notifier_Read_ini().get_enrollment_group_selection_button_by_xpath()). \
                    click()
                time.sleep(web_driver.one_second)

            radio_buttons = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                 get_radio_buttons_in_select_a_group_panel_by_xpath())
            for buttons in radio_buttons:
                if buttons.is_displayed():
                    buttons.click()
                    time.sleep(web_driver.one_second)
                    self.status.append(True)
                else:
                    self.status.append(False)
            self.logger.info("Radio buttons are visible...")
            self.logger.info("Radio buttons are clickable...")
            clear_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                               get_clear_button_on_select_a_group_panel_by_xpath())
            clear_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_012.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_012.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_012_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_012_exception.png")
            self.logger.error(f"TC_Notifier_012 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Clear_button_Close_button_and_Save_button_are_visible_and_clickable_texts_on_buttons_are_visible(self):
        try:
            self.logger.info("*********** TC_Notifier_013 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            close_button_on_group_selection_panel = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().get_close_button_on_group_selection_panel_by_xpath())
            if close_button_on_group_selection_panel.is_displayed():
                pass
            else:
                self.d.find_element(By.XPATH, Notifier_Read_ini().get_enrollment_group_selection_button_by_xpath()). \
                    click()
                time.sleep(web_driver.one_second)
            clear_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                               get_clear_button_on_select_a_group_panel_by_xpath())
            if clear_button.is_displayed():
                self.logger.info("'Clear' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if clear_button.is_enabled():
                self.logger.info("'Clear' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_clear_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                              get_clear_button_on_select_a_group_panel_by_xpath()).text
            self.logger.info(f"actual text on 'Clear' button: {actual_text_on_clear_button}")
            expected_text_on_clear_button = Notifier_Read_ini().get_expected_text_on_clear_button()
            self.logger.info(f"expected test on 'Clear' button: {expected_text_on_clear_button}")
            time.sleep(web_driver.one_second)
            if actual_text_on_clear_button == expected_text_on_clear_button:
                self.status.append(True)
            else:
                self.status.append(False)
            close_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                               get_close_button_on_select_a_group_panel_by_xpath())
            if close_button.is_displayed():
                self.logger.info("'Close' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if close_button.is_enabled():
                self.logger.info("'Close' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_close_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                              get_close_button_on_select_a_group_panel_by_xpath()).text
            self.logger.info(f"actual text on 'Close' button: {actual_text_on_close_button}")
            expected_text_on_close_button = Notifier_Read_ini().get_expected_text_on_close_button()
            self.logger.info(f"expected test on 'Close' button: {expected_text_on_close_button}")
            if actual_text_on_close_button == expected_text_on_close_button:
                self.status.append(True)
            else:
                self.status.append(False)
            save_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                              get_save_button_on_select_a_group_panel_by_xpath())
            if save_button.is_displayed():
                self.logger.info("'Save' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if save_button.is_enabled():
                self.logger.info("'Save' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_save_button = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_save_button_on_select_a_group_panel_by_xpath()).text
            self.logger.info(f"actual text on 'Save' button: {actual_text_on_save_button}")
            expected_text_on_save_button = Notifier_Read_ini().get_expected_text_on_save_button()
            self.logger.info(f"expected test on 'Save' button: {expected_text_on_save_button}")
            if actual_text_on_save_button == expected_text_on_save_button:
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_013.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_013.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_013_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_013_exception.png")
            self.logger.error(f"TC_Notifier_013 got exception as: {ex}")
        finally:
            self.close_notifier_module()


    def Select_one_group_and_click_on_Save_button_and_verify_that_group_name_is_visible_on_Notifier_panel_verify_Selected_group_s_text_is_visible(self):
        try:
            self.logger.info("*********** TC_Notifier_014 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            close_button_on_group_selection_panel = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().get_close_button_on_group_selection_panel_by_xpath())
            if close_button_on_group_selection_panel.is_displayed():
                pass
            else:
                self.d.find_element(By.XPATH, Notifier_Read_ini().get_enrollment_group_selection_button_by_xpath()). \
                    click()
                time.sleep(web_driver.one_second)
            radio_buttons = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                 get_radio_buttons_in_select_a_group_panel_by_xpath())
            radio_buttons[0].click()
            time.sleep(web_driver.one_second)
            self.logger.info("Group selected....")
            group_names = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                               get_group_names_in_select_a_group_panel_by_xpath())
            expected_selected_group_name = group_names[0].text.lower()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH,
                                Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).click()
            self.logger.info("Clicked on 'Save' button...")
            actual_selected_group_name = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                             get_name_of_group_selected_by_xpath()).text
            time.sleep(web_driver.one_second)
            self.logger.info(f"expected selected group: {expected_selected_group_name}")
            self.logger.info(f"actual selected group: {actual_selected_group_name}")

            if actual_selected_group_name == expected_selected_group_name:
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text = self.d.find_element(By.XPATH, Notifier_Read_ini().get_text_selected_groups_by_xpath()).text
            self.logger.info(f"actual text: {actual_text}")
            expected_text = Notifier_Read_ini().get_expected_text_selected_groups().upper()
            self.logger.info(f"expected text: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_close_group_selected_visible_on_notifier_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            # self.close_notifier_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_014.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_014.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_014_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_014_exception.png")
            self.logger.error(f"TC_Notifier_014 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Select_one_group_and_click_on_Clear_button_and_verify_the_selected_group_is_unselected(self):
        try:
            self.logger.info("*********** TC_Notifier_015 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            enrollment_group_selection_button = web_driver.explicit_wait(self, 10, "XPATH",
                                                                         Notifier_Read_ini().get_enrollment_group_selection_button_by_xpath(),
                                                                         self.d)
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            # close_button_on_group_selection_panel = self.d.find_element(By.XPATH, Notifier_Read_ini().get_close_button_on_group_selection_panel_by_xpath())
            close_button_on_group_selection_panel = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_close_button_on_group_selection_panel_by_xpath(), self.d)
            # enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_enrollment_group_selection_button_by_xpath())
            if close_button_on_group_selection_panel.is_displayed():
                pass
            else:
                enrollment_group_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_enrollment_group_selection_button_by_xpath(), self.d)
                enrollment_group_selection_button.click()
                time.sleep(web_driver.one_second)
            radio_buttons = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                 get_radio_buttons_in_select_a_group_panel_by_xpath())
            radio_buttons[0].click()
            time.sleep(web_driver.one_second)
            if radio_buttons[0].is_selected():
                self.logger.info("Group selected....")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on 'Clear' button...")
            if radio_buttons[0].is_selected():
                self.status.append(False)
            else:
                self.logger.info("No group selected....")
                self.status.append(True)
            close_button_on_group_selection_panel.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_015.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_015.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_015_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_015_exception.png")
            self.logger.error(f"TC_Notifier_015 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Click_on_Close_button_and_verify_group_selection_panel_is_closing(self):
        try:
            self.logger.info("*********** TC_Notifier_016 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            enrollment_group_selection_button = web_driver.explicit_wait(self, 10, "XPATH",
                                                                         Notifier_Read_ini().get_enrollment_group_selection_button_by_xpath(),
                                                                         self.d)
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            # close_button_on_group_selection_panel = self.d.find_element(By.XPATH, Notifier_Read_ini().get_close_button_on_group_selection_panel_by_xpath())
            close_button_on_group_selection_panel = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_close_button_on_group_selection_panel_by_xpath(), self.d)
            # enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_enrollment_group_selection_button_by_xpath())
            if close_button_on_group_selection_panel.is_displayed():
                pass
            else:
                enrollment_group_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_enrollment_group_selection_button_by_xpath(), self.d)
                enrollment_group_selection_button.click()
                time.sleep(web_driver.one_second)
            # dialog_box = self.d.find_element(By.XPATH, Notifier_Read_ini().get_select_group_dialog_box_in_enrollment_group_selection_by_xpath())
            dialog_box = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_select_group_dialog_box_in_enrollment_group_selection_by_xpath(), self.d)
            if dialog_box.is_displayed():
                self.logger.info("'Select a group' panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            close_button_on_group_selection_panel.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on 'Close' button on panel...")
            if dialog_box.is_displayed():
                self.status.append(False)
                self.logger.info("'Select a group' panel is still visible.")
            else:
                self.logger.info("'Select a group' panel is closed...")
                self.status.append(True)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_016.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_016.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_016_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_016_exception.png")
            self.logger.error(f"TC_Notifier_016 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Click_on_Org_Hierarchy_Selection_button_and_verify_new_panel_is_visible_verify_heading_on_Org_Hierarchy_panel(
            self):
        try:
            self.logger.info("*********** TC_Notifier_017 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            time.sleep(web_driver.one_second)
            close_button_on_group_selection_panel = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().get_close_button_on_group_selection_panel_by_xpath())
            if close_button_on_group_selection_panel.is_displayed():
                close_button_on_group_selection_panel.click()
                time.sleep(web_driver.one_second)
            else:
                pass
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            region_selection_panel = self.explicit_wait(10, "XPATH", Notifier_Read_ini().get_org_region_panel_by_xpath(), self.d)
            if region_selection_panel.is_displayed():
                self.logger.info("Org/Hierarchy selection panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_heading = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_heading_on_region_selection_panel_by_xpath()).text
            time.sleep(web_driver.one_second)
            self.logger.info(f"actual heading on Org/Hierarchy selection panel: {actual_heading}")
            expected_heading = Notifier_Read_ini().get_expected_heading_on_region_selection_panel()
            self.logger.info(f"expected heading on Org/Hierarchy selection panel: {expected_heading}")
            if actual_heading == expected_heading:
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_017.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_017.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_017_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_017_exception.png")
            self.logger.error(f"TC_Notifier_017 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Collapse_all_Expand_all_Select_all_Unselect_all_buttons_are_visible_and_clickable_text_on_buttons_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Notifier_018 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            # collapse_all_button = self.d.find_element(By.XPATH, Notifier_Read_ini(). get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath(), self.d)
            if collapse_all_button.is_displayed():
                self.logger.info("'Collapse all' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if collapse_all_button.is_enabled():
                self.logger.info("'Collapse all' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_collapse_all_button = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_collapse_all_button_on_region_selection_panel_by_xpath()).text
            self.logger.info(f"actual text: {actual_text_on_collapse_all_button}")
            expected_text_on_collapse_all_button = Notifier_Read_ini().get_expected_text_on_collapse_all_button()
            self.logger.info(f"expected text: {expected_text_on_collapse_all_button}")
            if actual_text_on_collapse_all_button == expected_text_on_collapse_all_button:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)

            expand_all_button = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_expand_all_button_on_region_selection_panel_by_xpath())
            if expand_all_button.is_displayed():
                self.logger.info("'Expand all' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if expand_all_button.is_enabled():
                self.logger.info("'Expand all' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_expand_all_button = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_expand_all_button_on_region_selection_panel_by_xpath()).text
            self.logger.info(f"actual text: {actual_text_on_expand_all_button}")
            expected_text_on_expand_all_button = Notifier_Read_ini().get_expected_text_on_expand_all_button()
            self.logger.info(f"expected text: {expected_text_on_expand_all_button}")
            if actual_text_on_expand_all_button == expected_text_on_expand_all_button:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)

            select_all_button = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_select_all_button_on_region_selection_panel_by_xpath())
            if select_all_button.is_displayed():
                self.logger.info("'Select all' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if select_all_button.is_enabled():
                self.logger.info("'Select all' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_select_all_button = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_select_all_button_on_region_selection_panel_by_xpath()).text
            self.logger.info(f"actual text: {actual_text_on_select_all_button}")
            expected_text_on_select_all_button = Notifier_Read_ini().get_expected_text_on_select_all_button()
            self.logger.info(f"expected text: {expected_text_on_select_all_button}")
            if actual_text_on_select_all_button == expected_text_on_select_all_button:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)

            unselect_all_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_unselect_all_button_on_region_selection_panel_by_xpath())
            if unselect_all_button.is_displayed():
                self.logger.info("'Unselect all' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if unselect_all_button.is_enabled():
                self.logger.info("'Unselect all' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text_on_unselect_all_button = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_unselect_all_button_on_region_selection_panel_by_xpath()).text
            self.logger.info(f"actual text: {actual_text_on_unselect_all_button}")
            expected_text_on_unselect_all_button = Notifier_Read_ini().get_expected_text_on_unselect_all_button()
            self.logger.info(f"expected text: {expected_text_on_unselect_all_button}")
            if actual_text_on_unselect_all_button == expected_text_on_unselect_all_button:
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_018.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_018.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_018_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_018_exception.png")
            self.logger.error(f"TC_Notifier_018 got exception as: {ex}")
        finally:
            self.close_notifier_module()


    def Click_on_Collapse_all_button_and_verify_all_regions_are_collapsing(self):
        try:
            self.logger.info("*********** TC_Notifier_019 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on Org/Hierarchy Selection button...")
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)
            region_list = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                               get_region_list_in_org_hierarchy_selection_by_xpath())

            time.sleep(web_driver.one_second)
            if region_list[0].is_displayed():
                self.logger.info("Region names are expanded.....")
                self.status.append(True)
            else:
                self.status.append(False)

            # collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath(), self.d)
            collapse_all_btn.click()

            self.logger.info("Clicked on 'Collapse all' button....")
            time.sleep(web_driver.two_second)
            if region_list[0].is_displayed():
                self.status.append(False)
            else:
                self.logger.info("Region names are collapsed...")
                self.status.append(True)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_019.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_019.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_019_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_019_exception.png")
            self.logger.error(f"TC_Notifier_019 got exception as: {ex}")
        finally:
            self.close_notifier_module()


    def Click_on_Expand_all_and_verify_all_regions_are_expanding(self):
        try:
            self.logger.info("*********** TC_Notifier_020 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on Org/Hierarchy Selection button...")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                   get_collapse_all_button_on_region_selection_panel_by_xpath())
            region_list = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                               get_region_list_in_org_hierarchy_selection_by_xpath())

            collapse_all_btn.click()
            time.sleep(web_driver.two_second)
            if region_list[0].is_displayed():
                self.status.append(False)
            else:
                self.logger.info("Region names are collapsed...")
                self.status.append(True)
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Expand all' button...")
            if region_list[0].is_displayed():
                self.logger.info("Region names are expanded...")
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_020.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_020.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_020_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_020_exception.png")
            self.logger.error(f"TC_Notifier_020 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Click_on_Select_all_and_verify_all_regions_are_selecting(self):
        try:
            self.logger.info("*********** TC_Notifier_021 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on Org/Hierarchy Selection button...")
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)
            unselect_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                   get_unselect_all_button_on_region_selection_panel_by_xpath())
            unselect_all_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on 'Unselect all' button...")
            checkbox_besides_region = \
                self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                     get_checkbox_besides_region_names_in_org_hierarchy_selection_by_xpath())
            print("length of checkbox: ", len(checkbox_besides_region))
            if len(checkbox_besides_region) > 0:
                for items in checkbox_besides_region:
                    if 'check' in items.get_attribute('class'):
                        self.status.append(False)
                    else:
                        self.status.append(True)
                self.logger.info("All regions are unselected...")

            select_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_select_all_button_on_region_selection_panel_by_xpath())
            select_all_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Click on 'Select all' button...")

            if len(checkbox_besides_region) > 0:
                for items in checkbox_besides_region:
                    if 'check' in items.get_attribute('class'):
                        self.status.append(True)
                    else:
                        self.status.append(True)
                self.logger.info("All regions are selected...")

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_021.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_021.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_021_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_021_exception.png")
            self.logger.error(f"TC_Notifier_021 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Click_on_Unselect_all_and_verify_all_regions_are_unselecting(self):
        try:
            self.logger.info("*********** TC_Notifier_022 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on Org/Hierarchy Selection button...")
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)
            select_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_select_all_button_on_region_selection_panel_by_xpath())
            select_all_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Click on 'Select all' button...")
            checkbox_besides_region = \
                self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                     get_checkbox_besides_region_names_in_org_hierarchy_selection_by_xpath())
            if len(checkbox_besides_region) > 0:
                for items in checkbox_besides_region:
                    if 'check' in items.get_attribute('class'):
                        self.status.append(True)
                    else:
                        self.status.append(True)
                self.logger.info("All regions are selected...")

            unselect_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                   get_unselect_all_button_on_region_selection_panel_by_xpath())
            unselect_all_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on 'Unselect all' button...")
            checkbox_besides_region = \
                self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                     get_checkbox_besides_region_names_in_org_hierarchy_selection_by_xpath())
            if len(checkbox_besides_region) > 0:
                for items in checkbox_besides_region:
                    if 'check' in items.get_attribute('class'):
                        self.status.append(False)
                    else:
                        self.status.append(True)
                self.logger.info("All regions are unselected...")

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_022.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_022.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_022_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_022_exception.png")
            self.logger.error(f"TC_Notifier_022 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Search_textbox_is_visible_and_clickable_label_on_text_is_visible(self):
        try:
            self.logger.info("*********** TC_Notifier_023 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on Org/Hierarchy Selection button...")
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)
            search_textbox = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_search_textbox_on_org_hierarchy_panel_by_xpath())
            if search_textbox.is_displayed():
                self.logger.info("'Search' textbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if search_textbox.is_enabled():
                self.logger.info("'Search' textbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_label = search_textbox.get_attribute('placeholder')
            self.logger.info(f"actual label: {actual_label}")
            expected_label = Notifier_Read_ini().get_expected_label_on_search_textbox()
            self.logger.info(f"expected label: {expected_label}")
            if actual_label == expected_label:
                self.logger.info("Label on 'Search' textbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_023.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_023.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_023_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_023_exception.png")
            self.logger.error(f"TC_Notifier_023 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Enter_one_region_name_in_Search_textbox_and_verify_only_given_region_is_visible(self):
        try:
            self.logger.info("*********** TC_Notifier_024 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            time.sleep(web_driver.one_second)
            self.get_region_and_group_data()
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 20, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            before = []
            region_list_before = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                      get_region_list_in_org_hierarchy_selection_by_xpath())
            for items in region_list_before:
                if items.is_displayed():
                    before.append(True)
            search_textbox = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_search_textbox_on_org_hierarchy_panel_by_xpath())
            region = self.region_name[0]
            region1 = region.split('-')
            search_textbox.send_keys(region1[0])
            time.sleep(web_driver.one_second)
            self.logger.info(f"Entered region name as: {region1[0]}")
            region_list_after = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                     get_region_list_in_org_hierarchy_selection_by_xpath())
            after = []
            time.sleep(web_driver.one_second)
            for items in region_list_after:
                if items.is_displayed():
                    after.append(True)
            if before == after:
                self.logger.info("Entered name is not in region list....")
            else:
                self.status.append(True)

            time.sleep(web_driver.one_second)
            search_textbox.clear()
            self.close_notifier_module()
            self.logger.info(f"status: {self.status}")

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_024.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_024.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_024_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_024_exception.png")
            self.logger.error(f"TC_Notifier_024 got exception as: {ex}")

    def Verify_Close_button_on_Org_Hierarchy_is_visible_and_clickable_text_on_Close_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Notifier_025 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 20, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.two_second)
            close_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                               get_close_button_on_org_hierarchy_panel_by_xpath())
            if close_button.is_enabled():
                self.logger.info("'Close' button on Org/Hierarchy panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if close_button.is_enabled():
                self.logger.info("'Close' button on Org/Hierarchy panel is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text = close_button.text
            self.logger.info(f"actual text on 'Close' button: {actual_text}")
            expected_text = Notifier_Read_ini().get_expected_text_on_close_button()
            self.logger.info(f"expected text on 'Close' button: {expected_text}")
            # if actual_text == expected_text:
            #     self.status.append(True)
            # else:
            #     self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_025.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_025.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_025_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_025_exception.png")
            self.logger.error(f"TC_Notifier_025 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def click_on_Close_button_and_verify_Org_Hierarchy_Selection_panel_is_closing(self):
        try:
            self.logger.info("*********** TC_Notifier_026 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Org/Hierarchy selection panel opened...")
            time.sleep(web_driver.one_second)
            close_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                               get_close_button_on_org_hierarchy_panel_by_xpath())
            # while not close_button.is_displayed():
            #     collapse_all_btn = self.d.find_element(By.XPATH,
            #                                            Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            #     collapse_all_btn.click()
            #     time.sleep(web_driver.one_second)

            self.d.execute_script("arguments[0].click();", close_button)
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on 'Close' button...")
            heading = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_panel_heading_by_xpath())
            if heading.is_displayed():
                self.logger.info("Org/Hierarchy selection panel is closed...")
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_026.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_026.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_026_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_026_exception.png")
            self.logger.error(f"TC_Notifier_026 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Save_button_on_Org_Hierarchy_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Notifier_027 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            while not save_button.is_displayed():
                collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
                collapse_all_btn.click()
                time.sleep(web_driver.one_second)
            if save_button.is_displayed():
                self.logger.info("'Save' button on Org/Hierarchy selection panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if save_button.is_enabled():
                self.logger.info("'Save' button on Org/Hierarchy selection panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text = save_button.text
            self.logger.info(f"actual text on 'Save' button: {actual_text}")
            expected_text = Notifier_Read_ini().get_expected_text_on_save_button()
            self.logger.info(f"expected text on 'Save' button: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            time.sleep(web_driver.two_second)
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)
            self.close_notifier_module()
            self.logger.info(f"status: {self.status}")

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_027.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_027.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_027_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_027_exception.png")
            self.logger.error(f"TC_Notifier_027 got exception as: {ex}")

    def On_Org_Hierarchy_Selection_panel_verify_all_regions_under_root_with_their_cameras_are_visible_and_checkbox_besides_them_are_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Notifier_028 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.two_second)
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)
            region_list = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                               get_regions_under_root_region_by_xpath())
            # print(f"length of region: {len(region_list)}")
            for items in region_list:
                if items.is_displayed():
                    self.logger.info(f"Region name: {items.text}")
                    self.status.append(True)
                else:
                    self.status.append(False)

            for items in region_list:
                cameras = Notifier_Read_ini().get_cameras_in_region_by_xpath_1() + items.text + Notifier_Read_ini(). \
                    get_cameras_in_region_by_xpath_2()
                cameras = self.d.find_elements(By.XPATH, cameras)
                cameras_names = []
                if len(cameras) > 0:
                    self.logger.info(f"Total Cameras for Region {items.text}: {len(cameras)}")
                    for r in cameras:
                        cameras_names.append(r.text)
                    self.logger.info(f"List of Camera for Region {items.text}: {cameras_names}")
                else:
                    self.logger.info(f"No Camera for region {items.text}")

            time.sleep(web_driver.one_second)
            checkbox = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                            get_checkbox_besides_region_names_in_org_hierarchy_selection_by_xpath())
            for items in checkbox:
                if items.is_displayed():
                    items.click()
                    time.sleep(web_driver.one_second)
                    self.status.append(True)
                else:
                    self.status.append(False)

            self.logger.info(f"status: {self.status}")

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_028.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_028.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_028_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_028_exception.png")
            self.logger.error(f"TC_Notifier_028 got exception as: {ex}")
        finally:
            self.close_notifier_module()


    def Select_one_region_from_list_click_on_Save_button_and_verify_only_selected_region_events_are_visible_verify_STATION_text_is_visible(self):
        try:
            self.logger.info("*********** TC_Notifier_029 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.load_notifier_module()
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.two_second)
            region_list = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                               get_regions_under_root_region_by_xpath())

            camera_path1 = Notifier_Read_ini().get_cameras_in_region_by_xpath_1()
            camera_path2 = Notifier_Read_ini().get_cameras_in_region_by_xpath_2()
            cameras = camera_path1 + region_list[1].text + camera_path2
            print(cameras)
            cameras = self.d.find_elements(By.XPATH, cameras)

            camera_names = []
            for c in cameras:
                camera_names.append(c.text.split("\n"))

            print("camera names:", camera_names)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            checkboxes = Notifier_Read_ini().get_regions_under_root_region_by_xpath() + Notifier_Read_ini(). \
                get_checkboxes_for_regions_by_xpath()
            checkbox_for_region = self.d.find_elements(By.XPATH, checkboxes)
            checkbox_for_region[1].click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Selected Region as: {region_list[1].text}")
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                              get_save_button_on_org_hierarchy_panel_by_xpath())
            # while not save_button.is_displayed():
            #     collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
            #                                            get_collapse_all_button_on_region_selection_panel_by_xpath())
            #     collapse_all_btn.click()
            #     time.sleep(web_driver.one_second)
            self.d.execute_script("arguments[0].click();", save_button)
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on Save button...")
            time.sleep(web_driver.two_second)
            station_name = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                               get_station_name_for_of_event_generation_by_xpath())
            print("station_name>>", station_name.text)
            print("camera_names>>", camera_names)
            camera_names_list = [item for sublist in camera_names for item in sublist]
            if station_name.text in camera_names_list:
                self.logger.info(f"Events for {station_name.text} Station are visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_029.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_029.png")
                return False
            else:
                return True

        except Exception as ex:
            print(ex)
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_029_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_029_exception.png")
            self.logger.error(f"TC_Notifier_029 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Click_on_Notifier_Settings_and_verify_dialog_box_is_visible_verify_heading_on_dialog_box_is_visible(self):
        try:
            self.logger.info("*********** TC_Notifier_030 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            # notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_notifier_setting_button_by_xpath(), self.d)
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on 'Notifier Setting' button...")
            time.sleep(web_driver.one_second)
            notifier_setting_panel = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                         get_notifier_setting_panel_by_xpath())
            if notifier_setting_panel.is_displayed():
                self.logger.info("Notifier Setting panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            panel_heading = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_panel_heading_by_xpath())
            if panel_heading.is_displayed():
                self.logger.info("Notifier panel heading is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            cancel_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                get_cancel_button_on_notifier_setting_panel_by_xpath())
            cancel_button.click()
            time.sleep(web_driver.one_second)
            self.close_notifier_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_030.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_030.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_030_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_030_exception.png")
            self.logger.error(f"TC_Notifier_030 got exception as: {ex}")

    def On_Notifier_Settings_dialog_box_verify_CANCEL_and_SAVE_buttons_are_visible_and_clickable_text_on_buttons_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Notifier_031 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            # notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_notifier_setting_button_by_xpath(), self.d)
            cancel_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                get_cancel_button_on_notifier_setting_panel_by_xpath())
            if cancel_button.is_displayed():
                pass
            else:
                notifier_setting.click()
                time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            if cancel_button.is_displayed():
                self.logger.info("'CANCEL' button is visible....")
                self.status.append(True)
            else:
                self.status.append(False)
            if cancel_button.is_enabled():
                self.logger.info("'CANCEL' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text = cancel_button.text
            self.logger.info(f"actual text on CANCEL button: {actual_text}")
            expected_text = Notifier_Read_ini().get_expected_text_on_cancel_button()
            self.logger.info(f"expected text on CANCEL button: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            save_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                              get_save_button_on_notifier_setting_panel_by_xpath())
            if save_button.is_displayed():
                self.logger.info("'SAVE' button is visible....")
                self.status.append(True)
            else:
                self.status.append(False)
            if save_button.is_enabled():
                self.logger.info("'SAVE' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text = save_button.text
            self.logger.info(f"actual text on SAVE button: {actual_text}")
            expected_text = Notifier_Read_ini().get_expected_text_on_save_button().upper()
            self.logger.info(f"expected text on SAVE button: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_031.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_031.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_031_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_031_exception.png")
            self.logger.error(f"TC_Notifier_031 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def In_Notifier_Settings_verify_Refresh_Rate_text_and_dropdown_beside_it_is_visible_and_clickable_options_inside_dropdown_are_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Notifier_032 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()
            # notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_notifier_setting_button_by_xpath(), self.d)
            cancel_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                get_cancel_button_on_notifier_setting_panel_by_xpath())
            if cancel_button.is_displayed():
                pass
            else:
                notifier_setting.click()
                time.sleep(web_driver.one_second)
            actual_refresh_rate_text = self.d.find_element(By.XPATH, Notifier_Read_ini().get_refresh_rate_text_by_xpath()).text
            expected_refresh_rate_text = Notifier_Read_ini().get_expected_text_refresh_rate()
            if actual_refresh_rate_text == expected_refresh_rate_text:
                self.logger.info(f"{actual_refresh_rate_text} is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            refresh_rate_dropdown = self.d.find_element(By.XPATH, Notifier_Read_ini().get_refresh_rate_dropdown_by_xpath())
            if refresh_rate_dropdown.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            if refresh_rate_dropdown.is_enabled():
                self.status.append(True)
            else:
                self.status.append(False)

            refresh_rate_dropdown.click()
            time.sleep(web_driver.one_second)
            options_in_dropdown = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                       get_refresh_rate_dropdown_options_by_xpath())
            self.logger.info(f"Options in 'Refresh Rate' dropdown: ")
            for options in options_in_dropdown:
                for i in range(len(self.refresh_rate)):
                    if options.text == self.refresh_rate[i]:
                        self.logger.info(f"{i + 1}. {options.text}")
                        self.status.append(True)
                        break

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_032.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_032.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_032_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_032_exception.png")
            self.logger.error(f"TC_Notifier_032 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def In_Notifier_Settings_verify_Of_Events_Displayed_text_and_dropdown_beside_it_is_visible_and_clickable_options_inside_dropdown_are_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Notifier_033 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_notifier_setting_button_by_xpath(), self.d)
            cancel_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                get_cancel_button_on_notifier_setting_panel_by_xpath())
            if cancel_button.is_displayed():
                pass
            else:
                notifier_setting.click()
                time.sleep(web_driver.one_second)

            actual_of_events_displayed_text = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_of_events_display_text_on_notifier_panel_by_xpath()).text
            expected_text = Notifier_Read_ini().get_expected_text_of_events_display()
            print("ok"+ expected_text in actual_of_events_displayed_text)
            if expected_text in actual_of_events_displayed_text:
                self.logger.info(f"{actual_of_events_displayed_text} is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            of_events_display_dropdown = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                             get_events_display_dropdown_by_xpath())
            if of_events_display_dropdown.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            if of_events_display_dropdown.is_enabled():
                self.status.append(True)
            else:
                self.status.append(False)

            of_events_display_dropdown.click()
            time.sleep(web_driver.one_second)
            options_in_dropdown = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                       get_events_display_dropdown_options_by_xpath())
            self.logger.info(f"Options in '# Of Events Display' dropdown: ")
            for options in options_in_dropdown:
                for i in range(len(self.events_displayed)):
                    if str(options.text) == str(self.events_displayed[i]):
                        self.logger.info(f"{i + 1}. {str(options.text)}")
                        self.status.append(True)
                        break

            self.logger.info(f"status: {self.status}")

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_033.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_033.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_033_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_033_exception.png")
            self.logger.error(f"TC_Notifier_033 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def In_Notifier_Settings_verify_Photo_Size_text_and_dropdown_beside_it_is_visible_and_clickable_options_inside_dropdown_are_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Notifier_034 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()
            # notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_notifier_setting_button_by_xpath(), self.d)
            cancel_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                get_cancel_button_on_notifier_setting_panel_by_xpath())
            if cancel_button.is_displayed():
                pass
            else:
                notifier_setting.click()
                time.sleep(web_driver.one_second)

            actual_of_photo_size_text = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_photo_size_text_on_notifier_setting_panel_by_xpath()).text
            expected_text = Notifier_Read_ini().get_expected_text_photo_size()
            if expected_text == actual_of_photo_size_text:
                self.logger.info(f"{actual_of_photo_size_text} is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size_dropdown = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_photo_size_dropdown_by_xpath())
            if photo_size_dropdown.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            if photo_size_dropdown.is_enabled():
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size_dropdown.click()
            time.sleep(web_driver.one_second)
            options_in_dropdown = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                       get_photo_size_dropdown_options_by_xpath())
            self.logger.info(f"Options in 'Photo Size' dropdown: ")
            for options in options_in_dropdown:
                for i in range(len(self.photo_size)):
                    if str(options.text) == str(self.photo_size[i]):
                        self.logger.info(f"{i + 1}. {str(options.text)}")
                        self.status.append(True)
                        break

            self.logger.info(f"status: {self.status}")

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_034.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_034.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_034_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_034_exception.png")
            self.logger.error(f"TC_Notifier_034 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def In_Notifier_Settings_verify_Sound_Option_text_and_dropdown_beside_it_is_visible_and_clickable_options_inside_dropdown_are_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Notifier_035 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()
            # notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_notifier_setting_button_by_xpath(), self.d)
            cancel_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                get_cancel_button_on_notifier_setting_panel_by_xpath())
            if cancel_button.is_displayed():
                pass
            else:
                notifier_setting.click()
                time.sleep(web_driver.one_second)

            actual_of_sound_option_text = \
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_sound_option_text_on_notifier_setting_panel_by_xpath()).text
            expected_text = Notifier_Read_ini().get_expected_text_sound_option()
            if expected_text == actual_of_sound_option_text:
                self.logger.info(f"{actual_of_sound_option_text} is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            sound_option_dropdown = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_sound_option_dropdown_by_xpath())
            if sound_option_dropdown.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            if sound_option_dropdown.is_enabled():
                self.status.append(True)
            else:
                self.status.append(False)

            sound_option_dropdown.click()
            time.sleep(web_driver.one_second)
            options_in_dropdown = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                       get_sound_option_dropdown_options_by_xpath())
            self.logger.info(f"Options in 'Sound Option' dropdown: ")
            for options in options_in_dropdown:
                for i in range(len(self.sound_option)):
                    if str(options.text) == str(self.sound_option[i]):
                        self.logger.info(f"{i + 1}. {str(options.text)}")
                        self.status.append(True)
                        break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH,
                                Notifier_Read_ini().get_cancel_button_on_notifier_setting_panel_by_xpath()).click()
            self.close_notifier_module()
            self.logger.info(f"status: {self.status}")

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_035.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_035.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_035_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_035_exception.png")
            self.logger.error(f"TC_Notifier_035 got exception as: {ex}")

    def Verify_message_to_user_if_there_is_no_event_for_region_selected(self):
        try:
            self.logger.info("*********** TC_Notifier_036 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.two_second)
            region_list = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                               get_regions_under_root_region_by_xpath())
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)

            for items in region_list:
                cameras = Notifier_Read_ini().get_cameras_in_region_by_xpath_1() + items.text + Notifier_Read_ini(). \
                    get_cameras_in_region_by_xpath_2()
                cameras = self.d.find_elements(By.XPATH, cameras)
                self.logger.info(f"length of cameras: {len(cameras)}")
                if len(cameras) == 1:
                    self.logger.info(f"{items.text} -this Region has no camera...")
                    checkbox = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1() + items.text + Notifier_Read_ini(
                    ).get_checkbox_in_region_by_xpath_2()
                    checkbox = self.d.find_element(By.XPATH, checkbox)
                    checkbox.click()
                    time.sleep(web_driver.one_second)
                    self.status.append(True)
                    collapse_all_btn = self.d.find_element(By.XPATH,
                                                           Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
                    collapse_all_btn.click()
                    time.sleep(web_driver.one_second)
                    self.d.find_element(By.XPATH,
                                        Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath()).click()
                    time.sleep(web_driver.one_second)
                    # actual_message = self.d.find_element(By.XPATH, Notifier_Read_ini().get_message_to_user_for_region_selection_by_xpath())
                    actual_message = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_message_to_user_for_region_selection_by_xpath(), self.d)
                    self.logger.info(f"actual message to user: {actual_message.text}")
                    expected_message = Notifier_Read_ini().get_expected_message_to_user_for_region_selection()
                    self.logger.info(f"expected message to user: {expected_message}")
                    if actual_message.text == expected_message:
                        self.status.append(True)
                    else:
                        self.status.append(False)
                    break
                else:
                    self.logger.info(f"All regions have camera(s), please select specific region which is not having camera..")
            time.sleep(web_driver.one_second)
            self.close_notifier_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_036.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_036.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_036_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_036_exception.png")
            self.logger.error(f"TC_Notifier_036 got exception as: {ex}")

    def Verify_message_to_user_if_there_is_no_event_for_group_selected(self):
        try:
            self.logger.info("*********** TC_Notifier_037 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            groups = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                          get_group_items_below_filter_group_list_textbox_by_xpath())
            groups[0].click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH,
                                Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).click()
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.two_second)
            expand_all_btn = self.d.find_element(By.XPATH,
                                                 Notifier_Read_ini().get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)
            region_list = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                               get_regions_under_root_region_by_xpath())
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            for items in region_list:
                cameras = Notifier_Read_ini().get_cameras_in_region_by_xpath_1() + items.text + Notifier_Read_ini(). \
                    get_cameras_in_region_by_xpath_2()
                cameras = self.d.find_elements(By.XPATH, cameras)
                if len(cameras) == 1:
                    self.logger.info(f"{items.text} -this Region has no camera...")
                    checkbox = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1() + items.text + Notifier_Read_ini(
                    ).get_checkbox_in_region_by_xpath_2()
                    checkbox = self.d.find_element(By.XPATH, checkbox)
                    checkbox.click()
                    time.sleep(web_driver.one_second)
                    self.status.append(True)

                    collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
                    collapse_all_btn.click()
                    time.sleep(web_driver.one_second)
                    save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
                    self.d.execute_script("arguments[0].click();", save_btn)
                    time.sleep(web_driver.one_second)

                    # actual_message = self.d.find_element(By.XPATH, Notifier_Read_ini().get_message_to_user_for_group_selection_by_xpath())
                    actual_message = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_message_to_user_for_group_selection_by_xpath(), self.d)
                    self.logger.info(f"actual message for Group selection: {actual_message.text}")
                    expected_message = Notifier_Read_ini().get_expected_message_to_user_for_group_selection()
                    self.logger.info(f"expected message: {expected_message}")
                    if actual_message.text == expected_message:
                        self.status.append(True)
                    else:
                        self.status.append(False)

                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_close_group_selected_visible_on_notifier_panel_by_xpath()).click()
                    time.sleep(web_driver.one_second)
                else:
                    self.logger.info(
                        f"All regions have camera(s), please select specific region which is not having camera..")

            self.close_notifier_module()
            self.logger.info(f"status: {self.status}")

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_037.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_037.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_037_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_037_exception.png")
            self.logger.error(f"TC_Notifier_037 got exception as: {ex}")

    def On_Notifier_panel_verify_COLLAPSE_button_on_event_notification_info_is_visible_and_clickable_text_on_button_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Notifier_038 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()
            time.sleep(web_driver.one_second)
            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            collapse_button = self.explicit_wait(10, "XPATH", Notifier_Read_ini()
                                                 .get_collapse_button_on_event_info_by_xpath(), self.d)
            if collapse_button.is_displayed():
                self.logger.info("'-COLLAPSE' button is visible on event info...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if collapse_button.is_enabled():
                self.logger.info("'-COLLAPSE' button on event info is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text = collapse_button.text
            self.logger.info(f"actual text on COLLAPSE button: {actual_text}")
            expected_text = Notifier_Read_ini().get_expected_text_on_COLLAPSE_button()
            self.logger.info(f"expected text: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            self.close_notifier_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_038.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_038.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_038_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_038_exception.png")
            self.logger.error(f"TC_Notifier_038 got exception as: {ex}")

    def On_Notifier_panel_verify_Close_Notifier_button_on_event_notification_info_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Notifier_039 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()
            time.sleep(web_driver.one_second)

            close_notifier_button = web_driver.explicit_wait(self, 10, "XPATH",
                                     Notifier_Read_ini().
                                     get_close_notifier_button_on_event_info_by_xpath(), self.d)
            if close_notifier_button.is_displayed():
                self.logger.info("'Close Notifier' button is visible on event info..")
                self.status.append(True)
            else:
                self.status.append(False)
            if close_notifier_button.is_enabled():
                self.logger.info("'Close Notifier' button on event info is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text_on_button = close_notifier_button.text
            self.logger.info(f"actual text on 'Close Notifier' button: {actual_text_on_button}")
            expected_text = Notifier_Read_ini().get_expected_text_on_close_notifier_button_on_event_info()
            self.logger.info(f"expected text on 'Close Notifier' button: {expected_text}")
            time.sleep(web_driver.one_second)
            if actual_text_on_button == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            self.close_notifier_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_039.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_039.png")
                logout().logout_from_core(self.d)
                return False
            else:
                logout().logout_from_core(self.d)
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_039_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_039_exception.png")
            self.logger.error(f"TC_Notifier_039 got exception as: {ex}")

    def On_Notifier_panel_click_on_COLLAPSE_button_and_verify_event_alert_info_collapsed_and_EXPAND_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Notifier_040 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)

            radio_button1 = Notifier_Read_ini().get_radio_button_for_group_by_xpath_1()
            radio_button2 = Notifier_Read_ini().get_radio_button_for_group_by_xpath_2()
            radio_button = self.d.find_element(By.XPATH, radio_button1 + self.groups[2].lower() + radio_button2)
            radio_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Group selected as: {self.groups[2]}")
            self.d.find_element(By.XPATH,
                                Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).click()
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            checkbox1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, checkbox1 + Notifier_Read_ini().get_region_name() + checkbox2)
            checkbox.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Region selected as: {Notifier_Read_ini().get_region_name() }")
            time.sleep(web_driver.one_second)
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_button_on_event_info_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on COLLAPSE button..")
            expand_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                get_expand_button_on_event_info_by_xpath())
            if expand_button.is_displayed():
                self.logger.info(f"'+EXPAND' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_close_group_selected_visible_on_notifier_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_040.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_040.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_040_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_040_exception.png")
            self.logger.error(f"TC_Notifier_040 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_EXPAND_button_is_clickable_and_text_on_it_is_visible_click_on_EXPAND_button_and_verify_it_is_navigating_back_to_event_alert_info(self):
        try:
            self.logger.info("*********** TC_Notifier_041 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)

            radio_button1 = Notifier_Read_ini().get_radio_button_for_group_by_xpath_1()
            radio_button2 = Notifier_Read_ini().get_radio_button_for_group_by_xpath_2()
            radio_button = self.d.find_element(By.XPATH, radio_button1 + self.groups[0].lower() + radio_button2)
            radio_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Group selected as: {self.groups[0]}")
            self.d.find_element(By.XPATH,
                                Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            expand_all_btn = self.d.find_element(By.XPATH,
                                                 Notifier_Read_ini().get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            checkbox1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, checkbox1 + Notifier_Read_ini().get_region_name()  + checkbox2)
            checkbox.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Region selected as: {Notifier_Read_ini().get_region_name() }")
            time.sleep(web_driver.one_second)
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_button_on_event_info_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on COLLAPSE button..")
            expand_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                get_expand_button_on_event_info_by_xpath())
            if expand_button.is_enabled():
                self.logger.info(f"'+EXPAND' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text_on_expand_button = expand_button.text
            self.logger.info(f"actual text on +EXPAND button: {actual_text_on_expand_button}")
            expected_text = Notifier_Read_ini().get_expected_text_on_expand_button()
            self.logger.info(f"expected text: {expected_text}")
            if actual_text_on_expand_button == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)

            expand_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on '+ EXPAND' button....")

            collapse_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                  get_collapse_button_on_event_info_by_xpath())
            time.sleep(web_driver.one_second)
            if collapse_button.is_displayed():
                self.logger.info("It is navigated to event info page....")
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_notifier_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_041.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_041.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_041_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_041_exception.png")
            self.logger.error(f"TC_Notifier_041 got exception as: {ex}")

    def On_Notifier_panel_click_on_Close_Notifier_button_and_verify_notifier_is_closed_and_Events_panel_and_Enrollment_View_panel_are_visible(self):
        try:
            self.logger.info("*********** TC_Notifier_042 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            time.sleep(web_driver.three_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            cancel_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                get_cancel_button_on_notifier_setting_panel_by_xpath())
            while cancel_button.is_displayed():
                cancel_button.click()
                time.sleep(web_driver.one_second)
            time.sleep(web_driver.three_second)
            close_notifier_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_close_notifier_button_on_event_info_by_xpath())
            if close_notifier_btn.is_displayed():
                close_notifier_btn.click()
                self.logger.info("Clicked on 'Close Notifier' button.....")
                time.sleep(web_driver.three_second)

                enrollment_view_panel = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                            get_enrollment_view_panel_by_xpath())
                if enrollment_view_panel.is_displayed():
                    self.logger.info("'Enrollment-View' panel is visible...")
                    self.status.append(True)
                else:
                    self.status.append(False)

                events_panel = self.d.find_element(By.XPATH, Notifier_Read_ini().get_events_panel_by_xpath())
                if events_panel.is_displayed():
                    self.logger.info("'Events' panel is visible...")
                    self.status.append(True)
                else:
                    self.status.append(False)

                time.sleep(web_driver.one_second)
                close_all_panels = self.d.find_elements(By.XPATH,
                                                        Notifier_Read_ini().get_close_panel_buttons_by_xpath())

                for btn in close_all_panels:
                    btn.click()
                    time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_042.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_042.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_042_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_042_exception.png")
            self.logger.error(f"TC_Notifier_042 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def notifier_result_verification(self):
        try:
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")

            if len(actual_number_of_events) > 0:
                time.sleep(web_driver.one_second)
                expected_events = self.events_displayed[1]
                self.logger.info(f"expected number of events displayed: {expected_events}")
                if len(actual_number_of_events) == expected_events:
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(web_driver.one_second)
                actual_live_image_text = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                             get_live_image_text_by_xpath()).text
                self.logger.info(f"actual text: {actual_live_image_text}")
                expected_live_image_text = Notifier_Read_ini().get_expected_live_image_text()
                self.logger.info(f"expected text: {expected_live_image_text}")

                if actual_live_image_text == expected_live_image_text:
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(web_driver.one_second)
                actual_possible_match_text = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                 get_possible_match_text_by_xpath()).text
                self.logger.info(f"actual possible match text: {actual_possible_match_text}")
                expected_possible_match_text = Notifier_Read_ini().get_expected_text_possible_match()
                self.logger.info(f"expected text: {expected_possible_match_text}")
                if actual_possible_match_text == expected_possible_match_text:
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(web_driver.one_second)
                expected_alert_completion_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_alert_completion_time_on_notifier_panel_by_xpath()).text

                expected_notification_alert_real_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_notifier_alert_real_time_on_notifier_panel_by_xpath()).text

                expected_station_name = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                            get_station_name_for_of_event_generation_by_xpath()).text

                self.d.find_element(By.XPATH, Notifier_Read_ini().get_close_notifier_button_on_event_info_by_xpath()). \
                    click()
                time.sleep(web_driver.three_second)
                actual_alert_completion_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_alert_completion_time_on_events_panel_by_xpath()).text
                self.logger.info(f"actual alert completion time: {actual_alert_completion_time}")
                self.logger.info(f"expected Alert completion time: {expected_alert_completion_time}")
                if expected_alert_completion_time == actual_alert_completion_time:
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(web_driver.one_second)
                actual_notification_alert_real_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_notifier_alert_real_time_on_events_panel_by_xpath()).text
                self.logger.info(f"actual notification alert real time: {actual_notification_alert_real_time}")
                self.logger.info(f"expected Notification alert real time: {expected_notification_alert_real_time}")
                actual_time_list = actual_notification_alert_real_time.split(' ')
                expected_time_list = expected_notification_alert_real_time.split(' ')
                actual_num = actual_time_list[0]
                expected_num = expected_time_list[0]
                if actual_num.isnumeric():
                    actual_num = int(actual_num)
                if expected_num.isnumeric():
                    expected_num = int(expected_num)
                self.logger.info(f"actual_time: {actual_num} min")
                self.logger.info(f"expected_time: {expected_num} min")
                if actual_num.is_integer() and expected_num.is_integer():
                    if actual_num >= expected_num:
                        self.status.append(True)
                    else:
                        self.status.append(False)
                else:
                    self.logger.info(f"no number found in time string")
                time.sleep(web_driver.one_second)
                actual_station_name = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_station_name_on_events_panel_by_xpath()).text
                self.logger.info(f"actual station name: {actual_station_name}")
                self.logger.info(f"expected station name: {expected_station_name}")
                if actual_station_name == expected_station_name:
                    self.status.append(True)
                else:
                    self.status.append(False)
                self.d.find_element(By.XPATH, Notifier_Read_ini().
                                    get_enrollments_group_button_on_enrollments_view_panel_by_xpath()).click()
                time.sleep(10)
                enrollment_group_name = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_enrollment_group_name_on_enrollment_groups_panel_by_xpath())
                name = enrollment_group_name.text.upper()
                time.sleep(web_driver.one_second)
                self.logger.info(f"expected to select group name: {self.group_selected}")
                self.logger.info(f"actual selected group name: {name}")
                # if self.group_selected == name:
                #     self.logger.info(f"Enrollment Group name on 'Enrollment Groups' panel: {self.group_selected}")
                #     self.status.append(True)
                # else:
                #     self.status.append(False)
            else:
                actual_message = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                     get_message_to_user_for_group_selection_by_xpath()).text
                self.logger.info(f"Message to User: {actual_message}")
                if actual_message:
                    self.status.append(True)
                else:
                    self.status.append(False)
        except Exception as ex:
            self.logger.error(ex)
            return False

    def notifier_result_verification_for_all_groups_selected(self):
        try:
            time.sleep(web_driver.one_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            if len(actual_number_of_events) > 0:
                time.sleep(web_driver.one_second)
                actual_live_image_text = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                             get_live_image_text_by_xpath()).text
                self.logger.info(f"actual text: {actual_live_image_text}")
                expected_live_image_text = Notifier_Read_ini().get_expected_live_image_text()
                self.logger.info(f"expected text: {expected_live_image_text}")
                if actual_live_image_text == expected_live_image_text:
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(10)
                # actual_possible_match_text = self.d.find_element(By.XPATH, Notifier_Read_ini().
                #                                                  get_possible_match_text_by_xpath()).text
                # self.logger.info(f"actual possible match text: {actual_possible_match_text}")
                # expected_possible_match_text = Notifier_Read_ini().get_expected_text_possible_match()
                # self.logger.info(f"expected text: {expected_possible_match_text}")
                # if actual_possible_match_text == expected_possible_match_text:
                #     self.status.append(True)
                # else:
                #     self.status.append(False)

                expected_alert_completion_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_alert_completion_time_on_notifier_panel_by_xpath()).text
                expected_notification_alert_real_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_notifier_alert_real_time_on_notifier_panel_by_xpath()).text
                expected_station_name = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                            get_station_name_for_of_event_generation_by_xpath()).text
                self.d.find_element(By.XPATH, Notifier_Read_ini().get_close_notifier_button_on_event_info_by_xpath()). \
                    click()
                time.sleep(web_driver.three_second)
                actual_alert_completion_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_alert_completion_time_on_events_panel_by_xpath()).text
                act_num = actual_alert_completion_time.split(' ')
                self.logger.info(f"actual alert completion time: {actual_alert_completion_time}")
                self.logger.info(f"expected Alert completion time: {expected_alert_completion_time}")
                exp_num = expected_alert_completion_time.split(' ')

                time.sleep(web_driver.one_second)
                if (actual_alert_completion_time == expected_alert_completion_time) or (act_num[0] == exp_num[0]):
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(web_driver.one_second)
                actual_notification_alert_real_time = \
                    self.d.find_element(By.XPATH, Notifier_Read_ini().
                                        get_notifier_alert_real_time_on_events_panel_by_xpath()).text
                self.logger.info(f"actual notification alert real time: {actual_notification_alert_real_time}")
                self.logger.info(f"expected Notification alert real time: {expected_notification_alert_real_time}")

                if (actual_notification_alert_real_time == int(expected_notification_alert_real_time) - 1 or
                        int(expected_notification_alert_real_time) + 1):
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(web_driver.one_second)
                actual_station_name = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_station_name_on_events_panel_by_xpath()).text
                self.logger.info(f"actual station name: {actual_station_name}")
                self.logger.info(f"expected station name: {expected_station_name}")

                if str(actual_station_name) == str(expected_station_name):
                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                actual_message = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                     get_message_to_user_for_group_selection_by_xpath()).text
                self.logger.info(f"Message to User: {actual_message}")
                if actual_message:
                    self.status.append(True)
                else:
                    self.status.append(False)
        except Exception as ex:
            self.logger.error(ex)
            return False

    def Verify_Notifier_result_for_root_region_selected_with_refresh_rate_5_min_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_044 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()
            time.sleep(web_driver.three_second)
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[1])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[1]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[1]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[1])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[2])
            self.logger.info(f"Photo Size: {self.photo_size[2]}")
            time.sleep(web_driver.one_second)
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            updating_status = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                   get_updating_text_on_notifier_panel_by_xpath())
            updating_status_element = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_updating_text_on_notifier_panel_by_xpath())
            t = 300
            c = 0
            if len(updating_status) == 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"1Refreshing page after {c} seconds/5 minutes..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            elif len(updating_status) > 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"2Refreshing page after {c} seconds/5 minutes..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_044.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_044.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_044_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_044_exception.png")
            self.logger.error(f"TC_Notifier_044 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_region_selected_with_refresh_rate_4_min_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_045 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[2])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[2]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[1]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[1])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[2])
            self.logger.info(f"Photo Size: {self.photo_size[2]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            updating_status = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                   get_updating_text_on_notifier_panel_by_xpath())
            updating_status_element = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_updating_text_on_notifier_panel_by_xpath())
            t = 240
            c = 0
            if len(updating_status) == 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"1Refreshing page after {c} seconds/4 minutes..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            elif len(updating_status) > 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"2Refreshing page after {c} seconds/4 minutes..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_045.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_045.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_045_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_045_exception.png")
            self.logger.error(f"TC_Notifier_045 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_region_selected_with_refresh_rate_3_min_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_046 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[3])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[3]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[1]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[1])}")
            time.sleep(web_driver.one_second)
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[2])
            self.logger.info(f"Photo Size: {self.photo_size[2]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            updating_status = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                   get_updating_text_on_notifier_panel_by_xpath())
            updating_status_element = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_updating_text_on_notifier_panel_by_xpath())
            t = 180
            c = 0
            if len(updating_status) == 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"1Refreshing page after {c} seconds/3 minutes..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            elif len(updating_status) > 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"2Refreshing page after {c} seconds/3 minutes..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_046.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_046.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_046_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_046_exception.png")
            self.logger.error(f"TC_Notifier_046 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_region_selected_with_refresh_rate_2_min_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_047 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()
            time.sleep(web_driver.three_second)
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[4])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[4]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[1]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[1])}")
            time.sleep(web_driver.one_second)
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[2])
            self.logger.info(f"Photo Size: {self.photo_size[2]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            updating_status = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                   get_updating_text_on_notifier_panel_by_xpath())
            updating_status_element = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_updating_text_on_notifier_panel_by_xpath())
            t = 120
            c = 0
            if len(updating_status) == 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"1Refreshing page after {c} seconds/2 minutes..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            elif len(updating_status) > 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"2Refreshing page after {c} seconds/2 minutes..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_047.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_047.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_047_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_047_exception.png")
            self.logger.error(f"TC_Notifier_047 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_region_selected_with_refresh_rate_1_min_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_048 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()
            time.sleep(web_driver.three_second)
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[5])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[5]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[1]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[1])}")
            time.sleep(web_driver.one_second)
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[2])
            self.logger.info(f"Photo Size: {self.photo_size[2]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            updating_status = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                   get_updating_text_on_notifier_panel_by_xpath())
            updating_status_element = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_updating_text_on_notifier_panel_by_xpath())
            t = 60
            c = 0
            if len(updating_status) == 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"1Refreshing page after {c} seconds/1 minute..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            elif len(updating_status) > 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"2Refreshing page after {c} seconds..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_048.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_048.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_048_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_048_exception.png")
            self.logger.error(f"TC_Notifier_048 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_region_selected_with_refresh_rate_30_sec_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_049 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()
            time.sleep(web_driver.three_second)
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)

            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[6])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[6]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[1]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[1])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[2])
            self.logger.info(f"Photo Size: {self.photo_size[2]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            updating_status = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                   get_updating_text_on_notifier_panel_by_xpath())
            updating_status_element = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_updating_text_on_notifier_panel_by_xpath())
            t = 30
            c = 0
            if len(updating_status) == 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"1Refreshing page after {c} seconds..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            elif len(updating_status) > 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"2Refreshing page after {c} seconds..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_049.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_049.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_049_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_049_exception.png")
            self.logger.error(f"TC_Notifier_049 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_region_selected_with_refresh_rate_10_sec_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_050 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()
            time.sleep(web_driver.three_second)
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[7])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[7]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[1]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[1])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[2])
            self.logger.info(f"Photo Size: {self.photo_size[2]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)

            updating_status = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                   get_updating_text_on_notifier_panel_by_xpath())
            updating_status_element = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_updating_text_on_notifier_panel_by_xpath())
            t = 10
            c = 0
            if len(updating_status) == 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"1Refreshing page after {c} seconds..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            elif len(updating_status) > 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass

                self.logger.info(f"2Refreshing page after {c} seconds..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_050.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_050.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_050_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_050_exception.png")
            self.logger.error(f"TC_Notifier_050 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_region_selected_with_refresh_rate_5_sec_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_051 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()
            time.sleep(web_driver.three_second)
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[8])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[8]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[1]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[1])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[2])
            self.logger.info(f"Photo Size: {self.photo_size[2]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)

            updating_status = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                   get_updating_text_on_notifier_panel_by_xpath())
            updating_status_element = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_updating_text_on_notifier_panel_by_xpath())
            t = 5
            c = 0
            if len(updating_status) == 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.logger.info("UPDATING before time...")
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"1Refreshing page after {c} seconds..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            elif len(updating_status) > 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.logger.info("UPDATING before time...")
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"2Refreshing page after {c} seconds..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_051.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_051.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_051_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_051_exception.png")
            self.logger.error(f"TC_Notifier_051 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_region_selected_with_refresh_rate_1_sec_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_052 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()
            time.sleep(web_driver.three_second)
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[9])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[9]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[1]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[1])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[2])
            self.logger.info(f"Photo Size: {self.photo_size[2]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            updating_status = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                   get_updating_text_on_notifier_panel_by_xpath())
            updating_status_element = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_updating_text_on_notifier_panel_by_xpath())
            t = 1
            c = 0
            if len(updating_status) == 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"1Refreshing page after {c} second..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            elif len(updating_status) > 0:
                while t > 0:
                    time.sleep(web_driver.one_second)
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"2Refreshing page after {c} second..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_052.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_052.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_052_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_052_exception.png")
            self.logger.error(f"TC_Notifier_052 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_053 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[1]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[1])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[2])
            self.logger.info(f"Photo Size: {self.photo_size[2]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {actual_number_of_events}")
            expected_events = self.events_displayed[1]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.one_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()). \
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[2]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_053.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_053.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_053_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_053_exception.png")
            self.logger.error(f"TC_Notifier_053 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_1_photo_size_as_XX_Large_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_054 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[0]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[0])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[5])
            self.logger.info(f"Photo Size: {self.photo_size[5]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()). \
                click()
            time.sleep(web_driver.two_second)
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)

            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")
            expected_events = self.events_displayed[0]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.one_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()). \
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[5]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_054.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_054.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_054_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_054_exception.png")
            self.logger.error(f"TC_Notifier_054 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_3_photo_size_as_X_Large_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_055 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[2]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[2])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[4])
            self.logger.info(f"Photo Size: {self.photo_size[4]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")
            expected_events = self.events_displayed[2]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.one_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()). \
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[4]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_055.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_055.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_055_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_055_exception.png")
            self.logger.error(f"TC_Notifier_055 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_4_photo_size_as_Large_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_056 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[3]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[3])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[3])
            self.logger.info(f"Photo Size: {self.photo_size[3]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")
            expected_events = self.events_displayed[3]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.one_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()). \
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[3]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_056.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_056.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_056_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_056_exception.png")
            self.logger.error(f"TC_Notifier_056 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_5_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_057 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[4]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[4])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[2])
            self.logger.info(f"Photo Size: {self.photo_size[2]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")
            expected_events = self.events_displayed[4]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.one_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()). \
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[2]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_057.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_057.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_057_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_057_exception.png")
            self.logger.error(f"TC_Notifier_057 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_6_photo_size_as_Small_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_058 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            time.sleep(web_driver.two_second)
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.two_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.two_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.two_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[5]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[5])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[1])
            self.logger.info(f"Photo Size: {self.photo_size[1]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")
            expected_events = self.events_displayed[5]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.two_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()). \
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[1]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.two_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_058.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_058.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_058_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_058_exception.png")
            self.logger.error(f"TC_Notifier_058 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_7_photo_size_as_X_Small_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_059 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            time.sleep(web_driver.two_second)
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.two_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.two_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[6]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[6])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[0])
            self.logger.info(f"Photo Size: {self.photo_size[0]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")
            expected_events = self.events_displayed[6]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.two_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()). \
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[0]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.two_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_059.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_059.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_059_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_059_exception.png")
            self.logger.error(f"TC_Notifier_059 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_8_photo_size_as_X_Small_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_060 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[7]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[7])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[0])
            self.logger.info(f"Photo Size: {self.photo_size[0]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")
            expected_events = self.events_displayed[7]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.one_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()). \
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[0]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_060.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_060.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_060_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_060_exception.png")
            self.logger.error(f"TC_Notifier_060 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_9_photo_size_as_X_Small_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_061 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            time.sleep(web_driver.two_second)
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.two_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.two_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.two_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[8]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[8])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[0])
            self.logger.info(f"Photo Size: {self.photo_size[0]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")
            expected_events = self.events_displayed[8]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.two_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()). \
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[0]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.two_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_061.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_061.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_061_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_061_exception.png")
            self.logger.error(f"TC_Notifier_061 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_10_photo_size_as_X_Small_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_062 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[9]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[9])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[0])
            self.logger.info(f"Photo Size: {self.photo_size[0]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")
            expected_events = self.events_displayed[9]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.one_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()). \
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[0]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_062.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_062.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_062_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_062_exception.png")
            self.logger.error(f"TC_Notifier_062 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_11_photo_size_as_X_Small_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_063 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[10]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[10])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[0])
            self.logger.info(f"Photo Size: {self.photo_size[0]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")
            expected_events = self.events_displayed[10]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.one_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()). \
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[0]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_063.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_063.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_063_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_063_exception.png")
            self.logger.error(f"TC_Notifier_063 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_12_photo_size_as_X_Small_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_064 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[11]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[11])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[0])
            self.logger.info(f"Photo Size: {self.photo_size[0]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")
            expected_events = self.events_displayed[11]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.one_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()). \
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[0]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_064.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_064.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_064_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_064_exception.png")
            self.logger.error(f"TC_Notifier_064 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_13_photo_size_as_X_Small_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_065 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[12]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[12])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[0])
            self.logger.info(f"Photo Size: {self.photo_size[0]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")
            expected_events = self.events_displayed[12]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.one_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()). \
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[0]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_065.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_065.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_065_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_065_exception.png")
            self.logger.error(f"TC_Notifier_065 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_14_photo_size_as_X_Small_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_066 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[13]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[13])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[0])
            self.logger.info(f"Photo Size: {self.photo_size[0]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")
            expected_events = self.events_displayed[13]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.one_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()). \
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[0]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_066.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_066.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_066_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_066_exception.png")
            self.logger.error(f"TC_Notifier_066 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_15_photo_size_as_X_Small_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_067 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)

            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[14]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[14])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[0])
            self.logger.info(f"Photo Size: {self.photo_size[0]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")
            expected_events = self.events_displayed[14]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.one_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()). \
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[0]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_067.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_067.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_067_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_067_exception.png")
            self.logger.error(f"TC_Notifier_067 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_regions_selected_with_Auto_Refresh_Off_events_displayed_as_20_photo_size_as_X_Small_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_068 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[15]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[15])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[0])
            self.logger.info(f"Photo Size: {self.photo_size[0]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.two_second)
            actual_number_of_events = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                           get_number_of_events_displayed_by_xpath())
            self.logger.info(f"actual number of events displayed: {len(actual_number_of_events)}")
            expected_events = self.events_displayed[15]
            self.logger.info(f"expected number of events displayed: {expected_events}")
            time.sleep(web_driver.one_second)
            if len(actual_number_of_events) == expected_events:
                self.status.append(True)
            else:
                self.status.append(False)

            photo_size = self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_on_event_info_by_xpath()).\
                get_attribute('class')
            self.logger.info(f"actual photo size: {photo_size}")
            expected_photo_size = self.photo_size[0]
            self.logger.info(f"expected photo size: {expected_photo_size.lower()}")
            if expected_photo_size.lower() in photo_size:
                self.status.append(True)
            else:
                self.status.append(False)

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_068.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_068.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_068_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_068_exception.png")
            self.logger.error(f"TC_Notifier_068 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def get_default_notifier_setting_values(self):
        try:
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[0])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[0]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[1]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[1])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[2])
            self.logger.info(f"Photo Size: {self.photo_size[2]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[0])
            self.logger.info(f"Sound Option: {self.sound_option[0]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_ABE_group_from_ini(self):
        try:
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            select_group_textbox = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                       get_filter_group_list_textbox_by_xpath())
            select_group_textbox.clear()
            time.sleep(web_driver.one_second)
            select_group_textbox.send_keys(Notifier_Read_ini().get_abe_enrollment_group())
            time.sleep(web_driver.one_second)
            group_list_below_textbox = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                            get_group_items_below_filter_group_list_textbox_by_xpath())
            group_list_below_textbox[0].click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Group selected as: {group_list_below_textbox[0].text}")
            self.group_selected = group_list_below_textbox[0].text
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_PTE_group_from_ini(self):
        try:
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            select_group_textbox = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                       get_filter_group_list_textbox_by_xpath())
            select_group_textbox.clear()
            time.sleep(web_driver.one_second)
            select_group_textbox.send_keys(Notifier_Read_ini().get_pte_enrollment_group())
            time.sleep(web_driver.one_second)
            group_list_below_textbox = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                            get_group_items_below_filter_group_list_textbox_by_xpath())
            group_list_below_textbox[0].click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Group selected as: {group_list_below_textbox[0].text}")
            self.group_selected = group_list_below_textbox[0].text
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_FRAUDE_group_from_ini(self):
        try:
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            select_group_textbox = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                       get_filter_group_list_textbox_by_xpath())
            select_group_textbox.clear()
            time.sleep(web_driver.one_second)
            select_group_textbox.send_keys(Notifier_Read_ini().get_fraude_enrollment_group())
            time.sleep(web_driver.one_second)
            group_list_below_textbox = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                            get_group_items_below_filter_group_list_textbox_by_xpath())
            group_list_below_textbox[0].click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Group selected as: {group_list_below_textbox[0].text}")
            self.group_selected = group_list_below_textbox[0].text
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_VIPE_group_from_ini(self):
        try:
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            select_group_textbox = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                       get_filter_group_list_textbox_by_xpath())
            select_group_textbox.clear()
            time.sleep(web_driver.one_second)
            select_group_textbox.send_keys(Notifier_Read_ini().get_vipe_enrollment_group())
            time.sleep(web_driver.one_second)
            group_list_below_textbox = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                            get_group_items_below_filter_group_list_textbox_by_xpath())
            group_list_below_textbox[0].click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Group selected as: {group_list_below_textbox[0].text}")
            self.group_selected = group_list_below_textbox[0].text
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_SOE_group_from_ini(self):
        try:
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            select_group_textbox = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                       get_filter_group_list_textbox_by_xpath())
            select_group_textbox.clear()
            time.sleep(web_driver.one_second)
            select_group_textbox.send_keys(Notifier_Read_ini().get_soe_enrollment_group())
            time.sleep(web_driver.one_second)
            group_list_below_textbox = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                            get_group_items_below_filter_group_list_textbox_by_xpath())
            group_list_below_textbox[0].click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Group selected as: {group_list_below_textbox[0].text}")
            self.group_selected = group_list_below_textbox[0].text
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()). \
                click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_first_region_from_ini(self):
        try:
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)

            checkbox1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, checkbox1 + Notifier_Read_ini().get_region_name() + checkbox2)
            checkbox.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Region selected as: {Notifier_Read_ini().get_region_name()}")

            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_second_region_from_ini(self):
        try:
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)

            checkbox1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, checkbox1 + Notifier_Read_ini().get_region_name() + checkbox2)
            checkbox.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Region selected as: {Notifier_Read_ini().get_region_name()}")

            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_third_region_from_ini(self):
        try:
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)

            checkbox1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, checkbox1 + Notifier_Read_ini().get_region_name() + checkbox2)
            checkbox.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Region selected as: {Notifier_Read_ini().get_region_name()}")

            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_fourth_region_from_ini(self):
        try:
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)

            checkbox1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, checkbox1 + Notifier_Read_ini().get_region_name() + checkbox2)
            checkbox.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Region selected as: {Notifier_Read_ini().get_region_name()}")

            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def select_fifth_region_from_ini(self):
        try:
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)

            checkbox1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, checkbox1 + Notifier_Read_ini().get_region_name() + checkbox2)
            checkbox.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Region selected as: {Notifier_Read_ini().get_region_name()}")

            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def Verify_Notifier_result_for_root_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_069 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)

            self.select_ABE_group_from_ini()

            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            time.sleep(web_driver.one_second)
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_069.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_069.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_069_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_069_exception.png")
            self.logger.error(f"TC_Notifier_069 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_region_selected_with_group_selected_as_PTE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_070 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)

            self.select_PTE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_070.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_070.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_070_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_070_exception.png")
            self.logger.error(f"TC_Notifier_070 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_region_selected_with_group_selected_as_FRAUDE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_071 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)

            self.select_FRAUDE_group_from_ini()

            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_071.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_071.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_071_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_071_exception.png")
            self.logger.error(f"TC_Notifier_071 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_region_selected_with_group_selected_as_VIPE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_072 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)

            self.select_VIPE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_072.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_072.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_072_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_072_exception.png")
            self.logger.error(f"TC_Notifier_072 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_region_selected_with_group_selected_as_SOE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_073 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)

            self.select_SOE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_073.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_073.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_073_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_073_exception.png")
            self.logger.error(f"TC_Notifier_073 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_first_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_074 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_first_region_from_ini()
            self.select_ABE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_074.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_074.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_074_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_074_exception.png")
            self.logger.error(f"TC_Notifier_074 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_first_region_selected_with_group_selected_as_PTE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_075 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_first_region_from_ini()
            self.select_PTE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_075.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_075.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_075_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_075_exception.png")
            self.logger.error(f"TC_Notifier_075 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_first_region_selected_with_group_selected_as_FRAUDE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_076 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_first_region_from_ini()
            self.select_FRAUDE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_076.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_076.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_076_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_076_exception.png")
            self.logger.error(f"TC_Notifier_076 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_first_region_selected_with_group_selected_as_VIPE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_077 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_first_region_from_ini()
            self.select_VIPE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_077.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_077.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_077_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_077_exception.png")
            self.logger.error(f"TC_Notifier_077 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_first_region_selected_with_group_selected_as_SOE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_078 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_first_region_from_ini()
            self.select_SOE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_078.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_078.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_078_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_078_exception.png")
            self.logger.error(f"TC_Notifier_078 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_second_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_079 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_second_region_from_ini()
            self.select_ABE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_079.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_079.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_079_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_079_exception.png")
            self.logger.error(f"TC_Notifier_079 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_second_region_selected_with_group_selected_as_PTE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_080 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_second_region_from_ini()
            self.select_PTE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_080.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_080.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_080_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_080_exception.png")
            self.logger.error(f"TC_Notifier_080 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_second_region_selected_with_group_selected_as_FRAUDE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_081 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_second_region_from_ini()
            self.select_FRAUDE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_081.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_081.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_081_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_081_exception.png")
            self.logger.error(f"TC_Notifier_081 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_second_region_selected_with_group_selected_as_VIPE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_082 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_second_region_from_ini()
            self.select_VIPE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_082.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_082.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_082_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_082_exception.png")
            self.logger.error(f"TC_Notifier_082 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_second_region_selected_with_group_selected_as_SOE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_083 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_second_region_from_ini()
            self.select_SOE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_083.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_083.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_083_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_083_exception.png")
            self.logger.error(f"TC_Notifier_083 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_third_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_084 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_third_region_from_ini()
            self.select_ABE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_084.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_084.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_084_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_084_exception.png")
            self.logger.error(f"TC_Notifier_084 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_third_region_selected_with_group_selected_as_PTE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_085 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_third_region_from_ini()
            self.select_PTE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_085.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_085.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_085_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_085_exception.png")
            self.logger.error(f"TC_Notifier_085 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_third_region_selected_with_group_selected_as_FRAUDE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_086 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_third_region_from_ini()
            self.select_FRAUDE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_086.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_086.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_086_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_086_exception.png")
            self.logger.error(f"TC_Notifier_086 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_third_region_selected_with_group_selected_as_VIPE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_087 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_third_region_from_ini()
            self.select_VIPE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_087.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_087.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_087_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_087_exception.png")
            self.logger.error(f"TC_Notifier_087 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_third_region_selected_with_group_selected_as_SOE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_088 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_third_region_from_ini()
            self.select_SOE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_088.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_088.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_088_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_088_exception.png")
            self.logger.error(f"TC_Notifier_088 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_fourth_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_089 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_fourth_region_from_ini()
            self.select_ABE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_089.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_089.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_089_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_089_exception.png")
            self.logger.error(f"TC_Notifier_089 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_fourth_region_selected_with_group_selected_as_PTE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_090 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_fourth_region_from_ini()
            self.select_PTE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_090.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_090.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_090_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_090_exception.png")
            self.logger.error(f"TC_Notifier_090 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_fourth_region_selected_with_group_selected_as_FRAUDE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_091 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_fourth_region_from_ini()
            self.select_FRAUDE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_091.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_091.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_091_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_091_exception.png")
            self.logger.error(f"TC_Notifier_091 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_fourth_region_selected_with_group_selected_as_VIPE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_092 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_fourth_region_from_ini()
            self.select_VIPE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_092.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_092.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_092_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_092_exception.png")
            self.logger.error(f"TC_Notifier_092 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_fourth_region_selected_with_group_selected_as_SOE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_093 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_fourth_region_from_ini()
            self.select_SOE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_093.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_093.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_093_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_093_exception.png")
            self.logger.error(f"TC_Notifier_093 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_fifth_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(
            self):
        try:
            self.logger.info("*********** TC_Notifier_094 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_fifth_region_from_ini()
            self.select_ABE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_094.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_094.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_094_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_094_exception.png")
            self.logger.error(f"TC_Notifier_094 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_fifth_region_selected_with_group_selected_as_PTE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(
            self):
        try:
            self.logger.info("*********** TC_Notifier_095 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_fifth_region_from_ini()
            self.select_PTE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_095.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_095.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_095_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_095_exception.png")
            self.logger.error(f"TC_Notifier_095 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_fifth_region_selected_with_group_selected_as_FRAUDE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(
            self):
        try:
            self.logger.info("*********** TC_Notifier_096 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_fifth_region_from_ini()
            self.select_FRAUDE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_096.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_096.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_096_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_096_exception.png")
            self.logger.error(f"TC_Notifier_096 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_fifth_region_selected_with_group_selected_as_VIPE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(
            self):
        try:
            self.logger.info("*********** TC_Notifier_097 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
             
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_fifth_region_from_ini()
            self.select_VIPE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_097.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_097.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_097_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_097_exception.png")
            self.logger.error(f"TC_Notifier_097 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_fifth_region_selected_with_group_selected_as_SOE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(
            self):
        try:
            self.logger.info("*********** TC_Notifier_098 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.select_fifth_region_from_ini()
            self.select_SOE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()
            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_098.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_098.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_098_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_098_exception.png")
            self.logger.error(f"TC_Notifier_098 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_087 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            camera_1 = Notifier_Read_ini().get_cameras_in_region_by_xpath_1()
            camera_2 = Notifier_Read_ini().get_cameras_in_region_by_xpath_2()
            checkbox_1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox_2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            print(camera_1 + Notifier_Read_ini().get_camera0() + camera_2 + checkbox_1 +
                                           Notifier_Read_ini().get_camera1() + checkbox_2)
            checkbox = self.d.find_element(By.XPATH, camera_1 + Notifier_Read_ini().get_camera0() + camera_2 + checkbox_1 +
                                           Notifier_Read_ini().get_camera1() + checkbox_2)
            checkbox.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Camera selected as: {Notifier_Read_ini().get_camera0()}")
            time.sleep(web_driver.one_second)
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                   get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            self.select_ABE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()

            # close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            # for btn in close_all_panels:
            #     btn.click()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_087.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_087.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_087_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_087_exception.png")
            self.logger.error(f"TC_Notifier_087 got exception as: {ex}")
        finally:
            # pass
            self.close_notifier_module()

    def Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_PTE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(
            self):
        try:
            self.logger.info("*********** TC_Notifier_088 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH",  Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            camera_1 = Notifier_Read_ini().get_cameras_in_region_by_xpath_1()
            camera_2 = Notifier_Read_ini().get_cameras_in_region_by_xpath_2()
            checkbox_1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox_2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, camera_1 + Notifier_Read_ini().get_camera0() + camera_2 + checkbox_1 +
                                           Notifier_Read_ini().get_camera1() + checkbox_2)
            checkbox.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Camera selected as: {Notifier_Read_ini().get_camera0()}")
            time.sleep(web_driver.one_second)
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                   get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            self.select_PTE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_088.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_088.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_088_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_088_exception.png")
            self.logger.error(f"TC_Notifier_088 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_FRAUDE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(self):
        try:
            self.logger.info("*********** TC_Notifier_089 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            camera_1 = Notifier_Read_ini().get_cameras_in_region_by_xpath_1()
            camera_2 = Notifier_Read_ini().get_cameras_in_region_by_xpath_2()
            checkbox_1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox_2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, camera_1 + Notifier_Read_ini().get_camera0() + camera_2 + checkbox_1 +
                                           Notifier_Read_ini().get_camera1() + checkbox_2)
            checkbox.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Camera selected as: {Notifier_Read_ini().get_camera0()}")
            time.sleep(web_driver.one_second)
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            # self.select_SOE_group_from_ini()
            self.select_FRAUDE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_089.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_089.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_089_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_089_exception.png")
            self.logger.error(f"TC_Notifier_089 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_VIPE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(
            self):
        try:
            self.logger.info("*********** TC_Notifier_90 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.logger.info("executed load_notifier_module")
            self.get_region_and_group_data()
            self.logger.info("executed get_region_and_group_data")

            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                 get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.two_second)
            camera_1 = Notifier_Read_ini().get_cameras_in_region_by_xpath_1()
            camera_2 = Notifier_Read_ini().get_cameras_in_region_by_xpath_2()
            checkbox_1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox_2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, camera_1 + Notifier_Read_ini().get_camera0() + camera_2 + checkbox_1 +
                                           Notifier_Read_ini().get_camera1() + checkbox_2)
            checkbox.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Camera selected as: {Notifier_Read_ini().get_camera0()}")
            time.sleep(web_driver.one_second)
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                   get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            self.select_VIPE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.two_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_90.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_102.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_90_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_90_exception.png")
            self.logger.error(f"TC_Notifier_90 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_SOE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF(
            self):
        try:
            self.logger.info("*********** TC_Notifier_91 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.logger.info("executed load_notifier_module")
            self.get_region_and_group_data()
            self.logger.info("executed get_region_and_group_data")

            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.two_second)
            expand_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().get_expand_all_button_on_region_selection_panel_by_xpath())
            expand_all_btn.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_unselect_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            camera_1 = Notifier_Read_ini().get_cameras_in_region_by_xpath_1()
            camera_2 = Notifier_Read_ini().get_cameras_in_region_by_xpath_2()
            checkbox_1 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_1()
            checkbox_2 = Notifier_Read_ini().get_checkbox_in_region_by_xpath_2()
            checkbox = self.d.find_element(By.XPATH, camera_1 + Notifier_Read_ini().get_camera0() + camera_2 + checkbox_1 +
                                           Notifier_Read_ini().get_camera1() + checkbox_2)
            checkbox.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"Camera selected as: {Notifier_Read_ini().get_camera0()}")
            time.sleep(web_driver.one_second)
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                   get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            self.select_SOE_group_from_ini()
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            self.get_default_notifier_setting_values()
            self.notifier_result_verification()

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_91.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_91.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_91_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_91_exception.png")
            self.logger.error(f"TC_Notifier_91 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_Notifier_result_for_root_region_selected_with_refresh_rate_10_sec_probable_match_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_ON(self):
        try:
            self.logger.info("*********** TC_Notifier_92 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.load_notifier_module()
            self.get_region_and_group_data()

            # org_hierarchy_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath())
            org_hierarchy_selection_button = web_driver.explicit_wait(self, 10, "XPATH", Notifier_Read_ini().get_org_hierarchy_selection_button_by_xpath(), self.d)
            org_hierarchy_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().
                                get_select_all_button_on_region_selection_panel_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.logger.info("All cameras of regions are selected....")
            collapse_all_btn = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                   get_collapse_all_button_on_region_selection_panel_by_xpath())
            collapse_all_btn.click()
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Notifier_Read_ini().get_save_button_on_org_hierarchy_panel_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            time.sleep(web_driver.one_second)
            enrollment_group_selection_button = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                                    get_enrollment_group_selection_button_by_xpath())
            enrollment_group_selection_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_clear_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_select_a_group_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            notifier_setting = self.d.find_element(By.XPATH, Notifier_Read_ini().get_notifier_setting_button_by_xpath())
            notifier_setting.click()
            time.sleep(web_driver.one_second)
            refresh_rate = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_refresh_rate_dropdown_by_xpath()))
            refresh_rate.select_by_visible_text(self.refresh_rate[7])
            self.logger.info(f"Refresh Rate: {self.refresh_rate[7]}")
            events_display = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                        get_events_display_dropdown_by_xpath()))
            events_display.select_by_visible_text(str(self.events_displayed[1]))
            self.logger.info(f"Events Displayed: {str(self.events_displayed[1])}")
            photo_size = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().get_photo_size_dropdown_by_xpath()))
            photo_size.select_by_visible_text(self.photo_size[2])
            self.logger.info(f"Photo Size: {self.photo_size[2]}")
            sound_option = Select(self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                      get_sound_option_dropdown_by_xpath()))
            sound_option.select_by_visible_text(self.sound_option[1])
            self.logger.info(f"Sound Option: {self.sound_option[1]}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Notifier_Read_ini().get_save_button_on_notifier_setting_panel_by_xpath()).\
                click()
            time.sleep(web_driver.one_second)
            updating_status = self.d.find_elements(By.XPATH, Notifier_Read_ini().
                                                   get_updating_text_on_notifier_panel_by_xpath())
            updating_status_element = self.d.find_element(By.XPATH, Notifier_Read_ini().
                                                          get_updating_text_on_notifier_panel_by_xpath())
            t = 10
            c = 0
            if len(updating_status) == 0:
                while t > 0:
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass
                self.logger.info(f"1Refreshing page after {c} seconds..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass
            elif len(updating_status) > 0:
                while t > 0:
                    t = t - 1
                    c = c + 1
                    # if updating_status_element.is_displayed():
                    #     self.status.append(False)
                    # else:
                    #     pass

                self.logger.info(f"2Refreshing page after {c} seconds..")
                if updating_status_element.is_displayed():
                    self.status.append(True)
                else:
                    pass

            self.notifier_result_verification_for_all_groups_selected()
            time.sleep(web_driver.one_second)

            close_all_panels = self.d.find_elements(By.XPATH, Notifier_Read_ini().get_close_panel_buttons_by_xpath())
            for btn in close_all_panels:
                btn.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_92.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_92.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_92_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_92_exception.png")
            self.logger.error(f"TC_Notifier_92 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_notifier_panel_should_display_LOCATION_with_valid_name(self):
        try:
            self.logger.info("*********** TC_Notifier_95 started **********")
            self.logger.info("TC_Notifier_verifying_Location_data")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            self.load_notifier_module()
            time.sleep(web_driver.two_second)
            Location_and_location_name = self.d.find_element(By.XPATH, Notifier_Read_ini().get_Location_Name())
            if Location_and_location_name.is_displayed():
                self.logger.info(f"LOCATION: {self.d.find_element(By.XPATH, Notifier_Read_ini().get_location_data()).text}")
                self.status.append(True)
            else:
                self.logger.info("Location and its name is not visible")
                self.status.append(False)

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_95.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_95.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_95.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_95_exception.png")
            self.logger.error(f"TC_Notifier_95 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_notifier_panel_should_display_CAMERA_with_valid_data(self):
        try:
            self.logger.info("*********** TC_Notifier_96 started **********")
            self.logger.info("TC_Notifier_verifying_Location_data")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            self.load_notifier_module()
            time.sleep(web_driver.two_second)
            camera_and_camera_name = self.d.find_element(By.XPATH,Notifier_Read_ini().get_station_camera_name())
            if camera_and_camera_name.is_displayed():
                self.logger.info(f"Camera: {self.d.find_element(By.XPATH, Notifier_Read_ini().get_station_camera_data()).text}")
                self.status.append(True)
            else:
                self.logger.info("camera and camera name is not visible")
                self.status.append(False)

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_96.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_96.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_96_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_96_exception.png")
            self.logger.error(f"TC_Notifier_96 name got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_notifier_panel_should_display_ENROLLMENT_NUMBER_with_valid_data(self):
        try:
            self.logger.info("*********** TC_Notifier_97 started **********")
            self.logger.info("TC_Notifier_verifying_Enrollment_Number_data")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            self.load_notifier_module()
            time.sleep(web_driver.two_second)
            enrollment_number = self.d.find_element(By.XPATH,Notifier_Read_ini().get_enrollment_number())
            if enrollment_number.is_displayed():
                self.logger.info(f"Enrollment Number: {self.d.find_element(By.XPATH, Notifier_Read_ini().get_enrollment_number_data()).text}")
                self.status.append(True)
            else:
                self.logger.info("Enrollment Number and Enrollment Number data is not visible")
                self.status.append(False)

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_97.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_97.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_97_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_97_exception.png")
            self.logger.error(f"TC_Notifier_97 name got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_notifier_panel_should_display_ACTION_with_valid_data(self):
        try:
            self.logger.info("*********** TC_Notifier_98 started **********")
            self.logger.info("TC_Notifier_verifying_Location_data")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            self.load_notifier_module()
            time.sleep(web_driver.two_second)
            action_and_action_details = self.d.find_element(By.XPATH,Notifier_Read_ini().get_Action())
            if action_and_action_details.is_displayed():
                self.logger.info(f"Action: {self.d.find_element(By.XPATH, Notifier_Read_ini().get_Action_data()).text}")
                self.status.append(True)
            else:
                self.logger.info("action and action details is not visible")
                self.status.append(False)

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_98.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_98.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Notifier_98_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_98_exception.png")
            self.logger.error(f"TC_Notifier_98 got exception as: {ex}")
        finally:
            self.close_notifier_module()

    def Verify_notifier_panel_should_display_INDEX_SCORE_with_valid_data(self):
        try:
            self.logger.info("*********** TC_Notifier_100 started **********")
            self.logger.info("TC_Notifier_verifying_Location_data")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            self.load_notifier_module()
            time.sleep(web_driver.two_second)
            index_and_score = self.d.find_element(By.XPATH, Notifier_Read_ini().get_Action())
            if index_and_score.is_displayed():
                self.logger.info(f"Index Score: {self.d.find_element(By.XPATH, Notifier_Read_ini().get_Index_data()).text}")
                self.status.append(True)
            else:
                self.logger.info("index and score is not visible")
                self.status.append(False)

            if False in self.status:
                self.logger.error(
                    f"screenshot file path: {self.screenshots_path}\\TC_Notifier_100.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_100.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(
                f"screenshot file path: {self.screenshots_path}\\TC_Notifier_100_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Notifier_100_exception.png")
            self.logger.error(f"TC_Notifier_100 got exception as: {ex}")
        finally:
            self.close_notifier_module()






