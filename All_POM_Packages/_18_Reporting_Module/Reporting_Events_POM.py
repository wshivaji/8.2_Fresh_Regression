from pathlib import Path

import time
import pandas as pd

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login
from All_Config_Packages._18_Reporting_Module_Config_Files.Reporting_Read_INI import Reporting_read_ini
from All_POM_Packages._18_Reporting_Module.Reporting_POM import Reporting_pom
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import Portal_Menu_Module_read_ini


class Reporting_Events_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    def __init__(self):
        self.end_datetime = self.end_time = self.end_date = self.end_date_and_time = self.start_datetime = \
            self.start_age = self.age_bucket = None
        self.start_time = self.start_date = self.start_date_and_time = self.groups = self.zones = self.end_age = None
        self.age_range_zones_groups_xlsx = \
            f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\18_Reporting_Module\\Data_From_Excel\\age_range_zones_groups_xlsx.xlsx"
        self.custom_dates_json = \
            f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\18_Reporting_Module\\Data_From_JSON\\custom_dates_json.json"

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

    def load_reporting_module(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            reporting_module = self.d.find_element(By.XPATH, Reporting_read_ini().get_reporting_module_by_xpath())
            if reporting_module.is_displayed():
                reporting_module.click()
                time.sleep(web_driver.one_second)
                panel_heading = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                    get_reporting_panel_heading_by_xpath())
            else:
                pass
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)
    
    def load_reporting_module_for_admin(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            reporting_module = self.explicit_wait(10, "XPATH", Reporting_read_ini().get_reporting_module_by_xpath(), self.d)
            if reporting_module.is_displayed():
                reporting_module.click()
                time.sleep(web_driver.one_second)
                panel_heading = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                    get_reporting_panel_heading_by_xpath())
            else:
                pass
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)
    
    def get_age_range(self):
        try:
            df_age_range = pd.read_excel(self.age_range_zones_groups_xlsx, sheet_name='age_range',
                                         names=['Start Age', 'End Age', 'Age Bucket'])
            df_zones = pd.read_excel(self.age_range_zones_groups_xlsx, sheet_name='zones', names=['Zones'])
            df_groups = pd.read_excel(self.age_range_zones_groups_xlsx, sheet_name='groups', names=['Groups'])
            self.start_age = [x for x in df_age_range['Start Age']]
            self.end_age = [y for y in df_age_range['End Age']]
            self.age_bucket = [z for z in df_age_range['Age Bucket']]
            self.zones = [x for x in df_zones['Zones']]
            self.groups = [x for x in df_groups['Groups']]
            # print(f"start age: {self.start_age}" f"length: {len(self.start_age)}")
            # print(f"df age range: {df_age_range}")
            # print(f"df zones: {df_zones}")
            # print(f"df groups: {df_groups}")
        except Exception as ex:
            self.logger.error(ex)

    def select_number_of_events_by_enrollment(self):
        try:
            time.sleep(web_driver.three_second)
            field1 = self.explicit_wait(10, "XPATH", Reporting_read_ini().get_report_field1_dropdown_by_xpath(), self.d)
            field2 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field2_dropdown_for_events_by_xpath())
            if field2.is_displayed():
                pass
            else:
                print("enter else >>>>>>>>.")
                field1_dropdown = Select(field1)
                time.sleep(web_driver.one_second)
                field1_dropdown.select_by_visible_text('number of probable match events')
                field2_dropdown = Select(field2)
                time.sleep(web_driver.one_second)
                field2_dropdown.select_by_visible_text('enrollment')
                time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def For_number_of_events_by_enrollment_verify_number_of_events_from_report_field1_and_enrollment_from_report_field2_texts_are_visible_on_dropdown(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_220 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            time.sleep(web_driver.one_second)
            field1.select_by_visible_text('number of probable match events')

            value1 = self.d.find_element(By.XPATH,
                                         Reporting_read_ini().get_report_field1_dropdown_by_xpath()).get_attribute(
                'value')
            self.logger.info(f"Value1: {value1}")
            if "number of events" in value1:
                self.logger.info("Selected 'number of events' from report field1 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            field2 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_report_field2_dropdown_for_events_by_xpath()))
            field2.select_by_visible_text('enrollment')

            value2 = self.d.find_element(By.XPATH, Reporting_read_ini().
                                         get_report_field2_dropdown_for_events_by_xpath()).get_attribute(
                'value')
            self.logger.info(f"Value2: {value2}")
            if Reporting_read_ini().get_expected_enrollment_text_from_field2() in value2:
                self.logger.info("Selected 'enrollment' from report field2 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_220.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_220.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_220_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_220_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_220 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_boxes_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_221 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_enrollment()
            actual_date_and_time_range_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                  get_date_and_time_range_text_by_xpath()).text
            self.logger.info(f"actual date & time range text: {actual_date_and_time_range_text}")
            expected_date_range_text = Reporting_read_ini().get_expected_date_and_time_range_text()
            self.logger.info(f"expected date & time range text: {expected_date_range_text}")
            if actual_date_and_time_range_text == expected_date_range_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_to_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_to_text_by_xpath()).text
            self.logger.info(f"actual 'to' text: {actual_to_text}")
            expected_to_text = Reporting_read_ini().get_expected_to_text()
            self.logger.info(f"expected 'to' text: {expected_to_text}")
            if actual_to_text == expected_to_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_horizontal_line_below_calenders = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_horizontal_line_below_calenders_by_xpath()).text
            self.logger.info(f"actual horizontal line below calenders: {actual_horizontal_line_below_calenders}")
            expected_horizontal_line_below_calenders = Reporting_read_ini(). \
                get_expected_horizontal_line_below_calenders()
            self.logger.info(f"expected horizontal line below calenders: {expected_horizontal_line_below_calenders}")
            if actual_horizontal_line_below_calenders == expected_horizontal_line_below_calenders:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_221.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_221.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_221_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_221_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_221 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()
            

    def For_number_of_events_by_enrollment_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_222 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_enrollment()
            start_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_start_date_calender_box_by_xpath())
            if start_date_calender_box.is_displayed():
                self.logger.info("Start date calender box is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if start_date_calender_box.is_enabled():
                self.status.append(False)
            else:
                self.logger.info("start date calender box is disabled by default !!")
                self.status.append(True)
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            if start_date_checkbox.is_displayed():
                self.logger.info("Start date checkbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if start_date_checkbox.is_enabled():
                self.logger.info("Start date checkbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_222.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_222.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_222_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_222_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_222 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_223 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_enrollment()
            end_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_end_date_calender_box_by_xpath())
            if end_date_calender_box.is_displayed():
                self.logger.info("End date calender box is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if end_date_calender_box.is_enabled():
                self.status.append(False)
            else:
                self.logger.info("End date calender box is disabled by default !!")
                self.status.append(True)
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            if end_date_checkbox.is_displayed():
                self.logger.info("End date checkbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if end_date_checkbox.is_enabled():
                self.logger.info("End date checkbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_223.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_223.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_223_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_223_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_223 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_224 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_enrollment()
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            start_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_start_date_calender_box_by_xpath())
            start_calender_disabled_status = start_date_calender_box.get_attribute("disabled")
            if start_date_checkbox.is_selected():
                start_date_checkbox.click()
                if start_calender_disabled_status:
                    self.logger.info("start calender disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"start date disable status: {start_calender_disabled_status}")
                if start_calender_disabled_status:
                    self.logger.info("start calender already disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            start_date_checkbox.click()
            self.logger.info(f"start calender disable status after click: "
                             f"{start_date_calender_box.get_attribute('disabled')}")
            if start_date_calender_box.get_attribute("disabled") is None:
                self.logger.info("start calender enabled !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if start_date_checkbox.is_selected():
                start_date_checkbox.click()
            else:
                pass
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_224.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_224.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_224_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_224_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_224 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_225 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_enrollment()
            end_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_end_date_calender_box_by_xpath())
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            end_calender_disabled_status = end_date_calender_box.get_attribute("disabled")
            if end_date_checkbox.is_selected():
                end_date_checkbox.click()
                if end_calender_disabled_status:
                    self.logger.info("End calender disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"End calender disable status: {end_calender_disabled_status}")
                if end_calender_disabled_status:
                    self.logger.info("End calender already disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            end_date_checkbox.click()
            self.logger.info(f"End calender disable status after click: "
                             f"{end_date_calender_box.get_attribute('disabled')}")
            if end_date_calender_box.get_attribute("disabled") is None:
                self.logger.info("End calender enabled !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if end_date_checkbox.is_selected():
                end_date_checkbox.click()
            else:
                pass
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_225.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_225.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_225_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_225_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_225 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_226 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_enrollment()
            action = ActionChains(self.d)
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            start_checkbox_hover = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                       get_include_in_search_hover_on_start_checkbox_by_xpath())
            action.move_to_element(start_date_checkbox).perform()
            if start_checkbox_hover.get_attribute("aria-describedby"):
                self.logger.info("'Include In Search' hover is visible for start date checkbox !!")
                self.status.append(True)
            else:
                self.logger.error("'Include In Search' hover is not visible for start date checkbox !!")
                self.status.append(False)
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            end_checkbox_hover = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                     get_include_in_search_hover_on_end_checkbox_by_xpath())
            action.move_to_element(end_date_checkbox).perform()
            if end_checkbox_hover.get_attribute("aria-describedby"):
                self.logger.info("'Include In Search' hover is visible for end date checkbox !!")
                self.status.append(True)
            else:
                self.logger.error("'Include In Search' hover is not visible for end date checkbox !!")
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_226.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_226.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_226_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_226_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_226 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_verify_Optional_Filter_text_is_visible_text_beside_Select_group_filter_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_227 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_enrollment()
            time.sleep(web_driver.one_second)
            actual_optional_filter_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                              get_optional_filters_text_by_xpath()).text
            self.logger.info(f"actual optional filter text: {actual_optional_filter_text}")
            expected_optional_filters_text = Reporting_read_ini().get_expected_optional_filters_text()
            self.logger.info(f"expected optional filter text: {expected_optional_filters_text}")
            if actual_optional_filter_text in expected_optional_filters_text:
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            actual_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                              get_text_beside_select_group_filter_button_by_xpath()).text
            self.logger.info(f"actual text: {actual_text}")
            expected_text = Reporting_read_ini().get_expected_text_beside_select_group_filter_button()
            self.logger.info(f"expected text: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_227.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_227.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_227_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_227_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_227 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_verify_Select_group_filter_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_228 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_enrollment()
            time.sleep(web_driver.one_second)
            select_group_filter_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                             get_select_group_filter_button_by_xpath())
            if select_group_filter_button.is_displayed():
                self.logger.info("Select group filter button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if select_group_filter_button.is_enabled():
                self.logger.info("Select group filter button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                              get_select_group_filter_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on Select group filter button: {actual_text}")
            expected_text = Reporting_read_ini().get_expected_text_on_select_group_filter_button()
            self.logger.info(f"expected text on Select group filter button: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            group_icon_on_select_grp_btn = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                               get_group_icon_on_select_group_filter_button_by_xpath())
            if group_icon_on_select_grp_btn.is_displayed():
                self.logger.info("group icon on Select group filter button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_228.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_228.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_228_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_228_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_228 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_verify_generate_report_button_is_visible_and_clickable_generate_report_text_and_chart_icon_both_are_visible_on_button(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_229 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_enrollment()
            generate_report_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                         get_generate_report_button_by_xpath())
            if generate_report_button.is_displayed():
                self.logger.info("Generate report button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if generate_report_button.is_enabled():
                self.logger.info("Generate report button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_chart_icon_on_generate_report_button_by_xpath()).\
                    is_displayed():
                self.logger.info("chart icon on Generate report button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_generate_report_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on Generate report button: {actual_text_on_generate_report_button}")
            expected_text_on_generate_report_button = Reporting_read_ini().get_expected_generate_report_text_on_button()
            self.logger.info(f"expected text on Generate report button: {expected_text_on_generate_report_button}")
            if actual_text_on_generate_report_button == expected_text_on_generate_report_button:
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_229.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_229.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_229_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_229_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_229 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_in_Select_group_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_230 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_enrollment()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_horizontal_line_below_reporting_panel_heading = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_horizontal_line_below_reporting_panel_heading_for_group_by_xpath()).text
            self.logger.info(f"actual horizontal line below panel heading: "
                             f"{actual_horizontal_line_below_reporting_panel_heading}")
            expected_horizontal_line_below_reporting_panel_heading = Reporting_read_ini(). \
                get_expected_horizontal_line_below_reporting_panel_heading_for_group()
            self.logger.info(f"expected horizontal line below panel heading: "
                             f"{expected_horizontal_line_below_reporting_panel_heading}")
            if actual_horizontal_line_below_reporting_panel_heading == \
                    expected_horizontal_line_below_reporting_panel_heading:
                self.logger.info("Horizontal line below panel heading is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_230.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_230.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_230_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_230_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_230 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_verify_filter_group_list_below_textbox_is_visible_and_clickable_label_on_textbox_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_231 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_events_by_enrollment()
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            filter_group_list_textbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                            get_filter_group_list_textbox_by_xpath())
            if filter_group_list_textbox.is_displayed():
                self.logger.info("'filter group list below..' textbox is visible")
                self.status.append(True)
            else:
                self.status.append(False)
            if filter_group_list_textbox.is_enabled():
                self.logger.info("'filter group list below..' textbox is clickable")
                self.status.append(True)
            else:

                self.status.append(False)
            filter_group_list_textbox.click()
            actual_label_on_textbox = filter_group_list_textbox.get_attribute('placeholder')
            self.logger.info(f"actual label on textbox: {actual_label_on_textbox}")
            expected_label_on_textbox = Reporting_read_ini().get_expected_label_on_filter_group_list_below_textbox()
            self.logger.info(f"expected label on textbox: {expected_label_on_textbox}")
            if actual_label_on_textbox == expected_label_on_textbox:
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_231.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_231.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_231_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_231_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_231 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_verify_group_list_below_filter_group_list_textbox_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_232 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_events_by_enrollment()
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                    get_group_items_list_below_filter_group_list_textbox())
            self.logger.info(f"Group items below 'filter group list' textbox: {len(group_items_list)}")
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH,
                                Reporting_read_ini().get_enrollment_groups_module_on_dashboard_by_xpath()).click()
            time.sleep(web_driver.three_second)
            actual_group_list_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                           get_group_item_list_from_enrollment_group_panel_by_xpath())
            time.sleep(web_driver.one_second)
            self.logger.info(f"Actual group items from 'Enrollment Groups': {len(actual_group_list_items)}")
            if len(group_items_list) == len(actual_group_list_items):

                self.logger.info("Group list items are visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            '''''
            for items in group_items_list:
                if items.is_displayed():
                    self.status.append(True)
                else:
                    self.status.append(False)
                if items.is_enabled():
                    self.status.append(True)
                else:
                    self.status.append(False)
            '''''
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_232.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_232.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_232_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_232_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_232 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_verify_select_all_button_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_233 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_events_by_enrollment()
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            select_all_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                    get_select_all_button_in_group_filter_by_xpath())
            if select_all_button.is_displayed():
                self.logger.info("'Select all' button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if select_all_button.is_enabled():
                self.logger.info("'Select all' button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_select_all_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_select_all_button_in_group_filter_by_xpath()).text
            self.logger.info(f"actual text on select all button in group filter: {actual_text_on_select_all_button}")
            self.logger.info(f"expected text on select all button in group filter: "
                             f"{Reporting_read_ini().get_expected_text_on_select_all_button()}")
            if actual_text_on_select_all_button == Reporting_read_ini().get_expected_text_on_select_all_button():
                self.logger.info("text on Select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_233.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_233.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_233_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_233_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_233 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_verify_selected_group_list_title_and_default_text_below_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_234 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_events_by_enrollment()
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_selected_group_list_title = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual title: {actual_selected_group_list_title}")
            self.logger.info(f"expected title: {Reporting_read_ini().get_expected_selected_group_list_title()}")
            if actual_selected_group_list_title == Reporting_read_ini().get_expected_selected_group_list_title():
                self.logger.info("'Selected group list' title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_first_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_first_default_te_below_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual first horizontal line: {actual_first_horizontal_line}")
            expected_first_horizontal_line = \
                Reporting_read_ini().get_expected_first_default_text_line_below_selected_group_list_title()
            self.logger.info(f"expected first horizontal line: {expected_first_horizontal_line}")
            if actual_first_horizontal_line == expected_first_horizontal_line:
                self.logger.info("First default text line below selected group list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_second_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_second_default_text_below_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual second default text line below 'Selected group list' title: "
                             f"{actual_second_horizontal_line}")
            expected_second_horizontal_line = \
                Reporting_read_ini().get_expected_second_default_text_line_below_selected_group_list_title()
            self.logger.info(f"expected second horizontal line: {expected_second_horizontal_line}")
            if actual_second_horizontal_line == expected_second_horizontal_line:
                self.logger.info("Second default text line below selected group list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_234.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_234.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_234_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_234_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_234 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_verify_close_group_menu_button_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_235 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_events_by_enrollment()
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            close_group_menu_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_close_group_menu_button_by_xpath())
            if close_group_menu_button.is_displayed():
                self.logger.info("'Close group menu' button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if close_group_menu_button.is_enabled():
                self.logger.info("'Close group menu' button is enabled !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_close_group_menu_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_text_on_close_group_menu_button_by_xpath()).text
            self.logger.info(f"actual text on close menu btn: {actual_text_on_close_group_menu_button}")
            expected_text_on_close_group_button = Reporting_read_ini().get_expected_text_on_close_group_menu_button()
            self.logger.info(f"expected text on close menu btn: {expected_text_on_close_group_button}")
            if actual_text_on_close_group_menu_button == expected_text_on_close_group_button:
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_235.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_235.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_235_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_235_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_235 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_click_on_select_all_button_and_verify_all_selected_groups_are_visible_in_selected_group_list(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_236 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_events_by_enrollment()
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_items_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_group_items_list_below_filter_group_list_textbox())
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)
            selected_group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_selected_group_list_items_by_xpath())
            if len(selected_group_list) == len(group_items_list):
                self.logger.info("All selected groups are visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_group_by_xpath()).\
                click()
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_236.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_236.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_236_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_236_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_236 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_click_on_select_all_button_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_237 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_events_by_enrollment()
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            clear_all_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_clear_all_button_on_selected_group_by_xpath())
            if clear_all_button.is_displayed():
                self.logger.info("'Clear all' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if clear_all_button.is_enabled():
                self.logger.info("'Clear all' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_clear_all_button_on_selected_group_by_xpath()).text
            self.logger.info(f"actual text on 'Clear all' button: {actual_text_on_button}")
            self.logger.info(f"expected text on 'Clear all' button: "
                             f"{Reporting_read_ini().get_expected_clear_all_text()}")
            if actual_text_on_button == Reporting_read_ini().get_expected_clear_all_text():
                self.logger.info("text on 'Clear all' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_group_by_xpath()).\
                click()
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_237.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_237.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_237_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_237_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_237 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_click_on_select_all_button_and_verify_save_group_selection_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_238 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_events_by_enrollment()
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            save_group_selection_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                              get_save_group_selection_button_by_xpath())
            if save_group_selection_button.is_displayed():
                self.logger.info("'Save group selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if save_group_selection_button.is_enabled():
                self.logger.info("'Save group selection' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH,
                                   Reporting_read_ini().get_group_icon_on_save_group_selection_button_by_xpath()).\
                    is_displayed():
                self.logger.info("group icon on 'Save group selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_save_group_selection_text_by_xpath()).text
            self.logger.info(f"actual text on 'Save group selection' button: {actual_text_on_button}")
            expected_text = Reporting_read_ini().get_expected_text_on_save_group_selection_button()
            self.logger.info(f"expected text on button: {expected_text}")
            if actual_text_on_button == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_group_by_xpath()).\
                click()
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_238.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_238.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_238_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_238_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_238 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_select_one_group_from_group_list_and_verify_selected_group_is_visible_in_selected_group_list_verify_save_group_selection_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_239 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_events_by_enrollment()
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_group_items_list_below_filter_group_list_textbox())
            first_group_name = group_list[0].text
            group_list[0].click()
            self.logger.info("Selected first group from groups list...")
            time.sleep(web_driver.one_second)
            selected_group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_selected_group_list_items_by_xpath())
            if first_group_name == selected_group_list[0].text:
                self.logger.info("Selected group is visible in Selected group list...")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH,
                                   Reporting_read_ini().get_save_group_selection_button_by_xpath()).is_displayed():
                self.logger.info("'Save group selection' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_group_by_xpath()).\
                click()
            # time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_239.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_239.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_239_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_239_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_239 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_click_on_save_group_selection_button_with_at_least_one_group_selected_and_verify_View_and_edit_groups_button_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_240 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_events_by_enrollment()
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            group_list[0].click()
            self.logger.info("Selected first group from group list...")
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save group selection' button...")
            time.sleep(web_driver.one_second)

            view_edit_groups_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_view_and_edit_groups_button_by_xpath())
            if view_edit_groups_button.is_displayed():
                self.logger.info("'View & edit GROUPS' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if view_edit_groups_button.is_enabled():
                self.logger.info("'View & edit GROUPS' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_240.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_240.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_240_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_240_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_240 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_enrollment_verify_text_and_numeric_value_of_number_of_selected_groups_on_view_and_edit_groups_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_EN_241 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_enrollment()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            group_list[0].click()
            self.logger.info("Selected first group from group list...")
            group_list[1].click()
            self.logger.info("Selected second group from group list...")
            time.sleep(web_driver.one_second)
            selected_groups = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_selected_group_list_items_by_xpath())
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save group selection' button...")
            time.sleep(web_driver.one_second)
            actual_text_on_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_view_and_edit_groups_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on button: {actual_text_on_button}")
            expected_numeric_value_of_group_selected = f"{len(selected_groups)}" + " " + "selected"

            if Reporting_read_ini().get_expected_text_on_view_and_edit_groups_button() in actual_text_on_button:
                self.logger.info("'View & edit GROUPS' text is visible on button...")
                self.status.append(True)
            else:
                self.status.append(False)
            if expected_numeric_value_of_group_selected in actual_text_on_button:
                self.logger.info(f"numeric value of expected selected groups: "
                                 f"{expected_numeric_value_of_group_selected}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_241.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_241.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_241_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_241_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_241 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def select_number_of_events_by_hour_of_day(self):
        try:
            time.sleep(web_driver.one_second)
            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            time.sleep(web_driver.one_second)
            field1.select_by_visible_text('number of probable match events')
            field2 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_report_field2_dropdown_for_events_by_xpath()))
            time.sleep(web_driver.one_second)
            field2.select_by_visible_text('hour of day')
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def For_number_of_events_by_hour_of_day_verify_number_of_events_from_report_field1_and_hour_of_day_from_report_field2_texts_are_visible_on_dropdown(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_242 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            time.sleep(web_driver.two_second)
            field1.select_by_visible_text('number of probable match events')

            value1 = self.d.find_element(By.XPATH,
                                         Reporting_read_ini().get_report_field1_dropdown_by_xpath()).get_attribute(
                'value')
            self.logger.info(f"Value1: {value1}")
            if "number of events" in value1:
                self.logger.info("Selected 'number of events' from report field1 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            field2 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_report_field2_dropdown_for_events_by_xpath()))
            field2.select_by_visible_text('hour of day')

            value2 = self.d.find_element(By.XPATH, Reporting_read_ini().
                                         get_report_field2_dropdown_for_events_by_xpath()).get_attribute(
                'value')
            self.logger.info(f"Value2: {value2}")
            if Reporting_read_ini().get_expected_first_text_from_field2() in value2:
                self.logger.info("Selected 'hour of day' from report field2 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_242.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_242.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_242_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_242_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_242 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_boxes_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_243 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            actual_date_and_time_range_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                  get_date_and_time_range_text_by_xpath()).text
            self.logger.info(f"actual date & time range text: {actual_date_and_time_range_text}")
            expected_date_range_text = Reporting_read_ini().get_expected_date_and_time_range_text()
            self.logger.info(f"expected date & time range text: {expected_date_range_text}")
            if actual_date_and_time_range_text == expected_date_range_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_to_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_to_text_by_xpath()).text
            self.logger.info(f"actual 'to' text: {actual_to_text}")
            expected_to_text = Reporting_read_ini().get_expected_to_text()
            self.logger.info(f"expected 'to' text: {expected_to_text}")
            if actual_to_text == expected_to_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_horizontal_line_below_calenders = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_horizontal_line_below_calenders_by_xpath()).text
            self.logger.info(f"actual horizontal line below calenders: {actual_horizontal_line_below_calenders}")
            expected_horizontal_line_below_calenders = Reporting_read_ini(). \
                get_expected_horizontal_line_below_calenders()
            self.logger.info(f"expected horizontal line below calenders: {expected_horizontal_line_below_calenders}")
            if actual_horizontal_line_below_calenders == expected_horizontal_line_below_calenders:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_243.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_243.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_243_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_243_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_243 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_244 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            start_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_start_date_calender_box_by_xpath())
            if start_date_calender_box.is_displayed():
                self.logger.info("Start date calender box is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if start_date_calender_box.is_enabled():
                self.status.append(False)
            else:
                self.logger.info("start date calender box is disabled by default !!")
                self.status.append(True)
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            if start_date_checkbox.is_displayed():
                self.logger.info("Start date checkbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if start_date_checkbox.is_enabled():
                self.logger.info("Start date checkbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_244.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_244.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_244_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_244_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_244 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_245 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            end_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_end_date_calender_box_by_xpath())
            if end_date_calender_box.is_displayed():
                self.logger.info("End date calender box is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if end_date_calender_box.is_enabled():
                self.status.append(False)
            else:
                self.logger.info("End date calender box is disabled by default !!")
                self.status.append(True)
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            if end_date_checkbox.is_displayed():
                self.logger.info("End date checkbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if end_date_checkbox.is_enabled():
                self.logger.info("End date checkbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_245.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_245.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_245_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_245_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_245 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_246 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            start_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_start_date_calender_box_by_xpath())
            start_calender_disabled_status = start_date_calender_box.get_attribute("disabled")
            if start_date_checkbox.is_selected():
                start_date_checkbox.click()
                if start_calender_disabled_status:
                    self.logger.info("start calender disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"start date disable status: {start_calender_disabled_status}")
                if start_calender_disabled_status:
                    self.logger.info("start calender already disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            start_date_checkbox.click()
            self.logger.info(f"start calender disable status after click: "
                             f"{start_date_calender_box.get_attribute('disabled')}")
            if start_date_calender_box.get_attribute("disabled") is None:
                self.logger.info("start calender enabled !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if start_date_checkbox.is_selected():
                start_date_checkbox.click()
            else:
                pass
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_246.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_246.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_246_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_246_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_246 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_247 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            end_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_end_date_calender_box_by_xpath())
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            end_calender_disabled_status = end_date_calender_box.get_attribute("disabled")
            if end_date_checkbox.is_selected():
                end_date_checkbox.click()
                if end_calender_disabled_status:
                    self.logger.info("End calender disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"End calender disable status: {end_calender_disabled_status}")
                if end_calender_disabled_status:
                    self.logger.info("End calender already disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            end_date_checkbox.click()
            self.logger.info(f"End calender disable status after click: "
                             f"{end_date_calender_box.get_attribute('disabled')}")
            if end_date_calender_box.get_attribute("disabled") is None:
                self.logger.info("End calender enabled !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if end_date_checkbox.is_selected():
                end_date_checkbox.click()
            else:
                pass
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_247.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_247.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_247_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_247_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_247 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_248 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            action = ActionChains(self.d)
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            start_checkbox_hover = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                       get_include_in_search_hover_on_start_checkbox_by_xpath())
            action.move_to_element(start_date_checkbox).perform()
            if start_checkbox_hover.get_attribute("aria-describedby"):
                self.logger.info("'Include In Search' hover is visible for start date checkbox !!")
                self.status.append(True)
            else:
                self.logger.error("'Include In Search' hover is not visible for start date checkbox !!")
                self.status.append(False)
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            end_checkbox_hover = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                     get_include_in_search_hover_on_end_checkbox_by_xpath())
            action.move_to_element(end_date_checkbox).perform()
            if end_checkbox_hover.get_attribute("aria-describedby"):
                self.logger.info("'Include In Search' hover is visible for end date checkbox !!")
                self.status.append(True)
            else:
                self.logger.error("'Include In Search' hover is not visible for end date checkbox !!")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_248.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_248.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_248_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_248_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_248 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_Optional_Filter_text_is_visible_text_beside_Select_group_filter_button_and_that_of_Select_zone_filter_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_249 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            time.sleep(web_driver.one_second)
            actual_optional_filters_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                               get_optional_filters_text_by_xpath()).text
            self.logger.info(f"actual optional filter text: {actual_optional_filters_text}")
            expected_optional_filters_text = Reporting_read_ini().get_expected_optional_filters_text()
            self.logger.info(f"expected optional filter text: {expected_optional_filters_text}")
            if actual_optional_filters_text in expected_optional_filters_text:
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            actual_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                              get_text_beside_select_group_filter_button_by_xpath()).text
            self.logger.info(f"actual text beside group filter button: {actual_text}")
            expected_text = Reporting_read_ini().get_expected_text_beside_select_group_filter_button()
            self.logger.info(f"expected text: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_beside_zone_filter_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_text_beside_select_zone_filter_button_by_xpath()).text
            self.logger.info(f"actual text beside zone filter button: {actual_text_beside_zone_filter_button}")
            expected_text_beside_zone_filter_btn = Reporting_read_ini().\
                get_expected_text_beside_select_zone_filter_button()
            self.logger.info(f"expected text: {expected_text_beside_zone_filter_btn}")
            if actual_text_beside_zone_filter_button == expected_text_beside_zone_filter_btn:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_249.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_249.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_249_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_249_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_249 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_Select_group_filter_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_250 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            time.sleep(web_driver.one_second)
            select_group_filter_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                             get_select_group_filter_button_by_xpath())
            if select_group_filter_button.is_displayed():
                self.logger.info("Select group filter button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if select_group_filter_button.is_enabled():
                self.logger.info("Select group filter button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                              get_select_group_filter_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on Select group filter button: {actual_text}")
            expected_text = Reporting_read_ini().get_expected_text_on_select_group_filter_button()
            self.logger.info(f"expected text on Select group filter button: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            group_icon_on_select_grp_btn = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                               get_group_icon_on_select_group_filter_button_by_xpath())
            if group_icon_on_select_grp_btn.is_displayed():
                self.logger.info("group icon on Select group filter button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_250.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_250.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_250_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_250_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_250 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_Select_zone_filter_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_251 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            time.sleep(web_driver.one_second)
            select_zone_filter_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                            get_select_zone_filter_button_by_xpath())
            if select_zone_filter_button.is_displayed():
                self.logger.info("Select zone filter button is visible !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            if select_zone_filter_button.is_enabled():
                self.logger.info("Select zone filter button is clickable !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_select_zone_button = self.d.find_element(
                By.XPATH, Reporting_read_ini().get_select_zone_filter_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on 'Select zone filter' button: {actual_text_on_select_zone_button}")
            expected_text_on_select_zone_button = Reporting_read_ini().get_expected_text_on_select_zone_filter_button()
            self.logger.info(f"expected text on 'Select zone filter' button: {expected_text_on_select_zone_button}")
            if actual_text_on_select_zone_button == expected_text_on_select_zone_button:
                self.logger.info(" text on select zone button is visible !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_dot_circle_icon_for_zone_by_xpath()). \
                    is_displayed():
                self.logger.info(" dot circle zone icon on button is visible !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            time.sleep(web_driver.one_second)
            
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_251.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_251.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_251_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_251_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_251 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_Generate_Report_button_is_visible_and_clickable_text_and_chart_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_252 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            generate_report_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                         get_generate_report_button_by_xpath())
            if generate_report_button.is_displayed():
                self.logger.info("Generate report button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if generate_report_button.is_enabled():
                self.logger.info("Generate report button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_chart_icon_on_generate_report_button_by_xpath()).\
                    is_displayed():
                self.logger.info("chart icon on Generate report button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_generate_report_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on Generate report button: {actual_text_on_generate_report_button}")
            expected_text_on_generate_report_button = Reporting_read_ini().get_expected_generate_report_text_on_button()
            self.logger.info(f"expected text on Generate report button: {expected_text_on_generate_report_button}")
            if actual_text_on_generate_report_button == expected_text_on_generate_report_button:
                self.status.append(True)
            else:
                self.status.append(False)
            chart_icon_on_generate_report_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_chart_icon_on_generate_report_button_by_xpath())
            if chart_icon_on_generate_report_button.is_displayed():
                self.logger.info("Chart icon on Generate report button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_252.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_252.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_252_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_252_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_252 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_in_Select_group_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_253 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_horizontal_line_below_reporting_panel_heading = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_horizontal_line_below_reporting_panel_heading_for_group_by_xpath()).text
            self.logger.info(f"actual horizontal line below  heading: "
                             f"{actual_horizontal_line_below_reporting_panel_heading}")
            expected_horizontal_line_below_reporting_panel_heading = Reporting_read_ini(). \
                get_expected_horizontal_line_below_reporting_panel_heading_for_group()
            self.logger.info(f"expected horizontal line below  heading: "
                             f"{expected_horizontal_line_below_reporting_panel_heading}")
            if actual_horizontal_line_below_reporting_panel_heading == \
                    expected_horizontal_line_below_reporting_panel_heading:
                self.logger.info("Horizontal line below panel heading is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_253.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_253.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_253_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_253_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_253 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_filter_group_list_below_textbox_is_visible_and_clickable_label_on_textbox_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_254 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            filter_group_list_textbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                            get_filter_group_list_textbox_by_xpath())
            if filter_group_list_textbox.is_displayed():
                self.logger.info("'filter group list below..' textbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if filter_group_list_textbox.is_enabled():
                self.logger.info("'filter group list below..' textbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            filter_group_list_textbox.click()
            actual_label_on_textbox = filter_group_list_textbox.get_attribute('placeholder')
            self.logger.info(f"actual label on textbox: {actual_label_on_textbox}")
            expected_label = Reporting_read_ini().get_expected_label_on_filter_group_list_below_textbox()
            self.logger.info(f"expected label on textbox: {expected_label}")
            if actual_label_on_textbox == expected_label:
                self.logger.info("label is visible on textbox..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_254.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_254.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_254_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_254_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_254 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_group_list_below_filter_group_list_textbox_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_255 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                    get_group_items_list_below_filter_group_list_textbox())
            self.logger.info(f"Group items below 'filter group list' textbox: {len(group_items_list)}")
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH,
                                Reporting_read_ini().get_enrollment_groups_module_on_dashboard_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_group_list_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                           get_group_item_list_from_enrollment_group_panel_by_xpath())
            time.sleep(web_driver.one_second)
            self.logger.info(f"Actual group items from 'Enrollment Groups': {len(actual_group_list_items)}")
            if len(group_items_list) == len(actual_group_list_items):

                self.logger.info("Group list items are visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            '''''
            for items in group_items_list:
                if items.is_displayed():
                    self.status.append(True)
                else:
                    self.status.append(False)
                if items.is_enabled():
                    self.status.append(True)
                else:
                    self.status.append(False)
            '''''
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_255.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_255.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_255_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_255_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_255 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_select_all_button_in_group_filter_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_256 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            select_all_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                    get_select_all_button_in_group_filter_by_xpath())
            if select_all_button.is_displayed():
                self.logger.info("Select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if select_all_button.is_enabled():
                self.logger.info("Select all button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_select_all_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_select_all_button_in_group_filter_by_xpath()).text
            self.logger.info(f"actual text on select all button in group filter: {actual_text_on_select_all_button}")
            self.logger.info(f"expected text on select all button in group filter: "
                             f"{Reporting_read_ini().get_expected_text_on_select_all_button()}")
            if actual_text_on_select_all_button == Reporting_read_ini().get_expected_text_on_select_all_button():
                self.logger.info("text on Select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_256.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_256.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_256_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_256_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_256 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_selected_group_list_title_and_default_text_below_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_257 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_selected_group_list_title = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual title: {actual_selected_group_list_title}")
            self.logger.info(f"expected title: {Reporting_read_ini().get_expected_selected_group_list_title()}")
            if actual_selected_group_list_title == Reporting_read_ini().get_expected_selected_group_list_title():
                self.logger.info("'Selected group list' title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_first_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_first_default_te_below_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual first horizontal line: {actual_first_horizontal_line}")
            expected_first_horizontal_line = \
                Reporting_read_ini().get_expected_first_default_text_line_below_selected_group_list_title()
            self.logger.info(f"expected first horizontal line: {expected_first_horizontal_line}")
            if actual_first_horizontal_line == expected_first_horizontal_line:
                self.logger.info("First default text line below selected group list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_second_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_second_default_text_below_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual second default text line below 'Selected group list' title: "
                             f"{actual_second_horizontal_line}")
            expected_second_horizontal_line = \
                Reporting_read_ini().get_expected_second_default_text_line_below_selected_group_list_title()
            self.logger.info(f"expected second horizontal line: {expected_second_horizontal_line}")
            if actual_second_horizontal_line == expected_second_horizontal_line:
                self.logger.info("Second default text line below selected group list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_257.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_257.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_257_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_257_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_257 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_close_group_menu_button_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_258 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            close_group_menu_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_close_group_menu_button_by_xpath())
            if close_group_menu_button.is_displayed():
                self.logger.info("'Close group menu' button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if close_group_menu_button.is_enabled():
                self.logger.info("'Close group menu' button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_close_group_menu_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_text_on_close_group_menu_button_by_xpath()).text
            self.logger.info(f"actual text on close menu btn: {actual_text_on_close_group_menu_button}")
            expected_text_on_close_group_button = Reporting_read_ini().get_expected_text_on_close_group_menu_button()
            self.logger.info(f"expected text on close menu btn: {expected_text_on_close_group_button}")
            if actual_text_on_close_group_menu_button == expected_text_on_close_group_button:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_258.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_258.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_258_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_258_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_258 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_click_on_select_all_button_and_verify_all_selected_groups_are_visible_in_selected_group_list(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_259 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_items_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_group_items_list_below_filter_group_list_textbox())
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)
            selected_group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_selected_group_list_items_by_xpath())
            if len(selected_group_list) == len(group_items_list):
                self.logger.info("All selected groups are visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_259.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_259.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_259_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_259_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_259 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_click_on_select_all_button_in_group_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_260 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            clear_all_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_clear_all_button_on_selected_group_by_xpath())
            if clear_all_button.is_displayed():
                self.logger.info("'Clear all' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if clear_all_button.is_enabled():
                self.logger.info("'Clear all' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_clear_all_button_on_selected_group_by_xpath()).text
            self.logger.info(f"actual text on 'Clear all' button: {actual_text_on_button}")
            self.logger.info(f"expected text on 'Clear all' button: "
                             f"{Reporting_read_ini().get_expected_clear_all_text()}")
            if actual_text_on_button == Reporting_read_ini().get_expected_clear_all_text():
                self.logger.info("text on 'Clear all' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_260.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_260.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_260_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_260_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_260 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_click_on_select_all_button_and_verify_save_group_selection_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_261 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            save_group_selection_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                              get_save_group_selection_button_by_xpath())
            if save_group_selection_button.is_displayed():
                self.logger.info("'Save group selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if save_group_selection_button.is_enabled():
                self.logger.info("'Save group selection' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH,
                                   Reporting_read_ini().get_group_icon_on_save_group_selection_button_by_xpath()).\
                    is_displayed():
                self.logger.info("group icon on 'Save group selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_save_group_selection_text_by_xpath()).text
            self.logger.info(f"actual text on 'Save group selection' button: {actual_text_on_button}")
            expected_text = Reporting_read_ini().get_expected_text_on_save_group_selection_button()
            self.logger.info(f"expected text on button: {expected_text}")
            if actual_text_on_button == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_261.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_261.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_261_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_261_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_261 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_select_one_group_from_group_list_and_verify_selected_group_is_visible_in_selected_group_list_verify_save_group_selection_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_262 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_group_items_list_below_filter_group_list_textbox())
            first_group_name = group_list[0].text
            group_list[0].click()
            self.logger.info("Selected first group from groups list...")
            time.sleep(web_driver.one_second)
            selected_group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_selected_group_list_items_by_xpath())
            if first_group_name == selected_group_list[0].text:
                self.logger.info("Selected group is visible in Selected group list...")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH,
                                   Reporting_read_ini().get_save_group_selection_button_by_xpath()).is_displayed():
                self.logger.info("'Save group selection' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error("screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_262.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_262.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_262_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_262_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_262 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_click_on_save_group_selection_button_with_at_least_one_group_selected_and_verify_View_and_edit_groups_button_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_263 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            group_list[0].click()
            self.logger.info("Selected first group from group list...")
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save group selection' button...")
            time.sleep(web_driver.one_second)

            view_edit_groups_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_view_and_edit_groups_button_by_xpath())
            if view_edit_groups_button.is_displayed():
                self.logger.info("'View & edit GROUPS' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if view_edit_groups_button.is_enabled():
                self.logger.info("'View & edit GROUPS' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_263.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_263.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_263_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_263_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_263 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_text_and_numeric_value_of_number_of_selected_groups_on_view_and_edit_groups_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_264 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            group_list[0].click()
            self.logger.info("Selected first group from group list...")
            group_list[1].click()
            self.logger.info("Selected second group from group list...")
            time.sleep(web_driver.one_second)
            selected_groups = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_selected_group_list_items_by_xpath())
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save group selection' button...")
            time.sleep(web_driver.one_second)
            actual_text_on_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_view_and_edit_groups_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on button: {actual_text_on_button}")
            expected_numeric_value_of_group_selected = f"{len(selected_groups)}" + " " + "selected"

            if Reporting_read_ini().get_expected_text_on_view_and_edit_groups_button() in actual_text_on_button:
                self.logger.info("'View & edit GROUPS' text is visible on button...")
                self.status.append(True)
            else:
                self.status.append(False)
            if expected_numeric_value_of_group_selected in actual_text_on_button:
                self.logger.info(f"numeric value of expected selected groups: "
                                 f"{expected_numeric_value_of_group_selected}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_264.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_264.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_264_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_264_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_264 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_in_select_zone_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_265 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_horizontal_line_below_reporting_panel_heading = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_horizontal_line_below_reporting_panel_heading_by_xpath()).text
            self.logger.info(f"actual horizontal line below reporting panel heading: "
                             f"{actual_horizontal_line_below_reporting_panel_heading}")
            expected_horizontal_line_below_reporting_panel_heading = Reporting_read_ini(). \
                get_expected_horizontal_line_below_reporting_panel_heading()
            self.logger.info(f"expected horizontal line below reporting panel heading: "
                             f"{expected_horizontal_line_below_reporting_panel_heading}")
            if actual_horizontal_line_below_reporting_panel_heading == \
                    expected_horizontal_line_below_reporting_panel_heading:
                self.logger.info("'Select zone(s) to narrow report results' is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_265.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_265.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_265_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_265_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_265 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_search_zones_textbox_is_visible_and_clickable_label_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_266 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            search_zone_textbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_search_zone_textbox_by_xpath())
            if search_zone_textbox.is_displayed():
                self.logger.info("Select zone textbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if search_zone_textbox.is_enabled():
                self.logger.info("Select zone textbox is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            search_zone_textbox.click()
            time.sleep(web_driver.one_second)
            actual_label_on_search_zone_textbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                      get_search_zone_textbox_by_xpath()). \
                get_attribute("placeholder")
            self.logger.info(f"actual label on search zone textbox: {actual_label_on_search_zone_textbox}")
            expected_label_on_search_zone_textbox = Reporting_read_ini().get_expected_label_on_search_zone_textbox()
            self.logger.info(f"expected label on search zone textbox: {expected_label_on_search_zone_textbox}")
            if actual_label_on_search_zone_textbox == expected_label_on_search_zone_textbox:
                self.logger.info("'Search zone...' label on textbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_266.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_266.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_266_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_266_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_266 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_zone_list_below_search_zones_textbox_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_267 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            self.logger.info(f"Zone items below 'Search zone' textbox: {len(zone_items_list)}")
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_zone_module_on_dashboard_by_xpath()).click()
            time.sleep(web_driver.one_second)

            actual_zone_item_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                         get_zone_item_list_from_zone_panel_by_xpath())
            self.logger.info(f"Actual zones list from 'Zones' module: {len(actual_zone_item_list)}")
            time.sleep(web_driver.one_second)
            if len(zone_items_list) == len(actual_zone_item_list):
                self.logger.info("Zones list items list is visible....")
                self.status.append(True)
            else:
                self.status.append(False)

            for items in zone_items_list:
                if items.is_displayed():
                    self.status.append(True)
                else:
                    self.status.append(False)
                if items.is_enabled():
                    self.status.append(True)
                else:
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_267.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_267.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_267_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_267_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_267 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_select_all_button_in_zone_filter_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_268 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()). \
                    is_displayed():
                self.logger.info("Select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()). \
                    is_enabled():
                self.logger.info("Select all button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_select_all_button_in_zone_filter = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()).text
            self.logger.info(f"actual text on btn: {actual_text_on_select_all_button_in_zone_filter}")
            self.logger.info(f"expected text on btn: {Reporting_read_ini().get_expected_text_on_select_all_button()}")
            if actual_text_on_select_all_button_in_zone_filter == \
                    Reporting_read_ini().get_expected_text_on_select_all_button():
                self.logger.info("text on select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_268.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_268.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_268_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_268_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_268 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_selected_zone_list_title_and_default_text_below_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_269 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_selected_zone_list_title = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                  get_selected_zone_list_title_by_xpath()).text
            self.logger.info(f"actual title text: {actual_selected_zone_list_title}")
            expected_selected_zone_list_title = Reporting_read_ini().get_expected_selected_zone_list_title()
            self.logger.info(f"expected title text: {expected_selected_zone_list_title}")
            if actual_selected_zone_list_title == expected_selected_zone_list_title:
                self.logger.info("'Selected zone list' title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_first_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_first_default_text_line_below_selected_zone_list_title_by_xpath()).text
            self.logger.info(f"actual first default line below title: {actual_first_horizontal_line}")
            expected_first_horizontal_line = Reporting_read_ini(). \
                get_expected_first_default_text_line_below_selected_zone_list_title()
            self.logger.info(f"expected first default line below title: {expected_first_horizontal_line}")
            if actual_first_horizontal_line == expected_first_horizontal_line:
                self.logger.info("first default text line below selected zone list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_second_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_second_default_text_line_below_selected_zone_list_title_by_xpath()).text
            self.logger.info(f"actual second default line below title: {actual_second_horizontal_line}")
            expected_second_horizontal_line = Reporting_read_ini(). \
                get_expected_second_default_text_line_below_selected_zone_list_title()
            self.logger.info(f"expected second default line below title: {expected_second_horizontal_line}")
            if actual_second_horizontal_line == expected_second_horizontal_line:
                self.logger.info("second default text line below selected zone list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_269.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_269.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_269_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_269_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_269 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_close_zone_menu_button_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_270 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            close_zone_menu_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                         get_close_zone_menu_button_by_xpath())
            if close_zone_menu_button.is_displayed():
                self.logger.info("'Close zone menu' button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if close_zone_menu_button.is_enabled():
                self.logger.info("'Close zone menu' button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_close_zone_menu_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_text_on_close_zone_menu_button_by_xpath()).text
            self.logger.info(f"actual text on btn: {actual_text_on_close_zone_menu_button}")
            expected_text_on_close_zone_menu_button = Reporting_read_ini().get_expected_text_on_close_zone_menu_button()
            self.logger.info(f"expected text on btn: {expected_text_on_close_zone_menu_button}")
            if actual_text_on_close_zone_menu_button == expected_text_on_close_zone_menu_button:
                self.logger.info("text on 'Close zone menu' is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_270.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_270.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_270_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_270_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_270 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_click_on_select_all_button_and_verify_all_selected_zones_are_visible_in_selected_zone_list(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_271 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                             get_zone_items_list_below_search_zone_textbox_by_xpath())
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)
            selected_zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                      get_selected_zone_list_items_by_xpath())

            if len(selected_zone_list) == len(zone_list):
                self.logger.info("All selected zones are visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_271.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_271.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_271_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_271_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_271 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_click_on_select_all_button_in_zone_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_272 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            clear_all_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_clear_all_button_on_selected_zone_by_xpath())
            if clear_all_button.is_displayed():
                self.logger.info("'Clear all' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if clear_all_button.is_enabled():
                self.logger.info("'Clear all' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_clear_all_button_on_selected_zone_by_xpath()).text
            self.logger.info(f"actual text on 'Clear all' button: {actual_text_on_button}")
            self.logger.info(f"expected text on 'Clear all' button: "
                             f"{Reporting_read_ini().get_expected_clear_all_text()}")
            if actual_text_on_button == Reporting_read_ini().get_expected_clear_all_text():
                self.logger.info("text on 'Clear all' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_272.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_272.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_272_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_272_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_272 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_click_on_select_all_button_and_verify_save_zone_selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_273 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            save_zone_selection_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                             get_save_zone_selection_button_by_xpath())
            if save_zone_selection_button.is_displayed():
                self.logger.info("'Save zone selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if save_zone_selection_button.is_enabled():
                self.logger.info("'Save zone selection' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_dot_circle_icon_on_save_zone_selection_button()).\
                    is_displayed():
                self.logger.info("dot circle icon on 'Save group selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_save_zone_selection_text_by_xpath()).text
            self.logger.info(f"actual text on 'Save zone selection' button: {actual_text_on_button}")
            self.logger.info(f"expected text on button: {Reporting_read_ini().get_expected_save_zone_selection_text()}")
            if actual_text_on_button == Reporting_read_ini().get_expected_save_zone_selection_text():
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_273.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_273.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_273_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_273_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_273 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_select_one_zone_from_zone_list_and_verify_selected_zone_is_visible_in_selected_zone_list_verify_save_zone_selection_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_274 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            actual_first_zone = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                     get_first_zone_in_search_zone_list_by_xpath())
            first_zone_name = actual_first_zone[0].text
            zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                             get_zone_items_list_below_search_zone_textbox_by_xpath())
            zone_list[0].click()
            self.logger.info("Selected first zone from zones list...")
            time.sleep(web_driver.one_second)

            first_name_from_selected_zone_list = \
                self.d.find_element(By.XPATH,
                                    Reporting_read_ini().get_first_zone_name_in_selected_zone_list_by_xpath()).text
            if first_zone_name == first_name_from_selected_zone_list:
                self.logger.info("Selected zone is visible in Selected zones list...")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()). \
                    is_displayed():
                self.logger.info("'Save zone selection' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_274.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_274.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_274_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_274_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_274 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_click_on_save_zone_selection_button_with_at_least_one_zone_selected_and_verify_View_and_edit_zones_button_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_275 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                             get_zone_items_list_below_search_zone_textbox_by_xpath())
            zone_list[0].click()
            self.logger.info("Selected first zone from zones list...")
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button...")
            time.sleep(web_driver.one_second)

            view_edit_zones_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                         get_view_and_edit_zones_button_by_xpath())
            if view_edit_zones_button.is_displayed():
                self.logger.info("'View & edit ZONES' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if view_edit_zones_button.is_enabled():
                self.logger.info("'View & edit ZONES' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_275.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_275.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_275_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_275_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_275 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_day_verify_text_and_numeric_value_of_number_of_selected_zones_on_view_and_edit_zones_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HD_276 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_day()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                             get_zone_items_list_below_search_zone_textbox_by_xpath())
            zone_list[0].click()
            self.logger.info("Selected first zone from zone list...")
            time.sleep(web_driver.one_second)

            selected_zones = self.d.find_elements(By.XPATH,
                                                  Reporting_read_ini().get_selected_zone_list_items_by_xpath())

            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button...")
            time.sleep(web_driver.one_second)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_view_and_edit_zones_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on button: {actual_text_on_button}")
            expected_numeric_value_of_zone_selected = f"{len(selected_zones)}" + " " + "selected"

            if Reporting_read_ini().get_expected_view_and_edit_zones_text() in actual_text_on_button:
                self.logger.info("'View & edit ZONES' text is visible on button...")
                self.status.append(True)
            else:
                self.status.append(False)
            if expected_numeric_value_of_zone_selected in actual_text_on_button:
                self.logger.info(f"numeric value of expected selected zones: "
                                 f"{expected_numeric_value_of_zone_selected}")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_276.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_276.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_276_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_276_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_276 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def select_number_of_events_by_day_of_week(self):
        try:
            time.sleep(web_driver.one_second)
            field1 = Select(web_driver.explicit_wait(self, 10, "XPATH",Reporting_read_ini().get_report_field1_dropdown_by_xpath(), self.d))
            time.sleep(web_driver.one_second)
            field1.select_by_visible_text('number of probable match events')
            field2 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_report_field2_dropdown_for_events_by_xpath()))
            time.sleep(web_driver.one_second)
            field2.select_by_visible_text('day of week')
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def For_number_of_events_by_day_of_week_verify_number_of_events_from_report_field1_and_day_of_week_from_report_field2_texts_are_visible_on_dropdown(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_277 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            time.sleep(web_driver.one_second)
            field1.select_by_visible_text('number of probable match events')

            value1 = self.d.find_element(By.XPATH,
                                         Reporting_read_ini().get_report_field1_dropdown_by_xpath()).get_attribute(
                'value')
            self.logger.info(f"Value1: {value1}")
            if "number of events" in value1:
                self.logger.info("Selected 'number of events' from report field1 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            field2 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_report_field2_dropdown_for_events_by_xpath()))
            field2.select_by_visible_text('day of week')

            value2 = self.d.find_element(By.XPATH, Reporting_read_ini().
                                         get_report_field2_dropdown_for_events_by_xpath()).get_attribute(
                'value')
            self.logger.info(f"Value2: {value2}")
            if Reporting_read_ini().get_expected_second_text_from_field2() in value2:
                self.logger.info("Selected 'day of week' from report field2 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_277.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_277.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_277_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_277_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_277 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_boxes_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_278 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            actual_date_and_time_range_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                  get_date_and_time_range_text_by_xpath()).text
            self.logger.info(f"actual date & time range text: {actual_date_and_time_range_text}")
            expected_date_range_text = Reporting_read_ini().get_expected_date_and_time_range_text()
            self.logger.info(f"expected date & time range text: {expected_date_range_text}")
            if actual_date_and_time_range_text == expected_date_range_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_to_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_to_text_by_xpath()).text
            self.logger.info(f"actual 'to' text: {actual_to_text}")
            expected_to_text = Reporting_read_ini().get_expected_to_text()
            self.logger.info(f"expected 'to' text: {expected_to_text}")
            if actual_to_text == expected_to_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_horizontal_line_below_calenders = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_horizontal_line_below_calenders_by_xpath()).text
            self.logger.info(f"actual horizontal line below calenders: {actual_horizontal_line_below_calenders}")
            expected_horizontal_line_below_calenders = Reporting_read_ini(). \
                get_expected_horizontal_line_below_calenders()
            self.logger.info(f"expected horizontal line below calenders: {expected_horizontal_line_below_calenders}")
            if actual_horizontal_line_below_calenders == expected_horizontal_line_below_calenders:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_278.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_278.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_278_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_278_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_278 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_279 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            start_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_start_date_calender_box_by_xpath())
            if start_date_calender_box.is_displayed():
                self.logger.info("Start date calender box is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if start_date_calender_box.is_enabled():
                self.status.append(False)
            else:
                self.logger.info("start date calender box is disabled by default !!")
                self.status.append(True)
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            if start_date_checkbox.is_displayed():
                self.logger.info("Start date checkbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if start_date_checkbox.is_enabled():
                self.logger.info("Start date checkbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_279.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_279.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_279_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_279_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_279 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_280 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            end_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_end_date_calender_box_by_xpath())
            if end_date_calender_box.is_displayed():
                self.logger.info("End date calender box is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if end_date_calender_box.is_enabled():
                self.status.append(False)
            else:
                self.logger.info("End date calender box is disabled by default !!")
                self.status.append(True)
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            if end_date_checkbox.is_displayed():
                self.logger.info("End date checkbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if end_date_checkbox.is_enabled():
                self.logger.info("End date checkbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_280.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_280.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_280_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_280_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_280 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_281 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            start_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_start_date_calender_box_by_xpath())
            start_calender_disabled_status = start_date_calender_box.get_attribute("disabled")
            if start_date_checkbox.is_selected():
                start_date_checkbox.click()
                if start_calender_disabled_status:
                    self.logger.info("start calender disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"start date disable status: {start_calender_disabled_status}")
                if start_calender_disabled_status:
                    self.logger.info("start calender already disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            start_date_checkbox.click()
            self.logger.info(f"start calender disable status after click: "
                             f"{start_date_calender_box.get_attribute('disabled')}")
            if start_date_calender_box.get_attribute("disabled") is None:
                self.logger.info("start calender enabled !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if start_date_checkbox.is_selected():
                start_date_checkbox.click()
            else:
                pass
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_281.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_281.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_281_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_281_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_281 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_282 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            end_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_end_date_calender_box_by_xpath())
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            end_calender_disabled_status = end_date_calender_box.get_attribute("disabled")
            if end_date_checkbox.is_selected():
                end_date_checkbox.click()
                if end_calender_disabled_status:
                    self.logger.info("End calender disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"End calender disable status: {end_calender_disabled_status}")
                if end_calender_disabled_status:
                    self.logger.info("End calender already disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            end_date_checkbox.click()
            self.logger.info(f"End calender disable status after click: "
                             f"{end_date_calender_box.get_attribute('disabled')}")
            if end_date_calender_box.get_attribute("disabled") is None:
                self.logger.info("End calender enabled !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if end_date_checkbox.is_selected():
                end_date_checkbox.click()
            else:
                pass
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_282.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_282.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_282_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_282_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_282 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_283 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            action = ActionChains(self.d)
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            start_checkbox_hover = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                       get_include_in_search_hover_on_start_checkbox_by_xpath())
            action.move_to_element(start_date_checkbox).perform()
            if start_checkbox_hover.get_attribute("aria-describedby"):
                self.logger.info("'Include In Search' hover is visible for start date checkbox !!")
                self.status.append(True)
            else:
                self.logger.error("'Include In Search' hover is not visible for start date checkbox !!")
                self.status.append(False)
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            end_checkbox_hover = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                     get_include_in_search_hover_on_end_checkbox_by_xpath())
            action.move_to_element(end_date_checkbox).perform()
            if end_checkbox_hover.get_attribute("aria-describedby"):
                self.logger.info("'Include In Search' hover is visible for end date checkbox !!")
                self.status.append(True)
            else:
                self.logger.error("'Include In Search' hover is not visible for end date checkbox !!")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_283.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_283.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_283_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_283_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_283 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_Optional_Filter_text_is_visible_text_beside_Select_group_filter_button_and_that_of_Select_zone_filter_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_284 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            time.sleep(web_driver.one_second)
            actual_optional_filters_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                               get_optional_filters_text_by_xpath()).text
            self.logger.info(f"actual optional filter text: {actual_optional_filters_text}")
            expected_optional_filters_text = Reporting_read_ini().get_expected_optional_filters_text()
            self.logger.info(f"expected optional filter text: {expected_optional_filters_text}")
            if actual_optional_filters_text in expected_optional_filters_text:
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            actual_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                              get_text_beside_select_group_filter_button_by_xpath()).text
            self.logger.info(f"actual text beside group filter button: {actual_text}")
            expected_text = Reporting_read_ini().get_expected_text_beside_select_group_filter_button()
            self.logger.info(f"expected text: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_beside_zone_filter_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_text_beside_select_zone_filter_button_by_xpath()).text
            self.logger.info(f"actual text beside zone filter button: {actual_text_beside_zone_filter_button}")
            expected_text_beside_zone_filter_btn = Reporting_read_ini().\
                get_expected_text_beside_select_zone_filter_button()
            self.logger.info(f"expected text: {expected_text_beside_zone_filter_btn}")
            if actual_text_beside_zone_filter_button == expected_text_beside_zone_filter_btn:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_284.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_284.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_284_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_284_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_284 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_Select_group_filter_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_285 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            time.sleep(web_driver.one_second)
            select_group_filter_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                             get_select_group_filter_button_by_xpath())
            if select_group_filter_button.is_displayed():
                self.logger.info("Select group filter button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if select_group_filter_button.is_enabled():
                self.logger.info("Select group filter button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                              get_select_group_filter_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on Select group filter button: {actual_text}")
            expected_text = Reporting_read_ini().get_expected_text_on_select_group_filter_button()
            self.logger.info(f"expected text on Select group filter button: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            group_icon_on_select_grp_btn = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                               get_group_icon_on_select_group_filter_button_by_xpath())
            if group_icon_on_select_grp_btn.is_displayed():
                self.logger.info("group icon on Select group filter button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_285.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_285.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_285_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_285_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_285 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_Select_zone_filter_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_286 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            time.sleep(web_driver.one_second)
            select_zone_filter_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                            get_select_zone_filter_button_by_xpath())
            if select_zone_filter_button.is_displayed():
                self.logger.info("Select zone filter button is visible !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            if select_zone_filter_button.is_enabled():
                self.logger.info("Select zone filter button is clickable !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_select_zone_button = self.d.find_element(
                By.XPATH, Reporting_read_ini().get_select_zone_filter_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on 'Select zone filter' button: {actual_text_on_select_zone_button}")
            expected_text_on_select_zone_button = Reporting_read_ini().get_expected_text_on_select_zone_filter_button()
            self.logger.info(f"expected text on 'Select zone filter' button: {expected_text_on_select_zone_button}")
            if actual_text_on_select_zone_button == expected_text_on_select_zone_button:
                self.logger.info(" text on select zone button is visible !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_dot_circle_icon_for_zone_by_xpath()). \
                    is_displayed():
                self.logger.info(" dot circle zone icon on button is visible !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            time.sleep(web_driver.one_second)
            
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_286.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_286.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_286_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_286_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_286 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_Generate_Report_button_is_visible_and_clickable_text_and_chart_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_287 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            time.sleep(web_driver.two_second)
            generate_report_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                         get_generate_report_button_by_xpath())
            if generate_report_button.is_displayed():
                self.logger.info("Generate report button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if generate_report_button.is_enabled():
                self.logger.info("Generate report button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_chart_icon_on_generate_report_button_by_xpath()).\
                    is_displayed():
                self.logger.info("chart icon on Generate report button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_generate_report_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on Generate report button: {actual_text_on_generate_report_button}")
            expected_text_on_generate_report_button = Reporting_read_ini().get_expected_generate_report_text_on_button()
            self.logger.info(f"expected text on Generate report button: {expected_text_on_generate_report_button}")
            if actual_text_on_generate_report_button == expected_text_on_generate_report_button:
                self.status.append(True)
            else:
                self.status.append(False)
            chart_icon_on_generate_report_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_chart_icon_on_generate_report_button_by_xpath())
            if chart_icon_on_generate_report_button.is_displayed():
                self.logger.info("Chart icon on Generate report button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_287.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_287.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_287_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_287_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_287 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_in_Select_group_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_288 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_horizontal_line_below_reporting_panel_heading = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_horizontal_line_below_reporting_panel_heading_for_group_by_xpath()).text
            self.logger.info(f"actual horizontal line below  heading: "
                             f"{actual_horizontal_line_below_reporting_panel_heading}")
            expected_horizontal_line_below_reporting_panel_heading = Reporting_read_ini(). \
                get_expected_horizontal_line_below_reporting_panel_heading_for_group()
            self.logger.info(f"expected horizontal line below  heading: "
                             f"{expected_horizontal_line_below_reporting_panel_heading}")
            if actual_horizontal_line_below_reporting_panel_heading == \
                    expected_horizontal_line_below_reporting_panel_heading:
                self.logger.info("Horizontal line below panel heading is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_288.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_288.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_288_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_288_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_288 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_filter_group_list_below_textbox_is_visible_and_clickable_label_on_textbox_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_289 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            time.sleep(web_driver.three_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.three_second)
            filter_group_list_textbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                            get_filter_group_list_textbox_by_xpath())
            if filter_group_list_textbox.is_displayed():
                self.logger.info("'filter group list below..' textbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if filter_group_list_textbox.is_enabled():
                self.logger.info("'filter group list below..' textbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            filter_group_list_textbox.click()
            actual_label_on_textbox = filter_group_list_textbox.get_attribute('placeholder')
            self.logger.info(f"actual label on textbox: {actual_label_on_textbox}")
            expected_label = Reporting_read_ini().get_expected_label_on_filter_group_list_below_textbox()
            self.logger.info(f"expected label on textbox: {expected_label}")
            if actual_label_on_textbox == expected_label:
                self.logger.info("label is visible on textbox..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_289.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_289.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_289_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_289_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_289 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_group_list_below_filter_group_list_textbox_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_290 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                    get_group_items_list_below_filter_group_list_textbox())
            self.logger.info(f"Group items below 'filter group list' textbox: {len(group_items_list)}")
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH,
                                Reporting_read_ini().get_enrollment_groups_module_on_dashboard_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_group_list_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                           get_group_item_list_from_enrollment_group_panel_by_xpath())
            time.sleep(web_driver.one_second)
            self.logger.info(f"Actual group items from 'Enrollment Groups': {len(actual_group_list_items)}")
            if len(group_items_list) == len(actual_group_list_items):

                self.logger.info("Group list items are visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            '''''
            for items in group_items_list:
                if items.is_displayed():
                    self.status.append(True)
                else:
                    self.status.append(False)
                if items.is_enabled():
                    self.status.append(True)
                else:
                    self.status.append(False)
            '''''
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_290.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_290.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_290_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_290_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_290 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_select_all_button_in_group_filter_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_291 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            select_all_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                    get_select_all_button_in_group_filter_by_xpath())
            if select_all_button.is_displayed():
                self.logger.info("Select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if select_all_button.is_enabled():
                self.logger.info("Select all button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_select_all_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_select_all_button_in_group_filter_by_xpath()).text
            self.logger.info(f"actual text on select all button in group filter: {actual_text_on_select_all_button}")
            self.logger.info(f"expected text on select all button in group filter: "
                             f"{Reporting_read_ini().get_expected_text_on_select_all_button()}")
            if actual_text_on_select_all_button == Reporting_read_ini().get_expected_text_on_select_all_button():
                self.logger.info("text on Select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_291.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_291.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_291_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_291_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_291 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_selected_group_list_title_and_default_text_below_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_292 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_selected_group_list_title = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual title: {actual_selected_group_list_title}")
            self.logger.info(f"expected title: {Reporting_read_ini().get_expected_selected_group_list_title()}")
            if actual_selected_group_list_title == Reporting_read_ini().get_expected_selected_group_list_title():
                self.logger.info("'Selected group list' title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_first_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_first_default_te_below_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual first horizontal line: {actual_first_horizontal_line}")
            expected_first_horizontal_line = \
                Reporting_read_ini().get_expected_first_default_text_line_below_selected_group_list_title()
            self.logger.info(f"expected first horizontal line: {expected_first_horizontal_line}")
            if actual_first_horizontal_line == expected_first_horizontal_line:
                self.logger.info("First default text line below selected group list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_second_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_second_default_text_below_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual second default text line below 'Selected group list' title: "
                             f"{actual_second_horizontal_line}")
            expected_second_horizontal_line = \
                Reporting_read_ini().get_expected_second_default_text_line_below_selected_group_list_title()
            self.logger.info(f"expected second horizontal line: {expected_second_horizontal_line}")
            if actual_second_horizontal_line == expected_second_horizontal_line:
                self.logger.info("Second default text line below selected group list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_292.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_292.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_292_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_292_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_292 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_close_group_menu_button_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_293 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            close_group_menu_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_close_group_menu_button_by_xpath())
            if close_group_menu_button.is_displayed():
                self.logger.info("'Close group menu' button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if close_group_menu_button.is_enabled():
                self.logger.info("'Close group menu' button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_close_group_menu_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_text_on_close_group_menu_button_by_xpath()).text
            self.logger.info(f"actual text on close menu btn: {actual_text_on_close_group_menu_button}")
            expected_text_on_close_group_button = Reporting_read_ini().get_expected_text_on_close_group_menu_button()
            self.logger.info(f"expected text on close menu btn: {expected_text_on_close_group_button}")
            if actual_text_on_close_group_menu_button == expected_text_on_close_group_button:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_293.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_293.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_293_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_293_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_293 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_click_on_select_all_button_and_verify_all_selected_groups_are_visible_in_selected_group_list(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_294 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_items_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_group_items_list_below_filter_group_list_textbox())
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)
            selected_group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_selected_group_list_items_by_xpath())
            if len(selected_group_list) == len(group_items_list):
                self.logger.info("All selected groups are visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_294.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_294.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_294_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_294_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_294 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_click_on_select_all_button_in_group_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_295 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            clear_all_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_clear_all_button_on_selected_group_by_xpath())
            if clear_all_button.is_displayed():
                self.logger.info("'Clear all' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if clear_all_button.is_enabled():
                self.logger.info("'Clear all' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_clear_all_button_on_selected_group_by_xpath()).text
            self.logger.info(f"actual text on 'Clear all' button: {actual_text_on_button}")
            self.logger.info(f"expected text on 'Clear all' button: "
                             f"{Reporting_read_ini().get_expected_clear_all_text()}")
            if actual_text_on_button == Reporting_read_ini().get_expected_clear_all_text():
                self.logger.info("text on 'Clear all' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_295.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_295.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_295_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_295_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_295 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_click_on_select_all_button_and_verify_save_group_selection_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_296 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            save_group_selection_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                              get_save_group_selection_button_by_xpath())
            if save_group_selection_button.is_displayed():
                self.logger.info("'Save group selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if save_group_selection_button.is_enabled():
                self.logger.info("'Save group selection' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH,
                                   Reporting_read_ini().get_group_icon_on_save_group_selection_button_by_xpath()).\
                    is_displayed():
                self.logger.info("group icon on 'Save group selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_save_group_selection_text_by_xpath()).text
            self.logger.info(f"actual text on 'Save group selection' button: {actual_text_on_button}")
            expected_text = Reporting_read_ini().get_expected_text_on_save_group_selection_button()
            self.logger.info(f"expected text on button: {expected_text}")
            if actual_text_on_button == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_296.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_296.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_296_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_296_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_296 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_select_one_group_from_group_list_and_verify_selected_group_is_visible_in_selected_group_list_verify_save_group_selection_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_297 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_group_items_list_below_filter_group_list_textbox())
            first_group_name = group_list[0].text
            group_list[0].click()
            self.logger.info("Selected first group from groups list...")
            time.sleep(web_driver.one_second)
            selected_group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_selected_group_list_items_by_xpath())
            if first_group_name == selected_group_list[0].text:
                self.logger.info("Selected group is visible in Selected group list...")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH,
                                   Reporting_read_ini().get_save_group_selection_button_by_xpath()).is_displayed():
                self.logger.info("'Save group selection' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_297.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_297.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_297_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_297_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_297 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_click_on_save_group_selection_button_with_at_least_one_group_selected_and_verify_View_and_edit_groups_button_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_298 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            group_list[0].click()
            self.logger.info("Selected first group from group list...")
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save group selection' button...")
            time.sleep(web_driver.one_second)

            view_edit_groups_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_view_and_edit_groups_button_by_xpath())
            if view_edit_groups_button.is_displayed():
                self.logger.info("'View & edit GROUPS' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if view_edit_groups_button.is_enabled():
                self.logger.info("'View & edit GROUPS' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_298.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_298.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_298_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_298_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_298 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_text_and_numeric_value_of_number_of_selected_groups_on_view_and_edit_groups_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_299 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            group_list[0].click()
            self.logger.info("Selected first group from group list...")
            group_list[1].click()
            self.logger.info("Selected second group from group list...")
            time.sleep(web_driver.one_second)
            selected_groups = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_selected_group_list_items_by_xpath())
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save group selection' button...")
            time.sleep(web_driver.one_second)
            actual_text_on_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_view_and_edit_groups_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on button: {actual_text_on_button}")
            expected_numeric_value_of_group_selected = f"{len(selected_groups)}" + " " + "selected"

            if Reporting_read_ini().get_expected_text_on_view_and_edit_groups_button() in actual_text_on_button:
                self.logger.info("'View & edit GROUPS' text is visible on button...")
                self.status.append(True)
            else:
                self.status.append(False)
            if expected_numeric_value_of_group_selected in actual_text_on_button:
                self.logger.info(f"numeric value of expected selected groups: "
                                 f"{expected_numeric_value_of_group_selected}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_299.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_299.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_299_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_299_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_299 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_in_select_zone_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_300 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_horizontal_line_below_reporting_panel_heading = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_horizontal_line_below_reporting_panel_heading_by_xpath()).text
            self.logger.info(f"actual horizontal line below reporting panel heading: "
                             f"{actual_horizontal_line_below_reporting_panel_heading}")
            expected_horizontal_line_below_reporting_panel_heading = Reporting_read_ini(). \
                get_expected_horizontal_line_below_reporting_panel_heading()
            self.logger.info(f"expected horizontal line below reporting panel heading: "
                             f"{expected_horizontal_line_below_reporting_panel_heading}")
            if actual_horizontal_line_below_reporting_panel_heading == \
                    expected_horizontal_line_below_reporting_panel_heading:
                self.logger.info("'Select zone(s) to narrow report results' is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_300.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_300.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_300_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_300_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_300 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_search_zones_textbox_is_visible_and_clickable_label_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_301 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            search_zone_textbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_search_zone_textbox_by_xpath())
            if search_zone_textbox.is_displayed():
                self.logger.info("Select zone textbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if search_zone_textbox.is_enabled():
                self.logger.info("Select zone textbox is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            search_zone_textbox.click()
            time.sleep(web_driver.one_second)
            actual_label_on_search_zone_textbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                      get_search_zone_textbox_by_xpath()). \
                get_attribute("placeholder")
            self.logger.info(f"actual label on search zone textbox: {actual_label_on_search_zone_textbox}")
            expected_label_on_search_zone_textbox = Reporting_read_ini().get_expected_label_on_search_zone_textbox()
            self.logger.info(f"expected label on search zone textbox: {expected_label_on_search_zone_textbox}")
            if actual_label_on_search_zone_textbox == expected_label_on_search_zone_textbox:
                self.logger.info("'Search zone...' label on textbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_301.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_301.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_301_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_301_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_301 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_zone_list_below_search_zones_textbox_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_302 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            self.logger.info(f"Zone items below 'Search zone' textbox: {len(zone_items_list)}")
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_zone_module_on_dashboard_by_xpath()).click()
            time.sleep(web_driver.one_second)

            actual_zone_item_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                         get_zone_item_list_from_zone_panel_by_xpath())
            self.logger.info(f"Actual zones list from 'Zones' module: {len(actual_zone_item_list)}")
            time.sleep(web_driver.one_second)
            if len(zone_items_list) == len(actual_zone_item_list):
                self.logger.info("Zones list items list is visible....")
                self.status.append(True)
            else:
                self.status.append(False)

            for items in zone_items_list:
                if items.is_displayed():
                    self.status.append(True)
                else:
                    self.status.append(False)
                if items.is_enabled():
                    self.status.append(True)
                else:
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_302.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_302.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_302_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_302_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_302 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_select_all_button_in_zone_filter_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_303 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()). \
                    is_displayed():
                self.logger.info("Select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()). \
                    is_enabled():
                self.logger.info("Select all button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_select_all_button_in_zone_filter = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()).text
            self.logger.info(f"actual text on btn: {actual_text_on_select_all_button_in_zone_filter}")
            self.logger.info(f"expected text on btn: {Reporting_read_ini().get_expected_text_on_select_all_button()}")
            if actual_text_on_select_all_button_in_zone_filter == \
                    Reporting_read_ini().get_expected_text_on_select_all_button():
                self.logger.info("text on select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_303.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_303.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_303_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_303_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_303 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_selected_zone_list_title_and_default_text_below_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_304 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_selected_zone_list_title = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                  get_selected_zone_list_title_by_xpath()).text
            self.logger.info(f"actual title text: {actual_selected_zone_list_title}")
            expected_selected_zone_list_title = Reporting_read_ini().get_expected_selected_zone_list_title()
            self.logger.info(f"expected title text: {expected_selected_zone_list_title}")
            if actual_selected_zone_list_title == expected_selected_zone_list_title:
                self.logger.info("'Selected zone list' title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_first_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_first_default_text_line_below_selected_zone_list_title_by_xpath()).text
            self.logger.info(f"actual first default line below title: {actual_first_horizontal_line}")
            expected_first_horizontal_line = Reporting_read_ini(). \
                get_expected_first_default_text_line_below_selected_zone_list_title()
            self.logger.info(f"expected first default line below title: {expected_first_horizontal_line}")
            if actual_first_horizontal_line == expected_first_horizontal_line:
                self.logger.info("first default text line below selected zone list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_second_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_second_default_text_line_below_selected_zone_list_title_by_xpath()).text
            self.logger.info(f"actual second default line below title: {actual_second_horizontal_line}")
            expected_second_horizontal_line = Reporting_read_ini(). \
                get_expected_second_default_text_line_below_selected_zone_list_title()
            self.logger.info(f"expected second default line below title: {expected_second_horizontal_line}")
            if actual_second_horizontal_line == expected_second_horizontal_line:
                self.logger.info("second default text line below selected zone list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_304.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_304.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_304_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_304_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_304 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_close_zone_menu_button_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_305 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            close_zone_menu_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                         get_close_zone_menu_button_by_xpath())
            if close_zone_menu_button.is_displayed():
                self.logger.info("'Close zone menu' button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if close_zone_menu_button.is_enabled():
                self.logger.info("'Close zone menu' button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_close_zone_menu_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_text_on_close_zone_menu_button_by_xpath()).text
            self.logger.info(f"actual text on btn: {actual_text_on_close_zone_menu_button}")
            expected_text_on_close_zone_menu_button = Reporting_read_ini().get_expected_text_on_close_zone_menu_button()
            self.logger.info(f"expected text on btn: {expected_text_on_close_zone_menu_button}")
            if actual_text_on_close_zone_menu_button == expected_text_on_close_zone_menu_button:
                self.logger.info("text on 'Close zone menu' is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_305.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_305.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_305_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_305_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_305 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_click_on_select_all_button_and_verify_all_selected_zones_are_visible_in_selected_zone_list(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_306 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                             get_zone_items_list_below_search_zone_textbox_by_xpath())
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)
            selected_zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                      get_selected_zone_list_items_by_xpath())

            if len(selected_zone_list) == len(zone_list):
                self.logger.info("All selected zones are visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_306.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_306.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_306_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_306_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_306 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_click_on_select_all_button_in_zone_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_307 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            clear_all_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_clear_all_button_on_selected_zone_by_xpath())
            if clear_all_button.is_displayed():
                self.logger.info("'Clear all' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if clear_all_button.is_enabled():
                self.logger.info("'Clear all' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_clear_all_button_on_selected_zone_by_xpath()).text
            self.logger.info(f"actual text on 'Clear all' button: {actual_text_on_button}")
            self.logger.info(f"expected text on 'Clear all' button: "
                             f"{Reporting_read_ini().get_expected_clear_all_text()}")
            if actual_text_on_button == Reporting_read_ini().get_expected_clear_all_text():
                self.logger.info("text on 'Clear all' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_307.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_307.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_307_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_307_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_307 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_click_on_select_all_button_and_verify_save_zone_selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_308 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            save_zone_selection_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                             get_save_zone_selection_button_by_xpath())
            if save_zone_selection_button.is_displayed():
                self.logger.info("'Save zone selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if save_zone_selection_button.is_enabled():
                self.logger.info("'Save zone selection' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_dot_circle_icon_on_save_zone_selection_button()).\
                    is_displayed():
                self.logger.info("dot circle icon on 'Save group selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_save_zone_selection_text_by_xpath()).text
            self.logger.info(f"actual text on 'Save zone selection' button: {actual_text_on_button}")
            self.logger.info(f"expected text on button: {Reporting_read_ini().get_expected_save_zone_selection_text()}")
            if actual_text_on_button == Reporting_read_ini().get_expected_save_zone_selection_text():
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_308.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_308.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_308_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_308_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_308 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_select_one_zone_from_zone_list_and_verify_selected_zone_is_visible_in_selected_zone_list_verify_save_zone_selection_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_309 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            actual_first_zone = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                     get_first_zone_in_search_zone_list_by_xpath())
            first_zone_name = actual_first_zone[0].text
            zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                             get_zone_items_list_below_search_zone_textbox_by_xpath())
            zone_list[0].click()
            self.logger.info("Selected first zone from zones list...")
            time.sleep(web_driver.one_second)

            first_name_from_selected_zone_list = \
                self.d.find_element(By.XPATH,
                                    Reporting_read_ini().get_first_zone_name_in_selected_zone_list_by_xpath()).text
            if first_zone_name == first_name_from_selected_zone_list:
                self.logger.info("Selected zone is visible in Selected zones list...")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()). \
                    is_displayed():
                self.logger.info("'Save zone selection' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_309.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_309.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_309_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_309_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_309 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_click_on_save_zone_selection_button_with_at_least_one_zone_selected_and_verify_View_and_edit_zones_button_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_310 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                             get_zone_items_list_below_search_zone_textbox_by_xpath())
            zone_list[0].click()
            self.logger.info("Selected first zone from zones list...")
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button...")
            time.sleep(web_driver.one_second)

            view_edit_zones_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                         get_view_and_edit_zones_button_by_xpath())
            if view_edit_zones_button.is_displayed():
                self.logger.info("'View & edit ZONES' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if view_edit_zones_button.is_enabled():
                self.logger.info("'View & edit ZONES' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_310.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_310.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_310_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_310_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_310 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_day_of_week_verify_text_and_numeric_value_of_number_of_selected_zones_on_view_and_edit_zones_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_DW_311 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                             get_zone_items_list_below_search_zone_textbox_by_xpath())
            zone_list[0].click()
            self.logger.info("Selected first zone from zone list...")
            time.sleep(web_driver.one_second)

            selected_zones = self.d.find_elements(By.XPATH,
                                                  Reporting_read_ini().get_selected_zone_list_items_by_xpath())

            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button...")
            time.sleep(web_driver.one_second)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_view_and_edit_zones_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on button: {actual_text_on_button}")
            expected_numeric_value_of_zone_selected = f"{len(selected_zones)}" + " " + "selected"

            if Reporting_read_ini().get_expected_view_and_edit_zones_text() in actual_text_on_button:
                self.logger.info("'View & edit ZONES' text is visible on button...")
                self.status.append(True)
            else:
                self.status.append(False)
            if expected_numeric_value_of_zone_selected in actual_text_on_button:
                self.logger.info(f"numeric value of expected selected zones: "
                                 f"{expected_numeric_value_of_zone_selected}")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_311.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_311.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_311_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_311_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_311 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def select_number_of_events_by_hour_of_week(self):
        try:
            time.sleep(web_driver.one_second)
            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            time.sleep(web_driver.one_second)
            field1.select_by_visible_text('number of probable match events')
            field2 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_report_field2_dropdown_for_events_by_xpath()))
            time.sleep(web_driver.one_second)
            field2.select_by_visible_text('hour of week')
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def For_number_of_events_by_hour_of_week_verify_number_of_events_from_report_field1_and_hour_of_week_from_report_field2_texts_are_visible_on_dropdown(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_312 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            time.sleep(web_driver.one_second)
            field1.select_by_visible_text('number of probable match events')

            value1 = self.d.find_element(By.XPATH,
                                         Reporting_read_ini().get_report_field1_dropdown_by_xpath()).get_attribute(
                'value')
            self.logger.info(f"Value1: {value1}")
            if "number of events" in value1:
                self.logger.info("Selected 'number of events' from report field1 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            field2 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_report_field2_dropdown_for_events_by_xpath()))
            field2.select_by_visible_text('hour of week')

            value2 = self.d.find_element(By.XPATH, Reporting_read_ini().
                                         get_report_field2_dropdown_for_events_by_xpath()).get_attribute(
                'value')
            self.logger.info(f"Value2: {value2}")
            if Reporting_read_ini().get_expected_third_text_from_field2() in value2:
                self.logger.info("Selected 'hour of week' from report field2 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_312.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_312.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_312_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_312_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_312 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_boxes_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_313 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            actual_date_and_time_range_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                  get_date_and_time_range_text_by_xpath()).text
            self.logger.info(f"actual date & time range text: {actual_date_and_time_range_text}")
            expected_date_range_text = Reporting_read_ini().get_expected_date_and_time_range_text()
            self.logger.info(f"expected date & time range text: {expected_date_range_text}")
            if actual_date_and_time_range_text == expected_date_range_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_to_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_to_text_by_xpath()).text
            self.logger.info(f"actual 'to' text: {actual_to_text}")
            expected_to_text = Reporting_read_ini().get_expected_to_text()
            self.logger.info(f"expected 'to' text: {expected_to_text}")
            if actual_to_text == expected_to_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_horizontal_line_below_calenders = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_horizontal_line_below_calenders_by_xpath()).text
            self.logger.info(f"actual horizontal line below calenders: {actual_horizontal_line_below_calenders}")
            expected_horizontal_line_below_calenders = Reporting_read_ini(). \
                get_expected_horizontal_line_below_calenders()
            self.logger.info(f"expected horizontal line below calenders: {expected_horizontal_line_below_calenders}")
            if actual_horizontal_line_below_calenders == expected_horizontal_line_below_calenders:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_313.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_313.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_313_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_313_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_313 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_314 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            start_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_start_date_calender_box_by_xpath())
            if start_date_calender_box.is_displayed():
                self.logger.info("Start date calender box is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if start_date_calender_box.is_enabled():
                self.status.append(False)
            else:
                self.logger.info("start date calender box is disabled by default !!")
                self.status.append(True)
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            if start_date_checkbox.is_displayed():
                self.logger.info("Start date checkbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if start_date_checkbox.is_enabled():
                self.logger.info("Start date checkbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_314.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_314.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_314_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_314_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_314 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_315 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            end_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_end_date_calender_box_by_xpath())
            if end_date_calender_box.is_displayed():
                self.logger.info("End date calender box is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if end_date_calender_box.is_enabled():
                self.status.append(False)
            else:
                self.logger.info("End date calender box is disabled by default !!")
                self.status.append(True)
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            if end_date_checkbox.is_displayed():
                self.logger.info("End date checkbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if end_date_checkbox.is_enabled():
                self.logger.info("End date checkbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_315.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_315.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_315_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_315_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_315 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_316 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            start_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_start_date_calender_box_by_xpath())
            start_calender_disabled_status = start_date_calender_box.get_attribute("disabled")
            if start_date_checkbox.is_selected():
                start_date_checkbox.click()
                if start_calender_disabled_status:
                    self.logger.info("start calender disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"start date disable status: {start_calender_disabled_status}")
                if start_calender_disabled_status:
                    self.logger.info("start calender already disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            start_date_checkbox.click()
            self.logger.info(f"start calender disable status after click: "
                             f"{start_date_calender_box.get_attribute('disabled')}")
            if start_date_calender_box.get_attribute("disabled") is None:
                self.logger.info("start calender enabled !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if start_date_checkbox.is_selected():
                start_date_checkbox.click()
            else:
                pass
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_316.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_316.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_316_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_316_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_316 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_317 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            end_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_end_date_calender_box_by_xpath())
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            end_calender_disabled_status = end_date_calender_box.get_attribute("disabled")
            if end_date_checkbox.is_selected():
                end_date_checkbox.click()
                if end_calender_disabled_status:
                    self.logger.info("End calender disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"End calender disable status: {end_calender_disabled_status}")
                if end_calender_disabled_status:
                    self.logger.info("End calender already disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            end_date_checkbox.click()
            self.logger.info(f"End calender disable status after click: "
                             f"{end_date_calender_box.get_attribute('disabled')}")
            if end_date_calender_box.get_attribute("disabled") is None:
                self.logger.info("End calender enabled !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if end_date_checkbox.is_selected():
                end_date_checkbox.click()
            else:
                pass
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_317.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_317.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_317_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_317_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_317 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_318 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            action = ActionChains(self.d)
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            start_checkbox_hover = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                       get_include_in_search_hover_on_start_checkbox_by_xpath())
            action.move_to_element(start_date_checkbox).perform()
            if start_checkbox_hover.get_attribute("aria-describedby"):
                self.logger.info("'Include In Search' hover is visible for start date checkbox !!")
                self.status.append(True)
            else:
                self.logger.error("'Include In Search' hover is not visible for start date checkbox !!")
                self.status.append(False)
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            end_checkbox_hover = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                     get_include_in_search_hover_on_end_checkbox_by_xpath())
            action.move_to_element(end_date_checkbox).perform()
            if end_checkbox_hover.get_attribute("aria-describedby"):
                self.logger.info("'Include In Search' hover is visible for end date checkbox !!")
                self.status.append(True)
            else:
                self.logger.error("'Include In Search' hover is not visible for end date checkbox !!")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_318.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_318.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_318_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_318_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_318 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()


    def For_number_of_events_by_hour_of_week_verify_Optional_Filter_text_is_visible_text_beside_Select_group_filter_button_and_that_of_Select_zone_filter_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_319 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            time.sleep(web_driver.one_second)
            actual_optional_filters_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                               get_optional_filters_text_by_xpath()).text
            self.logger.info(f"actual optional filter text: {actual_optional_filters_text}")
            expected_optional_filters_text = Reporting_read_ini().get_expected_optional_filters_text()
            self.logger.info(f"expected optional filter text: {expected_optional_filters_text}")
            if actual_optional_filters_text in expected_optional_filters_text:
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            actual_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                              get_text_beside_select_group_filter_button_by_xpath()).text
            self.logger.info(f"actual text beside group filter button: {actual_text}")
            expected_text = Reporting_read_ini().get_expected_text_beside_select_group_filter_button()
            self.logger.info(f"expected text: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_beside_zone_filter_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_text_beside_select_zone_filter_button_by_xpath()).text
            self.logger.info(f"actual text beside zone filter button: {actual_text_beside_zone_filter_button}")
            expected_text_beside_zone_filter_btn = Reporting_read_ini().\
                get_expected_text_beside_select_zone_filter_button()
            self.logger.info(f"expected text: {expected_text_beside_zone_filter_btn}")
            if actual_text_beside_zone_filter_button == expected_text_beside_zone_filter_btn:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_319.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_319.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_319_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_319_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_319 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_Select_group_filter_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_320 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            time.sleep(web_driver.one_second)
            select_group_filter_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                             get_select_group_filter_button_by_xpath())
            if select_group_filter_button.is_displayed():
                self.logger.info("Select group filter button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if select_group_filter_button.is_enabled():
                self.logger.info("Select group filter button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                              get_select_group_filter_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on Select group filter button: {actual_text}")
            expected_text = Reporting_read_ini().get_expected_text_on_select_group_filter_button()
            self.logger.info(f"expected text on Select group filter button: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            group_icon_on_select_grp_btn = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                               get_group_icon_on_select_group_filter_button_by_xpath())
            if group_icon_on_select_grp_btn.is_displayed():
                self.logger.info("group icon on Select group filter button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_320.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_320.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_320_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_320_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_320 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_Select_zone_filter_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_321 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            time.sleep(web_driver.one_second)
            select_zone_filter_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                            get_select_zone_filter_button_by_xpath())
            if select_zone_filter_button.is_displayed():
                self.logger.info("Select zone filter button is visible !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            if select_zone_filter_button.is_enabled():
                self.logger.info("Select zone filter button is clickable !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_select_zone_button = self.d.find_element(
                By.XPATH, Reporting_read_ini().get_select_zone_filter_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on 'Select zone filter' button: {actual_text_on_select_zone_button}")
            expected_text_on_select_zone_button = Reporting_read_ini().get_expected_text_on_select_zone_filter_button()
            self.logger.info(f"expected text on 'Select zone filter' button: {expected_text_on_select_zone_button}")
            if actual_text_on_select_zone_button == expected_text_on_select_zone_button:
                self.logger.info(" text on select zone button is visible !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_dot_circle_icon_for_zone_by_xpath()). \
                    is_displayed():
                self.logger.info(" dot circle zone icon on button is visible !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            time.sleep(web_driver.one_second)
            
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_321.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_321.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_321_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_321_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_321 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_Generate_Report_button_is_visible_and_clickable_text_and_chart_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_322 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            generate_report_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                         get_generate_report_button_by_xpath())
            if generate_report_button.is_displayed():
                self.logger.info("Generate report button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if generate_report_button.is_enabled():
                self.logger.info("Generate report button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_chart_icon_on_generate_report_button_by_xpath()).\
                    is_displayed():
                self.logger.info("chart icon on Generate report button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_generate_report_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on Generate report button: {actual_text_on_generate_report_button}")
            expected_text_on_generate_report_button = Reporting_read_ini().get_expected_generate_report_text_on_button()
            self.logger.info(f"expected text on Generate report button: {expected_text_on_generate_report_button}")
            if actual_text_on_generate_report_button == expected_text_on_generate_report_button:
                self.status.append(True)
            else:
                self.status.append(False)
            chart_icon_on_generate_report_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_chart_icon_on_generate_report_button_by_xpath())
            if chart_icon_on_generate_report_button.is_displayed():
                self.logger.info("Chart icon on Generate report button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_322.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_322.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_322_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_322_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_322 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_in_Select_group_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_323 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_horizontal_line_below_reporting_panel_heading = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_horizontal_line_below_reporting_panel_heading_for_group_by_xpath()).text
            self.logger.info(f"actual horizontal line below  heading: "
                             f"{actual_horizontal_line_below_reporting_panel_heading}")
            expected_horizontal_line_below_reporting_panel_heading = Reporting_read_ini(). \
                get_expected_horizontal_line_below_reporting_panel_heading_for_group()
            self.logger.info(f"expected horizontal line below  heading: "
                             f"{expected_horizontal_line_below_reporting_panel_heading}")
            if actual_horizontal_line_below_reporting_panel_heading == \
                    expected_horizontal_line_below_reporting_panel_heading:
                self.logger.info("Horizontal line below panel heading is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_323.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_323.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_323_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_323_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_323 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_filter_group_list_below_textbox_is_visible_and_clickable_label_on_textbox_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_324 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            filter_group_list_textbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                            get_filter_group_list_textbox_by_xpath())
            if filter_group_list_textbox.is_displayed():
                self.logger.info("'filter group list below..' textbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if filter_group_list_textbox.is_enabled():
                self.logger.info("'filter group list below..' textbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            filter_group_list_textbox.click()
            actual_label_on_textbox = filter_group_list_textbox.get_attribute('placeholder')
            self.logger.info(f"actual label on textbox: {actual_label_on_textbox}")
            expected_label = Reporting_read_ini().get_expected_label_on_filter_group_list_below_textbox()
            self.logger.info(f"expected label on textbox: {expected_label}")
            if actual_label_on_textbox == expected_label:
                self.logger.info("label is visible on textbox..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_324.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_324.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_324_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_324_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_324 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_group_list_below_filter_group_list_textbox_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_325 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                    get_group_items_list_below_filter_group_list_textbox())
            self.logger.info(f"Group items below 'filter group list' textbox: {len(group_items_list)}")
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH,
                                Reporting_read_ini().get_enrollment_groups_module_on_dashboard_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_group_list_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                           get_group_item_list_from_enrollment_group_panel_by_xpath())
            time.sleep(web_driver.one_second)
            self.logger.info(f"Actual group items from 'Enrollment Groups': {len(actual_group_list_items)}")
            if len(group_items_list) == len(actual_group_list_items):

                self.logger.info("Group list items are visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            '''''
            for items in group_items_list:
                if items.is_displayed():
                    self.status.append(True)
                else:
                    self.status.append(False)
                if items.is_enabled():
                    self.status.append(True)
                else:
                    self.status.append(False)
            '''''
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_325.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_325.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_325_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_325_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_325 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_select_all_button_in_group_filter_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_326 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            select_all_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                    get_select_all_button_in_group_filter_by_xpath())
            if select_all_button.is_displayed():
                self.logger.info("Select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if select_all_button.is_enabled():
                self.logger.info("Select all button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_select_all_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_select_all_button_in_group_filter_by_xpath()).text
            self.logger.info(f"actual text on select all button in group filter: {actual_text_on_select_all_button}")
            self.logger.info(f"expected text on select all button in group filter: "
                             f"{Reporting_read_ini().get_expected_text_on_select_all_button()}")
            if actual_text_on_select_all_button == Reporting_read_ini().get_expected_text_on_select_all_button():
                self.logger.info("text on Select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_326.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_326.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_326_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_326_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_326 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_selected_group_list_title_and_default_text_below_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_327 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_selected_group_list_title = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual title: {actual_selected_group_list_title}")
            self.logger.info(f"expected title: {Reporting_read_ini().get_expected_selected_group_list_title()}")
            if actual_selected_group_list_title == Reporting_read_ini().get_expected_selected_group_list_title():
                self.logger.info("'Selected group list' title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_first_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_first_default_te_below_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual first horizontal line: {actual_first_horizontal_line}")
            expected_first_horizontal_line = \
                Reporting_read_ini().get_expected_first_default_text_line_below_selected_group_list_title()
            self.logger.info(f"expected first horizontal line: {expected_first_horizontal_line}")
            if actual_first_horizontal_line == expected_first_horizontal_line:
                self.logger.info("First default text line below selected group list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_second_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_second_default_text_below_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual second default text line below 'Selected group list' title: "
                             f"{actual_second_horizontal_line}")
            expected_second_horizontal_line = \
                Reporting_read_ini().get_expected_second_default_text_line_below_selected_group_list_title()
            self.logger.info(f"expected second horizontal line: {expected_second_horizontal_line}")
            if actual_second_horizontal_line == expected_second_horizontal_line:
                self.logger.info("Second default text line below selected group list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_327.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_327.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_327_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_327_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_327 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_close_group_menu_button_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_328 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            close_group_menu_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_close_group_menu_button_by_xpath())
            if close_group_menu_button.is_displayed():
                self.logger.info("'Close group menu' button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if close_group_menu_button.is_enabled():
                self.logger.info("'Close group menu' button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_close_group_menu_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_text_on_close_group_menu_button_by_xpath()).text
            self.logger.info(f"actual text on close menu btn: {actual_text_on_close_group_menu_button}")
            expected_text_on_close_group_button = Reporting_read_ini().get_expected_text_on_close_group_menu_button()
            self.logger.info(f"expected text on close menu btn: {expected_text_on_close_group_button}")
            if actual_text_on_close_group_menu_button == expected_text_on_close_group_button:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_328.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_328.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_328_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_328_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_328 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_click_on_select_all_button_and_verify_all_selected_groups_are_visible_in_selected_group_list(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_329 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_items_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_group_items_list_below_filter_group_list_textbox())
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)
            selected_group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_selected_group_list_items_by_xpath())
            if len(selected_group_list) == len(group_items_list):
                self.logger.info("All selected groups are visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_329.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_329.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_329_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_329_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_329 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_click_on_select_all_button_in_group_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_330 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            clear_all_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_clear_all_button_on_selected_group_by_xpath())
            if clear_all_button.is_displayed():
                self.logger.info("'Clear all' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if clear_all_button.is_enabled():
                self.logger.info("'Clear all' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_clear_all_button_on_selected_group_by_xpath()).text
            self.logger.info(f"actual text on 'Clear all' button: {actual_text_on_button}")
            self.logger.info(f"expected text on 'Clear all' button: "
                             f"{Reporting_read_ini().get_expected_clear_all_text()}")
            if actual_text_on_button == Reporting_read_ini().get_expected_clear_all_text():
                self.logger.info("text on 'Clear all' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_330.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_330.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_330_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_330_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_330 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_click_on_select_all_button_and_verify_save_group_selection_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_331 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            save_group_selection_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                              get_save_group_selection_button_by_xpath())
            if save_group_selection_button.is_displayed():
                self.logger.info("'Save group selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if save_group_selection_button.is_enabled():
                self.logger.info("'Save group selection' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH,
                                   Reporting_read_ini().get_group_icon_on_save_group_selection_button_by_xpath()).\
                    is_displayed():
                self.logger.info("group icon on 'Save group selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_save_group_selection_text_by_xpath()).text
            self.logger.info(f"actual text on 'Save group selection' button: {actual_text_on_button}")
            expected_text = Reporting_read_ini().get_expected_text_on_save_group_selection_button()
            self.logger.info(f"expected text on button: {expected_text}")
            if actual_text_on_button == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_331.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_331.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_331_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_331_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_331 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_select_one_group_from_group_list_and_verify_selected_group_is_visible_in_selected_group_list_verify_save_group_selection_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_332 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_group_items_list_below_filter_group_list_textbox())
            first_group_name = group_list[0].text
            group_list[0].click()
            self.logger.info("Selected first group from groups list...")
            time.sleep(web_driver.one_second)
            selected_group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_selected_group_list_items_by_xpath())
            if first_group_name == selected_group_list[0].text:
                self.logger.info("Selected group is visible in Selected group list...")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH,
                                   Reporting_read_ini().get_save_group_selection_button_by_xpath()).is_displayed():
                self.logger.info("'Save group selection' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_332.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_332.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_332_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_332_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_332 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_click_on_save_group_selection_button_with_at_least_one_group_selected_and_verify_View_and_edit_groups_button_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_333 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.two_second)

            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            group_list[0].click()
            self.logger.info("Selected first group from group list...")
            time.sleep(web_driver.two_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save group selection' button...")
            time.sleep(web_driver.two_second)

            view_edit_groups_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_view_and_edit_groups_button_by_xpath())
            if view_edit_groups_button.is_displayed():
                self.logger.info("'View & edit GROUPS' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if view_edit_groups_button.is_enabled():
                self.logger.info("'View & edit GROUPS' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_333.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_333.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_333_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_333_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_333 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_text_and_numeric_value_of_number_of_selected_groups_on_view_and_edit_groups_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_334 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            group_list[0].click()
            self.logger.info("Selected first group from group list...")
            group_list[1].click()
            self.logger.info("Selected second group from group list...")
            time.sleep(web_driver.one_second)
            selected_groups = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_selected_group_list_items_by_xpath())
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save group selection' button...")
            time.sleep(web_driver.one_second)
            actual_text_on_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_view_and_edit_groups_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on button: {actual_text_on_button}")
            expected_numeric_value_of_group_selected = f"{len(selected_groups)}" + " " + "selected"

            if Reporting_read_ini().get_expected_text_on_view_and_edit_groups_button() in actual_text_on_button:
                self.logger.info("'View & edit GROUPS' text is visible on button...")
                self.status.append(True)
            else:
                self.status.append(False)
            if expected_numeric_value_of_group_selected in actual_text_on_button:
                self.logger.info(f"numeric value of expected selected groups: "
                                 f"{expected_numeric_value_of_group_selected}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_334.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_334.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_334_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_334_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_334 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_in_select_zone_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_335 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_horizontal_line_below_reporting_panel_heading = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_horizontal_line_below_reporting_panel_heading_by_xpath()).text
            self.logger.info(f"actual horizontal line below reporting panel heading: "
                             f"{actual_horizontal_line_below_reporting_panel_heading}")
            expected_horizontal_line_below_reporting_panel_heading = Reporting_read_ini(). \
                get_expected_horizontal_line_below_reporting_panel_heading()
            self.logger.info(f"expected horizontal line below reporting panel heading: "
                             f"{expected_horizontal_line_below_reporting_panel_heading}")
            if actual_horizontal_line_below_reporting_panel_heading == \
                    expected_horizontal_line_below_reporting_panel_heading:
                self.logger.info("'Select zone(s) to narrow report results' is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_335.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_335.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_335_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_335_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_335 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_search_zones_textbox_is_visible_and_clickable_label_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_336 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            search_zone_textbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_search_zone_textbox_by_xpath())
            if search_zone_textbox.is_displayed():
                self.logger.info("Select zone textbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if search_zone_textbox.is_enabled():
                self.logger.info("Select zone textbox is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            search_zone_textbox.click()
            time.sleep(web_driver.one_second)
            actual_label_on_search_zone_textbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                      get_search_zone_textbox_by_xpath()). \
                get_attribute("placeholder")
            self.logger.info(f"actual label on search zone textbox: {actual_label_on_search_zone_textbox}")
            expected_label_on_search_zone_textbox = Reporting_read_ini().get_expected_label_on_search_zone_textbox()
            self.logger.info(f"expected label on search zone textbox: {expected_label_on_search_zone_textbox}")
            if actual_label_on_search_zone_textbox == expected_label_on_search_zone_textbox:
                self.logger.info("'Search zone...' label on textbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_336.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_336.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_336_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_336_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_336 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_zone_list_below_search_zones_textbox_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_337 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            self.logger.info(f"Zone items below 'Search zone' textbox: {len(zone_items_list)}")
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_zone_module_on_dashboard_by_xpath()).click()
            time.sleep(web_driver.one_second)

            actual_zone_item_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                         get_zone_item_list_from_zone_panel_by_xpath())
            self.logger.info(f"Actual zones list from 'Zones' module: {len(actual_zone_item_list)}")
            time.sleep(web_driver.one_second)
            if len(zone_items_list) == len(actual_zone_item_list):
                self.logger.info("Zones list items list is visible....")
                self.status.append(True)
            else:
                self.status.append(False)

            for items in zone_items_list:
                if items.is_displayed():
                    self.status.append(True)
                else:
                    self.status.append(False)
                if items.is_enabled():
                    self.status.append(True)
                else:
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_337.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_337.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_337_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_337_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_337 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_select_all_button_in_zone_filter_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_338 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()). \
                    is_displayed():
                self.logger.info("Select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()). \
                    is_enabled():
                self.logger.info("Select all button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_select_all_button_in_zone_filter = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()).text
            self.logger.info(f"actual text on btn: {actual_text_on_select_all_button_in_zone_filter}")
            self.logger.info(f"expected text on btn: {Reporting_read_ini().get_expected_text_on_select_all_button()}")
            if actual_text_on_select_all_button_in_zone_filter == \
                    Reporting_read_ini().get_expected_text_on_select_all_button():
                self.logger.info("text on select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_338.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_338.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_338_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_338_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_338 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_selected_zone_list_title_and_default_text_below_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_339 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_selected_zone_list_title = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                  get_selected_zone_list_title_by_xpath()).text
            self.logger.info(f"actual title text: {actual_selected_zone_list_title}")
            expected_selected_zone_list_title = Reporting_read_ini().get_expected_selected_zone_list_title()
            self.logger.info(f"expected title text: {expected_selected_zone_list_title}")
            if actual_selected_zone_list_title == expected_selected_zone_list_title:
                self.logger.info("'Selected zone list' title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_first_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_first_default_text_line_below_selected_zone_list_title_by_xpath()).text
            self.logger.info(f"actual first default line below title: {actual_first_horizontal_line}")
            expected_first_horizontal_line = Reporting_read_ini(). \
                get_expected_first_default_text_line_below_selected_zone_list_title()
            self.logger.info(f"expected first default line below title: {expected_first_horizontal_line}")
            if actual_first_horizontal_line == expected_first_horizontal_line:
                self.logger.info("first default text line below selected zone list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_second_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_second_default_text_line_below_selected_zone_list_title_by_xpath()).text
            self.logger.info(f"actual second default line below title: {actual_second_horizontal_line}")
            expected_second_horizontal_line = Reporting_read_ini(). \
                get_expected_second_default_text_line_below_selected_zone_list_title()
            self.logger.info(f"expected second default line below title: {expected_second_horizontal_line}")
            if actual_second_horizontal_line == expected_second_horizontal_line:
                self.logger.info("second default text line below selected zone list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_339.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_339.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_339_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_339_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_339 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_close_zone_menu_button_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_340 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            close_zone_menu_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                         get_close_zone_menu_button_by_xpath())
            if close_zone_menu_button.is_displayed():
                self.logger.info("'Close zone menu' button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if close_zone_menu_button.is_enabled():
                self.logger.info("'Close zone menu' button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_close_zone_menu_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_text_on_close_zone_menu_button_by_xpath()).text
            self.logger.info(f"actual text on btn: {actual_text_on_close_zone_menu_button}")
            expected_text_on_close_zone_menu_button = Reporting_read_ini().get_expected_text_on_close_zone_menu_button()
            self.logger.info(f"expected text on btn: {expected_text_on_close_zone_menu_button}")
            if actual_text_on_close_zone_menu_button == expected_text_on_close_zone_menu_button:
                self.logger.info("text on 'Close zone menu' is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_340.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_340.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_340_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_340_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_340 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_click_on_select_all_button_and_verify_all_selected_zones_are_visible_in_selected_zone_list(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_341 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                             get_zone_items_list_below_search_zone_textbox_by_xpath())
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)
            selected_zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                      get_selected_zone_list_items_by_xpath())

            if len(selected_zone_list) == len(zone_list):
                self.logger.info("All selected zones are visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_341.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_341.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_341_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_341_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_341 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_click_on_select_all_button_in_zone_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_342 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            clear_all_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_clear_all_button_on_selected_zone_by_xpath())
            if clear_all_button.is_displayed():
                self.logger.info("'Clear all' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if clear_all_button.is_enabled():
                self.logger.info("'Clear all' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_clear_all_button_on_selected_zone_by_xpath()).text
            self.logger.info(f"actual text on 'Clear all' button: {actual_text_on_button}")
            self.logger.info(f"expected text on 'Clear all' button: "
                             f"{Reporting_read_ini().get_expected_clear_all_text()}")
            if actual_text_on_button == Reporting_read_ini().get_expected_clear_all_text():
                self.logger.info("text on 'Clear all' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_342.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_342.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_342_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_342_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_342 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_click_on_select_all_button_and_verify_save_zone_selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_343 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_zone_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            save_zone_selection_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                             get_save_zone_selection_button_by_xpath())
            if save_zone_selection_button.is_displayed():
                self.logger.info("'Save zone selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if save_zone_selection_button.is_enabled():
                self.logger.info("'Save zone selection' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_dot_circle_icon_on_save_zone_selection_button()).\
                    is_displayed():
                self.logger.info("dot circle icon on 'Save group selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_save_zone_selection_text_by_xpath()).text
            self.logger.info(f"actual text on 'Save zone selection' button: {actual_text_on_button}")
            self.logger.info(f"expected text on button: {Reporting_read_ini().get_expected_save_zone_selection_text()}")
            if actual_text_on_button == Reporting_read_ini().get_expected_save_zone_selection_text():
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_343.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_343.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_343_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_343_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_343 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_select_one_zone_from_zone_list_and_verify_selected_zone_is_visible_in_selected_zone_list_verify_save_zone_selection_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_344 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            actual_first_zone = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                     get_first_zone_in_search_zone_list_by_xpath())
            first_zone_name = actual_first_zone[0].text
            zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                             get_zone_items_list_below_search_zone_textbox_by_xpath())
            zone_list[0].click()
            self.logger.info("Selected first zone from zones list...")
            time.sleep(web_driver.one_second)

            first_name_from_selected_zone_list = \
                self.d.find_element(By.XPATH,
                                    Reporting_read_ini().get_first_zone_name_in_selected_zone_list_by_xpath()).text
            if first_zone_name == first_name_from_selected_zone_list:
                self.logger.info("Selected zone is visible in Selected zones list...")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()). \
                    is_displayed():
                self.logger.info("'Save zone selection' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_344.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_344.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_344_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_344_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_344 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_click_on_save_zone_selection_button_with_at_least_one_zone_selected_and_verify_View_and_edit_zones_button_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_345 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                             get_zone_items_list_below_search_zone_textbox_by_xpath())
            zone_list[0].click()
            self.logger.info("Selected first zone from zones list...")
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button...")
            time.sleep(web_driver.one_second)

            view_edit_zones_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                         get_view_and_edit_zones_button_by_xpath())
            if view_edit_zones_button.is_displayed():
                self.logger.info("'View & edit ZONES' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if view_edit_zones_button.is_enabled():
                self.logger.info("'View & edit ZONES' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_345.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_345.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_345_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_345_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_345 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_hour_of_week_verify_text_and_numeric_value_of_number_of_selected_zones_on_view_and_edit_zones_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_HW_346 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_day_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                             get_zone_items_list_below_search_zone_textbox_by_xpath())
            zone_list[0].click()
            self.logger.info("Selected first zone from zone list...")
            time.sleep(web_driver.one_second)

            selected_zones = self.d.find_elements(By.XPATH,
                                                  Reporting_read_ini().get_selected_zone_list_items_by_xpath())

            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button...")
            time.sleep(web_driver.one_second)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_view_and_edit_zones_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on button: {actual_text_on_button}")
            expected_numeric_value_of_zone_selected = f"{len(selected_zones)}" + " " + "selected"

            if Reporting_read_ini().get_expected_view_and_edit_zones_text() in actual_text_on_button:
                self.logger.info("'View & edit ZONES' text is visible on button...")
                self.status.append(True)
            else:
                self.status.append(False)
            if expected_numeric_value_of_zone_selected in actual_text_on_button:
                self.logger.info(f"numeric value of expected selected zones: "
                                 f"{expected_numeric_value_of_zone_selected}")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_346.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_346.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_346_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_346_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_346 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def select_number_of_events_by_zone(self):
        try:
            time.sleep(web_driver.one_second)
            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            time.sleep(web_driver.one_second)
            field1.select_by_visible_text('number of probable match events')
            field2 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_report_field2_dropdown_for_events_by_xpath()))
            time.sleep(web_driver.one_second)
            field2.select_by_visible_text('zone')
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def For_number_of_events_by_zone_verify_number_of_events_from_report_field1_and_zone_from_report_field2_texts_are_visible_on_dropdown(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_347 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            time.sleep(web_driver.one_second)
            field1.select_by_visible_text('number of probable match events')

            value1 = self.d.find_element(By.XPATH,
                                         Reporting_read_ini().get_report_field1_dropdown_by_xpath()).get_attribute(
                'value')
            self.logger.info(f"Value1: {value1}")
            if "number of events" in value1:
                self.logger.info("Selected 'number of events' from report field1 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            field2 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_report_field2_dropdown_for_events_by_xpath()))
            field2.select_by_visible_text('zone')

            value2 = self.d.find_element(By.XPATH, Reporting_read_ini().
                                         get_report_field2_dropdown_for_events_by_xpath()).get_attribute(
                'value')
            self.logger.info(f"Value2: {value2}")
            if Reporting_read_ini().get_expected_fourth_text_from_field2() in value2:
                self.logger.info("Selected 'zone' from report field2 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_347.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_347.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_347_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_347_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_347 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_boxes_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_348 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            actual_date_and_time_range_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                  get_date_and_time_range_text_by_xpath()).text
            self.logger.info(f"actual date & time range text: {actual_date_and_time_range_text}")
            expected_date_range_text = Reporting_read_ini().get_expected_date_and_time_range_text()
            self.logger.info(f"expected date & time range text: {expected_date_range_text}")
            if actual_date_and_time_range_text == expected_date_range_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_to_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_to_text_by_xpath()).text
            self.logger.info(f"actual 'to' text: {actual_to_text}")
            expected_to_text = Reporting_read_ini().get_expected_to_text()
            self.logger.info(f"expected 'to' text: {expected_to_text}")
            if actual_to_text == expected_to_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_horizontal_line_below_calenders = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_horizontal_line_below_calenders_by_xpath()).text
            self.logger.info(f"actual horizontal line below calenders: {actual_horizontal_line_below_calenders}")
            expected_horizontal_line_below_calenders = Reporting_read_ini(). \
                get_expected_horizontal_line_below_calenders()
            self.logger.info(f"expected horizontal line below calenders: {expected_horizontal_line_below_calenders}")
            if actual_horizontal_line_below_calenders == expected_horizontal_line_below_calenders:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_348.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_348.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_348_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_348_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_348 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_349 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            start_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_start_date_calender_box_by_xpath())
            if start_date_calender_box.is_displayed():
                self.logger.info("Start date calender box is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if start_date_calender_box.is_enabled():
                self.status.append(False)
            else:
                self.logger.info("start date calender box is disabled by default !!")
                self.status.append(True)
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            if start_date_checkbox.is_displayed():
                self.logger.info("Start date checkbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if start_date_checkbox.is_enabled():
                self.logger.info("Start date checkbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_349.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_349.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_349_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_349_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_349 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_350 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            end_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_end_date_calender_box_by_xpath())
            if end_date_calender_box.is_displayed():
                self.logger.info("End date calender box is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if end_date_calender_box.is_enabled():
                self.status.append(False)
            else:
                self.logger.info("End date calender box is disabled by default !!")
                self.status.append(True)
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            if end_date_checkbox.is_displayed():
                self.logger.info("End date checkbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if end_date_checkbox.is_enabled():
                self.logger.info("End date checkbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_350.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_350.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_350_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_350_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_350 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_351 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            start_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_start_date_calender_box_by_xpath())
            start_calender_disabled_status = start_date_calender_box.get_attribute("disabled")
            if start_date_checkbox.is_selected():
                start_date_checkbox.click()
                if start_calender_disabled_status:
                    self.logger.info("start calender disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"start date disable status: {start_calender_disabled_status}")
                if start_calender_disabled_status:
                    self.logger.info("start calender already disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            start_date_checkbox.click()
            self.logger.info(f"start calender disable status after click: "
                             f"{start_date_calender_box.get_attribute('disabled')}")
            if start_date_calender_box.get_attribute("disabled") is None:
                self.logger.info("start calender enabled !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if start_date_checkbox.is_selected():
                start_date_checkbox.click()
            else:
                pass
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_351.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_351.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_351_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_351_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_351 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_352 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            end_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_end_date_calender_box_by_xpath())
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            end_calender_disabled_status = end_date_calender_box.get_attribute("disabled")
            if end_date_checkbox.is_selected():
                end_date_checkbox.click()
                if end_calender_disabled_status:
                    self.logger.info("End calender disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"End calender disable status: {end_calender_disabled_status}")
                if end_calender_disabled_status:
                    self.logger.info("End calender already disabled !!!")
                    self.status.append(True)
                else:
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            end_date_checkbox.click()
            self.logger.info(f"End calender disable status after click: "
                             f"{end_date_calender_box.get_attribute('disabled')}")
            if end_date_calender_box.get_attribute("disabled") is None:
                self.logger.info("End calender enabled !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if end_date_checkbox.is_selected():
                end_date_checkbox.click()
            else:
                pass
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_352.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_352.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_352_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_352_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_352 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_353 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            action = ActionChains(self.d)
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            start_checkbox_hover = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                       get_include_in_search_hover_on_start_checkbox_by_xpath())
            action.move_to_element(start_date_checkbox).perform()
            if start_checkbox_hover.get_attribute("aria-describedby"):
                self.logger.info("'Include In Search' hover is visible for start date checkbox !!")
                self.status.append(True)
            else:
                self.logger.error("'Include In Search' hover is not visible for start date checkbox !!")
                self.status.append(False)
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            end_checkbox_hover = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                     get_include_in_search_hover_on_end_checkbox_by_xpath())
            action.move_to_element(end_date_checkbox).perform()
            if end_checkbox_hover.get_attribute("aria-describedby"):
                self.logger.info("'Include In Search' hover is visible for end date checkbox !!")
                self.status.append(True)
            else:
                self.logger.error("'Include In Search' hover is not visible for end date checkbox !!")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_353.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_353.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_353_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_353_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_353 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_verify_Optional_Filter_text_is_visible_text_beside_Select_group_filter_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_354 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            actual_optional_filter_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                              get_optional_filters_text_by_xpath()).text
            self.logger.info(f"actual optional filter text: {actual_optional_filter_text}")
            expected_optional_filters_text = Reporting_read_ini().get_expected_optional_filters_text()
            self.logger.info(f"expected optional filter text: {expected_optional_filters_text}")
            if actual_optional_filter_text in expected_optional_filters_text:
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            actual_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                              get_text_beside_select_group_filter_button_by_xpath()).text
            self.logger.info(f"actual text: {actual_text}")
            expected_text = Reporting_read_ini().get_expected_text_beside_select_group_filter_button()
            self.logger.info(f"expected text: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_354.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_354.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_354_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_354_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_354 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_verify_Select_group_filter_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_355 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            select_group_filter_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                             get_select_group_filter_button_by_xpath())
            if select_group_filter_button.is_displayed():
                self.logger.info("Select group filter button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if select_group_filter_button.is_enabled():
                self.logger.info("Select group filter button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                              get_select_group_filter_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on Select group filter button: {actual_text}")
            expected_text = Reporting_read_ini().get_expected_text_on_select_group_filter_button()
            self.logger.info(f"expected text on Select group filter button: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            group_icon_on_select_grp_btn = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                               get_group_icon_on_select_group_filter_button_by_xpath())
            if group_icon_on_select_grp_btn.is_displayed():
                self.logger.info("group icon on Select group filter button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_355.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_355.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_355_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_355_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_355 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_verify_generate_report_button_is_visible_and_clickable_generate_report_text_and_chart_icon_both_are_visible_on_button(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_356 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            generate_report_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                         get_generate_report_button_by_xpath())
            if generate_report_button.is_displayed():
                self.logger.info("Generate report button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if generate_report_button.is_enabled():
                self.logger.info("Generate report button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_chart_icon_on_generate_report_button_by_xpath()).\
                    is_displayed():
                self.logger.info("chart icon on Generate report button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_generate_report_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on Generate report button: {actual_text_on_generate_report_button}")
            expected_text_on_generate_report_button = Reporting_read_ini().get_expected_generate_report_text_on_button()
            self.logger.info(f"expected text on Generate report button: {expected_text_on_generate_report_button}")
            if actual_text_on_generate_report_button == expected_text_on_generate_report_button:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_356.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_356.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_356_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_356_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_356 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_in_Select_group_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_357 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_horizontal_line_below_reporting_panel_heading = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_horizontal_line_below_reporting_panel_heading_for_group_by_xpath()).text
            self.logger.info(f"actual horizontal line below panel heading: "
                             f"{actual_horizontal_line_below_reporting_panel_heading}")
            expected_horizontal_line_below_reporting_panel_heading = Reporting_read_ini(). \
                get_expected_horizontal_line_below_reporting_panel_heading_for_group()
            self.logger.info(f"expected horizontal line below panel heading: "
                             f"{expected_horizontal_line_below_reporting_panel_heading}")
            if actual_horizontal_line_below_reporting_panel_heading == \
                    expected_horizontal_line_below_reporting_panel_heading:
                self.logger.info("Horizontal line below panel heading is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_357.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_357.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_357_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_357_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_357 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_verify_filter_group_list_below_textbox_is_visible_and_clickable_label_on_textbox_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_358 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            filter_group_list_textbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                            get_filter_group_list_textbox_by_xpath())
            if filter_group_list_textbox.is_displayed():
                self.logger.info("'filter group list below..' textbox is visible")
                self.status.append(True)
            else:
                self.status.append(False)
            if filter_group_list_textbox.is_enabled():
                self.logger.info("'filter group list below..' textbox is clickable")
                self.status.append(True)
            else:

                self.status.append(False)
            filter_group_list_textbox.click()
            actual_label_on_textbox = filter_group_list_textbox.get_attribute('placeholder')
            self.logger.info(f"actual label on textbox: {actual_label_on_textbox}")
            expected_label_on_textbox = Reporting_read_ini().get_expected_label_on_filter_group_list_below_textbox()
            self.logger.info(f"expected label on textbox: {expected_label_on_textbox}")
            if actual_label_on_textbox == expected_label_on_textbox:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_358.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_358.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_358_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_358_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_358 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_verify_group_list_below_filter_group_list_textbox_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_359 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                    get_group_items_list_below_filter_group_list_textbox())
            self.logger.info(f"Group items below 'filter group list' textbox: {len(group_items_list)}")
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH,
                                Reporting_read_ini().get_enrollment_groups_module_on_dashboard_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_group_list_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                           get_group_item_list_from_enrollment_group_panel_by_xpath())
            time.sleep(web_driver.one_second)
            self.logger.info(f"Actual group items from 'Enrollment Groups': {len(actual_group_list_items)}")
            if len(group_items_list) == len(actual_group_list_items):
                self.logger.info("Group list items are visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            '''''
            for items in group_items_list:
                if items.is_displayed():
                    self.status.append(True)
                else:
                    self.status.append(False)
                if items.is_enabled():
                    self.status.append(True)
                else:
                    self.status.append(False)
            '''''
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_359.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_359.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_359_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_359_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_359 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_verify_select_all_button_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_360 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            select_all_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                    get_select_all_button_in_group_filter_by_xpath())
            if select_all_button.is_displayed():
                self.logger.info("Select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if select_all_button.is_enabled():
                self.logger.info("Select all button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_select_all_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_select_all_button_in_group_filter_by_xpath()).text
            self.logger.info(f"actual text on select all button in group filter: {actual_text_on_select_all_button}")
            self.logger.info(f"expected text on select all button in group filter: "
                             f"{Reporting_read_ini().get_expected_text_on_select_all_button()}")
            if actual_text_on_select_all_button == Reporting_read_ini().get_expected_text_on_select_all_button():
                self.logger.info("text on Select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_360.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_360.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_360_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_360_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_360 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_verify_selected_group_list_title_and_default_text_below_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_361 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_selected_group_list_title = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual title: {actual_selected_group_list_title}")
            self.logger.info(f"expected title: {Reporting_read_ini().get_expected_selected_group_list_title()}")
            if actual_selected_group_list_title == Reporting_read_ini().get_expected_selected_group_list_title():
                self.logger.info("'Selected group list' title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_first_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_first_default_te_below_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual first horizontal line: {actual_first_horizontal_line}")
            expected_first_horizontal_line = \
                Reporting_read_ini().get_expected_first_default_text_line_below_selected_group_list_title()
            self.logger.info(f"expected first horizontal line: {expected_first_horizontal_line}")
            if actual_first_horizontal_line == expected_first_horizontal_line:
                self.logger.info("First default text line below selected group list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_second_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_second_default_text_below_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual second default text line below 'Selected group list' title: "
                             f"{actual_second_horizontal_line}")
            expected_second_horizontal_line = \
                Reporting_read_ini().get_expected_second_default_text_line_below_selected_group_list_title()
            self.logger.info(f"expected second horizontal line: {expected_second_horizontal_line}")
            if actual_second_horizontal_line == expected_second_horizontal_line:
                self.logger.info("Second default text line below selected group list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_361.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_361.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_361_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_361_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_361 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_verify_close_group_menu_button_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_362 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            close_group_menu_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_close_group_menu_button_by_xpath())
            if close_group_menu_button.is_displayed():
                self.logger.info("'Close group menu' button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if close_group_menu_button.is_enabled():
                self.logger.info("'Close group menu' button is enabled !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_close_group_menu_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_text_on_close_group_menu_button_by_xpath()).text
            self.logger.info(f"actual text on close menu btn: {actual_text_on_close_group_menu_button}")
            expected_text_on_close_group_button = Reporting_read_ini().get_expected_text_on_close_group_menu_button()
            self.logger.info(f"expected text on close menu btn: {expected_text_on_close_group_button}")
            if actual_text_on_close_group_menu_button == expected_text_on_close_group_button:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_362.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_362.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_362_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_362_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_362 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_click_on_select_all_button_and_verify_all_selected_groups_are_visible_in_selected_group_list(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_363 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_items_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_group_items_list_below_filter_group_list_textbox())
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)
            selected_group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_selected_group_list_items_by_xpath())
            if len(selected_group_list) == len(group_items_list):
                self.logger.info("All selected groups are visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_363.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_363.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_363_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_363_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_363 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_click_on_select_all_button_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_364 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            clear_all_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_clear_all_button_on_selected_group_by_xpath())
            if clear_all_button.is_displayed():
                self.logger.info("'Clear all' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if clear_all_button.is_enabled():
                self.logger.info("'Clear all' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_clear_all_button_on_selected_group_by_xpath()).text
            self.logger.info(f"actual text on 'Clear all' button: {actual_text_on_button}")
            self.logger.info(f"expected text on 'Clear all' button: "
                             f"{Reporting_read_ini().get_expected_clear_all_text()}")
            if actual_text_on_button == Reporting_read_ini().get_expected_clear_all_text():
                self.logger.info("text on 'Clear all' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_364.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_364.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_364_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_364_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_364 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_click_on_select_all_button_and_verify_save_group_selection_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_365 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            self.logger.info("Clicked on 'Select all' button..")
            time.sleep(web_driver.one_second)

            save_group_selection_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                              get_save_group_selection_button_by_xpath())
            if save_group_selection_button.is_displayed():
                self.logger.info("'Save group selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            if save_group_selection_button.is_enabled():
                self.logger.info("'Save group selection' button is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH,
                                   Reporting_read_ini().get_group_icon_on_save_group_selection_button_by_xpath()).\
                    is_displayed():
                self.logger.info("group icon on 'Save group selection' button is visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text_on_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_save_group_selection_text_by_xpath()).text
            self.logger.info(f"actual text on 'Save group selection' button: {actual_text_on_button}")
            expected_text = Reporting_read_ini().get_expected_text_on_save_group_selection_button()
            self.logger.info(f"expected text on button: {expected_text}")
            if actual_text_on_button == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_365.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_365.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_365_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_365_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_365 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_select_one_group_from_group_list_and_verify_selected_group_is_visible_in_selected_group_list_verify_save_group_selection_button_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_366 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_group_items_list_below_filter_group_list_textbox())
            first_group_name = group_list[0].text
            group_list[0].click()
            self.logger.info("Selected first group from groups list...")
            time.sleep(web_driver.one_second)
            selected_group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_selected_group_list_items_by_xpath())
            if first_group_name == selected_group_list[0].text:
                self.logger.info("Selected group is visible in Selected group list...")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH,
                                   Reporting_read_ini().get_save_group_selection_button_by_xpath()).is_displayed():
                self.logger.info("'Save group selection' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_366.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_366.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_366_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_366_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_366 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_click_on_save_group_selection_button_with_at_least_one_group_selected_and_verify_View_and_edit_groups_button_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_367 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            group_list[0].click()
            self.logger.info("Selected first group from group list...")
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save group selection' button...")
            time.sleep(web_driver.one_second)

            view_edit_groups_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_view_and_edit_groups_button_by_xpath())
            if view_edit_groups_button.is_displayed():
                self.logger.info("'View & edit GROUPS' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if view_edit_groups_button.is_enabled():
                self.logger.info("'View & edit GROUPS' button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_367.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_367.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_367_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_367_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_367 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def For_number_of_events_by_zone_verify_text_and_numeric_value_of_number_of_selected_groups_on_view_and_edit_groups_button_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EV_ZN_368 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            group_list[0].click()
            self.logger.info("Selected first group from group list...")
            group_list[1].click()
            self.logger.info("Selected second group from group list...")
            time.sleep(web_driver.one_second)
            selected_groups = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_selected_group_list_items_by_xpath())
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save group selection' button...")
            time.sleep(web_driver.one_second)
            actual_text_on_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_view_and_edit_groups_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on button: {actual_text_on_button}")
            expected_numeric_value_of_group_selected = f"{len(selected_groups)}" + " " + "selected"

            if Reporting_read_ini().get_expected_text_on_view_and_edit_groups_button() in actual_text_on_button:
                self.logger.info("'View & edit GROUPS' text is visible on button...")
                self.status.append(True)
            else:
                self.status.append(False)
            if expected_numeric_value_of_group_selected in actual_text_on_button:
                self.logger.info(f"numeric value of expected selected groups: "
                                 f"{expected_numeric_value_of_group_selected}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_368.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_368.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_368_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_368_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_368 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def get_start_date(self):
        try:
            df_custom_dates = pd.read_json(self.custom_dates_json)
            self.start_date_and_time = list({df_custom_dates['date_range'][0]['start_date']})
            for items in self.start_date_and_time:
                items = items.split(' ')
                self.start_date = items[0]
                self.start_time = items[1]
                self.start_datetime = items[2]
            self.logger.info(f"start date: {self.start_date}{self.start_time}{self.start_datetime}")
            time.sleep(web_driver.one_second)
            start_date_calender_box = self.d.find_element(By.XPATH,
                                                          Reporting_read_ini().get_start_date_calender_box_by_xpath())
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            time.sleep(web_driver.one_second)
            start_date_checkbox.click()
            start_date_calender_box.click()
            action = ActionChains(self.d)
            time.sleep(web_driver.one_second)
            default_start_date = start_date_calender_box.get_attribute('value')
            default_start_date = list(default_start_date.split(' '))
            d_start_date = default_start_date[0]
            d_start_date = list(d_start_date.split('/'))
            s_month = d_start_date[0]
            s_date = d_start_date[1]
            input_start_date = list(self.start_date.split('/'))
            input_s_date = input_start_date[0]
            input_s_month = input_start_date[1]
            input_s_year = input_start_date[2]
            status = True
            if s_month < input_s_month:
                while status:
                    action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
                    current_date_and_time = start_date_calender_box.get_attribute('value')
                    current_date_and_time = list(current_date_and_time.split(' '))
                    current_date = current_date_and_time[0]
                    current_date = list(current_date.split('/'))
                    c_date = current_date[1]
                    c_month = current_date[0]
                    if c_month == input_s_month and c_date == input_s_date:
                        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                        self.logger.info(f"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
                        status = False
            elif s_month > input_s_month:
                while status:
                    action.key_down(Keys.ARROW_LEFT).key_up(Keys.ARROW_LEFT).perform()
                    current_date_and_time = start_date_calender_box.get_attribute('value')
                    current_date_and_time = list(current_date_and_time.split(' '))
                    current_date = current_date_and_time[0]
                    current_date = list(current_date.split('/'))
                    c_date = current_date[1]
                    c_month = current_date[0]
                    if c_month == input_s_month and c_date == input_s_date:
                        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                        self.logger.info(f"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
                        status = False
            else:
                if s_date > input_s_date:
                    while status:
                        action.key_down(Keys.ARROW_LEFT).key_up(Keys.ARROW_LEFT).perform()
                        current_date_and_time = start_date_calender_box.get_attribute('value')
                        current_date_and_time = list(current_date_and_time.split(' '))
                        current_date = current_date_and_time[0]
                        current_date = list(current_date.split('/'))
                        c_date = current_date[1]
                        c_month = current_date[0]
                        if c_month == input_s_month and c_date == input_s_date:
                            action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                            self.logger.info(f"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
                            status = False
                elif s_date < input_s_date:
                    while status:
                        action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
                        current_date_and_time = start_date_calender_box.get_attribute('value')
                        current_date_and_time = list(current_date_and_time.split(' '))
                        current_date = current_date_and_time[0]
                        current_date = list(current_date.split('/'))
                        c_date = current_date[1]
                        c_month = current_date[0]
                        if c_month == input_s_month and c_date == input_s_date:
                            action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                            self.logger.info(f"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
                            status = False
                else:
                    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        except Exception as ex:
            self.logger.error(ex)

    def get_end_date(self):
        try:
            df_custom_dates = pd.read_json(self.custom_dates_json)
            self.end_date_and_time = list({df_custom_dates['date_range'][0]['end_date']})
            for items in self.end_date_and_time:
                items = items.split(' ')
                self.end_date = items[0]
                self.end_time = items[1]
                self.end_datetime = items[2]
            self.logger.info(f"end date: {self.end_date}{self.end_time}{self.end_datetime}")
            time.sleep(web_driver.one_second)
            end_date_calender_box = self.d.find_element(By.XPATH,
                                                        Reporting_read_ini().get_end_date_calender_box_by_xpath())
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
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
                        self.logger.info(f"End date selected as:- {input_e_date}/{input_e_month}/{input_e_year}")
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
                        self.logger.info(f"End date selected as:- {input_e_date}/{input_e_month}/{input_e_year}")
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
                            self.logger.info(f"End date selected as:- {input_e_date}/{input_e_month}/{input_e_year}")
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
                            self.logger.info(f"End date selected as:- {input_e_date}/{input_e_month}/{input_e_year}")
                            status = False
                else:
                    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        except Exception as ex:
            self.logger.error(ex)

    def verify_report_for_number_of_events_by_enrollment_with_default_dates_1_month_and_with_group_selected_as_SOE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_EN_369 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_enrollment()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on 'Select group filter' button..")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_soe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_soe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on Generate report button")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_369.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_369.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_369_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_369_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_369 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_enrollment_with_default_dates_1_month_and_with_group_selected_as_ABE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_EN_370 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_enrollment()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on 'Select group filter' button..")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_abe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_abe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on Generate report button")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_370.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_370.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_370_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_370_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_370 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_enrollment_with_default_dates_1_month_and_with_group_selected_as_PTE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_EN_371 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_enrollment()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on 'Select group filter' button..")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_pte_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_pte_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on Generate report button")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_371.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_371.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_371_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_371_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_371 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_enrollment_with_default_dates_1_month_and_with_group_selected_as_FRAUDE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_EN_372 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_enrollment()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on 'Select group filter' button..")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_fraude_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_fraude_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on Generate report button")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_372.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_372.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_372_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_372_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_372 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_enrollment_with_default_dates_1_month_and_with_group_selected_as_VIPE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_EN_373 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_enrollment()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on 'Select group filter' button..")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_vipe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_vipe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on Generate report button")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_373.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_373.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_373_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_373_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_373 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_enrollment_with_date_range_from_json_file_with_group_selected_as_SOE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_EN_374 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_enrollment()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on 'Select group filter' button..")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_soe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_soe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on Generate report button")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_374.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_374.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_374_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_374_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_374 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_enrollment_with_date_range_from_json_file_with_group_selected_as_ABE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_EN_375 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_enrollment()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on 'Select group filter' button..")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_abe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_abe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on Generate report button")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_375.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_375.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_375_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_375_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_375 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_enrollment_with_date_range_from_json_file_with_group_selected_as_PTE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_EN_376 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_enrollment()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on 'Select group filter' button..")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_pte_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_pte_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on Generate report button")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(
                    f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_376.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_376.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_376_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_376_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_376 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_enrollment_with_date_range_from_json_file_with_group_selected_as_FRAUDE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_EN_377 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_enrollment()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on 'Select group filter' button..")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_fraude_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_fraude_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on Generate report button")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_377.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_377.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_377_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_377_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_377 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_enrollment_with_date_range_from_json_file_with_group_selected_as_VIPE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_EN_378 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_enrollment()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on 'Select group filter' button..")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_vipe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_vipe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on Generate report button")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_378.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_378.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_378_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_378_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_378 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_individual_report_for_number_of_events_by_enrollment_with_date_range_from_json_file_with_group_selected_as_SOE_ABE_PTE_FRAUDE_and_VIPE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_EN_379 started ************")
            self.load_reporting_module_for_admin()
            self.logger.info("executed load_reporting_module_for_admin")
            self.select_number_of_events_by_enrollment()
            self.logger.info("executed select_number_of_events_by_enrollment")
            self.get_age_range()
            self.logger.info("executed get_age_range")
            self.get_start_date()
            self.logger.info("executed get_start_date")
            self.get_end_date()
            self.logger.info("executed get_end_date")
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on 'Select group filter' button..")
            time.sleep(web_driver.one_second)
            self.groups_list = [Reporting_read_ini().get_abe_enrollment_group(),
                                Reporting_read_ini().get_soe_enrollment_group(),
                                Reporting_read_ini().get_pte_enrollment_group(),
                                Reporting_read_ini().get_fraude_enrollment_group(),
                                Reporting_read_ini().get_vipe_enrollment_group()]
            for i in range(len(self.groups_list)):
                time.sleep(web_driver.one_second)
                self.d.find_element(By.XPATH, Reporting_read_ini().get_filter_group_list_textbox_by_xpath()). \
                    send_keys(self.groups_list[i])
                group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                  get_group_items_list_below_filter_group_list_textbox())
                for items in group_list:
                    if items.text.upper() == self.groups_list[i].upper():
                        time.sleep(web_driver.one_second)
                        items.click()
                        self.logger.info(f"Selected group as: {self.groups_list[i]}")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
                        self.logger.info("clicked on save_group_selection_button_by_xpath")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Reporting_read_ini().get_generate_report_button_by_xpath()).click()
                        self.logger.info("clicked on generate_report_button_by_xpath")
                        time.sleep(web_driver.two_second)
                        self.logger.info("Clicked on generate report button...")
                        self.d.find_element(By.XPATH, Reporting_read_ini().
                                            get_view_and_edit_groups_button_by_xpath()).click()
                        self.logger.info("clicked on view_and_edit_groups_button_by_xpath")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH, Reporting_read_ini().
                                            get_clear_all_button_on_selected_group_by_xpath()).click()
                        self.logger.info("clicked on clear_all_button_on_selected_group_by_xpath")
                        self.status.append(True)
                        time.sleep(web_driver.one_second)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_379.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_379.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_EN_379_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_EN_379_exception.png")
            self.logger.error(f"TC_Reporting_EV_EN_379 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_day_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HD_380 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_day()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_abe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_abe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_380.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_380.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_380_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_380_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_380 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_day_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HD_381 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_day()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_pte_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_pte_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_381.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_381.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_381_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_381_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_381 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_day_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HD_382 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_day()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_soe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_soe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_382.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_382.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_382_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_382_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_382 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_day_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HD_383 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_day()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_vipe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_vipe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_383.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_383.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_383_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_383_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_383 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_day_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HD_384 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_day()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_fraude_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_fraude_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_384.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_384.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_384_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_384_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_384 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_day_with_date_range_from_json_file_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HD_385 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_day()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_abe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_abe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_385.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_385.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_385_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_385_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_385 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_day_with_date_range_from_json_file_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HD_386 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_day()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_pte_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_pte_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_386.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_386.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_386_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_386_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_386 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_day_with_date_range_from_json_file_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HD_387 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_day()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_soe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_soe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_387.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_387.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_387_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_387_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_387 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_day_with_date_range_from_json_file_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HD_388 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_day()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_vipe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_vipe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_388.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_388.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_388_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_388_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_388 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_day_with_date_range_from_json_file_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HD_389 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_day()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_fraude_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_fraude_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_389.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_389.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_389_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_389_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_389 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_individual_report_for_number_of_events_by_hour_of_day_with_date_range_from_json_file_and_with_groups_as_SOE_ABE_PTE_FRAUDE_VIPE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HD_390 started ************")
            self.load_reporting_module_for_admin()
            self.logger.info("executed load_reporting_module_for_admin")
            self.select_number_of_events_by_hour_of_day()
            self.logger.info("executed select_number_of_events_by_hour_of_day")
            self.get_age_range()
            self.logger.info("executed get_age_range")
            self.get_start_date()
            self.logger.info("executed get_start_date")
            self.get_end_date()
            self.logger.info("executed get_end_date")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.zones_list = [Reporting_read_ini().get_zones()]
            self.groups_list = [Reporting_read_ini().get_abe_enrollment_group(),
                                Reporting_read_ini().get_soe_enrollment_group(),
                                Reporting_read_ini().get_pte_enrollment_group(),
                                Reporting_read_ini().get_fraude_enrollment_group(),
                                Reporting_read_ini().get_vipe_enrollment_group()]
            for i in range(len(self.groups_list)):
                time.sleep(web_driver.one_second)
                self.d.find_element(By.XPATH, Reporting_read_ini().get_filter_group_list_textbox_by_xpath()).send_keys(
                    self.groups_list[i])
                group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                  get_group_items_list_below_filter_group_list_textbox())
                for items in group_list:
                    if items.text.upper() == self.groups_list[i].upper():
                        time.sleep(web_driver.one_second)
                        items.click()
                        self.logger.info(f"Selected group as: {self.groups_list[i]}")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
                        time.sleep(web_driver.one_second)
                        self.logger.info("clicked on save_group_selection_button_by_xpath())")
                        view_and_edit_zones_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                         get_view_and_edit_zones_button_by_xpath())
                        self.logger.info(f"view_and_edit_zones_button displayed: {view_and_edit_zones_button.is_displayed()}")
                        if view_and_edit_zones_button.is_displayed():
                            view_and_edit_zones_button.click()
                            self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_clear_all_button_on_selected_zone_by_xpath()).click()
                            self.logger.info("clicked on get_clear_all_button_on_selected_zone_by_xpath")
                        else:
                            pass
                        select_zone_filter_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                        get_select_zone_filter_button_by_xpath())
                        self.logger.info(f"select_zone_filter_button displayed: {select_zone_filter_button.is_displayed()}")
                        if select_zone_filter_button.is_displayed():
                            select_zone_filter_button.click()
                        else:
                            pass
                        for j in range(len(self.zones_list)):
                            time.sleep(web_driver.one_second)
                            self.d.find_element(By.XPATH, Reporting_read_ini().get_search_zone_textbox_by_xpath()). \
                                send_keys(self.zones_list[j])
                            zone_list = self.d.find_elements(
                                By.XPATH, Reporting_read_ini().get_zone_items_list_below_search_zone_textbox_by_xpath())
                            for Items in zone_list:
                                if Items.text.upper() == self.zones_list[j].upper():
                                    time.sleep(web_driver.one_second)
                                    Items.click()
                                    self.logger.info(f"Selected zone as: {self.zones_list[j]}")
                                    time.sleep(web_driver.one_second)
                                    self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_save_zone_selection_button_by_xpath()).click()
                                    self.logger.info("clicked on save_zone_selection_button_by_xpath")

                        self.explicit_wait(10, "XPATH", Reporting_read_ini().get_generate_report_button_by_xpath(), self.d).click()
                        self.logger.info("Clicked on Generate report button...")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Reporting_read_ini().get_view_and_edit_groups_button_by_xpath()).click()
                        self.logger.info("clicked on view_and_edit_groups_button_by_xpath")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH, Reporting_read_ini().
                                            get_clear_all_button_on_selected_group_by_xpath()).click()
                        self.logger.info("clicked on clear_all_button_on_selected_group_by_xpath")
                        self.status.append(True)
                        time.sleep(web_driver.one_second)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_390.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_390.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HD_390_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HD_390_exception.png")
            self.logger.error(f"TC_Reporting_EV_HD_390 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_day_of_week_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_DW_391 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_day_of_week()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_abe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_abe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_391.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_391.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_391_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_391_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_391 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_day_of_week_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_DW_392 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_day_of_week()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_pte_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_pte_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_392.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_392.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_392_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_392_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_392 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_day_of_week_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_DW_393 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_day_of_week()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_soe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_soe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_393.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_393.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_393_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_393_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_393 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_day_of_week_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_DW_394 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_day_of_week()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_vipe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_vipe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_394.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_394.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_394_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_394_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_394 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_day_of_week_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_DW_395 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_day_of_week()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_fraude_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_fraude_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_395.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_395.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_395_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_395_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_395 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_day_of_week_with_date_range_from_json_file_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_DW_396 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_day_of_week()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_abe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_abe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_396.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_396.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_396_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_396_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_396 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_day_of_week_with_date_range_from_json_file_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_DW_397 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_day_of_week()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_pte_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_pte_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_397.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_397.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_397_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_397_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_397 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_day_of_week_with_date_range_from_json_file_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_DW_398 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_day_of_week()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_soe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_soe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_398.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_398.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_398_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_398_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_398 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_day_of_week_with_date_range_from_json_file_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_DW_399 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_day_of_week()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_vipe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_vipe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_399.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_399.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_399_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_399_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_399 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_day_of_week_with_date_range_from_json_file_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_DW_400 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_day_of_week()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_fraude_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_fraude_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_400.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_400.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_400_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_400_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_400 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_individual_report_for_number_of_events_by_day_of_week_with_date_range_from_json_file_and_with_groups_as_SOE_ABE_PTE_FRAUDE_VIPE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_DW_401 started ************")
            self.load_reporting_module_for_admin()
            self.logger.info("executed load_reporting_module_for_admin")
            self.select_number_of_events_by_day_of_week()
            self.logger.info("executed select_number_of_events_by_day_of_week")
            self.get_age_range()
            self.logger.info("executed get_age_range")
            self.get_start_date()
            self.logger.info("executed get_start_date")
            self.get_end_date()
            self.logger.info("executed get_end_date")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.zones_list = [Reporting_read_ini().get_zones()]
            self.groups_list = [Reporting_read_ini().get_abe_enrollment_group(),
                                Reporting_read_ini().get_soe_enrollment_group(),
                                Reporting_read_ini().get_pte_enrollment_group(),
                                Reporting_read_ini().get_fraude_enrollment_group(),
                                Reporting_read_ini().get_vipe_enrollment_group()]
            for i in range(len(self.groups_list)):
                time.sleep(web_driver.one_second)
                self.d.find_element(By.XPATH, Reporting_read_ini().get_filter_group_list_textbox_by_xpath()).send_keys(
                    self.groups_list[i])
                group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                  get_group_items_list_below_filter_group_list_textbox())
                for items in group_list:
                    if items.text.upper() == self.groups_list[i].upper():
                        time.sleep(web_driver.one_second)
                        items.click()
                        self.logger.info(f"Selected group as: {self.groups_list[i]}")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
                        self.logger.info("clicked on save_group_selection_button_by_xpath")
                        time.sleep(web_driver.one_second)
                        view_and_edit_zones_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                         get_view_and_edit_zones_button_by_xpath())
                        if view_and_edit_zones_button.is_displayed():
                            view_and_edit_zones_button.click()
                            self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_clear_all_button_on_selected_zone_by_xpath()).click()
                            self.logger.info("clicked on get_clear_all_button_on_selected_zone_by_xpath")
                        else:
                            pass
                        select_zone_filter_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                        get_select_zone_filter_button_by_xpath())
                        if select_zone_filter_button.is_displayed():
                            select_zone_filter_button.click()
                        else:
                            pass
                        for j in range(len(self.zones_list)):
                            time.sleep(web_driver.one_second)
                            self.d.find_element(By.XPATH, Reporting_read_ini().get_search_zone_textbox_by_xpath()). \
                                send_keys(self.zones_list[j])
                            zone_list = self.d.find_elements(
                                By.XPATH, Reporting_read_ini().get_zone_items_list_below_search_zone_textbox_by_xpath())
                            for Items in zone_list:
                                if Items.text.upper() == self.zones_list[j].upper():
                                    time.sleep(web_driver.one_second)
                                    Items.click()
                                    self.logger.info(f"Selected zone as: {self.zones_list[j]}")
                                    time.sleep(web_driver.one_second)
                                    self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_save_zone_selection_button_by_xpath()).click()
                                    self.logger.info("clicked on get_save_zone_selection_button_by_xpath")

                        self.explicit_wait(10, "XPATH", Reporting_read_ini().get_generate_report_button_by_xpath(),
                                           self.d).click()
                        time.sleep(web_driver.one_second)
                        self.logger.info("Clicked on Generate report button...")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Reporting_read_ini().get_view_and_edit_groups_button_by_xpath()).click()
                        time.sleep(web_driver.one_second)
                        self.logger.info("clicked on get_view_and_edit_groups_button_by_xpath")
                        self.d.find_element(By.XPATH, Reporting_read_ini().
                                            get_clear_all_button_on_selected_group_by_xpath()).click()
                        self.logger.info("clicked on get_clear_all_button_on_selected_group_by_xpath")
                        self.status.append(True)
                        time.sleep(web_driver.one_second)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_401.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_401.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_DW_401_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_DW_401_exception.png")
            self.logger.error(f"TC_Reporting_EV_DW_401 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HW_402 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_week()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_abe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_abe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_402.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_402.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_402_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_402_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_402 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HW_403 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_week()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_pte_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_pte_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_403.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_403.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_403_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_403_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_403 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HW_404 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_week()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_soe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_soe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_404.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_404.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_404_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_404_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_404 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HW_405 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_week()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_vipe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_vipe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_405.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_405.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_405_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_405_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_405 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_week_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HW_406 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_week()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_fraude_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_fraude_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_406.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_406.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_406_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_406_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_406 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_week_with_date_range_from_json_file_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HW_407 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_week()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_abe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_abe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_407.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_407.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_407_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_407_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_407 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_week_with_date_range_from_json_file_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HW_408 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_week()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_pte_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_pte_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_408.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_408.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_408_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_408_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_408 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_week_with_date_range_from_json_file_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HW_409 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_week()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_soe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_soe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_409.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_409.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_409_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_409_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_409 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_week_with_date_range_from_json_file_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HW_410 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_week()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_vipe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_vipe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_410.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_410.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_410_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_410_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_410 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_hour_of_week_with_date_range_from_json_file_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HW_411 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_hour_of_week()
            self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_fraude_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_fraude_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select zone filter button...")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == Reporting_read_ini().get_zones():
                        items.click()
                        self.logger.info(f"Selected zone as: {Reporting_read_ini().get_zones()}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_411.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_411.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_411_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_411_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_411 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_individual_report_for_number_of_events_by_hour_of_week_with_date_range_from_json_file_and_with_groups_as_SOE_ABE_PTE_FRAUDE_VIPE_and_zone_selected_as_All_devices(self):
        try:
            self.logger.info("********* TC_Reporting_EV_HW_412 started ************")
            self.load_reporting_module_for_admin()
            self.logger.info("executed load_reporting_module_for_admin")
            self.select_number_of_events_by_hour_of_week()
            self.logger.info("executed select_number_of_events_by_hour_of_week")
            self.get_age_range()
            self.logger.info("executed get_age_range")
            self.get_start_date()
            self.logger.info("executed get_start_date")
            self.get_end_date()
            self.logger.info("executed get_end_date")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.zones_list = [Reporting_read_ini().get_zones()]
            self.groups_list = [Reporting_read_ini().get_abe_enrollment_group(),
                                Reporting_read_ini().get_soe_enrollment_group(),
                                Reporting_read_ini().get_pte_enrollment_group(),
                                Reporting_read_ini().get_fraude_enrollment_group(),
                                Reporting_read_ini().get_vipe_enrollment_group()]
            for i in range(len(self.groups_list)):
                time.sleep(web_driver.one_second)
                self.d.find_element(By.XPATH, Reporting_read_ini().get_filter_group_list_textbox_by_xpath()).send_keys(
                    self.groups_list[i])
                group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                  get_group_items_list_below_filter_group_list_textbox())
                for items in group_list:
                    if items.text.upper() == self.groups_list[i].upper():
                        time.sleep(web_driver.one_second)
                        items.click()
                        self.logger.info(f"Selected group as: {self.groups_list[i]}")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
                        self.logger.info("clicked on get_save_group_selection_button_by_xpath")
                        time.sleep(web_driver.one_second)
                        view_and_edit_zones_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                         get_view_and_edit_zones_button_by_xpath())
                        if view_and_edit_zones_button.is_displayed():
                            view_and_edit_zones_button.click()
                            self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_clear_all_button_on_selected_zone_by_xpath()).click()
                            self.logger.info("clicked on get_clear_all_button_on_selected_zone_by_xpath")
                        else:
                            pass
                        select_zone_filter_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                        get_select_zone_filter_button_by_xpath())
                        if select_zone_filter_button.is_displayed():
                            select_zone_filter_button.click()
                        else:
                            pass
                        for j in range(len(self.zones_list)):
                            time.sleep(web_driver.one_second)
                            self.d.find_element(By.XPATH, Reporting_read_ini().get_search_zone_textbox_by_xpath()). \
                                send_keys(self.zones_list[j])
                            zone_list = self.d.find_elements(
                                By.XPATH, Reporting_read_ini().get_zone_items_list_below_search_zone_textbox_by_xpath())
                            for Items in zone_list:
                                if Items.text.upper() == self.zones_list[j].upper():
                                    time.sleep(web_driver.one_second)
                                    Items.click()
                                    self.logger.info(f"Selected zone as: {self.zones_list[j]}")
                                    time.sleep(web_driver.one_second)
                                    self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_save_zone_selection_button_by_xpath()).click()
                                    self.logger.info("clicked on get_save_zone_selection_button_by_xpath")

                        self.explicit_wait(10, "XPATH", Reporting_read_ini().get_generate_report_button_by_xpath(),
                                           self.d).click()
                        self.logger.info("clicked on get_generate_report_button_by_xpath")

                        time.sleep(web_driver.two_second)
                        self.logger.info("Clicked on Generate report button...")
                        self.d.find_element(By.XPATH,
                                            Reporting_read_ini().get_view_and_edit_groups_button_by_xpath()).click()
                        time.sleep(web_driver.one_second)
                        self.logger.info("clicked on get_generate_report_button_by_xpath")
                        self.d.find_element(By.XPATH, Reporting_read_ini().
                                            get_clear_all_button_on_selected_group_by_xpath()).click()
                        self.status.append(True)
                        time.sleep(web_driver.one_second)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_412.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_412.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_HW_412_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_HW_412_exception.png")
            self.logger.error(f"TC_Reporting_EV_HW_412 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_zone_with_default_dates_1_month_and_with_group_selected_as_SOE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_ZN_413 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_zone()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_soe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_soe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_413.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_413.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_413_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_413_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_413 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_zone_with_default_dates_1_month_and_with_group_selected_as_ABE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_ZN_414 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_zone()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_abe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_abe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_414.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_414.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_414_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_414_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_414 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_zone_with_default_dates_1_month_and_with_group_selected_as_PTE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_ZN_415 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_zone()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_pte_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_pte_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_415.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_415.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_415_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_415_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_415 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_zone_with_default_dates_1_month_and_with_group_selected_as_FRAUDE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_ZN_416 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_zone()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_fraude_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_fraude_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_416.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_416.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_416_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_416_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_416 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_zone_with_default_dates_1_month_and_with_group_selected_as_VIPE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_ZN_417 started ************")
            self.load_reporting_module_for_admin()
            self.select_number_of_events_by_zone()
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_vipe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_vipe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_417.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_417.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_417_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_417_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_417 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_zone_with_date_range_from_json_file_with_group_selected_as_SOE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_ZN_418 started ************")
            self.load_reporting_module_for_admin()
            time.sleep(web_driver.one_second)
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.get_start_date()
            time.sleep(web_driver.one_second)
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_soe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_soe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_418.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_418.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_418_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_418_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_418 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_zone_with_date_range_from_json_file_with_group_selected_as_ABE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_ZN_419 started ************")
            self.load_reporting_module_for_admin()
            time.sleep(web_driver.one_second)
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.get_start_date()
            time.sleep(web_driver.one_second)
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_abe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_abe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_419.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_419.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_419_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_419_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_419 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_zone_with_date_range_from_json_file_with_group_selected_as_PTE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_ZN_420 started ************")
            self.load_reporting_module_for_admin()
            time.sleep(web_driver.one_second)
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.get_start_date()
            time.sleep(web_driver.one_second)
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_pte_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_pte_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_420.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_420.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_420_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_420_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_420 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_zone_with_date_range_from_json_file_with_group_selected_as_FRAUDE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_ZN_421 started ************")
            self.load_reporting_module_for_admin()
            time.sleep(web_driver.one_second)
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.get_start_date()
            time.sleep(web_driver.one_second)
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_fraude_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_fraude_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_421.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_421.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_421_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_421_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_421 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_report_for_number_of_events_by_zone_with_date_range_from_json_file_with_group_selected_as_VIPE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_ZN_422 started ************")
            self.load_reporting_module_for_admin()
            time.sleep(web_driver.one_second)
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.get_start_date()
            time.sleep(web_driver.one_second)
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on Select group filter button...")
            time.sleep(web_driver.one_second)
            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            for items in group_list:
                if items.text == Reporting_read_ini().get_vipe_enrollment_group():
                    items.click()
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_vipe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on generate report button...")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            if new_reporting_panel.is_displayed():
                self.logger.info(f"Reporting panel heading: {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_422.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_422.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_422_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_422_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_422 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()

    def verify_individual_report_for_number_of_events_by_zone_with_date_range_from_json_file_with_group_selected_as_SOE_ABE_PTE_FRAUDE_and_VIPE(self):
        try:
            self.logger.info("********* TC_Reporting_EV_ZN_423 started ************")
            self.load_reporting_module_for_admin()
            time.sleep(web_driver.one_second)
            self.logger.info("executed load_reporting_module_for_admin")
            self.select_number_of_events_by_zone()
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_number_of_events_by_zone")
            self.get_age_range()
            time.sleep(web_driver.one_second)
            self.logger.info("executed get_age_range")
            self.get_start_date()
            time.sleep(web_driver.one_second)
            self.logger.info("executed get_start_date")
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.logger.info("executed get_end_date")
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.groups_list = [Reporting_read_ini().get_abe_enrollment_group(),
                                Reporting_read_ini().get_soe_enrollment_group(),
                                Reporting_read_ini().get_pte_enrollment_group(),
                                Reporting_read_ini().get_fraude_enrollment_group(),
                                Reporting_read_ini().get_vipe_enrollment_group()]
            for i in range(len(self.groups_list)):
                time.sleep(web_driver.one_second)
                self.d.find_element(By.XPATH, Reporting_read_ini().get_filter_group_list_textbox_by_xpath()). \
                    send_keys(self.groups_list[i])
                group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                  get_group_items_list_below_filter_group_list_textbox())
                for items in group_list:

                    if items.text.upper() == self.groups_list[i].upper():
                        time.sleep(web_driver.one_second)
                        items.click()
                        self.logger.info(f"Selected group as: {self.groups_list[i]}")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
                        self.logger.info("Clicked on get_save_group_selection_button_by_xpath...")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Reporting_read_ini().get_generate_report_button_by_xpath()).click()
                        self.logger.info("Clicked on get_generate_report_button_by_xpath...")
                        time.sleep(web_driver.one_second)
                        self.logger.info("Clicked on generate report button...")
                        self.d.find_element(By.XPATH, Reporting_read_ini().
                                            get_view_and_edit_groups_button_by_xpath()).click()
                        self.logger.info("Clicked on get_view_and_edit_groups_button_by_xpath...")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH, Reporting_read_ini().
                                            get_clear_all_button_on_selected_group_by_xpath()).click()
                        self.logger.info("Clicked on get_clear_all_button_on_selected_group_by_xpath...")
                        self.status.append(True)
                        time.sleep(web_driver.one_second)

            time.sleep(web_driver.one_second)
            
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_423.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_423.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EV_ZN_423_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EV_ZN_423_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_423 got exception as: {ex}")
        finally:
            Reporting_pom().close_reporting_module()
