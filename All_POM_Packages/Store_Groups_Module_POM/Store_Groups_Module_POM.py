import time

from All_Config_Packages._10_Events_Config_Files.Events_Read_Ini import events_Read_Ini
from All_Config_Packages._1_Portal_Login_Module_Config_Files.Portal_Login_Page_Read_INI import \
    Portal_login_page_read_ini
from All_Config_Packages._4_Users_Module_Config_Files.Users_Read_INI import Read_Users_Components
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import \
    Portal_Menu_Module_read_ini
from All_Config_Packages._7_Visitor_Search_Module_Config_Files.Visitor_Search_Read_INI import \
    Read_Visitor_Search_Components
from All_POM_Packages._4_Users_Module_POM.Users_Module_POM import Users_Module_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from selenium.webdriver.common.by import By
from Base_Package.Login_Logout_Ops import login
from Base_Package.Login_Logout_Ops import logout
from All_Config_Packages.Store_Groups_Config_Files.Store_Groups_Read_INI import store_group_page_read_ini


class Store_Groups_Module_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    def close_all_panels(self):
        try:
            cloud_menu = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath(),
                                            self.d)
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            close_all_panels = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                                                  get_close_all_panels_menu_by_xpath(), self.d)
            close_all_panels.click()
        except Exception as ex:
            self.logger.info(f"close all panels got an exception as: {ex}")

    def click_on_logout_button(self):
        try:
            time.sleep(web_driver.one_second)
            # logout_button = self.d.find_element(By.XPATH, Read_Users_Components().logout_btn_by_xpath())
            logout_button = web_driver.explicit_wait(self, 5, "XPATH",
                                                     Read_Users_Components().logout_btn_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            logout_button.click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}click_on_logout_button_failed_from_users_module.png")
            self.logger.info(f"click_on_logout_button_failed: {ex}")
            return False

    def accept_terms_and_conditions_for_login_for_new_user(self):
        try:
            self.logger.info("entered into AUP function")
            time.sleep(web_driver.one_second)
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

    def select_region_from_org_hierarchy(self):
        try:
            # self.explicit_wait(5, "XPATH", events_Read_Ini().regions_xpath(), self.d)
            time.sleep(web_driver.two_second)
            region_list = self.d.find_elements(By.XPATH, events_Read_Ini().regions_xpath())
            region_checkbox_list = self.d.find_elements(By.XPATH, events_Read_Ini().region_checkbox_xpath())

            self.logger.info(f"region length: {len(region_list)}")
            if len(region_list) > 0:
                for i in range(len(region_list)):
                    if region_list[i].text == events_Read_Ini().edge_name():
                        region_checkbox_list[i].click()
            else:
                self.logger.info(f"region name list not displayed.")
            save_btn = self.explicit_wait(5, "XPATH", events_Read_Ini().save_zone_button_by_xpath(), self.d)
            if save_btn.is_displayed():
                self.logger.info(f"save btn is visible: {save_btn.is_displayed()}")
                save_btn.click()
            else:
                self.logger.info("save btn not displayed.")
        except Exception as ex:
            self.logger.info(f"select_region_from_org_hierarchy ex: {ex.args}")

    def select_region(self, region_text):
        """
        This function is used to handle the region drop-down and select the required options
        :param region_text:
        :return:
        """
        # region_ele = self.d.find_element(By.XPATH, Read_Users_Components().region_by_xpath())
        region_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Users_Components().region_by_xpath(), self.d)
        region_ele.click()
        time.sleep(web_driver.two_second)
        region_text_list = self.d.find_elements(By.XPATH, Read_Users_Components().region_list_by_xpath())
        expected_region_text = region_text
        try:
            for i in range(len(region_text_list) + 1):
                actual_zone_text = region_text_list.__getitem__(i).text
                self.logger.info(actual_zone_text)
                self.logger.info(expected_region_text)
                if expected_region_text.upper() in actual_zone_text.upper():
                    region_text_list.__getitem__(i).click()
                    break
            save = self.d.find_element(By.XPATH, Read_Users_Components().region_save_btn_by_xpath())
            # save.click()
            self.d.execute_script("arguments[0].click();", save)
            self.logger.info(f"select region: {region_text}")
            time.sleep(web_driver.one_second)
        except Exception as ex:
            str(ex)

    def create_store_groups(self):
        try:
            self.logger.info("********** Test_EG_01 Begin  **********")
            status = []
            users_dict = Users_Module_pom().Read_user_from_json()
            users_list = []
            username = users_dict["users"][4]["username"]
            login().login_with_persona_user(self.d, username)
            time.sleep(web_driver.one_second)
            login().accept_terms_and_conditions_for_login_for_new_user()
            store_group_menu = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                  get_store_groups_menu_by_xpath(), self.d)
            if store_group_menu:
                store_group_menu.click()
            time.sleep(web_driver.one_second)

            self.explicit_wait(10, "XPATH", store_group_page_read_ini().get_title_on_store_groups_panel_by_xpath(),
                               self.d)
            description = store_group_page_read_ini().get_store_group_description()
            edge_name = Read_Visitor_Search_Components().zone_data_input()
            x = store_group_page_read_ini().get_store_group_name()
            store_group = x.split(',')

            for i in range(len(store_group)):
                action_button = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                   get_action_dropdown_on_store_groups_panel_by_xpath(), self.d)
                if action_button:
                    action_button.click()
                    time.sleep(web_driver.one_second)
                    create_store_group_option = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                                   get_create_store_group_option_by_xpath(), self.d)
                    create_store_group_option.click()
                    time.sleep(web_driver.one_second)
                    name_field = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                    get_name_field_for_creating_store_group_by_xpath(), self.d)
                    name_field.send_keys(store_group[i])
                    self.logger.info(f"store name entered as {store_group[i]}")
                    time.sleep(web_driver.one_second)
                    description_field = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                           get_description_field_by_xpath(), self.d)
                    description_field.send_keys(description)
                    time.sleep(web_driver.one_second)
                    org_selection_button = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                              get_org_selection_button_by_xpath(), self.d)
                    org_selection_button.click()
                    self.select_region_from_org_hierarchy()
                    time.sleep(web_driver.one_second)
                    save_button = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                     get_save_button_on_store_group_creation_panel_by_xpath(), self.d)
                    save_button.click()
                    time.sleep(web_driver.one_second)
                    success_message = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                         get_store_group_creation_success_message_by_xpath(), self.d)
                    if success_message.text == store_group_page_read_ini().\
                            get_success_message_after_store_group_creation():
                        self.status.append(True)
                        self.logger.info(f"store group {store_group[i]} created successfully!")
                    else:
                        self.status.append(False)
            self.logger.info(f"status: {self.status}")
            if False in status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_0_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_0_failed.png")
                return False
            else:
                return True
            # logout().logout_from_core()

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_SLT_0_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_SLT_0_exception.png")
            self.logger.error(f"TC_SLT_0 got exception as: {ex.args}")
            return False

        finally:
            logout().logout_from_core(self.d)

    def Verify_Store_Groups_appears_in_portal_web_menu_only_if_logged_in_user_holds_Store_Group_and_Configuration_Permisisons_in_userroles(self):
        try:
            self.logger.info("********** TC_Store_Groups_01 started ********")
            self.logger.info("Verify_Store_Groups_appears_in_portal_web_menu_only_if_logged_in_user_holds_Store_Group_and_Configuration_Permisisons_in_userroles")
            print(f"Verify_Store_Groups_appears_in_portal_web_menu_only_if_logged_in_user_holds_Store_Group_and_Configuration_Permisisons_in_userroles")
            login().login_to_cloud_if_not_done(self.d)

            usernames = ["TC_SG_EX1", "TC_SG_AD1"]
            roles = ["1. executive", "5. it system admin"]
            emails = ["sgex1@facefirst.com", "sgad1@facefirst.com"]
            password = "Right_1r1s"
            a = Portal_Menu_Module_read_ini().get_executive_menus()
            executive_permissions = a.split(',')
            b = Portal_Menu_Module_read_ini().get_it_admin_menus()
            it_admin_permissions = b.split(',')

            time.sleep(web_driver.one_second)
            for i in range(len(usernames)):
                Users_Module_pom().click_user_on_cloud_menu()
                Users_Module_pom().click_on_action_create_user_option()
                time.sleep(web_driver.one_second)
                # username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
                Users_Module_pom().enter_user_name(usernames[i])
                Users_Module_pom().enter_first_name("user")
                Users_Module_pom().enter_last_name("test")
                Users_Module_pom().d.find_element(By.XPATH, "//select[@name='userRoleId']").click()
                Users_Module_pom().select_user_role(roles[i])
                Users_Module_pom().enter_password(password)
                self.select_region_from_org_hierarchy()
                region = Read_Users_Components().region_data_input()
                self.select_region(region)
                # Users_Module_pom().select_region(users_dict["users"][i]["user_orgahierarchy"])
                # self.select_store_group(users_dict["users"][i]["store_group"])
                Users_Module_pom().enter_email(emails[i])
                Users_Module_pom().enter_alert_email(emails[i])
                Users_Module_pom().select_time_zone(Read_Users_Components().time_zone_input_data())
                time.sleep(web_driver.one_second)
                Users_Module_pom().click_on_save_btn()
                time.sleep(web_driver.two_second)
                if Users_Module_pom().check_if_user_is_created(usernames[i]):
                    time.sleep(web_driver.one_second)
                    self.logger.info(f"{usernames[i]} user created successfully")
                    # self.close_all_panel_one_by_one()
                    self.status.append(True)
                else:
                    self.d.save_screenshot(f"{self.screenshots_path}test_TC_US_1_failed.png")
                    self.status.append(False)
                self.logger.info(f"user list contains {usernames[i]}")
                self.close_all_panels()

            time.sleep(web_driver.one_second)
            self.click_on_logout_button()
            login().login_with_persona_user(self.d, usernames[0])
            self.accept_terms_and_conditions_for_login_for_new_user()
            for e in range(len(executive_permissions)):
                if executive_permissions[e] == "Store Groups":
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            self.click_on_logout_button()
            login().login_with_persona_user(self.d, usernames[1])
            self.accept_terms_and_conditions_for_login_for_new_user()
            for a in range(len(it_admin_permissions)):
                if it_admin_permissions[a] == "Store Groups":
                    self.status.append(True)
            time.sleep(web_driver.one_second)
            self.click_on_logout_button()
            time.sleep(web_driver.one_second)
            login().login_to_cloud_if_not_done(self.d)
            Users_Module_pom().click_user_on_cloud_menu()
            time.sleep(web_driver.one_second)
            users_created = web_driver.explicit_wait(self, 5, "XPATH", Read_Users_Components().facefirst_user_xpath(),
                                                     self.d)
            search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
            search_box.send_keys(usernames[0])
            time.sleep(web_driver.one_second)
            user_checkbox = self.d.find_element(By.XPATH, Read_Users_Components().user_checkbox_by_xpath())
            user_checkbox.click()
            time.sleep(web_driver.one_second)
            action_btn = self.d.find_element(By.XPATH, Read_Users_Components().action_dropdown_by_xpath())
            action_btn.click()
            time.sleep(web_driver.one_second)
            delete_user = self.d.find_element(By.XPATH, Read_Users_Components().delete_selected_user_by_xpath())
            delete_user.click()
            time.sleep(web_driver.one_second)
            yes_delete_selected = self.d.find_element(By.XPATH, Read_Users_Components().yes_delete_selected_button())
            yes_delete_selected.click()
            time.sleep(web_driver.two_second)
            search_box.send_keys(usernames[1])
            time.sleep(web_driver.one_second)
            user_checkbox = self.d.find_element(By.XPATH, Read_Users_Components().user_checkbox_by_xpath())
            user_checkbox.click()
            time.sleep(web_driver.one_second)
            action_btn = self.d.find_element(By.XPATH, Read_Users_Components().action_dropdown_by_xpath())
            action_btn.click()
            time.sleep(web_driver.one_second)
            delete_user = self.d.find_element(By.XPATH, Read_Users_Components().delete_selected_user_by_xpath())
            delete_user.click()
            time.sleep(web_driver.one_second)
            yes_delete_selected = self.d.find_element(By.XPATH, Read_Users_Components().yes_delete_selected_button())
            yes_delete_selected.click()
            time.sleep(web_driver.two_second)
            self.click_on_logout_button()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Store_Groups_01.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Store_Groups_01.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Store_Groups_01_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Store_Groups_01_exception.png")
            self.logger.error(f"TC_Store_Groups_01 got exception as: {ex}")

    def Verify_admin_user_able_to_create_store_group_successfully_by_entering_required_fields_such_as_Name_and_Location_Verify_user_able_to_see_success_message_as_Success_A_store_group_has_been_created(self):
        try:
            self.logger.info("********** TC_Store_Groups_15 started ********")
            self.logger.info(
                "Verify_admin_user_able_to_create_store_group_successfully_by_entering_required_fields_such_as_Name_and_Location_Verify_user_able_to_see_success_message_as_Success_A_store_group_has_been_created")
            print(
                f"Verify_admin_user_able_to_create_store_group_successfully_by_entering_required_fields_such_as_Name_and_Location_Verify_user_able_to_see_success_message_as_Success_A_store_group_has_been_created")
            login().login_to_cloud_if_not_done(self.d)
            Users_Module_pom().click_user_on_cloud_menu()
            Users_Module_pom().click_on_action_create_user_option()
            time.sleep(web_driver.one_second)
            username = "TC_SG_AD2"
            # username = Read_Users_Components().user_name_input_data() + str(generate_random_number())
            Users_Module_pom().enter_user_name(username)
            Users_Module_pom().enter_first_name("user")
            Users_Module_pom().enter_last_name("test")
            Users_Module_pom().d.find_element(By.XPATH, "//select[@name='userRoleId']").click()
            Users_Module_pom().select_user_role("5. it system admin")
            Users_Module_pom().enter_password("Right_1r1s")
            self.select_region_from_org_hierarchy()
            region = store_group_page_read_ini().get_root_region_input()
            self.select_region(region)
            # Users_Module_pom().select_region(users_dict["users"][i]["user_orgahierarchy"])
            # self.select_store_group(users_dict["users"][i]["store_group"])
            Users_Module_pom().enter_email("sgad2@facefirst.com")
            Users_Module_pom().enter_alert_email("sgad2@facefirst.com")
            Users_Module_pom().select_time_zone(Read_Users_Components().time_zone_input_data())
            time.sleep(web_driver.one_second)
            Users_Module_pom().click_on_save_btn()
            time.sleep(web_driver.two_second)
            if Users_Module_pom().check_if_user_is_created(username):
                time.sleep(web_driver.one_second)
                self.logger.info(f"{username} user created successfully")
                # self.close_all_panel_one_by_one()
                self.status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}test_TC_SG_15_failed.png")
                self.status.append(False)
            self.logger.info(f"user list contains {username}")
            time.sleep(web_driver.one_second)
            self.click_on_logout_button()
            login().login_with_persona_user(self.d, username)
            self.accept_terms_and_conditions_for_login_for_new_user()
            store_group_menu = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                  get_store_groups_menu_by_xpath(), self.d)
            if store_group_menu:
                store_group_menu.click()
            time.sleep(web_driver.one_second)

            self.explicit_wait(10, "XPATH", store_group_page_read_ini().get_title_on_store_groups_panel_by_xpath(),
                               self.d)
            # description = store_group_page_read_ini().get_store_group_description()
            # edge_name = Read_Visitor_Search_Components().zone_data_input()
            x = store_group_page_read_ini().get_store_group_name()
            store_group = x.split(',')

            for i in range(len(store_group)):
                action_button = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                   get_action_dropdown_on_store_groups_panel_by_xpath(), self.d)
                if action_button:
                    action_button.click()
                    time.sleep(web_driver.one_second)
                    create_store_group_option = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                                   get_create_store_group_option_by_xpath(), self.d)
                    create_store_group_option.click()
                    time.sleep(web_driver.one_second)
                    name_field = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                    get_name_field_for_creating_store_group_by_xpath(), self.d)
                    name_field.send_keys(store_group[i])
                    self.logger.info(f"store name entered as {store_group[i]}")
                    time.sleep(web_driver.one_second)
                    # description_field = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                    #                                        get_description_field_by_xpath(), self.d)
                    # description_field.send_keys(description)
                    # time.sleep(web_driver.one_second)
                    org_selection_button = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                              get_org_selection_button_by_xpath(), self.d)
                    org_selection_button.click()
                    self.select_region_from_org_hierarchy()
                    time.sleep(web_driver.one_second)
                    save_button = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                     get_save_button_on_store_group_creation_panel_by_xpath(), self.d)
                    save_button.click()
                    time.sleep(web_driver.one_second)
                    success_message = self.explicit_wait(10, "XPATH", store_group_page_read_ini().
                                                         get_store_group_creation_success_message_by_xpath(), self.d)
                    if success_message.text == store_group_page_read_ini(). \
                            get_success_message_after_store_group_creation():
                        self.status.append(True)
                        self.logger.info(f"store group {store_group[i]} created successfully!")
                    else:
                        self.status.append(False)
            time.sleep(web_driver.one_second)
            self.click_on_logout_button()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Store_Groups_15.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Store_Groups_15.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Store_Groups_15_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Store_Groups_15_exception.png")
            self.logger.error(f"TC_Store_Groups_15 got exception as: {ex}")
