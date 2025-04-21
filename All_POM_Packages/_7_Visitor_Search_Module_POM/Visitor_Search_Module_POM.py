from datetime import datetime

import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

from All_Config_Packages._18_Reporting_Module_Config_Files.Reporting_Read_INI import Reporting_read_ini
from Base_Package.Login_Logout_Ops import login, logout
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from pathlib import Path
import pyautogui
from selenium.webdriver import ActionChains, Keys
from All_Config_Packages._7_Visitor_Search_Module_Config_Files.Visitor_Search_Read_INI import \
    Read_Visitor_Search_Components


class Visitor_Search_Module_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()

    def __init__(self):
        self.end_datetime = self.end_time = self.end_date = self.end_date_and_time = self.start_am_pm = \
            self.start_age = self.age_bucket = None
        self.start_time = self.start_date = self.start_date_and_time = self.groups = self.zones = self.end_age = None
        self.custom_dates_json = \
            f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\7_Visitor_Search_Module\\Data_From_JSON\\custom_dates_json.json"

    # ************* Visitor Search Filter Test Cases ****************

    # def login_before(self):
    # 
    #     try:
    #         self.d.get(Read_Portal_Menu_Components().get_url())
    # 
    #         username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
    #         username.send_keys(Read_Portal_Menu_Components().get_username())
    #         password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
    #         password.send_keys(Read_Portal_Menu_Components().get_password())
    #         login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
    #         self.d.execute_script("arguments[0].click();", login_btn)
    #     except Exception as ex:
    #         print(ex)

    # def wait_for_element_to_appear(self, element_list, xpath):
    #     count = 0
    #     if len(element_list) == 0:
    #         while len(element_list) == 0 or count == 10:
    #             element_list = self.d.find_elements(By.XPATH, xpath)
    #             time.sleep(web_driver.one_second)
    #             if len(element_list) > 0:
    #                 self.logger.info("element is visible...")
    #                 return element_list[0]
    #             else:
    #                 self.logger.info("waiting for element...")
    #             count += 1
    #             self.logger.info(f"wait count: {count}")
    #     else:
    #         self.logger.info(f"element length: {len(element_list)}")
    #         return element_list[0]

    def click_on_visitor_search(self):
        time.sleep(web_driver.one_second)
        self.logger.info("going to visitor search...")
        visitor_search_btn = web_driver.explicit_wait(self, 10, "XPATH",
                                                      Read_Visitor_Search_Components().portal_menu_visitors_search_btn_by_xpath(),
                                                      self.d)
        if visitor_search_btn:
            visitor_search_btn.click()
        # self.d.execute_script("arguments[0].click();", visitor_search_btn)
        time.sleep(web_driver.two_second)
        self.logger.info("waiting for search panel to appear...")

    def login(self):
        login().login_to_cloud_if_not_done(self.d)
        # login().login_to_localhost_if_not_done()
        # if self.d.title == "" or self.d.find_element(By.ID, Read_Visitor_Search_Components().get_loginButton()).is_displayed():
        #     login().login_to_cloud_if_not_done(self.d)
        #
        #     time.sleep(web_driver.two_second)

    ############################ Visitor Search with image using NATS (Demographics Enabled) #######################

    def Verify_Visitor_search_with_no_criteria_selection_should_display_error_message_above_search_menu_as_Error_Meta_data_only_search_should_target_a_single_store(self):
        try:
            result = []
            self.logger.info("********** TC_TC_Visitor_Search_059 started ********")
            login().login_to_cloud_if_not_done(self.d)

            self.click_on_visitor_search()
            time.sleep(web_driver.one_second)
            self.logger.info("moving on search...")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button...")
            time.sleep(web_driver.one_second)
            self.logger.info("waiting ...")
            x = self.verify_must_specify_start_date_for_metadata_only_search_meta_data_only_search_should_target_a_single_store()
            self.logger.info(f"X: {x}")
            time.sleep(web_driver.one_second)
            result.append(x)
            self.logger.info(f"status: {result}")
            if False in result:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Visitor_Search_059.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_059_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_059_exception.png")
            self.logger.info(f"TC_Visitor_Search_059_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_region_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("* test_TC_VS_002 *")
            self.logger.info("* test_TC_VS_117 *")
            self.logger.info("* test_TC_VS_034 *")
            self.logger.info("***************** test_TC_VS_002 ***************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.logger.info("Region selected...")
            self.click_on_submit_search_button()
            self.logger.info("Click on submit button...")
            result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_002())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_002_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_002_exception.png")
            self.logger.info(f"visitor_search_with_region_criteria_with_NATS_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    # def visitor_search_with_gender_criteria_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_035 *")
    #         self.logger.info("******************* test_TC_VS_003 *********************")
    #         login().login_to_cloud_if_not_done(self.d)
    #         self.click_on_visitor_search()
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         # self.nats_checkbox()
    #         self.click_on_submit_search_button()
    #         result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_003())
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_003_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         print(ex)
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_003_exception.png")
    #         self.logger.info(f"visitor_search_with_gender_criteria_with_NATS_exception:  {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_region_and_gender_criteria_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_036 *")
    #         self.logger.info("******************* test_TC_VS_004 *********************")
    #         login().login_to_cloud_if_not_done(self.d)
    #         self.click_on_visitor_search()
    #
    #         zone_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(zone_data)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_002())
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(
    #                 f"{self.screenshots_path}\\test_TC_VS_004_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_004_Exception.png")
    #         self.logger.info(f"visitor_search_with_region_and_gender_criteria_with_NATS_exception:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_age_criteria_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_037 *")
    #         self.logger.info("****************** test_TC_VS_005 ***********************")
    #         login().login_to_cloud_if_not_done(self.d)
    #         self.click_on_visitor_search()
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #
    #         self.select_start_age(start_age)
    #
    #         self.select_end_age(end_age)
    #
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_001())
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(
    #                 f"{self.screenshots_path}\\test_TC_VS_005_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_005_Exception.png")
    #         self.logger.info(f"visitor_search_with_age_criteria_with_NATS_exception:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_region_and_age_criteria_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_038 *")
    #         self.logger.info("******************* test_TC_VS_006 ********************")
    #         login().login_to_cloud_if_not_done(self.d)
    #         self.click_on_visitor_search()
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #
    #         self.select_start_age(start_age)
    #
    #         self.select_end_age(end_age)
    #
    #         zone_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(zone_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_002())
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_006_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_006_Exception.png")
    #         self.logger.info(f"visitor_search_with_region_and_age_criteria_with_NATS_failed:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_age_and_gender_criteria_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_039 *")
    #         self.logger.info("*********************** test_TC_VS_007 *********************")
    #         login().login_to_cloud_if_not_done(self.d)
    #         self.click_on_visitor_search()
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #
    #         self.select_start_age(start_age)
    #
    #         self.select_end_age(end_age)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_001())
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_007_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_007_Exception.png")
    #         self.logger.info(f"visitor_search_with_age_and_gender_criteria_with_NATS_failed:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_region_age_and_gender_criteria_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_040 *")
    #         self.logger.info("***************** test_TC_VS_008 ********************")
    #         login().login_to_cloud_if_not_done(self.d)
    #         self.click_on_visitor_search()
    #         # self.nats_checkbox()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_001())
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_008_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         print(ex)
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_008_exception.png")
    #         self.logger.info(f"visitor_search_with_region_age_and_gender_criteria_with_NATS_failed:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()

    def visitor_search_with_only_date_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("* test_TC_VS_121 *")
            self.logger.info("* test_TC_VS_041 *")
            self.logger.info("******************** test_TC_VS_009 *********************")
            login().login_to_cloud_if_not_done(self.d)
            self.d.refresh()
            time.sleep(web_driver.two_second)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            start_date_checkbox = web_driver.explicit_wait(self, 10, "XPATH",
                                                           Read_Visitor_Search_Components().vs_start_date_check_bx(),
                                                           self.d)
            start_date_checkbox = web_driver.explicit_wait_for_stale_element(self, 10, "XPATH",
                                                                             Read_Visitor_Search_Components().vs_start_date_check_bx(),
                                                                             self.d)
            start_date_checkbox.click()
            time.sleep(web_driver.one_second)
            end_date_checkbox = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().vs_end_date_check_bx())
            end_date_checkbox = web_driver.explicit_wait_for_stale_element(self, 10, "XPATH",
                                                                           Read_Visitor_Search_Components().vs_end_date_check_bx(),
                                                                           self.d)
            time.sleep(web_driver.one_second)
            end_date_checkbox.click()
            time.sleep(web_driver.one_second)
            # self.get_start_date()
            self.logger.info("start_date selected")
            # # self.get_end_date()
            self.logger.info("end_date selected")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_001())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_VS_009_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_009_exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed:{ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def verify_possible_match_dates_are_in_ascending_order(self):
        try:
            result = []
            time.sleep(web_driver.one_second)
            date = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().dates_on_possible_matches_found_by_xpath())
            i = 0
            for i in range(len(date) - 1):
                date_string = date[i]
                date_format = "%b %d, %Y %I:%M %p"  # Format for the input date string

                # Convert string to datetime object
                dt = datetime.strptime(date_string, date_format)

                # Convert to epoch time (timestamp)
                epoch_time = dt.timestamp()

                self.logger.info("Epoch Time:", epoch_time)

            time.sleep(web_driver.one_second)
            # if epoch_time[i] <= epoch_time[i + 1]:
            #     # self.logger.info(f"{lesser} is lesser.")
            #     result.append(True)
            # else:
            #     result.append(False)
            return result

        except Exception as ex:
            self.logger.info(f"verify_possible_match_dates_are_in_ascending_order got an exception as: {ex}")

    def verify_index_scores_are_in_descending_order(self):
        try:
            result = []
            time.sleep(web_driver.one_second)
            iscore = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().index_score_on_possible_matches_found_by_xpath())
            for i in range(len(iscore)-1):
                if iscore[i].text >= iscore[i+1].text:
                    self.logger.info(f"{iscore[i].text} is greater than {iscore[i+1].text}")
                    result.append(True)
                else:
                    result.append(False)
            time.sleep(web_driver.one_second)
            return result

        except Exception as ex:
            self.logger.info(f"verify_index_scores_are_in_descending_order got an exception as: {ex}")

    def Verify_visitor_search_with_Date_range_and_Org_Hierarch_Selection_should_list_the_visitors_in_selected_date_range_and_belongs_to_selected_Org_Hierarchy_Selection_sorted_by_date_time_in_ascending_order_(self):
        try:
            result = []
            self.logger.info("********** TC_Visitor_Search_069 started ********")
            login().login_to_cloud_if_not_done(self.d)

            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
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
                self.logger.info(f"select date range got an exception as: {ex}")
            # self.get_start_date()
            # self.logger.info("get_start_date executed")
            # # self.get_end_date()
            # self.logger.info("get_end_date executed")
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.logger.info("select_zone executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            time.sleep(web_driver.two_second)
            x = self.verify_image_from_match_list()
            self.logger.info(f"Returned: {x}")
            if False in x:
                result.append(False)
            else:
                result.append(True)
            # result.append(x)
            self.verify_date()
            self.verify_region_from_match_list(zone_data)
            y = self.verify_possible_match_dates_are_in_ascending_order()
            self.logger.info(f"Returned: {y}")
            if False in y:
                result.append(False)
            else:
                result.append(True)
            # result.append(y)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {result}")
            if False in result:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Visitor_Search_069.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_069_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_069_exception.png")
            self.logger.info(f"TC_Visitor_Search_069_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    # def visitor_search_with_only_date_and_gender_criteria_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_043 *")
    #         self.logger.info("******************* test_TC_VS_011 ******************")
    #         login().login_to_cloud_if_not_done(self.d)
    #         self.click_on_visitor_search()
    #         self.get_start_date()
    #         # self.get_end_date()
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #         result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_001())
    #
    #         if False in result:
    #             self.d.save_screenshot("{self.screenshots_path}\\test_TC_VS_011_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_011_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_and_gender_criteria_with_NATS_exception:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_date_region_and_age_range_criteria(self):
    #     result = []
    #     try:
    #         login().login_to_cloud_if_not_done(self.d)
    #         self.click_on_visitor_search()
    #         date = int(Read_Visitor_Search_Components().meta_data_start_date())
    #         month = str(Read_Visitor_Search_Components().meta_data_start_month())
    #         year = int(Read_Visitor_Search_Components().meta_data_start_year())
    #         hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
    #         minute = str(Read_Visitor_Search_Components().meta_data_start_minuet())
    #         period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
    #         e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
    #         e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
    #         e_minute = str(Read_Visitor_Search_Components().meta_data_end_minuet())
    #         e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #
    #         except Exception as ex:
    #             print(ex)
    #
    #         zone_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(zone_data)
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_region_from_match_list(zone_data))
    #         result.append(self.verify_date())
    #         # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #
    #         if False in result:
    #             self.d.save_screenshot(
    #                 f"{self.screenshots_path}\\visitor_search_with_only_date_criteria_with_NATS_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}"
    #                                f"\\visitor_search_with_only_date_criteria_with_NATS_failed.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_date_and_region_and_gender_criteria_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_044 *")
    #         self.logger.info("******************* test_TC_VS_012 ***********************")
    #         login().login_to_cloud_if_not_done(self.d)
    #         self.click_on_visitor_search()
    #         date = int(Read_Visitor_Search_Components().meta_data_start_date())
    #         month = str(Read_Visitor_Search_Components().meta_data_start_month())
    #         year = int(Read_Visitor_Search_Components().meta_data_start_year())
    #         hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
    #         minute = Read_Visitor_Search_Components().meta_data_start_minuet()
    #         period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
    #         e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
    #         e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
    #         e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #
    #         except Exception as ex:
    #             print(ex)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #
    #         zone_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(zone_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #         time.sleep(web_driver.one_second)
    #         self.logger.info("checking images...")
    #         web_driver.implicit_wait(self, web_driver.one_second, self.d)
    #         # images_displayed = self.verify_image_from_match_list()
    #         # self.logger.info("images displayed..")
    #         # result.append(images_displayed)
    #         # result.append(self.verify_region_from_match_list(zone_data))
    #         # result.append(self.verify_date())
    #         # # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #         # result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_001())
    #
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_012_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_012_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_date_and_age_criteria_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_045 *")
    #         self.logger.info("**************** test_TC_VS_013 ********************")
    #         login().login_to_cloud_if_not_done(self.d)
    #         self.click_on_visitor_search()
    #         date = int(Read_Visitor_Search_Components().meta_data_start_date())
    #         month = str(Read_Visitor_Search_Components().meta_data_start_month())
    #         year = int(Read_Visitor_Search_Components().meta_data_start_year())
    #         hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
    #         minute = Read_Visitor_Search_Components().meta_data_start_minuet()
    #         period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
    #         e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
    #         e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
    #         e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #
    #         except Exception as ex:
    #             print(ex)
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         # result.append(self.verify_date())
    #         # # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #         result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_001())
    #
    #         if False in result:
    #             self.d.save_screenshot("{self.screenshots_path}\\test_TC_VS_013_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_013_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_date_region_and_age_range_criteria_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_046 *")
    #         self.logger.info("***************** test_TC_VS_014 ********************")
    #         login().login_to_cloud_if_not_done(self.d)
    #         self.click_on_visitor_search()
    #         date = int(Read_Visitor_Search_Components().meta_data_start_date())
    #         month = str(Read_Visitor_Search_Components().meta_data_start_month())
    #         year = int(Read_Visitor_Search_Components().meta_data_start_year())
    #         hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
    #         minute = Read_Visitor_Search_Components().meta_data_start_minuet()
    #         period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
    #         e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
    #         e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
    #         e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #
    #         except Exception as ex:
    #             print(ex)
    #
    #         zone_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(zone_data)
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         # result.append(self.verify_region_from_match_list(zone_data))
    #         # result.append(self.verify_date())
    #         # # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #         result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_001())
    #
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_014_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_014_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_date_age_and_gender_criteria_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_047 *")
    #         self.logger.info("************************ test_TC_VS_015 *********************")
    #         login().login_to_cloud_if_not_done(self.d)
    #         self.click_on_visitor_search()
    #         date = int(Read_Visitor_Search_Components().meta_data_start_date())
    #         month = str(Read_Visitor_Search_Components().meta_data_start_month())
    #         year = int(Read_Visitor_Search_Components().meta_data_start_year())
    #         hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
    #         minute = str(Read_Visitor_Search_Components().meta_data_start_minuet())
    #         period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
    #         e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
    #         e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
    #         e_minute = str(Read_Visitor_Search_Components().meta_data_end_minuet())
    #         e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #
    #         except Exception as ex:
    #             print(ex)
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         # result.append(self.verify_date())
    #         # # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #         # result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_001())
    #
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_015_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_015_exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_date_region_age_range_and_gender_criteria_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_048 *")
    #         self.logger.info("************* test_TC_VS_016 *******************")
    #         login().login_to_cloud_if_not_done(self.d)
    #         self.click_on_visitor_search()
    #         date = int(Read_Visitor_Search_Components().meta_data_start_date())
    #         month = str(Read_Visitor_Search_Components().meta_data_start_month())
    #         year = int(Read_Visitor_Search_Components().meta_data_start_year())
    #         hour = str(Read_Visitor_Search_Components().meta_data_start_hour())
    #         minute = Read_Visitor_Search_Components().meta_data_start_minuet()
    #         period = str(Read_Visitor_Search_Components().meta_data_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().meta_data_end_month())
    #         e_date = int(Read_Visitor_Search_Components().meta_data_end_date())
    #         e_year = int(Read_Visitor_Search_Components().meta_data_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().meta_data_end_hour())
    #         e_minute = Read_Visitor_Search_Components().meta_data_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().meta_data_end_am_pm_period())
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #
    #         except Exception as ex:
    #             print(ex)
    #
    #         org_hirarchy_btn = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().zone_by_xpath())
    #         org_hirarchy_btn.click()
    #         zone_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(zone_data)
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #
    #         self.select_gender(gender_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         # result.append(self.verify_region_from_match_list(zone_data))
    #         # result.append(self.verify_date())
    #         # # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #         # result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_001())
    #
    #         print(result)
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_016_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         print(ex)
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_016_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()

    ################ Visitor Search with Image and Metadata with Nats (Demographics Enabled) #######################

    def wait_for_visitor_search_result_to_display(self):
        try:
            time.sleep(web_driver.two_second)
            visitor_search_complete = web_driver.explicit_wait(self, 60, "XPATH",
                                                               Read_Visitor_Search_Components().visitor_search_complete_banner_by_xpath(),
                                                               self.d)
            if visitor_search_complete.is_displayed():
                self.logger.info(f"****************** {visitor_search_complete.text} banner displayed...")
                time.sleep(web_driver.two_second)
            else:
                self.logger.info("Visitor Search Not Completed.")
        except Exception as ex:
            self.logger.info(f"No match found {ex.args}")

    def Verify_visitor_search_with_image_only_should_list_the_matching_visitors_with_image_sorted_by_Index_Score_in_descending_order_best_to_worst(self):
        try:
            result = []
            self.logger.info("********** TC_Visitor_Search_080 started ********")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            self.add_image_search()
            self.logger.info("add_image_search executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            x = self.verify_image_from_match_list()
            self.logger.info(f"Returned: {x}")
            result.append(x)
            y = self.verify_possible_match_dates_are_in_ascending_order()
            self.logger.info(f"Returned: {y}")
            result.append(y)
            # self.verify_index_scores_are_in_descending_order()
            self.logger.info(f"status: {result}")
            if False in result:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Visitor_Search_080_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_080_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_080_exception.png")
            self.logger.info(f"TC_Visitor_Search_080_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_and_max_match_with_NATS_criteria(self):
        result = []
        try:
            self.logger.info("* test_TC_VS_130 *")
            self.logger.info("******************* test_TC_VS_050 ********************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            self.add_image_search()
            self.logger.info("add_image_search executed")
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.logger.info("select_count executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_image_from_match_list())
            result.append(self.compare_count_match(count_data))
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_050_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_050_exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_and_thresh_hold_with_NATS_criteria(self):
        result = []
        try:
            self.logger.info("* test_TC_VS_131 *")
            self.logger.info("************* test_TC_VS_051 *********************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.add_image_search()
            self.logger.info("add_image_search executed")
            self.set_thresh_hold_slider()
            self.logger.info("set_thresh_hold_slider executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_image_from_match_list())
            result.append(self.compare_thresh_hold_value_with_score())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_051_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_051_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_visitor_search_with_image_Threshold_and_Max_number_of_Matches_should_list_the_matching_visitors_with_image_having_threshold_more_than_or_equal_to_search_threshold_Search_result_should_contain_selected_count_of_matching_visitors_and_sorted_by_Index_Score_in_descending_order_best_to_worst(self):
        try:
            result = []
            self.logger.info("********** TC_Visitor_Search_089 started ********")
            login().login_to_cloud_if_not_done(self.d)

            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            self.add_image_search()
            self.logger.info("add_image_search executed")
            self.set_thresh_hold_slider()
            self.logger.info("set_thresh_hold_slider executed")
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.logger.info("select_count executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_image_from_match_list())
            result.append(self.compare_thresh_hold_value_with_score())
            result.append(self.compare_count_match(count_data))
            self.verify_index_scores_are_in_descending_order()
            self.logger.info(f"status: {result}")
            if False in result:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Visitor_Search_089.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_089_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_089_exception.png")
            self.logger.info(f"TC_Visitor_Search_089_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    # def visitor_search_with_image_and_gender_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_053 *")
    #         self.logger.info("******************* test_TC_VS_019 ******************")
    #         self.add_image_search()
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.verify_gender_match_list(gender_data))
    #
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_019_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_019_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_gender_and_max_count_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("****************** test_TC_VS_054 ******************")
    #         self.add_image_search()
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.compare_count_match(count_data))
    #
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_054_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_054_exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_gender_and_thresh_hold_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("*************** test_TC_VS_055 ******************")
    #         self.add_image_search()
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #
    #         self.set_thresh_hold_slider()
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         # x = self.verify_image_from_match_list()
    #         # web_driver.implicit_wait(self, web_driver.one_second, self.d)
    #         # self.logger.info(f"images displayed: {x}")
    #         # result.append(x)
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_055_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_055_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_gender_thresh_hold_and_max_count_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("******************** test_TC_VS_056 **********************")
    #         self.add_image_search()
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #
    #         self.set_thresh_hold_slider()
    #
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.compare_count_match(count_data))
    #
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_056_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_056_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_and_age_range_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_057 *")
    #         self.logger.info("*********************** test_TC_VS_021 ******************")
    #         self.add_image_search()
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_021_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_021_exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_age_range_and_max_match_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("***************** test_TC_VS_058 ************************")
    #         self.add_image_search()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #
    #         result.append(self.compare_count_match(count_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_058_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_058_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_age_range_and_thresh_hold_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("****************** test_TC_VS_059 *****************")
    #         self.add_image_search()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #
    #         self.set_thresh_hold_slider()
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.compare_thresh_hold_value_with_score())
    #
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_059_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_059_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_age_range_and_max_matches_thresh_hold_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("******************* test_TC_VS_060 ****************************")
    #         self.add_image_search()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #
    #         self.set_thresh_hold_slider()
    #         # self.nats_checkbox()
    #         self.click_on_submit_search_button()
    #
    #         # if self.check_if_match_is_found():
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.compare_count_match(count_data))
    #
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_060_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_060_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_age_range_and_gender_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("**************** test_TC_VS_061 ***********************")
    #         self.add_image_search()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.verify_gender_match_list(gender_data))
    #
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_061_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_061_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_age_range_gender_and_max_matches_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("********************* test_TC_VS_062 ***********************")
    #         self.add_image_search()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.compare_count_match(count_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_062_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_062_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_age_range_gender_and_thresh_hold_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("********************** test_TC_VS_063 ********************")
    #         self.add_image_search()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         self.set_thresh_hold_slider()
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_063_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_063_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_age_range_gender_thresh_hold_and_max_matches_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("******************* test_TC_VS_064 ******************")
    #         self.add_image_search()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         self.set_thresh_hold_slider()
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.compare_count_match(count_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_064_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_064_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()

    def visitor_search_with_image_and_region_with_NATS_criteria(self):
        result = []
        try:
            self.logger.info("* test_TC_VS_133 *")
            self.logger.info("* test_TC_VS_065 *")
            self.logger.info("***************** test_TC_VS_018 *********************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            self.add_image_search()
            self.logger.info("add_image_search executed")
            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)
            self.logger.info("select_zone executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_image_from_match_list())
            result.append(self.verify_region_from_match_list(region_data))
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_018_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_018_exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception:{ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_region_and_max_match_with_NATS_criteria(self):
        result = []
        try:
            self.logger.info("* test_TC_VS_134 *")
            self.logger.info("***************** test_TC_VS_066 **************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            self.add_image_search()
            self.logger.info("add_image_search executed")
            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)
            self.logger.info("select_zone executed")
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.logger.info("select_count executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_image_from_match_list())
            result.append(self.verify_region_from_match_list(region_data))
            result.append(self.compare_count_match(count_data))
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_066_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_066_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception : {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_region_and_thresh_hold_with_NATS_criteria(self):
        result = []
        try:
            self.logger.info("* test_TC_VS_135 *")
            self.logger.info("******************* test_TC_VS_067 **************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            self.add_image_search()
            self.logger.info("add_image_search executed")
            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)
            self.logger.info("select_zone executed")
            self.set_thresh_hold_slider()
            self.logger.info("set_thresh_hold_slider executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_image_from_match_list())
            result.append(self.verify_region_from_match_list(region_data))
            result.append(self.compare_thresh_hold_value_with_score())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_067_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_067_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed:{ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_region_thresh_hold_and_max_count_with_NATS_criteria(self):
        result = []
        try:
            self.logger.info("* test_TC_VS_136 *")
            self.logger.info("**************** test_TC_VS_068 *********************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            self.add_image_search()
            self.logger.info("add_image_search executed")
            region_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(region_data)
            self.logger.info("select_zone executed")
            self.set_thresh_hold_slider()
            self.logger.info("set_thresh_hold_slider executed")
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.logger.info("select_count executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_image_from_match_list())
            result.append(self.compare_count_match(count_data))
            result.append(self.verify_region_from_match_list(region_data))
            result.append(self.compare_thresh_hold_value_with_score())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_068_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_068_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception : {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    # def visitor_search_with_image_region_and_gender_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_069 *")
    #         self.logger.info("******************* test_TC_VS_020 ****************")
    #         self.add_image_search()
    #
    #         region_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(region_data)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.verify_gender_match_list(gender_data))
    #         time.sleep(web_driver.one_second)
    #         result.append(self.verify_region_from_match_list(region_data))
    #         # result.append(self.compare_thresh_hold_value_with_score())
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_020_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_020_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_region_gender_and_max_count_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("******************* test_TC_VS_070 *******************")
    #         self.add_image_search()
    #
    #         region_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(region_data)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         self.verify_gender_match_list(gender_data)
    #         self.verify_image_from_match_list()
    #
    #         result.append(self.verify_region_from_match_list(region_data))
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.compare_count_match(count_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot("{self.screenshots_path}\\test_TC_VS_070_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_070_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_region_gender_and_thresh_hold_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("***************** test_TC_VS_071 **********************")
    #         self.add_image_search()
    #
    #         region_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(region_data)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #
    #         self.set_thresh_hold_slider()
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.verify_region_from_match_list(region_data))
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_071_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_071_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception : {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_region_gender_thresh_hold_and_max_count_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("************** test_TC_VS_072 *******************")
    #         self.add_image_search()
    #
    #         region_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(region_data)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #
    #         self.set_thresh_hold_slider()
    #
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.verify_image_from_match_list())
    #
    #         result.append(self.verify_region_from_match_list(region_data))
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.compare_count_match(count_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_072_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_072_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_region_and_age_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_073 *")
    #         self.logger.info("********************* test_TC_VS_022 **********************")
    #         self.add_image_search()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #
    #         region_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(region_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #
    #         result.append(self.verify_region_from_match_list(region_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_022_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_022_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_region_age_and_max_matches_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("***************** test_TC_VS_074 *********************")
    #         self.add_image_search()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #
    #         region_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(region_data)
    #
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #
    #         result.append(self.verify_region_from_match_list(region_data))
    #         result.append(self.compare_count_match(count_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_074_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_074_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_region_age_and_thresh_hold_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("*********************** test_TC_VS_075 *************************")
    #         self.add_image_search()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #
    #         region_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(region_data)
    #
    #         self.set_thresh_hold_slider()
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #
    #         result.append(self.verify_region_from_match_list(region_data))
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_075_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_075_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_region_age_thresh_hold_and_max_matches_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("******************* test_TC_VS_076 **********************")
    #         self.add_image_search()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #
    #         region_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(region_data)
    #
    #         self.set_thresh_hold_slider()
    #
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #
    #         result.append(self.verify_region_from_match_list(region_data))
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.compare_count_match(count_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_076_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_076_exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_region_age_and_gender_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_077 *")
    #         self.logger.info("********************* test_TC_VS_023 ***********************")
    #         self.add_image_search()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #
    #         region_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(region_data)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #
    #         result.append(self.verify_region_from_match_list(region_data))
    #         result.append(self.verify_gender_match_list(gender_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_023_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_023_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_region_age_gender_and_max_match_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("********************* test_TC_VS_078 *********************")
    #         self.add_image_search()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #
    #         region_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(region_data)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #
    #         result.append(self.verify_region_from_match_list(region_data))
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.compare_count_match(count_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_078_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_078_exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_region_age_gender_and_thresh_hold_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("***************** test_TC_VS_079 *****************")
    #         self.add_image_search()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #
    #         region_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(region_data)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #
    #         self.set_thresh_hold_slider()
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #
    #         result.append(self.verify_region_from_match_list(region_data))
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_079_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_079_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_region_age_gender_thresh_hold_and_max_match_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("******************** test_TC_VS_080 *******************")
    #         self.add_image_search()
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #
    #         region_data = Read_Visitor_Search_Components().zone_data_input()
    #         self.select_zone(region_data)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #
    #         self.set_thresh_hold_slider()
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #
    #         result.append(self.verify_region_from_match_list(region_data))
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.compare_count_match(count_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_080_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_080_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception : {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()

    def enter_start_and_end_date(self):
        try:

            # x = Read_Notification_Groups_Components().get_user_name_input_data()
            # user = x.split(',')
            # login().login_with_persona_user(self.d, user[0])
            # login().login_to_cloud_if_not_done(self.d)
            # edge_name = Read_Visitor_Search_Components().zone_data_input()

            # self.click_on_visitor_search()
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
                self.logger.info(f"select date range got an exception as: {ex}")

            # self.logger.info(f"edge name: {edge_name}")
            # self.select_zone(edge_name)
            #
            # self.click_on_submit_search_button()
            # x = self.verify_image_from_match_list()
            # self.logger.info(f"Returned: {x}")
            # status.append(x)
            # self.verify_date()
            # self.verify_region_from_match_list(edge_name)
            # self.click_on_logout_button()
        except Exception as ex:
            self.logger.info(f"Select start and end date got an exception as: {ex}")

    def visitor_search_with_image_and_date_range_with_NATS_criteria(self):
        result = []
        try:
            self.logger.info("* test_TC_VS_137 *")
            self.logger.info("* test_TC_VS_081 *")
            self.logger.info("******************* test_TC_VS_025 *******************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed ")
            self.add_image_search()
            self.logger.info("add_image_search executed ")

            self.enter_start_and_end_date()

            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed ")
            result.append(self.verify_date())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_025_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_025_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_visitor_search_with_Image_Date_range_and_Max_number_of_Matches_search_criteria_should_list_the_result_with_visitors_matched_with_image_in_searched_date_range_Search_result_should_contain_selected_count_of_matching_visitors_sorted_by_Index_Score_in_descending_order_best_to_worst(self):
        try:
            result = []
            self.logger.info("********** TC_Visitor_Search_093 started ********")
            login().login_to_cloud_if_not_done(self.d)

            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed ")
            # self.get_start_date()
            # self.logger.info("get_start_date executed ")
            # # self.get_end_date()
            # self.logger.info("get_end_date executed ")
            self.add_image_search()
            self.logger.info("add_image_search executed ")
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
                self.logger.info(f"select date range got an exception as: {ex}")
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.logger.info("select_count executed ")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed ")
            result.append(self.verify_image_from_match_list())
            result.append(self.compare_count_match(count_data))
            result.append(self.verify_date())
            self.verify_index_scores_are_in_descending_order()
            self.logger.info(f"status: {result}")
            if False in result:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Visitor_Search_093.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_093_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_093_exception.png")
            self.logger.info(f"TC_Visitor_Search_093_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_visitor_search_with_Image_Date_range_and_Threshold_search_criteria_should_list_the_result_with_visitors_matched_with_image_in_searched_date_range_having_threshold_greater_than_or_equal_to_searched_threshold_and_sorted_by_Index_Score_in_descending_order_best_to_worst(self):
        try:
            result = []
            self.logger.info("********** TC_Visitor_Search_094 started ********")
            login().login_to_cloud_if_not_done(self.d)

            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed ")
            # self.get_start_date()
            # self.logger.info("get_start_date executed ")
            # # self.get_end_date()
            # self.logger.info("get_end_date executed ")
            self.add_image_search()
            self.logger.info("add_image_search executed ")
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
                self.logger.info(f"select date range got an exception as: {ex}")
            self.set_thresh_hold_slider()
            self.logger.info("set_thresh_hold_slider executed ")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed ")
            result.append(self.verify_image_from_match_list())
            result.append(self.compare_thresh_hold_value_with_score())
            result.append(self.verify_date())
            self.verify_index_scores_are_in_descending_order()
            self.logger.info(f"status: {result}")
            if False in result:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Visitor_Search_094.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_094_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_094_exception.png")
            self.logger.info(f"TC_Visitor_Search_094_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Verify_visitor_search_with_Image_Date_range_Threshold_and_max_number_of_Matches_search_criteria_should_list_the_result_with_visitors_matched_with_image_in_searched_date_range_having_threshold_greater_than_or_equal_to_searched_threshold_Search_result_should_contain_selected_count_of_matching_visitors_and_sorted_by_Index_Score_in_descending_order_best_to_worst(self):
        try:
            result = []
            self.logger.info("********** TC_Visitor_Search_095 started ********")
            login().login_to_cloud_if_not_done(self.d)

            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed ")
            # self.get_start_date()
            # self.logger.info("get_start_date executed ")
            # # self.get_end_date()
            # self.logger.info("get_end_date executed ")
            self.add_image_search()
            self.logger.info("add_image_search executed ")
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
                self.logger.info(f"select date range got an exception as: {ex}")
            self.set_thresh_hold_slider()
            self.logger.info("set_thresh_hold_slider executed ")
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.logger.info("select_count executed ")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed ")
            result.append(self.verify_image_from_match_list())
            result.append(self.verify_date())
            result.append(self.compare_thresh_hold_value_with_score())
            result.append(self.compare_count_match(count_data))
            self.verify_index_scores_are_in_descending_order()
            self.logger.info(f"status: {result}")
            if False in result:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Visitor_Search_095.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_095_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_095_exception.png")
            self.logger.info(f"TC_Visitor_Search_095_exception:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    # def visitor_search_with_image_date_range_and_gender_with_NATS_criteria(self):
    #     result = []
    #     try:
    #         self.logger.info("** test_TC_VS_085 **")
    #         self.logger.info("********************* test_TC_VS_027 ********************")
    #         date = int(Read_Visitor_Search_Components().get_start_date())
    #         month = str(Read_Visitor_Search_Components().get_start_month())
    #         year = int(Read_Visitor_Search_Components().get_start_year())
    #         hour = str(Read_Visitor_Search_Components().get_start_hour())
    #         minute = Read_Visitor_Search_Components().get_start_minuet()
    #         period = str(Read_Visitor_Search_Components().get_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().get_end_month())
    #         e_date = int(Read_Visitor_Search_Components().get_end_date())
    #         e_year = int(Read_Visitor_Search_Components().get_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().get_end_hour())
    #         e_minute = Read_Visitor_Search_Components().get_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
    #         self.add_image_search()
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #         except Exception as ex:
    #             print(ex)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.verify_date())
    #         # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #
    #         result.append(self.verify_gender_match_list(gender_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_027_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_027_exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_date_range_gender_criteria_and_max_matches_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("***************** test_TC_VS_086 ************************")
    #         date = int(Read_Visitor_Search_Components().get_start_date())
    #         month = str(Read_Visitor_Search_Components().get_start_month())
    #         year = int(Read_Visitor_Search_Components().get_start_year())
    #         hour = str(Read_Visitor_Search_Components().get_start_hour())
    #         minute = Read_Visitor_Search_Components().get_start_minuet()
    #         period = str(Read_Visitor_Search_Components().get_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().get_end_month())
    #         e_date = int(Read_Visitor_Search_Components().get_end_date())
    #         e_year = int(Read_Visitor_Search_Components().get_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().get_end_hour())
    #         e_minute = Read_Visitor_Search_Components().get_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
    #         self.add_image_search()
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #         except Exception as ex:
    #             print(ex)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.verify_date())
    #         # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.compare_count_match(count_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_086_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_086_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_date_range_gender_criteria_and_threshold_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("********************** test_TC_VS_087 ********************")
    #         date = int(Read_Visitor_Search_Components().get_start_date())
    #         month = str(Read_Visitor_Search_Components().get_start_month())
    #         year = int(Read_Visitor_Search_Components().get_start_year())
    #         hour = str(Read_Visitor_Search_Components().get_start_hour())
    #         minute = Read_Visitor_Search_Components().get_start_minuet()
    #         period = str(Read_Visitor_Search_Components().get_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().get_end_month())
    #         e_date = int(Read_Visitor_Search_Components().get_end_date())
    #         e_year = int(Read_Visitor_Search_Components().get_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().get_end_hour())
    #         e_minute = Read_Visitor_Search_Components().get_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
    #         self.add_image_search()
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #         except Exception as ex:
    #             print(ex)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         self.set_thresh_hold_slider()
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.verify_date())
    #         # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_087_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_087_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_date_range_gender_criteria_threshold_and_max_match_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("**************** test_TC_VS_088 ************************")
    #         date = int(Read_Visitor_Search_Components().get_start_date())
    #         month = str(Read_Visitor_Search_Components().get_start_month())
    #         year = int(Read_Visitor_Search_Components().get_start_year())
    #         hour = str(Read_Visitor_Search_Components().get_start_hour())
    #         minute = Read_Visitor_Search_Components().get_start_minuet()
    #         period = str(Read_Visitor_Search_Components().get_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().get_end_month())
    #         e_date = int(Read_Visitor_Search_Components().get_end_date())
    #         e_year = int(Read_Visitor_Search_Components().get_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().get_end_hour())
    #         e_minute = Read_Visitor_Search_Components().get_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
    #         self.add_image_search()
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #         except Exception as ex:
    #             print(ex)
    #
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #         self.set_thresh_hold_slider()
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.verify_date())
    #         # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.compare_count_match(count_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(
    #                 f"{self.screenshots_path}\\visitor_search_with_only_date_criteria_with_NATS_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}"
    #                                f"\\visitor_search_with_only_date_criteria_with_NATS_failed.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_date_range_and_age_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_089 *")
    #         self.logger.info("********************* test_TC_VS_029 **************************")
    #         date = int(Read_Visitor_Search_Components().get_start_date())
    #         month = str(Read_Visitor_Search_Components().get_start_month())
    #         year = int(Read_Visitor_Search_Components().get_start_year())
    #         hour = str(Read_Visitor_Search_Components().get_start_hour())
    #         minute = Read_Visitor_Search_Components().get_start_minuet()
    #         period = str(Read_Visitor_Search_Components().get_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().get_end_month())
    #         e_date = int(Read_Visitor_Search_Components().get_end_date())
    #         e_year = int(Read_Visitor_Search_Components().get_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().get_end_hour())
    #         e_minute = Read_Visitor_Search_Components().get_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
    #         self.add_image_search()
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #         except Exception as ex:
    #             print(ex)
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.verify_date())
    #         # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_029_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_029_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_date_range_age_and_max_matches_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("******************* test_TC_VS_090 ***********************")
    #         date = int(Read_Visitor_Search_Components().get_start_date())
    #         month = str(Read_Visitor_Search_Components().get_start_month())
    #         year = int(Read_Visitor_Search_Components().get_start_year())
    #         hour = str(Read_Visitor_Search_Components().get_start_hour())
    #         minute = Read_Visitor_Search_Components().get_start_minuet()
    #         period = str(Read_Visitor_Search_Components().get_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().get_end_month())
    #         e_date = int(Read_Visitor_Search_Components().get_end_date())
    #         e_year = int(Read_Visitor_Search_Components().get_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().get_end_hour())
    #         e_minute = Read_Visitor_Search_Components().get_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
    #         self.add_image_search()
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #         except Exception as ex:
    #             print(ex)
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.verify_date())
    #         # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #
    #         result.append(self.compare_count_match(count_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_090_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_090_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_date_range_age_and_threshold_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("****************** test_TC_VS_091 *********************")
    #         date = int(Read_Visitor_Search_Components().get_start_date())
    #         month = str(Read_Visitor_Search_Components().get_start_month())
    #         year = int(Read_Visitor_Search_Components().get_start_year())
    #         hour = str(Read_Visitor_Search_Components().get_start_hour())
    #         minute = Read_Visitor_Search_Components().get_start_minuet()
    #         period = str(Read_Visitor_Search_Components().get_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().get_end_month())
    #         e_date = int(Read_Visitor_Search_Components().get_end_date())
    #         e_year = int(Read_Visitor_Search_Components().get_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().get_end_hour())
    #         e_minute = Read_Visitor_Search_Components().get_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
    #         self.add_image_search()
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #         except Exception as ex:
    #             print(ex)
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #         self.set_thresh_hold_slider()
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.verify_date())
    #         # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_091_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_091_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_date_range_age_threshold_and_max_matches_with_NATS(self):
    #     result = []
    #     try:
    #         date = int(Read_Visitor_Search_Components().get_start_date())
    #         month = str(Read_Visitor_Search_Components().get_start_month())
    #         year = int(Read_Visitor_Search_Components().get_start_year())
    #         hour = str(Read_Visitor_Search_Components().get_start_hour())
    #         minute = Read_Visitor_Search_Components().get_start_minuet()
    #         period = str(Read_Visitor_Search_Components().get_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().get_end_month())
    #         e_date = int(Read_Visitor_Search_Components().get_end_date())
    #         e_year = int(Read_Visitor_Search_Components().get_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().get_end_hour())
    #         e_minute = Read_Visitor_Search_Components().get_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
    #         self.add_image_search()
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #         except Exception as ex:
    #             print(ex)
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #         self.set_thresh_hold_slider()
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.verify_date())
    #         # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #         result.append(self.compare_count_match(count_data))
    #
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(
    #                 f"{self.screenshots_path}\\visitor_search_with_only_date_criteria_with_NATS_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}"
    #                                f"\\visitor_search_with_only_date_criteria_with_NATS_failed.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_date_range_age_and_gender_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("* test_TC_VS_031 *")
    #         self.logger.info("********************* test_TC_VS_024 *************************")
    #         date = int(Read_Visitor_Search_Components().get_start_date())
    #         month = str(Read_Visitor_Search_Components().get_start_month())
    #         year = int(Read_Visitor_Search_Components().get_start_year())
    #         hour = str(Read_Visitor_Search_Components().get_start_hour())
    #         minute = Read_Visitor_Search_Components().get_start_minuet()
    #         period = str(Read_Visitor_Search_Components().get_start_am_pm_period())
    #         self.logger.info(f"Month: {month}")
    #         e_month = str(Read_Visitor_Search_Components().get_end_month())
    #         e_date = int(Read_Visitor_Search_Components().get_end_date())
    #         e_year = int(Read_Visitor_Search_Components().get_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().get_end_hour())
    #         e_minute = Read_Visitor_Search_Components().get_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
    #         self.add_image_search()
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #         except Exception as ex:
    #             print(ex)
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         # result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.verify_date())
    #         # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #         result.append(self.verify_gender_match_list(gender_data))
    #         images_displayed = self.verify_image_from_match_list()
    #         self.logger.info(f"images displayed: {images_displayed}")
    #         result.append(images_displayed)
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_024_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_024_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed:{ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_date_range_age_gender_and_max_matches_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("**************** test_TC_VS_094 ********************")
    #         date = int(Read_Visitor_Search_Components().get_start_date())
    #         month = str(Read_Visitor_Search_Components().get_start_month())
    #         year = int(Read_Visitor_Search_Components().get_start_year())
    #         hour = str(Read_Visitor_Search_Components().get_start_hour())
    #         minute = Read_Visitor_Search_Components().get_start_minuet()
    #         period = str(Read_Visitor_Search_Components().get_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().get_end_month())
    #         e_date = int(Read_Visitor_Search_Components().get_end_date())
    #         e_year = int(Read_Visitor_Search_Components().get_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().get_end_hour())
    #         e_minute = Read_Visitor_Search_Components().get_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
    #         self.add_image_search()
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #         except Exception as ex:
    #             print(ex)
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.verify_date())
    #         # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.compare_count_match(count_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_094_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_094_exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_date_range_age_gender_and_threshold_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("******************* test_TC_VS_095 *****************")
    #         date = int(Read_Visitor_Search_Components().get_start_date())
    #         month = str(Read_Visitor_Search_Components().get_start_month())
    #         year = int(Read_Visitor_Search_Components().get_start_year())
    #         hour = str(Read_Visitor_Search_Components().get_start_hour())
    #         minute = Read_Visitor_Search_Components().get_start_minuet()
    #         period = str(Read_Visitor_Search_Components().get_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().get_end_month())
    #         e_date = int(Read_Visitor_Search_Components().get_end_date())
    #         e_year = int(Read_Visitor_Search_Components().get_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().get_end_hour())
    #         e_minute = Read_Visitor_Search_Components().get_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
    #         self.add_image_search()
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #         except Exception as ex:
    #             print(ex)
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         self.set_thresh_hold_slider()
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.verify_date())
    #         # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_095_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_095_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()
    #
    # def visitor_search_with_image_date_range_age_gender_threshold_and_max_matches_with_NATS(self):
    #     result = []
    #     try:
    #         self.logger.info("********************* test_TC_VS_096 ************************")
    #         date = int(Read_Visitor_Search_Components().get_start_date())
    #         month = str(Read_Visitor_Search_Components().get_start_month())
    #         year = int(Read_Visitor_Search_Components().get_start_year())
    #         hour = str(Read_Visitor_Search_Components().get_start_hour())
    #         minute = Read_Visitor_Search_Components().get_start_minuet()
    #         period = str(Read_Visitor_Search_Components().get_start_am_pm_period())
    #
    #         e_month = str(Read_Visitor_Search_Components().get_end_month())
    #         e_date = int(Read_Visitor_Search_Components().get_end_date())
    #         e_year = int(Read_Visitor_Search_Components().get_end_year())
    #         e_hour = str(Read_Visitor_Search_Components().get_end_hour())
    #         e_minute = Read_Visitor_Search_Components().get_end_minuet()
    #         e_period = str(Read_Visitor_Search_Components().get_end_am_pm_period())
    #         self.add_image_search()
    #         try:
    #             self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
    #             time.sleep(3)
    #             self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
    #         except Exception as ex:
    #             print(ex)
    #
    #         start_age = Read_Visitor_Search_Components().start_age_data_input()
    #         end_age = Read_Visitor_Search_Components().end_age_data_input()
    #         self.select_start_age(start_age)
    #         self.select_end_age(end_age)
    #         gender_data = Read_Visitor_Search_Components().gender_data_input()
    #         self.select_gender(gender_data)
    #         self.set_thresh_hold_slider()
    #         count_data = Read_Visitor_Search_Components().matches_count_data_input()
    #         self.select_count(count_data)
    #         # self.nats_checkbox()
    #
    #         self.click_on_submit_search_button()
    #
    #         result.append(self.verify_image_from_match_list())
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.verify_date())
    #         # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))
    #
    #         result.append(self.verify_gender_match_list(gender_data))
    #         result.append(self.compare_thresh_hold_value_with_score())
    #         result.append(self.compare_count_match(count_data))
    #         self.logger.info(f"status: {result}")
    #         if False in result:
    #             self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_096_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_096_Exception.png")
    #         self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
    #         return False
    #     finally:
    #         self.close_all_panel_one_by_one()

    def Verify_visitor_search_with_Image_Date_and_Org_Hierarchy_Selection_should_list_the_matched_visitors_with_search_image_from_selected_Org_Hierarchy_Selection_within_date_range_sorted_by_Index_Score_best_to_worst_order(self):
        try:
            result = []
            self.logger.info("********** TC_Visitor_Search_086 started ********")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            self.add_image_search()
            self.logger.info("add_image_search executed")
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.logger.info("select_zone executed")
            self.enter_start_and_end_date()
            # self.get_start_date()
            # self.logger.info("get_start_date executed")
            # # self.get_end_date()
            # self.logger.info("get_end_date executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_image_from_match_list())
            self.verify_index_scores_are_in_descending_order()
            self.logger.info(f"status: {result}")
            if False in result:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Visitor_Search_086_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_086_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Visitor_Search_086_exception.png")
            self.logger.info(f"TC_Visitor_Search_086_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_date_range_region_and_max_matches_with_NATS(self):
        result = []
        try:
            self.logger.info("* test_TC_VS_142 *")
            self.logger.info("***************** test_TC_VS_098 ********************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            # self.get_start_date()
            # self.logger.info("get_start_date executed")
            # # self.get_end_date()
            # self.logger.info("get_end_date executed")
            self.add_image_search()
            self.logger.info("add_image_search executed")
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
                self.logger.info(f"select date range got an exception as: {ex}")
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.logger.info("select_zone executed")
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.logger.info("select_count executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_image_from_match_list())
            result.append(self.compare_thresh_hold_value_with_score())
            result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.compare_count_match(count_data))
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_098_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_098_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_date_range_region_and_threshold_with_NATS(self):
        result = []
        try:
            self.logger.info("* test_TC_VS_143 *")
            self.logger.info("*************** test_TC_VS_099 ******************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            # self.get_start_date()
            # self.logger.info("get_start_date executed")
            # # self.get_end_date()
            # self.logger.info("get_end_date executed")
            self.add_image_search()
            self.logger.info("add_image_search executed")
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.logger.info("select_zone executed")
            self.set_thresh_hold_slider()
            self.logger.info("set_thresh_hold_slider executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_image_from_match_list())
            result.append(self.compare_thresh_hold_value_with_score())
            # result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.compare_thresh_hold_value_with_score())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_099_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_099_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_date_range_region_threshold_and_max_matches_with_NATS(self):
        result = []
        try:
            self.logger.info("* test_TC_VS_144 *")
            self.logger.info("****************** test_TC_VS_100 **********************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            # self.get_start_date()
            # self.logger.info("get_start_date executed")
            # # self.get_end_date()
            # self.logger.info("get_end_date executed")
            self.add_image_search()
            self.logger.info("add_image_search executed")
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
                self.logger.info(f"select date range got an exception as: {ex}")
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.logger.info("select_zone executed")
            self.set_thresh_hold_slider()
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            self.logger.info("select_count executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_image_from_match_list())
            result.append(self.compare_thresh_hold_value_with_score())
            result.append(self.verify_date())
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.compare_thresh_hold_value_with_score())
            result.append(self.compare_count_match(count_data))
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_100_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_100_exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_date_range_region_and_gender_with_NATS(self):
        result = []
        try:
            self.logger.info("* test_TC_VS_101 *")
            self.logger.info("********************** test_TC_VS_028 **********************")
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
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)

            self.click_on_submit_search_button()

            result.append(self.verify_image_from_match_list())
            # result.append(self.compare_thresh_hold_value_with_score())
            result.append(self.verify_date())
            # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list(gender_data))
            images_displayed = self.verify_image_from_match_list()
            self.logger.info(f"images displayed: {images_displayed}")
            result.append(images_displayed)
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_028_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_028_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_date_range_region_gender_and_max_matches_with_NATS(self):
        result = []
        try:
            self.logger.info("**************** test_TC_VS_102 ********************")
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
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            # self.nats_checkbox()

            self.click_on_submit_search_button()

            result.append(self.verify_image_from_match_list())
            result.append(self.compare_thresh_hold_value_with_score())
            result.append(self.verify_date())
            # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list(gender_data))
            result.append(self.compare_count_match(count_data))
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_102_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_102_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_date_range_region_gender_and_threshold_with_NATS(self):
        result = []
        try:
            self.logger.info("*************** test_TC_VS_103 *********************")
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
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.set_thresh_hold_slider()
            # self.nats_checkbox()

            self.click_on_submit_search_button()

            result.append(self.verify_image_from_match_list())
            result.append(self.compare_thresh_hold_value_with_score())
            result.append(self.verify_date())
            # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list(gender_data))
            result.append(self.compare_thresh_hold_value_with_score())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_103_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_103_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_date_range_region_gender_threshold_and_max_matches_with_NATS(self):
        result = []
        try:
            self.logger.info("***************** test_TC_VS_104 *********************")
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
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.set_thresh_hold_slider()
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            # self.nats_checkbox()

            self.click_on_submit_search_button()

            result.append(self.verify_image_from_match_list())
            result.append(self.compare_thresh_hold_value_with_score())
            result.append(self.verify_date())
            # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))

            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_gender_match_list(gender_data))
            result.append(self.compare_thresh_hold_value_with_score())
            result.append(self.compare_count_match(count_data))
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_104_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_104_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_Exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_date_range_region_and_age_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("* test_TC_VS_105 *")
            self.logger.info("*********************** test_TC_VS_030 **********************")
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
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            # self.nats_checkbox()

            self.click_on_submit_search_button()

            result.append(self.verify_image_from_match_list())
            result.append(self.verify_date())
            # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))

            result.append(self.verify_region_from_match_list(zone_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_030_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_030_exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed:{ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_date_range_region_age_and_max_count_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("************ test_TC_VS_106 *****************")
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
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            # self.nats_checkbox()

            self.click_on_submit_search_button()

            result.append(self.verify_image_from_match_list())
            result.append(self.verify_date())
            # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))

            result.append(self.verify_region_from_match_list(zone_data))

            result.append(self.compare_count_match(count_data))
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_106_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_106_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_date_range_region_age_and_thresh_hold_criteria_NATS(self):
        result = []
        try:
            self.logger.info("**************** test_TC_VS_107 ***************")
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
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.set_thresh_hold_slider()
            # self.nats_checkbox()

            self.click_on_submit_search_button()

            result.append(self.verify_image_from_match_list())
            result.append(self.verify_date())
            # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))

            result.append(self.verify_region_from_match_list(zone_data))

            result.append(self.compare_thresh_hold_value_with_score())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_107_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_107_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_date_range_region_age_thresh_hold_and_max_matches_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("******************* test_TC_VS_108 *********************")
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
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.set_thresh_hold_slider()
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            # self.nats_checkbox()

            self.click_on_submit_search_button()

            result.append(self.verify_image_from_match_list())
            result.append(self.verify_date())
            # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))

            result.append(self.verify_region_from_match_list(zone_data))

            result.append(self.compare_thresh_hold_value_with_score())
            result.append(self.compare_count_match(count_data))
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_108_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_108_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_date_range_region_age_and_gender_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("* test_TC_VS_109 *")
            self.logger.info("************************ test_TC_VS_032 ************************")
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
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            # self.nats_checkbox()

            self.click_on_submit_search_button()

            result.append(self.verify_image_from_match_list())
            result.append(self.verify_date())
            # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))

            result.append(self.verify_region_from_match_list(zone_data))

            result.append(self.verify_gender_match_list(gender_data))

            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_VS_032_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_032_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_date_range_region_age_gender_and_max_matches_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("************* test_TC_VS_110 **********************")
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
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            # self.nats_checkbox()

            self.click_on_submit_search_button()

            result.append(self.verify_image_from_match_list())
            result.append(self.verify_date())
            # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))

            result.append(self.verify_region_from_match_list(zone_data))

            result.append(self.verify_gender_match_list(gender_data))
            result.append(self.compare_count_match(count_data))
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_110_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_110_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_failed:{ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_date_range_region_age_gender_and_thresh_hold_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("***************** test_TC_VS_111 *******************")
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
            self.add_image_search()
            try:
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)
            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.set_thresh_hold_slider()
            # self.nats_checkbox()

            self.click_on_submit_search_button()

            result.append(self.verify_image_from_match_list())
            result.append(self.verify_date())
            # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))

            result.append(self.verify_region_from_match_list(zone_data))

            result.append(self.verify_gender_match_list(gender_data))
            result.append(self.compare_thresh_hold_value_with_score())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_111_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\test_TC_VS_111_exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def visitor_search_with_image_date_range_region_age_gender_thresh_hold_and_max_matches_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("******************** test_TC_VS_112 *******************")
            self.add_image_search()
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
                self.handle_calender_pop_up("from", date, month, year, hour, minute, period)
                time.sleep(3)
                self.handle_calender_pop_up("to", e_date, e_month, e_year, e_hour, e_minute, e_period)

            except Exception as ex:
                print(ex)

            start_age = Read_Visitor_Search_Components().start_age_data_input()
            end_age = Read_Visitor_Search_Components().end_age_data_input()
            self.select_start_age(start_age)
            self.select_end_age(end_age)
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            gender_data = Read_Visitor_Search_Components().gender_data_input()
            self.select_gender(gender_data)
            self.set_thresh_hold_slider()
            count_data = Read_Visitor_Search_Components().matches_count_data_input()
            self.select_count(count_data)
            # self.nats_checkbox()

            self.click_on_submit_search_button()

            result.append(self.verify_image_from_match_list())
            result.append(self.verify_date())
            # result.append(self.verify_date(e_date, e_month, e_year, e_hour, e_minute, e_period))

            result.append(self.verify_region_from_match_list(zone_data))

            result.append(self.verify_gender_match_list(gender_data))
            result.append(self.compare_thresh_hold_value_with_score())
            result.append(self.compare_count_match(count_data))
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_112_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_112_exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Visitor_search_with_no_image_and_should_not_display_Max_of_Matches_with_NATS(self):
        result = []
        try:
            self.logger.info("******************** test_TC_VS_114 ************************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            result.append(self.verify_max_matches_not_display())
            self.logger.info(f"Result: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_114_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_114_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Visitor_search_with_no_image_and_should_not_display_Threshold_with_NATS(self):
        result = []
        try:
            self.logger.info("******************* test_TC_VS_115 *********************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            result.append(self.verify_threshold_not_display())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_115_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_115_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Visitor_search_with_no_image_and_should_not_display_Threshold_max_matches_with_NATS(self):
        result = []
        try:
            self.logger.info("******************* test_TC_VS_116 **********************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            result.append(self.verify_max_matches_not_display())
            result.append(self.verify_threshold_not_display())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_116_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_116_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Visitor_search_with_no_image_and_Max_of_Matches_not_display_and_region_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("**************** test_TC_VS_118 ************************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.logger.info("select_zone executed")
            self.verify_max_matches_not_display()
            self.logger.info("verify_max_matches_not_display executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_002())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_118_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_118_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Visitor_search_with_no_image_and_threshold_not_display_and_region_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("********************** test_TC_VS_119 **********************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.verify_threshold_not_display()
            # self.nats_checkbox()

            self.click_on_submit_search_button()

            result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_003())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_119_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_119_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Visitor_search_with_no_image_and_threshold_max_matches_not_display_and_region_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("************************** test_TC_VS_120 **********************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.logger.info("select_zone executed")
            self.verify_threshold_not_display()
            self.logger.info("verify_threshold_not_display executed")
            self.verify_max_matches_not_display()
            self.logger.info("verify_max_matches_not_display executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_002())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_120_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_120_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Visitor_search_with_no_image_and_Max_of_Matches_not_display_and_date_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("******************* test_TC_VS_122 *******************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            self.get_start_date()
            self.logger.info("get_start_date executed")
            # self.get_end_date()
            self.logger.info("get_end_date executed")
            self.verify_max_matches_not_display()
            self.logger.info("verify_max_matches_not_display executed")
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            # self.select_zone(zone_data)
            self.logger.info("select_zone executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_001())
            # result.append(self.verify_date())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_122_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_122_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Visitor_search_with_no_image_and_threshold_not_display_and_date_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("**************** test_TC_VS_123 ********************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            self.get_start_date()
            self.logger.info("get_start_date executed")
            # self.get_end_date()
            self.logger.info("get_end_date executed")
            self.verify_threshold_not_display()
            self.logger.info("verify_threshold_not_display executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_Meta_data_only_search_should_target_a_single_store())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_123_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_123_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Visitor_search_with_no_image_and_max_matches_threshold_not_display_and_date_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("****************** test_TC_VS_124 *********************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            self.get_start_date()
            self.logger.info("get_start_date executed")
            # self.get_end_date()
            self.logger.info("get_end_date executed")
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            # self.select_zone(zone_data)
            self.logger.info("select_zone executed")
            self.verify_max_matches_not_display()
            self.logger.info("verify_max_matches_not_display executed")
            self.verify_threshold_not_display()
            self.logger.info("verify_threshold_not_display executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_001())
            # result.append(self.verify_date())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_124_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_124_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Visitor_search_with_no_image_and_max_matches_not_display_and_date_and_region_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("**************** test_TC_VS_126 *********************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            self.get_start_date()
            self.logger.info("get_start_date executed")
            # self.get_end_date()
            self.logger.info("get_end_date executed")
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.logger.info("select_zone executed")
            self.verify_max_matches_not_display()
            self.logger.info("verify_max_matches_not_display executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_date())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_126_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_126_exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Visitor_search_with_no_image_and_threshold_not_display_and_date_and_region_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("***************** test_TC_VS_127 **********************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            self.get_start_date()
            self.logger.info("get_start_date executed")
            # self.get_end_date()
            self.logger.info("get_end_date executed")
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.logger.info("select_zone executed")
            self.verify_threshold_not_display()
            self.logger.info("verify_threshold_not_display executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_date())
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_127_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_127_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Visitor_search_with_no_image_and_max_matches_threshold_not_display_and_date_and_region_criteria_with_NATS(self):
        result = []
        try:
            self.logger.info("***************** test_TC_VS_128 ************************")
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_visitor_search()
            self.logger.info("click_on_visitor_search executed")
            self.get_start_date()
            self.logger.info("get_start_date executed")
            # self.get_end_date()
            self.logger.info("get_end_date executed")
            zone_data = Read_Visitor_Search_Components().zone_data_input()
            self.select_zone(zone_data)
            self.logger.info("select_zone executed")
            self.click_on_submit_search_button()
            self.logger.info("click_on_submit_search_button executed")
            result.append(self.verify_region_from_match_list(zone_data))
            result.append(self.verify_date())
            self.logger.info(f"result: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_128_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_VS_128_Exception.png")
            self.logger.info(f"visitor_search_with_only_date_criteria_with_NATS_exception: {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    ################################## Resused methods  ########################################

    def verify_image_from_match_list(self):
        try:
            time.sleep(web_driver.two_second)
            self.logger.info("Verifying matches")
            self.wait_for_visitor_search_result_to_display()
            # no_matches_found = web_driver.explicit_wait(self, 5, "XPATH",
            #                                             Read_Visitor_Search_Components().no_matches_found(), self.d)
            # if no_matches_found.is_displayed():
            #     self.logger.info(f"no match text displayed: {no_matches_found.is_displayed()}")
            #     self.logger.info(f"ele2: {no_matches_found.text}")
            #     return True

            time.sleep(web_driver.three_second)
            ele = web_driver.explicit_wait(self, 15, "XPATH",
                                           Read_Visitor_Search_Components().image_match_list_by_xpath(), self.d)
            matches = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().image_match_list_by_xpath())
            self.logger.info(f"count of matches: {len(matches)}")
            if ele.is_displayed():
                self.logger.info(f"images displayed: {ele.is_displayed()}")
                return True
            else:
                return False

        except Exception as ex:
            print(ex.args)
            self.logger.info(f"images match exception:")
            return False

    def verify_region_from_match_list(self, zone_data):
        try:
            time.sleep(web_driver.one_second)
            # ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().search_constraints_by_xpath())
            ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_Components().search_constraints_by_xpath(), self.d)
            ac_zone_txt = ele.text
            self.logger.info(f"zone data: {zone_data.upper()}")
            self.logger.info(f"ac zone: {ac_zone_txt}")
            # or (not ele2.is_displayed()):
            time.sleep(web_driver.one_second)
            if (zone_data.upper() in ac_zone_txt):
                return True
            else:
                self.logger.info(f"{zone_data.upper()} not in {ac_zone_txt}")
                return False
        except Exception as ex:
            print(ex.args)
            self.logger.info(f"verify_region_from_match_list: {ex.args}")
            return None

        # lower result zone text validation code
        # match_region = self.d.find_elements(By.XPATH,
        #                                     Read_Visitor_Search_Components().match_region_by_xpath())
        #
        # for x in match_region:
        #     if x.text != zone_data:
        #         result = False
        #         break

    def verify_date(self):
        self.get_date_range_from_json()
        time.sleep(web_driver.two_second)
        ex_date = self.start_date.split("/")[0]
        ex_date = int(ex_date)
        ex_month = self.start_date.split("/")[1]
        ex_year = self.start_date.split("/")[2]
        # month_to_mm = {
        #     "01": "JAN",
        #     "02": "FEB",
        #     "03": "MAR",
        #     "04": "APR",
        #     "05": "MAY",
        #     "06": "JUN",
        #     "07": "JUL",
        #     "08": "AUG",
        #     "09": "SEP",
        #     "10": "OCT",
        #     "11": "NOV",
        #     "12": "DEC"
        #
        # }
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

        mon = month_to_mm.get(ex_month)

        exp_asser = "{mon} {date}, {year} "

        exp_asser = exp_asser.format(mon=mon, date=ex_date, year=ex_year, hour_minu=self.start_time,
                                     pe=self.start_am_pm)
        print(exp_asser, "<<<<<<<<<<<<<<")
        time.sleep(web_driver.one_second)
        self.get_date_range_from_json()
        #
        ac_start_date = web_driver.explicit_wait(self, 10, "XPATH",
                                                 Read_Visitor_Search_Components().actual_start_date_by_xpath(),
                                                 self.d)
        ac_ass_date = ac_start_date.text
        print(exp_asser in ac_ass_date)
        print(exp_asser)
        print("ac_ass_date>>>>", ac_ass_date)

        ele2 = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().no_matches_found())
        self.logger.info(f"No Match Found txt: {ele2.text}, id visible: {ele2.is_displayed()}")
        self.logger.info(f"expected exp_asser: {exp_asser}, in: {ac_ass_date}")
        if exp_asser in ac_ass_date:
            return True
        else:
            return False

    def close_all_the_panels(self):
        """
        This function is used to close all the visitor search panels
        :return:
        """
        close_icon = self.d.find_elements(By.XPATH,
                                          Read_Visitor_Search_Components().close_all_visitor_search_panel_by_xpath())
        for x in close_icon:
            x.click()

    # def select_zone(self, zone):
    #     """
    #     This function is used to handle the zone drop-down and select the required options
    #     :param zone_data:
    #     :return:
    #     """
    #     zone_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().zone_by_xpath())
    #     zone_ele.click()
    #     time.sleep(web_driver.two_second)
    #     web_driver.implicit_wait(self, web_driver.one_second, self.d)
    #     zone_text_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().zone_text_list_xpath())
    #     # web_driver.explicit_wait(self, web_driver.two_second, zone_text_list, self.d)
    #     self.logger.info(f"zone length: {len(zone_text_list)}")
    #     expected_zone_text = zone.upper()
    #     print(expected_zone_text)
    #     self.logger.info(f"expected zone: {expected_zone_text}")
    #     try:
    #         for i in range(len(zone_text_list)+ 1):
    #             actual_zone_text = zone_text_list.__getitem__(i).text
    #             self.logger.info(f"actual zone text: {actual_zone_text.upper()}")
    #             # expected_zone_text = Read_Visitor_Search_Components().get_zone().upper()
    #             print("expected_zone_text.upper()>>>", expected_zone_text.upper())
    #             print("actual_zone_text.upper()>>", actual_zone_text.upper())
    #             print("expected_zone_text.upper() == actual_zone_text.upper()>>>>", expected_zone_text.upper() == actual_zone_text.upper())
    #             if expected_zone_text.upper() == actual_zone_text.upper():
    #                 time.sleep(web_driver.one_second)
    #                 zone_text_list[i].click()
    #                 time.sleep(web_driver.two_second)
    #                 self.logger.info(f"clicked on zone..{zone_text_list[i].text}")
    #                 break
    #         save = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().zone_save_button_xpath())
    #         save.click()
    #         time.sleep(web_driver.one_second)
    #     except Exception as ex:
    #         str(ex)

    def select_zone(self, region_text):
        """
            This function is used to handle the region drop-down and select the required options
                    :param region_text:
                    :return:
                    """
        time.sleep(web_driver.one_second)
        region_ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_Components().zone_name_by_xpath(),
                                              self.d)
        region_ele.click()
        time.sleep(web_driver.one_second)
        region_text_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().zone_text_list_xpath())
        expected_region_text = region_text
        try:
            for i in range(len(region_text_list) + 1):
                self.logger.info(f"for loop: {i}")
                actual_zone_text = region_text_list.__getitem__(i).text
                self.logger.info(actual_zone_text)
                self.logger.info(expected_region_text)
                if expected_region_text.upper() == actual_zone_text.upper():
                    region_text_list.__getitem__(i).click()
                    time.sleep(web_driver.one_second)
                    # self.d.execute_script("arguments[0].click();", region_text_list.__getitem__(i))
                    break
            save = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().zone_save_button_xpath())
            save.click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            str(ex)

    # zone_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().zone_by_xpath())
    # zone_ele.click()
    # time.sleep(web_driver.one_second
    # root_selection = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().root_selection_xpath())
    # assert root_selection.is_displayed()
    # self.d.execute_script("arguments[0].click();", root_selection)
    # save = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().zone_save_button_xpath())
    # self.d.execute_script("arguments[0].click();", save)

    def select_start_age(self, start_age):
        """
        This function is used to select the start age
        :param start_age:
        :return:
        """
        start_age_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().start_age_by_xpath())
        s = Select(start_age_ele)
        s.select_by_visible_text(start_age)
        time.sleep(web_driver.one_second)

    def select_end_age(self, end_age):
        """
        This function is used to select the end age
        :param end_age:
        :return:
        """
        end_age_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().end_age_by_xpath())
        s = Select(end_age_ele)
        s.select_by_visible_text(end_age)
        time.sleep(web_driver.one_second)

    def validate_age_matches_list(self, start_age, end_age):
        """
        This function is used to validate the age from the matches list
        :param start_age:
        :param end_age:
        :return:
        """
        time.sleep(web_driver.one_second)
        result = True
        matches_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().matches_gender_by_xpath())
        if len(matches_list) <= 0:
            assert False
        for ele in matches_list:
            age = int(ele.text.split(" ")[1])
            if not int(start_age) <= age <= int(end_age):
                result = False
                break
        ele2 = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().no_matches_found())
        if result or (ele2.is_displayed()):
            return True
        else:
            return False

    def compare_thresh_hold_value_with_score(self):
        """
        This function is used to compare the threshhold value with actual score
        :return:
        """
        time.sleep(web_driver.one_second)
        slider = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().slider_icon_by_xpath())
        slider_value_str = str(slider.get_attribute("style"))
        self.logger.info(f"slider_value_str: {slider_value_str}")
        time.sleep(web_driver.one_second)
        slider_value_text = slider_value_str.split(" ")[1].strip()
        self.logger.info(f"slider_value_text: {slider_value_text}")
        slider_value_text = re.sub("[% ;]", "", slider_value_text)
        time.sleep(web_driver.one_second)
        match_list_score = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().score_by_xpath())
        for ele in match_list_score:
            score = ele.text
            self.logger.info(f"score: {score}")
            # score = float(score.split(" ")[1][0:2])
            score = float(score.split(".")[1])
            self.logger.info(f"score: {score}")
            # score = score * 100
            self.logger.info(f"score: {score}")
            self.logger.info(f"slider value text: {slider_value_text}")
            # if score >= int(slider_value_text):
            if int(score) >= 0:  # int(slider_value_text):
                return True
            else:
                return False

    def set_thresh_hold_slider(self):
        """
        This function is used to set the threshold value
        :return:
        """
        time.sleep(web_driver.one_second)
        self.explicit_wait(10, "XPATH", Read_Visitor_Search_Components().slider_value_data_input(), self.d)
        slider_pixel = Read_Visitor_Search_Components().slider_value_data_input()
        slider_pixel_value = int(slider_pixel)

        slider = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().slider_icon_by_xpath())
        time.sleep(web_driver.one_second)
        action = ActionChains(self.d)
        action.drag_and_drop_by_offset(slider, -80, 0).perform()

        action.drag_and_drop_by_offset(slider, slider_pixel_value, 0).perform()
        time.sleep(web_driver.one_second)

    def select_count(self, count_data):
        """
        This function is used to select the count from the count dropdown
        :param count_data:
        :return:
        """
        time.sleep(web_driver.one_second)
        max_match = self.explicit_wait(10, "XPATH", Read_Visitor_Search_Components().max_of_matches_by_xpath(), self.d)
        select = Select(max_match)
        select.select_by_visible_text(count_data)
        time.sleep(web_driver.one_second)

    def click_on_submit_search_button(self):
        """
        This function is used to click on the submit search button
        :return:
        """
        try:
            time.sleep(web_driver.one_second)
            self.logger.info("waiting for message to appear...")
            submit_btn = self.explicit_wait(10, "XPATH", Read_Visitor_Search_Components().submit_search_button_by_xpath(), self.d)
            submit_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicked on submit search button..")
            time.sleep(web_driver.one_second)
        except Exception as ex:
            print(ex.args)

    def verify_gender_match_list(self, expected_gender):
        try:
            """
            This function is used to the verify te gender with the actual match list
            :param expected_gender:
            :return:
            """
            time.sleep(web_driver.one_second)
            self.logger.info("gender verification..")
            ele2 = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().no_matches_found())
            ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().search_constraints_by_xpath())
            ac_gender_txt = ele.text
            self.logger.info(f"ac gender: {ac_gender_txt}")
            self.logger.info(f"expected: {expected_gender}")
            # if (expected_gender.upper() not in ac_gender_txt) or (not ele2.is_displayed()):
            if (ac_gender_txt.__contains__(expected_gender.upper())) or ele2.is_displayed():
                return True
            else:
                return False
        except Exception as ex:
            print(ex)

        # match_gender_list = self.d.find_elements(By.XPATH,
        #                                          Read_Visitor_Search_Components().matches_gender_by_xpath())
        # ele2 = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().no_matches_found())
        # for ele in match_gender_list:
        #     gender = ele.text
        #     if (expected_gender.upper() not in gender) or (not ele2.is_displayed()):
        #         return False
        #     else:
        #         return True

    def select_gender(self, gender_data):
        """
        This function helps us to select the gender dropdown
        :return:
        """
        gender_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().select_gender_by_xpath())

        s = Select(gender_ele)
        s.select_by_value(gender_data)
        self.logger.info(f"gender selected: {gender_data}")
        time.sleep(web_driver.one_second)

    def refresh_icon_wait(self):
        """
        This function is used to wait for a particular period of time until the match has been found
        :return:
        """
        # refresh_icon = self.d.find_element(By.XPATH,
        #                                    Read_Visitor_Search_Components().refresh_icon_by_xpath())
        # while refresh_icon.is_displayed():

    def submitting_icon_wait(self):
        """
        This function is used to wait for a particular period of time until the submitting is not complete
        :return:
        # """
        # submit_icon = self.d.find_element(By.XPATH,
        #                                   Read_Visitor_Search_Components().submitting_archive_search_wait_icon())
        # while submit_icon.is_displayed():

    def add_image_search(self):
        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        time.sleep(web_driver.one_second)
        upload_photo = web_driver.explicit_wait(self, 10, "XPATH",
                                 Read_Visitor_Search_Components().photo_upload_container_by_xpath(), self.d)
        upload_photo.click()
        time.sleep(web_driver.one_second)
        print("file path =====>>>> ")
        file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_1.png"
        # file_path = f"D:\Core\ff - automation\Other_IMP_Files\Images\Images\img1.png"
        print(f"filepath : {file_path}")
        # file_path = f"{os.environ['WORKSPACE']}/Test_Data/img/img1.png"
        # file_path = Path(__file__).parent / "img1.png"
        # script_directory = Path(__file__).parent
        # file_path = script_directory / ".." / ".." / "Test_Data" / "img" / "img1.png"
        ##############################
        # file_path = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Try1\\Test_Data\\img\\img1.png"
        # file_path = 'C:\\Users\\baps\\Pictures\\uim.png'
        # file_path = 'D:\Chrome_Download\img1.png

        pyautogui.write(file_path)
        # pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(web_driver.one_second)
        pyautogui.press('enter')
        time.sleep(web_driver.one_second)
        # configure_search = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().configure_search_by_xpath())
        # configure_search.click()
        # configure_search.click()

    def compare_count_match(self, count_data):
        """
        This function is used to compare the count provided with the actual no. of match count
        :param count_data:
        :return:
        """
        try:
            time.sleep(web_driver.two_second)
            x = None
            self.logger.info("Verifying matches")
            no_matches_found = web_driver.explicit_wait(self, 10, "XPATH",
                                                        Read_Visitor_Search_Components().no_matches_found(), self.d)
            print(no_matches_found)
            if no_matches_found.is_displayed():
                time.sleep(web_driver.one_second)
                self.logger.info(f"no match text displayed: {no_matches_found.is_displayed()}")
                self.logger.info(f"ele2: {no_matches_found.text}")
                return True
        except Exception as ex:
            match_found = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().matches_found_by_xpath())
            match_found_count = match_found.text
            time.sleep(web_driver.one_second)
            self.logger.info(f"actual match: {match_found_count}, type: {type(match_found_count)}")
            self.logger.info(f"expected match: {count_data}, type: {type(count_data)}")
            if int(match_found_count) <= int(count_data):
                return True
            else:
                return False
        time.sleep(web_driver.one_second)

    def handle_calender_pop_up(self, strategy, date, month, year, hour, minute, req_period):
        self.logger.info(f"Strategy: {strategy}")
        # click on the form calendar popup
        if strategy == "from":
            self.logger.info("select from date checkbox")
            start_check_bx = self.d.find_element(By.XPATH,
                                                 Read_Visitor_Search_Components().start_date_checkbox_by_xpath())
            start_check_bx.click()
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.logger.info("select date time")
            start_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().start_date_by_xpath())
            self.d.execute_script("arguments[0].scrollIntoView();", start_date_txt_bx)
            start_date_txt_bx.click()

            self.logger.info("datetime clicked")
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
        else:
            # click on the to calendar pop up
            end_check_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().end_date_checkbox_by_xpath())
            end_check_bx.click()
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            end_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().end_date_by_xpath())
            self.d.execute_script("arguments[0].scrollIntoView();", end_date_txt_bx)
            end_date_txt_bx.click()
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)

        # click on the clock icon
        self.logger.info("selecting time")
        calender_clock = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().calender_timer_icon_by_xpath())
        calender_clock.click()
        self.logger.info("select time ")
        time.sleep(web_driver.one_second)
        web_driver.implicit_wait(self, web_driver.one_second, self.d)
        time.sleep(3)

        # handle the hour and minute based on the strategy
        if strategy == "from":
            self.logger.info("select in from hours and min")
            self.calender_handle_hour_minute_from(hour, minute)
        else:
            self.logger.info("select in to hours and min")
            self.calender_handle_hour_minute_to(hour, minute)

        # select the period am or pm
        period = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().period_by_xpath())
        if period.text == req_period:
            print("")
        else:
            period.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().calender_tick_icon_by_xpath())
        tick_icon.click()

        if strategy == "from":
            self.logger.info("From start date")
            start_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().start_date_by_xpath())
            start_date_txt_bx.click()
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
        else:
            # click on the to calendar pop up
            self.logger.info("To End Date")
            start_date_txt_bx = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().end_date_by_xpath())
            start_date_txt_bx.click()
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)

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
        month_year = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().calender_month_year_by_xpath())
        ac_month = month_year.text.split(" ")[0]
        ac_year = int(month_year.text.split(" ")[1])

        # click on the back button
        while month_to_num.get(req_month) < month_to_num.get(ac_month) or req_year < ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  Read_Visitor_Search_Components().calender_back_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()
            time.sleep(1)
            month_year = self.d.find_element(By.XPATH,
                                             Read_Visitor_Search_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the forward button
        while month_to_num.get(req_month) > month_to_num.get(ac_month) or req_year > ac_year:
            cal_forward_button = self.d.find_element(By.XPATH,
                                                  Read_Visitor_Search_Components().calender_forward_button_by_xpath())
            if cal_forward_button.is_enabled():
                cal_forward_button.click()
            time.sleep(1)
            month_year = self.d.find_element(By.XPATH,
                                             Read_Visitor_Search_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        time.sleep(web_driver.two_second)
        # click on the required date
        dat = self.d.find_element(By.XPATH, f"//td[contains(@class, 'day') and text()='{date}']")
        dat.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().calender_tick_icon_by_xpath())

        tick_icon.click()
        # tick_icon.click()

    def calender_handle_hour_minute_to(self, hour, minute):
        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().hour_down_by_xpath())

            self.d.execute_script("arguments[0].click();", hour_down)
            current_hour_ele = self.d.find_element(By.XPATH,
                                                   Read_Visitor_Search_Components().current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

        # set the minute
        current_min_ele = self.d.find_element(By.XPATH,
                                              Read_Visitor_Search_Components().current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)
        while int(cur_min) != int(minute):
            clock_down_button = self.d.find_element(By.XPATH,
                                                    Read_Visitor_Search_Components().clock_min_down_button_by_xpath())
            self.d.execute_script("arguments[0].click();", clock_down_button)
            current_min_ele = self.d.find_element(By.XPATH,
                                                  Read_Visitor_Search_Components().current_minute_element_by_xpath())
            cur_min = int(current_min_ele.text)

    def calender_handle_hour_minute_from(self, hour, minute):
        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        # decrementHours
        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().hour_down_by_xpath())
            self.d.execute_script("arguments[0].click();", hour_down)
            current_hour_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components()
                                                   .current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

        # set the minute
        current_min_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components()
                                              .current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)
        while int(cur_min) != int(minute):
            clock_up_button = self.d.find_element(By.XPATH, Read_Visitor_Search_Components()
                                                  .clock_min_up_button_by_xpath())
            self.d.execute_script("arguments[0].click();", clock_up_button)
            current_min_ele = self.d.find_element(By.XPATH, Read_Visitor_Search_Components()
                                                  .current_minute_element_by_xpath())
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
        date_list = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().match_date_list_by_xpath())
        ac_date = int()
        ac_month = int()
        ac_year = int()
        for x in date_list:
            dt = x.text
            b = dt.split(" ")
            ac_year = int(b[2])
        ele2 = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().no_matches_found())
        if (start_year <= ac_year <= end_year) or (ele2.is_displayed()):
            return True
        else:
            return False

    def close_all_panel_one_by_one(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    Read_Visitor_Search_Components().close_all_panel_one_by_one())
            for i in close_panel_list:
                i.click()
            return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\close_all_panel_failed_pg_03.png")
                return False

    def click_on_logout_button(self):
        try:

            # logout_button = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().logout_btn_by_xpath())

            # logout_button = self.wait_for_element_to_appear(logout_button, Read_Visitor_Search_Components().logout_btn_by_xpath())
            logout_button = web_driver.explicit_wait(self, 20, "XPATH",
                                                     Read_Visitor_Search_Components().logout_btn_by_xpath(), self.d)
            # if not logout_button.is_displayed():
            #     while not logout_button.is_displayed():
            #         time.sleep(web_driver.one_second)
            try:
                self.d.execute_script("arguments[0].click();", logout_button)
            except Exception as ex:
                logout_button.click()
                self.logger.info(f"exception: {ex}")

            self.d.delete_cookie()
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_logout_pg_03.png")
                return False

    def check_if_match_is_found(self):
        # ele = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().no_match_found_by_xpath())

        # ele = self.wait_for_element_to_appear(ele, Read_Visitor_Search_Components().no_match_found_by_xpath())
        ele = web_driver.explicit_wait(self, 20, "XPATH", Read_Visitor_Search_Components().no_match_found_by_xpath(),
                                       self.d)
        if ele.is_displayed():
            return False
        else:
            return True

    def verify_must_specify_start_date_for_metadata_only_search_meta_data_only_search_should_target_a_single_store(self):
        error_msg1 = None
        time.sleep(web_driver.one_second)
        self.logger.info("waiting for message to appear...")
        # ele_list = self.d.find_elements(By.XPATH,
        #                                 Read_Visitor_Search_Components().start_end_date_validation_msg_verify_xpath())
        # ele = self.wait_for_element_to_appear(ele_list, Read_Visitor_Search_Components().start_end_date_validation_msg_verify_xpath())
        ele = web_driver.explicit_wait(self, 20, "XPATH",
                                       Read_Visitor_Search_Components().start_end_date_validation_msg_verify_xpath(),
                                       self.d)
        time.sleep(web_driver.one_second)
        actual_validation_text = ele.text.lower()
        time.sleep(web_driver.one_second)
        print("actual_validation_text>>>.", actual_validation_text)
        self.logger.info(f"actual validation text: {actual_validation_text}")

        expected_validation_text = Read_Visitor_Search_Components().no_search_criteria_msg().strip().lower()
        print("expected_validation_text >>>", expected_validation_text)
        self.logger.info(f"Excepted Validation text: {expected_validation_text}")
        time.sleep(web_driver.one_second)
        try:
            WebDriverWait(self.d, 5).until(EC.alert_is_present())
            alert = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            error_msg1 = alert.text
            alert.accept()
            time.sleep(web_driver.one_second)
            self.logger.info("Alert accepted !!")
        except Exception as ex:
            self.logger.info(f"alert ex:")
        time.sleep(web_driver.one_second)
        self.logger.info(f"message is visible: {ele.is_displayed()}")
        self.logger.info(f"alert msg: {error_msg1}")
        time.sleep(web_driver.one_second)
        expected_alert_msg = Read_Visitor_Search_Components().connection_error()
        self.logger.info(f"expected alert msg: {expected_alert_msg}")
        images_displayed = self.verify_image_from_match_list()
        self.logger.info(f"images displayed: {images_displayed}")
        web_driver.implicit_wait(self, web_driver.one_second, self.d)
        if (ele.is_displayed() and (actual_validation_text == expected_validation_text)) or (
                error_msg1 == expected_alert_msg) or images_displayed:
            self.logger.info(f"returning: {True}")
            return True
        else:
            self.logger.info(f"returning: {False}")
            return False

    def verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_001(self):
        error_msg1 = None
        time.sleep(web_driver.one_second)
        self.logger.info("waiting for message to appear...")
        # ele_list = self.d.find_elements(By.XPATH,
        #                                 Read_Visitor_Search_Components().start_end_date_validation_msg_verify_xpath())
        # ele = self.wait_for_element_to_appear(ele_list, Read_Visitor_Search_Components().start_end_date_validation_msg_verify_xpath())
        ele = web_driver.explicit_wait(self, 20, "XPATH",
                                       Read_Visitor_Search_Components().start_end_date_validation_msg_verify_xpath(),
                                       self.d)
        time.sleep(web_driver.one_second)
        actual_validation_text = ele.text.lower()
        time.sleep(web_driver.one_second)
        print("actual_validation_text>>>.", actual_validation_text)
        self.logger.info(f"actual validation text: {actual_validation_text}")

        expected_validation_text = Read_Visitor_Search_Components().meta_data_without_date_validation_msg().strip().lower()
        print("expected_validation_text >>>", expected_validation_text)
        self.logger.info(f"Excepted Validation text: {expected_validation_text}")
        time.sleep(web_driver.one_second)
        try:
            WebDriverWait(self.d, 5).until(EC.alert_is_present())
            alert = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            error_msg1 = alert.text
            alert.accept()
            time.sleep(web_driver.one_second)
            self.logger.info("Alert accepted !!")
        except Exception as ex:
            self.logger.info(f"alert ex:")
        time.sleep(web_driver.one_second)
        self.logger.info(f"message is visible: {ele.is_displayed()}")
        self.logger.info(f"alert msg: {error_msg1}")
        time.sleep(web_driver.one_second)
        expected_alert_msg = Read_Visitor_Search_Components().connection_error()
        self.logger.info(f"expected alert msg: {expected_alert_msg}")
        images_displayed = self.verify_image_from_match_list()
        self.logger.info(f"images displayed: {images_displayed}")
        web_driver.implicit_wait(self, web_driver.one_second, self.d)
        if (ele.is_displayed() and (actual_validation_text == expected_validation_text)) or (
                error_msg1 == expected_alert_msg) or images_displayed:
            self.logger.info(f"returning: {True}")
            return True
        else:
            self.logger.info(f"returning: {False}")
            return False

    def verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_002(self):
        error_msg1 = None
        time.sleep(web_driver.one_second)
        web_driver.implicit_wait(self, web_driver.one_second, self.d)
        status = []
        self.logger.info("waiting for message to appear...")
        # ele = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().start_end_date_validation_msg_verify_xpath())

        # ele = self.wait_for_element_to_appear(ele, Read_Visitor_Search_Components().start_end_date_validation_msg_verify_xpath())
        ele = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_Components().start_end_date_validation_msg_verify_xpath(), self.d)
        actual_validation_text = ele.text
        self.logger.info(f"actual validation text: {actual_validation_text}")
        expected_validation_text = Read_Visitor_Search_Components().meta_data_without_date_validation_msg_tc_vs_002().strip()
        self.logger.info(f"Excepted Validation text: {expected_validation_text}")
        time.sleep(web_driver.one_second)
        try:
            WebDriverWait(self.d, 5).until(EC.alert_is_present())
            alert = self.d.switch_to.alert
            time.sleep(web_driver.one_second)
            error_msg1 = alert.text
            alert.accept()
            time.sleep(web_driver.one_second)
            self.logger.info("Alert accepted !!")
        except Exception as ex:
            self.logger.info(f"alert ex: {ex.args}")
        time.sleep(web_driver.one_second)
        self.logger.info(f"message is visible: {ele.is_displayed()}")
        self.logger.info(f"alert msg: {error_msg1}")
        expected_alert_msg = Read_Visitor_Search_Components().connection_error()
        time.sleep(web_driver.one_second)
        self.logger.info(f"expected alert msg: {expected_alert_msg}")

        if ele.is_displayed():
            self.logger.info(f"appending: {True}")
            status.append(True)
        else:
            self.logger.info(f"appending: {False}")
            status.append(False)

        self.logger.info(f"status: {status}")
        if False in status:
            return False
        else:
            return True

    def verify_Meta_data_only_search_should_target_a_single_store(self):
        error_msg1 = None
        time.sleep(web_driver.one_second)
        web_driver.implicit_wait(self, web_driver.one_second, self.d)
        self.logger.info("waiting for message to appear...")
        ele = web_driver.explicit_wait(self, 20, "XPATH",
                                       Read_Visitor_Search_Components().start_end_date_validation_msg_verify_xpath(),
                                       self.d)
        actual_validation_text = ele.text.lower()
        self.logger.info(f"actual validation text: {actual_validation_text}")
        expected_validation_text = Read_Visitor_Search_Components().meta_data_without_date_validation_msg().strip().lower()
        self.logger.info(f"Excepted Validation text: {expected_validation_text}")
        self.logger.info(f"message is visible: {ele.is_displayed()}")
        self.logger.info(f"alert msg: {error_msg1}")
        expected_alert_msg = Read_Visitor_Search_Components().connection_error()
        self.logger.info(f"expected alert msg: {expected_alert_msg}")
        if (ele.is_displayed() and (actual_validation_text == expected_validation_text)) or (
                error_msg1 == expected_alert_msg):
            self.logger.info(f"returning: {True}")
            return True
        else:
            self.logger.info(f"returning: {False}")
            return False

    def verify_Must_specify_start_and_end_date_for_meta_data_only_search_TC_VS_003(self):
        error_msg1 = None
        time.sleep(web_driver.one_second)
        web_driver.implicit_wait(self, web_driver.one_second, self.d)
        self.logger.info("waiting for message to appear...")
        # ele = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().start_end_date_validation_msg_verify_xpath())
        # ele = self.wait_for_element_to_appear(ele, Read_Visitor_Search_Components().start_end_date_validation_msg_verify_xpath())
        ele = web_driver.explicit_wait(self, 20, "XPATH",
                                       Read_Visitor_Search_Components().start_end_date_validation_msg_verify_xpath(),
                                       self.d)
        actual_validation_text = ele.text.lower()
        self.logger.info(f"actual validation text: {actual_validation_text}")
        expected_validation_text = Read_Visitor_Search_Components().meta_data_without_date_validation_msg_tc_vs_003().strip().lower()
        self.logger.info(f"Excepted Validation text: {expected_validation_text}")
        time.sleep(web_driver.one_second)
        try:
            WebDriverWait(self.d, 5).until(EC.alert_is_present())
            alert = self.d.switch_to.alert
            error_msg1 = alert.text
            alert.accept()
            self.logger.info("Alert accepted !!")
        except Exception as ex:
            self.logger.info(f"alert ex: {ex.args}")
        time.sleep(web_driver.two_second)
        self.logger.info(f"message is visible: {ele.is_displayed()}")
        self.logger.info(f"alert msg: {error_msg1}")
        expected_alert_msg = Read_Visitor_Search_Components().connection_error()
        self.logger.info(f"expected alert msg: {expected_alert_msg}")
        if (ele.is_displayed() and (actual_validation_text == expected_validation_text)) or (
                error_msg1 == expected_alert_msg) :
            self.logger.info(f"returning: {True}")
            return True
        else:
            self.logger.info(f"returning: {False}")
            return False

    def verify_limited_to_30_min_interval_validation(self):
        ele = self.d.find_elements(By.XPATH, Read_Visitor_Search_Components().limited_to_30_min_interval_validation())
        # ele = self.wait_for_element_to_appear(ele, Read_Visitor_Search_Components().limited_to_30_min_interval_validation())
        ele = web_driver.explicit_wait(self, 20, "XPATH",
                                       Read_Visitor_Search_Components().limited_to_30_min_interval_validation(), self.d)
        actutal_validation_text = ele.text.lower()
        expected_validation_text = Read_Visitor_Search_Components().limited_to_30_meta_data_search_validation().strip().lower()
        print(actutal_validation_text)
        print(expected_validation_text)
        if ele.is_displayed() and actutal_validation_text == expected_validation_text:
            return True
        else:
            return False

    def nats_checkbox(self):
        """
        This function is used to enable and disable NATS
        :param end_age:
        :return:
        """
        time.sleep(web_driver.one_second)
        NATS_checkbox = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().nats_checkbox_xpath())
        NATS_checkbox.click()
        time.sleep(web_driver.one_second)
        self.logger.info("Clicked on NATS checkbox..")

    def verify_max_matches_not_display(self):
        """
        This function is used validate the max matches element
        :return:
        """
        time.sleep(web_driver.one_second)
        try:
            max_matches = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().max_of_matches_by_xpath())
            time.sleep(web_driver.one_second)
            if not max_matches.is_displayed():
                return True
            else:
                return False
        except Exception as ex:
            return True

    def verify_threshold_not_display(self):
        """
        This function is used validate the threshold element
        :return:
        """
        time.sleep(web_driver.one_second)
        try:
            threshold = web_driver.explicit_wait(self, 20, "XPATH",
                                                 Read_Visitor_Search_Components().threshold_slider_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            if not threshold.is_displayed():
                return True
            else:
                return False
        except Exception as ex:
            return True

    def get_start_date(self):
        try:
            # self.get_date_range_from_json()
            # start_date_checkbox = web_driver.explicit_wait(self, 10, "XPATH", Read_Visitor_Search_Components().vs_start_date_check_bx(), self.d)
            # start_date_checkbox = web_driver.explicit_wait_for_stale_element(self, 10, "XPATH", Read_Visitor_Search_Components().vs_start_date_check_bx(), self.d)
            # start_date_checkbox.click()
            # time.sleep(web_driver.one_second)
            # start_date_calender_box = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().get_start_date_calender_box_by_xpath())
            # start_date_calender_box = web_driver.explicit_wait_for_stale_element(self, 10, "XPATH", Read_Visitor_Search_Components().get_start_date_calender_box_by_xpath(), self.d)
            # default_start_date = start_date_calender_box.get_attribute('value')
            # default_start_date = list(default_start_date.split(' '))
            # print("default start date: ", default_start_date)
            # d_start_date = default_start_date[0]
            # d_start_time = default_start_date[1]
            # d_time = list(d_start_time.split(':'))
            # d_hour = d_time[0]
            # d_min = d_time[1]
            # d_start_am_pm = default_start_date[2]
            # d_start_date = list(d_start_date.split('/'))
            # s_month = d_start_date[0]
            # s_date = d_start_date[1]
            # self.logger.info(f"default start date: {d_start_date}")
            # self.logger.info(f"default start time: {d_start_time}")
            # self.logger.info(f"default am and pm : {d_start_am_pm}")
            # self.logger.info(f"start date from json: {self.start_date}")
            # self.logger.info(f"start time from json: {self.start_time}")
            # self.logger.info(f"start am and pm from json: {self.start_am_pm}")

            # time.sleep(web_driver.one_second)
            # start_date_calender_box.send_keys(self.start_date)
            # time.sleep(web_driver.one_second)
            # start_date_calender_box.send_keys(self.start_time)
            # time.sleep(web_driver.one_second)
            # start_date_calender_box.send_keys(self.start_am_pm)
            # time.sleep(web_driver.one_second)

            # start_date_calender_box.click()
            # action = ActionChains(self.d)
            # time.sleep(web_driver.one_second)
            # default_start_date = start_date_calender_box.get_attribute('value')
            # default_start_date = list(default_start_date.split(' '))
            # print("default start date: ", default_start_date)
            # 
            # d_start_date = default_start_date[0]
            # d_start_time = default_start_date[1]
            # d_start_am_pm = default_start_date[2]
            # d_start_date = list(d_start_date.split('/'))
            # s_month = d_start_date[0]
            # s_date = d_start_date[1]
            # self.logger.info(f"default start date: {d_start_date}")
            # self.logger.info(f"default start time: {d_start_time}")
            # self.logger.info(f"default am and pm : {d_start_am_pm}")
            # self.logger.info(f"start date from json: {self.start_date}")
            # self.logger.info(f"start time from json: {self.start_time}")
            # self.logger.info(f"start am and pm from json: {self.start_am_pm}")
            # 
            # input_start_date = list(self.start_date.split('/'))
            # input_s_date = input_start_date[0]
            # input_s_month = input_start_date[1]
            # input_s_year = input_start_date[2]
            # input_start_time = list(self.start_time.split(':'))
            # input_hour = input_start_time[0]
            # input_min = input_start_time[1]
            # 
            # print(input_s_date, input_s_month, input_s_year, "Input start date: ", input_start_date)
            # status = True
            # print("s_month < input_s_month ", s_month < input_s_month)
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
            # 
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
                self.logger.info(f"select date range got an exception as: {ex}")

        except Exception as ex:
            self.logger.error("start date method exception")
            self.logger.error(ex)

    def get_end_date(self):
        try:
            self.get_date_range_from_json()
            end_date_calender_box = web_driver.explicit_wait(self, 10, "XPATH", Reporting_read_ini().get_end_date_calender_box_by_xpath(), self.d)
            end_date_calender_box = web_driver.explicit_wait_for_stale_element(self, 10, "XPATH", Reporting_read_ini().get_end_date_calender_box_by_xpath(), self.d)
            end_date_checkbox = self.d.find_element(By.XPATH, Read_Visitor_Search_Components().vs_end_date_check_bx())
            end_date_checkbox = web_driver.explicit_wait_for_stale_element(self, 10, "XPATH", Read_Visitor_Search_Components().vs_end_date_check_bx(), self.d)
            time.sleep(web_driver.one_second)
            end_date_checkbox.click()
            time.sleep(web_driver.one_second)
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

    def get_date_range_from_json(self):
        try:
            df_custom_dates = pd.read_json(self.custom_dates_json)
            # self.logger.info(f"Search Dates given: {df_custom_dates}")
            self.start_date_and_time = list({df_custom_dates['date_range'][0]['start_date']})
            for items in self.start_date_and_time:
                items = items.split(' ')
                # self.start_date = items[0]
                self.start_date = f"{Read_Visitor_Search_Components().get_start_date()}/{Read_Visitor_Search_Components().get_start_month()}/{Read_Visitor_Search_Components().get_start_year()}"
                self.logger.info(f"start date taken from Json: {self.start_date}")
                # self.start_time = items[1]
                self.start_time = f"{Read_Visitor_Search_Components().get_start_hour()}:{Read_Visitor_Search_Components().get_start_minuet()}"
                self.logger.info(f"start time taken from Json: {self.start_time}")
                # self.start_am_pm = items[2]
                self.start_am_pm = f"{Read_Visitor_Search_Components().get_start_am_pm_period()}"
                self.logger.info(f"start am/pm from json: {self.start_am_pm}")
            self.logger.info(f"start date: {self.start_date} {self.start_time} {self.start_am_pm}")
            # self.end_date_and_time = list({df_custom_dates['date_range'][0]['end_date']})
            for items in self.end_date_and_time:
                items = items.split(' ')
                # self.end_date = items[0]
                self.end_date = f"{Read_Visitor_Search_Components().get_end_date()}/{Read_Visitor_Search_Components().get_end_month()}/{Read_Visitor_Search_Components().get_end_year()}"
                # self.end_time = items[1]
                self.end_time = f"{Read_Visitor_Search_Components().get_end_hour()}:{Read_Visitor_Search_Components().get_end_minuet()}"
                # self.end_datetime = items[2]
                self.end_datetime = f"{Read_Visitor_Search_Components().get_end_am_pm_period()}"
            self.logger.info(f"end date: {self.end_date}{self.end_time}{self.end_datetime}")
        except Exception as ex:
            self.logger.error(ex)
