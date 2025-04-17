import time
from pathlib import Path
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from All_Config_Packages._10_Events_Config_Files.Events_Read_Ini import events_Read_Ini
from All_Config_Packages._9_tags_module_Config_Files.Tags_Read_INI import Read_Tags_Components
from Base_Package.Login_Logout_Ops import login
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


class events_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []
    # def __init__(self):
    #     self.d = web_driver.d()
    #     self.logger = web_logger.logger_obj()
    #     self.status = []

    def add_details_panel_cancel(self):
        self.logger.info("cancel btn on add details panel")
        cancle_btn = self.d.find_element(By.XPATH, events_Read_Ini().cancle_btn_on_add_details_panel_by_xpath())
        if cancle_btn.is_displayed():
            cancle_btn.click()
            time.sleep(web_driver.one_second)
        else:
            pass

        time.sleep(web_driver.one_second)

        cancle_on_warning = self.d.find_element(By.XPATH, events_Read_Ini().cancel_button_in_warning_add_details())
        if cancle_on_warning.is_displayed():
            cancle_on_warning.click()
            time.sleep(web_driver.one_second)
        else:
            pass

        time.sleep(web_driver.one_second)

    def verify_load_more_btn(self):
        try:
            self.logger.info("verifying load more btn")
            displaying_number_of_events_text = self.d.find_element(By.XPATH, events_Read_Ini().total_number_of_events_happened_out_of_total_number_of_events())
            self.logger.info(f"events text displayed: {displaying_number_of_events_text.text}")
            load_more_list = self.d.find_elements(By.XPATH, events_Read_Ini().loadmore_button())
            load_more_btn = 0

            if len(load_more_list) > 0:
                load_more_btn = load_more_list[0].is_displayed()
            else:
                load_more_btn = False
            print(f"displaying: {displaying_number_of_events_text.text}")
            text_displayed = displaying_number_of_events_text.text
            text_list = text_displayed.split(' ')
            self.logger.info(f"text list: {text_list}")
            num = []
            if len(text_list) > 0:
                for x in text_list:
                    if x.isdigit():
                        num.append(int(x))
                        self.logger.info(f"x: {x}")
                    else:
                        pass
            self.logger.info(f"num: {num}")
            displayed_events = 0
            total_events = 0
            if len(num) > 0:
                displayed_events = num[0]
                total_events = num[1]
            self.logger.info(f"events displayed: {displayed_events}")
            self.logger.info(f"total events: {total_events}")
            if total_events > 0:
                if total_events > 20 and load_more_btn == True:
                    return True
                if total_events < 20 and load_more_btn == False:
                    return True
                else:
                    return False
            else:
                print("No events displayed")
                return True

        except Exception as ex:
            print(f"Load More btn exception: {ex.args}")

    def Launching_login_page(self):
        try:
            self.logger.info(f"*****TC_001***** started")
            login().login_to_cloud_if_not_done(self.d)
            # self.d.get(events_Read_Ini().get_Launching_url())
            expected_url = events_Read_Ini().get_Launching_url()
            time.sleep(web_driver.one_second)
            # self.d.maximize_window()
            actual_url = self.d.current_url
            print(f"actual: {actual_url}, \nexpected: {expected_url}")
            if expected_url == actual_url:
                self.status.append(True)
            else:
                self.status.append(False)

            actual_title = self.d.title
            print("actual is", actual_title)
            expected_title = events_Read_Ini().get_expecting_title_webportal_login()
            print("expected title is", expected_title)
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            print(self.status)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_events_001.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_001.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_events_001.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\Tc_events_001.png")
            self.logger.error(f"Tc_events_001 got exception as: {ex}")

    def logo_username_texbox_password_textbox_is_visible(self):
        try:
            self.logger.info("*****TC_002***** started")
            login().login_to_cloud_if_not_done(self.d)
            # self.d.get(events_Read_Ini().get_Launching_url())
            self.status.clear()
            time.sleep(web_driver.three_second)
            # self.d.maximize_window()
            logo = self.d.find_element(By.XPATH, events_Read_Ini().get_logo_is_visible_on_login_page())
            username = self.d.find_element(By.XPATH, events_Read_Ini().get_username_textbox())
            # username.is_displayed()
            time.sleep(web_driver.one_second)
            password = self.d.find_element(By.XPATH, events_Read_Ini().get_password_textbox())
            # password.is_displayed()
            time.sleep(web_driver.one_second)
            if logo.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            print(self.status)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_events_002.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_002.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_002.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\Tc_events_002.png")
            self.logger.error(f"TC_events_002 got exception as: {ex} ")

    def load_login_page_if_not_loaded(self):
        try:
            self.d.get(events_Read_Ini().get_Launching_url())
            expected_url = events_Read_Ini().get_Launching_url()
            time.sleep(web_driver.one_second)
            self.d.maximize_window()
            time.sleep(web_driver.one_second)
            actual_url = self.d.current_url
            print(f"actual: {actual_url}, \nexpected: {expected_url}")
            if expected_url == actual_url:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.three_second)
            username = self.d.find_element(By.XPATH, events_Read_Ini().get_username_textbox())
            username.clear()
            time.sleep(web_driver.one_second)
            username.send_keys(events_Read_Ini().get_valid_username())
            time.sleep(web_driver.two_second)
            password = self.d.find_element(By.XPATH, events_Read_Ini().get_password_textbox())
            password.clear()
            time.sleep(web_driver.one_second)
            password.send_keys(events_Read_Ini().get_valid_password())
            time.sleep(web_driver.two_second)
            cloud_login = self.d.find_element(By.XPATH, events_Read_Ini().get_cloudlogin_button())
            cloud_login.click()
            time.sleep(web_driver.two_second)
        except Exception as ex:
            print(ex)

    def verify_on_cloud_menu_after_login(self):
        try:
            self.logger.info("*****TC_003_*****started")
            # # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            cloud_menu = self.d.find_element(By.XPATH, events_Read_Ini().get_cloud_menu())
            time.sleep(web_driver.one_second)
            if cloud_menu.is_displayed():
                self.logger.info(f"cloud menu is displayed after login, {cloud_menu}")
                self.status.append(True)
            else:
                self.logger.info(f"cloud menu is not displayed after login, {cloud_menu}")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_003.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_003.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_003.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_003.png")
            self.logger.error(f"TC_events_003 got exception as: {ex} ")

    def verify_Events_are_displayed_in_dashboard_items(self):
        try:
            self.logger.info("******TC_004******* started")
            login().login_to_cloud_if_not_done(self.d)
            # # self.load_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            if events.is_displayed():
                self.logger.info(f"events are visible in dashboard items:")
                self.status.append(True)
            else:
                self.logger.info(f"events  are not visible in dashboard items:")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_004.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_004.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_004.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_004.png")
            self.logger.error(f"TC_events_004 got exception as: {ex} ")

    def click_on_Events_and_verify_panel_heading_of_Events_is_visible(self):
        try:
            self.logger.info("******TC_005******** started")
            login().login_to_cloud_if_not_done(self.d)
            # # self.load_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.two_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            events_panel_heading = self.d.find_element(By.XPATH, events_Read_Ini().get_events_panel_heading())
            time.sleep(web_driver.one_second)
            if events_panel_heading.is_displayed():
                self.logger.info(" panel heading 'events' is visible")
                self.status.append(True)
            else:
                self.logger.info("panel heading 'events' is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            if False in self.status:

                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_005.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_005.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_005.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_005.png")
            self.logger.error(f"TC_events_005 got exception as: {ex} ")

    def verify_view_dropdown_is_visible(self):
        try:
            self.logger.info("********TC_006******* started")
            login().login_to_cloud_if_not_done(self.d)
            # # self.load_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            time.sleep(web_driver.one_second)
            if view_dropdown.is_displayed():
                self.logger.info("view dropdown is visible")
                self.status.append(True)
            else:
                self.logger.info("view dropdown is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_006.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_006.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_006.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_006.png")
            self.logger.error(f"TC_events_006 got exception as: {ex} ")

    def on_Events_panel_heading_verify_cross_symbol_is_visible(self):
        try:
            self.logger.info("********TC_007******** staerted")
            login().login_to_cloud_if_not_done(self.d)
            # # self.load_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            cross_symbol = self.d.find_element(By.XPATH, events_Read_Ini().event_page_cross_symbol())
            if cross_symbol.is_displayed():
                self.logger.info("cross symbol is visible ")
                self.status.append(True)
            else:
                self.logger.info("cross symbol is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_007.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_007.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_007.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_007.png")
            self.logger.error(f"TC_events_007 got exception as: {ex} ")

    def on_Events_page_verify_filter_search_results_textbox_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.logger.info("*******TC_008********* started")
            login().login_to_cloud_if_not_done(self.d)
            # # self.load_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.one_second)
            # events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            time.sleep(web_driver.one_second)
            search_filter_by_action_textbox = self.d.find_element(By.XPATH, events_Read_Ini().search_filter_by_action_textbox())
            time.sleep(web_driver.one_second)
            if search_filter_by_action_textbox.is_displayed():
                self.logger.info("search filter by action textbox is visible")
                self.status.append(True)
            else:
                self.logger.info("search filter by action textbox is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_008.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_008.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_008.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_008.png")
            self.logger.error(f"TC_events_008 got exception as: {ex} ")

    def on_Events_page_Enter_a_text_in_search_filter_by_action_textbox_and_verify_number_of_events_displayed(self):
        try:
            self.logger.info("*********TC_009****** started")
            # # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            search_filter_by_action_textbox = self.d.find_element(By.XPATH, events_Read_Ini().search_filter_by_action_textbox())
            search_filter_by_action_textbox.clear()
            time.sleep(web_driver.one_second)
            search_filter_by_action_textbox.send_keys(events_Read_Ini().Enter_a_action_text())
            time.sleep(web_driver.two_second)
            diplaying_text_actualtext = self.d.find_element(By.XPATH, events_Read_Ini().total_number_of_events_happened_out_of_total_number_of_events())
            print(diplaying_text_actualtext.text)
            time.sleep(web_driver.one_second)
            number_of_events_happened_text = self.d.find_element(By.XPATH, events_Read_Ini().get_number_of_text())
            print(number_of_events_happened_text.text)
            if diplaying_text_actualtext.is_displayed():
                self.logger.info("displayed number of events of mentioned action")
                self.status.append(True)
            else:
                self.logger.info(" number of events of mention action is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_009.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_009.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_009.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_009.png")
            self.logger.error(f"TC_events_009 got exception as: {ex} ")

    def On_Events_page_after_entering_action_verify_remove_filter_button_is_visible(self):
        try:
            self.logger.info("*********TC_010****** started")
            # # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            search_filter_by_action_textbox = self.d.find_element(By.XPATH, events_Read_Ini().search_filter_by_action_textbox())
            search_filter_by_action_textbox.clear()
            time.sleep(web_driver.one_second)
            search_filter_by_action_textbox.send_keys(events_Read_Ini().Enter_a_action_text())
            time.sleep(web_driver.two_second)
            remove_filter = self.d.find_element(By.XPATH, events_Read_Ini().remove_filter_button())
            if remove_filter.is_displayed():
                self.logger.info("remove filter button is visible")
                self.status.append(True)
            else:
                self.logger.info("remove filter button is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_010.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_010.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_010.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_010.png")
            self.logger.error(f"TC_events_010 got exception as: {ex} ")

    def on_Events_page_verify_search_dropdown_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.logger.info("********TC_010******* started")
            # # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            # events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events = web_driver.explicit_wait(self,  10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_dropdown_in_events())
            if search_dropdown.is_displayed():
                self.logger.info("search dropdown is visible")
                self.status.append(True)
            else:
                self.logger.info("search dropdown is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_010.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_010.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_010.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_010.png")
            self.logger.error(f"TC_events_010 got exception as: {ex} ")

    def on_Events_page_verify_Action_dropdown_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.logger.info("********TC_O11**** started")
            # # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            action = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            if action.is_displayed():
                self.logger.info("action dropdown is visible")
                self.status.append(True)
            else:
                self.logger.info("action dropdown is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_011.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_011.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_011.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_011.png")
            self.logger.error(f"TC_events_011 got exception as: {ex} ")

    def on_Events_page_verify_SELECT_ALL_checkbox_is_visible_and_clickable_select_all_text_is_visible(self):
        try:
            self.logger.info("********TC_012******** started")
            # # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            time.sleep(web_driver.one_second)
            web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_events_panel_heading(), self.d)
            select_all_checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_all_checkbox())
            time.sleep(web_driver.one_second)
            select_all_text = self.d.find_element(By.XPATH, events_Read_Ini().select_all_text())
            if select_all_checkbox.is_displayed():
                self.logger.info("select_all_checkbox is visible")
                self.status.append(True)
            else:
                self.logger.info("select all checkbox is not visible")
                self.status.append(False)
            if select_all_text.is_displayed():
                self.logger.info("select all text is visible")
                self.status.append(True)
            else:
                self.logger.info("select all text is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_012.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_012.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_012.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_012.png")
            self.logger.error(f"TC_events_012 got exception as: {ex} ")

    def on_Events_page_verify_Event_real_time_is_visible(self):
        try:
            self.logger.info("*******TC_013********* started")
            # # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            event_happened_banner = self.d.find_element(By.XPATH, events_Read_Ini().real_time_event_happened())
            time.sleep(web_driver.one_second)
            if event_happened_banner.is_displayed():
                self.logger.info("time when an event happened is visible")
                self.status.append(True)
            else:
                self.logger.info("time when an event happened is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_013.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_013.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_013.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_013.png")
            self.logger.error(f"TC_events_013 got exception as: {ex} ")

    def on_Events_page_verify_location_store_along_with_case_subject_Index_score_Action_taken_region_this_event_info_is_visible(self):
        try:
            self.logger.info("*******TC_014********* started")
            # # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            location_subject = self.d.find_element(By.XPATH, events_Read_Ini().location_casesubject_of_an_event())
            time.sleep(web_driver.one_second)
            indexscore = self.d.find_element(By.XPATH, events_Read_Ini().indexscore_of_event())
            time.sleep(web_driver.one_second)
            action_taken = self.d.find_element(By.XPATH, events_Read_Ini().actiontaken_by_an_event())
            time.sleep(web_driver.one_second)
            region = self.d.find_element(By.XPATH, events_Read_Ini().region_ofan_event())
            if location_subject.is_displayed():
                self.logger.info("location/case/subject  of event is visible beside of an event ")
                self.status.append(True)
            else:
                self.logger.info("location/case/subject of an event is not visible beside of an event ")
                self.status.append(False)
            if indexscore.is_displayed():
                self.logger.info("indexscore of an event is visible beside an event")
                self.status.append(True)
            else:
                self.logger.info("index score of an event is not visible beside of an event")
                self.status.append(False)
            if action_taken.is_displayed():
                self.logger.info("action taken by an event is visible beside of an event")
                self.status.append(True)
            else:
                self.logger.info("action taken by an event is not visible beside of an event")
                self.status.append(False)
            if region.is_displayed():
                self.logger.info("region of an event is visible beside of an event")
                self.status.append(True)
            else:
                self.logger.info("region of an event is not visible beside of an event")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_014.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_014.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_014.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_014.png")
            self.logger.error(f"TC_events_014 got exception as: {ex} ")

    def on_Events_page_verify_Live_Image_text_and_Live_Image_is_visible(self):
        try:
            self.logger.info("********TC_015****** started")
            # # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            live_image = self.d.find_element(By.XPATH, events_Read_Ini().live_image())
            time.sleep(web_driver.two_second)
            live_image_text = self.d.find_element(By.XPATH, events_Read_Ini().live_image_text())
            time.sleep(web_driver.one_second)
            if live_image.is_displayed():
                self.logger.info("live  image is visible")
                self.status.append(True)
            else:
                self.logger.info("live image is not visible")
                self.status.append(False)
            if live_image_text.is_displayed():
                self.logger.info("live image text is visible")
                self.status.append(True)
            else:
                self.logger.info("live image text is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_015.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_015.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_015.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_015.png")
            self.logger.error(f"TC_events_015 got exception as: {ex} ")

    def on_Events_page_verify_File_Image_text_File_Image_is_visible(self):
        try:
            self.logger.info("********TC_016***** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            file_image_text = self.d.find_element(By.XPATH, events_Read_Ini().file_image_text())
            time.sleep(web_driver.one_second)
            file_image = self.d.find_element(By.XPATH, events_Read_Ini().file_image())
            time.sleep(web_driver.one_second)
            if file_image.is_displayed():
                self.logger.info("file image is visible")
                self.status.append(True)
            else:
                self.logger.info("file image is not visible")
                self.status.append(False)
            if file_image_text.is_displayed():
                self.logger.info("file image text is visible")
                self.status.append(True)
            else:
                self.logger.info("file image text is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_016.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_016.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_016.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_016.png")
            self.logger.error(f"TC_events_016 got exception as: {ex} ")

    def on_Events_page_verify_Event_button_is_visible_and_symbol_on_button_is_visible(self):
        try:
            self.logger.info("*******TC_017****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            events_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            time.sleep(web_driver.one_second)
            events_symbol = self.d.find_element(By.XPATH, events_Read_Ini().events_button_symbol())
            if events_button.is_displayed():
                self.logger.info("events button is visible")
                self.status.append(True)
            else:
                self.logger.info("evnts button is not visible")
                self.status.append(False)
            if events_symbol.is_displayed():
                self.logger.info("events_symbol is visible")
                self.status.append(True)
            else:
                self.logger.info("events_symbol is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_017.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_017.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_017.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_017.png")
            self.logger.error(f"TC_events_017 got exception as: {ex} ")

    def on_Events_page_verify_tag_button_is_visible_and_symbol_on_button_is_visible(self):
        try:
            self.logger.info("********TC_018***** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            tags_button = self.d.find_element(By.XPATH, events_Read_Ini().tags_button_in_eventspage())
            time.sleep(web_driver.one_second)
            tags_button_symbol = self.d.find_element(By.XPATH, events_Read_Ini().tags_button_symbol())
            time.sleep(web_driver.one_second)
            if tags_button.is_displayed():
                self.logger.info("tags button is visible")
                self.status.append(True)
            else:
                self.logger.info("tags button is not visible")
                self.status.append(False)
            if tags_button_symbol.is_displayed():
                self.logger.info("tags buttton symbol is visible")
                self.status.append(True)
            else:
                self.logger.info("tags button symbol is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_018.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_018.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_018.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_018.png")
            self.logger.error(f"TC_events_018 got exception as: {ex} ")

    def on_Events_page_verify_extent_menu_button_and_symbol_on_button_is_visible(self):
        try:
            self.logger.info("*******TC_019******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            extent_menu = self.d.find_element(By.XPATH, events_Read_Ini().extent_menu())
            time.sleep(web_driver.one_second)
            extent_menu_symbol = self.d.find_element(By.XPATH, events_Read_Ini().extent_menu_symbol())
            time.sleep(web_driver.one_second)
            if extent_menu.is_displayed():
                self.logger.info("extent menu is visible")
                self.status.append(True)
            else:
                self.logger.info("extent menu is not visible")
                self.status.append(False)
            if extent_menu_symbol.is_displayed():
                self.logger.info("extent_menu symbol is visible")
                self.status.append(True)
            else:
                self.logger.info("extent-menu symbol is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_019.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_019.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_019.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_019.png")
            self.logger.error(f"TC_events_019 got exception as: {ex} ")

    def on_Events_page_verify_Load_More_button_is_visible_and_clickable(self):
        try:
            self.logger.info("********TC_020****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_elements(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            if len(events) <= 0:
                self.d.refresh()
            events = events[0]
            events.click()
            time.sleep(web_driver.three_second)
            # load_more = self.d.find_element(By.XPATH, events_Read_Ini().loadmore_button())
            self.status.append(self.verify_load_more_btn())

            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_020.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_020.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_020.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_020.png")
            self.logger.error(f"TC_events_020 got exception as: {ex} ")

    def on_Events_page_verify_number_of_events_are_visible_below_Load_More_button(self):
        try:
            self.logger.info("****TC_021******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            displaying_number_of_events_text = self.d.find_element(By.XPATH, events_Read_Ini().total_number_of_events_happened_out_of_total_number_of_events())
            if displaying_number_of_events_text.is_displayed():
                self.logger.info("displaying number of events out of total number of events happened")
                self.status.append(True)
            else:
                self.logger.info("number of events displayed text is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_021.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_021.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_021.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_021.png")
            self.logger.error(f"TC_events_021 got exception as: {ex} ")

    def on_Events_page_click_on_load_more_button_and_verify_number_of_Events_count_is_40_displayed(self):
        try:
            self.logger.info("********TC_022******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_elements(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            if len(events) <= 0:
                self.d.refresh()

            events = self.explicit_wait(10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)

            self.logger.info("waiting for events")
            events.click()
            time.sleep(web_driver.three_second)

            # load_more_button = self.d.find_element(By.XPATH, events_Read_Ini().loadmore_button())
            # load_more_button = self.explicit_wait(10, "XPATH", events_Read_Ini().loadmore_button(), self.d)
            load_more_btn = self.verify_load_more_btn()
            time.sleep(web_driver.one_second)
            self.logger.info("waiting for load more.")
            if load_more_btn:
                load_more_list = self.d.find_elements(By.XPATH, events_Read_Ini().loadmore_button())
                # load_more_btn = 0
                if len(load_more_list) > 0:
                    load_more = load_more_list[0]
                    load_more.click()
                    time.sleep(web_driver.one_second)
                    displaying_text_list = self.d.find_elements(By.XPATH, events_Read_Ini().total_number_of_events_happened_out_of_total_number_of_events())
                    if len(displaying_text_list) > 0:
                        displaying_text = displaying_text_list[0].text
                        print(displaying_text)
                        time.sleep(web_driver.one_second)
                        no_of_events_text = self.d.find_element(By.XPATH, events_Read_Ini().get_number_of_text())
                        print(no_of_events_text.text)
                        self.logger.info(f"number of events: {no_of_events_text.text}")
                        if int(no_of_events_text.text) > 20:
                            self.logger.info("after clicking loadmore button next 20 is displayed")
                            self.status.append(True)
                        else:
                            self.logger.info("next 20 events i.e, 40 is not displayed")
                            self.status.append(False)
                        self.logger.info(f"status :{self.status}")
            else:
                self.logger.info("Load More Btn is not displayed.")
                self.status.append(True)
            # time.sleep(web_driver.one_second)

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_022.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_022.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_022.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_022.png")
            self.logger.error(f"TC_events_022 got exception as: {ex} ")

    def click_on_view_dropdown_and_verify_location_is_visible(self):
        try:
            self.logger.info("*******TC_024******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            all_options = self.d.find_elements(By.XPATH, events_Read_Ini().view_dropdown_options())
            for option in all_options:
                if option.is_displayed():
                    self.logger.info(f" {option.text} Option in VIEW dropdown is visible...")
                    self.status.append(True)
                else:
                    self.status.append(False)

            # location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            # if location_in_viewdropdown.is_displayed():
            #     self.logger.info("location is visible in view dropdown")
            #     self.status.append(True)
            # else:
            #     self.logger.info("location is not visible in view dropdown")
            #     self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_024.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_024.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_024.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_024.png")
            self.logger.error(f"TC_events_024 got exception as: {ex} ")

    def In_view_dropdown_click_on_location_an_alert_is_opened_click_ok_an_alert_select_a_event_and_verify_panel_heading_of_Events_location_is_visible(self):
        try:
            self.logger.info("*******TC_025****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            events_location_panel = self.d.find_element(By.XPATH, events_Read_Ini().events_location_panel())
            time.sleep(web_driver.one_second)
            if events_location_panel.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_025.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_025.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_025.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_025.png")
            self.logger.error(f"TC_events_025 got exception as: {ex} ")

    def on_Events_location_page_verify_Find_textbox_is_visible(self):
        try:
            self.logger.info("********TC_026******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            textbox = self.d.find_element(By.XPATH, events_Read_Ini().get_find_location_textbox_in_notes_location())
            if textbox.is_displayed():
                self.logger.info("textbox is visible")
                self.status.append(True)
            else:
                self.logger.info("textbox is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_026.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_026.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_026.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_026.png")
            self.logger.error(f"TC_events_026 got exception as: {ex} ")

    def on_Events_location_page_on_map_facefirst_logo_is_visible_click_on_logo_event_is_visible(self):
        try:
            self.logger.info("*******TC_027****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            facefirstlogo = self.d.find_element(By.XPATH, events_Read_Ini().facefirst_logo_on_map())
            facefirstlogo.click()
            time.sleep(web_driver.one_second)
            live_image_onmap = self.d.find_element(By.XPATH, events_Read_Ini().live_image_on_map())
            time.sleep(web_driver.one_second)
            file_image_onmap = self.d.find_element(By.XPATH, events_Read_Ini().file_image_on_map())
            if live_image_onmap.is_displayed():

                self.logger.info("live image is visible")
                self.status.append(True)
            else:
                self.logger.info("live image  is not visible")
                self.status.append(False)
            if file_image_onmap.is_displayed():
                self.logger.info("file image is visible")
                self.status.append(True)
            else:
                self.logger.info("file image is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_027.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_027.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_027.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_027.png")
            self.logger.error(f"TC_events_027 got exception as: {ex} ")

    def on_Events_location_page_verify_Draw_circle_button_is_visible(self):
        try:
            self.logger.info("*********TC_028********* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            draw_circle = self.d.find_element(By.XPATH, events_Read_Ini().get_drawcircle_button())
            if draw_circle.is_displayed():
                self.logger.info("draw circle button is visible")
                self.status.append(True)
            else:
                self.logger.info("draw circle button is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_028.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_028.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_028.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_028.png")
            self.logger.error(f"TC_events_028 got exception as: {ex} ")

    def on_Events_Location_page_verify_serach_area_button_is_visible(self):
        try:
            self.logger.info("******TC_029**** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            search_area = self.d.find_element(By.XPATH, events_Read_Ini().get_search_area_button_on_notes_location())
            if search_area.is_displayed():
                self.logger.info("search area button is visible")
                self.status.append(True)
            else:
                self.logger.info("search area button is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_029.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_029.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_029.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_029.png")
            self.logger.error(f"TC_events_029 got exception as: {ex} ")

    def on_Events_location_page_verify_extent_menu_is_visible(self):
        try:
            self.logger.info("******TC_030 ******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            extent_menu = self.d.find_element(By.XPATH, events_Read_Ini().get_tribar_on_map())
            if extent_menu.is_displayed():
                self.logger.info("extent menu is visible")
                self.status.append(True)
            else:
                self.logger.info("extent menu is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_030.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_030.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_030.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_030.png")
            self.logger.error(f"TC_events_030 got exception as: {ex} ")

    def on_Events_location_page_click_on_extent_menu_verify_search_target_window_dialouge_box_is_displayed(self):
        try:
            self.logger.info("******TC_031***** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            extent_menu = self.d.find_element(By.XPATH, events_Read_Ini().get_tribar_on_map())
            extent_menu.click()
            time.sleep(web_driver.one_second)
            search_target_dialougebox = self.d.find_element(By.XPATH, events_Read_Ini().get_linktext_searchtarget_on_map())
            if search_target_dialougebox.is_displayed():
                self.logger.info("search target dialouge box is visible")
                self.status.append(True)
            else:
                self.logger.info("search target dialouge box is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_031.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_031.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_031.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_031.png")
            self.logger.error(f"TC_events_031 got exception as: {ex} ")

    def on_Events_location_page_in_select_a_search_target_dialouge_box_a_dropdown_is_visible_and_clickable(self):
        try:
            self.logger.info("**********TC_032 ******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            extent_menu = self.d.find_element(By.XPATH, events_Read_Ini().get_tribar_on_map())
            extent_menu.click()
            time.sleep(web_driver.one_second)
            search_target_dropdow = self.d.find_element(By.XPATH, events_Read_Ini().get_search_target_dropdown())
            if search_target_dropdow.is_displayed():
                self.logger.info("search target dropdown is visible")
                self.status.append(True)
            else:
                self.logger.info("search target dropdown is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_032.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_032.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_032.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_032.png")
            self.logger.error(f"TC_events_032 got exception as: {ex} ")

    def on_Events_location_page_In_select_a_search_target_dropdown_click_on_NOTES_option_Notes_location_page_is_visible(self):
        try:
            self.logger.info("******TC_033******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            extent_menu = self.d.find_element(By.XPATH, events_Read_Ini().get_tribar_on_map())
            extent_menu.click()
            time.sleep(web_driver.one_second)
            sel = Select(self.d.find_element(By.XPATH, events_Read_Ini().get_search_target_dropdown()))
            sel.select_by_visible_text("Notes")
            self.logger.info("eventsis selected in search target dropdown")
            time.sleep(web_driver.two_second)
            Notes_location = self.d.find_element(By.XPATH, events_Read_Ini().get_location_panel_headings())
            if Notes_location.is_displayed():
                self.logger.info("eventsloaction panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("eventslocation panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_033.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_033.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_033.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_033.png")
            self.logger.error(f"TC_events_033 got exception as: {ex} ")
            print(ex)

    def on_Events_location_page_In_select_a_search_target_dropdown_click_on_Events_option_Events_location_page_is_visible(self):
        try:
            self.logger.info("********TC_034********* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            time.sleep(web_driver.one_second)
            web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_events_panel_heading(), self.d)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                                .location_in_view_dropdown(), self.d)
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                                .location_in_view_dropdown(), self.d)
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            extent_menu = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_tribar_on_map(), self.d)
            extent_menu.click()
            time.sleep(web_driver.one_second)
            sel = Select(self.d.find_element(By.XPATH, events_Read_Ini().get_search_target_dropdown()))
            sel.select_by_visible_text("Probable Match Events")
            self.logger.info("selecting events in search target window")
            time.sleep(web_driver.two_second)
            Event_location = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                      .get_location_panel_headings(), self.d)
            if Event_location.is_displayed():
                self.logger.info("notes-events location panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("notes-events location panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_034.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_034.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_034.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_034.png")
            self.logger.error(f"TC_events_034 got exception as: {ex} ")
            print(ex)

    def on_Events_location_page_In_select_a_search_target_dialouge_box_verify_cancel_button_is_visible_and_clickable(self):
        try:
            self.logger.info("*******TC_035******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            self.logger.info("events panel opened.")
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            self.logger.info("view dropdown clicked.")
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            self.logger.info("location option clicked.")
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            self.logger.info("checkbox selected.")
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            extent_menu = self.d.find_element(By.XPATH, events_Read_Ini().get_tribar_on_map())
            extent_menu.click()
            self.logger.info("extent menu clicked.")
            time.sleep(web_driver.one_second)
            cancel_button = self.d.find_element(By.XPATH, events_Read_Ini().get_cancel_button())
            if cancel_button.is_displayed():
                self.logger.info("cancel button is visible")
                self.status.append(True)
            else:
                self.logger.info("cancel button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_035.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_035.png")
                self.logger.info("returning false.")
                return False
            else:
                self.logger.info("returning true.")
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_035.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_035.png")
            self.logger.error(f"TC_events_035 got exception as: {ex} ")
            print(ex)

    def on_Events_location_page_In_select_search_target_dropdown_click_on_cancel_button_verify_Events_location_panel_heading_is_visible(self):
        try:
            self.logger.info("*******TC_036****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            self.logger.info("events panel opened.")
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            self.logger.info("view dropdown clicked.")
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            self.logger.info("location option selected.")
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            self.logger.info("checkbox is clicked.")
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            self.logger.info("location option selected.")
            time.sleep(web_driver.one_second)
            extent_menu = self.d.find_element(By.XPATH, events_Read_Ini().get_tribar_on_map())
            extent_menu.click()
            self.logger.info("extent btn is clicked.")
            time.sleep(web_driver.one_second)
            cancel_button = self.d.find_element(By.XPATH, events_Read_Ini().get_cancel_button())
            cancel_button.click()
            self.logger.info("cancle btn clicked.")
            Event_location = self.d.find_element(By.XPATH, events_Read_Ini().get_location_panel_headings())
            self.logger.info(f"events location displayed: {Event_location.is_displayed()}")
            if Event_location.is_displayed():
                self.logger.info("notes-events location panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("notes-events location panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_036.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_036.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_notes_036.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_notes_036.png")
            self.logger.error(f"TC_notes_036 got exception as: {ex} ")
            print(ex)

    def on_Events_location_page_Click_on_full_screen_toggle_symbol_full_screen_is_displayed(self):
        try:
            self.logger.info("*****TC_037********* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            toggle_symbol = self.d.find_element(By.XPATH, events_Read_Ini().get_toggle_full_screen_view())
            toggle_symbol.click()
            time.sleep(web_driver.one_second)
            after_clicking_fullscreen_toggle = self.d.find_element(By.XPATH, events_Read_Ini().get_after_clicking_fullscreen_view())
            if after_clicking_fullscreen_toggle.is_displayed():
                self.logger.info("full screen toggle symbol is visible")
                self.status.append(True)
            else:
                self.logger.info("full screen toggle symbol is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            after_clicking_fullscreen_toggle.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_037.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_037.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_eventss_037.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_eventss_037.png")
            self.logger.error(f"TC_events_037 got exception as: {ex} ")
            print(ex)

    def on_Events_location_page_Click_on_ESC_button_from_keyboard_Full_Screen_view_to_minimize_full_screen_view(self):
        try:
            self.logger.info("******TC_038***** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.explicit_wait(10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.explicit_wait(10, "XPATH", events_Read_Ini().view_dropdown(), self.d)
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.explicit_wait(10, "XPATH", events_Read_Ini().location_in_view_dropdown(), self.d)
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.two_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            toggle_symbol = self.explicit_wait(10, "XPATH", events_Read_Ini().get_toggle_full_screen_view(), self.d)
            toggle_symbol.click()
            time.sleep(web_driver.one_second)
            after_clicking_fullscreen_toggle = self.explicit_wait(10, "XPATH", events_Read_Ini().get_after_clicking_fullscreen_view(), self.d)
            time.sleep(web_driver.one_second)
            after_clicking_fullscreen_toggle.click()
            time.sleep(web_driver.one_second)
            # map = self.d.find_element(By.XPATH, events_Read_Ini().after_clicking_togglesymbol_map_xpath())
            # map.send_keys(Keys.ESCAPE)
            # time.sleep(web_driver.one_second)
            Event_location = self.d.find_element(By.XPATH, events_Read_Ini().get_location_panel_headings())
            if Event_location.is_displayed():
                self.logger.info("notes-events location panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("notes-events location panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_038.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_038.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_038.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_038.png")
            self.logger.error(f"TC_events_038 got exception as: {ex} ")
            print(ex)

    def on_Events_location_page_verify_and_click_on_plus_symbol_is_visible(self):
        try:
            self.logger.info("*****TC_039**** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            zoom_in_or_plussymbol = self.d.find_element(By.XPATH, events_Read_Ini().get_zoom_in_on_map())
            if zoom_in_or_plussymbol.is_displayed():
                self.logger.info("zoom in or plus symbol is visible")
                self.status.append(True)
            else:
                self.logger.info("zoom in or plus symbol is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_039.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_039.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_039.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_039.png")
            self.logger.error(f"TC_events_039 got exception as: {ex} ")

    def on_Events_location_page_verify_and_click_on_plus_symbol_on_Notes_location_page_map_performs_zoom_in(self):
        try:
            self.logger.info("**********TC_040******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            zoom_in_or_plussymbol = self.d.find_element(By.XPATH, events_Read_Ini().get_zoom_in_on_map())
            zoom_in_or_plussymbol.click()
            time.sleep(web_driver.one_second)
            zoom_in_or_plussymbol.click()
            time.sleep(web_driver.one_second)
            Event_location = self.d.find_element(By.XPATH, events_Read_Ini().get_location_panel_headings())
            if Event_location.is_displayed():
                self.logger.info("events location panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("events location panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_040.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_040.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_040.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_040.png")
            self.logger.error(f"TC_events_040 got exception as: {ex} ")

    def on_Events_location_page_verify_minus_symbol_is_visible(self):
        try:
            self.logger.info("*******TC_041****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            zoom_out_or_minussymbol = self.d.find_element(By.XPATH, events_Read_Ini().get_zoom_out_())
            if zoom_out_or_minussymbol.is_displayed():
                self.logger.info("minus symol is visible")
                self.status.append(True)
            else:
                self.logger.info("minus symbol is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:

                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_041.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_041.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_041.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_041.png")
            self.logger.error(f"TC_events_041 got exception as: {ex} ")

    def on_Events_location_page_verify_and_click_on_minus_symbol_on_Notes_location_page_map_performs_zoom_out(self):
        try:
            self.logger.info("******TC_042**** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.one_second)
            zoom_out_or_minussymbol = self.d.find_element(By.XPATH, events_Read_Ini().get_zoom_out_())
            zoom_out_or_minussymbol.click()
            zoom_out_or_minussymbol.click()
            Event_location = self.d.find_element(By.XPATH, events_Read_Ini().get_location_panel_headings())
            if Event_location.is_displayed():
                self.logger.info("events location panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("events location panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_042.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_042.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_042.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_042.png")
            self.logger.error(f"TC_events_042 got exception as: {ex} ")

    def on_Events_page_click_on_select_All_checkbox_click_on_location_in_view_dropdown_verify_number_of_events_on_that_location(self):
        try:
            self.logger.info("*******TC_043******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            select_all_checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_all_checkbox())
            select_all_checkbox.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            location_in_viewdropdown = self.d.find_element(By.XPATH, events_Read_Ini().location_in_view_dropdown())
            location_in_viewdropdown.click()
            time.sleep(web_driver.three_second)
            number_of_events_visible_on_map = self.d.find_element(By.XPATH, events_Read_Ini().on_map_number_of_events_visible())
            print(number_of_events_visible_on_map.text)
            if number_of_events_visible_on_map.is_displayed():
                self.logger.info("number of events visible on map ")
                self.status.append(True)
            else:
                self.logger.info("number events are not visible on map")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_043.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_043.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_043.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_043.png")
            self.logger.error(f"TC_events_043 got exception as: {ex} ")

    def on_Events_page_verify_in_view_dropdown_display_tags_option_is_visible(self):
        try:
            self.logger.info("*******TC_044******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            display_tags = self.d.find_element(By.XPATH, events_Read_Ini().display_tags_in_eventspage())
            if display_tags.is_displayed():
                self.logger.info("display tags option is visible in view dropdown ")
                self.status.append(True)
            else:
                self.logger.info("display tags option is not visible in view dropdown")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_044.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_044.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_044.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_044.png")
            self.logger.error(f"TC_events_044 got exception as: {ex} ")

    def on_Events_page_click_on_display_tags_and_verify_Tags_are_visible_inthe_formof_horizantal_line_below_the_events(self):
        try:
            self.logger.info("**********TC_045********* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().view_dropdown())
            view_dropdown.click()
            time.sleep(web_driver.one_second)
            display_tags = self.d.find_element(By.XPATH, events_Read_Ini().display_tags_in_eventspage())
            display_tags.click()
            time.sleep(web_driver.one_second)
            tags_display_belowline = self.d.find_element(By.XPATH, events_Read_Ini().tags_display_below_the_events())
            if tags_display_belowline.is_displayed():
                self.logger.info("tags are visible below the events")
                self.status.append(True)
            else:
                self.logger.info("tags are not visible below the events")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_045.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_045.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_045.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_045.png")
            self.logger.error(f"TC_events_04 got exception as: {ex} ")

    def on_Events_page_click_on_search_dropdown_and_verify_Date_time_range_is_visible_and_clickable(self):
        try:
            self.logger.info("*******TC_046******** startes")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_dropdown_in_events())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            date_time_range = self.d.find_element(By.XPATH, events_Read_Ini().date_and_time_range_in_searchdropdown())
            if date_time_range.is_displayed():
                self.logger.info("date and time range text box is visible in search dropdown")
                self.status.append(True)
            else:
                self.status.append("date and time text box is not visible in search dropdown")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_046.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_046.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_046.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_046.png")
            self.logger.error(f"TC_events_046 got exception as: {ex} ")

    def on_Events_page_click_on_search_dropdown_and_verify_Date_time_range_to_is_visible_and_clickable(self):
        try:
            self.logger.info("*******TC_047******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_dropdown_in_events())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            date_time_to = self.d.find_element(By.XPATH, events_Read_Ini().date_and_time_range_to_in_searchdropdown())
            if date_time_to.is_displayed():
                self.logger.info("date and time range to text box is visible")
                self.status.append(True)
            else:
                self.logger.info("date and time to textbox is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_047.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_047.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_047.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_047.png")
            self.logger.error(f"TC_events_047 got exception as: {ex} ")

    def on_Events_page_click_on_search_dropdown_and_verify_Enrollment_group_selection_button_is_visible_and_clickable(self):
        try:
            self.logger.info("*********TC_048******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_dropdown_in_events())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            enrollment_group_selection = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_group_selection())
            if enrollment_group_selection.is_displayed():
                self.logger.info("enrollment group selection button is visible")
                self.status.append(True)
            else:
                self.logger.info("enrollment group selection button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_048.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_048.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_048.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_048.png")
            self.logger.error(f"TC_events_048 got exception as: {ex} ")

    def on_Events_page_click_on_search_dropdown_and_verify_org_hierarchy_selection_button_is_visible_and_clickable(self):
        try:
            self.logger.info("*******TC_049****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_dropdown_in_events())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            org_hierarchy_selection = self.d.find_element(By.XPATH, events_Read_Ini().org_hierarchy_selection())
            if org_hierarchy_selection.is_displayed():
                self.logger.info("org_hierarchy selection is visible")
                self.status.append(True)
            else:
                self.logger.info("org_hierarchy selection is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_049.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_049.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_049.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_049.png")
            self.logger.error(f"TC_events_049 got exception as: {ex} ")

    def on_Events_page_click_on_search_dropdown_and_verify_tag_selection_button_is_visible_and_clickable(self):
        try:
            self.logger.info("********TC_050********* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_dropdown_in_events())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            tag_selection_button = self.d.find_element(By.XPATH, events_Read_Ini().tag_selection())
            if tag_selection_button.is_displayed():
                self.logger.info("tag selection button is visible in search dropdown")
                self.status.append(True)
            else:
                self.logger.info("tag selection button is not visible in search dropdown")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_050.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_050.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_050.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_050.png")
            self.logger.error(f"TC_events_050 got exception as: {ex} ")

    def on_Events_page_click_on_search_dropdown_and_verify_sort_by_dropdown_is_visible_and_clickable(self):
        try:
            self.logger.info("*********TC_051******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.one_second)
            search_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_dropdown_in_events())
            search_dropdown.click()
            time.sleep(web_driver.one_second)
            sort_by_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().sort_by_dropdown_in_searchdropdown())
            if sort_by_dropdown.is_displayed():
                self.logger.info("sort by dropdown is visible")
                self.status.append(True)
            else:
                self.logger.info("sort by dropdown is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_051.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_051.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_051.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_051.png")
            self.logger.error(f"TC_events_051 got exception as: {ex} ")

    def on_Events_page_click_on_search_dropdow_and_verify_sort_by_AtoZ_radio_button_is_visible_and_clickable(self):
        try:
            self.logger.info("******TC_052******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            search_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_dropdown_in_events())
            search_dropdown.click()
            time.sleep(web_driver.two_second)
            sort_by_atoz_radiobutton = self.d.find_element(By.XPATH, events_Read_Ini().sort_by_atoz_radiobutton())
            if sort_by_atoz_radiobutton.is_displayed():
                self.logger.info("sort by atoz radio button is visible")
                self.status.append(True)
            else:
                self.logger.info("sort by atoz radio button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_052.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_052.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_052.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_052.png")
            self.logger.error(f"TC_events_052 got exception as: {ex} ")

    def on_Events_page_click_on_search_dropdown_and_verify_sort_by_ZtoA_radio_button_is_visible_and_clickable(self):
        try:
            self.logger.info("******TC_053******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            search_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_dropdown_in_events())
            search_dropdown.click()
            time.sleep(web_driver.three_second)
            sort_by_ztoa_radiobutton = self.d.find_element(By.XPATH, events_Read_Ini().sort_by_ztoa_radiobutton())
            if sort_by_ztoa_radiobutton.is_displayed():
                self.logger.info("sort by ztoa radio button is visible")
                self.status.append(True)
            else:
                self.logger.info("sort by ztoa radio button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_053.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_053.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_053.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_053.png")
            self.logger.error(f"TC_events_053 got exception as: {ex} ")

    def on_Events_page_click_on_search_dropdown_verify_clear_button_is_visible_and_clickable(self):
        try:
            self.logger.info("********TC_54******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            search_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_dropdown_in_events())
            search_dropdown.click()
            time.sleep(web_driver.three_second)
            clear_button_in_searchdropdown = self.d.find_element(By.XPATH, events_Read_Ini().clear_button_in_searchdropdown())
            if clear_button_in_searchdropdown.is_displayed():
                self.logger.info("clear button is visible in search dropdown")
                self.status.append(True)
            else:
                self.logger.info("clear button is not visible in search dropdown")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_054.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_054.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_054.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_054.png")
            self.logger.error(f"TC_events_054 got exception as: {ex} ")

    def on_Events_page_click_on_search_dropdown_andverify_location_search_button_is_visible_and_clickable(self):
        try:
            self.logger.info("******TC_055******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            search_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_dropdown_in_events())
            search_dropdown.click()
            time.sleep(web_driver.two_second)
            location_search_button = self.d.find_element(By.XPATH, events_Read_Ini().location_search_button_in_searchdropdown())
            print(location_search_button.text)
            if location_search_button.is_displayed():
                self.logger.info("location search button is visible")
                self.status.append(True)
            else:
                self.logger.info("location search button is not visible in search dropdown")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_055.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_055.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_055.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_055.png")
            self.logger.error(f"TC_events_055 got exception as: {ex} ")

    def verify_an_event_search_with_not_selected_any_button_in_search_dropdown_click_on_search(self):
        try:
            self.logger.info("********TC_056******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            search_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_dropdown_in_events())
            search_dropdown.click()
            time.sleep(web_driver.two_second)
            search_button_in_searchdropdown = self.d.find_element(By.XPATH, events_Read_Ini().search_button_in_searchdropdown())
            if search_button_in_searchdropdown.is_displayed():
                self.logger.info("search button is visible in search dropdown")
                self.status.append(True)
            else:
                self.logger.info("search button is not visible in search dropdown")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_056.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_056.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_056.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_056.png")
            self.logger.error(f"TC_events_056 got exception as: {ex} ")

    def on_Events_page_click_on_Action_dropdown_and_verify_dropdown_options_are_visible(self):
        try:
            self.logger.info("*******TC_072******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            action_dropdown_options = self.d.find_elements(By.XPATH, events_Read_Ini().action_dropdown_options())
            for options in action_dropdown_options:
                if options.is_displayed():
                    self.logger.info(f"options are {options.text}")
                    self.status.append(True)
                else:
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_072.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_072.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_072.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_072.png")
            self.logger.error(f"TC_events_072 got exception as: {ex} ")

    def on_Events_page_click_on_Action_dropdown_followed_by_Edit_tags_not_selecting_an_event_verify_an_alert_is_visible(self):
        try:
            self.logger.info("********TC_073******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            if a:
                self.logger.info("alert is visible")
                self.status.append(True)
            else:
                self.logger.info("alert is not visible")
                self.status.append(False)
            var = a.text
            print(var)
            time.sleep(web_driver.one_second)
            a.accept()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_073.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_073.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_073.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_073.png")
            self.logger.error(f"TC_events_073 got exception as: {ex} ")

    def on_Events_page_In_Action_dropdown_click_on_Edit_tags_option_and_verify_Events_tags_panel_is_visible_and_verify_panel_heading(self):
        try:
            self.logger.info("******TC_074******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            events_tags_panel_heading = self.d.find_element(By.XPATH, events_Read_Ini().events_tags_panel_heading())
            if events_tags_panel_heading.is_displayed():
                self.logger.info("events_tags panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("events tags panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_074.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_074.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_074.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_074.png")
            self.logger.error(f"TC_events_074 got exception as: {ex} ")

    def on_Events_tags_panel_verify_filter_dropdown_is_visible_and_clickable(self):
        try:
            self.logger.info("*******TC_075****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            events_tags_panel_heading = self.d.find_element(By.XPATH, events_Read_Ini().events_tags_panel_heading())
            filter_dropown = self.d.find_element(By.XPATH, events_Read_Ini().filter_dropdown_in_events_tag())
            if filter_dropown.is_displayed():
                self.logger.info("filter dropdown is visible in events tag panel is visible")
                self.status.append(True)
            else:
                self.logger.info("filter dropdown in events tag panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_075.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_075.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_075.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_075.png")
            self.logger.error(f"TC_events_075 got exception as: {ex} ")

    def on_Events_tags_panel_click_on_filter_dropdown_and_verify_linked_tags_and_unlinked_tag_options_are_visible(self):
        try:
            self.logger.info("*******TC_076******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            events_tags_panel_heading = self.d.find_element(By.XPATH, events_Read_Ini().events_tags_panel_heading())
            filter_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().filter_dropdown_in_events_tag())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)
            filter_dropdown_options = self.d.find_elements(By.XPATH, events_Read_Ini().filter_dropdown_options())
            for options in filter_dropdown_options:
                if options.is_displayed():
                    self.logger.info(f"options are {options.text}")
                    self.status.append(True)
                else:
                    self.logger.info("filter dropdown options are not visible")
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_076.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_076.png")
                return True
            else:
                return False
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_076.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_076.png")
            self.logger.error(f"TC_events_076 got exception as: {ex} ")

    def on_Events_tags_panel_click_on_linked_tags_in_filter_dropdown_and_verify_only_linked_tags_are_disiplayed(self):
        try:
            self.logger.info("*******TC_077******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            events_tags_panel_heading = self.d.find_element(By.XPATH, events_Read_Ini().events_tags_panel_heading())
            # filter_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().filter_dropdown_in_events_tag())
            # filter_dropdown.click()
            # time.sleep(web_driver.one_second)
            # linked_tags_option_in_filterdropdown = self.d.find_element(By.XPATH, events_Read_Ini().linked_tags_by_xpath())
            # linked_tags_option_in_filterdropdown.click()
            time.sleep(web_driver.one_second)
            linked_tags_banner = self.d.find_element(By.XPATH, events_Read_Ini().tags_banner())
            linked_tags = self.d.find_elements(By.XPATH, events_Read_Ini().tags_names())
            if linked_tags_banner.is_displayed():
                for i in linked_tags:
                    if i.is_displayed():
                        self.logger.info(f"linked tags are {i.text}")
                        self.status.append(True)
                    else:
                        self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False != [True, True, True, True]:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_077.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_077.png")
                return True
            else:
                return False
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_077.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_077.png")
            self.logger.error(f"TC_events_077 got exception as: {ex} ")

    def on_Events_tags_panelclick_on_unlinked_tags_in_filter_dropdown_and_verify_only_unlinked_tags_banner_and_unlinked_tags_are_displayed(self):
        try:
            self.logger.info("*********TC_078******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            events_tags_panel_heading = self.d.find_element(By.XPATH, events_Read_Ini().events_tags_panel_heading())
            filter_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().filter_dropdown_in_events_tag())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)
            unlinked_tags = self.d.find_element(By.XPATH, events_Read_Ini().unlinked_tags_by_xpath())
            unlinked_tags.click()
            time.sleep(web_driver.one_second)
            unlinked_tags_banner = self.d.find_element(By.XPATH, events_Read_Ini().tags_banner())
            unlinked_tags_names = self.d.find_elements(By.XPATH, events_Read_Ini().tags_names())
            if unlinked_tags_banner.is_displayed():
                self.logger.info("unlinked tags banner is visible")
                self.status.append(True)
                for i in unlinked_tags_names:
                    if i.is_displayed():
                        self.logger.info(f"unlinked tags are {i.text}")
            else:
                self.logger.info("unlinked tags banner is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False != [True]:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_078.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_078.png")
                return True
            else:
                return False
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_078.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_078.png")
            self.logger.error(f"TC_events_078 got exception as: {ex} ")

    def on_Events_tags_panel_verify_filter_tag_name_text_box_is_visible(self):
        try:
            self.logger.info("*********TC_079******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            filter_tag_name_textbox = self.d.find_element(By.XPATH, events_Read_Ini().filter_tags_name_textbox())
            if filter_tag_name_textbox.is_displayed():
                self.logger.info("filter tag by name textbox is visible in events tag panel")
                self.status.append(True)
            else:
                self.logger.info("events tag by name textbox is not visible")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False != [True]:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_079.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_079.png")
                return True
            else:
                return False
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_079.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_079.png")
            self.logger.error(f"TC_events_079 got exception as: {ex} ")

    def on_Events_tags_panelEnter_a_tagname_in_filter_tag_name_text_and_verify_only_text_entered_tags_are_displayed(self):
        try:
            self.logger.info("******TC_080****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            filter_tag_name_textbox = self.d.find_element(By.XPATH, events_Read_Ini().filter_tags_name_textbox())
            filter_tag_name_textbox.clear()
            filter_tag_name_textbox.send_keys(events_Read_Ini().enter_a_text_in_filter_tagname_texbox())
            time.sleep(web_driver.one_second)
            filter_tag_banner = self.d.find_element(By.XPATH, events_Read_Ini().tags_banner())
            if filter_tag_name_textbox.is_displayed():
                self.logger.info(f"tagname:{filter_tag_banner.text} is displayed")
                self.status.append(True)
            else:
                self.logger.info(f"tagname:{filter_tag_banner.text} is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False != [True]:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_080.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_080.png")
                return True
            else:
                return False
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_080.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_080.png")
            self.logger.error(f"TC_events_080 got exception as: {ex} ")

    def on_Events_tags_verify_Details_button_is_visible_in_each_tag(self):
        try:
            self.logger.info("******TC_081***** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            time.sleep(web_driver.one_second)
            self.logger.info("events ta is visible")
            time.sleep(web_driver.one_second)
            web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_events_panel_heading(), self.d)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            self.logger.info("action dropdown clicked")
            edit_tags_option = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().edit_tags_in_actiondropdown(), self.d)
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            self.logger.info("edit tag edit tag pop")
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            self.logger.info("checkbox selected.")
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                        .edit_tags_in_actiondropdown(), self.d)
            edit_tags_option.click()
            self.logger.info(f"edit tags options visible: {edit_tags_option.is_displayed()}")
            time.sleep(web_driver.two_second)
            web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_match_event_tags_filter_dropdown(), self.d).click()
            self.logger.info("match event tag filter dropdown clicked.")
            time.sleep(web_driver.one_second)
            web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_match_event_tags_filter_unlink_tag(), self.d).click()
            self.logger.info("match event tags filter unlink tag clicked.")
            time.sleep(web_driver.one_second)
            # filter_tag_name_textbox = self.d.find_element(By.XPATH, events_Read_Ini().filter_tags_name_textbox())
            # filter_tag_name_textbox.clear()
            # filter_tag_name_textbox.send_keys(events_Read_Ini().enter_a_text_in_filter_tagname_texbox())
            # time.sleep(web_driver.one_second)
            filter_tag_banner = self.d.find_element(By.XPATH, events_Read_Ini().tags_banner())
            self.logger.info(f"filter tags banner visible: {filter_tag_banner.is_displayed()}")
            details_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().tag_details_button(), self.d)
            self.logger.info(f"tag details button visible: {details_button.is_displayed()}")
            if details_button.is_displayed():
                self.logger.info("tag details button is visible")
                self.status.append(True)
            else:
                self.logger.info("tag details button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False != [True]:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_081.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_081.png")
                return True
            else:
                return False
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_081.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_081.png")
            self.logger.error(f"TC_events_081 got exception as: {ex} ")

    def on_Events_tags_click_on_Details_button_and_verify_Tag_Details_panel_is_visible(self):
        try:
            self.logger.info("********TC_082******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            # filter_tag_name_textbox = self.d.find_element(By.XPATH, events_Read_Ini().filter_tags_name_textbox())
            # filter_tag_name_textbox.clear()
            # filter_tag_name_textbox.send_keys(events_Read_Ini().enter_a_text_in_filter_tagname_texbox())
            # time.sleep(web_driver.one_second)
            filter_tag_banner = self.d.find_element(By.XPATH, events_Read_Ini().tags_banner())
            self.d.find_element(By.XPATH, events_Read_Ini().get_match_event_tags_filter_dropdown()).click()
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_match_event_tags_filter_unlink_tag()).click()
            time.sleep(web_driver.two_second)
            details_button = self.d.find_element(By.XPATH, events_Read_Ini().tag_details_button())
            details_button.click()
            time.sleep(web_driver.one_second)
            Tag_details_panel = self.d.find_element(By.XPATH, events_Read_Ini().tag_details_panel_heading())


            # details_button = self.d.find_element(By.XPATH, events_Read_Ini().tag_details_button())
            # details_button.click()
            # time.sleep(web_driver.one_second)
            # Tag_details_panel = self.d.find_element(By.XPATH, events_Read_Ini().tag_details_panel_heading())
            if Tag_details_panel.is_displayed():
                self.logger.info("tag details panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("tag details panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False != [True]:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_082.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_082.png")
                return True
            else:
                return False
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_082.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_082.png")
            self.logger.error(f"TC_events_082 got exception as: {ex} ")

    def on_Events_tags_panel_verify_Action_dropdown_is_visible(self):
        try:
            self.logger.info("******TC_083********** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            filter_tag_name_textbox = self.d.find_element(By.XPATH, events_Read_Ini().filter_tags_name_textbox())
            filter_tag_name_textbox.clear()
            filter_tag_name_textbox.send_keys(events_Read_Ini().enter_a_text_in_filter_tagname_texbox())
            time.sleep(web_driver.one_second)
            action_dropdown_in_event_tag_panel = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events_tag())
            if action_dropdown_in_event_tag_panel.is_displayed():
                self.logger.info("action dropdown is visible in events tag panel")
                self.status.append(True)
            else:
                self.logger.info("action dropdown is not visible in events tag panel")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False != [True]:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_083.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_083.png")
                return True
            else:
                return False
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_083.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_083.png")
            self.logger.error(f"TC_events_083 got exception as: {ex} ")

    def on_Events_tags_panel_click_on_Action_dropdrown_followed_by_Addtags_to_events_without_selecting_checkbox_an_alert_is_visible_verify_text_and_ok_on_alert(self):
        try:
            self.logger.info("********TC_084********* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().first_checkbox_in_events())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            filter_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().filter_dropdown_in_events_tag())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)
            unlinked_tags = self.d.find_element(By.XPATH, events_Read_Ini().unlinked_tags_by_xpath())
            unlinked_tags.click()
            time.sleep(web_driver.two_second)
            action_dropdown_in_event_tag_panel = self.d.find_element(By.XPATH,
                                                                     events_Read_Ini().action_dropdown_in_events_tag())
            action_dropdown_in_event_tag_panel.click()
            time.sleep(web_driver.two_second)
            add_tags_to_event = self.d.find_element(By.XPATH, events_Read_Ini().add_tags_to_event_option_in_event_tags())
            add_tags_to_event.click()
            time.sleep(web_driver.two_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            var = a.text
            print(var)
            if a:
                self.logger.info("alert is visible")
                self.status.append(True)
            else:
                self.logger.info("alert is not visible")
                self.status.append(False)
            a.accept()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False != [True]:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_084.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_084.png")
                return True
            else:
                return False
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_084.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_084.png")
            self.logger.error(f"TC_events_084 got exception as: {ex} ")

    def on_Events_tags_panel_click_on_Action_dropdrown_followed_by_Addtags_to_events_selecting_a_checkbox_verify_tagname_is_visible_to_an_event(self):
        try:
            self.logger.info("********TC_085******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().first_checkbox_in_events())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            filter_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().filter_dropdown_in_events_tag())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)
            unlinked_tags = self.d.find_element(By.XPATH, events_Read_Ini().unlinked_tags_by_xpath())
            unlinked_tags.click()
            # time.sleep(web_driver.one_second)
            # a  = self.d.switch_to.alert
            # a.accept()
            time.sleep(web_driver.one_second)
            checkbox_twentyfour = self.d.find_element(By.XPATH, events_Read_Ini().checkbox_number_twentyfour())
            checkbox_twentyfour.click()
            time.sleep(web_driver.one_second)
            action_dropdown_in_eventstags = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events_tag())
            action_dropdown_in_eventstags.click()
            time.sleep(web_driver.one_second)
            add_tags =  self.d.find_element(By.XPATH, events_Read_Ini().add_tags_to_event_option_in_event_tags())
            add_tags.click()
            time.sleep(web_driver.two_second)
            tagnames = self.d.find_elements(By.XPATH, events_Read_Ini().tagnames_below_to_an_event())
            for op in tagnames:
                if op.is_displayed():
                    self.logger.info(f"tagnames are visible {op.text}")
                    self.status.append(True)
                else:
                    self.logger.info("tagnames are not visible")
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_085.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_085.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_085.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_085.png")
            self.logger.error(f"TC_events_085 got exception as: {ex} ")

    def on_Events_tags_panel_click_on_Action_dropdrown_followed_by_Remove_tags_to_events_not_selected_a_checkbox_an_alert_is_visible_verify_ok_and_text_on_an_alert(self):
        try:
            self.logger.info("*********TC_086******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            filter_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().filter_dropdown_in_events_tag())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)
            unlinked_tags = self.d.find_element(By.XPATH, events_Read_Ini().unlinked_tags_by_xpath())
            unlinked_tags.click()
            time.sleep(web_driver.one_second)
            action_dropdown_in_events_tag = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events_tag())
            action_dropdown_in_events_tag.click()
            time.sleep(web_driver.one_second)
            remove_tags = self.d.find_element(By.XPATH, events_Read_Ini().remove_tags_to_event_in_eventstag())
            remove_tags.click()
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            var = a.text
            print(var)
            if a:
                self.logger.info("alert is visible")
                self.status.append(True)
            else:
                self.logger.info("alert is not visible")
                self.status.append(False)
            a.accept()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_086.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_086.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_086.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_086.png")
            self.logger.error(f"TC_events_086 got exception as: {ex} ")

    def on_Events_tags_panel_click_on_Action_dropdrown_followed_by_Remove_tags_to_events_selecting_a_checkbox_an_alert_is_visible_verify_ok_and_text_on_an_alert(self):
        try:
            self.logger.info("********TC_087******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_events_panel_heading(), self.d)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().first_checkbox_in_events())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            edit_tags_option = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().edit_tags_in_actiondropdown(), self.d)
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_match_event_tags_filter_dropdown(), self.d).click()
            time.sleep(web_driver.one_second)
            web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_match_event_tags_filter_unlink_tag(), self.d).click()
            time.sleep(web_driver.one_second)
            details_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().tag_details_button(), self.d)
            filter_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().filter_dropdown_in_events_tag())
            filter_dropdown.click()
            time.sleep(web_driver.one_second)
            linked_tags = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().linked_tags_by_xpath(), self.d)
            linked_tags.click()
            time.sleep(web_driver.one_second)
            checkbox_twentyfour = self.d.find_element(By.XPATH, events_Read_Ini().checkbox_number_twentyfour())
            checkbox_twentyfour.click()
            time.sleep(web_driver.one_second)
            action_dropdown_in_events_tag = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events_tag())
            action_dropdown_in_events_tag.click()
            time.sleep(web_driver.one_second)
            remove_tags = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().remove_tags_to_event_in_eventstag(), self.d)
            remove_tags.click()
            time.sleep(web_driver.one_second)
            tagnames = self.d.find_elements(By.XPATH, events_Read_Ini().tagnames_below_to_an_event())
            for opt in tagnames:
                if opt.is_displayed():
                    self.logger.info(f"options are {opt.text} ")
                    self.status.append(True)
                else:
                    self.logger.info("options are not visible")
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_087.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_087.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_087.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_087.png")
            self.logger.error(f"TC_events_087 got exception as: {ex} ")

    def on_Events_tags_panel_click_on_refresh_option_in_action_dropdown_and_verify_updated_text(self):
        try:
            self.logger.info("*****TC_088******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().select_checkbox_by_xpath())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            edit_tags_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_tags_in_actiondropdown())
            edit_tags_option.click()
            time.sleep(web_driver.two_second)
            action_dropdown_in_events_tag = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events_tag())
            action_dropdown_in_events_tag.click()
            time.sleep(web_driver.one_second)
            refresh_option = self.d.find_element(By.XPATH, events_Read_Ini().refresh_option_in_eventtags())
            refresh_option.click()
            time.sleep(web_driver.one_second)
            updating = self.d.find_element(By.XPATH, events_Read_Ini().updating_text())
            if updating.is_displayed():
                self.logger.info("updating text is visible")
                self.status.append(True)
            else:
                self.logger.info("updating text is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_088.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_088.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_088.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_088.png")
            self.logger.error(f"TC_events_088 got exception as: {ex} ")

    def In_Events_page_In_Action_dropdown_click_on_refresh_option_and_verify_page_is_refreshed_and_verify_updated_text(self):
        try:
            self.logger.info("*******TC_089******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            time.sleep(web_driver.one_second)
            web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_events_panel_heading(), self.d)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            refresh_option = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().refresh_option_in_action_dropdown_on_events_page(), self.d)
            refresh_option.click()
            time.sleep(web_driver.one_second)
            updating_text = self.d.find_element(By.XPATH, events_Read_Ini().updating_text_in_event())
            if updating_text.is_displayed():
                self.logger.info("updating text is displayed after clicking refresh option")
                self.status.append(True)
            else:
                self.logger.info("updating text is not visible after clicking refresh option")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_089.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_089.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_089.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_089.png")
            self.logger.error(f"TC_events_089 got exception as: {ex} ")

    def In_Events_page_In_Action_dropdown_click_on_change_refresh_option_and_verify_change_refresh_rate_dialouge_box_is_opened(self):
        try:
            self.logger.info("*********TC_090******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            change_panel_refresh = self.d.find_element(By.XPATH, events_Read_Ini().change_panel_refresh_in_action_dropdown())
            change_panel_refresh.click()
            time.sleep(web_driver.one_second)
            change_panel_refresh_dialouge = self.d.find_element(By.XPATH, events_Read_Ini().change_panel_refresh_dialouge_box())
            print(change_panel_refresh_dialouge.text)
            if change_panel_refresh_dialouge.text == events_Read_Ini().change_panel_refresh_rate_text():
                self.logger.info("change refresh panel dialouge box is visible")
                self.status.append(True)
            else:
                self.logger.info("change refresh panel dialouge box is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_090.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_090.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_090.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_090.png")
            self.logger.error(f"TC_events_090 got exception as: {ex} ")

    def  on_Events_page_In_change_refresh_rate_dialouge_box_verify_dropdown_options_are_visible(self):
        try:
            self.logger.info("********TC_091***** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            change_panel_refresh = self.d.find_element(By.XPATH, events_Read_Ini().change_panel_refresh_in_action_dropdown())
            change_panel_refresh.click()
            time.sleep(web_driver.one_second)
            change_panel_refresh_dropdown = self.d.find_elements(By.XPATH, events_Read_Ini().change_panel_refresh_dropdown())
            for opt in change_panel_refresh_dropdown:
                if opt.is_displayed():
                    print(opt.text)
                    self.logger.info(f"dropdown options are {opt.text}")
                    self.status.append(True)
                else:
                    self.logger.info("dropdown options are not visible")
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_091.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_091.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_091.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_091.png")
            self.logger.error(f"TC_events_091 got exception as: {ex} ")

    def on_Events_page_on_Inchange_refresh_rate_dialouge_box_dropdown_select_a_1_minute_dropdown_option_and_verify_in_Action_dropdown_showing_changerefresh_rate_1_minute_is_visible(self):
        try:
            self.logger.info("********TC_092****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            change_panel_refresh = self.d.find_element(By.XPATH, events_Read_Ini().change_panel_refresh_in_action_dropdown())
            change_panel_refresh.click()
            time.sleep(web_driver.one_second)
            sel = Select(self.d.find_element(By.XPATH, events_Read_Ini().change_panel_refresh_dropdown()))
            sel.select_by_visible_text("5 minutes")
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            minutes_selected = self.d.find_element(By.XPATH, events_Read_Ini().minutes_selected_change_panelrate_refresh())
            if minutes_selected.is_displayed():
                self.status.append("no of minutes selected is visible")
                self.status.append(True)
            else:
                self.logger.info("no of minutes selected is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_092.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_092.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_092.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_092.png")
            self.logger.error(f"TC_events_092 got exception as: {ex} ")

    def on_Events_page_In_change_refresh_rate_dialouge_box_verify_cancel_button_is_visible(self):
        try:
            self.logger.info("*******TC_093******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            change_panel_refresh = self.d.find_element(By.XPATH,
                                                       events_Read_Ini().change_panel_refresh_in_action_dropdown())
            change_panel_refresh.click()
            time.sleep(web_driver.one_second)
            cancel_button = self.d.find_element(By.XPATH, events_Read_Ini().cancel_button_in_change_panel_rate())
            if cancel_button.is_displayed():
                self.logger.info("cancel button is visible")
                self.status.append(True)
            else:
                self.logger.info("cancel button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_093.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_093.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_093.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_093.png")
            self.logger.error(f"TC_events_093 got exception as: {ex} ")

    def on_Events_page_click_on_cancel_button_on_change_refresh_rate_dialouge_box_dialouge_box_is_closed(self):
        try:
            self.logger.info("******TC_094******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            change_panel_refresh = self.d.find_element(By.XPATH,
                                                       events_Read_Ini().change_panel_refresh_in_action_dropdown())
            change_panel_refresh.click()
            time.sleep(web_driver.one_second)
            cancel_button = self.d.find_element(By.XPATH, events_Read_Ini().cancel_button_in_change_panel_rate())
            cancel_button.click()
            time.sleep(web_driver.three_second)
            if cancel_button.is_displayed():
                self.status.append(False)
            else:
                self.status.append(True)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_094.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_094.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_094.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_094.png")
            self.logger.error(f"TC_events_094 got exception as: {ex} ")

    def In_Events_page_click_on_Action_dropdown_verify_print_option_is_visible(self):
        try:
            self.logger.info("********TC_095**** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            print_option = self.d.find_element(By.XPATH, events_Read_Ini().print_option_in_actiondropdown())
            if print_option.is_displayed():
                self.logger.info("print option in action dropdown is visible")
                self.status.append(True)
            else:
                self.logger.info("print option in action dropdown is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_095.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_095.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_095.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_095.png")
            self.logger.error(f"TC_events_095 got exception as: {ex} ")

    def In_Events_page_click_on_Action_dropdown_click_on_print_verify_print_and_cancel_buttons_are_visible(self):
        try:
            self.logger.info("*******TC_096**** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            checkbox = self.d.find_element(By.XPATH, events_Read_Ini().first_checkbox_in_events())
            checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            print_option = self.d.find_element(By.XPATH, events_Read_Ini().print_option_in_actiondropdown())
            print_option.click()
            time.sleep(web_driver.one_second)
            print_button = self.d.find_element(By.XPATH, events_Read_Ini().print_button_after_clicking_print())
            time.sleep(web_driver.one_second)
            cancel_button = self.d.find_element(By.XPATH, events_Read_Ini().cancel_button_after_clicking_print())
            time.sleep(web_driver.one_second)
            if print_button.is_displayed():
                self.logger.info("print button is visible")
                self.status.append(True)
            else:
                self.logger.info("print button is not visible")
                self.status.append(False)
            if cancel_button.is_displayed():
                self.logger.info("cancel button is visible")
                self.status.append(True)
            else:
                self.logger.info("cancel button is not visible")
                self.status.append(False)
            cancel_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_096.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_096.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_096.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_096.png")
            self.logger.error(f"TC_events_096 got exception as: {ex} ")

    def on_Events_page_click_on_Events_symbol_and_verify_Event_view_and_Enrollment_view_panels_are_visible(self):
        try:
            self.logger.info("*******TC_097***** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.three_second)
            event_view = self.d.find_element(By.XPATH, events_Read_Ini().event_view_panel_heading())
            time.sleep(web_driver.one_second)
            enrollment_view = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_view_panel_heading())
            time.sleep(web_driver.one_second)
            if event_view.is_displayed():
                self.logger.info("event view panel is visible")
                self.status.append(True)
            else:
                self.logger.info("event view panel is not visible")
                self.status.append(False)
            if enrollment_view.is_displayed():
                self.logger.info("enrollment view panel is visible")
                self.status.append(True)
            else:
                self.logger.info("enrollment view panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            # self.add_details_panel_cancel()
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_097.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_097.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_097.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_097.png")
            self.logger.error(f"TC_events_097 got exception as: {ex} ")

    def on_Event_view_panel_verify_Action_dropdown_is_visible(self):
        try:
            self.logger.info("*******TC_098******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            action_dropdown_in_event_view_panel = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_event_view())
            if action_dropdown_in_event_view_panel.is_displayed():
                self.logger.info("action dropdown in events view panel is visible")
                self.status.append(True)
            else:
                self.logger.info("action dropdown in event view panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_098.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_098.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_098.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_098.png")
            self.logger.error(f"TC_events_098 got exception as: {ex} ")

    def on_Event_view_panel_click_on_Action_dropdown_followed_by_Identify_within_enrollments_option_in_dropdown_and_verify_Identify_enroll_and_identify_results_panel_are_visible(self):
        try:
            self.logger.info("******TC_099***** started")
            self.load_login_page_if_not_loaded()
            # login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()

            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            action_dropdown_in_event_view_panel = self.d.find_element(By.XPATH,
                                                                      events_Read_Ini().action_dropdown_in_event_view())
            action_dropdown_in_event_view_panel.click()
            time.sleep(web_driver.one_second)
            identify_within_enrollments = self.d.find_element(By.XPATH, events_Read_Ini().identify_within_enrollments())
            identify_within_enrollments.click()
            time.sleep(web_driver.two_second)
            identify_and_enroll = self.d.find_element(By.XPATH, events_Read_Ini().identify_and_enroll_panel())
            time.sleep(web_driver.two_second)
            identify_results = self.d.find_element(By.XPATH, events_Read_Ini().identify_results_panel())
            if identify_and_enroll.is_displayed():
                self.logger.info("identify and enroll panel is visible")
                self.status.append(True)
            else:
                self.logger.info("identify and enroll panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            # self.add_details_panel_cancel()
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_099.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_099.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_099.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_099.png")
            self.logger.error(f"TC_events_099 got exception as: {ex} ")

    def on_Event_view_panel_click_on_Action_dropdown_followed_by_Identify_within_visitor_option_in_dropdown_and_verify_visitor_search_panel_is_visible(self):
        try:
            self.logger.info("********TC_0100******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            action_dropdown_in_event_view_panel = self.d.find_element(By.XPATH,
                                                                      events_Read_Ini().action_dropdown_in_event_view())
            action_dropdown_in_event_view_panel.click()
            time.sleep(web_driver.one_second)
            identify_within_visitors = self.d.find_element(By.XPATH, events_Read_Ini().identify_within_visitors_option_in_eventview())
            identify_within_visitors.click()
            time.sleep(web_driver.three_second)
            visitors_search_panel = self.d.find_element(By.XPATH, events_Read_Ini().visitor_search_panel())
            if visitors_search_panel.is_displayed():
                self.logger.info("visitor search panel is visible")
                self.status.append(True)
            else:
                self.logger.info("visitors search panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_100.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_100.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_100.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_100.png")
            self.logger.error(f"TC_events_100 got exception as: {ex} ")

    def on_Event_view_click_on_print_option_in_Action_dropdown_and_verify_print_page_is_visible_print_button_and_cancel_button_are_visible(self):
        try:
            self.logger.info("*******101******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_events_panel_heading(), self.d)
            event_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().events_button(), self.d)
            event_button.click()
            time.sleep(web_driver.two_second)
            action_dropdown_in_event_view_panel = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                                           .action_dropdown_in_event_view(), self.d)
            action_dropdown_in_event_view_panel.click()
            time.sleep(web_driver.two_second)
            print_option = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                    .print_option_in_eventview_actiondropdon(), self.d)
            print_option.click()
            time.sleep(web_driver.two_second)
            print_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                    .print_button_after_clicking_print(), self.d)
            time.sleep(web_driver.one_second)
            cancel_button = self.d.find_element(By.XPATH, events_Read_Ini().cancel_button_after_clicking_print())
            time.sleep(web_driver.one_second)
            if print_button.is_displayed():
                self.logger.info("print button is visible")
                self.status.append(True)
            else:
                self.logger.info("print button is not visible in ")
                self.status.append(False)
            cancel_button.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_101.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_101.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_101.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_101.png")
            self.logger.error(f"TC_events_101 got exception as: {ex} ")

    def on_Event_view_panel_verify_video_button_is_visible_and_clickable(self):
        try:
            self.logger.info("********TC_102******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            video_button = self.d.find_element(By.XPATH, events_Read_Ini().videobutton_in_eventview())
            if video_button.is_displayed():
                self.logger.info("video button is visible")
                self.status.append(True)
            else:
                self.logger.info("video button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_102.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_102.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_102.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_102.png")
            self.logger.error(f"TC_events_102 got exception as: {ex} ")

    def on_Event_view_panel_click_on_video_button_and_verify_Event_video_panel_is_visible(self):
        try:
            self.logger.info("*******TC_103****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            self.logger.info("events panel opened.")
            web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_events_panel_heading(), self.d)
            event_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().events_button(), self.d)
            event_button.click()
            self.logger.info("events btn is displayed.")
            time.sleep(web_driver.two_second)
            video_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                    .videobutton_in_eventview(), self.d)
            video_button.click()
            self.logger.info("video btn is clicked.")
            time.sleep(web_driver.one_second)
            video_details_panel = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                           .video_details_panel(), self.d)

            if video_details_panel.is_displayed():
                self.logger.info("video details panel is visible")
                self.status.append(True)
            else:
                self.logger.info("video details banner is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_103.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_103.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_103.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_103.png")
            self.logger.error(f"TC_events_103 got exception as: {ex} ")

    def on_Event_view_panel_verify_tags_button_is_visible_and_clickable(self):
        try:
            self.logger.info("*****TC_104******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            tags_button = self.d.find_element(By.XPATH, events_Read_Ini().tagbutton_in_event_view())
            if tags_button.is_displayed():
                self.logger.info("tag button is visible in event view")
                self.status.append(True)
            else:
                self.logger.info("tags button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_104.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_104.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_104.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_104.png")
            self.logger.error(f"TC_events_104 got exception as: {ex} ")

    def on_Event_view_panel_click_on_tags_button_and_verify_Events_tags_panel_is_visible(self):
        try:
            self.logger.info("*****TC_105**** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            time.sleep(web_driver.three_second)
            web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_events_panel_heading(), self.d)
            event_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().events_button(), self.d)
            event_button.click()
            time.sleep(web_driver.two_second)
            tags_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                   .tagbutton_in_event_view(), self.d)
            tags_button.click()
            time.sleep(web_driver.three_second)
            event_tags_panel = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                        .events_tags_panel_heading(), self.d)
            if event_tags_panel.is_displayed():
                self.logger.info("events tag panel is visible")
                self.status.append(True)
            else:
                self.logger.info("events tag panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_105.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_105.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_105.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_105.png")
            self.logger.error(f"TC_events_105 got exception as: {ex} ")

    def In_Enrollment_view_panel_verify_Action_dropdown_is_visible_and_clickable(self):
        try:
            self.logger.info("*****TC_106***** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_enrollmentview())
            if action_dropdown.is_displayed():
                self.logger.info("action dropdown is visible in enrollment view")
                self.status.append(True)
            else:
                self.logger.info("action dropdown is not visible in enrollemnt view")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_106.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_106.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_106.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_106.png")
            self.logger.error(f"TC_events_106 got exception as: {ex} ")

    def on_Enrollment_view_click_on_Action_dropdown_followed_by_Identify_within_enrollments_and_verify_Identify_and_enroll_identify_results_panels_are_visible(self):
        try:
            self.logger.info("*******TC_107***** started")
            self.load_login_page_if_not_loaded()
            # login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            self.logger.info("events panel opened")
            time.sleep(web_driver.one_second)
            web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_events_panel_heading(), self.d)
            event_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().events_button(), self.d)
            event_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("events btn clicked.")
            action_dropdown = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                       .action_dropdown_in_enrollmentview(), self.d)
            action_dropdown.click()
            self.logger.info("action dropdown is visible.")
            identify_within_enrollments = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                                   .identify_within_enrollments_in_enrollmentview(), self.d)
            identify_within_enrollments.click()
            self.logger.info("identify within enrollments option visible")
            time.sleep(web_driver.one_second)
            identify_enroll_panel = web_driver.explicit_wait(self, 10, "XPATH",events_Read_Ini()
                                                             .identify_and_enroll_panel(), self.d)

            identify_results = web_driver.explicit_wait(self, 10, "XPATH",
                                     events_Read_Ini().identify_results_panel(), self.d)
            self.logger.info(f"identify result panel visible: {identify_results.is_displayed()}")
            if identify_enroll_panel.is_displayed():
                self.logger.info("identify and enroll panel is visible")
                self.status.append(True)
            else:
                self.logger.info("identify and enroll panel is not visible")
                self.status.append(False)
            if identify_results.is_displayed():
                self.logger.info("identify results panel is visible")
                self.status.append(True)
            else:
                self.logger.info("identify results panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            # self.add_details_panel_cancel()
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_107.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_107.png")
                self.logger.info("returning False.")
                return False
            else:
                self.logger.info("returning True.")
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_107.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_107.png")
            self.logger.error(f"TC_events_107 got exception as: {ex} ")

    def on_Enrollment_view_Action_dropdown_on_Enrollment_view_followed_by_Identify_within_visitors_and_verify_visitor_search_panel_is_visible(self):
        try:
            self.logger.info("********TC_108********* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_enrollmentview())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            identify_within_visitors = self.d.find_element(By.XPATH, events_Read_Ini().identify_within_visitors_in_enrollmentview())
            identify_within_visitors.click()
            time.sleep(web_driver.two_second)
            visitor_search_panel = self.d.find_element(By.XPATH, events_Read_Ini().visitor_search_panel())
            if visitor_search_panel.is_displayed():
                self.logger.info("visitor search panel is visible")
                self.status.append(True)
            else:
                self.logger.info("visitor seaarch panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_108.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_108.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_108.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_108.png")
            self.logger.error(f"TC_events_108 got exception as: {ex} ")

    def on_Enrollment_view_click_on_view_Edits_details_in_Acton_dropdown_and_verify_Enrollment_details_panel_is_visible(self):
        try:
            self.logger.info("*******TC_109******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_enrollmentview())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            edit_view_option = self.d.find_element(By.XPATH, events_Read_Ini().edit_view_enrollment_option_in_actiondropdown())
            edit_view_option.click()
            time.sleep(web_driver.one_second)
            enrollment_details_panel = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_details_panel())
            if enrollment_details_panel.is_displayed():
                self.logger.info("enrollment details panel is visible")
                self.status.append(True)
            else:
                self.logger.info("enrollment details panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_109.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_109.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_109.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_109.png")
            self.logger.error(f"TC_events_109 got exception as: {ex} ")

    def on_Enrollment_view_click_Disiable_enrollment_in_Actiondropdown_an_alert_is_visible_click_ok_an_alert_Event_is_disabled_verify_in_Events_page_goto_event_Diabled_text_is_visible_in_that_event(self):
        try:
            self.logger.info("******TC_110******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            # events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            self.logger.info("events panel is opened.")
            time.sleep(web_driver.three_second)
            # event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().events_button(), self.d)
            event_button.click()
            self.logger.info("events btn is clicked")
            time.sleep(web_driver.two_second)
            # action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_enrollmentview())
            action_dropdown = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().action_dropdown_in_enrollmentview(), self.d)
            action_dropdown.click()
            self.logger.info("action dropdown is clicked.")
            time.sleep(web_driver.one_second)
            # disabled_enrollment = self.d.find_element(By.XPATH, events_Read_Ini().disabled_enrollment_in_enrollmentview())
            disabled_enrollment = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().disabled_enrollment_in_enrollmentview(), self.d)
            disabled_enrollment.click()
            self.logger.info("disable enrollment clicked.")
            time.sleep(web_driver.one_second)
            a = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            a.accept()
            time.sleep(web_driver.one_second)
            # checkbox = self.d.find_element(By.XPATH, events_Read_Ini().first_checkbox_in_events())
            # checkbox.click()
            # time.sleep(web_driver.one_second)
            # action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_enrollmentview())
            # action_dropdown.click()
            # time.sleep(web_driver.one_second)
            # disabled_enrollment = self.d.find_element(By.XPATH, events_Read_Ini().disabled_enrollment_in_enrollmentview())
            # disabled_enrollment.click()
            disabled_text_in_enrollmentview = self.d.find_element(By.XPATH, events_Read_Ini().disabled_text_in_enrollmentview_page())
            self.logger.info(f"disabled text visible: {disabled_text_in_enrollmentview.is_displayed()}")
            if disabled_text_in_enrollmentview.is_displayed():
                self.logger.info("disabled text is visible in enrollment view panel")
                self.status.append(True)
                self.logger.info("appending True")
            else:
                self.logger.info("disabled text is not visible in enrollment view panel")
                self.status.append(False)
                self.logger.info("appending False")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_110.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_110.png")
                self.logger.info("returning False")
                return False
            else:
                self.logger.info("returning True")
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_110.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_110.png")
            self.logger.error(f"TC_events_110 got exception as: {ex} ")

    def on_Enrollment_view_click_Permanently_DELETE_Enrollment_in_Action_dropdown_verify_warning_dialouge_box_is_visible(self):
        try:
            self.logger.info("*********TC_111**** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_enrollmentview())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            permenantly_delete_enrollment = self.d.find_element(By.XPATH, events_Read_Ini().permenantly_delete_enrollment_option_in_enrollment())
            permenantly_delete_enrollment.click()
            time.sleep(web_driver.one_second)
            warning_dialouge_box = self.d.find_element(By.XPATH, events_Read_Ini().warning_dialouge_box())
            if warning_dialouge_box.is_displayed():
                self.logger.info("warning dialouge box is visible")
                self.status.append(True)
            else:
                self.logger.info("warning dialouge box is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_111.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_111.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_111.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_111.png")
            self.logger.error(f"TC_events_111 got exception as: {ex} ")

    def on_Enrollment_view_click_on_Actiondropdown_followed_by_Permanently_DELETE_Enrollment_verify_warning_dialouge_box_is_visible_click_on_Nocancel_button_and_verify_warning_dialouge_box_is_closed(self):
        try:
            self.logger.info("*********TC_012******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_enrollmentview())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            permenantly_delete_enrollment = self.d.find_element(By.XPATH,
                                                                events_Read_Ini().permenantly_delete_enrollment_option_in_enrollment())
            permenantly_delete_enrollment.click()
            time.sleep(web_driver.one_second)
            cancel_button = self.d.find_element(By.XPATH, events_Read_Ini().cancel_button_in_warning_dialouge_box())
            cancel_button.click()
            time.sleep(web_driver.one_second)
            Enrollment_view_panel = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_view_panel_heading())
            if Enrollment_view_panel.is_displayed():
                self.logger.info("enrollment view panel is visible")
                self.status.append(True)
            else:
                self.logger.info("enrollment view panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_112.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_112.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_112.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_112.png")
            self.logger.error(f"TC_events_112 got exception as: {ex} ")

    def on_Enrollment_view_click_Permanently_DELETE_Enrollment_in_Action_dropdown_a_warning_dialouge_box_is_visible_click_on_Yes_Delete_Person_and_Their_Events_button_verify_event_is_removed(self):
        try:
            self.logger.info("********TC_113********* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_enrollmentview())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            permenantly_delete_enrollment = self.d.find_element(By.XPATH, events_Read_Ini().permenantly_delete_enrollment_option_in_enrollment())
            permenantly_delete_enrollment.click()
            time.sleep(web_driver.one_second)
            yes_delete_selected_enrollment_button = self.d.find_element(By.XPATH, events_Read_Ini().yes_delecte_selected_event_and_their_events_button_on_warning_dialougebox())
            # yes_delete_selected_enrollment_button.click()
        except Exception as ex:
            print(ex)

    def verify_Enrollment_Details_button_is_visible_in_Enrollment_view_panel(self):
        try:
            self.logger.info("*********TC_114******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            enrollment_details_button = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_details_button_in_enrollment_view_panel())
            if enrollment_details_button.is_displayed():
                self.logger.info("enrollment details button is visible in enrollment view panel")
                self.status.append(True)
            else:
                self.logger.info("enrollments details button is not visible in enrollment view panel")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_114.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_114.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_114.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_114.png")
            self.logger.error(f"TC_events_114 got exception as: {ex} ")

    def on_Enrollment_view_panel_click_on_Enrollment_Details_button_and_verify_Enrollment_Details_panel_is_visible(self):
        try:
            self.logger.info("********TC_115******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            enrollment_details_button = self.d.find_element(By.XPATH,
                                                            events_Read_Ini().enrollment_details_button_in_enrollment_view_panel())
            enrollment_details_button.click()
            time.sleep(web_driver.one_second)
            enrollment_details_panel = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_details_panel())
            if enrollment_details_panel.is_displayed():
                self.logger.info("enrollment details panel is visible")
                self.status.append(True)
            else:
                self.logger.info("enrollments details panel is not visible")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_115.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_115.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_115.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_115.png")
            self.logger.error(f"TC_events_115 got exception as: {ex} ")

    def verify_Faces_button_is_visible_in_Enrollment_view_panel(self):
        try:
            self.logger.info("********TC_116***** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            faces_button = self.d.find_element(By.XPATH, events_Read_Ini().faces_button_in_enrollmentview())
            if faces_button.is_displayed():
                self.logger.info("faces button is  visible")
                self.status.append(True)
            else:
                self.logger.info("faces button is  not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_116.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_116.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_116.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_116.png")
            self.logger.error(f"TC_events_116 got exception as: {ex} ")

    def on_Enrollment_view_panel_click_on_Faces_button_and_verify_Enrollment_Faces_panel_is_visible(self):
        try:
            self.logger.info("******TC_117********* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            event_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().events_button(), self.d)
            event_button.click()
            faces_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                    .faces_button_in_enrollmentview(), self.d)
            faces_button.click()
            time.sleep(web_driver.one_second)
            enrollment_faces_panel = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini()
                                                              .Enrollment_Faces_panel(), self.d)
            if enrollment_faces_panel.is_displayed():
                self.logger.info("enrollment faces panel is visible")
                self.status.append(True)
            else:
                self.logger.info("enrollments faces panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_117.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_117.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_117.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_117.png")
            self.logger.error(f"TC_events_117 got exception as: {ex} ")

    def on_Enrollment_view_verify_Events_button_is_visible(self):
        try:
            self.logger.info("*******TC_118***** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            events_button_in_enrollment_view = self.d.find_element(By.XPATH, events_Read_Ini().events_button_enrollment_view())
            if events_button_in_enrollment_view.is_displayed():
                self.logger.info("events button is visible enrollment view panel")
                self.status.append(True)
            else:
                self.logger.info("events button is not visible in enrollment view panel")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_118.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_118.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_118.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_118.png")
            self.logger.error(f"TC_events_118 got exception as: {ex} ")

    def on_Enrollment_view_click_on_Events_Events_panel_is_visible(self):
        try:
            self.logger.info("*********TC_119***** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            events_button_in_enrollment_view = self.d.find_element(By.XPATH, events_Read_Ini().events_button_enrollment_view())
            events_button_in_enrollment_view.click()
            time.sleep(web_driver.one_second)
            events_panel = self.d.find_element(By.XPATH, events_Read_Ini().events_panel_heading_after_clicking_events_button_in_enrollmentview())
            if events_panel.is_displayed():
                self.logger.info("events panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("events panel heading is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_119.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_119.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_119.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_119.png")
            self.logger.error(f"TC_events_119 got exception as: {ex} ")

    def verify_Enrollment_groups_button_is_visible_in_Enrollment_view_panel(self):
        try:
            self.logger.info("********TC_120******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            enrollment_group_button = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_groups_button_in_enrollmentview())
            if enrollment_group_button.is_displayed():
                self.logger.info("enrollment group button is visible in enrollment view panel")
                self.status.append(True)
            else:
                self.logger.info("enrollmrnt group button is not visible in enrollment view panel")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_120.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_120.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_120.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_120.png")
            self.logger.error(f"TC_events_120 got exception as: {ex} ")

    def on_Enrollment_view_panel_click_on_Enrollment_groups_button_and_verify_Enrollment_groups_panel_is_visible(self):
        try:
            self.logger.info("*******TC_121****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            # events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            self.logger.info("events menu clicked.")
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().events_button(), self.d)
            event_button.click()
            self.logger.info("events btn clicked.")
            time.sleep(web_driver.two_second)
            # enrollment_group_button = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_groups_button_in_enrollmentview())
            enrollment_group_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().enrollment_groups_button_in_enrollmentview(), self.d)

            enrollment_group_button.click()
            self.logger.info("enrollment groups btn clicked.")
            time.sleep(web_driver.two_second)
            # enrollment_group_panel = self.d.find_element(By.XPATH, events_Read_Ini().enrollment_group_panel())
            enrollment_group_panel = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().enrollment_group_panel(), self.d)
            self.logger.info(f"enrollments panel is visible: {enrollment_group_panel.is_displayed()}")
            if enrollment_group_panel.is_displayed():
                self.logger.info("enrollment group panel is visible.")
                self.status.append(True)
            else:
                self.logger.info("enrollment group panel is not visible.")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            # self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            ele = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_facefirst_logout_button(), self.d)
            ele.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_121.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_121.png")
                self.logger.info("returning False")
                return False
            else:
                self.logger.info("returning True")
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_121.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_121.png")
            self.logger.error(f"TC_events_121 got exception as: {ex} ")

    def verify_Notes_button_is_visible_in_Enrollment_view_panel(self):
        try:
            self.logger.info("*********TC_122******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button.click()
            time.sleep(web_driver.two_second)
            notes_button = self.d.find_element(By.XPATH, events_Read_Ini().notes_button_in_enrollmentview())
            if notes_button.is_displayed():
                self.logger.info("notes button is visible")
                self.status.append(True)
            else:
                self.logger.info("visible button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_122.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_122.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_122.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_122.png")
            self.logger.error(f"TC_events_122 got exception as: {ex} ")

    def on_Enrollment_view_panel_click_on_Notes_button_and_verify_Enrollment_notes_panel_is_visible(self):
        try:
            self.logger.info("*******TC_123****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            # events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            time.sleep(web_driver.three_second)
            # event_button = self.d.find_element(By.XPATH, events_Read_Ini().events_button())
            event_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().events_button(), self.d)
            event_button.click()
            time.sleep(web_driver.two_second)
            # notes_button = self.d.find_element(By.XPATH, events_Read_Ini().notes_button_in_enrollmentview())
            notes_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().notes_button_in_enrollmentview(), self.d)
            notes_button.click()
            time.sleep(web_driver.one_second)
            # notes_panel = self.d.find_element(By.XPATH, events_Read_Ini().notes_panel())
            notes_panel = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().notes_panel(), self.d)
            if notes_panel.is_displayed():
                self.logger.info("notes panel is visible ")
                self.status.append(True)
            else:
                self.logger.info("notes panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_123.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_123.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_123.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_123.png")
            self.logger.error(f"TC_events_123 got exception as: {ex} ")

    def on_Event_page_click_on_tags_symbol_and_verify_Events_Tags_panel_is_visible(self):
        try:
            self.logger.info("******TC_124***** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            tags_symbol = self.d.find_element(By.XPATH, events_Read_Ini().tags_button_in_eventspage())
            tags_symbol.click()
            time.sleep(web_driver.two_second)
            events_tags_panel = self.d.find_element(By.XPATH, events_Read_Ini().events_tags_panel_heading())
            if events_tags_panel.is_displayed():
                self.logger.info("events tags panel is visible")
                self.status.append(True)
            else:
                self.logger.info("events tags panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_124.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_124.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_124.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_124.png")
            self.logger.error(f"TC_events_124 got exception as: {ex} ")

    def on_Eventpage_click_on_extent_menu_button_and_verify_video_location_symbol_is_visible(self):
        try:
            self.logger.info("**********TC_125**** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            extent_menu = self.d.find_element(By.XPATH, events_Read_Ini().extent_menu())
            extent_menu.click()
            time.sleep(web_driver.two_second)
            location_button_in_extentmenu = self.d.find_element(By.XPATH, events_Read_Ini().location_button_in_events_page())
            video_button = self.d.find_element(By.XPATH, events_Read_Ini().video_button_in_events_page())
            if location_button_in_extentmenu.is_displayed():
                self.logger.info("location button is visible")
                self.status.append(True)
            else:
                self.logger.info("location button is not visible")
                self.status.append(False)
            if video_button.is_displayed():
                self.logger.info("video button is visible")
                self.status.append(True)
            else:
                self.logger.info("video button is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_125.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_125.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_125.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_125.png")
            self.logger.error(f"TC_events_125 got exception as: {ex} ")

    def on_Event_page_click_on_extent_menu_followed_by_video_symbol_and_verify_Event_video_panel_is_visible(self):
        try:
            self.logger.info("********TC_126******* started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            # events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().get_Events_in_dashboard(), self.d)
            events.click()
            self.logger.info("events panel opened.")
            time.sleep(web_driver.three_second)
            # extent_menu = self.d.find_element(By.XPATH, events_Read_Ini().extent_menu())
            extent_menu = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().extent_menu(), self.d)
            extent_menu.click()
            self.logger.info("extent menu clicked.")
            time.sleep(web_driver.two_second)
            # video_button = self.d.find_element(By.XPATH, events_Read_Ini().video_button_in_events_page())
            video_button = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().video_button_in_events_page(), self.d)
            video_button.click()
            self.logger.info("video btn is clicked.")
            time.sleep(web_driver.one_second)
            # Event_video_panel = self.d.find_element(By.XPATH, events_Read_Ini().video_details_panel())
            Event_video_panel = web_driver.explicit_wait(self, 10, "XPATH", events_Read_Ini().video_details_panel(), self.d)
            self.logger.info(f"events video panel is displayed: {Event_video_panel.is_displayed()}")
            if Event_video_panel.is_displayed():
                self.logger.info("video details panel is visible")
                self.logger.info("appending True")
                self.status.append(True)
            else:
                self.logger.info("video details panel is not visible")
                self.logger.info("appending False")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_126.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_126.png")
                self.logger.info("returning False")
                return False
            else:
                self.logger.info("returning True")
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_126.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_126.png")
            self.logger.error(f"TC_events_126 got exception as: {ex} ")

    def on_Event_video_panel_verify_video_is_visible(self):
        try:
            self.logger.info("*******TC_127****** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            self.logger.info("events panel is opened.")
            time.sleep(web_driver.three_second)
            extent_menu = self.d.find_element(By.XPATH, events_Read_Ini().extent_menu())
            extent_menu.click()
            self.logger.info("extent menu clicked.")
            time.sleep(web_driver.two_second)
            video_button = self.d.find_element(By.XPATH, events_Read_Ini().video_button_in_events_page())
            video_button.click()
            self.logger.info("video btn clicked.")
            time.sleep(web_driver.one_second)
            video = self.d.find_element(By.XPATH, events_Read_Ini().video_in_event_video_panel())
            self.logger.info(f"video is visible: {video.is_displayed()}")
            if video.is_displayed():
                self.logger.info("video is visible")
                self.status.append(True)
            else:
                self.logger.info("video is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_127.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_127.png")
                self.logger.info("returning False")
                return False
            else:
                self.logger.info("returning True.")
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_127.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_127.png")
            self.logger.error(f"TC_events_127 got exception as: {ex} ")

    def on_Event_page_click_on_extentmenu_followed_by_location_symbol_and_verify_Events_Location_is_panel_is_visible(self):
        try:
            self.logger.info("********TC_128******** started")
            # self.load_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            extent_menu = self.d.find_element(By.XPATH, events_Read_Ini().extent_menu())
            extent_menu.click()
            time.sleep(web_driver.two_second)
            location_button = self.d.find_element(By.XPATH, events_Read_Ini().location_button_in_events_page())
            location_button.click()
            time.sleep(web_driver.one_second)
            event_location = self.d.find_element(By.XPATH, events_Read_Ini().events_location_panel())
            if event_location.is_displayed():
                self.logger.info("events location panel is visible")
                self.status.append(True)
            else:
                self.logger.info("events location panel is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_128.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_128.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_128.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_128.png")
            self.logger.error(f"TC_events_128 got exception as: {ex} ")

    def verify_user_able_to_delete_selected_Probable_Match_Events(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            events = self.d.find_element(By.XPATH, events_Read_Ini().get_Events_in_dashboard())
            events.click()
            time.sleep(web_driver.three_second)
            selecting_checkbox = self.d.find_element(By.XPATH , events_Read_Ini().first_event_checkbox())
            selecting_checkbox.click()
            time.sleep(web_driver.one_second)
            action_dropdown = self.d.find_element(By.XPATH, events_Read_Ini().action_dropdown_in_events())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            permenant_delete_option = self.d.find_element(By.LINK_TEXT,"Permanently DELETE Selected Events")
            permenant_delete_option.click()
            time.sleep(web_driver.two_second)
            delete_event_option = self.d.find_element(By.XPATH, events_Read_Ini().delete_event_button())
            delete_event_option.click()
            time.sleep(web_driver.one_second)
            Event_deletion_success_msg = self.d.find_element(By.XPATH , events_Read_Ini().event_deleting_success_msg())
            if Event_deletion_success_msg.is_displayed():
                self.logger.info(" Event deletion success msg is visible")
                self.status.append(True)
            else:
                self.logger.info("Event deletion success msg is not visible")
                self.status.append(True)
            self.logger.info(f"status:{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, events_Read_Ini().get_facefirst_logout_button()).click()
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_139.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_139.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_events_139.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_events_139.png")
            self.logger.error(f"TC_events_128 got exception as: {ex} ")


    def close_all_panels(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH, Read_Tags_Components().close_all_panel_list_in_tags())
            for i in close_panel_list:
                i.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\close_all_panel_one_by_one_failed.png")
            self.log.info(f"close_all_panel_one_by_one_failed:  {ex}")

