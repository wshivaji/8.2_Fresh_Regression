import time
from pathlib import Path
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

from All_Config_Packages._6_Notes_Module_Config_Files.Notes_Read_Ini import notes_Read_Ini
from Base_Package.Web_Logger import web_logger
from Base_Package.Web_Driver import web_driver
from Base_Package.Login_Logout_Ops import login, logout


class notes_pom(web_driver, web_logger):
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

    def Launching_login_page(self):
        try:
            self.logger.info(f"*****TC_001***** started")
            self.d.get(notes_Read_Ini().get_Launching_url())
            expected_url = notes_Read_Ini().get_Launching_url()
            time.sleep(web_driver.one_second)
            self.d.maximize_window()
            actual_url = self.d.current_url
            print(f"actual: {actual_url},\nexpected: {expected_url}")
            if expected_url == actual_url:
                self.status.append(True)
            else:
                self.status.append(False)

            actual_title = self.d.title
            print("actual is", actual_title)
            expected_title = notes_Read_Ini().get_expecting_title_webportal_login()
            print("expected title is", expected_title)
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            print(self.status)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_notes_001.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_001.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_notes_001.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\Tc_notes_001.png")
            self.logger.error(f"Tc_notes_001 got exception as: {ex}")
            print(ex)

    def logo_username_texbox_password_textbox_is_visible(self):
        try:
            self.logger.info("*****TC_002***** started")
            self.d.get(notes_Read_Ini().get_Launching_url())
            self.status.clear()
            time.sleep(web_driver.three_second)
            logo = self.d.find_element(By.XPATH, notes_Read_Ini().get_logo_is_visible_on_login_page())
            self.logger.info("logo is visible")
            username = self.d.find_element(By.XPATH, notes_Read_Ini().get_username_textbox())
            username.is_displayed()
            self.logger.info("username textbox is visible")
            password = self.d.find_element(By.XPATH, notes_Read_Ini().get_password_textbox())
            password.is_displayed()
            self.logger.info("password textbox is visible")
            if logo.is_displayed():
                self.logger.info("logo is visible ")
                self.status.append(True)
            else:
                self.logger.info("logo is not visible")
                self.status.append(False)
            print(self.status)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_notes_002.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_002.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_002.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\Tc_notes_002.png")
            self.logger.error(f"TC_notes_002 got exception as: {ex} ")
            print(ex)

    def load_login_page_if_not_loaded(self):
        try:
            self.d.get(notes_Read_Ini().get_Launching_url())
            expected_url = notes_Read_Ini().get_Launching_url()
            time.sleep(web_driver.one_second)
            self.d.maximize_window()
            actual_url = self.d.current_url
            print(f"actual: {actual_url},\nexpected: {expected_url}")
            if expected_url == actual_url:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            username = self.d.find_element(By.XPATH, notes_Read_Ini().get_username_textbox())
            username.clear()
            username.send_keys(notes_Read_Ini().get_valid_username())
            time.sleep(web_driver.one_second)
            password = self.d.find_element(By.XPATH, notes_Read_Ini().get_password_textbox())
            password.clear()
            password.send_keys(notes_Read_Ini().get_valid_password())
            time.sleep(web_driver.one_second)
            cloud_login = self.d.find_element(By.XPATH, notes_Read_Ini().get_cloudlogin_button())
            cloud_login.click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            print(ex)

    def verify_and_click_on_cloud_menu_after_login(self):
        try:
            self.logger.info("*****TC_003_*****started")
            self.load_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.two_second)
            cloud_menu_after_login = self.d.find_element(By.XPATH,
                                                         notes_Read_Ini().get_afterlogin_cloud_menu_is_visible())
            if cloud_menu_after_login.is_displayed():
                self.logger.info("cloudlogin is visible in dashboard")
                self.status.append(True)
            else:
                self.logger.info("cloudlogin is not visible in dashboard")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\tc_notes_003.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_003.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\tc_notes_003.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_003.png")
            self.logger.error(f"TC_notes_003 got exception as: {ex} ")
            print(ex)

    def verify_cloudmenubutton_is_displayed_after_successfull_login(self):
        try:
            self.logger.info("*****TC_004***** started")
            self.load_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.two_second)
            cloud_login_menu_after_login = self.d.find_element(By.XPATH,
                                                               notes_Read_Ini().get_afterlogin_cloud_menu_is_visible())
            if cloud_login_menu_after_login.is_displayed():
                self.logger.info("cloudmenu is visible after login")
                self.status.append(True)
            else:
                self.logger.info("cloudlogin is not visible")
                self.status.append(False)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_004.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_004.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_004.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_004.png")
            self.logger.error(f"TC_notes_004 got exception as: {ex} ")
            print(ex)

    def verify_notes_is_visible_on_cloud_menu(self):
        try:
            self.logger.info("******TC_005***** started")
            self.load_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            if notes.is_displayed():
                print("if notes is displayed")
                self.logger.info("notes is visible in dashboard items")
                self.status.append(True)
            else:
                self.logger.info("notes is not visible in dashboard items")
                print("if notes is not displayed")
                self.status.append(False)
            print(self.status)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_005.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_005.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_005.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_005.png")
            self.logger.error(f"TC_notes_005 got exception as: {ex} ")
            print(ex)

    def click_on_NOTES_and_check_heading_of_the_notes_page(self):
        try:
            self.logger.info("*****TC_001***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            time.sleep(web_driver.one_second)
            heading_notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_page()).text
            self.logger.info("after login clicking on notes heading of notes panel ")
            print(f"heading is visible:{heading_notes}")
            if heading_notes == "Notes":
                self.logger.info(f"notes panel heading: {heading_notes}")
                self.status.append(True)
            else:
                self.logger.info(f"notes panel heading is not visible")
                self.status.append(False)
            print(self.status)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_001.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_001.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_001.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_001.png")
            self.logger.error(f"TC_notes_001 got exception as: {ex} ")

    def on_notes_panel_verify_searchdropdown_is_visible(self):
        try:
            self.logger.info("*****TC_002***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            if search_dropdown.is_displayed():
                self.logger.info("search dropdown is visible on notes page")
                self.status.append(True)
            else:
                self.logger.info("search dropdown is not visible on notes page")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_002.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_002.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_002.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_002.png")
            self.logger.error(f"TC_notes_002 got exception as: {ex} ")

    def On_notes_panel_click_on_Search_dropdown_the_List_of_elements_are_displayed(self):
        try:
            self.logger.info("*****TC_003***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_description_in_search_dropdown())
            print("description is visible")
            if description_in_searchdropdown.is_displayed():
                self.logger.info("description is visible in search dropdown")
                self.status.append(True)
            else:
                self.logger.info("description is not visible in search dropdown")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            print("logout successfully")
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_003.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_003.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_003.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_003.png")
            self.logger.error(f"TC_notes_003 got exception as: {ex} ")

    def click_on_search_dropdown_on_notes_panel_verify_Location_store_textbox_is_visible(self):
        try:
            self.logger.info("*****TC_004***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.explicit_wait(10, "XPATH", notes_Read_Ini().get_notes_is_displayed(), self.d)
            notes.click()
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_heading_of_notes_page(), self.d)
            heading_notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            self.logger.info("search dropdown is visible")
            search_dropdown.click()
            time.sleep(web_driver.two_second)
            description_in_searchdropdown = self.explicit_wait(10, "XPATH", notes_Read_Ini()
                                                               .get_description_in_search_dropdown(), self.d)
            print("description is visible")
            description_in_searchdropdown.click()
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_Location_store_in_Description(), self.d)
            location_store = self.explicit_wait(10, "XPATH", notes_Read_Ini()
                                                .get_Location_store_in_Description(), self.d)
            if location_store.is_displayed():
                self.logger.info("location store text is visible")
                self.status.append(True)
            else:
                self.logger.info("location store textbox is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_008.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_008.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_009.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_009.png")
            self.logger.error(f"TC_notes_009 got exception as: {ex} ")

    def on_notes_panel_Inside_search_dropdown_Enter_a_text_on_Location_store_click_in_search_notes_is_displayed_as_expected(self):
        try:
            self.logger.info("*****TC_05****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            time.sleep(web_driver.three_second)
            self.create_notes()
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_description_in_search_dropdown())
            description_in_searchdropdown.click()
            time.sleep(web_driver.one_second)
            location_store = self.d.find_element(By.XPATH, notes_Read_Ini().get_Location_store_in_Description())
            location_store.clear()
            location_store.send_keys(notes_Read_Ini().enter_a_text_in_location_store())
            self.logger.info("text is entered on location store textbox")
            time.sleep(web_driver.one_second)
            search_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_button_on_Description())
            search_button.click()
            time.sleep(web_driver.one_second)
            search_criteria = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_criteria())
            if search_criteria.is_displayed():
                self.logger.info("search criteria is displayed after clicking on search button")
                self.status.append(True)
            else:
                self.logger.info("search criteria is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_05.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_05.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_05.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_05.png")
            self.logger.error(f"TC_notes_05 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_inside_search_dropdown_Enter_a_text_on_Location_store_click_on_clear_text_is_cleared_on_textbox(self):
        try:
            self.logger.info("*****TC_06***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            time.sleep(web_driver.one_second)
            heading_notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.two_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH,
                                                                notes_Read_Ini().get_description_in_search_dropdown())
            print("description is visible")
            description_in_searchdropdown.click()
            location_store = self.d.find_element(By.XPATH, notes_Read_Ini().get_Location_store_in_Description())
            location_store.clear()
            location_store.send_keys(notes_Read_Ini().enter_a_text_in_location_store())
            time.sleep(web_driver.two_second)
            clear_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_clear_button_on_Description())
            clear_button.click()
            text = location_store.text
            print("text is empty")
            text = location_store.text
            print("text is", text)
            if text == "":
                self.logger.info("text is cleared on location store textbox")
                self.status.append(True)
            else:
                self.logger.info("text is not cleared on location store text box")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_06.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_06.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_06.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_06.png")
            self.logger.error(f"TC_notes_06 got exception as: {ex} ")

    def on_notes_panel_inside_search_dropdown_verify_case_Subject_textbox_is_visible(self):
        try:
            self.logger.info("*****TC_007***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.explicit_wait(10, "XPATH", notes_Read_Ini().get_notes_is_displayed(), self.d)
            notes.click()
            time.sleep(web_driver.one_second)
            heading_notes = self.explicit_wait(10, "XPATH", notes_Read_Ini().get_heading_of_notes_page(), self.d)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.two_second)
            description_in_searchdropdown = self.explicit_wait(10, "XPATH", notes_Read_Ini()
                                                               .get_description_in_search_dropdown(), self.d)
            print("description is visible")
            description_in_searchdropdown.click()
            case_subject = self.explicit_wait(10, "XPATH", notes_Read_Ini().get_case_subject_in_Description(), self.d)
            print("case/subject is visible")
            if case_subject.is_displayed():
                self.logger.info("case/subject textbox is visible in description")
                self.status.append(True)
            else:
                self.logger.info("case/subject textbox is not visible in description")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_007.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_007.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_007.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_007.png")
            self.logger.error(f"TC_notes_007 got exception as: {ex} ")

    def on_notes_panel_inside_action_dropdown_Enter_a_text_on_case_Subject_and_click_on_search_notes_is_displayed_as_expected(self):
        try:
            self.logger.info("*****TC_08***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.two_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH,
                                                                notes_Read_Ini().get_description_in_search_dropdown())
            print("description is visible")
            description_in_searchdropdown.click()
            case_subject = self.d.find_element(By.XPATH, notes_Read_Ini().get_case_subject_in_Description())
            case_subject.clear()
            case_subject.send_keys(notes_Read_Ini().enter_a_text_in_Case_subject())
            self.logger.info("text is entered on case/subject textbox")
            time.sleep(web_driver.one_second)
            search_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_button_on_Description())
            search_button.click()
            time.sleep(web_driver.one_second)
            search_criteria = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_criteria())
            print("case/subject is on search creteria")
            if search_criteria.is_displayed():
                self.logger.info("search criteria for case/subject is visible")
                self.status.append(True)
            else:
                self.logger.info("search criteria for case/subject is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_08.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_08.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_08.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_08.png")
            self.logger.error(f"TC_notes_08 got exception as: {ex} ")

    def on_notes_panel_inside_search_dropdown_Enter_a_case_Subject_and_click_on_clear_text_is_cleared_on_textbox(self):
        try:
            self.logger.info("*****TC_09***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH,
                                                                notes_Read_Ini().get_description_in_search_dropdown())
            description_in_searchdropdown.click()
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, notes_Read_Ini().get_case_subject_in_Description())
            case_subject.clear()
            case_subject.send_keys(notes_Read_Ini().enter_a_text_in_Case_subject())
            time.sleep(web_driver.one_second)
            clear_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_clear_button_on_Description())
            clear_button.click()
            print("text on case/subject is cleared")
            text = case_subject.text
            print("text is", text)
            if text == "":
                self.logger.info("text is cleared on textbox")
                self.status.append(True)
            else:
                self.logger.info("text is not cleared on textbox")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_09.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_09.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_09.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_09.png")
            self.logger.error(f"TC_notes_09 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_inside_search_dropdown_verify_and_click_either_sort_by_A_Z_or_sort_by_Z_A_radio_button_is_clickable(self):
        try:
            self.logger.info("*****TC_010***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH,
                                                                notes_Read_Ini().get_description_in_search_dropdown())
            description_in_searchdropdown.click()
            time.sleep(web_driver.one_second)
            # radio_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_sort_by_AtoZ_radiobutton_in_Description())
            # radio_button.click()
            radio_button = self.d.find_element(By.XPATH,
                                               notes_Read_Ini().get_sort_by_ZtoA_radiobutton_in_Description())
            radio_button.click()
            time.sleep(web_driver.one_second)
            print("radio button is selected")
            if radio_button.is_enabled():
                self.logger.info("radio button is enabled")
                self.status.append(True)
            else:
                self.logger.info("radio button is not enabled")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_010.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_010.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_010.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_010.png")
            self.logger.error(f"TC_notes_010 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_inside_search_dropdown_click_on_sort_by_AtoZ_radio_button_followed_by_Location_store_in_sort_by_dropdown_click_on_search_notes_is_displayed(
            self):
        try:
            self.logger.info("*****TC_011***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH,
                                                                notes_Read_Ini().get_description_in_search_dropdown())
            description_in_searchdropdown.click()
            radio_button = self.d.find_element(By.XPATH,
                                               notes_Read_Ini().get_sort_by_AtoZ_radiobutton_in_Description())
            radio_button.click()
            sel = Select(self.d.find_element(By.XPATH, notes_Read_Ini().get_sort_by_dropdown()))
            sel.select_by_index(1)
            self.logger.info("selecting location/store in sort by dropdown")
            search_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_button_on_Description())
            search_button.click()
            time.sleep(web_driver.two_second)
            sort_key = self.d.find_element(By.XPATH, notes_Read_Ini().get_sort_key_on_notes())
            if sort_key.is_displayed():
                self.logger.info("sort key is displayed after clicking search button")
                self.status.append(True)
            else:
                self.logger.info("sort key is not displayed after clicking search button")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_011.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_011.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_011.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_011.png")
            self.logger.error(f"TC_notes_011 got exception as: {ex} ")

    def on_notes_panel_inside_search_dropdown_click_on_sort_by_AtoZ_radio_button_followed_by_Location_store_in_sort_by_dropdown_click_on_clear_Location_store_is_cleared_on_dropdown(
            self):
        try:
            self.logger.info("*****TC_012***** started")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH,
                                                                notes_Read_Ini().get_description_in_search_dropdown())
            description_in_searchdropdown.click()
            radio_button = self.d.find_element(By.XPATH,
                                               notes_Read_Ini().get_sort_by_AtoZ_radiobutton_in_Description())
            radio_button.click()
            sel = Select(self.d.find_element(By.XPATH, notes_Read_Ini().get_sort_by_dropdown()))
            sel.select_by_index(1)
            self.logger.info("selecting first option in sort by dropdown")
            clear_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_clear_button_on_Description())
            clear_button.click()
            if radio_button.is_enabled():
                self.logger.info("after clicking clear button checking radio button is enabled")
                self.status.append(True)
            else:
                self.logger.info("after clicking clear button checking radio button is not enabled")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_012.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_012.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_012.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_012.png")
            self.logger.error(f"TC_notes_012 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_inside_search_dropdown_click_on_sort_by_Z_A_radio_button_followed_by_case_subject_in_sort_by_dropdown_click_on_search_notes_is_displayed(self):
        try:
            self.logger.info("*****TC_013***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH,notes_Read_Ini().get_description_in_search_dropdown())
            description_in_searchdropdown.click()
            time.sleep(web_driver.two_second)
            radio_button = self.d.find_element(By.XPATH,notes_Read_Ini().get_sort_by_ZtoA_radiobutton_in_Description())
            radio_button.click()
            sel = Select(self.d.find_element(By.XPATH, notes_Read_Ini().get_sort_by_dropdown()))
            sel.select_by_index(2)
            self.logger.info("selecting second option in sort by dropdown")
            time.sleep(web_driver.one_second)
            search_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_button_on_Description())
            search_button.click()
            time.sleep(web_driver.one_second)
            sort_key = self.d.find_element(By.XPATH, notes_Read_Ini().get_sort_key_on_notes())
            if sort_key.is_displayed():
                self.logger.info("sortkey is displayed by selecting case/subject")
                self.status.append(True)
            else:
                self.logger.info("sort key is not displayed by selecting case/subject")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_013.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_013.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_013.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_013.png")
            self.logger.error(f"TC_notes_013 got exception as: {ex} ")

    def on_notes_panel_inside_search_dropdown_click_on_sort_by_ZtoA_radio_button_followed_by_case_subject_in_sort_by_dropdown_click_on_clear_case_subject_is_cleared_on_dropdown(
            self):
        try:
            self.logger.info("*****TC_014***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH,notes_Read_Ini().get_description_in_search_dropdown())
            description_in_searchdropdown.click()
            radio_button = self.d.find_element(By.XPATH,notes_Read_Ini().get_sort_by_ZtoA_radiobutton_in_Description())
            radio_button.click()
            sel = Select(self.d.find_element(By.XPATH, notes_Read_Ini().get_sort_by_dropdown()))
            sel.select_by_index(2)
            self.logger.info("selecting second option in sort by dropdown")
            clear_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_clear_button_on_Description())
            clear_button.click()
            time.sleep(web_driver.two_second)
            if radio_button.is_enabled():
                self.logger.info(" radio button is enabled after clearing")
                self.status.append(True)
            else:
                self.logger.info("radio button is not enabled after clearing")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_014.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_014.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_014.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_014.png")
            self.logger.error(f"TC_notes_014 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_inside_search_dropdown_verify_and_enter_a_text_on_both_Location_store_and_Case_subject_and_click_on_search_notes_is_displayed(self):
        try:
            self.logger.info("*****TC_015***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH,
                                                                notes_Read_Ini().get_description_in_search_dropdown())
            description_in_searchdropdown.click()
            time.sleep(web_driver.one_second)
            location_store = self.d.find_element(By.XPATH, notes_Read_Ini().get_Location_store_in_Description())
            location_store.clear()
            location_store.send_keys(notes_Read_Ini().enter_a_text_in_location_store())
            self.logger.info("text is enterd on loaction/store")
            case_subject = self.d.find_element(By.XPATH, notes_Read_Ini().get_case_subject_in_Description())
            case_subject.clear()
            case_subject.send_keys(notes_Read_Ini().enter_a_text_in_Case_subject())
            self.logger.info("text is entered on case/subject")
            time.sleep(web_driver.one_second)
            search_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_button_on_Description())
            search_button.click()
            time.sleep(web_driver.one_second)
            search_criteria = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_criteria())
            print("Location/store and case/subject is on search creteria")
            if search_criteria.is_displayed():
                self.logger.info("search criteria is showing both location and case text")
                self.status.append(True)
            else:
                self.logger.info("search criteria is not showing both location and case text")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_015.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_015.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_015.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_015.png")
            self.logger.error(f"TC_notes_015 got exception as: {ex} ")


    def on_notes_panel_inside_searchdropdown_verify_and_enter_a_text_on_both_Location_store_and_Case_subject_and_click_on_clear_text_is_cleared(self):
        try:
            self.logger.info("*****TC_016***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH,
                                                                notes_Read_Ini().get_description_in_search_dropdown())
            description_in_searchdropdown.click()
            time.sleep(web_driver.one_second)
            location_store = self.d.find_element(By.XPATH, notes_Read_Ini().get_Location_store_in_Description())
            location_store.clear()
            location_store.send_keys(notes_Read_Ini().enter_a_text_in_location_store())
            case_subject = self.d.find_element(By.XPATH, notes_Read_Ini().get_case_subject_in_Description())
            case_subject.clear()
            case_subject.send_keys(notes_Read_Ini().enter_a_text_in_Case_subject())
            time.sleep(web_driver.one_second)
            clear_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_clear_button_on_Description())
            clear_button.click()
            print("text on case/subject is cleared")
            text = case_subject.text
            print("text is", text)
            if text == "":
                self.logger.info("text is cleared on both textboxes")
                self.status.append(True)
            else:
                self.logger.info("text is not cleared on both textboxes")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_016.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_016.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_016.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_016.png")
            self.logger.error(f"TC_notes_016 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_inside_searchdropdown_Enter_a_text_on_location_store_textbox_click_on_search_on_note_page_in_search_criteria_location_store_details_are_visible(
            self):
        try:
            self.logger.info("*****TC_017***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH,
                                                                notes_Read_Ini().get_description_in_search_dropdown())
            description_in_searchdropdown.click()
            time.sleep(web_driver.one_second)
            location_store = self.d.find_element(By.XPATH, notes_Read_Ini().get_Location_store_in_Description())
            location_store.clear()
            location_store.send_keys(notes_Read_Ini().enter_a_text_in_location_store())
            time.sleep(web_driver.one_second)
            search_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_button_on_Description())
            search_button.click()
            location_store_name = self.d.find_element(By.XPATH,
                                                      notes_Read_Ini().get_location_store_in_search_criteria())
            if location_store_name.is_displayed():
                self.logger.info("search criteria is showing location/store details")
                self.status.append(True)
            else:
                self.logger.info("search criteria is not showing location/store details")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_017.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_017.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_017.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_017.png")
            self.logger.error(f"TC_notes_017 got exception as: {ex} ")

    def on_notes_panel_inside_searchdropdown_Enter_a_text_on_case_subject_textbox_click_on_search_on_notes_page_search_criteria_case_subject_details_are_visible(
            self):
        try:
            self.logger.info("******TC_018***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH,
                                                                notes_Read_Ini().get_description_in_search_dropdown())
            description_in_searchdropdown.click()
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, notes_Read_Ini().get_case_subject_in_Description())
            case_subject.clear()
            case_subject.send_keys(notes_Read_Ini().enter_a_text_in_Case_subject())
            time.sleep(web_driver.one_second)
            search_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_button_on_Description())
            search_button.click()
            case_subject_name = self.d.find_element(By.XPATH,
                                                    notes_Read_Ini().get_location_store_in_search_criteria())
            if case_subject_name.is_displayed():
                self.logger.info("search criteria is showing case/subject details")
                self.status.append(True)
            else:
                self.logger.info("search criteria is not showing case/subject details")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_018.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_018.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_018.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_018.png")
            self.logger.error(f"TC_notes_018 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_inside_search_dropdown_Enter_both_location_store_and_case_subject_both_details_are_displayed_on_search_criteria(self):
        try:
            self.logger.info("******TC_019******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH,
                                                                notes_Read_Ini().get_description_in_search_dropdown())
            description_in_searchdropdown.click()
            time.sleep(web_driver.one_second)
            location_store = self.d.find_element(By.XPATH, notes_Read_Ini().get_Location_store_in_Description())
            location_store.clear()
            location_store.send_keys(notes_Read_Ini().enter_a_text_in_location_store())
            case_subject = self.d.find_element(By.XPATH, notes_Read_Ini().get_case_subject_in_Description())
            case_subject.clear()
            case_subject.send_keys(notes_Read_Ini().enter_a_text_in_Case_subject())
            time.sleep(web_driver.one_second)
            search_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_button_on_Description())
            search_button.click()
            search_criteria = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_criteria())
            print("Location/store and case/subject is on search creteria")
            if search_criteria.is_displayed():
                self.logger.info("search criteria is showing both location/case deails")
                self.status.append(True)
            else:
                self.logger.info("search criteria is not showing both loaction/store,case/subject details")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_019.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_019.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_019.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_019.png")
            self.logger.error(f"TC_notes_019 got exception as: {ex} ")

    def on_notes_panel_inside_searchdropdown_Enter_both_location_store_and_case_subject_and_click_on_cross_symbol_on_search_criteria_details_on_search_criteria_are_removed(
            self):
        try:
            self.logger.info("*******TC_020******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            description_in_searchdropdown = self.d.find_element(By.XPATH,
                                                                notes_Read_Ini().get_description_in_search_dropdown())
            description_in_searchdropdown.click()
            time.sleep(web_driver.one_second)
            location_store = self.d.find_element(By.XPATH, notes_Read_Ini().get_Location_store_in_Description())
            location_store.clear()
            location_store.send_keys(notes_Read_Ini().enter_a_text_in_location_store())
            case_subject = self.d.find_element(By.XPATH, notes_Read_Ini().get_case_subject_in_Description())
            case_subject.clear()
            case_subject.send_keys(notes_Read_Ini().enter_a_text_in_Case_subject())
            time.sleep(web_driver.one_second)
            search_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_button_on_Description())
            search_button.click()
            search_criteria = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_criteria())
            print("Location/store and case/subject is on search creteria")
            cross_symbol_on_searchcriteria = self.d.find_element(By.XPATH,
                                                                 notes_Read_Ini().get_cross_symbol_on_searchcriteria())
            cross_symbol_on_searchcriteria.click()
            if search_criteria.is_displayed():
                self.logger.info("location/store,case/subject details are removed after clicking cross symbol")
                self.status.append(True)
            else:
                self.logger.info("location/store,case/subject is not removed")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_020.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_020.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_020.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_020.png")
            self.logger.error(f"TC_notes_020 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_Click_on_location_inside_Search_Drop_down_map_is_visible(self):
        try:
            self.logger.info("*******TC_021***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            Location_in_searchdropdown = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().get_location_in_searchdropdown())
            self.logger.info("location option is visible in search dropdown")
            Location_in_searchdropdown.click()
            map_visible = self.d.find_element(By.XPATH, notes_Read_Ini().get_map_is_visible())
            if map_visible.is_displayed():
                self.logger.info("map is visible")
                self.status.append(True)
            else:
                self.logger.info("map is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_021.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_021.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_021.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_021.png")
            self.logger.error(f"TC_notes_021 got exception as: {ex} ")
            print(ex)

    def verify_the_heading_of_map_Notes_Location_is_visible(self):
        try:
            self.logger.info("********TC_022***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            Location_in_searchdropdown = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().get_location_in_searchdropdown())
            Location_in_searchdropdown.click()
            time.sleep(web_driver.one_second)
            heading_notes_location = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_location())
            time.sleep(web_driver.one_second)
            if heading_notes_location.is_displayed():
                self.logger.info("notes location panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("notes location panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_022.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_022.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_022.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_022.png")
            self.logger.error(f"TC_notes_022 got exception as: {ex} ")

    def verify_Find_location_textbox_is_visible_on_Notes_Location_page(self):
        try:
            self.logger.info("******TC_023***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            Location_in_searchdropdown = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().get_location_in_searchdropdown())
            Location_in_searchdropdown.click()
            time.sleep(web_driver.one_second)
            find_location_textbox = self.d.find_element(By.XPATH,
                                                        notes_Read_Ini().get_find_location_textbox_in_notes_location())
            if find_location_textbox.is_displayed():
                self.logger.info("find loction text box is visible in notes-location page")
                self.status.append(True)
            else:
                self.logger.info("find location text box is not visible in notes-location page")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_023.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_023.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_023.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_023.png")
            self.logger.error(f"TC_notes_023 got exception as: {ex} ")

    def on_notes_location_panel_Enter_a_location_in_Find_location_textbox_verify_dropdown_list_is_visible(self):
        try:
            self.logger.info("*******TC_024***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            Location_in_searchdropdown = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().get_location_in_searchdropdown())
            Location_in_searchdropdown.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_location())
            if len(heading_notes_location) > 0:
                find_location_textbox = self.d.find_element(By.XPATH,notes_Read_Ini().get_find_location_textbox_in_notes_location())
                find_location_textbox.clear()
                find_location_textbox.send_keys(notes_Read_Ini().enter_text_on_find_location())
                self.logger.info("text is enterd on location textbox")
                time.sleep(web_driver.two_second)
                action = ActionChains(self.d)
                action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                time.sleep(web_driver.two_second)
                marker = self.d.find_element(By.XPATH, notes_Read_Ini().get_marker_pointer())
                if marker.is_displayed():
                    self.logger.info("marker is visible on entered location")
                    self.status.append(True)
                else:
                    self.logger.info("marker is not visible on entered location")
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_024.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_024.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_024.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_024.png")
            self.logger.error(f"TC_notes_024 got exception as: {ex} ")

    def on_notes_location_panel_verify_Draw_circle_button_is_visible(self):
        try:
            self.logger.info("******TC_025****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            Location_in_searchdropdown = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().get_location_in_searchdropdown())
            Location_in_searchdropdown.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_elements(By.XPATH,
                                                          notes_Read_Ini().get_heading_of_notes_location())
            time.sleep(web_driver.one_second)
            drawcircle_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_drawcircle_button())
            if drawcircle_button.is_displayed():
                self.logger.info("draw circle button is visible on notes-location")
                self.status.append(True)
            else:
                self.logger.info("draw circle button is not visible on notes-location")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_025.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_025.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_025.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_025.png")
            self.logger.error(f"TC_notes_025 got exception as: {ex} ")

    def click_on_Draw_circle_circle_is_drawn_on_map_map_marker_is_pointing_location(self):
        try:
            # self.logger.info("*******TC_031******started")
            self.load_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.one_second)
            heading_notes_location = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_location())
            if len(heading_notes_location) > 0:
                drawcircle_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_drawcircle_button())
                drawcircle_button.click()
                # moving_to_map=self.d.find_element(By.XPATH,notes_Read_Ini().get_circledrawn_on_map())
                action = ActionChains(self.d)
                moving_particular_location = self.d.find_element(By.XPATH,
                                                                 notes_Read_Ini().moving_paricular_location_on_map())
                print(moving_particular_location.location)
                # action=ActionChains(self.d)
                # action.move_to_element_with_offset(moving_to_map,120,150).perform()
            else:
                cloud_login_menu_after_login = self.d.find_element(By.XPATH,
                                                                   notes_Read_Ini().get_afterlogin_cloud_menu_is_visible())
                cloud_login_menu_after_login.click()
                time.sleep(web_driver.one_second)
                notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
                notes.click()
                heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
                time.sleep(web_driver.one_second)
                search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
                search_dropdown.click()
                time.sleep(web_driver.one_second)
                Location_in_searchdropdown = self.d.find_element(By.XPATH,
                                                                 notes_Read_Ini().get_location_in_searchdropdown())
                Location_in_searchdropdown.click()
                time.sleep(web_driver.two_second)
                heading_notes_location = self.d.find_elements(By.XPATH,
                                                              notes_Read_Ini().get_heading_of_notes_location())
                time.sleep(web_driver.one_second)
                drawcircle_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_drawcircle_button())
                drawcircle_button.click()
                # moving_to_map = self.d.find_element(By.XPATH, notes_Read_Ini().get_circledrawn_on_map())
                action = ActionChains(self.d)
                action.move_by_offset(24, 71).pause(5).perform()
                # action.move_to_element_with_offset(moving_to_map, 60, 75).perform()
        except Exception as ex:
            print(ex)

    def on_notes_loaction_panel_Click_on_toggle_symbol_full_screen_is_displayed(self):
        try:
            self.logger.info("*******TC_026****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.explicit_wait(10, "XPATH", notes_Read_Ini().get_notes_is_displayed(), self.d)
            notes.click()
            heading_notes = self.explicit_wait(10, "XPATH", notes_Read_Ini().get_heading_of_notes_page(), self.d)
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            Location_in_searchdropdown = self.explicit_wait(10, "XPATH", notes_Read_Ini()
                                                            .get_location_in_searchdropdown(), self.d)
            Location_in_searchdropdown.click()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_heading_of_notes_location(), self.d)
            heading_notes_location = self.d.find_elements(By.XPATH,
                                                          notes_Read_Ini().get_heading_of_notes_location())
            time.sleep(web_driver.one_second)
            toggle_symbol = self.d.find_element(By.XPATH, notes_Read_Ini().get_toggle_full_screen_view())
            self.logger.info("toogle is displayed on notes-location")
            toggle_symbol.click()
            time.sleep(web_driver.one_second)
            after_clicking_fullscreen_toggle = self.explicit_wait(10, "XPATH", notes_Read_Ini()
                                                                  .get_after_clicking_fullscreen_view(), self.d)
            if after_clicking_fullscreen_toggle.is_displayed():
                self.logger.info("full screen toggle symbol is visible")
                self.status.append(True)
            else:
                self.logger.info("full screen toggle symbol is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            after_clicking_fullscreen_toggle.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_026.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_026.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_026.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_026.png")
            self.logger.error(f"TC_notes_026 got exception as: {ex} ")
            print(ex)

    def on_notes_location_panel_Click_on_ESC_button_on_keyboard_Full_Screen_view_is_minimized(self):
        try:
            self.logger.info("*******TC_027**** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.explicit_wait(10, "XPATH", notes_Read_Ini().get_notes_is_displayed(), self.d)
            notes.click()
            heading_notes = self.explicit_wait(10, "XPATH", notes_Read_Ini().get_heading_of_notes_page(), self.d)
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            Location_in_searchdropdown = self.explicit_wait(10, "XPATH", notes_Read_Ini()
                                                            .get_location_in_searchdropdown(), self.d)
            Location_in_searchdropdown.click()
            time.sleep(web_driver.two_second)
            toggle_symbol = self.explicit_wait(10, "XPATH", notes_Read_Ini().get_toggle_full_screen_view(), self.d)
            toggle_symbol.click()
            time.sleep(web_driver.one_second)
            after_clicking_fullscreen_toggle = self.explicit_wait(10, "XPATH", notes_Read_Ini()
                                                                  .get_after_clicking_fullscreen_view(), self.d)
            time.sleep(web_driver.one_second)
            after_clicking_fullscreen_toggle.click()
            if toggle_symbol.is_displayed():
                self.logger.info("after clicking esc button by using keys full screen is minimized toggle symbol is displayed")
                self.status.append(True)
            else:
                self.logger.info("after clicking esc button by using sendkeys full screen is not minimezed and not showing toogle symbol")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_027.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_027.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_027.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_027.png")
            self.logger.error(f"TC_notes_027 got exception as: {ex} ")

    def on_notes_location_panel_verify_and_click_on_plus_symbol_on_Notes_location_page_map_is_maximized(self):
        try:
            self.logger.info("******TC_028***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            Location_in_searchdropdown = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().get_location_in_searchdropdown())
            Location_in_searchdropdown.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_elements(By.XPATH,
                                                          notes_Read_Ini().get_heading_of_notes_location())
            time.sleep(web_driver.one_second)
            print("Symbol is visible")
            zoom_in = self.d.find_element(By.XPATH, notes_Read_Ini().get_zoom_in_on_map())
            zoom_in.click()
            zoom_in.click()
            time.sleep(web_driver.two_second)
            toggle_symbol = self.d.find_element(By.XPATH, notes_Read_Ini().get_toggle_full_screen_view())
            if toggle_symbol.is_displayed():
                self.logger.info("clicking the plus symbol map is zoom in")
                self.status.append(True)
            else:
                self.logger.info("clicking the plus symbol map is zoom out")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_028.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_028.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_028.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_028.png")
            self.logger.error(f"TC_notes_028 got exception as: {ex} ")
            print(ex)

    def on_notes_location_panel_click_on_minus_symbol_on_Notes_location_page_map_is_minimized(self):
        try:
            self.logger.info("*****TC_029***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            Location_in_searchdropdown = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().get_location_in_searchdropdown())
            Location_in_searchdropdown.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_elements(By.XPATH,
                                                          notes_Read_Ini().get_heading_of_notes_location())
            time.sleep(web_driver.one_second)
            print("Symbol is visible")
            zoom_out = self.d.find_element(By.XPATH, notes_Read_Ini().get_zoom_out_())
            zoom_out.click()
            zoom_out.click()
            toggle_symbol = self.d.find_element(By.XPATH, notes_Read_Ini().get_toggle_full_screen_view())
            if toggle_symbol.is_displayed():
                self.logger.info("clicking minus symbol map is zoom out")
                self.status.append(True)
            else:
                self.logger.info("clicking the minus symbol map is zoom out")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_029.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_029.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_029.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_029.png")
            self.logger.error(f"TC_notes_029 got exception as: {ex} ")

    def on_notes__location_panel_Click_on_three_horizantal_lines_on_right_side_of_map_Select_a_Search_Target_Window_is_dispayed(self):
        try:
            self.logger.info("*********TC_030***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            Location_in_searchdropdown = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().get_location_in_searchdropdown())
            Location_in_searchdropdown.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_elements(By.XPATH,
                                                          notes_Read_Ini().get_heading_of_notes_location())
            time.sleep(web_driver.one_second)
            tribar = self.d.find_element(By.XPATH, notes_Read_Ini().get_tribar_on_map())
            self.logger.info("on map three horizantal lines are displeyed")
            tribar.click()
            time.sleep(web_driver.one_second)
            search_target_window = self.d.find_element(By.XPATH,
                                                       notes_Read_Ini().get_linktext_searchtarget_on_map())
            if search_target_window.is_displayed():
                self.logger.info("after clicking tribar search target window is displayed")
                self.status.append(True)
            else:
                self.logger.info("after clicking tribar search target window is not displayed")
                self.status.append(False)
            cancel_button=self.d.find_element(By.XPATH,notes_Read_Ini().get_cancel_button())
            cancel_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_030.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_030.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_030.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_030.png")
            self.logger.error(f"TC_notes_030 got exception as: {ex} ")
            print(ex)

    def on_notes_location_panel_In_Select_a_search_Target_Drop_down_and_click_on_Events_location_map_is_displayed(self):
        try:
            self.logger.info("********TC_031****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_heading_of_notes_page(), self.d)
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            Location_in_searchdropdown = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().get_location_in_searchdropdown())
            Location_in_searchdropdown.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_elements(By.XPATH,
                                                          notes_Read_Ini().get_heading_of_notes_location())
            time.sleep(web_driver.one_second)
            tribar = self.d.find_element(By.XPATH, notes_Read_Ini().get_tribar_on_map())
            tribar.click()
            time.sleep(web_driver.one_second)
            sel = Select(self.d.find_element(By.XPATH, notes_Read_Ini().get_search_target_dropdown()))
            sel.select_by_visible_text("Probable Match Events")
            self.logger.info("selecting events in search target window")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_location_panel_headings(), self.d)
            Event_location = self.d.find_element(By.XPATH, notes_Read_Ini().get_location_panel_headings())
            if Event_location.is_displayed():
                self.logger.info("notes-events location panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("notes-events location panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)

            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_031.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_031.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_031.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_031.png")
            self.logger.error(f"TC_notes_031 got exception as: {ex} ")
            print(ex)

    def on_notes_location_panel_in_Select_a_search_Target_Drop_down_and_click_on_Notes_Notes_location_map_is_displayed(self):
        try:
            self.logger.info("********TC_032******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            Location_in_searchdropdown = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().get_location_in_searchdropdown())
            Location_in_searchdropdown.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_elements(By.XPATH,
                                                          notes_Read_Ini().get_heading_of_notes_location())
            time.sleep(web_driver.one_second)
            tribar = self.d.find_element(By.XPATH, notes_Read_Ini().get_tribar_on_map())
            tribar.click()
            time.sleep(web_driver.one_second)
            sel = Select(self.d.find_element(By.XPATH, notes_Read_Ini().get_search_target_dropdown()))
            sel.select_by_visible_text("Notes")
            self.logger.info("notes is selected in search target dropdown")
            time.sleep(web_driver.two_second)
            Notes_location = self.d.find_element(By.XPATH, notes_Read_Ini().get_location_panel_headings())
            if Notes_location.is_displayed():
                self.logger.info("notes loaction panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("notes location panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)

            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_032.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_032.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_032.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_032.png")
            self.logger.error(f"TC_notes_032 got exception as: {ex} ")

    def on_notes_location_panel_click_on_three_horizantal_lines_followed_by_click_on_cancel_button_on_Select_Search_Target_window_is_closed(self):
        try:
            self.logger.info("******TC_033******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            Location_in_searchdropdown = self.d.find_element(By.XPATH,notes_Read_Ini().get_location_in_searchdropdown())
            Location_in_searchdropdown.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_elements(By.XPATH,notes_Read_Ini().get_heading_of_notes_location())
            time.sleep(web_driver.one_second)
            tribar = self.d.find_element(By.XPATH, notes_Read_Ini().get_tribar_on_map())
            tribar.click()
            time.sleep(web_driver.one_second)
            cancel_button = self.d.find_element(By.XPATH, notes_Read_Ini().get_cancel_button())
            cancel_button.click()
            time.sleep(web_driver.one_second)
            Notes_location = self.d.find_element(By.XPATH, notes_Read_Ini().get_location_panel_headings())
            if Notes_location.is_displayed():
                self.logger.info("after clicking cancel button notes-loaction panel heading is visible ")
                self.status.append(True)
            else:
                self.logger.info("after clicking cancel button notes-location panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)

            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_033.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_033.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_033.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_033.png")
            self.logger.error(f"TC_notes_033 got exception as: {ex} ")
            print(ex)

    def click_on_cross_symbol_on_Notes_location_page_is_closed(self):
        try:
            self.logger.info("*******TC_034***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            Location_in_searchdropdown = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().get_location_in_searchdropdown())
            Location_in_searchdropdown.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_elements(By.XPATH,
                                                          notes_Read_Ini().get_heading_of_notes_location())
            time.sleep(web_driver.one_second)
            closing_notes_Location_panel = self.d.find_element(By.XPATH, notes_Read_Ini().get_close_button())
            closing_notes_Location_panel.click()
            time.sleep(web_driver.two_second)
            if len(heading_notes_location) > 1:
                self.logger.info("closing notes-location more than one page is displayed")
                self.status.append(False)
            else:
                self.logger.info("closing notes-location  one page is displayed")
                self.status.append(True)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_034.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_034.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_034.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_034.png")
            self.logger.error(f"TC_notes_034 got exception as: {ex} ")
            print(ex)

    def click_on_cross_symbol_on_Event_page_is_closed(self):
        try:
            self.logger.info("*******TC_035******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.two_second)
            search_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_search_dropdown_on_notes_page())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            Location_in_searchdropdown = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().get_location_in_searchdropdown())
            Location_in_searchdropdown.click()
            time.sleep(web_driver.two_second)
            tribar = self.d.find_element(By.XPATH, notes_Read_Ini().get_tribar_on_map())
            tribar.click()
            time.sleep(web_driver.one_second)
            sel = Select(self.d.find_element(By.XPATH, notes_Read_Ini().get_search_target_dropdown()))
            sel.select_by_visible_text("Probable Match Events")
            time.sleep(web_driver.two_second)
            closing_notes_Location_panel = self.d.find_element(By.XPATH, notes_Read_Ini().get_close_button())
            closing_notes_Location_panel.click()
            time.sleep(web_driver.one_second)
            Events_location = self.d.find_elements(By.XPATH, notes_Read_Ini().get_Events_location_whole_xpath())
            if len(Events_location) > 1:
                self.logger.info("closing events location page dispalying more than one page")
                self.status.append(False)
            else:
                self.logger.info("closing events location page displaying only one page")
                self.status.append(True)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_035.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_035.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_035.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_035.png")
            self.logger.error(f"TC_notes_035 got exception as: {ex} ")

    def verify_Action_Drop_down_is_visible_on_Notes(self):
        try:
            self.logger.info("******TC_036****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            if Action_dropdown.is_displayed():
                self.logger.info("action dropdown is visible on notes")
                self.status.append(True)
            else:
                self.logger.info("action dropdown is not visible in notes page")
                self.status.append(False)
            time.sleep(web_driver.one_second)

            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:

                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_036.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_036.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_036.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_036.png")
            self.logger.error(f"TC_notes_036 got exception as: {ex} ")
            print(ex)

    def click_on_Action_Drop_down_list_is_visible(self):
        try:
            self.logger.info("*******TC_037**** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            if create_note.is_displayed():
                self.logger.info("create note is visible in action dropdown")
                self.status.append(True)
            else:
                self.logger.info("create note is not visible in action dropdown")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_037.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_037.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_037.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_037.png")
            self.logger.error(f"TC_notes_037 got exception as: {ex} ")
            print(ex)

    def click_on_Create_User_in_Action_Dropdown_check_Create_Note_heading_is_visible(self):
        try:
            self.logger.info("*******TC_038****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.one_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.one_second)
            create_note_heading = self.d.find_element(By.XPATH, notes_Read_Ini().create_note_panel_heading())
            if create_note_heading.is_displayed():
                self.logger.info("create-note panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("create-note panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)

            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_038.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_038.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_038.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_038.png")
            self.logger.error(f"TC_notes_038 got exception as: {ex} ")
            print(ex)

    def verify_0n_Create_Note_imagebox_is_visible(self):
        try:
            self.logger.info("********TC_039****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.one_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.one_second)
            browse_a_image = self.d.find_element(By.XPATH, notes_Read_Ini().browse_a_image())
            if browse_a_image.is_displayed():
                self.logger.info("imagebox is visible")
                self.status.append(True)
            else:
                self.logger.info("imagebox is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_039.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_039.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_039.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_039.png")
            self.logger.error(f"TC_notes_039 got exception as: {ex} ")
            print(ex)

    def click_on_imagebox_and_select_a_image_from_desktop_location(self):
        try:
            self.logger.info("******TC_040***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.two_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            print("reached to img box")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\images\\img1.png"
            self.d.find_element(By.ID, "image0").send_keys(file_image_path)
            time.sleep(web_driver.two_second)
            add_image_heading = self.d.find_element(By.XPATH, notes_Read_Ini().add_note_image_panel_heading())
            if add_image_heading.is_displayed():
                self.logger.info("after uploading a image add-image panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("after uploading a image add-image panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_040.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_040.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_040.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_040.png")
            self.logger.error(f"TC_notes_040 got exception as: {ex} ")
            print(ex)

    def on_note_add_image_panel__after_image_selected_from_desktop_crop_image_skip_cropping_and_cancel_buttons_are_visible(self):
        try:
            self.logger.info("******TC_041***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.two_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            print("reached to img box")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\images\\img1.png"
            self.d.find_element(By.ID, "image0").send_keys(file_image_path)
            time.sleep(web_driver.two_second)
            add_image_heading = self.d.find_element(By.XPATH, notes_Read_Ini().add_note_image_panel_heading())
            cancel_button = self.d.find_element(By.XPATH, notes_Read_Ini().cancel_button_in_add_image())
            skip_cropping = self.d.find_element(By.XPATH, notes_Read_Ini().skip_cropping_button_in_add_image())
            crop_image = self.d.find_element(By.XPATH, notes_Read_Ini().crop_photo_button_in_add_image())
            time.sleep(web_driver.one_second)
            if cancel_button.is_displayed():
                self.logger.info("cancel button is visible")
                self.status.append(True)
            else:
                self.logger.info("cancel button is not visible")
                self.status.append(False)
            if skip_cropping.is_displayed():
                self.logger.info("skip cropping button is visible")
                self.status.append(True)
            else:
                self.logger.info("skip cropping button is not visible")
                self.status.append(False)
            if crop_image.is_displayed():
                self.logger.info("crop image button is visible")
                self.status.append(True)
            else:
                self.logger.info("crop image button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_041.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_041.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_041.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_041.png")
            self.logger.error(f"TC_notes_041 got exception as: {ex} ")
            print(ex)

    def on_note_add_image_panel_Click_cancel_button_on_Note_Add_Image_page_is_closed(self):
        try:
            self.logger.info("******TC_042******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.two_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            print("reached to img box")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\images\\img1.png"
            self.d.find_element(By.ID, "image0").send_keys(file_image_path)
            time.sleep(web_driver.two_second)
            add_image_heading = self.d.find_element(By.XPATH, notes_Read_Ini().add_note_image_panel_heading())
            time.sleep(web_driver.three_second)
            cancel_button = self.d.find_element(By.XPATH, notes_Read_Ini().cancel_button_in_add_image())
            cancel_button.click()
            time.sleep(web_driver.three_second)
            create_note = self.d.find_elements(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            if len(create_note) > 0:
                self.logger.info("after clicking cancel button pages are closed")
                self.status.append(True)
            else:
                self.logger.info("after clicking cancel button pages are not closed showing more than one pages")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            # logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_042.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_042.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_042.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_042.png")
            self.logger.error(f"TC_notes_042 got exception as: {ex} ")

    def on_note_add_image_panel_click_on_skip_cropping_Re_Crop_photo_select_photo_buttons_are_visible(self):
        try:
            self.logger.info("*********TC_043******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.three_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.three_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            print("reached to img box")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\images\\img1.png"
            self.d.find_element(By.ID, "image0").send_keys(file_image_path)
            time.sleep(web_driver.two_second)
            add_image_heading = self.d.find_element(By.XPATH, notes_Read_Ini().add_note_image_panel_heading())
            time.sleep(web_driver.three_second)
            skip_cropping = self.d.find_element(By.XPATH, notes_Read_Ini().skip_cropping_button_in_add_image())
            skip_cropping.click()
            time.sleep(web_driver.two_second)
            re_crop_button = self.d.find_element(By.XPATH, notes_Read_Ini().recrop_photo_button())
            time.sleep(web_driver.three_second)
            select_image = self.d.find_element(By.XPATH, notes_Read_Ini().select_image_button())
            time.sleep(web_driver.three_second)
            if re_crop_button.is_displayed():
                self.logger.info("re-crop button is visible")
                self.status.append(True)
            else:
                self.logger.info("re-crop button is not visible")
                self.status.append(False)
            if select_image.is_displayed():
                self.logger.info("select image button is visible")
                self.status.append(True)
            else:
                self.logger.info("select image button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_043.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_043.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_043.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_043.png")
            self.logger.error(f"TC_notes_043 got exception as: {ex} ")
            print(ex)

    def on_note_add_image_panel_click_on_select_photo_button_photo_is_selected(self):
        try:
            self.logger.info("*******TC_044******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.three_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.three_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            print("reached to img box")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\images\\img1.png"
            self.d.find_element(By.ID, "image0").send_keys(file_image_path)
            time.sleep(web_driver.two_second)
            add_image_heading = self.d.find_element(By.XPATH, notes_Read_Ini().add_note_image_panel_heading())
            time.sleep(web_driver.three_second)
            skip_cropping = self.d.find_element(By.XPATH, notes_Read_Ini().skip_cropping_button_in_add_image())
            skip_cropping.click()
            time.sleep(web_driver.two_second)
            select_image = self.d.find_element(By.XPATH, notes_Read_Ini().select_image_button())
            select_image.click()
            time.sleep(web_driver.three_second)
            create_note = self.d.find_elements(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            if len(create_note) > 0:
                self.logger.info("after uploading a image create-note is not displayed then status true")
                self.status.append(True)
            else:
                self.logger.info("after uploading a image create note is displayed then status false")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_044.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_044.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_044.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_044.png")
            self.logger.error(f"TC_notes_044 got exception as: {ex} ")
            print(ex)

    def on_note_add_image_panel_click_on_Re_Crop_button_cancel_Skip_cropping_crop_image_buttons_are_visible(self):
        try:
            self.logger.info("********TC_045****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.three_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.three_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            print("reached to img box")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\images\\img1.png"
            self.d.find_element(By.ID, "image0").send_keys(file_image_path)
            time.sleep(web_driver.two_second)
            add_image_heading = self.d.find_element(By.XPATH, notes_Read_Ini().add_note_image_panel_heading())
            skip_cropping = self.d.find_element(By.XPATH, notes_Read_Ini().skip_cropping_button_in_add_image())
            skip_cropping.click()
            time.sleep(web_driver.two_second)
            re_crop_button = self.d.find_element(By.XPATH, notes_Read_Ini().recrop_photo_button())
            re_crop_button.click()
            time.sleep(web_driver.two_second)
            cancel_button = self.d.find_element(By.XPATH, notes_Read_Ini().cancel_button_in_add_image())
            time.sleep(web_driver.two_second)
            skip_cropping = self.d.find_element(By.XPATH, notes_Read_Ini().skip_cropping_button_in_add_image())
            time.sleep(web_driver.two_second)
            crop_image = self.d.find_element(By.XPATH, notes_Read_Ini().crop_photo_button_in_add_image())
            time.sleep(web_driver.one_second)
            if cancel_button.is_displayed():
                self.logger.info("cancel button is displayed")
                self.status.append(True)
            else:
                self.logger.info("cancel button is not displaye")
                self.status.append(False)
            if skip_cropping.is_displayed():
                self.logger.info("skip-croping button is displayed")
                self.status.append(True)
            else:
                self.logger.info("skip cropping is button is not displayed")
                self.status.append(False)
            if crop_image.is_displayed():
                self.logger.info("crop image button is visible")
                self.status.append(True)
            else:
                self.logger.info("crop image button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_045.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_045.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_045.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_045.png")
            self.logger.error(f"TC_notes_045 got exception as: {ex} ")
            print(ex)

    def on_note_add_image_panel_click_on_crop_image_alert_is_displayed(self):
        try:
            self.logger.info("******TC_046****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.three_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.three_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            print("reached to img box")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\images\\img1.png"
            self.d.find_element(By.ID, "image0").send_keys(file_image_path)
            time.sleep(web_driver.two_second)
            crop_image = self.d.find_element(By.XPATH, notes_Read_Ini().crop_photo_button_in_add_image())
            crop_image.click()
            time.sleep(web_driver.two_second)
            a = self.d.switch_to.alert
            a.accept()
            add_image_heading = self.d.find_elements(By.XPATH, notes_Read_Ini().add_note_image_panel_heading())
            if len(add_image_heading) > 0:
                self.logger.info("add-iamge page is visible")
                self.status.append(True)
            else:
                self.logger.info("add-image page is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_046.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_046.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_046.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_046.png")
            self.logger.error(f"TC_notes_046 got exception as: {ex} ")
            print(ex)

    def on_create_note_panel_LOCATION_STORE_textbox_is_visible(self):
        try:
            self.logger.info("*******TC_047******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            Location_store_textbox_in_createnote = self.d.find_element(By.XPATH,notes_Read_Ini().Location_store_textbox_on_create_note())
            if Location_store_textbox_in_createnote.is_displayed():
                self.logger.info("location store textbox is visible")
                self.status.append(True)
            else:
                self.logger.info("location store textbox is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_047.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_047.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_047.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_047.png")
            self.logger.error(f"TC_notes_047 got exception as: {ex} ")
            print(ex)

    def on_create_note_panel_Enter_a_text_on_LOCATION_STORE_textbox(self):
        try:
            self.logger.info("******TC_048***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            Location_store_textbox_in_createnote = self.d.find_element(By.XPATH,
                                                                       notes_Read_Ini().Location_store_textbox_on_create_note())
            Location_store_textbox_in_createnote.clear()
            Location_store_textbox_in_createnote.send_keys(
                notes_Read_Ini().Enter_text_in_Location_store_in_create_note())
            entered_text = self.d.find_element(By.XPATH,
                                               notes_Read_Ini().Location_store_textbox_on_create_note()).text
            print(entered_text)
            if entered_text == notes_Read_Ini().Enter_text_in_Location_store_in_create_note():
                self.logger.info("if enterd text and reading text is not equal then status false")
                self.status.append(False)
            else:
                self.logger.info("if entered text and reading text from notes read ini  equal then status true")
                self.status.append(True)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_048.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_048.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_048.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_048.png")
            self.logger.error(f"TC_notes_048 got exception as: {ex} ")
            print(ex)

    def verify_CASE_SUBJECT_textbox_is_visible_on_create_note(self):
        try:
            self.logger.info("********TC_49********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            case_subject_in_createnote = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().case_subject_textbox_in_create_note())
            if case_subject_in_createnote.is_displayed():
                self.logger.info("case/subject textbox is visible")
                self.status.append(True)
            else:
                self.logger.info("case/subject textbox is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_049.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_049.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_049.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_049.png")
            self.logger.error(f"TC_notes_049 got exception as: {ex} ")
            print(ex)

    def on_crate_note_panel_Enter_a_text_on_CASE_SUBJECT_textbox(self):
        try:
            self.logger.info("*******TC_050****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            time.sleep(web_driver.two_second)
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            case_subject_in_createnote = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().case_subject_textbox_in_create_note())
            case_subject_in_createnote.clear()
            case_subject_in_createnote.send_keys(notes_Read_Ini().Enter_text_in_case_subject_in_create_note())
            time.sleep(web_driver.one_second)
            if case_subject_in_createnote.text == notes_Read_Ini().Enter_text_in_case_subject_in_create_note():
                self.status.append(False)
            else:
                self.status.append(True)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_050.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_050.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_050.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_050.png")
            self.logger.error(f"TC_notes_050 got exception as: {ex} ")
            print(ex)

    def verify_REPORTED_LOSS_textbox_is_visible_on_create_note(self):
        try:
            self.logger.info("*******TC_051****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            reported_loss = self.d.find_element(By.XPATH, notes_Read_Ini().reported_loss_in_create_note())
            if reported_loss.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_051.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_051.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_051.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_051.png")
            self.logger.error(f"TC_notes_051 got exception as: {ex} ")
            print(ex)

    def enter_a_text_on_REPORTED_LOSS_on_create_note_panel(self):
        try:
            self.logger.info("******TC_052******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            reported_loss = self.d.find_element(By.XPATH, notes_Read_Ini().reported_loss_in_create_note())
            reported_loss.clear()
            reported_loss.send_keys(notes_Read_Ini().Enter_reported_loss())
            if reported_loss.text == notes_Read_Ini().Enter_reported_loss():
                self.status.append(False)
            else:
                self.status.append(True)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_052.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_051.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_052.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_052.png")
            self.logger.error(f"TC_notes_052 got exception as: {ex} ")
            print(ex)

    def verify_on_create_note_claender_is_visible_in_date_of_incident(self):
        try:
            self.logger.info("*******TC_053****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            date_of_incident = self.d.find_element(By.XPATH, notes_Read_Ini().Date_of_incident())
            if date_of_incident.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_053.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_053.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_053.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_053.png")
            self.logger.error(f"TC_notes_053 got exception as: {ex} ")
            print(ex)

    def on_create_notes_panel_click_date_of_incident_calender_symbol_calender_is_displayed(self):
        try:
            self.logger.info("********TC_054******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            date_of_incident = self.d.find_element(By.XPATH, notes_Read_Ini().Date_of_incident())
            date_of_incident.send_keys(notes_Read_Ini().date_time_of_incident())
            if date_of_incident.text == notes_Read_Ini().date_time_of_incident():
                self.status.append(False)
            else:
                self.status.append(True)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_054.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_054.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_054.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_054.png")
            self.logger.error(f"TC_notes_054 got exception as: {ex} ")
            print(ex)

    def on_create_note_panel_verify_CASE_EVENT_TYPE_drop_down_is_visible(self):
        try:
            self.logger.info("*******TC_055****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            case_event_type_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().case_event_type())
            if case_event_type_dropdown.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_055.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_055.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_055.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_055.png")
            self.logger.error(f"TC_notes_055 got exception as: {ex} ")
            print(ex)

    def on_create_note_panel_click_on_CASE_EVENT_TYPE_dropdown_list_is_visible_select_any_element_present_in_dropdown_list(self):
        try:
            self.logger.info("*******TC_056******** started")
            mylist = []
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            case_event_type_dropdown = self.d.find_elements(By.XPATH, notes_Read_Ini().case_event_type())
            time.sleep(web_driver.two_second)
            Employee_threatened_assaulted = self.d.find_element(By.XPATH,
                                                                notes_Read_Ini().employee_threat_by_xpath())
            print(Employee_threatened_assaulted.text)
            Employee_threatened_assaulted.click()
            time.sleep(web_driver.one_second)
            if Employee_threatened_assaulted.text.lower() == notes_Read_Ini().Employee_threatened_assaulted_option_in_dropdown().lower():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_056.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_056.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_056.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_056.png")
            self.logger.error(f"TC_notes_056 got exception as: {ex} ")
            print(ex)

    def verify_ACTIVITY_TYPE_drop_down_list_visible_on_create_note_panel(self):
        try:
            self.logger.info("*******TC_057****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            case_event_type_dropdown = self.d.find_elements(By.XPATH, notes_Read_Ini().case_event_type())
            time.sleep(web_driver.two_second)
            activity_type_dropdown_in_createnote = self.d.find_element(By.XPATH,
                                                                       notes_Read_Ini().activity_type_dropdown())
            time.sleep(web_driver.one_second)
            if activity_type_dropdown_in_createnote.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_057.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_057.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_057.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_057.png")
            self.logger.error(f"TC_notes_057 got exception as: {ex} ")
            print(ex)

    def on_create_note_panel_select_any_option_on_ACTIVITY_TYPE_drop_down_option_and_verify_option_is_selected(self):
        try:
            self.logger.info("********tc_058******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            case_event_type_dropdown = self.d.find_elements(By.XPATH, notes_Read_Ini().case_event_type())
            activity_type_dropdown_in_createnote = self.d.find_element(By.XPATH,
                                                                       notes_Read_Ini().activity_type_dropdown())
            activity_type_dropdown_in_createnote.click()
            time.sleep(web_driver.one_second)
            gift_card_option_in_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().gift_card_by_xpath())
            gift_card_option_in_dropdown.click()
            print(gift_card_option_in_dropdown.text)
            time.sleep(web_driver.one_second)
            if gift_card_option_in_dropdown.text.lower() == notes_Read_Ini().gift_card_option_in_activity_type().lower():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_058.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_058.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_058.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_058.png")
            self.logger.error(f"TC_notes_058 got exception as: {ex} ")
            print(ex)

    def on_create_note_panel__click_on_METHOD_OF_OFFENCE_drop_down_list_is_visible(self):
        try:
            self.logger.info("*******TC_059****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            method_of_offence = self.d.find_element(By.XPATH, notes_Read_Ini().method_of_offence())
            if method_of_offence.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_059.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_059.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_059.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_059.png")
            self.logger.error(f"TC_notes_059 got exception as: {ex} ")
            print(ex)

    def on_create_note_panel_verify_and_select_element_on_METHOD_OF_OFFENCE_drop_down_is_selected(self):
        try:
            self.logger.info("******TC_060*******started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            method_of_offence = self.d.find_element(By.XPATH, notes_Read_Ini().method_of_offence())
            method_of_offence.click()
            time.sleep(web_driver.one_second)
            concealment_in_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().concealment_by_xpath())
            concealment_in_dropdown.click()
            print(concealment_in_dropdown.text)
            time.sleep(web_driver.one_second)
            if concealment_in_dropdown.text.lower() == notes_Read_Ini().concealment_option_in_dropdown().lower():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            cancel_btn = self.d.find_element(By.XPATH, notes_Read_Ini().create_notes_cancel_btn())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_060.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_060.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_060.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_060.png")
            self.logger.error(f"TC_notes_060 got exception as: {ex} ")
            print(ex)

    def verify_REPORTED_BY_textbox_is_visible_on_create_note(self):
        try:
            self.logger.info("*******TC_061****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            reported_by = self.d.find_element(By.XPATH, notes_Read_Ini().reported_by_textbox())
            time.sleep(web_driver.one_second)
            if reported_by.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_061.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_061.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_061.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_061.png")
            self.logger.error(f"TC_notes_061 got exception as: {ex} ")
            print(ex)

    def on_create_note_panel_Enter_a_text_on_REPORTED_BY_textbox(self):
        try:
            self.logger.info("*******TC_062****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            reported_by = self.d.find_element(By.XPATH, notes_Read_Ini().reported_by_textbox())
            time.sleep(web_driver.one_second)
            reported_by.send_keys(notes_Read_Ini().Enter_reported_loss())
            print(reported_by.text)
            if reported_by.text == "":
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_062.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_062.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_062.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_062.png")
            self.logger.error(f"TC_notes_062 got exception as: {ex} ")
            print(ex)

    def verify_on_BUILD_textbox_is_visible_on_create_note(self):
        try:
            self.logger.info("********TC_063******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            build_on_create_note = self.d.find_element(By.XPATH, notes_Read_Ini().build_on_createnote())
            if build_on_create_note.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_063.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_063.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_063.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_063.png")
            self.logger.error(f"TC_notes_063 got exception as: {ex} ")
            print(ex)

    def on_create_note_Enter_a_text_on_BUILD_textbox(self):
        try:
            self.logger.info("*******Tc_064***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            build_on_create_note = self.d.find_element(By.XPATH, notes_Read_Ini().build_on_createnote())
            build_on_create_note.send_keys(notes_Read_Ini().Enter_a_test_in_build())
            if build_on_create_note.text == "":
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_064.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_064.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_064.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_064.png")
            self.logger.error(f"TC_notes_064 got exception as: {ex} ")
            print(ex)

    def verify_BODY_MARKINGS_textbox_is_visible_on_create_note(self):
        try:
            self.logger.info("*****TC_065***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            body_markings = self.d.find_element(By.XPATH, notes_Read_Ini().body_markings_textbox())
            if body_markings.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_070.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_070.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_070.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_070.png")
            self.logger.error(f"TC_notes_070 got exception as: {ex} ")
            print(ex)

    def on_create_note_enter_a_text_on_BODY_MARKINGS_textbox(self):
        try:
            self.logger.info("*******TC_066****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            body_markings = self.d.find_element(By.XPATH, notes_Read_Ini().body_markings_textbox())
            body_markings.send_keys(notes_Read_Ini().Enter_a_text_on_bodymarkings())
            print(body_markings.text)
            if body_markings.text == "":
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_066.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_066.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_066.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_066.png")
            self.logger.error(f"TC_notes_066 got exception as: {ex} ")
            print(ex)

    def verify_GENDER_drop_down_is_displayed_on_create_note_panel(self):
        try:
            self.logger.info("*******TC_067******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            gender_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().gender_dropdown())
            if gender_dropdown.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_067.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_067.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_067.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_067.png")
            self.logger.error(f"TC_notes_067 got exception as: {ex} ")
            print(ex)

    def on_create_note_panel_verify_and_select_a_options_on_GENDER_drop_down_option_is_selected(self):
        try:
            self.logger.info("*******TC_068******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            gender_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().gender_dropdown())
            gender_dropdown.click()
            time.sleep(web_driver.one_second)
            female_option_in_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().female_in_genderdropdown())
            female_option_in_dropdown.click()
            print(female_option_in_dropdown.text)
            time.sleep(web_driver.one_second)
            if female_option_in_dropdown.text.lower() == notes_Read_Ini().female_text_in_gender_dropdown().lower():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_068.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_068.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_068.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_068.png")
            self.logger.error(f"TC_notes_068 got exception as: {ex} ")
            print(ex)

    def verify_HEIGHT_drop_down_is_displayed_on_create_note(self):
        try:
            self.logger.info("******TC_069****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.one_second)
            Height_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().Height_dropdown())
            if Height_dropdown.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_069.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_069.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_069.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_069.png")
            self.logger.error(f"TC_notes_069 got exception as: {ex} ")
            print(ex)

    def on_create_note_panel_select_a_element_on_HEIGHT_drop_down_verify_option_is_selected(self):
        try:
            self.logger.info("*******TC_070****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.one_second)
            Height_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().Height_dropdown())
            Height_dropdown.click()
            time.sleep(web_driver.one_second)
            Height_dropdown_options = self.d.find_element(By.XPATH, notes_Read_Ini().Height_dropdown_options())
            Height_dropdown_options.click()
            print(Height_dropdown_options.text)
            time.sleep(web_driver.one_second)
            if Height_dropdown_options.text == notes_Read_Ini().Height_dropdown_text():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_070.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_070.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_070.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_070.png")
            self.logger.error(f"TC_notes_070 got exception as: {ex} ")
            print(ex)

    def verify_NARRATIVES_text_box_is_visible_on_create_note(self):
        try:
            self.logger.info("******TC_071****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.one_second)
            narratives_textbox = self.d.find_element(By.XPATH, notes_Read_Ini().Narratives_textbox())
            if narratives_textbox.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_071.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_071.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_071.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_071.png")
            self.logger.error(f"TC_notes_071 got exception as: {ex} ")
            print(ex)

    def on_create_notes_panel_enter_a_text_on_NARRATIVES_textbox(self):
        try:
            self.logger.info("******TC_072***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.one_second)
            narratives_textbox = self.d.find_element(By.XPATH, notes_Read_Ini().Narratives_textbox())
            narratives_textbox.send_keys(notes_Read_Ini().enter_text_in_narratives_textbox())
            time.sleep(web_driver.one_second)
            print(narratives_textbox.text)
            if narratives_textbox.text != "":
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_072.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_072.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_072.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_072.png")
            self.logger.error(f"TC_notes_072 got exception as: {ex} ")
            print(ex)

    def verify_action_textbox_is_visible_in_create_note(self):
        try:
            self.logger.info("********TC_073****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.one_second)
            action_textbox = self.d.find_element(By.XPATH, notes_Read_Ini().action_textbox())
            if action_textbox.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_073.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_073.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_073.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_073.png")
            self.logger.error(f"TC_notes_073 got exception as: {ex} ")
            print(ex)

    def on_create_note_panel_Enter_a_text_in_action_textbox(self):
        try:
            self.logger.info("********TC_074***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.one_second)
            action_textbox = self.d.find_element(By.XPATH, notes_Read_Ini().action_textbox())
            action_textbox.send_keys(notes_Read_Ini().entering_text_in_action_textbox())
            print(action_textbox.text)
            if action_textbox.text == "":
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_074.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_074.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_074.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_074.png")
            self.logger.error(f"TC_notes_074 got exception as: {ex} ")
            print(ex)

    def verify_ADD_LOCATION_button_is_visible_on_create_note(self):
        try:
            self.logger.info("******TC_075****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.one_second)
            add_location_button = self.d.find_element(By.XPATH, notes_Read_Ini().add_location_button())
            if add_location_button.is_displayed():
                self.logger.info("add location button is visible")
                self.status.append(True)
            else:
                self.logger.info("add location button is visible ")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_075.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_075.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_075.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_075.png")
            self.logger.error(f"TC_notes_075 got exception as: {ex} ")
            print(ex)

    def click_on_ADD_LOCATION_on_create_note_notes_location_page_is_visible_followed_by_click_on_any_location_facefirst_logo_is_displayed(
            self):
        try:
            self.logger.info("*******TC_76******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

                # action = ActionChains(self.d)
                # action.move_by_offset(50, 71).pause(2).perform()
                # action.click()

            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            time.sleep(web_driver.one_second)
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.one_second)
            add_location_button = self.d.find_element(By.XPATH, notes_Read_Ini().add_location_button())
            add_location_button.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_location())
            move_cursur_to_map = self.d.find_element(By.XPATH, notes_Read_Ini().moving_mouse_into_map())
            action = ActionChains(self.d).move_to_element_with_offset(move_cursur_to_map, 50, 70).click().perform()
            time.sleep(web_driver.two_second)
            facefirst_logo_visible_on_location = self.d.find_element(By.XPATH,
                                                                     notes_Read_Ini().facefirst_logo_on_map())
            if facefirst_logo_visible_on_location.is_displayed():
                self.logger.info("facefirst logo is visible on map for a selected location")
                self.status.append(True)
            else:
                self.logger.info("facefirst logo is not visible on map for a selected location")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_076.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_076.png")
                return False
            else:
                return True
                # action.move_by_offset(50, 71).pause(2).perform()
                # action.click()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_076.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_076.png")
            self.logger.error(f"TC_notes_076 got exception as: {ex} ")
            print(ex)

    def verify_user_able_create_a_note(self):
        try:
            self.logger.info("*********TC_082********** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_notes_is_displayed(), self.d)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_heading_of_notes_page(), self.d)
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.three_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.three_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.two_second)
            print("reached to img box")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\images\\img1.png"
            self.d.find_element(By.ID, "image0").send_keys(file_image_path)
            time.sleep(web_driver.two_second)
            add_image_heading = self.d.find_element(By.XPATH, notes_Read_Ini().add_note_image_panel_heading())
            time.sleep(web_driver.three_second)
            skip_cropping = self.d.find_element(By.XPATH, notes_Read_Ini().skip_cropping_button_in_add_image())
            skip_cropping.click()
            time.sleep(web_driver.two_second)
            select_image = self.d.find_element(By.XPATH, notes_Read_Ini().select_image_button())
            select_image.click()
            time.sleep(web_driver.three_second)

            Location_store_textbox_in_createnote = self.d.find_element(By.XPATH,
                                                                       notes_Read_Ini().Location_store_textbox_on_create_note())
            Location_store_textbox_in_createnote.clear()
            Location_store_textbox_in_createnote.send_keys(
                notes_Read_Ini().Enter_text_in_Location_store_in_create_note())
            time.sleep(web_driver.one_second)
            case_subject_in_createnote = self.d.find_element(By.XPATH,
                                                             notes_Read_Ini().case_subject_textbox_in_create_note())
            case_subject_in_createnote.clear()
            case_subject_in_createnote.send_keys(notes_Read_Ini().Enter_text_in_case_subject_in_create_note())
            time.sleep(web_driver.one_second)
            reported_loss = self.d.find_element(By.XPATH, notes_Read_Ini().reported_loss_in_create_note())
            reported_loss.clear()
            reported_loss.send_keys(notes_Read_Ini().Enter_reported_loss())
            time.sleep(web_driver.one_second)
            build_on_create_note = self.d.find_element(By.XPATH, notes_Read_Ini().build_on_createnote())
            build_on_create_note.send_keys(notes_Read_Ini().Enter_a_test_in_build())
            time.sleep(web_driver.one_second)
            body_markings = self.d.find_element(By.XPATH, notes_Read_Ini().body_markings_textbox())
            body_markings.send_keys(notes_Read_Ini().Enter_a_text_on_bodymarkings())
            time.sleep(web_driver.one_second)
            gender_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().gender_dropdown())
            gender_dropdown.click()
            time.sleep(web_driver.one_second)
            female_option_in_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().female_in_genderdropdown())
            female_option_in_dropdown.click()
            time.sleep(web_driver.one_second)
            Height_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().Height_dropdown())
            Height_dropdown.click()
            time.sleep(web_driver.one_second)
            Height_dropdown_options = self.d.find_element(By.XPATH, notes_Read_Ini().Height_dropdown_options())
            Height_dropdown_options.click()
            time.sleep(web_driver.one_second)
            narratives_textbox = self.d.find_element(By.XPATH, notes_Read_Ini().Narratives_textbox())
            narratives_textbox.send_keys(notes_Read_Ini().enter_text_in_narratives_textbox())
            time.sleep(web_driver.one_second)
            action_textbox = self.d.find_element(By.XPATH, notes_Read_Ini().action_textbox())
            action_textbox.send_keys(notes_Read_Ini().entering_text_in_action_textbox())
            time.sleep(web_driver.one_second)
            add_location_button = self.d.find_element(By.XPATH, notes_Read_Ini().add_location_button())
            add_location_button.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_location())
            move_cursur_to_map = self.d.find_element(By.XPATH, notes_Read_Ini().moving_mouse_into_map())
            action = ActionChains(self.d).move_to_element_with_offset(move_cursur_to_map, 50, 70).click().perform()
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, notes_Read_Ini().save_button_in_createnote())
            save_button.click()
            time.sleep(web_driver.one_second)
            notes_panel_heading = self.d.find_element(By.XPATH,notes_Read_Ini().get_heading_of_notes_page())
            if notes_panel_heading.is_displayed():
                self.logger.info("notes_details are visible")
                self.status.append(True)
            else:
                self.logger.info("notes details are not visible")
                self.status.append(False)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status is {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_076.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_076.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_076.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_076.png")
            self.logger.error(f"TC_notes_076 got exception as: {ex} ")
            print(ex)

    def verify_save_button_is_visible_on_create_note(self):
        try:
            self.logger.info("*******TC_077******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, notes_Read_Ini().save_button_in_createnote())
            if save_button.is_displayed():
                self.logger.info("save button is visible")
                self.status.append(True)
            else:
                self.logger.info("save button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_077.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_077.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_077.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_077.png")
            self.logger.error(f"TC_notes_077 got exception as: {ex} ")
            print(ex)

    def on_create_note_panel_click_on_save_button(self):
        try:
            self.logger.info("********TC_078******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.one_second)
            add_location_button = self.d.find_element(By.XPATH, notes_Read_Ini().add_location_button())
            add_location_button.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_location())
            move_cursur_to_map = self.d.find_element(By.XPATH, notes_Read_Ini().moving_mouse_into_map())
            action = ActionChains(self.d).move_to_element_with_offset(move_cursur_to_map, 50, 70).click().perform()
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, notes_Read_Ini().save_button_in_createnote())
            save_button.click()
            time.sleep(web_driver.one_second)
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            if len(heading_notes) > 0:
                self.logger.info("if number of pages greater than 0 after clicking save button")
                self.status.append(True)
            else:
                self.logger.info("if number of pages less than 0 notes is closed")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_078.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_078.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_078.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_078.png")
            self.logger.error(f"TC_notes_078 got exception as: {ex} ")
            print(ex)

    def verify_cancel_button_is_visible_on_create_note(self):
        try:
            self.logger.info("******TC_079******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)

            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.one_second)
            cancel_button = self.d.find_element(By.XPATH, notes_Read_Ini().cancel_button_in_createnote())
            if cancel_button.is_displayed():
                self.logger.info("cancel button is visible")
                self.status.append(True)
            else:
                self.logger.info("cancel button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_079.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_079.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_079.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_079.png")
            self.logger.error(f"TC_notes_079 got exception as: {ex} ")
            print(ex)

    def click_on_cancel_button_in_createnote_panel(self):
        try:
            self.logger.info("******TC_080****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
            create_note.click()
            time.sleep(web_driver.one_second)
            cancel_button = self.d.find_element(By.XPATH, notes_Read_Ini().cancel_button_in_createnote())
            cancel_button.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            if len(heading_notes) > 0:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_080.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_080.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_080.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_080.png")
            self.logger.error(f"TC_notes_080 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_verify_refresh_in_action_dropdown(self):
        try:
            self.logger.info("*******TC_082******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.one_second)
            refresh = self.d.find_element(By.XPATH, notes_Read_Ini().refresh_in_action_dropdown())
            if refresh.is_displayed():
                self.logger.info("refresh option is visible in action dropdown")
                self.status.append(True)
            else:
                self.logger.info("refresh option is not visible in action dropdown")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_082.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_082.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_082.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_082.png")
            self.logger.error(f"TC_notes_082 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_click_on_refresh_on_Action_Drop_down_the_page_gets_refreshed(self):
        try:
            self.logger.info("********TC_083 started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            refresh = self.d.find_element(By.XPATH, notes_Read_Ini().refresh_in_action_dropdown())
            refresh.click()
            time.sleep(web_driver.two_second)
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            if len(heading_notes) > 0:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_083.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_083.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_083.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_083.png")
            self.logger.error(f"TC_notes_083 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_verify_Delete_selected_notes_is_visible_on_Action_drop_down(self):
        try:
            self.logger.info("**********TC_084********* satrted")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            delete_selected_notes = self.d.find_element(By.XPATH, notes_Read_Ini().delete_selected_notes())
            if delete_selected_notes.is_displayed():
                self.logger.info("delete selected note is visible on action dropdown")
                self.status.append(True)
            else:
                self.logger.info("delete selected note is not visible on action dropdown")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_084.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_084.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_084.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_084.png")
            self.logger.error(f"TC_notes_084 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_click_on_Delete_selected_notes_an_alert_window_is_displayed_click_ok_on_alert(self):
        try:
            self.logger.info("*******TC_085******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            delete_selected_notes = self.d.find_element(By.XPATH, notes_Read_Ini().delete_selected_notes())
            delete_selected_notes.click()
            time.sleep(web_driver.two_second)
            a = self.d.switch_to.alert
            a.accept()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            if len(heading_notes) > 0:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_085.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_085.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_085.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_085.png")
            self.logger.error(f"TC_notes_085 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_For_deleting_notes_select_check_box(self):
        try:
            self.logger.info("*******TC_086****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.two_second)
            checkbox = self.d.find_element(By.XPATH, notes_Read_Ini().delete_notes_checkbox())
            checkbox.click()
            if checkbox.is_enabled():
                self.logger.info("checkbox is enabled showing tick mark")
                self.status.append(True)
            else:
                self.logger.info("checkbox is not enabled tickmark is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            login().login_to_cloud_if_not_done(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_086.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_086.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_086.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_086.png")
            self.logger.error(f"TC_notes_086 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_selecting_a_checkbox_and_click_on_delete_selected_notes_a_WARNING_message_window_is_displayed(self):
        try:
            self.logger.info("*********TC_087*****started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, notes_Read_Ini().delete_notes_checkbox())
            self.d.execute_script("arguments[0].click();", checkbox)
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            delete_selected_notes = self.d.find_element(By.XPATH, notes_Read_Ini().delete_selected_notes())
            delete_selected_notes.click()
            time.sleep(web_driver.one_second)
            no_of_selected_notes_text = self.d.find_element(By.XPATH,notes_Read_Ini().gives_no_for_deleting_notes_text())
            print(no_of_selected_notes_text.text)
            if no_of_selected_notes_text.text == notes_Read_Ini().text_present_in_deleted_notes():
                self.logger.info("gives number for selected deleting notes")
                self.status.append(True)
            else:
                self.logger.info("not showing number for deleting selected deleting notes")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            # yes_delete_selected_button = self.d.find_element(By.XPATH,
            #                                                  notes_Read_Ini().yes_delete_selected_notes_button())
            # yes_delete_selected_button.click()
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_087.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_087.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_087.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_087.png")
            self.logger.error(f"TC_notes_087 got exception as: {ex} ")
            print(ex)

    def verify_user_able_to_delete_a_notes_from_notes_panel(self):
        try:
            self.logger.info("********TC_107***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            notes = self.explicit_wait(10, "XPATH", notes_Read_Ini().get_notes_is_displayed(), self.d)
            notes.click()
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_heading_of_notes_page(), self.d)
            checkbox = self.d.find_element(By.XPATH, notes_Read_Ini().delete_notes_checkbox())
            checkbox.click()
            time.sleep(web_driver.three_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            delete_selected_notes = self.d.find_element(By.XPATH, notes_Read_Ini().delete_selected_notes())
            delete_selected_notes.click()
            time.sleep(web_driver.three_second)
            no_of_selected_notes_text = self.d.find_element(By.XPATH, notes_Read_Ini().gives_no_for_deleting_notes_text())
            print(no_of_selected_notes_text.text)
            if no_of_selected_notes_text.text == notes_Read_Ini().text_present_in_deleted_notes():
                self.logger.info("gives number for selected deleting notes")
                self.status.append(True)
            else:
                self.logger.info("not showing number for deleting selected deleting notes")
                self.status.append(False)
                time.sleep(web_driver.one_second)
            yes_delete_selected_button = self.d.find_element(By.XPATH,
                                                                 notes_Read_Ini().yes_delete_selected_notes_button())
            yes_delete_selected_button.click()
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_107.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_107.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_107.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_107.png")
            self.logger.error(f"TC_notes_107 got exception as: {ex} ")
            print(ex)

    def click_on_select_All_check_box_followed_by_Delete_Selected_notes_in_warning_window_click_on_yes_delete_selected_button_notes_is_deleted(
            self):
        try:
            self.logger.info("********TC_089********* started")
            self.load_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            time.sleep(web_driver.two_second)
            select_all_checkbox = self.d.find_element(By.XPATH,
                                                      notes_Read_Ini().select_all_checkboxes_for_deleting_notes())
            select_all_checkbox.click()
            time.sleep(web_driver.two_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            delete_selected_notes = self.d.find_element(By.XPATH, notes_Read_Ini().delete_selected_notes())
            delete_selected_notes.click()
            time.sleep(web_driver.one_second)
            yes_delete_selected_button = self.d.find_element(By.XPATH,notes_Read_Ini().yes_delete_selected_notes_button())
            #yes_delete_selected_button.click()
            time.sleep(web_driver.one_second)
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            if len(heading_notes) > 0:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_089.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_089.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_089.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_089.png")
            self.logger.error(f"TC_notes_089 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_click_on_NO_cancel_button_on_warning_window_notes_is_not_deleted(self):
        try:
            self.logger.info("*******TC_089******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            time.sleep(web_driver.two_second)
            select_all_checkbox = self.d.find_element(By.XPATH,
                                                      notes_Read_Ini().select_all_checkboxes_for_deleting_notes())
            select_all_checkbox.click()
            time.sleep(web_driver.two_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            delete_selected_notes = self.d.find_element(By.XPATH, notes_Read_Ini().delete_selected_notes())
            delete_selected_notes.click()
            time.sleep(web_driver.one_second)
            cancel_button_in_deleting_notes = self.d.find_element(By.XPATH,
                                                                  notes_Read_Ini().no_cancel_button_in_deleting_notes())
            cancel_button_in_deleting_notes.click()
            time.sleep(web_driver.one_second)
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            if len(heading_notes) > 0:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_089.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_089.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_089.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_089.png")
            self.logger.error(f"TC_notes_089 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_change_panel_refresh_rate_is_visible_in_Action_dropdown(self):
        try:
            self.logger.info("*******TC_090******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.one_second)
            change_panel_refresh = self.d.find_element(By.XPATH, notes_Read_Ini().change_panel_refresh())
            if change_panel_refresh.is_displayed():
                self.logger.info("change refresh panel is visible in action dropdown")
                self.status.append(True)

            else:
                self.logger.info("change refresh panel is not visible in action dropdown")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_090.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_090.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_090.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_090.png")
            self.logger.error(f"TC_notes_090 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_click_on_change_panel_refresh_rate_change_panel_refresh_rate_window_is_opened(self):
        try:
            self.logger.info("*******TC_091******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            change_panel_refresh = self.d.find_element(By.XPATH, notes_Read_Ini().change_panel_refresh())
            change_panel_refresh.click()
            time.sleep(web_driver.two_second)
            change_panel_refresh_text = self.d.find_element(By.XPATH, notes_Read_Ini().change_refresh_panel_text())
            if change_panel_refresh_text.is_displayed():
                self.logger.info("change refresh panel text is visible")
                self.status.append(True)
            else:
                self.logger.info("change refresh panel text is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_091.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_091.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_091.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_091.png")
            self.logger.error(f"TC_notes_091 got exception as: {ex} ")
            print(ex)

    def click_on_change_refresh_option_inside_action_dropdown_and_verify_Auto_refresh_off_drop_down_is_visible(self):
        try:
            self.logger.info("********TC_092********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.one_second)
            change_panel_refresh = self.d.find_element(By.XPATH, notes_Read_Ini().change_panel_refresh())
            change_panel_refresh.click()
            time.sleep(web_driver.two_second)
            auto_refresh_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().auto_refresh_dropdown())
            if auto_refresh_dropdown.is_displayed():
                self.logger.info("auto refresh dropdown is visible")
                self.status.append(True)
            else:
                self.logger.info("auto refresh dropdown is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_092.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_092.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_092.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_092.png")
            self.logger.error(f"TC_notes_092 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_click_on_change_refresh_rate_panel_select_a_optioninside_Auto_refresh_off_drop_down_option_is_selected_and_displayed_on_Action_dropdown(
            self):
        try:
            self.logger.info("********TC_093******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            change_panel_refresh = self.d.find_element(By.XPATH, notes_Read_Ini().change_panel_refresh())
            change_panel_refresh.click()
            time.sleep(web_driver.two_second)
            auto_refresh_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().auto_refresh_dropdown())
            auto_refresh_option = self.d.find_element(By.XPATH, notes_Read_Ini().auto_refresh_option())
            print(auto_refresh_option.text)
            auto_refresh_option.click()
            time.sleep(web_driver.one_second)
            print(auto_refresh_option.get_attribute('label'))
            if auto_refresh_option.get_attribute('label') == notes_Read_Ini().auto_refresh_text():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_093.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_093.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_093.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_093.png")
            self.logger.error(f"TC_notes_093 got exception as: {ex} ")
            print(ex)

    def verify_cancel_button_is_visible_in_change_refresh_rate_window(self):
        try:
            self.logger.info("********TC_094******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.one_second)
            change_panel_refresh = self.d.find_element(By.XPATH, notes_Read_Ini().change_panel_refresh())
            change_panel_refresh.click()
            time.sleep(web_driver.one_second)
            cancel_button = self.d.find_element(By.XPATH,
                                                notes_Read_Ini().cancel_button_in_change_refresh_dropdown())
            if cancel_button.is_displayed():
                self.logger.info("cancel button is visible")
                self.status.append(True)
            else:
                self.logger.info("cancel button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
               self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_094.png")
               self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_094.png")
               return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_094.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_094.png")
            self.logger.error(f"TC_notes_094 got exception as: {ex} ")
            print(ex)

    def click_on_cancel_button_in_change_refresh_rate_window(self):
        try:
            self.logger.info("*********TC_95****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.two_second)
            Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
            Action_dropdown.click()
            time.sleep(web_driver.two_second)
            change_panel_refresh = self.d.find_element(By.XPATH, notes_Read_Ini().change_panel_refresh())
            change_panel_refresh.click()
            time.sleep(web_driver.two_second)
            cancel_button = self.d.find_element(By.XPATH,
                                                notes_Read_Ini().cancel_button_in_change_refresh_dropdown())
            cancel_button.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            if len(heading_notes) > 0:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_095.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_095.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_095.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_095.png")
            self.logger.error(f"TC_notes_095 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_verify_view_dropdown_is_visible(self):
        try:
            self.logger.info("*********TC_96********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.two_second)
            view_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().view_dropdown())
            if view_dropdown.is_displayed():
                self.logger.info("view dropdown is visible")
                self.status.append(True)
            else:
                self.logger.info("view dropdown is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_100.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_100.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_100.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_100.png")
            self.logger.error(f"TC_notes_100 got exception as: {ex} ")
            print(ex)

    def click_on_locations_inside_view_dropdown_notes_location_is_visible(self):
        try:
            self.logger.info("*********TC_97******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.three_second)
            view_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.two_second)
            location_in_view_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().location_in_view_dropdown())
            location_in_view_dropdown.click()
            time.sleep(web_driver.two_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            check_box = self.d.find_element(By.XPATH, notes_Read_Ini().delete_notes_checkbox())
            check_box.click()
            time.sleep(web_driver.three_second)
            view_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.two_second)
            location_in_view_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().location_in_view_dropdown())
            location_in_view_dropdown.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_location())
            if heading_notes_location.is_displayed():
                self.logger.info("notes-location panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("notes-location panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_97.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_97.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_97png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_97.png")
            self.logger.error(f"TC_notes_97 got exception as: {ex} ")
            print(ex)

    def verify_location_symbol_is_visible_on_notes_panel(self):
        try:
            self.logger.info("********TC_93******started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.three_second)
            location_symbol = self.d.find_element(By.XPATH, notes_Read_Ini().location_symbol())
            if location_symbol.is_displayed():
                self.logger.info("location symbol is visible")
                self.status.append(True)
            else:
                self.logger.info("location symbol is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_93.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_93.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_93.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_93.png")
            self.logger.error(f"TC_notes_93 got exception as: {ex} ")
            print(ex)

    def verify_user_able_to_view_created_notes(self):
        try:
            self.logger.info("********TC_94******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            location_symbol = self.d.find_element(By.XPATH, notes_Read_Ini().location_symbol())
            location_symbol.click()
            time.sleep(web_driver.two_second)
            heading_notes_location = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_location())
            if heading_notes_location.is_displayed():
                self.logger.info("notes-location panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("notes-location panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)

            self.logger.info(f"status:{self.status}")
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_94.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_94.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_94.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_94.png")
            self.logger.error(f"TC_notes_94 got exception as: {ex} ")
            print(ex)

    def verify_notes_details_symbol_is_visible_on_notes_panel(self):
        try:
            self.logger.info("*******TC_100******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            notes_view_details_symbol = self.d.find_element(By.XPATH, notes_Read_Ini().view_details_button())
            if notes_view_details_symbol.is_displayed():
                self.logger.info("notes-details symbol is visible")
                self.status.append(True)
            else:
                self.logger.info("notes-details symbol is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_100.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_100.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_100.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_100.png")
            self.logger.error(f"TC_notes_100 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_click_on_view_details_symbol_notes_details_are_visible(self):
        try:
            self.logger.info("********TC_101******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.three_second)
            view_details = self.d.find_element(By.XPATH, notes_Read_Ini().view_details_button())
            view_details.click()
            time.sleep(web_driver.two_second)
            notes_viewdetails_heading = self.d.find_element(By.XPATH, notes_Read_Ini().notes_details_heading())
            if notes_viewdetails_heading.is_displayed():
                self.logger.info("notes-view details panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("notes-view details details panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_101.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_101.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_101.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_101.png")
            self.logger.error(f"TC_notes_101 got exception as: {ex} ")
            print(ex)

    def verify_three_horizantal_lines_button_is_visible_in_notes_panel(self):
        try:
            self.logger.info("*******TC_102******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.three_second)
            tribar = self.d.find_element(By.XPATH, notes_Read_Ini().tribar_in_notes())
            if tribar.is_displayed():
                self.logger.info("tribar is visible")
                self.status.append(True)
            else:
                self.logger.info("tribar is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_102.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_102.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_102.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_102.png")
            self.logger.error(f"TC_notes_102 got exception as: {ex} ")
            print(ex)

    def click_on_three_horizantal_lines_button_and_verify_image_and_enrollments_buttons_are_visible(self):
        try:
            self.logger.info("*******TC_103****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.append(True)
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.three_second)
            # tribar = self.d.find_element(By.XPATH, notes_Read_Ini().tribar_in_notes())
            tribar = self.d.find_element(By.XPATH, notes_Read_Ini().tribar_in_notes())
            tribar.click()
            image_button = self.d.find_element(By.XPATH, notes_Read_Ini().images_button())
            enrollment_button = self.d.find_element(By.XPATH, notes_Read_Ini().enrollment_button())
            if image_button.is_displayed():
                self.logger.info("image-button is displayed")
                self.status.append(True)
            else:
                self.logger.info("image button is not dispalyed")
                self.status.append(False)
            if enrollment_button.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_103.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_103.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_103.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_103.png")
            self.logger.error(f"TC_notes_103 got exception as: {ex} ")
            print(ex)

    def click_on_enrollment_button_on_three_horizantal_lines_button_enrollments_groups_are_visible_if_not_alert_is_displayed(self):
        try:
            self.logger.info("********TC_104***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            tribar = self.d.find_element(By.XPATH, notes_Read_Ini().tribar_in_notes())
            tribar.click()
            time.sleep(web_driver.one_second)
            enrollment_button = self.d.find_element(By.XPATH, notes_Read_Ini().enrollment_button())
            enrollment_button.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            heading_notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            if heading_notes.is_displayed():
                self.logger.info("notes heading panel is visible")
                self.status.append(True)
            else:
                self.logger.info("notes heading panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_104.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_104.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_104.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_104.png")
            self.logger.error(f"TC_notes_104 got exception as: {ex} ")
            print(ex)

    def on_notes_panel_click_on_three_horizantal_lines_button_followed_by_images_button_notes_image_is_visible(self):
        try:
            self.logger.info("********TC_105******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()

            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.one_second)
            tribar = self.d.find_element(By.XPATH, notes_Read_Ini().tribar_in_notes())
            tribar = self.d.find_element(By.XPATH, notes_Read_Ini().tribar_in_notes())
            tribar.click()
            time.sleep(web_driver.one_second)
            image_button = self.d.find_element(By.XPATH, notes_Read_Ini().images_button())
            image_button.click()
            time.sleep(web_driver.one_second)
            notes_image_heading = self.d.find_element(By.XPATH, notes_Read_Ini().image_heading())
            if notes_image_heading.is_displayed():
                self.logger.info("notes-image panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("notes-image panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_105.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_109.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_105.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_105.png")
            self.logger.error(f"TC_notes_105 got exception as: {ex} ")
            print(ex)

    def close_notes_panel(self):
        try:
            self.logger.info("******TC_106****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            notes = self.explicit_wait(10, "XPATH", notes_Read_Ini().get_notes_is_displayed(), self.d)
            notes.click()
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.three_second)
            close_panel = self.d.find_element(By.XPATH, notes_Read_Ini().close_notes_panel())
            close_panel.click()
            time.sleep(web_driver.two_second)
            cloud_login_menu_after_login = self.d.find_element(By.XPATH,
                                                               notes_Read_Ini().get_afterlogin_cloud_menu_is_visible())
            if cloud_login_menu_after_login.is_displayed():
                self.logger.info("after closing notes  cloud menu is visible")
                self.status.append(True)
            else:
                self.logger.info("notes page is not closed properly")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_106.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_106.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_106.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_106.png")
            self.logger.error(f"TC_notes_110 got exception as: {ex} ")
            print(ex)

    def close_panels_one_by_one(self):
        try:
            close_panel = self.d.find_elements(By.XPATH,notes_Read_Ini().close_panels_one_by_one())
            for c in close_panel:
                c.click()
        except Exception as ex:
            print(ex)

    def click_on_Edit_note_on_notes_details_panel_and_verify_notes_is_edited(self):
        try:
            self.logger.info("**********TC_88******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_notes_is_displayed(), self.d)
            notes = self.d.find_element(By.XPATH, notes_Read_Ini().get_notes_is_displayed())
            notes.click()
            self.explicit_wait(10, "XPATH", notes_Read_Ini().get_heading_of_notes_page(), self.d)
            heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            time.sleep(web_driver.three_second)
            self.explicit_wait(10, "XPATH", notes_Read_Ini().view_details_button(), self.d)
            view_details = self.d.find_element(By.XPATH, notes_Read_Ini().view_details_button())
            view_details.click()
            self.explicit_wait(10, "XPATH", notes_Read_Ini().action_dropdown_in_notes_details_panel(), self.d)
            # time.sleep(web_driver.three_second)
            action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().action_dropdown_in_notes_details_panel())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            edit_notes = self.d.find_element(By.XPATH, notes_Read_Ini().Edit_note_option())
            edit_notes.click()
            time.sleep(web_driver.one_second)
            Height_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().Height_dropdown())
            Height_dropdown.click()
            time.sleep(web_driver.three_second)
            Height_dropdown_options = self.d.find_element(By.XPATH, notes_Read_Ini().Height_dropdown_options())
            Height_dropdown_options.click()
            time.sleep(web_driver.three_second)
            save_button = self.d.find_element(By.XPATH, notes_Read_Ini().save_button_on_notes_details())
            save_button.click()
            time.sleep(web_driver.one_second)

            notes_panel_heading = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
            if notes_panel_heading.is_displayed():
                self.logger.info("notes_details are visible")
                self.status.append(True)
            else:
                self.logger.info("notes details are not visible")
                self.status.append(False)
            self.close_panels_one_by_one()
            logout().logout_from_core(self.d)
            self.logger.info(f"status is {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_88.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_88.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_107.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_107.png")
            self.logger.error(f"TC_notes_106 got exception as: {ex} ")

    def create_notes(self):
        self.explicit_wait(10, "XPATH", notes_Read_Ini().get_heading_of_notes_page(), self.d)
        heading_notes = self.d.find_elements(By.XPATH, notes_Read_Ini().get_heading_of_notes_page())
        time.sleep(web_driver.three_second)
        Action_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().get_Action_dropdown_on_notes_page())
        Action_dropdown.click()
        time.sleep(web_driver.three_second)
        create_note = self.d.find_element(By.XPATH, notes_Read_Ini().get_create_note_on_action_dropdown())
        create_note.click()
        time.sleep(web_driver.two_second)
        print("reached to img box")
        file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\images\\img1.png"
        self.d.find_element(By.ID, "image0").send_keys(file_image_path)
        time.sleep(web_driver.two_second)
        add_image_heading = self.d.find_element(By.XPATH, notes_Read_Ini().add_note_image_panel_heading())
        time.sleep(web_driver.three_second)
        skip_cropping = self.d.find_element(By.XPATH, notes_Read_Ini().skip_cropping_button_in_add_image())
        skip_cropping.click()
        time.sleep(web_driver.two_second)
        select_image = self.d.find_element(By.XPATH, notes_Read_Ini().select_image_button())
        select_image.click()
        time.sleep(web_driver.three_second)

        Location_store_textbox_in_createnote = self.d.find_element(By.XPATH,
                                                                   notes_Read_Ini().Location_store_textbox_on_create_note())
        Location_store_textbox_in_createnote.clear()
        Location_store_textbox_in_createnote.send_keys(
            notes_Read_Ini().Enter_text_in_Location_store_in_create_note())
        time.sleep(web_driver.one_second)
        case_subject_in_createnote = self.d.find_element(By.XPATH,
                                                         notes_Read_Ini().case_subject_textbox_in_create_note())
        case_subject_in_createnote.clear()
        case_subject_in_createnote.send_keys(notes_Read_Ini().Enter_text_in_case_subject_in_create_note())
        time.sleep(web_driver.one_second)
        reported_loss = self.d.find_element(By.XPATH, notes_Read_Ini().reported_loss_in_create_note())
        reported_loss.clear()
        reported_loss.send_keys(notes_Read_Ini().Enter_reported_loss())
        time.sleep(web_driver.one_second)
        build_on_create_note = self.d.find_element(By.XPATH, notes_Read_Ini().build_on_createnote())
        build_on_create_note.send_keys(notes_Read_Ini().Enter_a_test_in_build())
        time.sleep(web_driver.one_second)
        body_markings = self.d.find_element(By.XPATH, notes_Read_Ini().body_markings_textbox())
        body_markings.send_keys(notes_Read_Ini().Enter_a_text_on_bodymarkings())
        time.sleep(web_driver.one_second)
        gender_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().gender_dropdown())
        gender_dropdown.click()
        time.sleep(web_driver.one_second)
        female_option_in_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().female_in_genderdropdown())
        female_option_in_dropdown.click()
        time.sleep(web_driver.one_second)
        Height_dropdown = self.d.find_element(By.XPATH, notes_Read_Ini().Height_dropdown())
        Height_dropdown.click()
        time.sleep(web_driver.one_second)
        Height_dropdown_options = self.d.find_element(By.XPATH, notes_Read_Ini().Height_dropdown_options())
        Height_dropdown_options.click()
        time.sleep(web_driver.one_second)
        narratives_textbox = self.d.find_element(By.XPATH, notes_Read_Ini().Narratives_textbox())
        narratives_textbox.send_keys(notes_Read_Ini().enter_text_in_narratives_textbox())
        time.sleep(web_driver.one_second)
        action_textbox = self.d.find_element(By.XPATH, notes_Read_Ini().action_textbox())
        action_textbox.send_keys(notes_Read_Ini().entering_text_in_action_textbox())
        time.sleep(web_driver.one_second)
        add_location_button = self.d.find_element(By.XPATH, notes_Read_Ini().add_location_button())
        add_location_button.click()
        time.sleep(web_driver.two_second)
        heading_notes_location = self.d.find_element(By.XPATH, notes_Read_Ini().get_heading_of_notes_location())
        move_cursur_to_map = self.d.find_element(By.XPATH, notes_Read_Ini().moving_mouse_into_map())
        action = ActionChains(self.d).move_to_element_with_offset(move_cursur_to_map, 50, 70).click().perform()
        time.sleep(web_driver.two_second)
        save_button = self.d.find_element(By.XPATH, notes_Read_Ini().save_button_in_createnote())
        save_button.click()




'''
    def Enter_username_password_click_on_cloud_Login(self):
        try:
            time.sleep(web_driver.two_second)
            username = self.d.find_element(By.XPATH, notes_Read_Ini().get_username_textbox())
            username.clear()
            username.send_keys(notes_Read_Ini().get_valid_username())
            time.sleep(web_driver.one_second)
            password = self.d.find_element(By.XPATH, notes_Read_Ini().get_password_textbox())
            password.clear()
            password.send_keys(notes_Read_Ini().get_valid_password())
            time.sleep(web_driver.one_second)
            cloud_login = self.d.find_element(By.XPATH, notes_Read_Ini().get_cloudmenu_textbox())
            cloud_login.click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            print(ex)'''


# notes_pom().verify_tribar_in_notes()
# notes_pom().click_on_ADD_LOCATION_on_create_note_notes_location_page_is_visible_followed_by_click_on_any_location_facefirst_logo_is_displayed()
