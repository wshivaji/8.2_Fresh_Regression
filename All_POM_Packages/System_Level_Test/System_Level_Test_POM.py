import time
from pathlib import Path
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from selenium.webdriver.common.by import By
from All_Config_Packages._4_Users_Module_Config_Files.Users_Read_INI import Read_Users_Components
from All_Config_Packages._3_User_Roles_Module_Config_Files.User_Roles_Read_Ini import user_roles_read_ini
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import Portal_Menu_Module_read_ini
from All_Config_Packages._6_Notification_Groups_Module_Config_Files.Notification_Groups_Read_INI import Read_Notification_Groups_Components
from Base_Package.Login_Logout_Ops import login, logout
from All_POM_Packages._6_Notification_Groups_Module.notification_groups_module_POM import Notification_Groups_Module_pom
from All_POM_Packages._7_Visitor_Search_Module_POM.Visitor_Search_Module_POM import Visitor_Search_Module_pom
from All_Config_Packages._7_Visitor_Search_Module_Config_Files.Visitor_Search_Read_INI import Read_Visitor_Search_Components
from All_Config_Packages.System_Level_Test.System_Level_Test_Read_INI import system_level_test_read_ini


class System_Level_Test_pom(web_driver, web_logger):
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

    def creating_five_user_roles(self):
        try:
            self.logger.info("********** Test_SLT_01 Begin  **********")
            status = []
            time.sleep(web_driver.two_second)
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            actual_user_roles_menu_item_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
            if len(actual_user_roles_menu_item_list) > 0:
                actual_user_roles_menu_item = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_menu_item_by_xpath())
                actual_user_roles_menu_item.click()
                time.sleep(web_driver.one_second)
                action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
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
                                    self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                    if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                        self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                        status.append(True)
                                        # ----------------------------------------
                                        role_name_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rolename_text_box_to_enter_data_by_xpath())
                                        time.sleep(web_driver.one_second)
                                        description_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_description_text_box_to_enter_data_by_xpath())
                                        time.sleep(web_driver.one_second)
                                        role_name_text_box.click()
                                        time.sleep(web_driver.two_second)
                                        role_name_text_box.clear()
                                        time.sleep(web_driver.two_second)
                                        role_name_text_box.send_keys(system_level_test_read_ini().get_SO_user_role())
                                        time.sleep(web_driver.one_second)
                                        description_text_box.click()
                                        time.sleep(web_driver.two_second)
                                        description_text_box.clear()
                                        time.sleep(web_driver.two_second)
                                        description_text_box.send_keys(system_level_test_read_ini().get_SO_user_role_description())
                                        time.sleep(web_driver.one_second)
                                        entered_text = role_name_text_box.get_attribute('value')
                                        entered_description = description_text_box.get_attribute('value')
                                        self.logger.info(f"entered role: {entered_text}, \nentered description: {entered_description}")
                                        rights_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rights_checkbox_by_xpath())

                                        rights_check_box.click()
                                        time.sleep(web_driver.one_second)
                                        if entered_text == system_level_test_read_ini().get_SO_user_role():
                                            status.append(True)
                                        else:
                                            status.append(False)
                                        if entered_description == system_level_test_read_ini().get_SO_user_role_description():
                                            status.append(True)
                                            self.logger.info(f"verify: {True}")
                                        else:
                                            self.logger.info(f"verify: {False}")
                                            status.append(False)
                                        if rights_check_box.is_selected():
                                            pass
                                        else:
                                            rights_check_box.click()
                                            time.sleep(web_driver.two_second)

                                        save_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_save_btn_by_xpath())
                                        save_btn.click()
                                        time.sleep(web_driver.one_second)
                                        user_roles_profile_names = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_name_list_by_xpath())

                                        for name in user_roles_profile_names:
                                            if name.text == system_level_test_read_ini().get_SO_user_role():
                                                self.logger.info(f"{name.text} created successfully...")
                                                self.logger.info("User Created 1.. ")
                                                status.append(True)

                                    else:
                                        self.logger.info("Panel is not opened...")
                                        status.append(False)
                else:
                    self.logger.info("continue execution 1.. ")

                # -------------------------------------------
                time.sleep(web_driver.two_second)
                close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                self.logger.info(f"panel count: {len(close_panel)}")
                close_panel[1].click()
                time.sleep(web_driver.two_second)
                self.logger.info("panel closed 1.")
                self.logger.info(f"panel count: {len(close_panel)}")
                time.sleep(web_driver.one_second)
                action_drop_down = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_by_xpath())
                action_drop_down.click()
                time.sleep(web_driver.one_second)
                time.sleep(web_driver.one_second)
                options_inside_action_dropdown = self.d.find_elements(By.XPATH,
                                                                      user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                self.logger.info(f"option inside action dropdown count: {len(options_inside_action_dropdown)}")
                if len(options_inside_action_dropdown) > 0:
                    for y in range(len(options_inside_action_dropdown)):
                        option = options_inside_action_dropdown[y]
                        if option.text == user_roles_read_ini().get_create_user_role_option_text_inside_action_dropdown():
                            option.click()
                            time.sleep(web_driver.one_second)
                            user_role_panel_title_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_role_panel_title_by_xpath())
                            self.logger.info(f"user role panel count: {len(user_role_panel_title_list)}")
                            if len(user_role_panel_title_list) > 0:
                                for x in range(len(user_role_panel_title_list)):
                                    self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                    if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                        self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                        status.append(True)
                                        # ----------------------------------------
                                        role_name_text_box = self.d.find_element(By.XPATH,
                                                                                 user_roles_read_ini().get_rolename_text_box_to_enter_data_by_xpath())
                                        time.sleep(web_driver.one_second)
                                        description_text_box = self.d.find_element(By.XPATH,
                                                                                   user_roles_read_ini().get_description_text_box_to_enter_data_by_xpath())
                                        time.sleep(web_driver.one_second)
                                        role_name_text_box.click()
                                        time.sleep(web_driver.two_second)
                                        role_name_text_box.clear()
                                        time.sleep(web_driver.two_second)
                                        role_name_text_box.send_keys(system_level_test_read_ini().get_AB_user_role())
                                        time.sleep(web_driver.one_second)
                                        description_text_box.click()
                                        time.sleep(web_driver.two_second)
                                        description_text_box.clear()
                                        time.sleep(web_driver.two_second)
                                        description_text_box.send_keys(system_level_test_read_ini().get_AB_user_role_description())
                                        time.sleep(web_driver.one_second)
                                        entered_text = role_name_text_box.get_attribute('value')
                                        entered_description = description_text_box.get_attribute('value')
                                        self.logger.info(f"entered role: {entered_text}, \n entered description: {entered_description}")
                                        rights_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rights_checkbox_by_xpath())
                                        rights_check_box.click()
                                        time.sleep(web_driver.one_second)
                                        if entered_text == system_level_test_read_ini().get_AB_user_role():
                                            status.append(True)
                                        else:
                                            status.append(False)
                                        if entered_description == system_level_test_read_ini().get_AB_user_role_description():
                                            status.append(True)
                                            self.logger.info(f"verify: {True}")
                                        else:
                                            self.logger.info(f"verify: {False}")
                                            status.append(False)
                                        if rights_check_box.is_selected():
                                            pass
                                        else:
                                            rights_check_box.click()
                                            time.sleep(web_driver.two_second)
                                        time.sleep(web_driver.two_second)
                                        save_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_save_btn_by_xpath())
                                        save_btn.click()
                                        time.sleep(web_driver.one_second)
                                        user_roles_profile_names = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_name_list_by_xpath())

                                        for name in user_roles_profile_names:
                                            if name.text == system_level_test_read_ini().get_AB_user_role():
                                                self.logger.info(f"{name.text} created successfully...")
                                                self.logger.info("User Created 2.. ")
                                                status.append(True)

                                    else:
                                        self.logger.info("Panel is not opened...")
                                        status.append(False)
                else:
                    self.logger.info("Continue Execution 2..")

                # -------------------------------------------
                time.sleep(web_driver.two_second)
                close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                self.logger.info(f"panel count: {len(close_panel)}")
                close_panel[1].click()
                time.sleep(web_driver.two_second)
                self.logger.info("panel closed 2.")
                self.logger.info(f"panel count: {len(close_panel)}")

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
                                    self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                    if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                        self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                        status.append(True)
                                        # ----------------------------------------
                                        role_name_text_box = self.d.find_element(By.XPATH,
                                                                                 user_roles_read_ini().get_rolename_text_box_to_enter_data_by_xpath())
                                        time.sleep(web_driver.one_second)
                                        description_text_box = self.d.find_element(By.XPATH,
                                                                                   user_roles_read_ini().get_description_text_box_to_enter_data_by_xpath())
                                        time.sleep(web_driver.one_second)
                                        role_name_text_box.click()
                                        time.sleep(web_driver.two_second)
                                        role_name_text_box.clear()
                                        time.sleep(web_driver.two_second)
                                        role_name_text_box.send_keys(system_level_test_read_ini().get_PT_user_role())
                                        time.sleep(web_driver.one_second)
                                        description_text_box.click()
                                        time.sleep(web_driver.two_second)
                                        description_text_box.clear()
                                        time.sleep(web_driver.two_second)
                                        description_text_box.send_keys(system_level_test_read_ini().get_PT_user_role_description())
                                        time.sleep(web_driver.one_second)
                                        entered_text = role_name_text_box.get_attribute('value')
                                        entered_description = description_text_box.get_attribute('value')
                                        self.logger.info(f"entered role: {entered_text}, \n entered description: {entered_description}")
                                        rights_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rights_checkbox_by_xpath())

                                        rights_check_box.click()
                                        time.sleep(web_driver.one_second)
                                        if entered_text == system_level_test_read_ini().get_PT_user_role():
                                            status.append(True)
                                        else:
                                            status.append(False)
                                        if entered_description == system_level_test_read_ini().get_PT_user_role_description():
                                            status.append(True)
                                            self.logger.info(f"verify: {True}")
                                        else:
                                            self.logger.info(f"verify: {False}")
                                            status.append(False)
                                        if rights_check_box.is_selected():
                                            pass
                                        else:
                                            rights_check_box.click()
                                            time.sleep(web_driver.two_second)
                                        time.sleep(web_driver.two_second)
                                        save_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_save_btn_by_xpath())
                                        save_btn.click()
                                        time.sleep(web_driver.one_second)
                                        user_roles_profile_names = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_name_list_by_xpath())

                                        for name in user_roles_profile_names:
                                            if name.text == system_level_test_read_ini().get_PT_user_role():
                                                self.logger.info(f"{name.text} created successfully...")
                                                self.logger.info("User Created 3.. ")
                                                status.append(True)

                                    else:
                                        self.logger.info("Panel is not opened...")
                                        status.append(False)
                else:
                    self.logger.info("Continue Execution 3.. ")

                # -------------------------------------------
                time.sleep(web_driver.two_second)
                close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                self.logger.info(f"panel count: {len(close_panel)}")
                close_panel[1].click()
                time.sleep(web_driver.two_second)
                self.logger.info("panel closed 3.")
                self.logger.info(f"panel count: {len(close_panel)}")

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
                                    self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                    if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                        self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                        status.append(True)
                                        # ----------------------------------------
                                        role_name_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rolename_text_box_to_enter_data_by_xpath())
                                        time.sleep(web_driver.one_second)
                                        description_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_description_text_box_to_enter_data_by_xpath())
                                        time.sleep(web_driver.one_second)
                                        role_name_text_box.click()
                                        time.sleep(web_driver.two_second)
                                        role_name_text_box.clear()
                                        time.sleep(web_driver.two_second)
                                        role_name_text_box.send_keys(system_level_test_read_ini().get_VIP_user_role())
                                        time.sleep(web_driver.one_second)
                                        description_text_box.click()
                                        time.sleep(web_driver.two_second)
                                        description_text_box.clear()
                                        time.sleep(web_driver.two_second)
                                        description_text_box.send_keys(system_level_test_read_ini().get_VIP_user_role_description())
                                        time.sleep(web_driver.one_second)
                                        entered_text = role_name_text_box.get_attribute('value')
                                        entered_description = description_text_box.get_attribute('value')
                                        self.logger.info(f"entered role: {entered_text}, \nentered description: {entered_description}")
                                        rights_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rights_checkbox_by_xpath())

                                        rights_check_box.click()
                                        time.sleep(web_driver.one_second)
                                        if entered_text == system_level_test_read_ini().get_VIP_user_role():
                                            status.append(True)
                                        else:
                                            status.append(False)
                                        if entered_description == system_level_test_read_ini().get_VIP_user_role_description():
                                            status.append(True)
                                            self.logger.info(f"verify: {True}")
                                        else:
                                            self.logger.info(f"verify: {False}")
                                            status.append(False)
                                        if rights_check_box.is_selected():
                                            pass
                                        else:
                                            rights_check_box.click()
                                            time.sleep(web_driver.two_second)
                                        time.sleep(web_driver.two_second)
                                        save_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_save_btn_by_xpath())
                                        save_btn.click()
                                        time.sleep(web_driver.one_second)
                                        user_roles_profile_names = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_name_list_by_xpath())

                                        for name in user_roles_profile_names:
                                            if name.text == system_level_test_read_ini().get_VIP_user_role():
                                                self.logger.info(f"{name.text} created successfully...")
                                                self.logger.info("User Created 4.. ")
                                                status.append(True)

                                    else:
                                        self.logger.info("Panel is not opened...")
                                        status.append(False)
                else:
                    self.logger.info("Continue Execution 4..")

                # -------------------------------------------
                close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                self.logger.info(f"panel count: {len(close_panel)}")
                close_panel[1].click()
                time.sleep(web_driver.two_second)
                self.logger.info("panel closed 4.")
                self.logger.info(f"panel count: {len(close_panel)}")
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
                                    self.logger.info(f"Panel Heading: {user_role_panel_title_list[x].text}")
                                    if user_role_panel_title_list[x].text == user_roles_read_ini().get_user_role_panel_title_text():
                                        self.logger.info(f"Actual Panel Heading: {user_role_panel_title_list[x].text}")
                                        status.append(True)
                                        # ----------------------------------------
                                        role_name_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rolename_text_box_to_enter_data_by_xpath())
                                        time.sleep(web_driver.one_second)
                                        description_text_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_description_text_box_to_enter_data_by_xpath())
                                        time.sleep(web_driver.one_second)
                                        role_name_text_box.click()
                                        time.sleep(web_driver.two_second)
                                        role_name_text_box.clear()
                                        time.sleep(web_driver.two_second)
                                        role_name_text_box.send_keys(system_level_test_read_ini().get_FRAUD_user_role())
                                        time.sleep(web_driver.one_second)
                                        description_text_box.click()
                                        time.sleep(web_driver.two_second)
                                        description_text_box.clear()
                                        time.sleep(web_driver.two_second)
                                        description_text_box.send_keys(system_level_test_read_ini().get_FRAUD_user_role_description())
                                        time.sleep(web_driver.one_second)
                                        entered_text = role_name_text_box.get_attribute('value')
                                        entered_description = description_text_box.get_attribute('value')
                                        self.logger.info(f"entered role: {entered_text}, \nentered description: {entered_description}")
                                        rights_check_box = self.d.find_element(By.XPATH, user_roles_read_ini().get_rights_checkbox_by_xpath())

                                        rights_check_box.click()
                                        time.sleep(web_driver.one_second)
                                        if entered_text == system_level_test_read_ini().get_FRAUD_user_role():
                                            status.append(True)
                                        else:
                                            status.append(False)
                                        if entered_description == system_level_test_read_ini().get_FRAUD_user_role_description():
                                            status.append(True)
                                            self.logger.info(f"verify: {True}")
                                        else:
                                            self.logger.info(f"verify: {False}")
                                            status.append(False)
                                        if rights_check_box.is_selected():
                                            pass
                                        else:
                                            rights_check_box.click()
                                            time.sleep(web_driver.two_second)
                                        time.sleep(web_driver.two_second)
                                        save_btn = self.d.find_element(By.XPATH, user_roles_read_ini().get_save_btn_by_xpath())
                                        save_btn.click()
                                        time.sleep(web_driver.one_second)
                                        user_roles_profile_names = self.d.find_elements(By.XPATH, user_roles_read_ini().get_user_roles_profiles_name_list_by_xpath())
                                        for name in user_roles_profile_names:
                                            if name.text == system_level_test_read_ini().get_FRAUD_user_role():
                                                self.logger.info(f"{name.text} created successfully...")
                                                self.logger.info("User Created 5.. ")
                                                status.append(True)

                                    else:
                                        self.logger.info("Panel is not opened...")
                                        status.append(False)
                else:
                    self.logger.info("Continue Execution 5.. ")

            # ------------------------------------------- #
            time.sleep(web_driver.two_second)
            close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            for panels in close_panel:
                panels.click()
                time.sleep(web_driver.one_second)
            # -------------------------------------------
            self.logger.info(f"status: {status}")
            self.logger.info("TC_SLT_01 execution completed.\n")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_01.failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_01.failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_01_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_01_exception.png")
            self.logger.error(f"TC_SLT_01 got exception as: {ex.args}")

    def select_region(self, region_text):
        """
        This function is used to handle the region drop-down and select the required options
        :param region_text:
        :return:
        """
        region_ele = self.d.find_element(By.XPATH, system_level_test_read_ini().get_region_by_xpath())
        region_ele.click()
        time.sleep(web_driver.one_second)
        region_text_list = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_region_list_by_xpath())
        expected_region_text = region_text
        try:
            for i in range(len(region_text_list) + 1):
                actual_zone_text = region_text_list.__getitem__(i).text
                self.logger.info(f"Region selected: {actual_zone_text}")
                # self.logger.info(f"{expected_region_text}")
                if expected_region_text.upper() in actual_zone_text.upper():
                    region_text_list.__getitem__(i).click()
                    break
            time.sleep(web_driver.one_second)
            save = self.d.find_element(By.XPATH, system_level_test_read_ini().get_region_save_btn_by_xpath())
            save.click()
            time.sleep(web_driver.one_second)
            # self.d.execute_script("arguments[0].click();", save)
        except Exception as ex:
            str(ex)

    def validate_successful_message(self):
        """
        checks if the error message "Success! A user has been created." is displayed.
        """
        ex_result = [True, True]
        ac_result = []
        time.sleep(web_driver.one_second)
        ele = self.d.find_element(By.XPATH, system_level_test_read_ini().get_success_message_by_xpath())
        msg_validation = ele.text
        self.logger.info(f"element is displayed: {ele.is_displayed()}, text: {ele.text}")
        self.logger.info(f"actual message: {msg_validation}")
        self.logger.info(f"expected message: {system_level_test_read_ini().get_success_msg_validation_text()}")
        ac_result.append(msg_validation == system_level_test_read_ini().get_success_msg_validation_text())
        ac_result.append(ele.is_displayed())
        if ex_result == ac_result:
            return True
        else:
            return False

    def creating_dummy_user_with_firstname_lastname_user_role_password_region_email_timezone_display_success_msg(self):
        try:
            self.logger.info("********** Test_SLT_02 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            # self.click_user_on_cloud_menu()
            # self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Users_menu_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            # action_dropdown = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_user_panel_by_xpath())
            # action_dropdown.click()
            # options_inside_action_dropdown_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
            # self.logger.info(f"options inside action: {len(options_inside_action_dropdown_list)}")
            # if len(options_inside_action_dropdown_list) > 0:
            #     for option in options_inside_action_dropdown_list:
            #         if option.text != "":
            #             if option.text == "Create User":
            #                 option.click()
            #
            #     time.sleep(web_driver.one_second)

            # ------------------------------------------------

            x = system_level_test_read_ini().get_user_name_input_data()
            username = x.split(',')
            self.logger.info(f"username list: {username}")
            for user in username:
                self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Users_menu_by_xpath()).click()
                time.sleep(web_driver.one_second)
                action_dropdown = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_user_panel_by_xpath())
                action_dropdown.click()
                time.sleep(web_driver.one_second)
                options_inside_action_dropdown_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                self.logger.info(f"options inside action: {len(options_inside_action_dropdown_list)}")
                if len(options_inside_action_dropdown_list) > 0:
                    for option in options_inside_action_dropdown_list:
                        if option.text != "":
                            if option.text == "Create User":
                                option.click()
                time.sleep(web_driver.one_second)

                user_name_txt_bx = self.d.find_element(By.XPATH, system_level_test_read_ini().get_user_name_textbox_by_xpath())
                user_name_txt_bx.send_keys(user)
                time.sleep(web_driver.one_second)
                first_name_txt_bx = self.d.find_element(By.XPATH, user_roles_read_ini().get_first_name_textbox_by_xpath())
                first_name_txt_bx.send_keys(system_level_test_read_ini().get_first_name_input_data())
                time.sleep(web_driver.one_second)
                last_name_txt_bx = self.d.find_element(By.XPATH, user_roles_read_ini().get_lastname_textbox_by_xpath())
                last_name_txt_bx.send_keys(system_level_test_read_ini().get_last_name_input_data())
                time.sleep(web_driver.one_second)
                user_role_dropdown = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_dropdown_by_xpath())
                user_role_dropdown.click()
                time.sleep(web_driver.one_second)
                role_options_inside_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_role_option_in_user_role_dropdown_by_xpath())
                count = 0
                for role in role_options_inside_dropdown:
                    if role.text == system_level_test_read_ini().get_SO_user_role():
                        self.logger.info(f"User role: '{system_level_test_read_ini().get_SO_user_role()}' is visible..")
                        count = count + 1
                        if role.is_enabled():
                            role.click()
                            status.append(True)
                        else:
                            self.logger.info("User role is not clickable...")
                            status.append(False)
                if count == 1:
                    status.append(True)
                else:
                    self.logger.info("Created user role is not visible...")
                # ------------------------------------------------------ #
                time.sleep(web_driver.one_second)
                new_password = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_new_password_textbox_by_xpath())
                time.sleep(web_driver.one_second)
                confirm_password = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_confirm_password_textbox_by_xpath())
                time.sleep(web_driver.one_second)
                new_password.send_keys(system_level_test_read_ini().get_password_data_input())
                time.sleep(web_driver.one_second)
                confirm_password.send_keys(system_level_test_read_ini().get_password_data_input())
                time.sleep(web_driver.one_second)
                self.select_region(system_level_test_read_ini().get_region_data_input())

                email_txt_bx = self.d.find_element(By.XPATH, system_level_test_read_ini().get_email_by_xpath())
                email = f"{user}@facefirst.com"
                email_txt_bx.send_keys(email)
                time.sleep(web_driver.one_second)
                # email_txt_bx.send_keys(system_level_test_read_ini().get_email_input_data())

                time_zone = self.d.find_element(By.XPATH, system_level_test_read_ini().get_time_zone_by_xpath())
                select = Select(time_zone)
                time.sleep(web_driver.one_second)
                select.select_by_value(system_level_test_read_ini().get_time_zone_input_data())
                time.sleep(web_driver.one_second)
                save = self.d.find_element(By.XPATH, system_level_test_read_ini().get_user_panel_save_button_by_xpath())
                save.click()
                time.sleep(web_driver.one_second)
                status.append(self.validate_successful_message())
                time.sleep(web_driver.one_second)
                close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                time.sleep(web_driver.one_second)

                for panels in close_panel:
                    panels.click()
                    time.sleep(web_driver.one_second)
                # warning_pop_up_close_and_discard_changes_btn_by_xpath = self.d.find_element(By.XPATH,
                #                                                                             system_level_test_read_ini().warning_pop_up_close_and_discard_changes_btn_by_xpath())
                # self.explicit_wait(5, warning_pop_up_close_and_discard_changes_btn_by_xpath, self.d)
                # if warning_pop_up_close_and_discard_changes_btn_by_xpath.is_displayed():
                #     self.logger.info("warning msg displayed.")
                #     warning_pop_up_close_and_discard_changes_btn_by_xpath.click()
                # else:
                #     self.logger.info("warning msg not displayed.")
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_02_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_02_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_02_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_02_exception.png")
            self.logger.error(f"TC_SLT_02 got exception as: {ex.args}")
            return False

    def creating_dummy_Notification_Groups_Functionality_by_filling_Name_and_Description_data_it_should_displayed_Success_the_alert_below_has_been_created_message(self):
        try:
            self.logger.info("********** Test_SLT_03 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            x = system_level_test_read_ini().get_notification_group_name()
            notification_group_names_list = x.split(',')
            self.logger.info(f"notification Groups List: {notification_group_names_list}")
            for ng in notification_group_names_list:
                notification_groups_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().notification_groups_button_by_xpath())
                time.sleep(web_driver.one_second)
                self.d.execute_script("arguments[0].click();", notification_groups_btn)
                action_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().action_dropdown_button_by_xpath())
                time.sleep(web_driver.two_second)
                action_btn.click()
                time.sleep(web_driver.one_second)
                create_notification = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().create_notification_group_btn_by_xpath())
                create_notification.click()
                time.sleep(web_driver.one_second)
                # name_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().name_field_by_xpath())
                name_field = web_driver.explicit_wait(self, 10, "XPATH", Read_Notification_Groups_Components().name_field_by_xpath(), self.d)
                name_field.send_keys(ng)
                time.sleep(web_driver.one_second)
                description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().description_field_by_xpath())
                description_field.send_keys(system_level_test_read_ini().get_notification_group_description())
                time.sleep(web_driver.one_second)
                save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
                time.sleep(web_driver.one_second)
                save_button.click()
                time.sleep(web_driver.two_second)
                status.append(Notification_Groups_Module_pom().validate_successful_message())
                time.sleep(web_driver.one_second)
                close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                for panels in close_panel:
                    panels.click()
                    time.sleep(web_driver.one_second)

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_03_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_03_failed.png")
                return False
            else:
                return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_03_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_03_exception.png")
            self.logger.error(f"TC_SLT_03 got exception as: {ex.args}")
            return False

    def creating_dummy_enrollment_group_by_filling_name_description_data_success_message(self):
        try:
            self.logger.info("********** Test_SLT_04 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            x = system_level_test_read_ini().get_enrollment_group_name()
            enrollment_group_names_list = x.split(',')
            self.logger.info(f"eg list: {enrollment_group_names_list}")
            for eg in enrollment_group_names_list:
                time.sleep(web_driver.one_second)
                enrollment_groups_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Enrollment_Groups_menu_by_xpath())
                time.sleep(web_driver.one_second)
                enrollment_groups_btn.click()
                time.sleep(web_driver.one_second)
                # action_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().action_dropdown_button_by_xpath())
                action_btn = web_driver.explicit_wait(self, 5, "XPATH", Read_Notification_Groups_Components().action_dropdown_button_by_xpath(), self.d)
                time.sleep(web_driver.one_second)
                action_btn.click()
                time.sleep(web_driver.one_second)
                create_enrollment = self.d.find_element(By.XPATH, system_level_test_read_ini().get_create_enrollment_group_btn_by_xpath())
                create_enrollment.click()
                time.sleep(web_driver.one_second)

                name_field = self.d.find_element(By.XPATH, system_level_test_read_ini().get_name_field_by_xpath())
                name_field.send_keys(eg)
                time.sleep(web_driver.one_second)
                description_field = self.d.find_element(By.XPATH, system_level_test_read_ini().get_description_field_by_xpath())
                description_field.send_keys(system_level_test_read_ini().get_enrollment_group_description())
                time.sleep(web_driver.one_second)
                save_button = self.d.find_element(By.XPATH, system_level_test_read_ini().get_save_button_on_enrollment_group_by_xpath())
                time.sleep(web_driver.one_second)
                save_button.click()

                time.sleep(web_driver.two_second)
                success_message = self.d.find_element(By.XPATH, system_level_test_read_ini().get_enrollment_group_success_message_by_xpath()).text
                self.logger.info(f"actual message: {success_message}")
                ex_success_msg = system_level_test_read_ini().get_enrollment_group_success_message_validation_text()
                self.logger.info(f"expected message: {ex_success_msg}")
                if ex_success_msg == success_message:
                    status.append(True)
                else:
                    status.append(False)
                close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                time.sleep(web_driver.one_second)
                for panels in close_panel:
                    panels.click()
                    time.sleep(web_driver.one_second)

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_04_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_04_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_04_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_04_exception.png")
            self.logger.error(f"TC_SLT_04 got exception as: {ex.args}")
            return False

    def users_notification_group_enrollment_group_bottom_up_integration(self):
        try:
            self.logger.info("********** Test_SLT_05 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            # self.click_user_on_cloud_menu()
            ur_list = []
            ab_ur = system_level_test_read_ini().get_AB_user_role()
            pt_ur = system_level_test_read_ini().get_PT_user_role()
            so_ur = system_level_test_read_ini().get_SO_user_role()
            vip_ur = system_level_test_read_ini().get_VIP_user_role()
            fraud = system_level_test_read_ini().get_FRAUD_user_role()
            ur_list.append(ab_ur)
            ur_list.append(pt_ur)
            ur_list.append(so_ur)
            ur_list.append(vip_ur)
            ur_list.append(fraud)
            self.logger.info(f"user role list: {ur_list}")
            # ------------------------------------------------

            x = system_level_test_read_ini().get_user_name_input_data()
            username = x.split(',')
            self.logger.info(f"username list: {username}")
            y = system_level_test_read_ini().get_notification_group_name()
            notification_group_names_list = y.split(',')
            self.logger.info(f"ng list: {notification_group_names_list}")
            z = system_level_test_read_ini().get_enrollment_group_name()
            enrollment_group_names_list = z.split(',')
            self.logger.info(f"eg list: {enrollment_group_names_list}")
            # for user_index in range(len(username)):
            #     # users_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Users_menu_by_xpath())
            time.sleep(web_driver.one_second)
            users_menu = web_driver.explicit_wait(self, 10, "XPATH", Portal_Menu_Module_read_ini().get_Users_menu_by_xpath(), self.d)
            users_menu.click()
            time.sleep(web_driver.one_second)

            for u in range(len(username)):
                time.sleep(web_driver.one_second)
                print("username length:", len(username))
                user_search_filter = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())

                user_search_filter.clear()
                time.sleep(web_driver.one_second)
                user_search_filter.send_keys(username[u])
                time.sleep(web_driver.two_second)
                # action_dropdown = self.d.find_element(By.XPATH,
                #                                       user_roles_read_ini().get_action_dropdown_user_panel_by_xpath())
                # action_dropdown.click()
                # options_inside_action_dropdown_list = self.d.find_elements(By.XPATH,
                #                                                            user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                # if len(options_inside_action_dropdown_list) > 0:
                #     for option in options_inside_action_dropdown_list:
                #         if option.text != "":
                #             if option.text == "Create User":
                #                 option.click()
                #     time.sleep(web_driver.one_second)
                #
                # user_name_txt_bx = self.d.find_element(By.XPATH, system_level_test_read_ini().get_user_name_textbox_by_xpath())
                # user_name_txt_bx.send_keys(username[user_index])
                #
                # first_name_txt_bx = self.d.find_element(By.XPATH, user_roles_read_ini().get_first_name_textbox_by_xpath())
                # first_name_txt_bx.send_keys(system_level_test_read_ini().get_first_name_input_data())
                #
                # last_name_txt_bx = self.d.find_element(By.XPATH, user_roles_read_ini().get_lastname_textbox_by_xpath())
                # last_name_txt_bx.send_keys(system_level_test_read_ini().get_last_name_input_data())
                #
                # user_role_dropdown = self.d.find_element(By.XPATH,
                #                                          user_roles_read_ini().get_user_role_dropdown_by_xpath())
                # user_role_dropdown.click()
                # time.sleep(web_driver.one_second)
                # role_options_inside_dropdown = self.d.find_elements(By.XPATH,
                #                                                     user_roles_read_ini().get_role_option_in_user_role_dropdown_by_xpath())
                # count = 0
                #
                # for role in role_options_inside_dropdown:
                #     if role.text == ur_list[user_index]:
                #         self.logger.info(f"User role: '{ur_list[user_index]}' is visible..")
                #         count = count + 1
                #         if role.is_enabled():
                #             role.click()
                #             status.append(True)
                #         else:
                #             self.logger.info("User role is not clickable...")
                #             status.append(False)
                # if count == 1:
                #     status.append(True)
                # else:
                #     self.logger.info("Created user role is not visible...")
                # # ------------------------------------------------------
                # new_password = self.d.find_element(By.XPATH,
                #                                    Portal_Menu_Module_read_ini().get_new_password_textbox_by_xpath())
                # confirm_password = self.d.find_element(By.XPATH,
                #                                        Portal_Menu_Module_read_ini().get_confirm_password_textbox_by_xpath())
                # new_password.send_keys(system_level_test_read_ini().get_password_data_input())
                # confirm_password.send_keys(system_level_test_read_ini().get_password_data_input())
                #
                # self.select_region(system_level_test_read_ini().get_region_data_input())
                #
                # email_txt_bx = self.d.find_element(By.XPATH, system_level_test_read_ini().get_email_by_xpath())
                # email_txt_bx.send_keys(system_level_test_read_ini().get_email_input_data())
                #
                # time_zone = self.d.find_element(By.XPATH, system_level_test_read_ini().get_time_zone_by_xpath())
                # select = Select(time_zone)
                # select.select_by_value(system_level_test_read_ini().get_time_zone_input_data())
                # time.sleep(web_driver.one_second)
                # save = self.d.find_element(By.XPATH, system_level_test_read_ini().get_user_panel_save_button_by_xpath())
                # save.click()
                # time.sleep(web_driver.one_second)
                # status.append(self.validate_successful_message())
                # time.sleep(web_driver.one_second)
                notification_group_icon = self.d.find_element(By.XPATH, system_level_test_read_ini().get_notification_group_icon_btn_on_users_panel_by_xpath())
                time.sleep(web_driver.one_second)
                notification_group_icon.click()
                time.sleep(web_driver.one_second)
                # filter_button_on_alert = self.d.find_element(By.XPATH, system_level_test_read_ini().get_filter_btn_on_notification_groups_panel_by_xpath())
                filter_button_on_alert = web_driver.explicit_wait(self, 10, "XPATH", system_level_test_read_ini().get_filter_btn_on_notification_groups_panel_by_xpath(), self.d)
                # filter_button = web_driver.explicit_wait(self, 5, "XPATH", filter_button_on_alert, self.d)

                if filter_button_on_alert.is_displayed():
                    filter_button_on_alert.click()
                    self.status.append(True)
                else:
                    self.status.append(False)
                time.sleep(web_driver.one_second)
                unlinked_notification_groups = self.d.find_element(By.XPATH, system_level_test_read_ini().get_unlinked_notification_groups_btn_by_xpath())
                unlinked_notification_groups.click()
                time.sleep(web_driver.one_second)
                alert_groups = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_group_list_by_xpath())
                time.sleep(web_driver.one_second)
                checkbox = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_checkbox_by_xpath())
                time.sleep(web_driver.one_second)
                for i in range(len(alert_groups)):
                    self.logger.info(f"{len(alert_groups)}")
                    self.logger.info(f"i:{i}")
                    if alert_groups[i].text == notification_group_names_list[u]:

                        checkbox[i].click()
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH, system_level_test_read_ini().get_action_dropdown_on_notification_groups_panel_by_xpath()).click()
                        time.sleep(web_driver.one_second)
                        # add_to_user = self.d.find_element(By.XPATH, system_level_test_read_ini().get_add_to_user_option_in_action_dropdown_by_xpath())
                        add_to_user = web_driver.explicit_wait(self, 10, "XPATH", system_level_test_read_ini().get_add_to_user_option_in_action_dropdown_by_xpath(), self.d)
                        add_to_user.click()
                        time.sleep(web_driver.two_second)
                        alert_groups = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_group_list_by_xpath())

                        # enrollment_groups_btn = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_enrollment_groups_btn_on_notification_panel_by_xpath())
                        enrollment_groups_btn = web_driver.explicit_wait(self, 10, "XPATH", system_level_test_read_ini().get_enrollment_groups_btn_on_notification_panel_by_xpath(), self.d)
                        enrollment_groups_btn = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_enrollment_groups_btn_on_notification_panel_by_xpath())
                        self.logger.info(f"notification group length: {len(alert_groups)}")
                        self.logger.info(f"Enrollment Groups Btn: {len(enrollment_groups_btn)}")
                        for j in range(len(alert_groups)):
                            self.logger.info(f"{len(alert_groups)}")
                            self.logger.info(f"j:{j}")
                            if alert_groups[j].text == notification_group_names_list[u]:

                                self.logger.info(f"{notification_group_names_list[u]} alert group linked successfully with user..")
                                status.append(True)
                                enrollment_groups_btn[j].click()
                                time.sleep(web_driver.one_second)
                                filter_btn_on_case = self.d.find_element(By.XPATH, system_level_test_read_ini().get_filter_dropdown_on_enrollment_groups_panel_by_xpath())
                                filter_btn_on_case.click()
                                time.sleep(web_driver.two_second)
                                unlinked_enrollment_groups = self.d.find_element(By.XPATH, system_level_test_read_ini().get_unlinked_enrollment_groups_btn_by_xpath())
                                unlinked_enrollment_groups.click()
                                time.sleep(web_driver.two_second)
                                cases_list = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_unlinked_enrollment_groups_by_xpath())
                                cases_checkboxes = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_checkboxes_on_enrollment_groups_panel_by_xpath())
                                self.logger.info(f"unlinked enrollment groups list length: {len(cases_list)}")
                                self.logger.info(f"unlinked enrollment groups checkboxes list length: {len(cases_checkboxes)}")
                                time.sleep(web_driver.one_second)

                                for k in range(len(cases_list)):
                                    self.logger.info(f"{len(cases_list)}")
                                    self.logger.info(f"k:{k}")
                                    if cases_list[k].text == enrollment_group_names_list[u]:
                                        status.append(True)
                                        cases_checkboxes[k].click()
                                        time.sleep(web_driver.one_second)
                                        self.d.find_element(By.XPATH, system_level_test_read_ini().get_action_dropdown_on_enrollment_groups_panel_by_xpath()).click()
                                        time.sleep(web_driver.one_second)
                                        add_to_alert = self.d.find_element(By.XPATH, system_level_test_read_ini().get_add_alert_to_groups_btn_by_xpath())
                                        add_to_alert.click()
                                        time.sleep(web_driver.two_second)
                                        linked_cases_list = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_linked_enrollment_groups_by_xpath())
                                        time.sleep(web_driver.one_second)

                                        # for z in range(len(linked_cases_list)):
                                        #     self.logger.info(f"linking enrollment groups: {enrollment_group_names_list[u]}")
                                        #     self.logger.info(f"{len(linked_cases_list)}")
                                        #     self.logger.info(f"z:{z}")
                                        #     if linked_cases_list[z].text == enrollment_group_names_list[u]:
                                        #
                                        #         status.append(True)
                                        #         self.logger.info(f"{enrollment_group_names_list[u]} enrollment group linked successfully with user..")
                                        #         time.sleep(web_driver.one_second)
                                        #
                                        #
                                        #     self.logger.info("enrollment groups inner loop")
                                                # break
                                        # cases_list = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_unlinked_enrollment_groups_by_xpath())
                                        self.logger.info("enrollment group .")
                                        close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                                        for c in range(len(close_panel) - 1):
                                            close_panel[c + 1].click()
                                            time.sleep(web_driver.one_second)
                                        break
                                break
                            # alert_groups = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_group_list_by_xpath())
                        self.logger.info("Notification Group inner loop ")
                        break
                    # alert_groups = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_group_list_by_xpath())
                self.logger.info("Notification Group broken..")
            close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            time.sleep(web_driver.one_second)
            for panels in close_panel:
                panels.click()
                time.sleep(web_driver.one_second)
            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(
                    f"screenshot file path: {self.screenshots_path}\\TC_SLT_05_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_05_failed.png")
                return False
            else:
                return True
                # ------------------------------------------------------------------------
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_05_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_05_exception.png")
            self.logger.error(f"TC_SLT_05 got exception as: {ex.args}")
            return False

    def enrollment_group_notification_group_users_top_down_integration(self):
        try:
            self.logger.info("********** Test_SLT_06 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            enrollment_groups_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Enrollment_Groups_menu_by_xpath())
            time.sleep(web_driver.one_second)
            enrollment_groups_btn.click()
            time.sleep(web_driver.one_second)
            action_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().action_dropdown_button_by_xpath())
            time.sleep(web_driver.one_second)
            action_btn.click()
            time.sleep(web_driver.one_second)
            create_enrollment = self.d.find_element(By.XPATH, system_level_test_read_ini().get_create_enrollment_group_btn_by_xpath())
            create_enrollment.click()
            time.sleep(web_driver.one_second)
            name_field = web_driver.explicit_wait(self, 10, "XPATH", system_level_test_read_ini().get_name_field_by_xpath(), self.d)
            # name_field = self.d.find_element(By.XPATH, system_level_test_read_ini().get_name_field_by_xpath())
            x = system_level_test_read_ini().get_enrollment_group_name_integration()
            enrollment_group_names_list = x.split(',')
            name_field.send_keys(enrollment_group_names_list[0])
            time.sleep(web_driver.one_second)
            description_field = self.d.find_element(By.XPATH, system_level_test_read_ini().get_description_field_by_xpath())
            description_field.send_keys(system_level_test_read_ini().get_enrollment_group_description())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, system_level_test_read_ini().get_save_button_on_enrollment_group_by_xpath())
            time.sleep(web_driver.one_second)
            save_button.click()
            time.sleep(web_driver.one_second)
            ex_success_msg = system_level_test_read_ini().get_enrollment_group_success_message_validation_text()
            time.sleep(web_driver.one_second)
            success_message = self.d.find_element(By.XPATH, system_level_test_read_ini().get_enrollment_group_success_message_by_xpath()).text
            if ex_success_msg == success_message:
                status.append(True)
            else:
                status.append(False)
            time.sleep(web_driver.one_second)
            notification_group_btn = self.d.find_element(By.XPATH, system_level_test_read_ini().get_notification_group_btn_on_cases_panel_by_xpath())
            notification_group_btn.click()
            time.sleep(web_driver.one_second)
            filter_button_on_alert = self.d.find_element(By.XPATH, system_level_test_read_ini().get_filter_btn_on_notification_groups_panel_by_xpath())
            filter_button_on_alert.click()
            time.sleep(web_driver.two_second)
            unlinked_notification_groups = self.d.find_element(By.XPATH, system_level_test_read_ini().get_unlinked_notification_groups_btn_by_xpath())
            unlinked_notification_groups.click()
            time.sleep(web_driver.one_second)
            alert_groups = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_group_list_by_xpath())
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_checkbox_by_xpath())
            x = system_level_test_read_ini().get_notification_group_name()
            notification_group_names_list = x.split(',')
            count1 = 0
            for i in range(len(alert_groups)):
                if alert_groups[i].text == notification_group_names_list[0]:
                    count1 = count1 + 1
                    checkbox[i].click()
                    time.sleep(web_driver.one_second)
                    self.d.find_element(By.XPATH, system_level_test_read_ini().get_action_dropdown_on_notification_groups_panel_by_xpath()).click()
                    time.sleep(web_driver.one_second)
                    add_to_enrollment_group = self.d.find_element(By.XPATH, system_level_test_read_ini().get_add_to_enrollment_groups_option_by_xpath())
                    add_to_enrollment_group.click()
                    time.sleep(web_driver.one_second)
                    alert_groups = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_group_list_by_xpath())
                    time.sleep(web_driver.one_second)
                    users_btn = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_users_btn_on_notification_groups_panel_by_xpath())
                    for j in range(len(alert_groups)):
                        if alert_groups[j].text == notification_group_names_list[0]:
                            self.logger.info(
                                f"{notification_group_names_list[0]} alert group linked successfully with enrollment group..")
                            status.append(True)
                            users_btn[j].click()
                            time.sleep(web_driver.one_second)
                            filter_button_on_users = self.d.find_element(By.XPATH, system_level_test_read_ini().get_filter_btn_on_users_panel_by_xpath())
                            filter_button_on_users.click()
                            time.sleep(web_driver.one_second)
                            unlinked_users = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().user_filter_drp_dwn_button_by_xpath())
                            unlinked_users.click()
                            time.sleep(web_driver.two_second)
                            users_list = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_users_list_by_xpath())
                            time.sleep(web_driver.one_second)
                            cases_checkboxes = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_checkboxes_on_users_panel_by_xpath())
                            x = system_level_test_read_ini().get_user_name_input_data()
                            user_names_list = x.split(',')
                            time.sleep(web_driver.one_second)
                            for k in range(len(users_list)):
                                if users_list[k].text == user_names_list[1]:
                                    status.append(True)
                                    cases_checkboxes[k].click()
                                    self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_user_panel_by_xpath()).click()
                                    time.sleep(web_driver.one_second)
                                    add_user_to_alert = self.d.find_element(By.XPATH, system_level_test_read_ini().get_add_users_to_alert_btn_by_xpath())
                                    add_user_to_alert.click()
                                    time.sleep(web_driver.one_second)
                                    users_list = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_users_list_by_xpath())
                                    for z in range(len(users_list)):
                                        if users_list[z].text == user_names_list[0]:
                                            status.append(True)
                                            self.logger.info(f"{user_names_list[0]} user linked successfully with enrollment group..")
                                            time.sleep(web_driver.one_second)
                                            close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                                            time.sleep(web_driver.one_second)
                                            for panels in close_panel:
                                                panels.click()
                                                time.sleep(web_driver.one_second)

                                            self.logger.info(f"status: {status}")
                                            if False in status:
                                                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_06_failed.png")
                                                self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_06_failed.png")
                                                return False
                                            else:
                                                return True
            # -----------------------------------------------------------------
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_06_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_06_exception.png")
            self.logger.error(f"TC_SLT_06 got exception as: {ex.args}")
            return False

    def Creating_Notification_Group_from_Users_panel(self):
        try:
            self.logger.info("********** Test_SLT_7 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            # users_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Users_menu_by_xpath()).click()
            users_menu = web_driver.explicit_wait(self, 5, "XPATH", Portal_Menu_Module_read_ini().get_Users_menu_by_xpath(), self.d)
            users_menu.click()
            time.sleep(web_driver.one_second)
            users_list = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_users_list_by_xpath())
            alert_icons = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_notification_group_icon_btn_on_users_panel_by_xpath())
            x = system_level_test_read_ini().get_user_name_input_data()
            username = x.split(',')
            for i in range(len(users_list)):
                if users_list[i].text == username[0]:
                    alert_icons[i].click()
                    status.append(True)
                    time.sleep(web_driver.one_second)
                    action_btn = self.d.find_element(By.XPATH, system_level_test_read_ini().get_action_dropdown_on_notification_groups_panel_by_xpath())
                    action_btn.click()
                    time.sleep(web_driver.one_second)
                    create_notification = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().create_notification_group_btn_by_xpath())
                    create_notification.click()
                    time.sleep(web_driver.one_second)
                    name_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().name_field_by_xpath())

                    x = system_level_test_read_ini().get_dummy_notification_group_name_1()
                    notification_group_names_list = x.split(',')
                    name_field.send_keys(notification_group_names_list[1])
                    time.sleep(web_driver.one_second)
                    description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().description_field_by_xpath())
                    description_field.send_keys(system_level_test_read_ini().get_notification_group_description())
                    time.sleep(web_driver.one_second)
                    save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
                    save_button.click()
                    time.sleep(web_driver.two_second)
                    actual_message = self.d.find_element(By.XPATH, system_level_test_read_ini().get_success_message_on_alert_group_creation_by_xpath()).text
                    time.sleep(web_driver.one_second)
                    self.logger.info(f"actual message: {actual_message}")
                    expected_message = Read_Notification_Groups_Components().success_message_validation_text()
                    self.logger.info(f"expected message: {expected_message}")
                    if actual_message == expected_message:
                        status.append(True)
                    else:
                        status.append(False)
                    time.sleep(web_driver.one_second)
                    close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                    for panels in close_panel:
                        panels.click()
                        time.sleep(web_driver.one_second)
                    time.sleep(web_driver.one_second)
                    self.logger.info(f"status: {status}")
                    if False in status:
                        self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_7_failed.png")
                        self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_7_failed.png")
                        return False
                    else:
                        return True

            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_7_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_7_exception.png")
            self.logger.error(f"TC_SLT_7 got exception as: {ex.args}")
            return False

    def Creating_User_and_Enrollment_Group_from_Notification_Group_panel(self):
        try:
            self.logger.info("********** Test_SLT_8 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            # notification_groups_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().notification_groups_button_by_xpath())
            ng_btn = web_driver.explicit_wait(self, 5, "XPATH", Read_Notification_Groups_Components().notification_groups_button_by_xpath(), self.d)
            self.logger.info("ng btn displayed.")
            self.d.execute_script("arguments[0].click();", ng_btn)
            self.logger.info("ng btn clicked.")
            time.sleep(web_driver.one_second)
            alert = web_driver.explicit_wait(self, 5, "XPATH", Read_Notification_Groups_Components().alert_group_list_by_xpath(), self.d)
            alert_groups = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_group_list_by_xpath())
            time.sleep(web_driver.one_second)
            user_icons = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_users_btn_on_notification_groups_panel_by_xpath())
            x = system_level_test_read_ini().get_notification_group_name()
            notification_names_list = x.split(',')
            for i in range(len(alert_groups)):
                if alert_groups[i].text == notification_names_list[0]:
                    user_icons[i].click()
                    status.append(True)
                    time.sleep(web_driver.one_second)
                    action_dropdown = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_user_panel_by_xpath())
                    action_dropdown.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown_list) > 0:
                        for option in options_inside_action_dropdown_list:
                            if option.text != "":
                                if option.text == "Create User":
                                    option.click()
                        time.sleep(web_driver.one_second)

                    # ------------------------------------------------

                    x = system_level_test_read_ini().get_user_name_integration()
                    username = x.split(',')
                    user_name_txt_bx = self.d.find_element(By.XPATH, system_level_test_read_ini().get_user_name_textbox_by_xpath())
                    time.sleep(web_driver.one_second)
                    user_name_txt_bx.send_keys(username[0])
                    time.sleep(web_driver.one_second)
                    first_name_txt_bx = self.d.find_element(By.XPATH, user_roles_read_ini().get_first_name_textbox_by_xpath())
                    time.sleep(web_driver.one_second)
                    first_name_txt_bx.send_keys(system_level_test_read_ini().get_first_name_input_data())
                    time.sleep(web_driver.one_second)
                    last_name_txt_bx = self.d.find_element(By.XPATH, user_roles_read_ini().get_lastname_textbox_by_xpath())
                    time.sleep(web_driver.one_second)
                    last_name_txt_bx.send_keys(system_level_test_read_ini().get_last_name_input_data())
                    time.sleep(web_driver.one_second)
                    user_role_dropdown = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_dropdown_by_xpath())
                    user_role_dropdown.click()
                    time.sleep(web_driver.one_second)
                    role_options_inside_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_role_option_in_user_role_dropdown_by_xpath())
                    count = 0
                    for role in role_options_inside_dropdown:
                        if role.text == system_level_test_read_ini().get_SO_user_role():
                            # self.logger.info(f"User role: '{system_level_test_read_ini().get_SO_user_role()}' is visible..")
                            count = count + 1
                            if role.is_enabled():
                                role.click()
                                status.append(True)
                            else:
                                self.logger.info("User role is not clickable...")
                                status.append(False)
                    if count == 1:
                        status.append(True)
                    else:
                        self.logger.info("Created user role is not visible...")
                    # ------------------------------------------------------
                    time.sleep(web_driver.one_second)
                    new_password = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_new_password_textbox_by_xpath())
                    time.sleep(web_driver.one_second)
                    confirm_password = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_confirm_password_textbox_by_xpath())
                    new_password.send_keys(system_level_test_read_ini().get_password_data_input())
                    time.sleep(web_driver.one_second)
                    confirm_password.send_keys(system_level_test_read_ini().get_password_data_input())

                    self.select_region(system_level_test_read_ini().get_region_data_input())
                    time.sleep(web_driver.one_second)
                    email_txt_bx = self.d.find_element(By.XPATH, system_level_test_read_ini().get_email_by_xpath())
                    email_txt_bx.send_keys(system_level_test_read_ini().get_email_input_data())
                    time.sleep(web_driver.one_second)
                    time_zone = self.d.find_element(By.XPATH, system_level_test_read_ini().get_time_zone_by_xpath())
                    select = Select(time_zone)
                    select.select_by_value(system_level_test_read_ini().get_time_zone_input_data())
                    time.sleep(web_driver.one_second)
                    save = self.d.find_element(By.XPATH, system_level_test_read_ini().get_user_panel_save_button_by_xpath())
                    save.click()
                    time.sleep(web_driver.one_second)
                    status.append(self.validate_successful_message())
                    time.sleep(web_driver.one_second)
                    close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                    for panels in close_panel:
                        panels.click()
                        time.sleep(web_driver.one_second)
                    # ---------------------------------------------------------------------------------------------
                    time.sleep(web_driver.one_second)
                    notification_groups_btn = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().notification_groups_button_by_xpath())
                    time.sleep(web_driver.one_second)
                    notification_groups_btn.click()
                    time.sleep(web_driver.one_second)
                    cases_icon = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_enrollment_groups_btn_on_notification_panel_by_xpath())
                    time.sleep(web_driver.one_second)
                    alert_groups = self.d.find_elements(By.XPATH, Read_Notification_Groups_Components().alert_group_list_by_xpath())
                    for j in range(len(alert_groups)):
                        if alert_groups[j].text == notification_names_list[0]:
                            cases_icon[j].click()
                            status.append(True)
                            time.sleep(web_driver.one_second)
                            web_driver.explicit_wait(self, 5, "XPATH", system_level_test_read_ini().get_action_dropdown_on_enrollment_groups_panel_by_xpath(), self.d)
                            action_btn = self.d.find_element(By.XPATH, system_level_test_read_ini().get_action_dropdown_on_enrollment_groups_panel_by_xpath())
                            time.sleep(web_driver.one_second)
                            action_btn.click()
                            time.sleep(web_driver.one_second)
                            create_enrollment = self.d.find_element(By.XPATH, system_level_test_read_ini().get_create_enrollment_group_btn_by_xpath())
                            create_enrollment.click()
                            time.sleep(web_driver.one_second)
                            name_field = self.d.find_element(By.XPATH, system_level_test_read_ini().get_name_field_by_xpath())
                            x = system_level_test_read_ini().get_dummy_enrollment_group_name()
                            enrollment_group_names_list = x.split(',')
                            name_field.send_keys(enrollment_group_names_list[1])
                            time.sleep(web_driver.one_second)
                            description_field = self.d.find_element(By.XPATH, system_level_test_read_ini().get_description_field_by_xpath())
                            description_field.send_keys(system_level_test_read_ini().get_enrollment_group_description())
                            time.sleep(web_driver.one_second)
                            save_button = self.d.find_element(By.XPATH, system_level_test_read_ini().get_save_button_on_enrollment_group_by_xpath())
                            time.sleep(web_driver.one_second)
                            save_button.click()
                            time.sleep(web_driver.two_second)
                            success_message = self.d.find_element(By.XPATH, system_level_test_read_ini().get_success_message_on_case_group_creation_by_xpath()).text
                            self.logger.info(f"actual message: {success_message}")
                            ex_success_msg = system_level_test_read_ini().get_enrollment_group_success_message_validation_text()
                            self.logger.info(f"expected message: {ex_success_msg}")
                            time.sleep(web_driver.one_second)

                            if ex_success_msg == success_message:
                                status.append(True)
                            else:
                                status.append(False)
                            time.sleep(web_driver.one_second)
                            close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                            for panels in close_panel:
                                panels.click()
                                time.sleep(web_driver.one_second)

                            self.logger.info(f"status: {status}")
                            if False in status:
                                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_8_failed.png")
                                self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_8_failed.png")
                                return False
                            else:
                                return True
        # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_8_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_8_exception.png")
            self.logger.error(f"TC_SLT_8 got exception as: {ex.args}")
            return False

    def Creating_Notification_Group_and_User_from_Enrollment_Group_panel(self):
        try:
            self.logger.info("********** Test_SLT_9 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            enrollment_groups_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Enrollment_Groups_menu_by_xpath())
            enrollment_groups_btn.click()
            time.sleep(web_driver.one_second)
            cases_list = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_unlinked_enrollment_groups_by_xpath())
            time.sleep(web_driver.one_second)
            alert_icons = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_notification_group_icon_btn_on_users_panel_by_xpath())
            x = system_level_test_read_ini().get_enrollment_group_name()
            enrollment_names_list = x.split(',')
            for i in range(len(cases_list)):
                if cases_list[i].text == enrollment_names_list[0]:
                    alert_icons[i].click()
                    status.append(True)
                    time.sleep(web_driver.one_second)
                    action_btn = self.d.find_element(By.XPATH, system_level_test_read_ini().get_action_dropdown_on_notification_groups_panel_by_xpath())
                    action_btn.click()
                    time.sleep(web_driver.one_second)
                    create_notification = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().create_notification_group_btn_by_xpath())
                    create_notification.click()
                    time.sleep(web_driver.one_second)
                    name_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().name_field_by_xpath())
                    time.sleep(web_driver.one_second)
                    x = system_level_test_read_ini().get_dummy_notification_group_name()
                    notification_group_names_list = x.split(',')
                    name_field.send_keys(notification_group_names_list[0])
                    time.sleep(web_driver.one_second)
                    description_field = self.d.find_element(By.XPATH, Read_Notification_Groups_Components()
                                                            .description_field_by_xpath())
                    description_field.send_keys(system_level_test_read_ini().get_notification_group_description())
                    time.sleep(web_driver.one_second)
                    save_button = self.d.find_element(By.XPATH, Read_Notification_Groups_Components().save_button_by_xpath())
                    save_button.click()
                    time.sleep(web_driver.two_second)
                    actual_message = self.d.find_element(By.XPATH, system_level_test_read_ini().get_success_message_on_alert_group_creation_by_xpath()).text
                    self.logger.info(f"actual message: {actual_message}")
                    expected_message = Read_Notification_Groups_Components().success_message_validation_text()
                    self.logger.info(f"expected message: {expected_message}")
                    if actual_message == expected_message:
                        status.append(True)
                    else:
                        status.append(False)
                    time.sleep(web_driver.one_second)

                    # -------------------------------------------------------
                    user_btn = self.d.find_element(By.XPATH, system_level_test_read_ini().get_users_btn_on_notification_group_details_panel_by_xpath())
                    user_btn.click()
                    status.append(True)
                    time.sleep(web_driver.one_second)
                    action_dropdown = self.d.find_element(By.XPATH, user_roles_read_ini().get_action_dropdown_user_panel_by_xpath())
                    action_dropdown.click()
                    time.sleep(web_driver.one_second)
                    options_inside_action_dropdown_list = self.d.find_elements(By.XPATH, user_roles_read_ini().get_options_inside_action_dropdown_by_xpath())
                    if len(options_inside_action_dropdown_list) > 0:
                        for option in options_inside_action_dropdown_list:
                            if option.text != "":
                                if option.text == "Create User":
                                    option.click()
                        time.sleep(web_driver.one_second)

                    # ------------------------------------------------

                    x = system_level_test_read_ini().get_user_name_integration()
                    username = x.split(',')
                    user_name_txt_bx = self.d.find_element(By.XPATH, system_level_test_read_ini().get_user_name_textbox_by_xpath())
                    user_name_txt_bx.send_keys(username[1])
                    time.sleep(web_driver.one_second)
                    first_name_txt_bx = self.d.find_element(By.XPATH, user_roles_read_ini().get_first_name_textbox_by_xpath())
                    first_name_txt_bx.send_keys(system_level_test_read_ini().get_first_name_input_data())
                    time.sleep(web_driver.one_second)
                    last_name_txt_bx = self.d.find_element(By.XPATH, user_roles_read_ini().get_lastname_textbox_by_xpath())
                    last_name_txt_bx.send_keys(system_level_test_read_ini().get_last_name_input_data())
                    time.sleep(web_driver.one_second)
                    user_role_dropdown = self.d.find_element(By.XPATH, user_roles_read_ini().get_user_role_dropdown_by_xpath())
                    user_role_dropdown.click()
                    time.sleep(web_driver.one_second)
                    role_options_inside_dropdown = self.d.find_elements(By.XPATH, user_roles_read_ini().get_role_option_in_user_role_dropdown_by_xpath())
                    time.sleep(web_driver.one_second)
                    count = 0
                    for role in role_options_inside_dropdown:
                        if role.text == system_level_test_read_ini().get_SO_user_role():
                            # self.logger.info(f"User role: '{system_level_test_read_ini().get_SO_user_role()}' is visible..")
                            count = count + 1
                            if role.is_enabled():
                                role.click()
                                status.append(True)
                            else:
                                self.logger.info("User role is not clickable...")
                                status.append(False)
                    if count == 1:
                        status.append(True)
                    else:
                        self.logger.info("Created user role is not visible...")
                    # ------------------------------------------------------
                    time.sleep(web_driver.one_second)
                    new_password = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_new_password_textbox_by_xpath())
                    time.sleep(web_driver.one_second)
                    confirm_password = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_confirm_password_textbox_by_xpath())
                    new_password.send_keys(system_level_test_read_ini().get_password_data_input())
                    time.sleep(web_driver.one_second)
                    confirm_password.send_keys(system_level_test_read_ini().get_password_data_input())
                    time.sleep(web_driver.one_second)
                    self.select_region(system_level_test_read_ini().get_region_data_input())
                    time.sleep(web_driver.one_second)
                    email_txt_bx = self.d.find_element(By.XPATH, system_level_test_read_ini().get_email_by_xpath())
                    email = f"{username[1]}@facefirst.com"
                    email_txt_bx.send_keys(email)
                    time.sleep(web_driver.one_second)
                    # email_txt_bx.send_keys(system_level_test_read_ini().get_email_input_data())

                    time_zone = self.d.find_element(By.XPATH, system_level_test_read_ini().get_time_zone_by_xpath())
                    select = Select(time_zone)
                    select.select_by_value(system_level_test_read_ini().get_time_zone_input_data())
                    time.sleep(web_driver.one_second)
                    save = self.d.find_element(By.XPATH, system_level_test_read_ini().get_user_panel_save_button_by_xpath())
                    save.click()
                    time.sleep(web_driver.one_second)
                    status.append(self.validate_successful_message())
                    time.sleep(web_driver.one_second)

                    close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                    for panels in close_panel:
                        panels.click()
                        time.sleep(web_driver.one_second)

                    self.logger.info(f"status: {status}")
                    if False in status:
                        self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_9_failed.png")
                        self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_9_failed.png")
                        return False
                    else:
                        return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_9_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_9_exception.png")
            self.logger.error(f"TC_SLT_9 got exception as: {ex.args}")
            return False

    def click_on_visitor_search(self):
        try:
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info("going to visitor search...")
            time.sleep(web_driver.one_second)
            visitor_search_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Visitor_Search_menu_by_xpath())
            self.d.execute_script("arguments[0].click();", visitor_search_btn)
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info("waiting for search panel to appear...")
        except Exception as ex:
            self.logger.info(f"exception: {ex.args}")

    def click_on_submit_search_button(self):
        """
        This function is used to click on the submit search button
        :return:
        """
        time.sleep(web_driver.one_second)
        web_driver.implicit_wait(self, web_driver.one_second, self.d)
        self.logger.info("waiting for message to appear...")
        submit_btn = self.d.find_element(By.XPATH, system_level_test_read_ini().get_submit_search_button_by_xpath())
        submit_btn.click()
        time.sleep(web_driver.one_second)
        self.logger.info("clicked on submit search button..")

    def verify_image_from_match_list(self):
        try:
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            self.logger.info("Verifying matches")
            x = None
            time.sleep(web_driver.one_second)
            ele2 = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_no_matches_found())
            # WebDriverWait(self.d, 10).until(EC.presence_of_element_located(ele2[0]))
            # WebDriverWait(self.d, 10).until(EC.presence_of_element_located(ele2))
            # web_driver.explicit_wait(self, 30, ele2, self.d)
            if len(ele2) > 0:
                self.logger.info(f"no match text displayed: {ele2[0].is_displayed()}")
                self.logger.info(f"ele2: {ele2[0].text}")
                x = ele2[0].is_displayed()
            else:
                self.logger.info("comparing images.")
                time.sleep(web_driver.two_second)
                web_driver.implicit_wait(self, 1, self.d)
                auto_refresh_on = self.d.find_element(By.XPATH, system_level_test_read_ini().get_auto_refresh_on_by_xpath())
                time.sleep(web_driver.one_second)
                # while auto_refresh_on.is_displayed():
                #     time.sleep(web_driver.one_second)
                #     # self.logger.info("waiting for till auto refresh off..")
                auto_refresh_off = self.d.find_element(By.XPATH, system_level_test_read_ini().get_auto_refresh_off_by_xpath())
                if auto_refresh_off.is_displayed():
                    time.sleep(web_driver.one_second)
                    ele = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_image_match_list_by_xpath())
                    WebDriverWait(self.d, 30).until(EC.presence_of_element_located(ele[0]))
                    self.logger.info(f"length of ele: {len(ele)}")
                    if len(ele) > 0:
                        self.logger.info(f"images displayed: {ele[0].is_displayed()}")
                        for e in ele:
                            if e.is_displayed() or not x:
                                self.logger.info(f"Images Displayed: {e.is_displayed()}")
                                return True
                            else:
                                self.logger.info("no matches found..")
                                return False
                    return True
                else:
                    return False
        except Exception as ex:
            print(ex)
            self.logger.info(f"images match exception: {ex}")
        else:
            return True

    def select_enrollment_menu(self):
        try:
            time.sleep(web_driver.one_second)
            cloud_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath())
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            enrollments_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Enrollments_menu_by_xpath())
            enrollments_menu.click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.info(f"exception: {ex}")

    def Verify_visitor_enrollment_successfully_done_from_Visitor_Search_Results_for_visitor_with_image_for_all_edges_present(self):
        try:
            self.logger.info("********** Test_SLT_10 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)

            edge_names = system_level_test_read_ini().edge_name_input_data()
            self.logger.info(f"edge_names: {edge_names}")
            edge_names_list = edge_names.split(',')

            for i in range(len(edge_names_list)):
                self.logger.info(f"edge name: {edge_names_list[i]}")
                self.click_on_visitor_search()
                time.sleep(web_driver.one_second)
                upload_photo = self.d.find_element(By.XPATH, system_level_test_read_ini().get_photo_upload_container_by_xpath())
                upload_photo.click()
                time.sleep(web_driver.one_second)
                print("file path =====>>>> ")
                # file_path = ""
                if edge_names_list[i] == Read_Visitor_Search_Components().zone_data_input():
                    file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_2.png"
                elif edge_names_list[i] == Read_Visitor_Search_Components().zone_data_input1():
                    file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_2.png"
                else:
                    file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_2.png"

                print(f"filepath : {file_path}")
                pyautogui.write(file_path)
                pyautogui.press('enter')
                time.sleep(web_driver.one_second)
                pyautogui.press('enter')
                time.sleep(web_driver.one_second)

                self.click_on_submit_search_button()
                time.sleep(web_driver.one_second)
                self.explicit_wait(10, "XPATH", "//div[@class='complete-job-progress-container']", self.d)
                time.sleep(web_driver.two_second)
                x = self.verify_image_from_match_list()
                time.sleep(web_driver.one_second)
                self.logger.info(f"Returned: {x}")
                status.append(x)
                time.sleep(web_driver.one_second)
                # match_found = self.open_identify_enrollment_panel()
                # if match_found:
                #     self.logger.info(f"matched found: {match_found}")
                #     status.append(match_found)
                # else:
                #
                #     # ***************************************Enrollment Process start here**********************
                #     self.logger.info(f"matched found: {match_found}")
                #     self.select_enrollment_basis(i + 1)
                #     time.sleep(web_driver.one_second)
                #     self.select_enrollment_group(i + 1)
                #     time.sleep(web_driver.one_second)
                #     self.enter_required_fields(i, i, i)
                #     time.sleep(web_driver.one_second)
                #     region_btn = self.d.find_element(By.XPATH, system_level_test_read_ini().region_btn_by_xpath())
                #     time.sleep(web_driver.one_second)
                #     region_btn.click()
                #     time.sleep(web_driver.one_second)
                #
                #     region_names = self.d.find_elements(By.XPATH, system_level_test_read_ini().edge_name_list())
                #     self.logger.info(f"edge name: {edge_names_list[i]}")
                #     for j in range(len(region_names)):
                #         if edge_names_list[i] == region_names[j].text:
                #             region_names[j].click()
                #             self.logger.info(f"region selected as: {region_names[j].text}")
                #             break
                #
                #     time.sleep(web_driver.one_second)
                #     save_btn = self.d.find_element(By.XPATH, system_level_test_read_ini().save_btn_by_xpath())
                #     save_btn.click()
                #     self.logger.info("Saved selected region..")
                #
                #     save_btn = self.d.find_element(By.XPATH, system_level_test_read_ini().add_details_save_btn_by_xpath())
                #     save_btn.click()
                #     time.sleep(web_driver.one_second)
                #     wait_icon = self.d.find_element(By.XPATH, system_level_test_read_ini().enrollment_success_loader())
                #     time.sleep(web_driver.one_second)
                #     while wait_icon.is_displayed():
                #         time.sleep(web_driver.two_second)
                #
                #     WebDriverWait(self.d, 30).until(EC.presence_of_element_located(
                #         (By.XPATH, system_level_test_read_ini().enrollment_success_msg_xpath())))
                #     time.sleep(web_driver.three_second)
                #     success_msg = self.d.find_element(By.XPATH, system_level_test_read_ini()
                #                                       .enrollment_success_msg_xpath())
                #     self.logger.info(f"actual message: {success_msg.text}")
                #     self.logger.info(
                #         f"expected message: {system_level_test_read_ini().enrollment_success_msg_validation()}")
                #     if success_msg.text.lower() == system_level_test_read_ini().enrollment_success_msg_validation().lower():
                #         status.append(True)
                #     else:
                #         status.append(False)
                #
                #     time.sleep(web_driver.one_second)
                #     review_enrollment_details = self.d.find_element(By.XPATH, system_level_test_read_ini().review_enrollment_details_btn_by_xpath())
                #     review_enrollment_details.click()
                #     time.sleep(web_driver.one_second)
                #     status.append(self.enrollment_validation(i))

                time.sleep(web_driver.one_second)
                close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                for panels in close_panel:
                    panels.click()
                    time.sleep(web_driver.one_second)

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_10_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_10_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_10_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_10_exception.png")
            self.logger.error(f"TC_SLT_10 got exception as: {ex.args}")
            return False

    def select_zone(self, edge_name):
        """
        This function is used to handle the zone drop-down and select the required options
        :param edge_name:
        :return:
        """
        self.logger.info("zone selection")
        zone_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().zone_by_xpath())
        zone_ele.click()
        time.sleep(web_driver.one_second)
        self.logger.info("zone btn clicked.")
        time.sleep(web_driver.two_second)
        web_driver.implicit_wait(self, web_driver.one_second, self.d)

        region_names = self.d.find_elements(By.XPATH, system_level_test_read_ini().edge_name_list())
        time.sleep(web_driver.one_second)
        self.logger.info(f"region names length: {len(region_names)}")
        try:
            for i in range(len(region_names)):
                self.logger.info(f"edge_name in for loop: {edge_name}")
                self.logger.info(f"edge name in region list: {region_names[i].text}")
                if edge_name == region_names[i].text:
                    region_names[i].click()
                    self.logger.info(f"region selected as: {region_names[i].text}")
                    break
            save = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().zone_save_button_xpath())
            self.d.execute_script("arguments[0].click();", save)

        except Exception as ex:
            str(ex)

    def open_identify_enrollment_panel(self):
        try:
            time.sleep(web_driver.two_second)
            identify_within_enrollments = self.d.find_elements(By.XPATH, system_level_test_read_ini().get_identify_within_enrollments_btn_by_xpath())
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            # WebDriverWait(self.d, 10).until(EC.presence_of_element_located(identify_within_enrollments))
            # self.explicit_wait(10, identify_within_enrollments, self.d)
            for i in range(len(identify_within_enrollments) - 1):
                if identify_within_enrollments[i + 1].is_displayed():
                    identify_within_enrollments[i + 1].click()
                    self.logger.info("Clicked on 'Identify within enrollments'...")
                    time.sleep(web_driver.three_second)
                    WebDriverWait(self.d, 60).until(EC.presence_of_element_located((By.XPATH, system_level_test_read_ini().identify_enroll_panel_by_xpath())))

                    wait_icon = self.d.find_element(By.XPATH, system_level_test_read_ini().identifying_photo_wait_by_xpath())
                    while wait_icon.is_displayed():
                        time.sleep(web_driver.two_second)
                    time.sleep(web_driver.one_second)
                    # identify_results_panel = self.explicit_wait(2, "XPATH", "//p[contains(text(),'Identify Results')]", self.d)
                    # if identify_results_panel.is_displayed():
                    #     return True
                    # else:
                    time.sleep(web_driver.one_second)
                    add_details = self.d.find_elements(By.XPATH, system_level_test_read_ini().add_details_panel_by_xpath())
                    time.sleep(web_driver.one_second)
                    if len(add_details) > 0:
                        return False
                    else:
                        print("it is else block...")
                        identify_results_close = system_level_test_read_ini().identify_results_panel_by_xpath() + Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath()
                        print(f"{identify_results_close}")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH, identify_results_close).click()
                        time.sleep(web_driver.one_second)
                        identify_enroll_close = system_level_test_read_ini().identify_enroll_panel_by_xpath() + Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath()
                        print(f"{identify_enroll_close}")
                        self.d.find_element(By.XPATH, identify_enroll_close).click()
                        time.sleep(web_driver.one_second)
                        return True
                else:
                    pass

        except Exception as ex:
            self.logger.info(f"{ex.args}")

    def select_enrollment_basis(self, index):
        try:
            time.sleep(web_driver.two_second)
            WebDriverWait(self.d, 30).until(EC.presence_of_element_located((By.XPATH, system_level_test_read_ini().enrollment_basis_by_xpath())))
            enrollment_basis = self.d.find_element(By.XPATH, system_level_test_read_ini().enrollment_basis_by_xpath())
            select = Select(enrollment_basis)
            select.select_by_index(index)
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.info(f"{ex.args}")

    def select_enrollment_group(self, group_index):
        try:
            time.sleep(web_driver.two_second)
            enrollment_group = self.d.find_element(By.XPATH, system_level_test_read_ini().enrollment_group_by_xpath())
            select = Select(enrollment_group)
            select.select_by_index(group_index)
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
        except Exception as ex:
            self.logger.info(f"{ex.args}")

    def enter_required_fields(self, a, lo, c):
        try:
            time.sleep(web_driver.two_second)
            action_input = self.d.find_element(By.XPATH, system_level_test_read_ini().action_inpt_bx_by_xpath())
            action = system_level_test_read_ini().action_input_data()
            action_list = action.split(',')
            action_input.send_keys(action_list[a])
            time.sleep(web_driver.one_second)
            location_store = self.d.find_element(By.XPATH, system_level_test_read_ini().location_store_inpt_bx_by_xpath())
            location = system_level_test_read_ini().location_store_data()
            location_list = location.split(',')
            location_store.send_keys(location_list[lo])
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, system_level_test_read_ini().case_subject_inpt_bx_by_xpath())
            case = system_level_test_read_ini().case_subject_data()
            case_list = case.split(',')
            case_subject.send_keys(case_list[c])
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, system_level_test_read_ini().date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            date_incident.send_keys(system_level_test_read_ini().date_incident_data())
            time.sleep(web_driver.one_second)
            date_incident.send_keys(system_level_test_read_ini().date_incident_time())
            time.sleep(web_driver.one_second)
            date_incident.send_keys(system_level_test_read_ini().date_incident_am_pm())
            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, system_level_test_read_ini().reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(system_level_test_read_ini().reported_loss_data())
            time.sleep(web_driver.one_second)
            return lo, c
        except Exception as ex:
            self.logger.info(f"{ex.args}")

    def enrollment_validation(self, i):
        try:
            time.sleep(web_driver.one_second)
            expected_enrolled_on_date = self.d.find_element(By.XPATH, system_level_test_read_ini().enrolled_on_date_on_enrollment_details_panel_by_xpath()).text
            WebDriverWait(self.d, 60).until(EC.presence_of_element_located((By.XPATH, system_level_test_read_ini().enrolled_on_date_on_enrollment_details_panel_by_xpath())))

            self.logger.info(f"expected enrolled on date: {expected_enrolled_on_date}")

            self.select_enrollment_menu()
            time.sleep(web_driver.one_second)
            actual_enrolled_on_date = self.d.find_elements(By.XPATH, system_level_test_read_ini().enrolled_on_date_on_enrollments_panel_by_xpath())
            location_store_case_subject_on_enrollments_panel = self.d.find_elements(By.XPATH, system_level_test_read_ini().location_store_and_case_subject_on_enrollments_panel_by_xpath())
            action_on_enrollments_panel = self.d.find_elements(By.XPATH, system_level_test_read_ini().action_value_on_enrollments_panel_by_xpath())
            count = 0
            time.sleep(web_driver.one_second)
            for k in range(len(actual_enrolled_on_date)):

                # self.logger.info(f"{actual_enrolled_on_date[i].text}, type:{type(actual_enrolled_on_date[i].text)}")
                # self.logger.info(f"{expected_enrolled_on_date}, type: {type(expected_enrolled_on_date)}")
                if actual_enrolled_on_date[k].text == expected_enrolled_on_date:
                    count = count + 1

                    location_store = system_level_test_read_ini().location_store_data()
                    location_store_list = location_store.split(',')

                    case_subject = system_level_test_read_ini().case_subject_data()
                    case_subject_list = case_subject.split(',')

                    location_store_case_subject = location_store_list[i] + " " + case_subject_list[i]
                    self.logger.info(f"location_store_case_subject: {location_store_case_subject}")
                    self.logger.info(f"{location_store_case_subject_on_enrollments_panel[k].text}")

                    action = system_level_test_read_ini().action_input_data()
                    action_list = action.split(',')
                    self.logger.info(f"action: {action_list[i]}")
                    self.logger.info(f"{action_on_enrollments_panel[k].text}")

                    if location_store_case_subject_on_enrollments_panel[k].text == location_store_case_subject:
                        count = count + 1

                    if action_on_enrollments_panel[k].text == action_list[i]:
                        count = count + 1

            self.logger.info(f"Count: {count}")
            if count == 3:
                self.logger.info(f"Enrollment done from 'Visitor Search with pic' verified.....")
                return True
            else:
                return False

        except Exception as ex:
            self.logger.info(f"{ex.args}")

    def Verify_visitor_enrollment_successfully_done_from_Visitor_Search_Results_for_visitor_with_meta_data_for_all_edges_present(self):
        try:
            self.logger.info("********** Test_SLT_11 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)

            edge_names = system_level_test_read_ini().edge_name_input_data()
            edge_names_list = edge_names.split(',')
            time.sleep(web_driver.one_second)
            for i in range(len(edge_names_list)):
                self.click_on_visitor_search()
                date = int(system_level_test_read_ini().meta_data_start_date())
                month = str(system_level_test_read_ini().meta_data_start_month())
                year = int(system_level_test_read_ini().meta_data_start_year())
                hour = str(system_level_test_read_ini().meta_data_start_hour())
                minute = system_level_test_read_ini().meta_data_start_minuet()
                period = str(system_level_test_read_ini().meta_data_start_am_pm_period())

                e_month = str(system_level_test_read_ini().meta_data_end_month())
                e_date = int(system_level_test_read_ini().meta_data_end_date())
                e_year = int(system_level_test_read_ini().meta_data_end_year())
                e_hour = str(system_level_test_read_ini().meta_data_end_hour())
                e_minute = system_level_test_read_ini().meta_data_end_minuet()
                e_period = str(system_level_test_read_ini().meta_data_end_am_pm_period())
                try:
                    Visitor_Search_Module_pom().handle_calender_pop_up("from", date, month, year, hour, minute, period)
                    time.sleep(web_driver.one_second)
                    Visitor_Search_Module_pom().handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
                    time.sleep(web_driver.three_second)
                except Exception as ex:
                    print(ex)

                self.logger.info(f"edge name: {edge_names_list[i]}")
                self.select_zone(edge_names_list[i])
                time.sleep(web_driver.one_second)
                # start_age = Read_Visitor_Search_Components().start_age_data_input()
                # end_age = Read_Visitor_Search_Components().end_age_data_input()

                # Visitor_Search_Module_pom().select_start_age(start_age)
                # Visitor_Search_Module_pom().select_end_age(end_age)
                # gender_data = Read_Visitor_Search_Components().gender_data_input()

                # Visitor_Search_Module_pom().select_gender(gender_data)
                # self.nats_checkbox()

                self.click_on_submit_search_button()
                x = self.verify_image_from_match_list()
                self.logger.info(f"Returned: {x}")
                status.append(x)
                self.open_identify_enrollment_panel()
                time.sleep(web_driver.one_second)
                # ***************************************Enrollment Process start here**********************

                self.select_enrollment_basis(i+1)
                time.sleep(web_driver.one_second)
                self.select_enrollment_group(i+1)
                time.sleep(web_driver.one_second)
                self.enter_required_fields(i, i, i)
                time.sleep(web_driver.one_second)
                region_btn = self.d.find_element(By.XPATH, system_level_test_read_ini().region_btn_by_xpath())
                time.sleep(web_driver.one_second)
                region_btn.click()
                time.sleep(web_driver.one_second)

                region_names = self.d.find_elements(By.XPATH, system_level_test_read_ini().edge_name_list())
                self.logger.info(f"edge name: {edge_names_list[i]}")
                self.logger.info(f"actual_region_count: {len(region_names)}")
                for a in range(len(region_names)):
                    self.logger.info(f"region name: {region_names[a].text}")
                for j in range(len(region_names)):
                    if edge_names_list[i] == region_names[j].text:
                        region_names[j].click()
                        self.logger.info(f"region selected as: {region_names[j].text}")
                        break

                # region_names = self.d.find_elements(By.XPATH, system_level_test_read_ini().edge_name_list())
                # self.logger.info(f"edge name: {edge_names_list[i]}")
                # for j in range(len(region_names)):
                #     if edge_names_list[i] == region_names[j].text:
                #         region_names[j].click()
                #         self.logger.info(f"region selected as: {region_names[j].text}")
                #         break

                time.sleep(web_driver.one_second)
                save_btn = self.d.find_element(By.XPATH, system_level_test_read_ini().save_btn_by_xpath())
                save_btn.click()
                time.sleep(web_driver.one_second)
                self.logger.info("Saved selected region..")

                save_btn = self.d.find_element(By.XPATH, system_level_test_read_ini().add_details_save_btn_by_xpath())
                save_btn.click()
                time.sleep(web_driver.one_second)
                wait_icon = self.d.find_element(By.XPATH, system_level_test_read_ini().enrollment_success_loader())
                while wait_icon.is_displayed():
                    time.sleep(web_driver.two_second)

                WebDriverWait(self.d, 30).until(EC.presence_of_element_located((By.XPATH, system_level_test_read_ini().enrollment_success_msg_xpath())))
                time.sleep(web_driver.three_second)
                success_msg = self.d.find_element(By.XPATH, system_level_test_read_ini().enrollment_success_msg_xpath())
                time.sleep(web_driver.one_second)
                self.logger.info(f"actual message: {success_msg.text}")
                self.logger.info(f"expected message: {system_level_test_read_ini().enrollment_success_msg_validation()}")
                if success_msg.text.lower() == system_level_test_read_ini().enrollment_success_msg_validation().lower():
                    status.append(True)
                else:
                    status.append(False)

                time.sleep(web_driver.one_second)
                review_enrollment_details = self.d.find_element(By.XPATH, system_level_test_read_ini().review_enrollment_details_btn_by_xpath())
                review_enrollment_details.click()
                time.sleep(web_driver.one_second)
                status.append(self.enrollment_validation(i))
                time.sleep(web_driver.one_second)
                close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                for panels in close_panel:
                    panels.click()
                    time.sleep(web_driver.one_second)

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_11_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_11_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_11_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_11_exception.png")
            self.logger.error(f"TC_SLT_11 got exception as: {ex.args}")
            return False

    def Verify_visitor_enrollment_successfully_done_from_Visitor_Search_Results_for_visitor_with_image_and_meta_data_for_all_edges_present(self):
        try:
            self.logger.info("********** Test_SLT_12 Begin  **********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)

            edge_names = system_level_test_read_ini().edge_name_input_data()
            edge_names_list = edge_names.split(',')

            for i in range(len(edge_names_list)):
                self.click_on_visitor_search()
                time.sleep(web_driver.one_second)
                upload_photo = self.d.find_element(By.XPATH, system_level_test_read_ini().get_photo_upload_container_by_xpath())
                upload_photo.click()
                time.sleep(web_driver.one_second)
                print("file path =====>>>> ")
                # file_path = ""
                if edge_names_list[i] == "RSHINDE-PC":
                    file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\VS_images\\Visitor-3.png"

                elif edge_names_list[i] == "SWANKHEDE-PC":
                    file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\VS_images\\SWANKHEDE-PC-Visitor-5.png"

                else:
                    file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\VS_images\\SOMU-PC-Visitor-4.png"

                print(f"filepath : {file_path}")
                pyautogui.write(file_path)
                pyautogui.press('enter')
                time.sleep(web_driver.one_second)
                pyautogui.press('enter')
                time.sleep(web_driver.one_second)
                date = int(system_level_test_read_ini().meta_data_start_date())
                month = str(system_level_test_read_ini().meta_data_start_month())
                year = int(system_level_test_read_ini().meta_data_start_year())
                hour = str(system_level_test_read_ini().meta_data_start_hour())
                minute = system_level_test_read_ini().meta_data_start_minuet()
                period = str(system_level_test_read_ini().meta_data_start_am_pm_period())

                e_month = str(system_level_test_read_ini().meta_data_end_month())
                e_date = int(system_level_test_read_ini().meta_data_end_date())
                e_year = int(system_level_test_read_ini().meta_data_end_year())
                e_hour = str(system_level_test_read_ini().meta_data_end_hour())
                e_minute = system_level_test_read_ini().meta_data_end_minuet()
                e_period = str(system_level_test_read_ini().meta_data_end_am_pm_period())
                try:
                    Visitor_Search_Module_pom().handle_calender_pop_up("from", date, month, year, hour, minute, period)
                    # time.sleep(web_driver.three_second)
                    # Visitor_Search_Module_pom().handle_calender_pop_up("to", e_date, e_month, e_year, e_hour,
                    # e_minute, e_period)
                except Exception as ex:
                    print(ex)

                self.logger.info(f"edge name: {edge_names_list[i]}")
                self.select_zone(edge_names_list[i])

                start_age = Read_Visitor_Search_Components().start_age_data_input()
                end_age = Read_Visitor_Search_Components().end_age_data_input()

                Visitor_Search_Module_pom().select_start_age(start_age)
                Visitor_Search_Module_pom().select_end_age(end_age)
                gender_data = Read_Visitor_Search_Components().gender_data_input()

                Visitor_Search_Module_pom().select_gender(gender_data)
                # self.nats_checkbox()

                self.click_on_submit_search_button()
                x = self.verify_image_from_match_list()
                self.logger.info(f"Returned: {x}")
                status.append(x)
                self.open_identify_enrollment_panel()

                # ***************************************Enrollment Process start here**********************

                self.select_enrollment_basis(i + 1)
                self.select_enrollment_group(i + 1)
                self.enter_required_fields(i, i, i)
                time.sleep(web_driver.one_second)
                region_btn = self.d.find_element(By.XPATH, system_level_test_read_ini().region_btn_by_xpath())
                time.sleep(web_driver.one_second)
                region_btn.click()
                time.sleep(web_driver.one_second)

                region_names = self.d.find_elements(By.XPATH, system_level_test_read_ini().edge_name_list())
                self.logger.info(f"edge name: {edge_names_list[i]}")
                for j in range(len(region_names)):
                    if edge_names_list[i] in region_names[j].text:
                        region_names[j].click()
                        self.logger.info(f"region selected as: {region_names[j].text}")
                        break

                time.sleep(web_driver.one_second)
                save_btn = self.d.find_element(By.XPATH, system_level_test_read_ini().save_btn_by_xpath())
                save_btn.click()
                self.logger.info("Saved selected region..")

                save_btn = self.d.find_element(By.XPATH, system_level_test_read_ini().add_details_save_btn_by_xpath())
                save_btn.click()

                wait_icon = self.d.find_element(By.XPATH, system_level_test_read_ini().enrollment_success_loader())
                while wait_icon.is_displayed():
                    time.sleep(web_driver.two_second)

                WebDriverWait(self.d, 30).until(EC.presence_of_element_located(
                    (By.XPATH, system_level_test_read_ini().enrollment_success_msg_xpath())))
                time.sleep(web_driver.three_second)
                success_msg = self.d.find_element(By.XPATH, system_level_test_read_ini()
                                                  .enrollment_success_msg_xpath())
                self.logger.info(f"actual message: {success_msg.text}")
                self.logger.info(
                    f"expected message: {system_level_test_read_ini().enrollment_success_msg_validation()}")
                if success_msg.text.lower() == system_level_test_read_ini().enrollment_success_msg_validation(). \
                        lower():
                    status.append(True)
                else:
                    status.append(False)

                time.sleep(web_driver.one_second)
                review_enrollment_details = self.d.find_element(By.XPATH,
                                                                system_level_test_read_ini().review_enrollment_details_btn_by_xpath())
                review_enrollment_details.click()
                status.append(self.enrollment_validation(i))
                time.sleep(web_driver.one_second)
                close_panel = self.d.find_elements(By.XPATH,
                                                   Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
                for panels in close_panel:
                    panels.click()
                    time.sleep(web_driver.one_second)

            self.logger.info(f"status: {status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_12_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_12_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_12_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_12_exception.png")
            self.logger.error(f"TC_SLT_12 got exception as: {ex.args}")
            return False

