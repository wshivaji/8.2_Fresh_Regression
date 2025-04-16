import time
from pathlib import Path
import numpy as np
import pandas as pd

from All_Config_Packages._4_Users_Module_Config_Files.Users_Read_INI import Read_Users_Components
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from selenium.webdriver.common.by import By
from All_Config_Packages._3_User_Roles_Module_Config_Files.User_Roles_Read_Ini import user_roles_read_ini
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import Portal_Menu_Module_read_ini
from All_Config_Packages._0_login_logout_config_file.login_logout_read_ini import LoginLogout_Read_ini
from All_Config_Packages._6_Notification_Groups_Module_Config_Files.Notification_Groups_Read_INI import Read_Notification_Groups_Components
from Base_Package.Login_Logout_Ops import login, logout
from All_Other_Utility_Packages._3_User_Roles_Module.Read_Excel import Read_excel
from All_POM_Packages._4_Users_Module_POM.Users_Module_POM import Users_Module_pom


class user_roles_module_pom(web_driver, web_logger):
    status = []
    d = web_driver.d()
    logger = web_logger.logger_obj()
    user_details = None
    so_user = fraud_user = pt_user = vip_user = None
    user_roles_and_authentication_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\3_User_Roles_Module\\Data_From_CSV\\user_roles_and_authentications.csv"
    users_and_authentication_xlsx = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\3_User_Roles_Module\\Data_From_Excel\\Users_and_authentications_xlsx.xlsx"

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

    def get_user_roles_and_authentication_lists(self):
        try:
            df_so = pd.read_excel(self.users_and_authentication_xlsx, sheet_name='SO_User_Role_Auto_Test', names=['Authentication', 'Create', 'Read', 'Edit', 'Delete'])
            df_fraud = pd.read_excel(self.users_and_authentication_xlsx, sheet_name='Fraud_User_Role_Auto_Test', names=['Authentication', 'Create', 'Read', 'Edit', 'Delete'])
            df_pt = pd.read_excel(self.users_and_authentication_xlsx, sheet_name='PT_User_Role_Auto_Test', names=['Authentication', 'Create', 'Read', 'Edit', 'Delete'])
            df_vip = pd.read_excel(self.users_and_authentication_xlsx, sheet_name='VIP_User_Role_Auto_Test', names=['Authentication', 'Create', 'Read', 'Edit', 'Delete'])
            self.so_user = [{x: y} for x, y in zip(df_so['Authentication'], [[a, b, c, d] for a, b, c, d in zip(df_so['Create'], df_so['Read'], df_so['Edit'], df_so['Delete'])])]
            self.fraud_user = [{x: y} for x, y in zip(df_fraud['Authentication'], [[a, b, c, d] for a, b, c, d in zip(df_fraud['Create'], df_fraud['Read'], df_fraud['Edit'], df_fraud['Delete'])])]
            self.pt_user = [{x: y} for x, y in zip(df_pt['Authentication'], [[a, b, c, d] for a, b, c, d in zip(df_pt['Create'], df_pt['Read'], df_pt['Edit'], df_pt['Delete'])])]
            self.vip_user = [{x: y} for x, y in zip(df_vip['Authentication'], [[a, b, c, d] for a, b, c, d in zip(df_vip['Create'], df_vip['Read'], df_vip['Edit'], df_vip['Delete'])])]
            print('SO User List: ', self.so_user, 'Fraud User List: ', self.fraud_user, 'PT User List: ', self.pt_user, 'VIP User List: ', self.vip_user)
            ff_user_list = pd.read_excel(self.users_and_authentication_xlsx, sheet_name="Users", names=['username', 'first_name', 'last_name', 'password', 'email', 'role_name'])
            self.user_details = [{x: y} for x, y in zip(ff_user_list['username'], [[a, b, c, d, e] for a, b, c, d, e in zip(ff_user_list['first_name'], ff_user_list['last_name'], ff_user_list['password'], ff_user_list['email'], ff_user_list['role_name'])])]
            print(f'ff_user_list:{ff_user_list}list: {self.user_details}')
        except Exception as ex:
            self.logger.info(ex.args)

    def close_all_panel(self):
        try:
            time.sleep(web_driver.two_second)
            try:
                alert = self.d.switch_to_alert
                alert.accept()
            except Exception as ex:
                print("no alert")

            cloud_menu = self.d.find_element(By.XPATH, user_roles_read_ini().get_cloud_menu_by_xpath())
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            close_panel = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_close_all_panels_menu_by_xpath())
            if close_panel.is_displayed():
                close_panel.click()
                time.sleep(web_driver.one_second)
            else:
                cloud_menu.click()
                time.sleep(web_driver.one_second)

            try:
                alert = self.d.switch_to_alert
                alert.accept()
                time.sleep(web_driver.one_second)
            except Exception as ex:
                print("no alert")
        except Exception as ex:
            self.logger.info(f"exception in closing panel: {ex}")
            return False

    def verify_user_roles_panel_heading_and_action_dropdown_is_visible_and_clickable(self):
        try:
            self.logger.info("********** Test_TC_UR_01 Begin  **********")
            status = []
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)

            actual_user_roles_menu_item = self.explicit_wait(10, "XPATH", user_roles_read_ini().get_user_role_menu_item_by_xpath(), self.d)
            actual_user_roles_menu_item.click()
            time.sleep(web_driver.one_second)
            actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
            cloud_menu = self.d.find_element(By.XPATH, user_roles_read_ini().get_cloud_menu_by_xpath())
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            user_roles_panel_title_by_xpath_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_panel_title_by_xpath())
            if len(user_roles_panel_title_by_xpath_list) > 0:
                self.logger.info(f"user roles panel is opened...{user_roles_panel_title_by_xpath_list[0].text}")
                status.append(True)
                action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                self.logger.info(f"action dropdown: {action_drop_down.text}")
                if action_drop_down.is_displayed():
                    status.append(True)
                else:
                    status.append(False)
                if action_drop_down.text == user_roles_read_ini().get_action_dropdown_text():
                    status.append(True)
                else:
                    status.append(False)
            else:
                if len(actual_user_roles_menu_item_list) > 0:
                    self.logger.info(f"user roles menu item is visible...")
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    if action_drop_down.is_displayed():
                        status.append(True)
                    else:
                        status.append(False)
                    if action_drop_down.text == user_roles_read_ini().get_action_dropdown_text():
                        status.append(True)
                    else:
                        status.append(False)
                    if action_drop_down.is_enabled():
                        status.append(True)
                    else:
                        status.append(False)
                else:
                    self.logger.info(f"user roles menu item is not visible...")
                    cloud_menu = self.d.find_element(By.XPATH, user_roles_read_ini().get_cloud_menu_by_xpath())
                    cloud_menu.click()
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    if action_drop_down.is_displayed():
                        status.append(True)
                    else:
                        status.append(False)
                    if action_drop_down.text == user_roles_read_ini().get_action_dropdown_text():
                        status.append(True)
                    else:
                        status.append(False)
                    if action_drop_down.is_enabled():
                        status.append(True)
                    else:
                        status.append(False)
            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_01 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_01.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_01.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_01_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_01_exception.png")
            self.logger.error(f"TC_UR_01 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def verify_action_dropdown_is_clickable_click_on_action_drop_down_and_verify_options_inside_drop_down_are_visible_and_clickable(self):
        try:
            self.logger.info("********** Test_TC_UR_02 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
            cloud_menu = self.d.find_element(By.XPATH, user_roles_read_ini().get_cloud_menu_by_xpath())
            time.sleep(web_driver.one_second)
            user_roles_panel_title_by_xpath_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_panel_title_by_xpath())
            if len(user_roles_panel_title_by_xpath_list) > 0:
                self.logger.info(f"user roles panel is opened...{user_roles_panel_title_by_xpath_list[0].text}")
                status.append(True)
                action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                time.sleep(web_driver.one_second)
                self.logger.info(f"action dropdown: {action_drop_down.text}")
                if action_drop_down.is_displayed():
                    status.append(True)
                else:
                    status.append(False)
                if action_drop_down.text == user_roles_read_ini().get_action_dropdown_text():
                    status.append(True)
                else:
                    status.append(False)
                action_drop_down.click()
                time.sleep(web_driver.one_second)
                options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                time.sleep(web_driver.one_second)
                if len(options_inside_action_dropdown) > 0:
                    self.logger.info("action dropdown contains options...")
                    for x in range(len(options_inside_action_dropdown)):
                        option = options_inside_action_dropdown[x]
                        self.logger.info(f"option: {option.text}")
                        if option.is_displayed():
                            status.append(True)
                        else:
                            status.append(False)
                        if option.is_enabled():
                            status.append(True)
                        else:
                            status.append(False)
            else:
                if len(actual_user_roles_menu_item_list) > 0:
                    self.logger.info(f"user roles menu item is visible...")
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    if action_drop_down.is_displayed():
                        status.append(True)
                    else:
                        status.append(False)
                    if action_drop_down.text == user_roles_read_ini().get_action_dropdown_text():
                        status.append(True)
                    else:
                        status.append(False)
                    if action_drop_down.is_enabled():
                        status.append(True)
                    else:
                        status.append(False)
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for x in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[x]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                else:
                    self.logger.info(f"user roles menu item is not visible...")
                    cloud_menu = self.d.find_element(By.XPATH, user_roles_read_ini().get_cloud_menu_by_xpath())
                    cloud_menu.click()
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH,  user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for x in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[x]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, user_roles_read_ini().get_panel_container_outside_click_by_xpath()).click()
            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_02 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_02.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_02.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_02_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_02_exception.png")
            self.logger.error(f"TC_UR_02 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def verify_select_all_label_and_one_check_box_besides_it_is_visible_and_clickable(self):
        try:
            self.logger.info("********** Test_TC_UR_03 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
            cloud_menu = self.d.find_element(By.XPATH, user_roles_read_ini().get_cloud_menu_by_xpath())
            time.sleep(web_driver.one_second)
            user_roles_panel_title_by_xpath_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_panel_title_by_xpath())
            if len(user_roles_panel_title_by_xpath_list) > 0:
                self.logger.info(f"user roles panel is opened...{user_roles_panel_title_by_xpath_list[0].text}")
                status.append(True)
                time.sleep(web_driver.one_second)
                actual_select_all_label = self.d.find_element(By.XPATH, user_roles_read_ini().get_select_all_label_by_xpath())
                expected_select_all_label = user_roles_read_ini().get_select_all_label()
                time.sleep(web_driver.one_second)
                select_all_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_select_all_check_box_by_xpath())
                self.logger.info(f"actual: {actual_select_all_label.text}, \n expected: {expected_select_all_label}")
                self.logger.info(f"select check box visible: {select_all_check_box.is_displayed()}")
                if actual_select_all_label.text == expected_select_all_label:
                    status.append(True)
                else:
                    status.append(False)
                if actual_select_all_label.is_displayed():
                    status.append(True)
                else:
                    status.append(False)
                if select_all_check_box.is_displayed():
                    status.append(True)
                else:
                    status.append(False)
                if select_all_check_box.is_enabled():
                    status.append(True)
                else:
                    status.append(False)
            else:
                if len(actual_user_roles_menu_item_list) > 0:
                    self.logger.info(f"user roles menu item is visible...")
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    actual_select_all_label = self.d.find_element(By.XPATH, user_roles_read_ini().get_select_all_label_by_xpath())
                    expected_select_all_label = user_roles_read_ini().get_select_all_label()
                    time.sleep(web_driver.one_second)
                    select_all_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_select_all_check_box_by_xpath())
                    self.logger.info(f"actual: {actual_select_all_label.text}, \nexpected: {expected_select_all_label}")
                    self.logger.info(f"select check box visible: {select_all_check_box.is_displayed()}")
                    if actual_select_all_label.text == expected_select_all_label:
                        status.append(True)
                    else:
                        status.append(False)
                    if actual_select_all_label.is_displayed():
                        status.append(True)
                    else:
                        status.append(False)
                    if select_all_check_box.is_displayed():
                        status.append(True)
                    else:
                        status.append(False)
                    if select_all_check_box.is_enabled():
                        status.append(True)
                    else:
                        status.append(False)
                else:
                    self.logger.info(f"user roles menu item is not visible...")
                    time.sleep(web_driver.one_second)
                    cloud_menu = self.d.find_element(By.XPATH, user_roles_read_ini().get_cloud_menu_by_xpath())
                    cloud_menu.click()
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    actual_select_all_label = self.d.find_element(By.XPATH, user_roles_read_ini().get_select_all_label_by_xpath())
                    expected_select_all_label = user_roles_read_ini().get_select_all_label()
                    time.sleep(web_driver.one_second)
                    select_all_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_select_all_check_box_by_xpath())
                    self.logger.info(f"actual: {actual_select_all_label.text}, \nexpected: {expected_select_all_label}")
                    self.logger.info(f"select check box visible: {select_all_check_box.is_displayed()}")
                    if actual_select_all_label.text == expected_select_all_label:
                        status.append(True)
                    else:
                        status.append(False)
                    if actual_select_all_label.is_displayed():
                        status.append(True)
                    else:
                        status.append(False)
                    if select_all_check_box.is_displayed():
                        status.append(True)
                    else:
                        status.append(False)
                    if select_all_check_box.is_enabled():
                        status.append(True)
                    else:
                        status.append(False)
            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_03 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_03.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_03.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_03_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_03_exception.png")
            self.logger.error(f"TC_UR_03 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def verify_user_role_profiles_inside_user_roles_panel_are_enlisted_and_are_visible(self):
        try:
            self.logger.info("********** Test_TC_UR_04 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
            cloud_menu = self.d.find_element(By.XPATH, user_roles_read_ini().get_cloud_menu_by_xpath())
            time.sleep(web_driver.one_second)
            user_roles_panel_title_by_xpath_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_panel_title_by_xpath())

            if len(user_roles_panel_title_by_xpath_list) > 0:
                self.logger.info(f"user roles panel is opened...{user_roles_panel_title_by_xpath_list[0].text}")
                status.append(True)
                # -------------------------------- #
                time.sleep(web_driver.one_second)
                user_roles_profiles_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_list_by_xpath())
                time.sleep(web_driver.one_second)
                user_roles_profiles_name_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_name_list_by_xpath())
                for user in user_roles_profiles_list:
                    self.logger.info(f"User Role: {user.text}")
                    if user.is_displayed():
                        status.append(True)
                    else:
                        status.append(False)
                    if user.is_enabled():
                        status.append(True)
                for user in user_roles_profiles_name_list:
                    self.logger.info(f"User Role Name:  {user.text}")
                    if user.is_displayed():
                        status.append(True)
                    else:
                        status.append(False)
                    if user.is_enabled():
                        status.append(True)
                    else:
                        status.append(False)
            else:
                if len(actual_user_roles_menu_item_list) > 0:
                    self.logger.info(f"user roles menu item is visible...")
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    # --------------------------------
                    time.sleep(web_driver.one_second)
                    user_roles_profiles_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_list_by_xpath())
                    user_roles_profiles_name_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_name_list_by_xpath())
                    for user in user_roles_profiles_list:
                        self.logger.info(f"User Role: {user.text}")
                        if user.is_displayed():
                            status.append(True)
                        else:
                            status.append(False)
                        if user.is_enabled():
                            status.append(True)
                    for user in user_roles_profiles_name_list:
                        self.logger.info(f"User Role Name:  {user.text}")
                        if user.is_displayed():
                            status.append(True)
                        else:
                            status.append(False)
                        if user.is_enabled():
                            status.append(True)
                        else:
                            status.append(False)
                else:
                    self.logger.info(f"user roles menu item is not visible...")
                    time.sleep(web_driver.one_second)
                    cloud_menu = self.d.find_element(By.XPATH, user_roles_read_ini().get_cloud_menu_by_xpath())
                    cloud_menu.click()
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    # --------------------------------
                    time.sleep(web_driver.one_second)
                    user_roles_profiles_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_list_by_xpath())
                    time.sleep(web_driver.one_second)
                    user_roles_profiles_name_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_name_list_by_xpath())
                    for user in user_roles_profiles_list:
                        self.logger.info(f"User Role: {user.text}")
                        if user.is_displayed():
                            status.append(True)
                        else:
                            status.append(False)
                        if user.is_enabled():
                            status.append(True)
                    for user in user_roles_profiles_name_list:
                        self.logger.info(f"User Role Name:  {user.text}")
                        if user.is_displayed():
                            status.append(True)
                        else:
                            status.append(False)
                        if user.is_enabled():
                            status.append(True)
                        else:
                            status.append(False)
            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_04 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_04.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_04.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_04_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_04_exception.png")
            self.logger.error(f"TC_UR_04 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def click_on_action_dropdown_on_user_roles_panel_verify_all_options_are_visible_serach_for_create_user_role_click_on_it_and_verify_a_new_panel_user_role_is_visible(self):
        try:
            self.logger.info("********** Test_TC_UR_05 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
            cloud_menu = self.d.find_element(By.XPATH, user_roles_read_ini().get_cloud_menu_by_xpath())
            time.sleep(web_driver.one_second)
            user_roles_panel_title_by_xpath_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_panel_title_by_xpath())
            if len(user_roles_panel_title_by_xpath_list) > 0:
                self.logger.info(f"user roles panel is opened...{user_roles_panel_title_by_xpath_list[0].text}")
                status.append(True)
                time.sleep(web_driver.one_second)
                action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                self.logger.info(f"action dropdown: {action_drop_down.text}")
                if action_drop_down.is_displayed():
                    status.append(True)
                else:
                    status.append(False)
                if action_drop_down.text == user_roles_read_ini().get_action_dropdown_text():
                    status.append(True)
                else:
                    status.append(False)
                action_drop_down.click()
                time.sleep(web_driver.one_second)
                options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                if len(options_inside_action_dropdown) > 0:
                    self.logger.info("action dropdown contains options...")
                    for x in range(len(options_inside_action_dropdown)):
                        option = options_inside_action_dropdown[x]
                        self.logger.info(f"option: {option.text}")
                        if option.is_displayed():
                            status.append(True)
                        else:
                            status.append(False)
                        if option.is_enabled():
                            status.append(True)
                        else:
                            status.append(False)
                        if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                            self.logger.info(f"Option Name Selected: {option.text}")
                            option.click()
                            break
                time.sleep(web_driver.one_second)
                panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
                if len(panels_opened_list) > 0:
                    self.logger.info(f"Panels are opened...")
                    for x in range(len(panels_opened_list)):
                        user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                        if len(user_role_panel_title_list) > 0:
                            self.logger.info(f"Panel Heading: {user_role_panel_title_list[0].text}")
                            if user_role_panel_title_list[0].text == user_roles_read_ini().get_user_role_panel_title_text():
                                status.append(True)
                            else:
                                status.append(False)
            else:
                if len(actual_user_roles_menu_item_list) > 0:
                    self.logger.info(f"user roles menu item is visible...")
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    if action_drop_down.is_displayed():
                        status.append(True)
                    else:
                        status.append(False)
                    if action_drop_down.text == user_roles_read_ini().get_action_dropdown_text():
                        status.append(True)
                    else:
                        status.append(False)
                    if action_drop_down.is_enabled():
                        status.append(True)
                    else:
                        status.append(False)
                    time.sleep(web_driver.one_second)
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for x in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[x]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                break
                        time.sleep(web_driver.one_second)
                        panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
                        if len(panels_opened_list) > 0:
                            self.logger.info(f"Panels are opened...")
                            for x in range(len(panels_opened_list)):
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    self.logger.info(f"Panel Heading: {user_role_panel_title_list[0].text}")
                                    if user_role_panel_title_list[0].text == user_roles_read_ini().get_user_role_panel_title_text():
                                        status.append(True)
                                    else:
                                        status.append(False)
                else:
                    self.logger.info(f"user roles menu item is not visible...")
                    time.sleep(web_driver.one_second)
                    cloud_menu = self.d.find_element(By.XPATH, user_roles_read_ini().get_cloud_menu_by_xpath())
                    cloud_menu.click()
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for x in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[x]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                break
                        time.sleep(web_driver.one_second)
                        panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
                        if len(panels_opened_list) > 0:
                            self.logger.info(f"Panels are opened...")
                            for x in range(len(panels_opened_list)):
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    self.logger.info(f"Panel Heading: {user_role_panel_title_list[0].text}")
                                    if user_role_panel_title_list[0].text == user_roles_read_ini().get_user_role_panel_title_text():
                                        status.append(True)
                                    else:
                                        status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, user_roles_read_ini().get_panel_container_outside_click_by_xpath()).click()
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())

            for i in range(len(panels_opened_list)):
                time.sleep(web_driver.one_second)
                self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath()).click()
                time.sleep(web_driver.one_second)

            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_05 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_05.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_05.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_05_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_05_exception.png")
            self.logger.error(f"TC_UR_05 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def go_to_user_role_panel_and_verify_panel_heading_as_User_Role_Is_visible_below_it_cancle_save_btn_is_visible_and_clickable(self):
        try:
            self.logger.info("********** Test_TC_UR_06 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            if len(panels_opened_list) > 0:
                self.logger.info(f"Panels are opened...")
                for y in range(len(panels_opened_list)):
                    user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                    if len(user_role_panel_title_list) > 0:
                        for x in range(len(user_role_panel_title_list)):
                            self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                            if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                status.append(True)
                                # --------------------------------------- #
                                time.sleep(web_driver.one_second)
                                cancel_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_cancel_btn_by_xpath())
                                time.sleep(web_driver.one_second)
                                save_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_save_btn_by_xpath())
                                if cancel_btn.is_displayed():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if cancel_btn.is_enabled():
                                    status.append(True)
                                else:
                                    status.append(False)

                                if save_btn.is_displayed():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if save_btn.is_enabled():
                                    status.append(True)
                                else:
                                    status.append(False)
                                # -----------------------------------

                            else:
                                self.logger.info("Panel is not opened...")
                                status.append(False)

            else:
                self.logger.info(f"panel not opened...")
                time.sleep(web_driver.one_second)
                actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                if len(actual_user_roles_menu_item_list) > 0:
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for y in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[y]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    for x in range(len(user_role_panel_title_list)):
                                        self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                        if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                            self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                            status.append(True)
                                            # ---------------------------------------- #
                                            time.sleep(web_driver.one_second)
                                            cancel_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_cancel_btn_by_xpath())
                                            time.sleep(web_driver.one_second)
                                            save_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_save_btn_by_xpath())
                                            if cancel_btn.is_displayed():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if cancel_btn.is_enabled():
                                                status.append(True)
                                            else:
                                                status.append(False)

                                            if save_btn.is_displayed():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if save_btn.is_enabled():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            # ------------------------------------------- #
                                        else:
                                            self.logger.info("Panel is not opened...")
                                            status.append(False)
                                break

            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_06 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_06.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_06.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_06_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_06_exception.png")
            self.logger.error(f"TC_UR_06 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def verify_heading_as_New_User_Role_Details_is_visible_along_with_its_symbol(self):
        try:
            self.logger.info("********** Test_TC_UR_07 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            if len(panels_opened_list) > 0:
                self.logger.info(f"Panels are opened...")
                for y in range(len(panels_opened_list)):
                    time.sleep(web_driver.one_second)
                    user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                    if len(user_role_panel_title_list) > 0:
                        for x in range(len(user_role_panel_title_list)):
                            self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                            if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                status.append(True)
                                # --------------------------------------- #
                                time.sleep(web_driver.one_second)
                                actual_new_heading_text = self.d.find_element(By.XPATH, user_roles_read_ini().get_new_in_heading_by_xpath())
                                expected_new_heading_text = user_roles_read_ini().get_new_in_heading_text()
                                time.sleep(web_driver.one_second)
                                actual_user_role_details_text = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_details_in_heading_by_xpath())
                                expected_user_role_details_text = user_roles_read_ini().get_user_role_details_in_heading()
                                time.sleep(web_driver.one_second)
                                icon_heading = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_details_logo_symbol_by_xpath())
                                self.logger.info(f"actual New text: {actual_new_heading_text.text}, \nexpected New text: {expected_new_heading_text}")
                                self.logger.info(f"actual user role details text: {actual_user_role_details_text.text}, \nexpected: {expected_user_role_details_text}")
                                if actual_new_heading_text.is_displayed():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if actual_new_heading_text.text == expected_new_heading_text:
                                    status.append(True)
                                else:
                                    status.append(False)

                                if actual_user_role_details_text.is_displayed():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if actual_user_role_details_text.text == expected_user_role_details_text:
                                    status.append(True)
                                else:
                                    status.append(False)
                                if icon_heading.is_displayed():
                                    status.append(True)
                                else:
                                    status.append(False)

                                # ----------------------------------- #
                            else:
                                self.logger.info("Panel is not opened...")
                                status.append(False)
            else:
                self.logger.info(f"panel not opened...")
                time.sleep(web_driver.one_second)
                actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                if len(actual_user_roles_menu_item_list) > 0:
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for y in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[y]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    for x in range(len(user_role_panel_title_list)):
                                        self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                        if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                            self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                            status.append(True)
                                            # ---------------------------------------- #
                                            time.sleep(web_driver.one_second)
                                            actual_new_heading_text = self.d.find_element(By.XPATH, user_roles_read_ini().get_new_in_heading_by_xpath())
                                            expected_new_heading_text = user_roles_read_ini().get_new_in_heading_text()
                                            time.sleep(web_driver.one_second)
                                            actual_user_role_details_text = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_details_in_heading_by_xpath())
                                            expected_user_role_details_text = user_roles_read_ini().get_user_role_details_in_heading()
                                            time.sleep(web_driver.one_second)
                                            icon_heading = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_details_logo_symbol_by_xpath())
                                            self.logger.info(f"actual New text: {actual_new_heading_text.text}, \nexpected New text: {expected_new_heading_text}")
                                            self.logger.info(f"actual user role details text: {actual_user_role_details_text.text}, \nexpected: {expected_user_role_details_text}")
                                            if actual_new_heading_text.is_displayed():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if actual_new_heading_text.text == expected_new_heading_text:
                                                status.append(True)
                                            else:
                                                status.append(False)

                                            if actual_user_role_details_text.is_displayed():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if actual_user_role_details_text.text == expected_user_role_details_text:
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if icon_heading.is_displayed():
                                                status.append(True)
                                            else:
                                                status.append(False)

                                            # -------------------------------------------
                                        else:
                                            self.logger.info("Panel is not opened...")
                                            status.append(False)
                                break

            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_07 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_07.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_07.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_07_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_07_exception.png")
            self.logger.error(f"TC_UR_07 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def verify_role_name_text_box_and_its_label_is_displayed_and_enabled_below_heading(self):
        try:
            self.logger.info("********** Test_TC_UR_8 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            if len(panels_opened_list) > 0:
                self.logger.info(f"Panels are opened...")
                for y in range(len(panels_opened_list)):
                    time.sleep(web_driver.one_second)
                    user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                    if len(user_role_panel_title_list) > 0:
                        for x in range(len(user_role_panel_title_list)):
                            self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                            if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                status.append(True)
                                # --------------------------------------- #
                                time.sleep(web_driver.one_second)
                                actual_rolename_by_xpath = self.d.find_element(By.XPATH, user_roles_read_ini().get_rolename_label_by_xpath())
                                expected_rolename = user_roles_read_ini().get_rolename_label()
                                time.sleep(web_driver.one_second)
                                rolename_textbox = self.d.find_element(By.XPATH, user_roles_read_ini().get_rolename_textbox_by_xpath())
                                self.logger.info(f"actual: {actual_rolename_by_xpath.text}, \nexpected: {expected_rolename}")

                                if actual_rolename_by_xpath.is_displayed():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if actual_rolename_by_xpath.text == expected_rolename:
                                    status.append(True)
                                else:
                                    status.append(False)
                                if rolename_textbox.is_displayed():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if rolename_textbox.is_enabled():
                                    status.append(True)
                                else:
                                    status.append(False)
                                rolename_textbox.click()

                                # ----------------------------------- #
                            else:
                                self.logger.info("Panel is not opened...")
                                status.append(False)
            else:
                self.logger.info(f"panel not opened...")
                time.sleep(web_driver.one_second)
                actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                if len(actual_user_roles_menu_item_list) > 0:
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for y in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[y]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    for x in range(len(user_role_panel_title_list)):
                                        self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                        if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                            self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                            status.append(True)
                                            # ---------------------------------------- #
                                            time.sleep(web_driver.one_second)
                                            actual_rolename_by_xpath = self.d.find_element(By.XPATH, user_roles_read_ini().get_rolename_label_by_xpath())
                                            expected_rolename = user_roles_read_ini().get_rolename_label()
                                            time.sleep(web_driver.one_second)
                                            rolename_textbox = self.d.find_element(By.XPATH, user_roles_read_ini().get_rolename_textbox_by_xpath())
                                            self.logger.info(f"actual: {actual_rolename_by_xpath.text}, \n expected: {expected_rolename}")

                                            if actual_rolename_by_xpath.is_displayed():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if actual_rolename_by_xpath.text == expected_rolename:
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if rolename_textbox.is_displayed():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if rolename_textbox.is_enabled():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            rolename_textbox.click()
                                            # ------------------------------------------- #
                                        else:
                                            self.logger.info("Panel is not opened...")
                                            status.append(False)
                                break

            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_08 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_8.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_8.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_8_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_8_exception.png")
            self.logger.error(f"TC_UR_8 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def verify_Description_text_box_and_its_label_is_displayed_and_enabled_below_heading(self):
        try:
            self.logger.info("********** Test_TC_UR_9 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            if len(panels_opened_list) > 0:
                self.logger.info(f"Panels are opened...")
                for y in range(len(panels_opened_list)):
                    time.sleep(web_driver.one_second)
                    user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                    if len(user_role_panel_title_list) > 0:
                        for x in range(len(user_role_panel_title_list)):
                            self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                            if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                status.append(True)
                                # --------------------------------------- #
                                time.sleep(web_driver.one_second)
                                actual_description_label = self.d.find_element(By.XPATH, user_roles_read_ini().get_description_label_by_xpath())
                                expected_description_label = user_roles_read_ini().get_description_label()
                                time.sleep(web_driver.one_second)
                                description_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_description_textbox_by_xpath())
                                self.logger.info(f"actual: {actual_description_label.text}, \nexpected: {expected_description_label}")
                                if actual_description_label.is_displayed():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if actual_description_label.text == expected_description_label:
                                    status.append(True)
                                else:
                                    status.append(False)
                                if description_text_box.is_displayed():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if description_text_box.is_enabled():
                                    status.append(True)
                                else:
                                    status.append(False)
                                description_text_box.click()

                                # ----------------------------------- #
                            else:
                                self.logger.info("Panel is not opened...")
                                status.append(False)
            else:
                self.logger.info(f"panel not opened...")
                time.sleep(web_driver.one_second)
                actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                if len(actual_user_roles_menu_item_list) > 0:
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for y in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[y]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    for x in range(len(user_role_panel_title_list)):
                                        self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                        if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                            self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                            status.append(True)
                                            # ---------------------------------------- #
                                            time.sleep(web_driver.one_second)
                                            actual_description_label = self.d.find_element(By.XPATH, user_roles_read_ini().get_description_label_by_xpath())
                                            expected_description_label = user_roles_read_ini().get_description_label()
                                            time.sleep(web_driver.one_second)
                                            description_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_description_textbox_by_xpath())
                                            self.logger.info(f"actual: {actual_description_label.text}, \nexpected: {expected_description_label}")
                                            if actual_description_label.is_displayed():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if actual_description_label.text == expected_description_label:
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if description_text_box.is_displayed():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if description_text_box.is_enabled():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            description_text_box.click()

                                            # ------------------------------------------- #
                                        else:
                                            self.logger.info("Panel is not opened...")
                                            status.append(False)
                                break

            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_09 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_9.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_9.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_9_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_9_exception.png")
            self.logger.error(f"TC_UR_9 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def verify_Disabled_option_btn_and_its_label_is_visible_and_clickable_below_Description_text_box(self):
        try:
            self.logger.info("********** Test_TC_UR_10 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            if len(panels_opened_list) > 0:
                self.logger.info(f"Panels are opened...")
                for y in range(len(panels_opened_list)):
                    time.sleep(web_driver.one_second)
                    user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                    if len(user_role_panel_title_list) > 0:
                        for x in range(len(user_role_panel_title_list)):
                            self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                            if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                status.append(True)
                                # --------------------------------------- #
                                time.sleep(web_driver.one_second)
                                actual_disabled_label = self.d.find_element(By.XPATH, user_roles_read_ini().get_disabled_label_by_xpath())
                                expected_disabled_label = user_roles_read_ini().get_disabled_label()
                                time.sleep(web_driver.one_second)
                                disabled_option_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_disabled_option_btn_by_xpath())
                                self.logger.info(f"actual: {actual_disabled_label.text}, \nexpected: {expected_disabled_label}")
                                if actual_disabled_label.text == expected_disabled_label:
                                    status.append(True)
                                else:
                                    status.append(False)
                                if actual_disabled_label.is_displayed():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if disabled_option_btn.is_displayed():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if disabled_option_btn.is_enabled():
                                    status.append(True)
                                else:
                                    status.append(False)

                                # ----------------------------------- #
                            else:
                                self.logger.info("Panel is not opened...")
                                status.append(False)
            else:
                self.logger.info(f"panel not opened...")
                time.sleep(web_driver.one_second)
                actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                if len(actual_user_roles_menu_item_list) > 0:
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for y in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[y]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    for x in range(len(user_role_panel_title_list)):
                                        self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                        if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                            self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                            status.append(True)
                                            # ---------------------------------------- #
                                            time.sleep(web_driver.one_second)
                                            actual_disabled_label = self.d.find_element(By.XPATH, user_roles_read_ini().get_disabled_label_by_xpath())
                                            expected_disabled_label = user_roles_read_ini().get_disabled_label()
                                            time.sleep(web_driver.one_second)
                                            disabled_option_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_disabled_option_btn_by_xpath())
                                            self.logger.info(f"actual: {actual_disabled_label.text}, \nexpected: {expected_disabled_label}")
                                            if actual_disabled_label.text == expected_disabled_label:
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if actual_disabled_label.is_displayed():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if disabled_option_btn.is_displayed():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if disabled_option_btn.is_enabled():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            # ------------------------------------------- #
                                        else:
                                            self.logger.info("Panel is not opened...")
                                            status.append(False)
                                break

            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_10 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_10.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_10.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_10_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_10_exception.png")
            self.logger.error(f"TC_UR_10 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def verify_Enabled_option_btn_and_its_label_is_visible_and_clickable_below_Description_text_box(self):
        try:
            self.logger.info("********** Test_TC_UR_11 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            if len(panels_opened_list) > 0:
                self.logger.info(f"Panels are opened...")
                for y in range(len(panels_opened_list)):
                    time.sleep(web_driver.one_second)
                    user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                    if len(user_role_panel_title_list) > 0:
                        for x in range(len(user_role_panel_title_list)):
                            self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                            if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                status.append(True)
                                # --------------------------------------- #
                                time.sleep(web_driver.one_second)
                                actual_enabled_label = self.d.find_element(By.XPATH, user_roles_read_ini().get_enabled_label_by_xpath())
                                expected_enabled_label = user_roles_read_ini().get_enabled_label()
                                time.sleep(web_driver.one_second)
                                enabled_option_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_enabled_option_btn_by_xpath())
                                self.logger.info(f"actual: {actual_enabled_label.text}, \nexpected: {expected_enabled_label}")
                                if actual_enabled_label.text == expected_enabled_label:
                                    status.append(True)
                                else:
                                    status.append(False)
                                if actual_enabled_label.is_displayed():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if enabled_option_btn.is_displayed():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if enabled_option_btn.is_enabled():
                                    status.append(True)
                                else:
                                    status.append(False)

                                # ----------------------------------- #
                            else:
                                self.logger.info("Panel is not opened...")
                                status.append(False)
            else:
                self.logger.info(f"panel not opened...")
                actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                if len(actual_user_roles_menu_item_list) > 0:
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for y in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[y]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    for x in range(len(user_role_panel_title_list)):
                                        self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                        if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                            self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                            status.append(True)
                                            # ---------------------------------------- #
                                            time.sleep(web_driver.one_second)
                                            actual_enabled_label = self.d.find_element(By.XPATH, user_roles_read_ini().get_enabled_label_by_xpath())
                                            expected_enabled_label = user_roles_read_ini().get_enabled_label()
                                            time.sleep(web_driver.one_second)
                                            enabled_option_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_enabled_option_btn_by_xpath())
                                            self.logger.info(f"actual: {actual_enabled_label.text}, \nexpected: {expected_enabled_label}")
                                            if actual_enabled_label.text == expected_enabled_label:
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if actual_enabled_label.is_displayed():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if enabled_option_btn.is_displayed():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if enabled_option_btn.is_enabled():
                                                status.append(True)
                                            else:
                                                status.append(False)

                                            # ------------------------------------------- #
                                        else:
                                            self.logger.info("Panel is not opened...")
                                            status.append(False)
                                break

            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_11 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_11.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_11.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_11_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_11_exception.png")
            self.logger.error(f"TC_UR_11 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def verify_Enabled_option_btn_is_selected_by_default_and_tick_mark_is_visible_on_it(self):
        try:
            self.logger.info("********** Test_TC_UR_12 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            if len(panels_opened_list) > 0:
                self.logger.info(f"Panels are opened...")
                for y in range(len(panels_opened_list)):
                    time.sleep(web_driver.one_second)
                    user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                    if len(user_role_panel_title_list) > 0:
                        for x in range(len(user_role_panel_title_list)):
                            self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                            if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                status.append(True)
                                # --------------------------------------- #
                                time.sleep(web_driver.one_second)
                                actual_enabled_label = self.d.find_element(By.XPATH, user_roles_read_ini().get_enabled_label_by_xpath())
                                expected_enabled_label = user_roles_read_ini().get_enabled_label()
                                time.sleep(web_driver.one_second)
                                enabled_option_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_enabled_option_btn_by_xpath())
                                self.logger.info(f"actual: {actual_enabled_label.text}, \nexpected: {expected_enabled_label}")
                                self.logger.info(f"enabled: {enabled_option_btn.get_attribute('class')}")
                                if user_roles_read_ini().get_enabled_disabled_class_text() in enabled_option_btn.get_attribute('class'):
                                    self.logger.info(f"status: {True}")
                                    status.append(True)
                                else:
                                    self.logger.info(f"status: {False}")
                                    status.append(False)
                                time.sleep(web_driver.one_second)
                                self.d.find_element(By.XPATH, user_roles_read_ini().get_disabled_status_input_by_xpath()).click()
                                time.sleep(web_driver.one_second)
                                if user_roles_read_ini().get_enabled_disabled_class_text() in enabled_option_btn.get_attribute('class'):
                                    self.logger.info(f"status: {False}")
                                    status.append(False)
                                else:
                                    self.logger.info(f"status: {True}")
                                    status.append(True)
                                time.sleep(web_driver.one_second)
                                self.d.find_element(By.XPATH, user_roles_read_ini().get_enabled_option_btn_by_xpath()).click()

                                # ----------------------------------- #
                            else:
                                self.logger.info("Panel is not opened...")
                                status.append(False)
            else:
                self.logger.info(f"panel not opened...")
                time.sleep(web_driver.one_second)
                actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                if len(actual_user_roles_menu_item_list) > 0:
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for y in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[y]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    for x in range(len(user_role_panel_title_list)):
                                        self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                        if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                            self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                            status.append(True)
                                            # ---------------------------------------- #
                                            time.sleep(web_driver.one_second)
                                            actual_enabled_label = self.d.find_element(By.XPATH, user_roles_read_ini().get_enabled_label_by_xpath())
                                            expected_enabled_label = user_roles_read_ini().get_enabled_label()
                                            time.sleep(web_driver.one_second)
                                            enabled_option_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_enabled_option_btn_by_xpath())
                                            self.logger.info(f"actual: {actual_enabled_label.text}, \nexpected: {expected_enabled_label}")
                                            self.logger.info(f"enabled: {enabled_option_btn.is_selected()}")
                                            self.logger.info(f"enabled: {enabled_option_btn.get_attribute('class')}")
                                            if user_roles_read_ini().get_enabled_disabled_class_text() in enabled_option_btn.get_attribute('class'):
                                                self.logger.info(f"status: {True}")
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            time.sleep(web_driver.one_second)
                                            self.d.find_element(By.XPATH, user_roles_read_ini().get_disabled_status_input_by_xpath()).click()
                                            time.sleep(web_driver.one_second)
                                            if user_roles_read_ini().get_enabled_disabled_class_text() in enabled_option_btn.get_attribute('class'):
                                                self.logger.info(f"status: {False}")
                                                status.append(False)
                                            else:
                                                self.logger.info(f"status: {True}")
                                                status.append(True)
                                            time.sleep(web_driver.one_second)
                                            self.d.find_element(By.XPATH, user_roles_read_ini().get_enabled_option_btn_by_xpath()).click()

                                            # ------------------------------------------- #
                                        else:
                                            self.logger.info("Panel is not opened...")
                                            status.append(False)
                                break

            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_12 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_12.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_12.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_12_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_12_exception.png")
            self.logger.error(f"TC_UR_12 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def verify_Permissions_label_is_visible_below_enabled_and_disabled_option_btn(self):
        try:
            self.logger.info("********** Test_TC_UR_13 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            if len(panels_opened_list) > 0:
                self.logger.info(f"Panels are opened...")
                for y in range(len(panels_opened_list)):
                    time.sleep(web_driver.one_second)
                    user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                    if len(user_role_panel_title_list) > 0:
                        for x in range(len(user_role_panel_title_list)):
                            self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                            if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                status.append(True)
                                # --------------------------------------- #
                                time.sleep(web_driver.one_second)
                                actual_permissions_label = self.d.find_element(By.XPATH, user_roles_read_ini().get_permissions_label_by_xpath())
                                expected_permission_label = user_roles_read_ini().get_permissions_label()
                                self.logger.info(f"actual: {actual_permissions_label.text}, \n expected: {expected_permission_label}")
                                if actual_permissions_label.is_enabled():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if actual_permissions_label.text == expected_permission_label:
                                    status.append(True)
                                else:
                                    status.append(False)

                                # ----------------------------------- #
                            else:
                                self.logger.info("Panel is not opened...")
                                status.append(False)
            else:
                self.logger.info(f"panel not opened...")
                time.sleep(web_driver.one_second)
                actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                if len(actual_user_roles_menu_item_list) > 0:
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for y in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[y]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    for x in range(len(user_role_panel_title_list)):
                                        self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                        if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                            self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                            status.append(True)
                                            # ---------------------------------------- #
                                            time.sleep(web_driver.one_second)
                                            actual_permissions_label = self.d.find_element(By.XPATH, user_roles_read_ini().get_permissions_label_by_xpath())
                                            expected_permission_label = user_roles_read_ini().get_permissions_label()
                                            self.logger.info(f"actual: {actual_permissions_label.text}, \nexpected: {expected_permission_label}")
                                            if actual_permissions_label.is_enabled():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if actual_permissions_label.text == expected_permission_label:
                                                status.append(True)
                                            else:
                                                status.append(False)

                                            # ------------------------------------------- #
                                        else:
                                            self.logger.info("Panel is not opened...")
                                            status.append(False)
                                break

            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_13 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_13.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_13.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_13_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_13_exception.png")
            self.logger.error(f"TC_UR_13 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def verify_a_table_below_Permissions_label_and_its_content_are_visible_as_expected_along_with_checkbox(self):
        try:
            self.logger.info("********** Test_TC_UR_14 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            if len(panels_opened_list) > 0:
                self.logger.info(f"Panels are opened...")
                for y in range(len(panels_opened_list)):
                    time.sleep(web_driver.one_second)
                    user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                    if len(user_role_panel_title_list) > 0:
                        for x in range(len(user_role_panel_title_list)):
                            self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                            if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                status.append(True)
                                # --------------------------------------- #
                                time.sleep(web_driver.one_second)
                                table_headings_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_table_headings_by_xpath())
                                time.sleep(web_driver.one_second)
                                table_rows_headings_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_table_row_heading_by_xpath())
                                time.sleep(web_driver.one_second)
                                info_symbols_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_info_symbol_besides_table_row_heading_by_xpath())
                                time.sleep(web_driver.one_second)
                                checkboxes_after_table_row_headings_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_checkbox_after_table_row_heading_by_xpath())
                                time.sleep(web_driver.one_second)
                                create_column_checkboxes_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_create_column_checkbox_by_xpath())
                                time.sleep(web_driver.one_second)
                                read_column_checkboxes_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_read_column_checkbox_by_xpath())
                                time.sleep(web_driver.one_second)
                                edit_column_checkboxes_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_edit_column_checkbox_by_xpath())
                                time.sleep(web_driver.one_second)
                                delete_column_checkboxes_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_delete_column_checkbox_by_xpath())
                                time.sleep(web_driver.one_second)
                                for x in range(len(table_headings_list)):
                                    self.logger.info(f"Table Column Heading: {table_headings_list[x].text}")
                                    if table_headings_list[x].is_displayed():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                    if table_headings_list[x].is_enabled():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                for x in range(len(table_rows_headings_list)):
                                    self.logger.info(f"Table Row Heading: {table_rows_headings_list[x].text}")
                                    if table_rows_headings_list[x].is_displayed():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                    if table_rows_headings_list[x].is_enabled():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                for x in range(len(info_symbols_list)):
                                    self.logger.info(f"table row symbol: {info_symbols_list[x].is_displayed()}")
                                    if info_symbols_list[x].is_displayed():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                    if info_symbols_list[x].is_enabled():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                for x in range(len(checkboxes_after_table_row_headings_list)):
                                    self.logger.info(f"check boxes after row heading visible: {checkboxes_after_table_row_headings_list[x].is_displayed()}")
                                    if checkboxes_after_table_row_headings_list[x].is_displayed():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                    if checkboxes_after_table_row_headings_list[x].is_enabled():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                for x in range(len(create_column_checkboxes_list)):
                                    self.logger.info(f"'Create' Column Checkbox visible : {create_column_checkboxes_list[x].is_displayed()}")
                                    if create_column_checkboxes_list[x].is_displayed():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                    if create_column_checkboxes_list[x].is_enabled():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                for x in range(len(read_column_checkboxes_list)):
                                    self.logger.info(f"'Read' column checkbox visible: {read_column_checkboxes_list[x].is_displayed()}")
                                    if read_column_checkboxes_list[x].is_displayed():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                    if read_column_checkboxes_list[x].is_enabled():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                for x in range(len(edit_column_checkboxes_list)):
                                    self.logger.info(f"'Edit' column checkbox visible: {edit_column_checkboxes_list[x].is_displayed()}")
                                    if edit_column_checkboxes_list[x].is_displayed():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                    if edit_column_checkboxes_list[x].is_enabled():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                for x in range(len(delete_column_checkboxes_list)):
                                    self.logger.info(f"'Delete' column checkbox visible: {delete_column_checkboxes_list[x].is_displayed()}")
                                    if delete_column_checkboxes_list[x].is_displayed():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                    if delete_column_checkboxes_list[x].is_enabled():
                                        status.append(True)
                                    else:
                                        status.append(False)
                                # ----------------------------------- #
                            else:
                                self.logger.info("Panel is not opened...")
                                status.append(False)
            else:
                self.logger.info(f"panel not opened...")
                time.sleep(web_driver.one_second)
                actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                if len(actual_user_roles_menu_item_list) > 0:
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for y in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[y]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    for x in range(len(user_role_panel_title_list)):
                                        self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                        if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                            self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                            status.append(True)
                                            # ---------------------------------------- #
                                            time.sleep(web_driver.one_second)
                                            table_headings_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_table_headings_by_xpath())
                                            time.sleep(web_driver.one_second)
                                            table_rows_headings_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_table_row_heading_by_xpath())
                                            time.sleep(web_driver.one_second)
                                            info_symbols_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_info_symbol_besides_table_row_heading_by_xpath())
                                            time.sleep(web_driver.one_second)
                                            checkboxes_after_table_row_headings_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_checkbox_after_table_row_heading_by_xpath())
                                            time.sleep(web_driver.one_second)
                                            create_column_checkboxes_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_create_column_checkbox_by_xpath())
                                            time.sleep(web_driver.one_second)
                                            read_column_checkboxes_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_read_column_checkbox_by_xpath())
                                            time.sleep(web_driver.one_second)
                                            edit_column_checkboxes_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_edit_column_checkbox_by_xpath())
                                            time.sleep(web_driver.one_second)
                                            delete_column_checkboxes_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_delete_column_checkbox_by_xpath())
                                            for x in range(len(table_headings_list)):
                                                self.logger.info(f"Table Column Heading: {table_headings_list[x].text}")
                                                if table_headings_list[x].is_displayed():
                                                    status.append(True)
                                                else:
                                                    status.append(False)
                                                if table_headings_list[x].is_enabled():
                                                    status.append(True)
                                                else:
                                                    status.append(False)
                                            for x in range(len(table_rows_headings_list)):
                                                self.logger.info(f"Table Row Heading: {table_rows_headings_list[x].text}")
                                                if table_rows_headings_list[x].is_displayed():
                                                    status.append(True)
                                                else:
                                                    status.append(False)
                                                if table_rows_headings_list[x].is_enabled():
                                                    status.append(True)
                                                else:
                                                    status.append(False)
                                            for x in range(len(info_symbols_list)):
                                                self.logger.info(f"table row symbol: {info_symbols_list[x].is_displayed()}")
                                                if info_symbols_list[x].is_displayed():
                                                    status.append(True)
                                                else:
                                                    status.append(False)
                                                if info_symbols_list[x].is_enabled():
                                                    status.append(True)
                                                else:
                                                    status.append(False)
                                            for x in range(len(checkboxes_after_table_row_headings_list)):
                                                self.logger.info(f"check boxes after row heading visible: {checkboxes_after_table_row_headings_list[x].is_displayed()}")
                                                if checkboxes_after_table_row_headings_list[x].is_displayed():
                                                    status.append(True)
                                                else:
                                                    status.append(False)
                                                if checkboxes_after_table_row_headings_list[x].is_enabled():
                                                    status.append(True)
                                                else:
                                                    status.append(False)
                                            for x in range(len(create_column_checkboxes_list)):
                                                self.logger.info(f"'Create' Column Checkbox visible : {create_column_checkboxes_list[x].is_displayed()}")
                                                if create_column_checkboxes_list[x].is_displayed():
                                                    status.append(True)
                                                else:
                                                    status.append(False)
                                                if create_column_checkboxes_list[x].is_enabled():
                                                    status.append(True)
                                                else:
                                                    status.append(False)
                                            for x in range(len(read_column_checkboxes_list)):
                                                self.logger.info(f"'Read' column checkbox visible: {read_column_checkboxes_list[x].is_displayed()}")
                                                if read_column_checkboxes_list[x].is_displayed():
                                                    status.append(True)
                                                else:
                                                    status.append(False)
                                                if read_column_checkboxes_list[x].is_enabled():
                                                    status.append(True)
                                                else:
                                                    status.append(False)
                                            for x in range(len(edit_column_checkboxes_list)):
                                                self.logger.info(f"'Edit' column checkbox visible: {edit_column_checkboxes_list[x].is_displayed()}")
                                                if edit_column_checkboxes_list[x].is_displayed():
                                                    status.append(True)
                                                else:
                                                    status.append(False)
                                                if edit_column_checkboxes_list[x].is_enabled():
                                                    status.append(True)
                                                else:
                                                    status.append(False)
                                            for x in range(len(delete_column_checkboxes_list)):
                                                self.logger.info(f"'Delete' column checkbox visible: {delete_column_checkboxes_list[x].is_displayed()}")
                                                if delete_column_checkboxes_list[x].is_displayed():
                                                    status.append(True)
                                                else:
                                                    status.append(False)
                                                if delete_column_checkboxes_list[x].is_enabled():
                                                    status.append(True)
                                                else:
                                                    status.append(False)

                                            # ------------------------------------------- #
                                        else:
                                            self.logger.info("Panel is not opened...")
                                            status.append(False)
                                break

            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_14 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_14.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_14.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_14_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_14_exception.png")
            self.logger.error(f"TC_UR_14 got exception as: {ex.args}")

    def verify_all_check_box_inside_table_are_clickable_by_default_table_column_heading_checkbox_box_and_row_heading_checckbox_are_selected(self):
        try:
            pass
        except Exception as ex:
            self.logger.info(ex.args)

    def enter_so_user_role_insde_user_role_text_box_Serious_Offender_role_in_Description_text_box_and_verify_data_is_entered_successfully(self):
        try:
            self.logger.info("********** Test_TC_UR_16 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            if len(panels_opened_list) > 0:
                self.logger.info(f"Panels are opened...")
                for y in range(len(panels_opened_list)):
                    time.sleep(web_driver.one_second)
                    user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                    if len(user_role_panel_title_list) > 0:
                        for x in range(len(user_role_panel_title_list)):
                            self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                            if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                status.append(True)
                                # --------------------------------------- #
                                time.sleep(web_driver.one_second)
                                role_name_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rolename_text_box_to_enter_data_by_xpath())
                                time.sleep(web_driver.one_second)
                                description_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_description_text_box_to_enter_data_by_xpath())
                                role_name_text_box.click()
                                role_name_text_box.clear()
                                time.sleep(web_driver.one_second)
                                role_name_text_box.send_keys(user_roles_read_ini().get_so_user_role())
                                time.sleep(web_driver.one_second)
                                description_text_box.click()
                                description_text_box.clear()
                                time.sleep(web_driver.one_second)
                                description_text_box.send_keys(user_roles_read_ini().get_so_user_role_description())
                                time.sleep(web_driver.one_second)
                                entered_text = role_name_text_box.get_attribute('value')
                                entered_description = description_text_box.get_attribute('value')
                                self.logger.info(f"entered role: {entered_text}, \nentered description: {entered_description}")
                                if entered_text == user_roles_read_ini().get_so_user_role():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if entered_description == user_roles_read_ini().get_so_user_role_description():
                                    status.append(True)
                                    self.logger.info(f"verify: {True}")
                                else:
                                    self.logger.info(f"verify: {False}")
                                    status.append(False)
                                # ----------------------------------- #
                            else:
                                self.logger.info("Panel is not opened...")
                                status.append(False)
            else:
                self.logger.info(f"panel not opened...")
                time.sleep(web_driver.one_second)
                actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                if len(actual_user_roles_menu_item_list) > 0:
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for y in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[y]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    for x in range(len(user_role_panel_title_list)):
                                        self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                        if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                            self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                            status.append(True)
                                            # ---------------------------------------- #
                                            time.sleep(web_driver.one_second)
                                            role_name_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rolename_text_box_to_enter_data_by_xpath())
                                            time.sleep(web_driver.one_second)
                                            description_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_description_text_box_to_enter_data_by_xpath())

                                            role_name_text_box.click()
                                            role_name_text_box.clear()
                                            time.sleep(web_driver.one_second)
                                            role_name_text_box.send_keys(user_roles_read_ini().get_so_user_role())
                                            time.sleep(web_driver.one_second)
                                            description_text_box.click()
                                            description_text_box.clear()
                                            time.sleep(web_driver.one_second)
                                            description_text_box.send_keys(user_roles_read_ini().get_so_user_role_description())
                                            time.sleep(web_driver.one_second)
                                            entered_text = role_name_text_box.get_attribute('value')
                                            entered_description = description_text_box.get_attribute('value')
                                            self.logger.info(f"entered role: {entered_text}, \nentered description: {entered_description}")
                                            if entered_text == user_roles_read_ini().get_so_user_role():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if entered_description == user_roles_read_ini().get_so_user_role_description():
                                                status.append(True)
                                                self.logger.info(f"verify: {True}")
                                            else:
                                                self.logger.info(f"verify: {False}")
                                                status.append(False)
                                            # ------------------------------------------- #
                                        else:
                                            self.logger.info("Panel is not opened...")
                                            status.append(False)
                                break
            time.sleep(web_driver.one_second)
            user_role_cancel_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_panel_cancel_btn())
            user_role_cancel_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_16 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_16.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_16.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_16_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_16_exception.png")
            self.logger.error(f"TC_UR_16 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def click_on_Right_check_box_deselect_it_and_verify_Click_save_to_commit_changes_message_is_displayed_above_haeding(self):
        try:
            self.logger.info("********** Test_TC_UR_17 Begin  **********")
            status = []
            check_box_status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            if len(panels_opened_list) > 0:
                self.logger.info(f"Panels are opened...")
                for y in range(len(panels_opened_list)):
                    time.sleep(web_driver.one_second)
                    user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                    if len(user_role_panel_title_list) > 0:
                        for x in range(len(user_role_panel_title_list)):
                            self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                            if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                status.append(True)
                                # --------------------------------------- #
                                time.sleep(web_driver.one_second)
                                rights_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rights_checkbox_by_xpath())
                                self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                check_box_status.append(rights_check_box.is_selected())
                                rights_check_box.click()
                                time.sleep(web_driver.one_second)
                                self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                check_box_status.append(rights_check_box.is_selected())
                                rights_check_box.click()
                                time.sleep(web_driver.one_second)
                                self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                check_box_status.append(rights_check_box.is_selected())
                                rights_check_box.click()
                                time.sleep(web_driver.one_second)
                                self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                check_box_status.append(rights_check_box.is_selected())
                                time.sleep(web_driver.one_second)
                                actual_click_to_save_msg = self.d.find_element(By.XPATH, user_roles_read_ini().get_click_to_save_msg_by_xpath())
                                expected_click_to_save_msg = user_roles_read_ini().get_click_to_save_msg()
                                self.logger.info(f"actual: {actual_click_to_save_msg.text}, \nexpected: {expected_click_to_save_msg}")
                                if actual_click_to_save_msg.is_displayed():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if actual_click_to_save_msg.text == expected_click_to_save_msg:
                                    status.append(True)
                                else:
                                    status.append(False)

                                if check_box_status == [True, False, True, False, False, True, False, True] or check_box_status == [True, False, True, False]:
                                    status.append(True)
                                else:
                                    status.append(False)

                                # ----------------------------------- #
                            else:
                                self.logger.info("Panel is not opened...")
                                status.append(False)
            else:
                self.logger.info(f"panel not opened...")
                time.sleep(web_driver.one_second)
                actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                if len(actual_user_roles_menu_item_list) > 0:
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for y in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[y]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    for x in range(len(user_role_panel_title_list)):
                                        self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                        if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                            self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                            status.append(True)
                                            # ---------------------------------------- #
                                            time.sleep(web_driver.one_second)
                                            rights_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rights_checkbox_by_xpath())
                                            self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                            check_box_status.append(rights_check_box.is_selected())
                                            rights_check_box.click()
                                            time.sleep(web_driver.one_second)
                                            self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                            check_box_status.append(rights_check_box.is_selected())
                                            rights_check_box.click()
                                            time.sleep(web_driver.one_second)
                                            self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                            check_box_status.append(rights_check_box.is_selected())
                                            rights_check_box.click()
                                            time.sleep(web_driver.one_second)
                                            self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                            check_box_status.append(rights_check_box.is_selected())
                                            actual_click_to_save_msg = self.d.find_element(By.XPATH, user_roles_read_ini().get_click_to_save_msg_by_xpath())
                                            expected_click_to_save_msg = user_roles_read_ini().get_click_to_save_msg()
                                            self.logger.info(f"actual: {actual_click_to_save_msg.text}, \nexpected: {expected_click_to_save_msg}")
                                            if actual_click_to_save_msg.is_displayed():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if actual_click_to_save_msg.text == expected_click_to_save_msg:
                                                status.append(True)
                                            else:
                                                status.append(False)

                                            if check_box_status == [True, False, True, False, False, True, False, True] or check_box_status == [True, False, True, False]:
                                                status.append(True)
                                            else:
                                                status.append(False)

                                            # ------------------------------------------- #
                                        else:
                                            self.logger.info("Panel is not opened...")
                                            status.append(False)
                                break

            time.sleep(web_driver.one_second)
            user_role_cancel_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_panel_cancel_btn())
            user_role_cancel_btn.click()
            time.sleep(web_driver.one_second)

            self.logger.info(f"status: {status}, check box status: {check_box_status}")
            self.logger.info("TC_UR_17 execution completed.\n")

            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_17.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_17.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_17_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_17_exception.png")
            self.logger.error(f"TC_UR_17 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def click_on_Rights_checkbox_select_it_and_verify_Click_save_to_commit_changes_message_tick_mark_above_checkbox_is_displayed(self):
        try:
            self.logger.info("********** Test_TC_UR_18 Begin  **********")
            status = []
            check_box_status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            if len(panels_opened_list) > 0:
                self.logger.info(f"Panels are opened...")
                for y in range(len(panels_opened_list)):
                    user_role_panel_title_list = self.d.find_elements(By.XPATH,
                                                                      user_roles_read_ini().get_user_role_panel_title_by_xpath())
                    if len(user_role_panel_title_list) > 0:
                        for x in range(len(user_role_panel_title_list)):
                            self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                            if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                status.append(True)
                                # --------------------------------------- #
                                time.sleep(web_driver.one_second)
                                rights_check_box = self.d.find_element(By.XPATH,
                                                                       user_roles_read_ini().get_rights_checkbox_by_xpath())
                                self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                check_box_status.append(rights_check_box.is_selected())
                                rights_check_box.click()
                                time.sleep(web_driver.one_second)
                                self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                check_box_status.append(rights_check_box.is_selected())
                                rights_check_box.click()
                                time.sleep(web_driver.one_second)
                                self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                check_box_status.append(rights_check_box.is_selected())
                                rights_check_box.click()
                                time.sleep(web_driver.one_second)
                                self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                check_box_status.append(rights_check_box.is_selected())
                                actual_click_to_save_msg = self.d.find_element(By.XPATH, user_roles_read_ini().get_click_to_save_msg_by_xpath())
                                expected_click_to_save_msg = user_roles_read_ini().get_click_to_save_msg()
                                self.logger.info(f"actual: {actual_click_to_save_msg.text}, \nexpected: {expected_click_to_save_msg}")
                                if actual_click_to_save_msg.is_displayed():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if actual_click_to_save_msg.text == expected_click_to_save_msg:
                                    status.append(True)
                                else:
                                    status.append(False)

                                if check_box_status == [True, False, True, False, False, True, False,
                                                        True] or check_box_status == [True, False, True, False]:
                                    status.append(True)
                                else:
                                    status.append(False)

                                # ----------------------------------- #
                            else:
                                self.logger.info("Panel is not opened...")
                                status.append(False)
            else:
                self.logger.info(f"panel not opened...")
                time.sleep(web_driver.one_second)
                actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                if len(actual_user_roles_menu_item_list) > 0:
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for y in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[y]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    for x in range(len(user_role_panel_title_list)):
                                        self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                        if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                            self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                            status.append(True)
                                            # ---------------------------------------- #
                                            time.sleep(web_driver.one_second)
                                            rights_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rights_checkbox_by_xpath())
                                            self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                            check_box_status.append(rights_check_box.is_selected())
                                            rights_check_box.click()
                                            time.sleep(web_driver.one_second)
                                            self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                            check_box_status.append(rights_check_box.is_selected())
                                            rights_check_box.click()
                                            time.sleep(web_driver.one_second)
                                            self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                            check_box_status.append(rights_check_box.is_selected())
                                            rights_check_box.click()
                                            time.sleep(web_driver.one_second)
                                            self.logger.info(f"check box status: {rights_check_box.is_selected()}")
                                            check_box_status.append(rights_check_box.is_selected())
                                            time.sleep(web_driver.one_second)
                                            actual_click_to_save_msg = self.d.find_element(By.XPATH, user_roles_read_ini().get_click_to_save_msg_by_xpath())
                                            expected_click_to_save_msg = user_roles_read_ini().get_click_to_save_msg()
                                            self.logger.info(f"actual: {actual_click_to_save_msg.text}, \nexpected: {expected_click_to_save_msg}")
                                            if actual_click_to_save_msg.is_displayed():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if actual_click_to_save_msg.text == expected_click_to_save_msg:
                                                status.append(True)
                                            else:
                                                status.append(False)

                                            if check_box_status == [True, False, True, False, False, True, False,
                                                                    True] or check_box_status == [True, False, True,
                                                                                                  False]:
                                                status.append(True)
                                            else:
                                                status.append(False)

                                            # ------------------------------------------- #
                                        else:
                                            self.logger.info("Panel is not opened...")
                                            status.append(False)
                                break
            time.sleep(web_driver.one_second)
            user_role_cancel_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_panel_cancel_btn())
            user_role_cancel_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {status}, check box status: {check_box_status}")
            self.logger.info("TC_UR_18 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_18.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_18.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_18_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_18_exception.png")
            self.logger.error(f"TC_UR_18 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def when_Rights_checkbox_is_selected_verify_all_the_checkboxes_inside_table_are_selected_and_tik_mark_is_visible(self):
        try:
            self.logger.info("********** Test_TC_UR_19 Begin  **********")
            status = []
            check_box_status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            if len(panels_opened_list) > 0:
                self.logger.info(f"Panels are opened...")
                for y in range(len(panels_opened_list)):
                    time.sleep(web_driver.one_second)
                    user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                    if len(user_role_panel_title_list) > 0:
                        for x in range(len(user_role_panel_title_list)):
                            self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                            if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                status.append(True)
                                # --------------------------------------- #
                                time.sleep(web_driver.one_second)
                                rights_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rights_checkbox_by_xpath())

                                rights_check_box.click()
                                time.sleep(web_driver.one_second)

                                for i in range(4):
                                    time.sleep(web_driver.one_second)
                                    create_column_checkbox_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_create_column_checkbox_by_xpath())
                                    time.sleep(web_driver.one_second)
                                    read_column_checkbox_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_read_column_checkbox_by_xpath())
                                    time.sleep(web_driver.one_second)
                                    edit_column_checkbox_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_edit_column_checkbox_by_xpath())
                                    time.sleep(web_driver.one_second)
                                    delete_column_checkbox_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_delete_column_checkbox_by_xpath())
                                    self.logger.info(f"create class: {create_column_checkbox_list[i].get_attribute('class')}")
                                    self.logger.info(f"read class: {read_column_checkbox_list[i].get_attribute('class')}")
                                    self.logger.info(f"edit class: {edit_column_checkbox_list[i].get_attribute('class')}")
                                    self.logger.info(f"delete class: {delete_column_checkbox_list[i].get_attribute('class')}")
                                    rights_check_box.click()
                                    time.sleep(web_driver.one_second)
                                    if rights_check_box.is_selected():
                                        for x in range(len(create_column_checkbox_list)):
                                            if create_column_checkbox_list[x].is_selected():
                                                check_box_status.append(True)
                                            else:
                                                check_box_status.append(False)
                                        for x in range(len(read_column_checkbox_list)):
                                            if read_column_checkbox_list[x].is_selected():
                                                check_box_status.append(True)
                                            else:
                                                check_box_status.append(False)
                                        for x in range(len(edit_column_checkbox_list)):
                                            if edit_column_checkbox_list[x].is_selected():
                                                check_box_status.append(True)
                                            else:
                                                check_box_status.append(False)
                                        for x in range(len(delete_column_checkbox_list)):
                                            if delete_column_checkbox_list[x].is_selected():
                                                check_box_status.append(True)
                                            else:
                                                check_box_status.append(False)
                                    else:
                                        for x in range(len(create_column_checkbox_list)):
                                            if create_column_checkbox_list[x].is_selected():
                                                check_box_status.append(True)
                                            else:
                                                check_box_status.append(False)
                                        for x in range(len(read_column_checkbox_list)):
                                            if read_column_checkbox_list[x].is_selected():
                                                check_box_status.append(True)
                                            else:
                                                check_box_status.append(False)
                                        for x in range(len(edit_column_checkbox_list)):
                                            if edit_column_checkbox_list[x].is_selected():
                                                check_box_status.append(True)
                                            else:
                                                check_box_status.append(False)
                                        for x in range(len(delete_column_checkbox_list)):
                                            if delete_column_checkbox_list[x].is_selected():
                                                check_box_status.append(True)
                                            else:
                                                check_box_status.append(False)

                                # ----------------------------------- #
                            else:
                                self.logger.info("Panel is not opened...")
                                status.append(False)
            else:
                self.logger.info(f"panel not opened...")
                time.sleep(web_driver.one_second)
                actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                if len(actual_user_roles_menu_item_list) > 0:
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    self.explicit_wait(10, "XPATH", user_roles_read_ini().get_action_dropdown_by_xpath() ,self.d)
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.two_second)
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for y in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[y]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    for x in range(len(user_role_panel_title_list)):
                                        self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                        if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                            self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                            status.append(True)
                                            # ---------------------------------------- #
                                            time.sleep(web_driver.one_second)
                                            rights_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rights_checkbox_by_xpath())

                                            rights_check_box.click()
                                            time.sleep(web_driver.one_second)
                                            for i in range(4):
                                                time.sleep(web_driver.one_second)
                                                create_column_checkbox_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_create_column_checkbox_by_xpath())
                                                time.sleep(web_driver.one_second)
                                                read_column_checkbox_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_read_column_checkbox_by_xpath())
                                                time.sleep(web_driver.one_second)
                                                edit_column_checkbox_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_edit_column_checkbox_by_xpath())
                                                time.sleep(web_driver.one_second)
                                                delete_column_checkbox_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_delete_column_checkbox_by_xpath())
                                                self.logger.info(f"create class: {create_column_checkbox_list[i].get_attribute('class')}")
                                                self.logger.info(f"read class: {read_column_checkbox_list[i].get_attribute('class')}")
                                                self.logger.info(f"edit class: {edit_column_checkbox_list[i].get_attribute('class')}")
                                                self.logger.info(f"delete class: {delete_column_checkbox_list[i].get_attribute('class')}")
                                                rights_check_box.click()
                                                time.sleep(web_driver.one_second)
                                                if rights_check_box.is_selected():
                                                    for x in range(len(create_column_checkbox_list)):
                                                        if create_column_checkbox_list[x].is_selected():
                                                            check_box_status.append(True)
                                                        else:
                                                            check_box_status.append(False)
                                                    for x in range(len(read_column_checkbox_list)):
                                                        if read_column_checkbox_list[x].is_selected():
                                                            check_box_status.append(True)
                                                        else:
                                                            check_box_status.append(False)
                                                    for x in range(len(edit_column_checkbox_list)):
                                                        if edit_column_checkbox_list[x].is_selected():
                                                            check_box_status.append(True)
                                                        else:
                                                            check_box_status.append(False)
                                                    for x in range(len(delete_column_checkbox_list)):
                                                        if delete_column_checkbox_list[x].is_selected():
                                                            check_box_status.append(True)
                                                        else:
                                                            check_box_status.append(False)
                                                else:
                                                    for x in range(len(create_column_checkbox_list)):
                                                        if create_column_checkbox_list[x].is_selected():
                                                            check_box_status.append(True)
                                                        else:
                                                            check_box_status.append(False)
                                                    for x in range(len(read_column_checkbox_list)):
                                                        if read_column_checkbox_list[x].is_selected():
                                                            check_box_status.append(True)
                                                        else:
                                                            check_box_status.append(False)
                                                    for x in range(len(edit_column_checkbox_list)):
                                                        if edit_column_checkbox_list[x].is_selected():
                                                            check_box_status.append(True)
                                                        else:
                                                            check_box_status.append(False)
                                                    for x in range(len(delete_column_checkbox_list)):
                                                        if delete_column_checkbox_list[x].is_selected():
                                                            check_box_status.append(True)
                                                        else:
                                                            check_box_status.append(False)

                                            # ------------------------------------------- #
                                        else:
                                            self.logger.info("Panel is not opened...")
                                            status.append(False)
                                break

            self.logger.info(f"status: {status}, \ncheck box status: {check_box_status}, \nTrue count in check box status: {check_box_status.count(True)}, \nFalse Count in check box status: {check_box_status.count(False)}")
            if check_box_status.count(True) == check_box_status.count(False):
                status.append(True)
            else:
                status.append(False)

            self.logger.info("TC_UR_19 execution completed.\n")
            time.sleep(web_driver.one_second)
            user_role_cancel_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_panel_cancel_btn())
            user_role_cancel_btn.click()
            time.sleep(web_driver.one_second)

            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_19.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_19.png")
                logout().logout_from_core(self.d)
                return False
            else:
                logout().logout_from_core(self.d)
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_19_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_19_exception.png")
            self.logger.error(f"TC_UR_19 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def enter_user_role_details_and_click_on_Save_btn_and_verify_user_role_with_given_name_is_created_successfully(self):
        try:
            self.logger.info("********** Test_TC_UR_20 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            print("1 one")
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            if len(panels_opened_list) > 0:
                self.logger.info(f"Panels are opened...")
                for y in range(len(panels_opened_list)):
                    time.sleep(web_driver.one_second)
                    user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                    if len(user_role_panel_title_list) > 0:
                        for x in range(len(user_role_panel_title_list)):
                            self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                            if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                status.append(True)
                                # --------------------------------------- #
                                time.sleep(web_driver.one_second)
                                role_name_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rolename_text_box_to_enter_data_by_xpath())
                                time.sleep(web_driver.one_second)
                                description_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_description_text_box_to_enter_data_by_xpath())
                                time.sleep(web_driver.one_second)
                                role_name_text_box.click()
                                role_name_text_box.clear()
                                role_name_text_box.send_keys(user_roles_read_ini().get_so_user_role_so())
                                time.sleep(web_driver.one_second)
                                description_text_box.click()
                                description_text_box.clear()
                                description_text_box.send_keys(user_roles_read_ini().get_so_user_role_description())
                                time.sleep(web_driver.one_second)
                                entered_text = role_name_text_box.get_attribute('value')
                                entered_description = description_text_box.get_attribute('value')
                                self.logger.info(f"entered role: {entered_text}, \nentered description: {entered_description}")
                                rights_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rights_checkbox_by_xpath())
                                self.logger.info(f"right checkbox status: {rights_check_box.is_selected()}")
                                rights_check_box.click()
                                time.sleep(web_driver.one_second)
                                if entered_text == user_roles_read_ini().get_so_user_role_so():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if entered_description == user_roles_read_ini().get_so_user_role_description():
                                    status.append(True)
                                    self.logger.info(f"verify: {True}")
                                else:
                                    self.logger.info(f"verify: {False}")
                                    status.append(False)
                                if rights_check_box.is_selected():
                                    pass
                                else:
                                    rights_check_box.click()
                                time.sleep(web_driver.one_second)
                                save_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_save_btn_by_xpath())
                                save_btn.click()
                                time.sleep(web_driver.one_second)
                                user_roles_profile_names = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_name_list_by_xpath())
                                for name in user_roles_profile_names:
                                    self.logger.info(f"profile name: {name.text}")
                                    if name.text == user_roles_read_ini().get_so_user_role_so():
                                        self.logger.info("user created successfully...")
                                        self.logger.info("First IF block executed..")
                                        status.append(True)
                                        break
                                # ----------------------------------- #
                            else:
                                self.logger.info("Panel is not opened...")
                                status.append(False)
            else:
                self.logger.info(f"panel not opened...")
                time.sleep(web_driver.one_second)
                actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                if len(actual_user_roles_menu_item_list) > 0:
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.explicit_wait(10, "XPATH", user_roles_read_ini().get_user_role_menu_item_by_xpath(), self.d)
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.explicit_wait(10, "XPATH", user_roles_read_ini().get_action_dropdown_by_xpath(), self.d)
                    self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        self.logger.info("action dropdown contains options...")
                        for y in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[y]
                            self.logger.info(f"option: {option.text}")
                            if option.is_displayed():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.is_enabled():
                                status.append(True)
                            else:
                                status.append(False)
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                self.logger.info(f"Option Name Selected: {option.text}")
                                option.click()
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    for x in range(len(user_role_panel_title_list)):
                                        self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                        if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                            self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                            status.append(True)
                                            # ---------------------------------------- #
                                            time.sleep(web_driver.one_second)
                                            role_name_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rolename_text_box_to_enter_data_by_xpath())
                                            time.sleep(web_driver.one_second)
                                            description_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_description_text_box_to_enter_data_by_xpath())
                                            time.sleep(web_driver.one_second)
                                            role_name_text_box.click()
                                            role_name_text_box.clear()
                                            time.sleep(web_driver.one_second)
                                            role_name_text_box.send_keys(user_roles_read_ini().get_so_user_role_so())
                                            time.sleep(web_driver.one_second)
                                            description_text_box.click()
                                            description_text_box.clear()
                                            time.sleep(web_driver.one_second)
                                            description_text_box.send_keys(user_roles_read_ini().get_so_user_role_description())
                                            time.sleep(web_driver.one_second)
                                            entered_text = role_name_text_box.get_attribute('value')
                                            entered_description = description_text_box.get_attribute('value')
                                            self.logger.info(f"entered role: {entered_text}, \nentered description: {entered_description}")
                                            time.sleep(web_driver.one_second)
                                            rights_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rights_checkbox_by_xpath())
                                            self.logger.info(f"right checkbox status: {rights_check_box.is_selected()}")
                                            rights_check_box.click()
                                            time.sleep(web_driver.one_second)
                                            if entered_text == user_roles_read_ini().get_so_user_role_so():
                                                self.logger.info(f"user role name entered: {entered_text}")
                                                status.append(True)
                                            else:
                                                self.logger.info(f"user name entered not matching.. {entered_text}")
                                                status.append(False)
                                            if entered_description == user_roles_read_ini().get_so_user_role_description():
                                                status.append(True)
                                                self.logger.info(f"verify: {True}")
                                            else:
                                                self.logger.info(f"verify: {False}")
                                                status.append(False)
                                            if rights_check_box.is_selected():
                                                pass
                                            else:
                                                rights_check_box.click()
                                                time.sleep(web_driver.one_second)
                                            time.sleep(web_driver.one_second)
                                            save_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_save_btn_by_xpath())
                                            save_btn.click()
                                            time.sleep(web_driver.one_second)
                                            # -------- #
                                            # self.close_all_panel()
                                            # time.sleep(web_driver.one_second)
                                            # actual_user_roles_menu_item = self.explicit_wait(10, "XPATH", user_roles_read_ini().get_user_role_menu_item_by_xpath(), self.d)
                                            # actual_user_roles_menu_item.click()
                                            # time.sleep(web_driver.one_second)
                                            # -------- #
                                            user_roles_profile_names = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_name_list_by_xpath())

                                            for name in user_roles_profile_names:
                                                self.logger.info(f"profile name: {name.text}")
                                                if name.text == user_roles_read_ini().get_so_user_role_so():
                                                    self.logger.info("user created successfully...")
                                                    self.logger.info("First Else block executed..")
                                                    status.append(True)
                                                    break
                                            # ------------------------------------------- #
                                        else:
                                            self.logger.info("Panel is not opened...")
                                            status.append(False)
                                break
            # time.sleep(web_driver.one_second)
            # user_role_cancel_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_panel_cancel_btn())
            # user_role_cancel_btn.click()
            # time.sleep(web_driver.one_second)

            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_20 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_20.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_20.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_20_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_20_exception.png")
            self.logger.error(f"TC_UR_20 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def after_clicking_on_save_btn_close_user_roles_and_user_role_panels_and_verify_no_panel_is_visible_on_screen(self):
        try:
            self.logger.info("********** Test_TC_UR_21 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            # if len(panels_opened_list) > 0:
            #     self.logger.info(f"Panels are opened...{len(panels_opened_list)}")
            #     for y in range(len(panels_opened_list)):
            #         user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
            #         if len(user_role_panel_title_list) > 0:
            #             for x in range(len(user_role_panel_title_list)):
            #                 self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
            #                 if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
            #                     self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
            #                     status.append(True)
            #                     # ---------------------------------------
            #                     panels = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            #                     for i in range(len(panels)):
            #                         panels[i].click()
            #                         time.sleep(web_driver.one_second)
            #                     panel_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            #
            #                     if len(panel_list) == 0:
            #                         self.logger.info("note: no panel is visible")
            #                         status.append(True)
            #                     else:
            #                         self.logger.info(f"some panel is still visible: {[x.text for x in panel_list]}")
            #                         status.append(False)
            #
            #                     # -----------------------------------
            #                 else:
            #                     self.logger.info("Panel is not opened...")
            #                     status.append(False)
            # else:
            self.logger.info(f"panel not opened...")
            time.sleep(web_driver.one_second)
            actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
            if len(actual_user_roles_menu_item_list) > 0:
                time.sleep(web_driver.one_second)
                actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                actual_user_roles_menu_item.click()
                time.sleep(web_driver.two_second)
                action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                self.logger.info(f"actual action dropdown text: {action_drop_down.text}")
                action_drop_down.click()
                time.sleep(web_driver.one_second)
                options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                if len(options_inside_action_dropdown) > 0:
                    self.logger.info("action dropdown contains options...")
                    for y in range(len(options_inside_action_dropdown)):
                        option = options_inside_action_dropdown[y]
                        self.logger.info(f"option: {option.text}")
                        if option.is_displayed():
                            status.append(True)
                        else:
                            status.append(False)
                        if option.is_enabled():
                            status.append(True)
                        else:
                            status.append(False)
                        if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                            self.logger.info(f"Option Name Selected: {option.text}")
                            option.click()
                            time.sleep(web_driver.two_second)
                            user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                            if len(user_role_panel_title_list) > 0:
                                for x in range(len(user_role_panel_title_list)):
                                    self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                    if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                        self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                        status.append(True)
                                        # ---------------------------------------- #
                                        time.sleep(web_driver.one_second)
                                        panels = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                                        for i in range(len(panels)):
                                            panels[i].click()
                                            time.sleep(web_driver.two_second)
                                        time.sleep(web_driver.one_second)
                                        panel_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())

                                        if len(panel_list) == 0:
                                            self.logger.info("note: no panel is visible")
                                            status.append(True)
                                        else:
                                            self.logger.info("some panel is still visible")
                                            status.append(False)
                                        # ------------------------------------------- #
                                    else:
                                        self.logger.info("Panel is not opened...")
                                        status.append(False)
                            break

            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_21 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_21.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_21.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_21_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_21_exception.png")
            self.logger.error(f"TC_UR_21 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def verify_newly_created_user_role_is_available_for_user_creation_inside_user_roles_dropdown_on_create_user_panel(self):
        try:
            self.logger.info("********** Test_TC_UR_22 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, user_roles_read_ini().get_cloud_menu_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, user_roles_read_ini().get_users_sub_menu_item_by_xpath()).click()

            time.sleep(web_driver.one_second)
            actual_user_panel_title = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_panel_title_by_xpath())
            self.logger.info(f"actual: {actual_user_panel_title.text}")
            expected_user_panel_title = user_roles_read_ini().get_user_page_panel_title()
            self.logger.info(f"expected: {expected_user_panel_title}")
            if actual_user_panel_title.is_displayed():
                status.append(True)
            else:
                status.append(False)
            if expected_user_panel_title in actual_user_panel_title.text:
                status.append(True)
            else:
                status.append(False)
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_user_panel_by_xpath())
            action_dropdown.click()
            options_inside_action_dropdown_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
            if len(options_inside_action_dropdown_list) > 0:
                for option in options_inside_action_dropdown_list:
                    if option.text != "":
                        if option.text == "Create User":
                            option.click()
                time.sleep(web_driver.one_second)

                # ------------------------------------------------ #
                time.sleep(web_driver.one_second)
                user_role_dropdown = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_dropdown_by_xpath())
                user_role_dropdown.click()
                time.sleep(web_driver.one_second)
                role_options_inside_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_role_option_in_user_role_dropdown_by_xpath())
                count = 0
                for role in role_options_inside_dropdown:
                    if role.text == user_roles_read_ini().get_so_user_role():
                        self.logger.info(f"User role: '{user_roles_read_ini().get_so_user_role()}' is visible..")
                        count = count + 1
                        if role.is_enabled():
                            status.append(True)
                        else:
                            self.logger.info("User role is not clickable...")
                            status.append(False)
                if count == 1:
                    status.append(True)
                else:
                    self.logger.info("Created user role is not visible...")
                time.sleep(web_driver.one_second)
                self.d.find_element(By.XPATH, user_roles_read_ini().get_panel_container_outside_click_by_xpath()).click()
                panels = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                for i in range(len(panels)):
                    panels[i].click()
                    time.sleep(web_driver.one_second)
                # ----------------------------------------------- #
            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_22 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_22.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_22.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_22_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_22_exception.png")
            self.logger.error(f"TC_UR_22 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def Verify_User_role_deletion_functionality_by_deleting_one_user_role(self):
        try:
            self.logger.info("********** Test_TC_UR_23 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            panels_opened_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_number_of_panels_list_by_xpath())
            if len(panels_opened_list) > 0:
                self.logger.info(f"Panels are opened...")
                for y in range(len(panels_opened_list)):
                    time.sleep(web_driver.one_second)
                    user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                    if len(user_role_panel_title_list) > 0:
                        for x in range(len(user_role_panel_title_list)):
                            if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                status.append(True)
                                # --------------------------------------- #
                                time.sleep(web_driver.one_second)
                                role_name_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rolename_text_box_to_enter_data_by_xpath())
                                time.sleep(web_driver.one_second)
                                description_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_description_text_box_to_enter_data_by_xpath())
                                time.sleep(web_driver.one_second)
                                role_name_text_box.click()
                                role_name_text_box.clear()
                                time.sleep(web_driver.one_second)
                                role_name_text_box.send_keys(user_roles_read_ini().get_user_role_for_deletion())
                                time.sleep(web_driver.two_second)
                                description_text_box.click()
                                description_text_box.clear()
                                time.sleep(web_driver.one_second)
                                description_text_box.send_keys(user_roles_read_ini().get_so_user_role_description())
                                time.sleep(web_driver.two_second)
                                entered_text = role_name_text_box.get_attribute('value')
                                entered_description = description_text_box.get_attribute('value')
                                self.logger.info(f"entered role: {entered_text}, \nentered description: {entered_description}")
                                rights_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rights_checkbox_by_xpath())
                                self.logger.info(f"right checkbox status: {rights_check_box.is_selected()}")
                                rights_check_box.click()
                                time.sleep(web_driver.two_second)
                                if entered_text == user_roles_read_ini().get_user_role_for_deletion():
                                    status.append(True)
                                else:
                                    status.append(False)
                                if entered_description == user_roles_read_ini().get_so_user_role_description():
                                    status.append(True)
                                    self.logger.info(f"verify: {True}")
                                else:
                                    self.logger.info(f"verify: {False}")
                                    status.append(False)
                                if rights_check_box.is_selected():
                                    pass
                                else:
                                    rights_check_box.click()
                                time.sleep(web_driver.one_second)
                                save_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_save_btn_by_xpath())
                                save_btn.click()
                                time.sleep(web_driver.two_second)
                                user_roles_profile_names = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_name_list_by_xpath())
                                for name in user_roles_profile_names:
                                    # self.logger.info(f"profile name: {name.text}")
                                    if name.text == user_roles_read_ini().get_user_role_for_deletion():
                                        self.logger.info("user created successfully...")
                                        status.append(True)
                                # ----------------------------------- #
                            else:
                                self.logger.info("Panel is not opened...")
                                status.append(False)
            else:
                self.logger.info(f"panel not opened...")
                actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                if len(actual_user_roles_menu_item_list) > 0:
                    time.sleep(web_driver.one_second)
                    actual_user_roles_menu_item = self.explicit_wait(10, "XPATH", user_roles_read_ini().get_user_role_menu_item_by_xpath(), self.d)
                    actual_user_roles_menu_item.click()
                    time.sleep(web_driver.one_second)
                    action_drop_down = self.explicit_wait(10, "XPATH", user_roles_read_ini().get_action_dropdown_by_xpath(), self.d)
                    action_drop_down.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown) > 0:
                        for y in range(len(options_inside_action_dropdown)):
                            option = options_inside_action_dropdown[y]
                            if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                                option.click()
                                time.sleep(web_driver.one_second)
                                user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                                if len(user_role_panel_title_list) > 0:
                                    for x in range(len(user_role_panel_title_list)):
                                        if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                            status.append(True)
                                            # ---------------------------------------- #
                                            time.sleep(web_driver.one_second)
                                            role_name_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rolename_text_box_to_enter_data_by_xpath())
                                            time.sleep(web_driver.one_second)
                                            description_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_description_text_box_to_enter_data_by_xpath())
                                            time.sleep(web_driver.one_second)
                                            role_name_text_box.click()
                                            role_name_text_box.clear()
                                            time.sleep(web_driver.one_second)
                                            role_name_text_box.send_keys(user_roles_read_ini().get_user_role_for_deletion())
                                            time.sleep(web_driver.two_second)
                                            description_text_box.click()
                                            description_text_box.clear()
                                            time.sleep(web_driver.one_second)
                                            description_text_box.send_keys(user_roles_read_ini().get_so_user_role_description())
                                            time.sleep(web_driver.two_second)
                                            entered_text = role_name_text_box.get_attribute('value')
                                            entered_description = description_text_box.get_attribute('value')
                                            self.logger.info(f"entered role: {entered_text}, \nentered description: {entered_description}")
                                            time.sleep(web_driver.one_second)
                                            rights_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rights_checkbox_by_xpath())
                                            self.logger.info(f"right checkbox status: {rights_check_box.is_selected()}")
                                            rights_check_box.click()
                                            time.sleep(web_driver.one_second)
                                            if entered_text == user_roles_read_ini().get_user_role_for_deletion():
                                                status.append(True)
                                            else:
                                                status.append(False)
                                            if entered_description == user_roles_read_ini().get_so_user_role_description():
                                                status.append(True)
                                                self.logger.info(f"verify: {True}")
                                            else:
                                                self.logger.info(f"verify: {False}")
                                                status.append(False)
                                            if rights_check_box.is_selected():
                                                pass
                                            else:
                                                rights_check_box.click()
                                            time.sleep(web_driver.one_second)
                                            save_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_save_btn_by_xpath())
                                            save_btn.click()
                                            time.sleep(web_driver.two_second)
                                            user_roles_profile_names = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_name_list_by_xpath())

                                            for name in user_roles_profile_names:
                                                # self.logger.info(f"profile name: {name.text}")
                                                if name.text == user_roles_read_ini().get_user_role_for_deletion():
                                                    self.logger.info("user created successfully...")
                                                    status.append(True)

                                            # ------------------------------------------- #
                                        else:
                                            self.logger.info("Panel is not opened...")
                                            status.append(False)
            time.sleep(web_driver.one_second)
            user_roles_profile_names = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_name_list_by_xpath())
            time.sleep(web_driver.one_second)
            checkboxes = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_checkboxes_by_xpath())
            for i in range(len(user_roles_profile_names)-1):
                if user_roles_profile_names[i].text == user_roles_read_ini().get_user_role_for_deletion():
                    checkboxes[i].click()
                    time.sleep(web_driver.one_second)
                    self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath()).click()
                    time.sleep(web_driver.two_second)
                    options_inside_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    for y in range(len(options_inside_action_dropdown)-1):
                        option = options_inside_action_dropdown[y]
                        if option.text == user_roles_read_ini().get_delete_user_role_option_text_inside_action_dropdown():
                            # self.logger.info(f"Option Name Selected: {option.text}")
                            option.click()
                            time.sleep(web_driver.two_second)
                            self.d.find_element(By.XPATH, user_roles_read_ini().get_yes_delete_user_role_button_by_xpath()).click()
                            time.sleep(web_driver.two_second)

                            user_roles_profile_names = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_name_list_by_xpath())
                            time.sleep(web_driver.two_second)

                            for j in range(len(user_roles_profile_names)-1):
                                if user_roles_profile_names[j].text == user_roles_read_ini().get_user_role_for_deletion():
                                    status.append(False)
                                else:
                                    status.append(True)

            self.logger.info(f"status: {status}")
            self.logger.info("TC_UR_23 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_23.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_23.png")
                return False
            else:
                return True
            # logout().logout_from_core()

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR_23_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR_23_exception.png")
            self.logger.error(f"TC_UR_23 got exception as: {ex.args}")
        finally:
            self.close_all_panel()

    def get_excel_data(self):
        try:
            df_1, df_2 = Read_excel.get_user_role_authentication_data_df()
            df1 = df_1.replace(np.nan, '', regex=True)
            df2 = df_2.replace(np.nan, '', regex=True)
            # print(f"df1: {df1}, \ndf2: {df2}")
            person_1 = [i for i in df1['Enrollment_1']]
            event = [i for i in df1['Event_1']]
            station_1 = [i for i in df1['Station_1']]
            rights_1 = [i for i in df1['Rights_1']]
            df1_result_1 = [i for i in df1['Result_1']]
            df1_result_2 = [i for i in df1['Result_2']]
            df1_result_3 = [i for i in df1['Result_3']]
            df1_result_4 = [i for i in df1['Result_4']]
            df1_result_5 = [i for i in df1['Result_5']]
            df1_result_6 = [i for i in df1['Result_6']]

            person_2 = [i for i in df2['Enrollment_2']]
            profile = [i for i in df2['Profile_2']]
            station_2 = [i for i in df2['Station_2']]
            rights_2 = [i for i in df2['Rights_2']]
            df2_result_1 = [i for i in df2['Result_1']]
            df2_result_2 = [i for i in df2['Result_2']]
            df2_result_3 = [i for i in df2['Result_3']]
            df2_result_4 = [i for i in df2['Result_4']]
            # print(f"df2_result_3: {df2_result_3}")

            zip_list_1 = zip(person_1, event, station_1, rights_1)
            zip_list_2 = zip(df1_result_1, df1_result_2, df1_result_3, df1_result_4, df1_result_5, df1_result_6)
            person_event_station = list(zip_list_1)
            person_event_station_results = list(zip_list_2)

            zip_list_3 = zip(station_2, person_2, profile, rights_2)
            zip_list_4 = zip(df2_result_1, df2_result_2, df2_result_3, df2_result_4)
            station_person_profile = list(zip_list_3)
            station_person_profile_results = list(zip_list_4)

            print(f"person_event_station: {person_event_station[1]}")
            print(f"station_person_profile: {station_person_profile[1]}")
            print(f"person_event_station_results: {person_event_station_results[1]}")
            print(f"station_person_profile_results: {station_person_profile_results[1]}")

        except Exception as ex:
            print(ex.args)

    # def load_portal_login_page_if_not_loaded(self):
    #     try:
    #         if self.d.title == Portal_Menu_Module_read_ini().get_portal_title():
    #             pass
    #         else:
    #             self.d.get(Portal_Menu_Module_read_ini().get_portal_url())
    #             self.d.maximize_window()
    #     except Exception as ex:
    #         self.logger.error(ex)

    def login_to_cloud_with_user(self):
        try:
            self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.one_second)
            logout_button = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                get_logout_button_on_portal_by_xpath())
            if logout_button.is_displayed():
                pass
            else:
                if self.d.current_url == Portal_Menu_Module_read_ini().get_portal_url():
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(web_driver.two_second)
                login_username = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                     get_portal_login_username_textbox_by_xpath())
                login_username.clear()
                time.sleep(web_driver.one_second)
                login_username.send_keys(Portal_Menu_Module_read_ini().get_portal_login_username())
                time.sleep(web_driver.one_second)
                login_password = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                     get_portal_login_password_textbox_by_xpath())
                login_password.clear()
                time.sleep(web_driver.one_second)
                login_password.send_keys(Portal_Menu_Module_read_ini().get_portal_login_password())
                self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                    get_cloud_login_button_on_portal_by_xpath()).click()
                time.sleep(web_driver.one_second)

            if False in self.status:
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(ex)

    def create_test_user_role(self):
        try:
            self.logger.info("********** Test_TC_UR_ Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.get_excel_data()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath()).click()

            time.sleep(web_driver.two_second)

            action_dropdown = self.d.find_element(By.XPATH, user_roles_read_ini().
                                                  get_action_dropdown_by_xpath())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            options_in_action_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().
                                                              get_options_inside_action_dropdown_by_xpath())
            if len(options_in_action_dropdown) > 0:
                for option in options_in_action_dropdown:
                    if option.text == user_roles_read_ini(). \
                            get_create_user_role_option_text_inside_action_dropdown():
                        option.click()
                        time.sleep(web_driver.two_second)
            else:
                self.logger.info("options in actions dropdown is not visible...")

            role_name = user_roles_read_ini().get_test_user_role()
            description = user_roles_read_ini().get_test_user_role_description()
            time.sleep(web_driver.two_second)
            role_name_textbox = self.d.find_element(By.XPATH,
                                                    user_roles_read_ini().get_rolename_text_box_to_enter_data_by_xpath())
            role_name_textbox.click()
            role_name_textbox.clear()
            time.sleep(web_driver.one_second)
            role_name_textbox.send_keys(role_name)
            time.sleep(web_driver.one_second)
            self.logger.info(f"Role name: {role_name}")
            description_textbox = self.d.find_element(By.XPATH,
                                                      user_roles_read_ini().get_description_text_box_to_enter_data_by_xpath())
            description_textbox.click()
            description_textbox.clear()
            time.sleep(web_driver.one_second)
            description_textbox.send_keys(description)
            self.logger.info(f"Description: {description}")
            time.sleep(web_driver.one_second)
            entered_text = role_name_textbox.get_attribute('value')
            entered_description = description_textbox.get_attribute('value')
            self.logger.info(f"entered role: {entered_text}, \nentered description: {entered_description}")
            time.sleep(web_driver.two_second)
            save_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on Save button..")
            time.sleep(web_driver.two_second)
            user_roles_profile_names = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_name_list_by_xpath())
            time.sleep(web_driver.two_second)
            for name in user_roles_profile_names:
                if name.text == role_name:
                    self.logger.info(f"profile name: {name.text}")
                    self.logger.info("user role created successfully...")
                    status.append(True)
                else:
                    self.logger.info("user role is not created")
            self.click_on_logout()
            if False in status:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_UR__exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_UR__exception.png")
            self.logger.error(f"TC_UR_ got exception as: {ex.args}")


    def create_test_user(self):
        try:
            self.logger.info("creating test user")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            Users_Module_pom().click_user_on_cloud_menu()
            Users_Module_pom().click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            username_xpath = user_roles_read_ini().get_username_textbox_by_xpath()
            Users_Module_pom().enter_user_name(user_roles_read_ini().get_username())
            Users_Module_pom().enter_first_name(user_roles_read_ini().get_first_name())
            Users_Module_pom().enter_last_name(user_roles_read_ini().get_last_name())
            Users_Module_pom().select_user_role(user_roles_read_ini().get_user_role())
            Users_Module_pom().enter_password(user_roles_read_ini().get_password())
            Users_Module_pom().select_region(user_roles_read_ini().get_region_text())
            email = f"{user_roles_read_ini().get_username()}@facefirst.com"
            Users_Module_pom().enter_email(email)
            Users_Module_pom().select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            Users_Module_pom().click_on_save_btn()
            time.sleep(web_driver.one_second)
            if Users_Module_pom().check_if_user_is_created(user_name= user_roles_read_ini().get_username()):
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}user_creation_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}user_creation_exception.png")
            self.logger.info(f"test_TC_US_110_exception: {ex}")
            return False
        finally:
            self.click_on_logout()
            self.d.refresh()

    def click_on_logout(self):
        try:
            time.sleep(web_driver.two_second)
            logout = self.d.find_element(By.XPATH,user_roles_read_ini().get_logout_btn_link_by_xpath())
            time.sleep(web_driver.one_second)
            if logout.is_displayed():
                logout.click()
        except Exception as ex:
            print(ex.args)
