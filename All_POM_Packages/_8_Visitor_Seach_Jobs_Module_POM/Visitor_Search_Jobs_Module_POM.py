from All_Config_Packages._7_Visitor_Search_Module_Config_Files.Visitor_Search_Read_INI import Read_Visitor_Search_Components
from All_Config_Packages._8_Visitor_Search_Jobs_Module_Config_Files.Visitor_Search_Jobs_Read_INI import Read_Visitor_Search_jobs_Components
from All_POM_Packages._7_Visitor_Search_Module_POM.Visitor_Search_Module_POM import Visitor_Search_Module_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains, Keys
from pathlib import Path
import pyautogui


class Visitor_Search_Jobs_Module_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()

    # def login_before(self):
    #     try:
    #         self.d.get(Read_Portal_Menu_Components().get_url())
    #         time.sleep(web_driver.three_second)
    #         username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
    #         if not username.is_displayed():
    #             self.d.get(Read_Portal_Menu_Components().get_url())
    #         username.send_keys(Read_Portal_Menu_Components().get_username())
    #         password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
    #         password.send_keys(Read_Portal_Menu_Components().get_password())
    #         login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
    #         self.d.execute_script("arguments[0].click();", login_btn)
    #         time.sleep(web_driver.two_second)
    #     except Exception as ex:
    #         print(ex)

    def __init__(self):
        self.end_datetime = self.end_time = self.end_date = self.end_date_and_time = self.start_datetime = \
            self.start_age = None
        self.start_time = self.start_date = self.start_date_and_time = None

        self.custom_dates_json = \
            (f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\18_Reporting_Module\\Data_From_JSON"
             f"\\custom_dates_json.json")

    def wait_for_visitor_search_result_to_display(self):
        try:
            time.sleep(web_driver.two_second)
            # matches = web_driver.explicit_wait(self, 30, "XPATH", Read_Visitor_Search_jobs_Components().matches_list_by_xpath(), self.d)
            # if matches.is_displayed():
            #     self.logger.info("Image Matches Found.")
            # else:
            #     self.logger.info("Image Match failed.")
            visitor_search_complete = web_driver.explicit_wait(self, 60, "XPATH",
                                                               Read_Visitor_Search_jobs_Components().visitor_search_completed_banner(),
                                                               self.d)
            if visitor_search_complete.is_displayed():
                self.logger.info("Visitor Search Completed.")
            else:
                self.logger.info("Visitor Search Not Completed.")
        except Exception as ex:
            self.logger.info(f"No match found {ex.args}")

    def wait_for_element_to_appear(self, element_list, xpath):
        count = 0
        if len(element_list) == 0:
            while len(element_list) == 0 or count > 150:
                element_list = self.d.find_elements(By.XPATH, xpath)
                time.sleep(web_driver.two_second)
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

    def click_on_visitor_search_jobs_btn(self):
        time.sleep(web_driver.three_second)
        visitor_search_jobs_btn = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().visitors_search_job_btn_by_xpath(), self.d)
        self.d.execute_script("arguments[0].click();", visitor_search_jobs_btn)
        time.sleep(web_driver.two_second)
        visitor_search_jobs_panel_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_heading_by_xpath())
        count = 0
        while len(visitor_search_jobs_panel_list) == 0 or count > 150:
            visitor_search_jobs_panel_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_heading_by_xpath())
            self.logger.info("waiting for vsj panel")
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"visitor search job panel search function count: {count}")

    def login(self):
        # login().login_to_localhost_if_not_done()
        # if self.d.title == "" or self.d.find_element(By.ID, Read_Visitor_Search_jobs_Components().get_loginButton()).is_displayed():
        login().login_to_cloud_if_not_done(self.d)
        #
        #     time.sleep(web_driver.two_second)

    #############################################################################################################

    def Verify_user_able_to_view_the_Visitor_Search_jobs_on_the_cloud_menu(self):
        result = []
        try:
            self.login()
            time.sleep(web_driver.two_second)
            visitor_search_jobs_btn = self.explicit_wait(10, "XPATH", Read_Visitor_Search_jobs_Components().visitors_search_job_btn_by_xpath(), self.d)
            # visitor_search_jobs_btn = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_job_btn_by_xpath())
            result.append(visitor_search_jobs_btn.is_displayed())

            result.append(visitor_search_jobs_btn.is_enabled())
            self.logger.info(f"status: {result}")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_001_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_001_exception.png")
            self.logger.info(f"test_VSJ_001_exception:  {type(ex).__name__}")
            return False

    def verify_user_opens_vsj_then_visitor_search_jobs_panel_should_display(self):
        result = []
        try:

            self.login()
            time.sleep(web_driver.two_second)
            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            vsj_panel_title = self.explicit_wait(10, "XPATH", Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_by_xpath(), self.d)
            # vsj_panel_title = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_by_xpath())
            self.logger.info(f"visitor search jobs visible: {vsj_panel_title.is_displayed()}")
            result.append(vsj_panel_title.is_displayed())
            self.logger.info(f"vsj expected title: {Read_Visitor_Search_jobs_Components().vsj_panel_title()}")
            self.logger.info(f"actual title: {vsj_panel_title.text}")
            result.append(vsj_panel_title.text == Read_Visitor_Search_jobs_Components().vsj_panel_title())
            self.logger.info(f"status:{result}")

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_17_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_17_exception.png")
            self.logger.info(f"test_TC_VSJ_17_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_user_able_to_see_and_open_search_dropdown(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            vsj_search_btn = self.explicit_wait(10, "XPATH", Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_search_button(), self.d)
            # vsj_search_btn = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_search_button())
            self.logger.info(f"vsj search btn visible: {vsj_search_btn.is_displayed()}")
            result.append(vsj_search_btn.is_displayed())
            self.logger.info(f"vsj search btn enabled: {vsj_search_btn.is_enabled()}")
            result.append(vsj_search_btn.is_enabled())
            self.logger.info(f"status: {result}")

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_003_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_003_exception.png")
            self.logger.info(f"test_VSJ_003_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_users_able_to_see_and_open_action_dropdown(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            vsj_action_btn = self.explicit_wait(10, "XPATH", Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_action_button(), self.d)
            # vsj_action_btn = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_action_button())
            self.logger.info(f"vsj action btn visible: {vsj_action_btn.is_displayed()}")
            result.append(vsj_action_btn.is_displayed())
            self.logger.info(f"vsj action btn enabled: {vsj_action_btn.is_enabled()}")
            result.append(vsj_action_btn.is_enabled())
            self.logger.info(f"status: {result}")

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_004_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_004_exception.png")
            self.logger.info(f"test_VSJ_004_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_the_visitor_search_job_contains_the_visitors_from_the_data_range(self):
        result = []
        try:
            self.login()

            self.logger.info("logged in")
            time.sleep(web_driver.two_second)
            self.click_on_visitor_search()
            time.sleep(web_driver.two_second)
            org_hirarchy_btn_by_xpath = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().zone_by_xpath(), self.d)
            self.logger.info(f"org hirarchy btn visible: {org_hirarchy_btn_by_xpath.is_displayed()}")
            org_hirarchy_btn_by_xpath.click()
            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.logger.info(f"zone data: {zone_data}")
            self.select_zone(zone_data)
            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # # self.get_end_date()
            self.logger.info("end date entered")

            self.logger.info("date selected.")

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            try:
                self.connection_error()
            except Exception as ex:
                self.logger.info(f"exception of connection err try: {ex.args}")
                time.sleep(web_driver.two_second)
                self.click_on_cloud_menu()
                time.sleep(web_driver.two_second)
                self.click_on_visitor_search_jobs_btn()
                time.sleep(web_driver.two_second)

                # # result.append(self.verify_date())
                result.append(self.verify_region_from_match_list(zone_data))
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_005_exception.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_005_exception.png")
            self.logger.info(f"test_VSJ_005_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitor_search_job_contains_user_performs_visitor_search_with_date_and_org_selection(self):
        result = []
        try:
            self.login()
            time.sleep(web_driver.two_second)
            self.click_on_visitor_search()
            # date = int(Read_Visitor_Search_jobs_Components().get_start_date())
            # month = str(Read_Visitor_Search_jobs_Components().get_start_month())
            # year = int(Read_Visitor_Search_jobs_Components().get_start_year())
            # hour = str(Read_Visitor_Search_jobs_Components().get_start_hour())
            # minute = Read_Visitor_Search_jobs_Components().get_start_minuet()
            # period = str(Read_Visitor_Search_jobs_Components().get_start_am_pm_period())
            #
            # e_month = str(Read_Visitor_Search_jobs_Components().get_end_month())
            # e_date = int(Read_Visitor_Search_jobs_Components().get_end_date())
            # e_year = int(Read_Visitor_Search_jobs_Components().get_end_year())
            # e_hour = str(Read_Visitor_Search_jobs_Components().get_end_hour())
            # e_minute = Read_Visitor_Search_jobs_Components().get_end_minuet()
            # e_period = str(Read_Visitor_Search_jobs_Components().get_end_am_pm_period())

            org_hirarchy_btn_by_xpath = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().zone_by_xpath(), self.d)
            org_hirarchy_btn_by_xpath.click()
            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            # self.nats_checkbox()
            self.get_start_date()
            time.sleep(3)
            # self.get_end_date()
            time.sleep(3)
            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            # self.wait_till_auto_refresh_on()

            try:
                self.connection_error()
            except Exception as ex:
                self.logger.info(f"connection error exception: {ex.args}")
                time.sleep(web_driver.two_second)
                self.click_on_cloud_menu()
                time.sleep(web_driver.two_second)
                time.sleep(web_driver.two_second)
                self.click_on_visitor_search_jobs_btn()
                time.sleep(web_driver.two_second)
                # result.append(self.verify_date())
                result.append(self.verify_region_from_match_list(zone_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_006_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_006_exception.png")
            self.logger.info(f"test_VSJ_006_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitor_search_job_contains_the_visitor_in_selected_date_range_and_gender(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)
            time.sleep(web_driver.two_second)
            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)
            time.sleep(web_driver.two_second)
            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            self.wait_till_auto_refresh_on()
            no_match_found = self.wait_till_no_match_found()

            try:
                self.connection_error()
            except Exception as ex:
                self.logger.info(f"connection err: {ex.args}")
                time.sleep(web_driver.two_second)
                self.click_on_cloud_menu()
                time.sleep(web_driver.two_second)
                time.sleep(web_driver.two_second)
                self.click_on_visitor_search_jobs_btn()
                time.sleep(web_driver.two_second)
                time.sleep(web_driver.two_second)
                # result.append(self.verify_date())
                result.append(self.verify_region_from_match_list(zone_data))
                result.append(self.verify_gender_match_list(gender_data))
            self.logger.info(f"status: {result}")
            self.logger.info(f"status: {result}")
            if (False in result) and (not no_match_found):
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_007_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_007_exception.png")
            self.logger.info(f"test_VSJ_007_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitor_search_job_contains_the_selected_gender_visitors_in_date_range_and_Org_selection(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)
            time.sleep(web_driver.two_second)
            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            self.wait_till_auto_refresh_on()
            try:
                self.connection_error()
            except Exception as ex:
                self.logger.info(f"connection err exception: {ex.args}")

                time.sleep(web_driver.two_second)
                self.click_on_cloud_menu()
                time.sleep(web_driver.two_second)
                time.sleep(web_driver.two_second)
                self.click_on_visitor_search_jobs_btn()
                time.sleep(web_driver.two_second)
                time.sleep(web_driver.two_second)
                # result.append(self.verify_date())
                result.append(self.verify_region_from_match_list(zone_data))
                result.append(self.verify_gender_match_list(gender_data))
            self.logger.info(f"status: {result}")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_008_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_008_exception.png")
            self.logger.info(f"test_VSJ_008_exception:  {type(ex).__name__}")

            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitor_search_job_contains_the_visitors_in_selected_date_range_and_age_range(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)
            time.sleep(web_driver.two_second)
            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            time.sleep(web_driver.two_second)
            self.select_end_age(end_age)

            # self.nats_checkbox()
            time.sleep(web_driver.two_second)
            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            self.wait_till_auto_refresh_on()
            no_image_found = self.wait_till_no_match_found()
            try:
                self.connection_error()
            except Exception as ex:
                self.logger.info(f"connection error exception: {ex.args}")
                self.click_on_cloud_menu()
                time.sleep(web_driver.two_second)
                self.logger.info(web_driver.one_second)
                self.click_on_visitor_search_jobs_btn()
                time.sleep(web_driver.two_second)
                self.logger.info(web_driver.one_second)
                # result.append(self.verify_date())
                result.append(self.verify_region_from_match_list(zone_data))
            self.logger.info(f"status: {result}")
            self.logger.info(f"status: {result}")
            if (False in result) and (not no_image_found):
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_009_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_009_exception.png")
            self.logger.info(f"test_VSJ_009_exception:  {type(ex).__name__}")

            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitor_search_job_contains_the_visitors_in_date_range_and_age_range_and_org_selection(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)
            time.sleep(web_driver.two_second)
            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            time.sleep(web_driver.two_second)
            self.select_end_age(end_age)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            try:
                self.connection_error()
            except Exception as ex:
                self.logger.info(f"connection err exception: {ex.args}")
                time.sleep(web_driver.two_second)
                self.click_on_cloud_menu()
                time.sleep(web_driver.two_second)
                time.sleep(web_driver.two_second)
                self.click_on_visitor_search_jobs_btn()
                time.sleep(web_driver.two_second)
                time.sleep(web_driver.two_second)
                # result.append(self.verify_date())
                result.append(self.verify_region_from_match_list(zone_data))
            self.logger.info(f"status: {result}")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_010_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_010_exception.png")
            self.logger.info(f"test_VSJ_010_exception:  {type(ex).__name__}")

            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitor_search_job_contains_the_selected_gender_visitors_in_date_range_and_age_range(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)
            time.sleep(web_driver.two_second)
            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)
            time.sleep(web_driver.two_second)
            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)
            time.sleep(web_driver.two_second)
            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            self.wait_till_auto_refresh_on()
            no_matches_found = self.wait_till_no_match_found()
            try:
                self.connection_error()
            except Exception as ex:
                self.logger.info(f"connection err exception: {ex.args}")
                time.sleep(web_driver.two_second)
                self.click_on_cloud_menu()
                time.sleep(web_driver.two_second)
                time.sleep(web_driver.two_second)
                self.click_on_visitor_search_jobs_btn()
                time.sleep(web_driver.two_second)
                time.sleep(web_driver.two_second)
                # result.append(self.verify_date())
                result.append(self.verify_region_from_match_list(zone_data))
                result.append(self.verify_gender_match_list(gender_data))
            self.logger.info(f"status: {result}")
            self.logger.info(f"status: {result}")
            if (False in result) and (not no_matches_found):
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_011_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_011_exception.png")
            self.logger.info(f"test_VSJ_011_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitor_search_job_contains_gender_visitors_in_date_range_and_age_range_and_org_selection(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)
            time.sleep(web_driver.two_second)
            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)
            time.sleep(web_driver.two_second)
            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()
            time.sleep(web_driver.two_second)
            self.select_start_age(start_age)
            self.select_end_age(end_age)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            try:
                self.connection_error()
            except Exception as ex:
                self.logger.info(f"connection err exception: {ex.args}")
                time.sleep(web_driver.two_second)
                self.click_on_cloud_menu()
                time.sleep(web_driver.two_second)
                time.sleep(web_driver.two_second)
                self.click_on_visitor_search_jobs_btn()
                time.sleep(web_driver.two_second)
                time.sleep(web_driver.two_second)
                # result.append(self.verify_date())
                result.append(self.verify_region_from_match_list(zone_data))
                result.append(self.verify_gender_match_list(gender_data))
            self.logger.info(f"status: {result}")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_012_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_012_exception.png")
            self.logger.info(f"test_VSJ_012_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_the_visitor_search_job_contains_the_matching_visitors_with_image_when_visitor_search_with_image_only(self):
        result = []
        try:
            self.add_image_search()
            time.sleep(web_driver.two_second)
            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            visitor_search_complete = web_driver.explicit_wait(self, 80, "XPATH",
                                                               Read_Visitor_Search_jobs_Components().visitor_search_completed_banner(),
                                                               self.d)
            if visitor_search_complete.is_displayed():
                self.logger.info("Visitor Search Completed.")
            else:
                self.logger.info("Visitor Search Not Completed.")
            matches_found = web_driver.explicit_wait(self, 20, "XPATH",
                                                     Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found(),
                                                     self.d)
            max_count = matches_found.text
            self.logger.info(f"max match count text: {max_count}")
            max_number = max_count.split(" ")[0]
            self.logger.info(f"max match count: {max_number}")
            if max_number.isnumeric():
                result.append(int(max_number) <= 50)
                self.click_on_cloud_menu()
                self.click_on_visitor_search_jobs_btn()
                time.sleep(web_driver.two_second)
                max_matches = self.d.find_elements(By.XPATH,
                                                   Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
                count = 0
                while len(max_matches) == 0 or count > 150:
                    max_matches = self.d.find_elements(By.XPATH,
                                                       Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
                    time.sleep(web_driver.two_second)
                    count += 1
                    self.logger.info(f"max matches function count: {count}")
            if max_number.isnumeric():
                result.append(int(max_number) <= 50)
                self.click_on_cloud_menu()
                self.click_on_visitor_search_jobs_btn()
                time.sleep(web_driver.two_second)
                max_matches = self.d.find_elements(By.XPATH,
                                                   Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
                count = 0
                while len(max_matches) == 0 or count > 150:
                    max_matches = self.d.find_elements(By.XPATH,
                                                       Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
                    time.sleep(web_driver.two_second)
                    count += 1
                    self.logger.info(f"max matches function count: {count}")

                max_matches_text = max_matches[0].text
                self.logger.info(f"match count text on visitor search job panel: {max_matches_text}")
                max_number_counted = max_matches_text.split(" ")[0]
                self.logger.info(f"max count on vsj panel: {max_number_counted}")
                result.append(int(max_number_counted) <= 50)
                self.logger.info(f"status: {result}")
                if False in result:
                    self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_02_failed.png")
                    return False
                else:
                    return True
            else:
                self.logger.info("No Image count is displayed.")
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_02_exception.png")
            self.logger.info(f"test_TC_VSJ_02_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_vsj_contains_the_matching_visitors_max_count_should_be_50_search_with_image_only(self):
        result = []
        try:
            self.add_image_search()
            time.sleep(web_driver.two_second)
            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            visitor_search_complete = web_driver.explicit_wait(self, 80, "XPATH",
                                                               Read_Visitor_Search_jobs_Components().visitor_search_completed_banner(),
                                                               self.d)
            if visitor_search_complete.is_displayed():
                self.logger.info("Visitor Search Completed.")
            else:
                self.logger.info("Visitor Search Not Completed.")
            matches_found = web_driver.explicit_wait(self, 20, "XPATH",
                                                     Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found(),
                                                     self.d)
            max_count = matches_found.text
            self.logger.info(f"max match count text: {max_count}")
            max_number = max_count.split(" ")[0]
            self.logger.info(f"max match count: {max_number}")
            if max_number.isnumeric():
                result.append(int(max_number) <= 50)
                self.click_on_cloud_menu()
                self.click_on_visitor_search_jobs_btn()
                time.sleep(web_driver.two_second)
                max_matches = self.d.find_elements(By.XPATH,
                                                   Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
                count = 0
                while len(max_matches) == 0 or count > 150:
                    max_matches = self.d.find_elements(By.XPATH,
                                                       Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
                    time.sleep(web_driver.two_second)
                    count += 1
                    self.logger.info(f"max matches function count: {count}")
            if max_number.isnumeric():
                result.append(int(max_number) <= 50)
                self.click_on_cloud_menu()
                self.click_on_visitor_search_jobs_btn()
                time.sleep(web_driver.two_second)
                max_matches = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
                count = 0
                while len(max_matches) == 0 or count > 150:
                    max_matches = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
                    time.sleep(web_driver.two_second)
                    count += 1
                    self.logger.info(f"max matches function count: {count}")

                max_matches_text = max_matches[0].text
                self.logger.info(f"match count text on visitor search job panel: {max_matches_text}")
                max_number_counted = max_matches_text.split(" ")[0]
                self.logger.info(f"max count on vsj panel: {max_number_counted}")
                result.append(int(max_number_counted) <= 50)
                self.logger.info(f"status: {result}")
                if False in result:
                    self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_013_failed.png")
                    return False
                else:
                    return True
            else:
                self.logger.info("No Image count is displayed.")
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_013_exception.png")
            self.logger.info(f"test_VSJ_013_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    # def verify_that_the_vsj_contains_the_matching_visitors_max_count_should_be_50_search_with_image_only(self):
    #     result = []
    #     try:
    #         self.add_image_search()
    #         time.sleep(web_driver.two_second)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #         time.sleep(web_driver.two_second)
    #
    #         # self.wait_till_auto_refresh_on()
    #         time.sleep(web_driver.two_second)
    #         # matches_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
    #         visitor_search_complete = web_driver.explicit_wait(self, 60, "XPATH", Read_Visitor_Search_jobs_Components().visitor_search_completed_banner(), self.d)
    #         if visitor_search_complete.is_displayed():
    #             self.logger.info("Visitor Search Completed.")
    #         else:
    #             self.logger.info("Visitor Search Not Completed.")
    #         matches_found = web_driver.explicit_wait(self, 20, "XPATH", Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found(),
    #                                                            self.d)
    #         max_count = matches_found.text
    #         self.logger.info(f"max match count text: {max_count}")
    #         max_number = max_count.split(" ")[0]
    #         self.logger.info(f"max match count: {max_number}")
    #         if max_number.isnumeric():
    #             result.append(int(max_number) <= 50)
    #
    #             self.click_on_visitor_search_jobs_btn()
    #             time.sleep(web_driver.two_second)
    #             max_matches = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
    #             count = 0
    #             while len(max_matches) == 0 or count > 150:
    #                 max_matches = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
    #                 time.sleep(web_driver.two_second)
    #                 count += 1
    #                 self.logger.info(f"max matches function count: {count}")
    #
    #             max_matches_text = max_matches[0].text
    #             self.logger.info(f"match count text on visitor search job panel: {max_matches_text}")
    #             max_number_counted = max_matches_text.split(" ")[0]
    #             self.logger.info(f"max count on vsj panel: {max_number_counted}")
    #             result.append(int(max_number_counted) <= 50)
    #             self.logger.info(f"status: {result}")
    #             self.logger.info(f"status: {result}")
    #             if False in result:
    #                 self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_013_failed.png")
    #                 return False
    #             else:
    #                 return True
    #         else:
    #             self.logger.info("No Image count is displayed.")
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_013_exception.png")
    #         self.logger.info(f"test_VSJ_013_exception:  {type(ex).__name__}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()

    def verify_the_vsj_contains_the_count_of_matching_visitors_when_visitor_search_with_image_and_max_matches(self):
        result = []
        try:
            self.add_image_search()
            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)
            time.sleep(web_driver.two_second)

            self.click_on_submit_search_button()
            matches_found = web_driver.explicit_wait(self, 30, "XPATH", Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found(), self.d)
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            print(max_number)
            print(int(count_data))
            result.append(int(max_number) <= int(count_data))
            self.click_on_cloud_menu()
            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]
            result.append(int(max_number_counted) <= int(count_data))
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_014_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_014_exception.png")
            self.logger.info(f"test_VSJ_014_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_vsj_contains_threshold_greater_than_or_equal_to_threshold_with_image_and_threshold(self):
        result = []
        try:
            self.add_image_search()
            time.sleep(web_driver.two_second)
            threshold_data = self.set_thresh_hold_slider()
            
            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            matches_found = web_driver.explicit_wait(self, 20, "XPATH", Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found(), self.d)
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))
            self.click_on_cloud_menu()
            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            max_matches = web_driver.explicit_wait(self, 20, "XPATH", Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath(), self.d)
            max_matches_text = max_matches.text
            print(max_count)
            self.logger.info(f"max count: {max_count}")
            max_number_counted = max_matches_text.split(" ")[0]
            print(max_number_counted)
            self.logger.info(f"max number counted: {max_number_counted}")
            result.append(int(max_number_counted) <= int(threshold_data))
            self.logger.info(f"status: {result}")

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_05_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VSJ_05_exception.png")
            self.logger.info(f"test_TC_VSJ_05_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_threshold_when_search_threshold_with_image_threshold_and_max_matches(self):
        result = []
        try:
            self.add_image_search()
            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            threshold_data = self.set_thresh_hold_slider()

            # self.nats_checkbox()
            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            self.wait_for_visitor_search_result_to_display()

            matches_found = web_driver.explicit_wait(self, 20, "XPATH", Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found(), self.d)
            max_count = matches_found.text
            self.logger.info(f"match found: {max_count}")
            max_number = max_count.split(" ")[0]
            self.logger.info(f"count: {max_number}")
            if max_number.isnumeric():
                result.append(int(max_number) <= int(threshold_data))
                result.append(int(max_number) <= int(count_data))
                self.click_on_cloud_menu()
                self.click_on_visitor_search_jobs_btn()
                time.sleep(web_driver.two_second)
                max_matches = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath(), self.d)
                max_matches_text = max_matches.text
                self.logger.info(f"max count: {max_count}")
                max_number_counted = max_matches_text.split(" ")[0]
                self.logger.info(f"max number counted: {max_number_counted}")
                result.append(int(max_number_counted) <= int(threshold_data))
                result.append(int(max_number_counted) <= int(count_data))
                self.logger.info(f"status: {result}")
                if False in result:
                    self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_016_failed.png")
                    return False
                else:
                    return True
            else:
                self.logger.info(f"No possible match found")
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_016_exception.png")
            self.logger.info(f"test_VSJ_016_fexception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_vsj_contains_gender_result_when_the_visitor_search_with_image_and_gender(self):
        result = []
        try:
            self.add_image_search()

            # self.nats_checkbox()

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            # self.wait_till_auto_refresh_on()
            # self.refresh_icon_wait()

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            print(gender_data)
            self.logger.info(f"gender data: {gender_data}")
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            self.logger.info(f"status: {result}")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_017_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_017_exception.png")
            self.logger.info(f"test_VSJ_017_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_vsj_contains_visitors_and_gender_when_search_with_image_gender_and_max_matches(self):
        result = []
        try:
            self.add_image_search()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            self.wait_till_auto_refresh_on()
            # self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) == int(count_data))

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(int(max_number_counted) == int(count_data))

            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            self.logger.info(f"status: {result}")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_018_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_018_exception.png")
            self.logger.info(f"test_VSJ_018_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_vsj_contains_visitors_and_threshold_when_search_with_image_gender_and_threshold(self):
        result = []
        try:
            self.add_image_search()
            threshold_data = self.set_thresh_hold_slider()

            # self.nats_checkbox()

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            self.wait_till_auto_refresh_on()
            # self.refresh_icon_wait()

            matches_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]
            
            result.append(int(max_number_counted) <= int(threshold_data))

            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            self.logger.info(f"status: {result}")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_019_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_019_exception.png")
            self.logger.info(f"test_VSJ_019_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_gender_threshold_max_matches_when_search_with_image_gender_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()
            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            matches_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            if max_count < Read_Visitor_Search_jobs_Components().matches_found_text():
                self.logger.info("No match count...")
            else:
                self.logger.info(f"max count: {max_count}")
                max_number = max_count.split(" ")[0]
                self.logger.info(f"max number: {max_number}")
                result.append(int(max_number) <= int(threshold_data))
                result.append(int(max_number) <= int(count_data))
            time.sleep(web_driver.two_second)
            
            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            self.logger.info("clicked on visitor search jobs btn")
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            self.logger.info(f"max match text: {max_matches_text}")
            max_number_counted = max_matches_text.split(" ")[0]
            self.logger.info(f"max number counted: {max_number_counted}")

            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(int(max_number_counted) <= int(count_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            self.logger.info(f"status: {result}")
            
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_020_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_020_exception.png")
            self.logger.info(f"test_VSJ_020_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_vsj_contains_an_age_range_when_a_visitor_search_with_an_image_and_an_age_range(self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            
            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            print(start_age)
            print(end_age)
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_021_exception.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_021_exception.png")
            self.logger.info(f"test_VSJ_021_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_age_range_max_matches_when_visitor_search_with_image_age_range_max_matches(self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            # self.nats_checkbox()
            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()
            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text

            max_number = max_count.split(" ")[0]

            result.append(int(max_number) == int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(int(max_number_counted) <= int(count_data))

            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_022_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_022_exception.png")
            self.logger.info(f"test_VSJ_022_exception:  {type(ex).__name__}")

            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_age_range_and_threshold_when_visitor_search_with_image_age_range_and_threshold(self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            threshold_data = self.set_thresh_hold_slider()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()
            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_023_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_023_exception.png")
            self.logger.info(f"test_VSJ_023_exception:  {type(ex).__name__}")

            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_age_threshold_and_max_of_matches_when_search_with_image_age_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))

            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(int(max_number_counted) <= int(count_data))

            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_024_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_024_exception.png")
            self.logger.info(f"test_VSJ_024_exception:  {type(ex).__name__}")

            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_visitor_search_job_contains_age_gender_when_visitor_search_with_image_age_gender(self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            self.wait_till_auto_refresh_on()

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            print(start_age)
            print(end_age)
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_025_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_025_exception.png")
            self.logger.info(f"test_VSJ_025_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_age_gender_and_max_matches_when_search_with_image_age_gender_and_max_matches(self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_026_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_026_exception.png")
            self.logger.info(f"test_VSJ_026_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_age_gender_and_threshold_when_search_with_image_age_gender_and_threshold(self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_027_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_027_exception.png")
            self.logger.info(f"test_VSJ_027_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_age_gender_threshold_max_matches_search_image_age_gender_threshold_max_matches(
            self):
        result = []
        try:
            self.add_image_search()

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_028_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_028_exception.png")
            self.logger.info(f"test_VSJ_028_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_visitor_search_job_contains_region_when_visitor_search_with_image_and_region(self):
        result = []
        try:
            self.add_image_search()

            self.select_org_hirarchy_btn()
            self.logger.info("org hirarchy btn selected")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.logger.info(f"zone data: {zone_data}")
            self.select_zone(zone_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            self.logger.info("clicked on search btn")
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            result.append(self.verify_region_from_match_list(zone_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_029_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_029_exception.png")
            self.logger.info(f"test_VSJ_029_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_and_max_matches_when_visitor_search_with_image_region_and_max_matches(self):
        result = []
        try:
            self.add_image_search()

            self.select_org_hirarchy_btn()
            self.logger.info("org hirarchy selected")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_030_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_030_exception.png")
            self.logger.info(f"test_VSJ_030_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_and_threshold_when_visitor_search_with_image_region_and_threshold(self):
        result = []
        try:
            self.add_image_search()

            self.select_org_hirarchy_btn()
            self.logger.info("org hirarchy selected")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            threshold_data = self.set_thresh_hold_slider()

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_031_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_031_exception.png")
            self.logger.info(f"test_VSJ_031_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_threshold_max_matches_when_search_with_image_region_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()

            self.select_org_hirarchy_btn()
            self.logger.info("org hirarchy selected")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            # result.append(int(max_number_counted) <= int(threshold_data))
            # result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_032_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_032_exception.png")
            self.logger.info(f"test_VSJ_031_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_and_gender_when_search_with_image_region_and_gender(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_033_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_033_exception.png")
            self.logger.info(f"test_VSJ_033_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_gender_max_matches_when_search_with_image_region_gender_max_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()
            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_034_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_034_exception.png")
            self.logger.info(f"test_VSJ_034_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_gender_and_threshold_when_search_with_image_region_gender_and_threshold(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()
            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_035_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_035_exception.png")
            self.logger.info(f"test_VSJ_035_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_gender_threshold_max_matches_search_image_region_gender_threshold_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()
            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(count_data))
            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(count_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_036_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_036_exception.png")
            self.logger.info(f"test_VSJ_036_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_and_age_range_when_search_with_image_region_and_age_range(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_037_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_037_exception.png")
            self.logger.info(f"test_VSJ_037_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_age_range_max_matches_when_search_with_image_region_age_range_max_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            # result.append(int(max_number_counted) <= int(count_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_038_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_038_exception.png")
            self.logger.info(f"test_VSJ_038_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_age_threshold_matches_search_with_image_region_age_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            threshold_data = self.set_thresh_hold_slider()

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]

            # result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            # result.append(int(max_number_counted) <= int(threshold_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_039_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_039_exception.png")
            self.logger.info(f"test_VSJ_039_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_age_threshold_max_matches_search_with_image_region_age_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(int(max_number_counted) <= int(count_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_040_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_040_exception.png")
            self.logger.info(f"test_VSJ_040_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_age_range_gender_when_search_with_image_region_age_range_gender(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_041_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_041_exception.png")
            self.logger.info(f"test_VSJ_041_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_age_gender_mx_matches_when_search_with_image_region_age_gender_max_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_042_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_042_exception.png")
            self.logger.info(f"test_VSJ_042_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_region_age_gender_threshold_when_search_with_image_region_age_gender_threshold(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_043_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_043_exception.png")
            self.logger.info(f"test_VSJ_043_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_region_age_gender_threshold_mx_matches_search_image_region_age_gender_threshold_mx_matches(self):
        result = []
        try:
            self.add_image_search()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(threshold_data))
            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            result.append(int(max_number_counted) <= int(threshold_data))
            result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_044_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_044_exception.png")
            self.logger.info(f"test_VSJ_044_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_when_search_with_image_and_date_range(self):
        result = []
        try:
            # self.login()
            # self.click_on_visitor_search()
            self.add_image_search()
            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # result.append(self.verify_date())

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_045_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_045_exception.png")
            self.logger.info(f"test_VSJ_045_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_and_max_matches_when_search_with_image_and_date_range_and_max_matches(self):
        result = []
        try:
            self.add_image_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()
            self.logger.info("executed submit button")
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()
            self.logger.info("executed wait_till_auto_refresh_on")

            # matches_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(count_data))
            # matches_found = self.matches_found()
            # if type(matches_found) == bool:
            #     result.append(matches_found)
            # else:
            #     self.logger.info("no matches found")

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)
            self.click_on_visitor_search_jobs_btn()
            self.logger.info("clicked on click_on_visitor_search_jobs_btn")
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))
            time.sleep(web_driver.two_second)
            # self.get_start_date()
            # result.append(self.verify_date())
            print(result)

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_046_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_046_exception.png")
            self.logger.info(f"test_VSJ_046_exception:  {type(ex).__name__}")
            return False

        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_and_threshold_when_search_with_image_and_date_range_and_threshold(self):
        result = []
        try:
            # login().login_to_localhost_if_not_done()
            self.add_image_search()

            # self.nats_checkbox()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            threshold_data = self.set_thresh_hold_slider()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # result.append(self.wait_till_no_match_found())

            # self.refresh_icon_wait()
            # self.wait_till_auto_refresh_on()

            # no_match_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().no_match_found_by_xpath())
            # no_match_found_txt = no_match_found.text
            # matches_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)
            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            # no_match_found = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().no_match_found_by_xpath())
            # count = 0
            # while len(no_match_found) == 0 or count > 150:
            #     no_match_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().no_match_found_by_xpath())
            #     time.sleep(web_driver.two_second)
            #     result.append(no_match_found.is_displayed())
            #     count += 1
            #     self.logger.info(f"no match found function count: {count}")
            # result.append(no_match_found_txt in no_match_found[0].text)
            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]

            # result.append(int(max_number_counted) <= int(threshold_data))
            # result.append(self.verify_date(date, month, year, hour, minute, period))
            # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
            print(result)

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_047_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_047_exception.png")
            self.logger.info(f"test_VSJ_047_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_threshold_max_matches_search_image_date_range_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()

            # self.nats_checkbox()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            threshold_data = self.set_thresh_hold_slider()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # matches_found = self.matches_found()
            # if type(matches_found) == bool:
            #     result.append(matches_found)
            # else:
            #     self.logger.info("no matches found")
            # result.append(int(max_number) <= int(threshold_data))
            # result.append(int(max_number) <= int(count_data))

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)
            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))

            # result.append(int(max_number_counted) <= int(threshold_data))
            time.sleep(web_driver.two_second)
            # self.get_start_date()
            # result.append(self.verify_date())
            # result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_048_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_048_exception.png")
            self.logger.info(f"test_VSJ_048_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_and_gender_when_search_with_image_date_range_and_gender(self):
        result = []
        try:
            self.add_image_search()

            # self.nats_checkbox()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")
            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_049_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_049_exception.png")
            self.logger.info(f"test_VSJ_049_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_gender_max_matches_search_with_image_date_range_gender_max_matches(self):
        result = []
        try:
            self.add_image_search()

            # self.nats_checkbox()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")
            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()
            time.sleep(web_driver.two_second)
            # matches_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))
            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            # result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_050_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_050_exception.png")
            self.logger.info(f"test_VSJ_050_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_gender_threshold_search_with_image_date_range_gender_threshold(self):
        result = []
        try:
            self.add_image_search()

            # self.nats_checkbox()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")
            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()
            no_matches_found = self.wait_till_no_match_found()

            # matches_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
            # max_number_counted = 0
            # if len(max_matches) > 0:
            #     max_matches_text = max_matches[0].text
            #     self.logger.info(f"max_matches txt: {max_matches_text}")
            #     if max_matches_text == "MATCHES":
            #         max_number_counted = 0
            #     else:
            #         max_number_counted = max_matches_text.split(" ")[0]

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            # result.append(int(max_number_counted) <= int(threshold_data))

            self.logger.info(f"status: {result}")
            if (False in result) or (not no_matches_found):
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_051_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_051_exception.png")
            self.logger.info(f"test_VSJ_051_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_date_range_gender_threshold_mx_matches_search_image_date_range_gender_threshold_mx_matches(self):
        result = []
        try:
            self.add_image_search()

            # self.nats_checkbox()

            

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")
            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(threshold_data))
            # result.append(int(max_number) <= int(count_data))
            matches_found = self.matches_found()
            if type(matches_found) == bool:
                result.append(matches_found)
            else:
                self.logger.info("no matches found")

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))
            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            # result.append(int(max_number_counted) <= int(threshold_data))
            # result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_052_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_052_exception.png")
            self.logger.info(f"test_VSJ_052_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_and_age_when_search_with_image_date_range_and_age(self):
        result = []
        try:
            self.add_image_search()

            # self.nats_checkbox()

            

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            self.wait_till_auto_refresh_on()
            no_match_found = self.wait_till_no_match_found()
            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            self.logger.info(f"status: {result}")
            if (False in result) and (not no_match_found):
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_053_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_053_exception.png")
            self.logger.info(f"test_VSJ_053_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_age_and_max_matches_when_search_image_date_range_age_and_max_matches(self):
        result = []
        try:
            self.add_image_search()

            # self.nats_checkbox()

            

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(count_data))
            matches_found = self.matches_found()
            if type(matches_found) == bool:
                result.append(matches_found)
            else:
                self.logger.info("no matches found")

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            # result.append(int(max_number_counted) <= int(count_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_054_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_054_exception.png")
            self.logger.info(f"test_VSJ_054_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_range_age_and_threshold_when_search_image_date_range_age_and_threshold(self):
        result = []
        try:
            self.add_image_search()

            # self.nats_checkbox()

            

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            threshold_data = self.set_thresh_hold_slider()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()
            no_match_found = self.wait_till_no_match_found()
            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            # result.append(self.verify_date())
            # result.append(int(max_number_counted) <= int(threshold_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))

            self.logger.info(f"status: {result}")
            if (False in result) and (not no_match_found):
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_055_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_055_exception.png")
            self.logger.info(f"test_VSJ_055_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_age_threshold_max_matches_search_image_date_range_age_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(threshold_data))
            # result.append(int(max_number) <= int(count_data))
            matches_found = self.matches_found()
            if type(matches_found) == bool:
                result.append(matches_found)
            else:
                self.logger.info("no matches found")

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            # result.append(int(max_number_counted) <= int(threshold_data))
            # result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_056_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_056_exception.png")
            self.logger.info(f"test_VSJ_056_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_age_gender_when_search_with_image_date_range_age_and_gender(self):
        result = []
        try:
            self.add_image_search()

            # self.nats_checkbox()

            

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_057_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_057_exception.png")
            self.logger.info(f"test_VSJ_057_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_age_gender_max_matches_search_with_image_date_range_age_gender_max_matches(self):
        result = []
        try:
            self.add_image_search()
            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(count_data))
            matches_found = self.matches_found()
            if type(matches_found) == bool:
                result.append(matches_found)
            else:
                self.logger.info("no matches found")

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))
            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            # result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_058_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_058_exception.png")
            self.logger.info(f"test_VSJ_058_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_age_gender_threshold_search_with_image_date_range_age_gender_threshold(self):
        result = []
        try:
            self.add_image_search()

            # self.nats_checkbox()

            

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(threshold_data))
            matches_found = self.matches_found()
            if type(matches_found) == bool:
                result.append(matches_found)
            else:
                self.logger.info("no matches found")

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))
            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            # result.append(int(max_number_counted) <= int(threshold_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_059_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_059_exception.png")
            self.logger.info(f"test_VSJ_059_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_date_age_gender_threshold_matches_search_image_date_range_age_gender_threshold_matches(self):
        result = []
        try:
            self.add_image_search()

            # self.nats_checkbox()

            

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            self.wait_till_auto_refresh_on()
            no_match_found = self.wait_till_no_match_found()

            # self.refresh_icon_wait()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(count_data))
            # result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            # result.append(int(max_number_counted) <= int(count_data))
            # result.append(int(max_number_counted) <= int(threshold_data))

            self.logger.info(f"status: {result}")
            if (False in result) and (not no_match_found):
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_060_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_060_exception.png")
            self.logger.info(f"test_VSJ_060_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_when_search_with_image_date_range_region(self):
        result = []
        try:
            self.add_image_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            self.select_org_hirarchy_btn()
            self.logger.info("zone data selected")
            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            time.sleep(web_driver.two_second)
            # self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_061_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_061_exception.png")
            self.logger.info(f"test_VSJ_061_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_max_matches_when_search_with_image_date_range_region_max_matches(self):
        result = []
        try:
            self.add_image_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")
            self.select_org_hirarchy_btn()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(count_data))
            # matches_found = self.matches_found()
            # if type(matches_found) == bool:
            #     result.append(matches_found)
            # else:
            #     self.logger.info("no matches found")

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))
            time.sleep(web_driver.two_second)
            # self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            # result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_062_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_062_exception.png")
            self.logger.info(f"test_VSJ_062_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_age_gender_max_matches_search_image_date_region_age_gender_max_matches(self):
        result = []
        try:
            self.add_image_search()

            

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(count_data))
            matches_found = self.matches_found()
            if type(matches_found) == bool:
                result.append(matches_found)
            else:
                self.logger.info("no matches found")

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))
            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            # result.append(int(max_number_counted) <= int(count_data))
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_063_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_063_exception.png")
            self.logger.info(f"test_VSJ_063_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_threshold_max_matches_search_image_date_region_threshold_max_matches(self):
        result = []
        try:
            self.add_image_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            self.select_org_hirarchy_btn()
            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(count_data))
            # result.append(int(max_number) <= int(threshold_data))
            # try:
            #     matches_found = self.matches_found()
            #     print("type(matches_found) : ", type(matches_found))
            #     if type(matches_found) == bool:
            #         result.append(matches_found)
            #     else:
            #         self.logger.info("no matches found")
            # except Exception as ex:
            #     print(ex)
            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))

            time.sleep(web_driver.two_second)
            # self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            # result.append(int(max_number_counted) <= int(count_data))
            # result.append(int(max_number) <= int(threshold_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_064_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_064_exception.png")
            self.logger.info(f"test_VSJ_064_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_gender_when_search_with_image_date_region_and_gender(self):
        result = []
        try:
            self.add_image_search()

            

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_065_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_065_exception.png")
            self.logger.info(f"test_VSJ_065_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_gender_max_matches_search_with_image_date_region_gender_max_matches(self):
        result = []
        try:
            self.add_image_search()

            

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()
            no_match_found = self.wait_till_no_match_found()
            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            # result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if (False in result) and (not no_match_found):
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_066_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_066_exception.png")
            self.logger.info(f"test_VSJ_066_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_gender_threshold_search_with_image_date_region_gender_threshold(self):
        result = []
        try:
            self.add_image_search()

            

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(threshold_data))
            matches_found = self.matches_found()
            if type(matches_found) == bool:
                result.append(matches_found)
            else:
                self.logger.info("no matches found")

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            # result.append(int(max_number_counted) <= int(threshold_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_067_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_067_exception.png")
            self.logger.info(f"test_VSJ_067_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_date_region_gender_threshold_matches_search_image_date_region_gender_threshold_matches(self):
        result = []
        try:
            self.add_image_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(count_data))
            # result.append(int(max_number) <= int(threshold_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            # result.append(int(max_number_counted) <= int(count_data))
            # result.append(int(max_number_counted) <= int(threshold_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_068_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_068_exception.png")
            self.logger.info(f"test_VSJ_068_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_and_age_when_search_with_image_date_region_and_age(self):
        result = []
        try:
            self.add_image_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_region_from_match_list(zone_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_069_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_069_exception.png")
            self.logger.info(f"test_VSJ_069_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_age_max_matches_when_search_with_image_date_region_age_max_matches(self):
        result = []
        try:
            self.add_image_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(count_data))
            matches_found = self.matches_found()
            if type(matches_found) == bool:
                result.append(matches_found)
            else:
                self.logger.info("no matches found")
            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            # result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_070_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_070_exception.png")
            self.logger.info(f"test_VSJ_070_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_age_threshold_when_search_with_image_date_region_age_threshold(self):
        result = []
        try:
            self.add_image_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            threshold_data = self.set_thresh_hold_slider()

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(threshold_data))
            matches_found = self.matches_found()
            if type(matches_found) == bool:
                result.append(matches_found)
            else:
                self.logger.info("no matches found")

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            # result.append(int(max_number_counted) <= int(threshold_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_071_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_071_exception.png")
            self.logger.info(f"test_VSJ_071_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_age_threshold_matches_search_image_date_region_age_threshold_matches(self):
        result = []
        try:
            self.add_image_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(count_data))
            # result.append(int(max_number) <= int(threshold_data))
            matches_found = self.matches_found()
            if type(matches_found) == bool:
                result.append(matches_found)
            else:
                self.logger.info("no matches found")

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            # result.append(int(max_number_counted) <= int(count_data))
            # result.append(int(max_number_counted) <= int(threshold_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_072_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_072_exception.png")
            self.logger.info(f"test_VSJ_072_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_age_gender_when_search_with_image_date_region_age_and_gender(self):
        result = []
        try:
            self.add_image_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_073_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_073_exception.png")
            self.logger.info(f"test_VSJ_073_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_age_gender_matches_search_image_date_region_age_gender_and_matches(
            self):
        result = []
        try:
            self.add_image_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(count_data))
            matches_found = self.matches_found()
            if type(matches_found) == bool:
                result.append(matches_found)
            else:
                self.logger.info("no matches found")

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            # result.append(int(max_number_counted) <= int(count_data))
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_074_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_074_exception.png")
            self.logger.info(f"test_VSJ_074_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_contains_date_region_age_gender_threshold_search_image_date_region_age_gender_threshold(self):
        result = []
        try:
            self.add_image_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(threshold_data))
            matches_found = self.matches_found()
            if type(matches_found) == bool:
                result.append(matches_found)
            else:
                self.logger.info("no matches found")

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]
            max_number_counted = self.max_matches()
            self.logger.info(f"max_number_counted: {max_number_counted}")
            if max_number_counted != "No":
                result.append(int(max_number_counted) <= int(count_data))
            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            # result.append(int(max_number_counted) <= int(threshold_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_075_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_075_exception.png")
            self.logger.info(f"test_VSJ_075_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_vsj_date_region_age_gender_threshold_max_search_image_date_region_age_gender_threshold_max(self):
        result = []
        try:
            self.add_image_search()

            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            start_age = Read_Visitor_Search_jobs_Components().start_age_data_input()
            end_age = Read_Visitor_Search_jobs_Components().end_age_data_input()

            self.select_start_age(start_age)
            self.select_end_age(end_age)

            gender_data = Read_Visitor_Search_jobs_Components().gender_data_input()
            self.select_gender(gender_data)

            threshold_data = self.set_thresh_hold_slider()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()
            # no_match_found = self.wait_till_no_match_found()
            # matches_found = self.d.find_element(By.XPATH,
            #                                     Read_Visitor_Search_jobs_Components()
            #                                     .visitor_search_result_panel_matches_found())
            # max_count = matches_found.text
            # max_number = max_count.split(" ")[0]
            # result.append(int(max_number) <= int(threshold_data))
            # result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            # max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
            #                                   .visitors_search_jobs_panel_max_matches_by_xpath())
            # max_matches_text = max_matches.text
            # max_number_counted = max_matches_text.split(" ")[0]

            time.sleep(web_driver.two_second)
            self.get_start_date()
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.validate_age_matches_list_in_visitor_search_results(start_age, end_age))
            result.append(self.verify_gender_match_list_in_visitors(gender_data))
            # result.append(int(max_number_counted) <= int(threshold_data))
            # result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_076_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_076_exception.png")
            self.logger.info(f"test_VSJ_076_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_for_visitor_search_with_meta_data_single_edge_or_store_selection(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search()

            org_hirarchy_btn_by_xpath = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().zone_by_xpath(), self.d)
            org_hirarchy_btn_by_xpath.click()
            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)
            time.sleep(web_driver.two_second)
            self.get_start_date()
            self.logger.info("start date entered")
            # self.get_end_date()
            self.logger.info("end date entered")
            self.logger.info("date selected.")

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)
            try:
                self.connection_error()
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.click_on_cloud_menu()
                time.sleep(web_driver.two_second)

                self.click_on_visitor_search_jobs_btn()
                time.sleep(web_driver.two_second)

                # result.append(self.verify_date())
                result.append(self.verify_region_from_match_list(zone_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_077_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_077_exception.png")
            self.logger.info(f"test_VSJ_077_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_visitor_search_with_an_image_the_default_match_count_should_be_50(self):
        result = []
        try:
            self.add_image_search()

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            # self.wait_till_auto_refresh_on()
            self.wait_for_visitor_search_result_to_display()
            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)
            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            # self.wait_for_visitor_search_result_to_display()
            matches_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]
            if max_number.isnumeric():
                result.append(int(max_number) <= int(50))
                self.logger.info(f"status: {result}")
                if False in result:
                    self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_078_failed.png")
                    return False
                else:
                    return True
            else:
                self.logger.info(f"No match found displayed.")
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_078_exception.png")
            self.logger.info(f"test_VSJ_078_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_vs_with_image_the_visitor_search_result_should_be_listed_in_descending_order(self):
        result = []
        try:
            self.add_image_search()

            # self.nats_checkbox()

            zone_data = Read_Visitor_Search_jobs_Components().zone_data_input()
            self.select_zone(zone_data)

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            self.click_on_cloud_menu()

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            view_result = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_view_results())
            count = 0
            while len(view_result) == 0 or count > 150:
                view_result = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_view_results())
                time.sleep(web_driver.two_second)
                visitor_search_panel = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_by_xpath())
                if len(visitor_search_panel) > 0:
                    break
                count += 1
                self.logger.info(f"visitor search panel function count: {count}")
            view_result[0].click()
            time.sleep(web_driver.two_second)
            result.append(self.score_list_in_descending_order())

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_079_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_079_exception.png")
            self.logger.info(f"test_VSJ_079_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_view_result_button_is_visible_and_clickable_in_the_visitor_search_jobs_panel(self):
        result = []
        try:
            self.add_image_search()

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            view_result = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_view_results())

            result.append(view_result.is_enabled())

            result.append(view_result.is_displayed())

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_080_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_080_exception.png")
            self.logger.info(f"test_VSJ_080_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitors_search_results_according_to_the_selected_max_match_count(self):
        result = []
        try:
            self.add_image_search()

            count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
            self.select_count(count_data)

            # self.nats_checkbox()

            self.click_on_submit_search_button()
            time.sleep(web_driver.two_second)

            # self.refresh_icon_wait()
            self.wait_till_auto_refresh_on()
            matches_found = self.d.find_element(By.XPATH,
                                                Read_Visitor_Search_jobs_Components()
                                                .visitor_search_result_panel_matches_found())
            max_count = matches_found.text
            max_number = max_count.split(" ")[0]

            result.append(int(max_number) <= int(count_data))

            self.click_on_cloud_menu()
            time.sleep(web_driver.two_second)

            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitors_search_jobs_panel_max_matches_by_xpath())
            max_matches_text = max_matches.text
            max_number_counted = max_matches_text.split(" ")[0]

            result.append(int(max_number_counted) <= int(count_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_081_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_81_exception.png")
            self.logger.info(f"test_VSJ_081_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_visitors_search_results_match_score_it_should_be_in_descending_order(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            view_result = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_view_results())
            view_result.click()

            time.sleep(web_driver.two_second)

            result.append(self.score_list_in_descending_order())

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_082_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_082_exception.png")
            self.logger.info(f"test_VSJ_082_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_that_the_action_button_on_the_visitor_search_jobs_panel_is_visible_and_clickable(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            action_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                .visitor_search_jobs_panel_action_button())
            result.append(action_button.is_displayed())
            result.append(action_button.is_enabled())

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_084_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_084_exception.png")
            self.logger.info(f"test_VSJ_084_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_the_action_dropdown_options_cancel_jobs_delete_jobs_refresh_change_refresh_visible_clickable(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)
            action_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                .visitor_search_jobs_panel_action_button())
            action_button.click()

            cancel_text = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitor_search_jobs_panel_cancel_jobs())
            delete_text = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                              .visitor_search_jobs_panel_delete_jobs())
            refresh_text = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                               .visitor_search_jobs_panel_refresh())
            refresh_rate_text = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                                    .visitor_search_jobs_panel_show_panel_refresh_rate())

            result.append(cancel_text.is_displayed())
            result.append(cancel_text.is_enabled())
            result.append(delete_text.is_displayed())
            result.append(delete_text.is_enabled())
            result.append(refresh_text.is_displayed())
            result.append(refresh_text.is_enabled())
            result.append(refresh_rate_text.is_displayed())
            result.append(refresh_rate_text.is_enabled())

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_085_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_085_exception.png")
            self.logger.info(f"test_VSJ_085_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_view_result_panel_Location_identify_enrollments_track_faces_identify_visitors_visible_clickble(self):
        result = []
        try:
            self.login()
            self.click_on_visitor_search_jobs_btn()
            time.sleep(web_driver.two_second)

            view_result = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().completed_job_view_result_button())
            view_result.click()
            time.sleep(web_driver.two_second)

            location_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_location_by_xpath())
            result.append(location_button.is_enabled())
            result.append(location_button.is_displayed())

            identify_within_enrollments = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_identify_within_enrollments())
            result.append(identify_within_enrollments.is_enabled())
            result.append(identify_within_enrollments.is_displayed())

            # extend_menu = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_extend_menu_by_xpath())
            # result.append(extend_menu.is_enabled())
            # result.append(extend_menu.is_displayed())
            # extend_menu.click()

            # track_faces = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_track_faces_by_xpath())
            # result.append(track_faces.is_enabled())
            # result.append(track_faces.is_displayed())

            identify_within_visitors = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_identify_within_visitors_xpath())
            result.append(identify_within_visitors.is_enabled())
            result.append(identify_within_visitors.is_displayed())

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_086_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_VSJ_086_exception.png")
            self.logger.info(f"test_VSJ_086_exception:  {type(ex).__name__}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    ################################# generic methods ##############################################

    def nats_checkbox(self):
        """
        This function is used to enable and disable NATS
        :return:
        """
        time.sleep(web_driver.two_second)
        NATS_checkbox = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().nats_checkbox_xpath())
        NATS_checkbox.click()
        time.sleep(web_driver.two_second)

    def close_all_panel_one_by_one(self):
        try:
            time.sleep(web_driver.two_second)
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    Read_Visitor_Search_jobs_Components().close_panel_one_by_one_list())
            for i in close_panel_list:
                i.click()
        except Exception as ex:
            print(ex)

    def verify_image_from_match_list(self):
        time.sleep(web_driver.two_second)
        ele = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().image_match_list_by_xpath())
        for e in ele:
            if not e.is_displayed():
                return False
            else:
                return True

    def verify_region_from_match_list(self, zone_data):
        time.sleep(web_driver.two_second)
        ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_search_constraints(), self.d)
        ac_zone_txt = ele.text
        self.logger.info(f"zone test : {ac_zone_txt}")
        ac_zone_txt = ac_zone_txt[-11:]
        self.logger.info(f"actual zone: {ac_zone_txt}")
        self.logger.info(f"expected zone: {zone_data}")
        if zone_data != ac_zone_txt:
            self.logger.info("zone returning False")
            return False
        else:
            self.logger.info("zone returning True")
            return True

        # lower result zone text validation code
        # match_region = self.d.find_elements(By.XPATH,
        #                                     Read_Visitor_Search_jobs_Components().match_region_by_xpath())
        #
        # for x in match_region:
        #     if x.text != zone_data:
        #         result = False
        #         break

    def verify_date(self):
        self.get_date_range_from_json()
        ex_date = self.start_date.split("/")[0]
        ex_date = int(ex_date)
        ex_month = self.start_date.split("/")[1]
        ex_year = self.start_date.split("/")[2]
        ed_date = self.end_date.split("/")[0]
        ed_date = int(ed_date)
        ed_month = self.end_date.split("/")[1]
        ed_year = self.end_date.split("/")[2]
        print(ed_date)
        print(ed_month)
        print(ed_year)
        month_to_mm = {
            "01": "Jan",
            "02": "Feb",
            "03": "Mar",
            "04": "Apr",
            "05": "May",
            "06": "Jun",
            "07": "Jul",
            "08": "Aug",
            "09": "Sep",
            "10": "Oct",
            "11": "Nov",
            "12": "Dec"

        }

        mon = month_to_mm.get(ex_month)
        exp_asser = "{mon} {date}, {year} "
        mon_ed = month_to_mm.get(ed_month)
        exp_asser_2 = "{mon_ed} {date}, {year} "
        exp_asser = exp_asser.format(mon=mon, date=ex_date, year=ex_year)
        exp_asser_2 = exp_asser_2.format(mon_ed=mon_ed, date=ed_date, year=ed_year)
        time.sleep(web_driver.one_second)

        ac_start_date = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().
                                                 visitor_search_jobs_panel_search_constraints(), self.d)
        ac_ass_date = ac_start_date.text
        self.logger.info(f"expected exp_asser: {exp_asser}, in : {ac_ass_date}")
        self.logger.info(f"expected exp_asser2: {exp_asser_2}, in : {ac_ass_date}")
        if exp_asser in ac_ass_date and exp_asser_2 in ac_ass_date:
            return True
        else:
            return False
    # def verify_date(self, date, month, year, hour, minute, period):
    #     time.sleep(web_driver.two_second)
    #     month_to_mm = {
    #         "January": "JAN",
    #         "February": "FEB",
    #         "March": "MAR",
    #         "April": "APR",
    #         "May": "MAY",
    #         "June": "JUN",
    #         "July": "JUL",
    #         "August": "AUG",
    #         "September": "SEP",
    #         "October": "OCT",
    #         "November": "NOV",
    #         "December": "DEC"
    #     }
    #     mon = month_to_mm.get(month)
    #
    #     # exp_asser = "{mon} {date}, {year} {hour}:{minu} {pe}"
    #     exp_asser = "{mon} {date}, {year}"
    #     self.logger.info(f"before format: {exp_asser}")
    #     exp_asser = exp_asser.format(mon=mon, date=date, year=year, hour=int(hour), minu=minute, pe=period)
    #     self.logger.info(f"expected formatted: {exp_asser}")
    #     ac_start_date = web_driver.explicit_wait(self, 10, "XPATH",
    #                              Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_search_constraints(),
    #                              self.d)
    #     ac_ass_date = ac_start_date.text.upper()
    #     ac_ass_date = ac_ass_date[20:]
    #     self.logger.info(f"expected date: {exp_asser}")
    #     self.logger.info(f"actual date: {ac_ass_date}")
    #     if exp_asser in ac_ass_date:
    #         self.logger.info("date returning true")
    #         return True
    #     else:
    #         self.logger.info("date returning false")
    #         return False

    def verify_date_1(self, date, month, year, hour, minute, period):
        time.sleep(web_driver.two_second)
        month_to_mm = {
            "January": "JAN",
            "February": "FEB",
            "March": "MAR",
            "April": "APR",
            "May": "MAY",
            "June": "JUN",
            "July": "JUL",
            "August": "AUG",
            "September": "SEP",
            "October": "OCT",
            "November": "NOV",
            "December": "DEC"
        }
        mon = month_to_mm.get(month)

        # exp_asser = "{mon} {date}, {year} {hour}:{minu} {pe}"
        exp_asser = "{mon} {date}, {year}"
        self.logger.info(f"before format: {exp_asser}")
        exp_asser = exp_asser.format(mon=mon, date=date, year=year, hour=int(hour), minu=minute, pe=period)
        self.logger.info(f"expected formatted: {exp_asser}")
        
        ac_start_date = web_driver.explicit_wait(self, 10, "XPATH",
                                 Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_search_constraints(),
                                 self.d)
        ac_ass_date = ac_start_date.text.upper()
        ac_ass_date = ac_ass_date[20:]
        self.logger.info(f"expected date: {exp_asser}")
        self.logger.info(f"actual date: {ac_ass_date}")
        if exp_asser in ac_ass_date:
            self.logger.info("date returning true")
            return True
        else:
            self.logger.info("date returning false")
            return False

    def close_all_the_panels(self):
        """
        This function is used to close all the visitor search panels
        :return:
        """
        close_icon = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().close_all_visitor_search_panel_by_xpath())
        for x in close_icon:
            x.click()
            time.sleep(web_driver.two_second)

    def matches_found(self):

        matches_found = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
        # self.wait_for_element_to_appear(self, matches_found, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
        count = 0
        while len(matches_found) == 0 or count > 150:
            matches_found = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"matches found function count: {count}")
        if len(matches_found) > 0:
            x = matches_found[0]
            if x.text == Read_Visitor_Search_jobs_Components().matches_found_text():
                self.logger.info("no matches found... ")
                return x.text
            else:
                matches_found = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_matches_found())
                y = matches_found[0]
                time.sleep(web_driver.two_second)
                count_data = Read_Visitor_Search_jobs_Components().matches_count_data_input()
                max_count = y.text
                max_number = max_count.split(" ")[0]
                return int(max_number) <= int(count_data)

    def max_matches(self):
        max_matches = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
        count = 0
        while len(max_matches) == 0 or count > 150:
            max_matches = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitors_search_jobs_panel_max_matches_by_xpath())
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"max matches function count: {count}")
        max_number_counted = 0
        if len(max_matches) > 0:
            max_matches_text = max_matches[0].text
            max_number_counted = max_matches_text.split(" ")[0]
            return max_number_counted
        else:
            self.logger.info("no max match found")
            return max_number_counted

    def select_zone(self, zone):
        """
        This function is used to handle the zone drop-down and select the required options
        :return:
        """
        time.sleep(web_driver.three_second)
        self.explicit_wait(10, "XPATH", Read_Visitor_Search_jobs_Components().zone_name_by_xpath(), self.d)
        zone_ele = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().zone_name_by_xpath())

        for actual_zone in zone_ele:
            if actual_zone.text == zone:
                self.logger.info(f"actual zone: {actual_zone.text}")
                actual_zone.click()
                break

        # zone_ele.click()
        time.sleep(web_driver.two_second)
        zone_text_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().zone_text_list_xpath())
        expected_zone_text = zone.upper()
        self.logger.info(f"expected zone: {expected_zone_text}")
        self.logger.info(f"zone list length: {len(zone_text_list)}")
        try:
            for i in range(len(zone_text_list)):
                actual_zone_text = zone_text_list.__getitem__(i).text
                self.logger.info(f"actual zone: {actual_zone_text}")
                # expected_zone_text = Read_Visitor_Search_jobs_Components().get_zone().upper()
                if expected_zone_text.upper() in actual_zone_text.upper():
                    zone_text_list.__getitem__(i).click()
                    break
            save = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().zone_save_button_xpath())
            self.d.execute_script("arguments[0].click();", save)
            time.sleep(web_driver.two_second)
        except Exception as ex:
            str(ex)
        # zone_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().zone_by_xpath())
        # zone_ele.click()
        # time.sleep(web_driver.one_second
        # root_selection = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().root_selection_xpath())
        # assert root_selection.is_displayed()
        # self.d.execute_script("arguments[0].click();", root_selection)
        # save = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().zone_save_button_xpath())
        # self.d.execute_script("arguments[0].click();", save)

    def select_start_age(self, start_age):
        """
        This function is used to select the start age
        :param start_age:
        :return:
        """
        start_age_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().start_age_by_xpath())
        s = Select(start_age_ele)
        s.select_by_visible_text(start_age)
        time.sleep(web_driver.two_second)

    def select_end_age(self, end_age):
        """
        This function is used to select the end age
        :param end_age:
        :return:
        """
        end_age_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().end_age_by_xpath())
        s = Select(end_age_ele)
        s.select_by_visible_text(end_age)
        time.sleep(web_driver.two_second)

    def validate_age_matches_list(self, start_age, end_age):
        """
        This function is used to validate the age
        :param start_age:
        :param end_age:
        :return:
        """
        time.sleep(web_driver.two_second)
        age_range = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_jobs_panel_search_constraints())
        self.logger.info(f"start age: {start_age}")
        self.logger.info(f"end age: {end_age}")
        self.logger.info(f"age range: {age_range}")
        if start_age in age_range and end_age in age_range:
            return True
        else:
            return False

    def validate_age_matches_list_in_visitor_search_results(self, start_age, end_age):
        """
        This function is used to validate the age
        :param start_age:
        :param end_age:
        :return:
        """
        time.sleep(web_driver.two_second)
        age_range = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_search_constraints())
        age_range = age_range.text
        self.logger.info(f"start age: {start_age}")
        self.logger.info(f"end age: {end_age}")
        self.logger.info(f"age range: {age_range}")
        if start_age in age_range and end_age in age_range:
            return True
        else:
            return False

    def compare_thresh_hold_value_with_score(self):
        """
        This function is used to compare the threshhold value with actual score
        :return:
        """
        slider = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().slider_icon_by_xpath())
        slider_value_str = str(slider.get_attribute("style"))
        slider_value_text = slider_value_str.split(" ")[1].strip()
        slider_value_text = re.sub("[% ;]", "", slider_value_text)

        match_list_score = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().score_by_xpath())
        for ele in match_list_score:
            score = ele.text
            score = int(score.split(".")[1][0:2])
            if not score >= int(slider_value_text):
                return False
            else:
                return True
        pass

    def set_thresh_hold_slider(self):
        """
        This function is used to set the threshold value
        :return:
        """
        slider_pixel = Read_Visitor_Search_jobs_Components().slider_value_data_input()
        slider_pixel_value = int(slider_pixel)

        slider = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().slider_icon_by_xpath())
        action = ActionChains(self.d)
        action.drag_and_drop_by_offset(slider, -80, 0).perform()

        action.drag_and_drop_by_offset(slider, slider_pixel_value, 0).perform()
        return slider_pixel

    def select_count(self, count_data):
        """
        This function is used to select the count from the count dropdown
        :param count_data:
        :return:
        """
        max_match = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().max_of_matches_by_xpath())

        select = Select(max_match)

        select.select_by_visible_text(count_data)
        time.sleep(web_driver.two_second)

    def click_on_submit_search_button(self):
        """
        This function is used to click on the submit search button
        :return:
        """

        submit_btn = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().submit_search_button_by_xpath(), self.d)
        submit_btn.click()
        time.sleep(web_driver.two_second)
        try:
            result_wait = web_driver.explicit_wait(self, 10, "XPATH", "//div[@class='job-progress-container posrel fl disblk cb']", self.d)
            while result_wait.is_displayed():
                time.sleep(web_driver.two_second)
        except Exception as ex:
            pass

    def verify_gender_match_list(self, expected_gender):
        """
        This function is used to the verify te gender with the actual match list
        :param expected_gender:
        :return:
        """
        time.sleep(web_driver.two_second)
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().search_constraints_by_xpath())
        ac_gender_txt = ele.text[20:]
        ele2 = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().no_matches_found())
        self.logger.info(f"actual gender: {ac_gender_txt}, type: {type(ac_gender_txt)}")
        self.logger.info(f"expected gender: {expected_gender.upper()}, type: {type(expected_gender)}")
        if (expected_gender.upper() in ac_gender_txt) or (ele2.is_displayed()):
            return True
        else:
            return False

        # match_gender_list = self.d.find_elements(By.XPATH,
        #                                          Read_Visitor_Search_jobs_Components().matches_gender_by_xpath())
        # ele2 = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().no_matches_found())
        # for ele in match_gender_list:
        #     gender = ele.text
        #     if (expected_gender.upper() not in gender) or (not ele2.is_displayed()):
        #         return False
        #     else:
        #         return True

    def verify_gender_match_list_in_visitors(self, expected_gender):
        """
        This function is used to the verify te gender with the actual match list
        :param expected_gender:
        :return:
        """
        time.sleep(web_driver.two_second)
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components()
                                  .visitor_search_result_panel_search_constraints())
        ac_gender_txt = ele.text
        self.logger.info(f"actual gender: {ac_gender_txt}")
        time.sleep(web_driver.two_second)
        if expected_gender.upper() not in ac_gender_txt:
            return False
        else:
            return True

    def select_gender(self, gender_data):
        """
        This function helps us to select the gender dropdown
        :return:
        """
        gender_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().select_gender_by_xpath())

        s = Select(gender_ele)
        s.select_by_value(gender_data)
        time.sleep(web_driver.two_second)

    def wait_till_no_match_found(self):
        time.sleep(web_driver.two_second)
        auto_refresh_on = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().auto_refresh_on_by_xpath())
        count = 0
        while len(auto_refresh_on) == 0 or count > 150:
            auto_refresh_off = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().auto_refresh_off_by_xpath())
            if len(auto_refresh_off) > 0:
                break
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"auto refresh on function count: {count} ")
            self.logger.info("waiting for auto refresh text on visitor search panel")
        auto_refresh_on = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().auto_refresh_on_by_xpath())
        count = 0
        while auto_refresh_on.is_displayed() or count > 150:
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"auto refresh on function waiting count: {count}")
        time.sleep(web_driver.two_second)
        no_match_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().no_match_found_by_xpath())
        self.logger.info(f"no match found text displayed: {no_match_found.text}, status: {no_match_found.is_displayed()}")
        return no_match_found.is_displayed()

    def wait_till_auto_refresh_on(self):
        auto_refresh_on = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().auto_refresh_on_by_xpath())
        count = 0
        while (len(auto_refresh_on) == 0) or count > 150:
            auto_refresh_off = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().auto_refresh_off_by_xpath())
            if len(auto_refresh_off) > 0:
                break
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"count: {count}")
            self.logger.info("waiting for auto refresh text on visitor search panel")
        auto_refresh_on = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().auto_refresh_on_by_xpath())
        count = 0
        while auto_refresh_on.is_displayed() or count > 150:
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"count: {count}")

    def refresh_icon_wait(self):
        """
        This function is used to wait for a particular period of time until the match has been found
        :return:
        """
        refresh_icon = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().refresh_icon_by_xpath())
        count = 0
        while refresh_icon.is_displayed() or count > 150:
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"refresh icon count: {count}")

    def submitting_icon_wait(self):
        """
        This function is used to wait for a particular period of time until the submitting is not complete
        :return:
        # """
        # submit_icon = self.d.find_element(By.XPATH,
        #                                   Read_Visitor_Search_jobs_Components().submitting_archive_search_wait_icon())
        # while submit_icon.is_displayed():
        #
        pass

    def add_image_search(self):
        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        self.login()
        self.click_on_visitor_search()

        upload_photo = web_driver.explicit_wait(self, 20, "XPATH", Read_Visitor_Search_jobs_Components().photo_upload_container_by_xpath(), self.d)
        upload_photo.click()
        time.sleep(web_driver.two_second)
        file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_1.png"
        # file_path = f"{Path(__file__).parent.parent.parent}\\Test_Data\\img\\img1.png"
        # file_path = f"{os.environ['WORKSPACE']}/Test_Data/img/img1.png"
        # file_path = Path(__file__).parent / "img1.png"
        # script_directory = Path(__file__).parent
        # file_path = script_directory / ".." / ".." / "Test_Data" / "img" / "img1.png"
        ##############################
        # file_path = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Try1\\Test_Data\\img\\img1.png"
        # file_path = 'C:\\Users\\baps\\Pictures\\uim.png'
        # file_path = 'D:\Chrome_Download\img1.png ' #
        time.sleep(web_driver.two_second)
        pyautogui.write(file_path)
        # pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(web_driver.two_second)
        pyautogui.press('enter')
        time.sleep(web_driver.two_second)
        # configure_search = self.d.find_element(By.XPATH,
        #                                        Read_Visitor_Search_jobs_Components().configure_search_by_xpath())
        # configure_search.click()
        # configure_search.click()

    def compare_count_match(self, count_data):
        """
        This function is used to compare the count provided with the actual no. of match count
        :param count_data:
        :return:
        """
        # match_found = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().matches_found_by_xpath())
        # match_found_count = int(match_found.text)

        #
        pass

    def handle_calender_pop_up(self, strategy, date, month, year, hour, minute, req_period):

        # click on the form calendar popup
        if strategy == "from":
            start_check_bx = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().start_date_checkbox_by_xpath(), self.d)
            start_check_bx.click()
            time.sleep(web_driver.two_second)
            self.logger.info("checkbox selected...")
            start_date_txt_bx = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().start_date_by_xpath(), self.d)
            self.d.execute_script("arguments[0].scrollIntoView();", start_date_txt_bx)
            start_date_txt_bx.click()
            self.logger.info("start date selected")
        else:
            # click on the to calendar pop up
            end_check_bx = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().end_date_checkbox_by_xpath(), self.d)
            end_check_bx.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"end_ check box selected: {end_check_bx.is_displayed()}")
            end_date_txt_bx = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().end_date_by_xpath(), self.d)
            self.d.execute_script("arguments[0].scrollIntoView();", end_date_txt_bx)
            end_date_txt_bx.click()
            self.logger.info(f"end date selected: {end_check_bx.is_displayed()}")

        # click on the clock icon
        calender_clock = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().calender_timer_icon_by_xpath(), self.d)
        calender_clock.click()

        time.sleep(3)

        # handle the hour and minute based on the strategy
        if strategy == "from":
            self.calender_handle_hour_minute_from(hour, minute)
        else:
            self.calender_handle_hour_minute_to(hour, minute)

        # select the period am or pm
        period = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().period_by_xpath(), self.d)
        if period.text == req_period:
            print("")
        else:
            period.click()

        # click on the tick icon

        tick_icon = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().calender_tick_icon_by_xpath(), self.d)
        tick_icon.click()

        if strategy == "from":

            start_date_txt_bx = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().start_date_by_xpath(), self.d)
            start_date_txt_bx.click()
        else:
            # click on the to calendar pop up
            start_date_txt_bx = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().end_date_by_xpath(), self.d)
            start_date_txt_bx.click()

        req_month = month
        req_year = year
        month_to_num = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }

        month_year = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().calender_month_year_by_xpath(), self.d)
        ac_month = month_year.text.split(" ")[0]
        ac_year = int(month_year.text.split(" ")[1])

        # click on the back button
        count = 0
        while month_to_num.get(req_month) < month_to_num.get(ac_month) or req_year < ac_year:

            cal_back_button = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().calender_back_button_by_xpath(), self.d)
            if cal_back_button.is_enabled():
                cal_back_button.click()
            time.sleep(1)

            month_year = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().calender_month_year_by_xpath(), self.d)
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])
            count += 1
            self.logger.info(f"month and year function count: {count}")

        # click on the forward button
        count = 0
        while month_to_num.get(req_month) > month_to_num.get(ac_month) or req_year > ac_year:
            # action = ActionChains(self.d)
            # action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
            try:
                cal_back_button = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().calender_forward_button_by_xpath())
                if cal_back_button.is_enabled():
                    cal_back_button.click()
            except Exception as ex:
                title_name = self.d.find_element(By.XPATH, "//a[@title='Close the picker'']")
                title_name.click()
                pass
            time.sleep(1)
            month_year = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])
            count += 1

            self.logger.info(f"month and year function count: {count}")

        time.sleep(web_driver.three_second)
        # click on the required date
        web_driver.explicit_wait(self, 10, "XPATH", "(//td[@class='day' or @class='day weekend' or @class='day active' or @class='day active today' or @class='day today'])[" + str(date) + "]", self.d)
        date = self.d.find_element(By.XPATH, "(//td[@class='day' or @class='day weekend' or @class='day active' or @class='day active today' or @class='day today'])[" + str(date) + "]")
        date.click()
        time.sleep(web_driver.two_second)
        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().calender_tick_icon_by_xpath())
        time.sleep(web_driver.two_second)
        tick_icon.click()
        time.sleep(web_driver.two_second)
        
    def calender_handle_hour_minute_to(self, hour, minute):

        # set the minute
        current_min_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_minute_element_by_xpath(), self.d)
        cur_min = int(current_min_ele.text)
        self.logger.info(f"current minute: {cur_min}")
        while int(cur_min) != int(minute):
            self.logger.info(f"current min: {cur_min} and expected min: {minute}")
            clock_down_button = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().clock_min_down_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", clock_down_button)
            current_min_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_minute_element_by_xpath(), self.d)
            cur_min = int(current_min_ele.text)

        # set the hour
        current_hour_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_hour_ele_by_xpath(), self.d)
        cur_hour = int(current_hour_ele.text)
        self.logger.info(f"current hour: {cur_hour}")
        self.logger.info(f"calender handler hour to : {hour}")
        self.logger.info(f"calender handler minute to : {minute}")
        while int(cur_hour) != int(hour):
            hour_down = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().hour_down_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", hour_down)
            current_hour_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_hour_ele_by_xpath(), self.d)
            cur_hour = int(current_hour_ele.text)

    def calender_handle_hour_minute_from(self, hour, minute):
        # set the hour

        current_hour_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_hour_ele_by_xpath(), self.d)
        cur_hour = int(current_hour_ele.text)
        self.logger.info(f"calender handler hour from : {hour}")
        self.logger.info(f"calender handler minute from : {minute}")
        # decrementHours
        while int(cur_hour) != int(hour):
            hour_down = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().hour_down_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", hour_down)
            current_hour_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_hour_ele_by_xpath(), self.d)
            cur_hour = int(current_hour_ele.text)

        # set the minute
        current_min_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_minute_element_by_xpath(), self.d)
        cur_min = int(current_min_ele.text)
        print(cur_min)
        while int(cur_min) != int(minute):
            clock_up_button = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().clock_min_up_button_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", clock_up_button)
            current_min_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().current_minute_element_by_xpath(), self.d)
            cur_min = int(current_min_ele.text)

    def verify_date_range(self, start_year, end_year):
        month_to_num = {
            "JAN": 1,
            "FEB": 2,
            "MAR": 3,
            "APR": 4,
            "MAY": 5,
            "JUN": 6,
            "JUL": 7,
            "AUG": 8,
            "SEP": 9,
            "OCT": 10,
            "NOV": 11,
            "DEC": 12
        }
        date_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().match_date_list_by_xpath())
        ac_date = int()
        ac_month = int()
        ac_year = int()
        for x in date_list:
            dt = x.text
            b = dt.split(" ")
            ac_year = int(b[2])
        ele2 = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().no_matches_found(), self.d)
        if (start_year <= ac_year <= end_year) or (ele2.is_displayed()):
            return True
        else:
            return False

    def click_on_logout_button(self):
        try:
            time.sleep(web_driver.two_second)
            logout_button = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().logout_btn_by_xpath(), self.d)
            logout_button.click()
            time.sleep(web_driver.two_second)
        except Exception as ex:
            print(ex)

    def check_if_match_is_found(self):
        ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().no_match_found_by_xpath(), self.d)
        if ele.is_displayed():
            return False
        else:
            return True

    def verify_Must_specify_start_and_end_date_for_meta_data_only_search(self):
        ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().start_end_date_validation_msg_verify_xpath(), self.d)
        actual_validation_text = ele.text.lower()
        expected_validation_text = Read_Visitor_Search_jobs_Components().meta_data_without_date_validation_msg().strip().lower()

        time.sleep(web_driver.two_second)
        alert = self.d.switch_to.alert
        error_msg1 = alert.text
        self.logger.info(f"alert error message: {error_msg1}")
        alert.accept()
        if (ele.is_displayed() and actual_validation_text == expected_validation_text) or (error_msg1 == Read_Visitor_Search_jobs_Components().connection_error()):
            return True
        else:
            return False

    def verify_limited_to_30_min_interval_validation(self):
        ele = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().limited_to_30_min_interval_validation())
        actual_validation_text = ele.text.lower()
        expected_validation_text = Read_Visitor_Search_jobs_Components().limited_to_30_meta_data_search_validation().strip().lower()
        print(actual_validation_text)
        print(expected_validation_text)
        self.logger.info(f"actual: {actual_validation_text}")
        self.logger.info(f"expected: {expected_validation_text}")
        if ele.is_displayed() and actual_validation_text == expected_validation_text:
            return True
        else:
            return False

    def verify_max_matches_not_display(self):
        """
        This function is used validate the max matches element
        :return:
        """
        max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().max_of_matches_by_xpath())
        if not max_matches.is_displayed():
            return True
        else:
            return False

    def verify_threshold_not_display(self):
        """
        This function is used validate the threshold element
        :return:
        """
        threshold = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().threshold_slider_by_xpath())
        if not threshold.is_displayed():
            return True
        else:
            return False

    def click_on_visitor_search(self):
        time.sleep(web_driver.two_second)
        visitor_search_btn = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().portal_menu_visitors_search_btn_by_xpath(), self.d)
        visitor_search_btn.click()
        time.sleep(web_driver.two_second)

    def click_on_cloud_menu(self):
        # visitor_search_btn = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().cloud_menu_by_xpath())
        click_on_cloud_menu = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().cloud_menu_by_xpath(), self.d)
        # click_on_cloud_menu.click()
        time.sleep(web_driver.two_second)
        self.d.execute_script("arguments[0].click();", click_on_cloud_menu)
        time.sleep(web_driver.two_second)

    def connection_error(self):
        ele = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().start_end_date_validation_msg_verify_xpath())
        if len(ele) > 0:
            self.logger.info("elements found")
            actual_validation_text = ele[0].text.lower()
            expected_validation_text = Read_Visitor_Search_jobs_Components().meta_data_without_date_validation_msg().strip().lower()
            time.sleep(web_driver.two_second)
            alert = self.d.switch_to.alert
            error_msg1 = alert.text
            alert.accept()
            if (ele.is_displayed() and actual_validation_text == expected_validation_text) or (error_msg1 == Read_Visitor_Search_jobs_Components().connection_error()):
                return True
            else:
                return False
        else:
            self.logger.info("No element found")

    def score_list_in_descending_order(self):

        score_list = self.explicit_wait(20, "XPATH", Read_Visitor_Search_jobs_Components().visitor_search_result_panel_scores(), self.d)
        score_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_scores())
        # count = 0
        #
        # while len(score_list) == 0 or count > 150:
        #     score_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_jobs_Components().visitor_search_result_panel_scores())
        #     time.sleep(web_driver.two_second)
        #     count += 1
        #     self.logger.info(f"score list function count: {count}")

        if len(score_list) > 0:
            score = []
            for x in score_list:
                score.append(x.text.split(" ")[1])
            self.logger.info(f"score: {score}")
            for i in range(len(score) - 1):
                if score[i] < score[i + 1]:
                    self.logger.info("score returning False")
                    return False
                self.logger.info("score returning true")
                return True
        else:
            self.logger.info(f"score list length is {len(score_list)} and score: {score_list}")

    def get_date_range_from_json(self):
        try:
            df_custom_dates = pd.read_json(self.custom_dates_json)
            self.start_date_and_time = list({df_custom_dates['date_range'][0]['start_date']})
            for items in self.start_date_and_time:
                items = items.split(' ')
                self.start_date = items[0]
                self.start_time = items[1]
                self.start_datetime = items[2]
            self.logger.info(f"start date: {self.start_date}{self.start_time}{self.start_datetime}")
            self.end_date_and_time = list({df_custom_dates['date_range'][0]['end_date']})
            for items in self.end_date_and_time:
                items = items.split(' ')
                self.end_date = items[0]
                self.end_time = items[1]
                self.end_datetime = items[2]
            self.logger.info(f"end date: {self.end_date}{self.end_time}{self.end_datetime}")
        except Exception as ex:
            self.logger.error(ex)

    def get_start_date(self):
        try:
            # self.get_date_range_from_json()
            # time.sleep(web_driver.one_second)
            #
            # start_date_calender_box = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().start_date_calender_box_by_xpath(), self.d)
            # start_date_checkbox = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().start_date_checkbox_by_xpath(), self.d)
            # time.sleep(web_driver.one_second)
            # start_date_checkbox.click()
            # start_date_calender_box.click()
            # action = ActionChains(self.d)
            # time.sleep(web_driver.one_second)
            # default_start_date = start_date_calender_box.get_attribute('value')
            # default_start_date = list(default_start_date.split(' '))
            # d_start_date = default_start_date[0]
            # d_start_date = list(d_start_date.split('/'))
            # s_month = d_start_date[0]
            # s_date = d_start_date[1]
            # input_start_date = list(self.start_date.split('/'))
            # input_s_date = input_start_date[0]
            # input_s_month = input_start_date[1]
            # input_s_year = input_start_date[2]
            # status = True
            # if s_month < input_s_month:
            #     while status:
            #         action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
            #         current_date_and_time = start_date_calender_box.get_attribute('value')
            #         current_date_and_time = list(current_date_and_time.split(' '))
            #         current_date = current_date_and_time[0]
            #         current_date = list(current_date.split('/'))
            #         c_date = current_date[1]
            #         c_month = current_date[0]
            #         if c_month == input_s_month and c_date == input_s_date:
            #             action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            #             self.logger.info(F"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
            #             status = False
            # elif s_month > input_s_month:
            #     while status:
            #         action.key_down(Keys.ARROW_LEFT).key_up(Keys.ARROW_LEFT).perform()
            #         current_date_and_time = start_date_calender_box.get_attribute('value')
            #         current_date_and_time = list(current_date_and_time.split(' '))
            #         current_date = current_date_and_time[0]
            #         current_date = list(current_date.split('/'))
            #         c_date = current_date[1]
            #         c_month = current_date[0]
            #         if c_month == input_s_month and c_date == input_s_date:
            #             action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            #             self.logger.info(F"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
            #             status = False
            # else:
            #     if s_date > input_s_date:
            #         while status:
            #             action.key_down(Keys.ARROW_LEFT).key_up(Keys.ARROW_LEFT).perform()
            #             current_date_and_time = start_date_calender_box.get_attribute('value')
            #             current_date_and_time = list(current_date_and_time.split(' '))
            #             current_date = current_date_and_time[0]
            #             current_date = list(current_date.split('/'))
            #             c_date = current_date[1]
            #             c_month = current_date[0]
            #             if c_month == input_s_month and c_date == input_s_date:
            #                 action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            #                 self.logger.info(F"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
            #                 status = False
            #     elif s_date < input_s_date:
            #         while status:
            #             action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
            #             current_date_and_time = start_date_calender_box.get_attribute('value')
            #             current_date_and_time = list(current_date_and_time.split(' '))
            #             current_date = current_date_and_time[0]
            #             current_date = list(current_date.split('/'))
            #             c_date = current_date[1]
            #             c_month = current_date[0]
            #             if c_month == input_s_month and c_date == input_s_date:
            #                 action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            #                 self.logger.info(F"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
            #                 status = False
            #     else:
            #         action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            date = int(Read_Visitor_Search_Components().get_start_date())
            month = str(Read_Visitor_Search_Components().get_start_month())
            year = int(Read_Visitor_Search_Components().get_start_year())
            hour = str(Read_Visitor_Search_Components().get_start_hour())
            minute = Read_Visitor_Search_Components().get_start_minuet()
            period = str(Read_Visitor_Search_Components().get_start_am_pm_period())

            e_month = str(Read_Visitor_Search_Components().get_end_month())
            e_date = int(Read_Visitor_Search_Components().get_end_date())
            e_year = int(Read_Visitor_Search_Components().get_end_year())
            e_hour = str(Read_Visitor_Search_Components().get_end_hour())
            e_minute = Read_Visitor_Search_Components().get_end_minuet()
            e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())

            try:
                Visitor_Search_Module_pom().handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(web_driver.one_second)
                Visitor_Search_Module_pom().handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute,
                                                                   e_period)
                time.sleep(web_driver.three_second)
            except Exception as ex:
                self.logger.info(f"select date range got an exception as: {type(ex).__name__}")
        except Exception as ex:
            self.logger.error("start date method exception")
            self.logger.error(ex)

    def get_end_date(self):
        try:
            self.get_date_range_from_json()
            time.sleep(web_driver.one_second)
            end_date_calender_box = self.d.find_element(By.XPATH,
                                                        Read_Visitor_Search_jobs_Components().end_date_calender_box_by_xpath())
            end_date_checkbox = self.d.find_element(By.XPATH, Read_Visitor_Search_jobs_Components().end_date_checkbox_by_xpath())
            time.sleep(web_driver.one_second)
            end_date_checkbox.click()
            end_date_calender_box.click()
            action = ActionChains(self.d)
            default_end_date = end_date_calender_box.get_attribute('value')
            default_end_date = list(default_end_date.split(' '))
            d_end_date = default_end_date[0]
            d_end_date = list(d_end_date.split('/'))
            e_month = d_end_date[0]
            e_date = d_end_date[1]
            input_end_date = list(self.end_date.split('/'))
            input_e_date = input_end_date[0]
            input_e_month = input_end_date[1]
            input_e_year = input_end_date[2]
            status = True
            if e_month < input_e_month:
                while status:
                    action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
                    current_date_and_time = end_date_calender_box.get_attribute('value')
                    current_date_and_time = list(current_date_and_time.split(' '))
                    current_date = current_date_and_time[0]
                    current_date = list(current_date.split('/'))
                    c_date = current_date[1]
                    c_month = current_date[0]
                    if c_month == input_e_month and c_date == input_e_date:
                        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                        self.logger.info(F"End date selected as:- {input_e_date}/{input_e_month}/{input_e_year}")
                        status = False
            elif e_month > input_e_month:
                while status:
                    action.key_down(Keys.ARROW_LEFT).key_up(Keys.ARROW_LEFT).perform()
                    current_date_and_time = end_date_calender_box.get_attribute('value')
                    current_date_and_time = list(current_date_and_time.split(' '))
                    current_date = current_date_and_time[0]
                    current_date = list(current_date.split('/'))
                    c_date = current_date[1]
                    c_month = current_date[0]
                    if c_month == input_e_month and c_date == input_e_date:
                        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                        self.logger.info(F"End date selected as:- {input_e_date}/{input_e_month}/{input_e_year}")
                        status = False
            elif e_month == input_e_month:
                if e_date > input_e_date:
                    while status:
                        action.key_down(Keys.ARROW_LEFT).key_up(Keys.ARROW_LEFT).perform()
                        current_date_and_time = end_date_calender_box.get_attribute('value')
                        current_date_and_time = list(current_date_and_time.split(' '))
                        current_date = current_date_and_time[0]
                        current_date = list(current_date.split('/'))
                        c_date = current_date[1]
                        c_month = current_date[0]
                        if c_month == input_e_month and c_date == input_e_date:
                            action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                            self.logger.info(F"End date selected as:- {input_e_date}/{input_e_month}/{input_e_year}")
                            status = False
                elif e_date < input_e_date:
                    while status:
                        action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
                        current_date_and_time = end_date_calender_box.get_attribute('value')
                        current_date_and_time = list(current_date_and_time.split(' '))
                        current_date = current_date_and_time[0]
                        current_date = list(current_date.split('/'))
                        c_date = current_date[1]
                        c_month = current_date[0]
                        if c_month == input_e_month and c_date == input_e_date:
                            action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                            self.logger.info(F"End date selected as:- {input_e_date}/{input_e_month}/{input_e_year}")
                            status = False
                else:
                    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        except Exception as ex:
            self.logger.error("end date method exception")
            self.logger.error(ex)

    def select_org_hirarchy_btn(self):
        try:
            time.sleep(web_driver.one_second)
            org_hirarchy_btn_by_xpath = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_jobs_Components().zone_by_xpath(), self.d)
            self.logger.info(f"org hirarchy btn visible: {org_hirarchy_btn_by_xpath.is_displayed()}")
            org_hirarchy_btn_by_xpath.click()
            time.sleep(web_driver.two_second)
        except Exception as ex:
            self.logger.info(f"select org hirarchy btn: {ex.args}")
