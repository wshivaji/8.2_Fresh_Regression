from pathlib import Path
import time
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login, logout
from All_Config_Packages._18_Reporting_Module_Config_Files.Reporting_Read_INI import Reporting_read_ini
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import Portal_Menu_Module_read_ini


class Reporting_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []
    
    def __init__(self):
        self.end_datetime = self.end_time = self.end_date = self.end_date_and_time = self.start_datetime = \
            self.start_age = self.age_bucket = None
        self.start_time = self.start_date = self.start_date_and_time = self.groups = self.zones = self.end_age = None
        self.zones = Reporting_read_ini().get_all_zones().split(',')
        
        self.age_range_zones_groups_xlsx = \
            (f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\18_Reporting_Module\\Data_From_Excel"
             f"\\age_range_zones_groups_xlsx.xlsx")
        self.custom_dates_json = \
            (f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\18_Reporting_Module\\Data_From_JSON"
             f"\\custom_dates_json.json")

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

    def load_reporting_module_for_admin(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            reporting_module = self.d.find_element(By.XPATH, Reporting_read_ini().get_reporting_module_by_xpath())
            if reporting_module.is_displayed():
                reporting_module.click()
                time.sleep(web_driver.one_second)
            else:
                pass

        except Exception as ex:
            self.logger.error(ex)

    def load_reporting_module(self):
        try:
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

    def close_reporting_module(self):
        try:
            cloud_menu_button = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath())
            cloud_menu_button.click()
            time.sleep(web_driver.one_second)
            close_all_panels_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_close_all_panels_button_on_dashboard_by_xpath())
            if close_all_panels_button.is_displayed():
                close_all_panels_button.click()
            else:
                pass
        except Exception as ex:
            print(ex)

    def get_age_range(self):
        try:
            df_age_range = pd.read_excel(self.age_range_zones_groups_xlsx, sheet_name='age_range',
                                         names=['Start Age', 'End Age', 'Age Bucket'])
            df_zones = pd.read_excel(self.age_range_zones_groups_xlsx, sheet_name='zones', names=['Zones'])
            df_groups = pd.read_excel(self.age_range_zones_groups_xlsx, sheet_name='groups', names=['Groups'])
            self.start_age = [x for x in df_age_range['Start Age']]
            self.end_age = [y for y in df_age_range['End Age']]
            self.age_bucket = [z for z in df_age_range['Age Bucket']]
            self.zones = Reporting_read_ini().get_all_zones().split(',')
            self.groups = [x for x in df_groups['Groups']]
            # print(f"start age: {self.start_age}" f"length: {len(self.start_age)}")
            # print(f"df age range: {df_age_range}")
            # print(f"df zones: {df_zones}")
            # print(f"df groups: {df_groups}")
        except Exception as ex:
            self.logger.error(ex)

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
    
    def verify_reporting_is_visible_in_dashboard_items_click_on_reporting_and_verify_it_is_navigating_to_reporting_panel(
            self):
        try:
            self.logger.info("*********** TC_Reporting_002 started **********")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            dashboard_items = self.d.find_elements(By.XPATH, Reporting_read_ini().get_dashboard_menu_items_by_xpath())
            for items in dashboard_items:
                if items.text == Reporting_read_ini().get_reporting_module():
                    self.status.append(True)
                    self.logger.info("Reporting is visible on dashboard..")
                    break
            else:
                self.logger.error("Reporting is not visible.!!!")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_reporting_module_by_xpath()).click()
            self.logger.info("Clicked on Reporting module...")
            time.sleep(web_driver.one_second)
            actual_panel_heading = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                       get_reporting_panel_heading_by_xpath()).text
            if actual_panel_heading == Reporting_read_ini().get_reporting_module():
                self.logger.info("Reporting panel is visible..")
                self.status.append(True)
            else:
                self.logger.error("Reporting panel is not visible.!!!")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_002.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_002.png")
                return False
            else:
                return True

            logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_002_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_002_exception.png")
            self.logger.error(f"TC_Reporting_002 got exception as: {ex}")

    def verify_Reporting_module_is_not_visible_in_dashboard_menu_without_having_permission_in_local(self):
        try:
            self.logger.info("*********** TC_Reporting_424 started **********")
            login().login_to_cloud_if_not_done(self.d)
            dashboard_items = self.d.find_elements(By.XPATH, Reporting_read_ini().get_dashboard_menu_items_by_xpath())
            for items in dashboard_items:
                if items.text == Reporting_read_ini().get_reporting_module():
                    self.logger.info("Reporting is visible. User has permission!!!!")
                    self.status.append(False)
                    break
            else:
                self.logger.info("Reporting is not visible. Use is not permitted!!!")
                self.status.append(True)

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_logout_button_on_portal_by_xpath()).click()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_424.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_424.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_424_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_424_exception.png")
            self.logger.error(f"TC_Reporting_424 got exception as: {ex}")

    def verify_reporting_panel_heading_is_visible_close_panel_button_on_panel_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_003 started **********")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_reporting_module_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_panel_heading = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                       get_reporting_panel_heading_by_xpath()).text
            if actual_panel_heading == Reporting_read_ini().get_reporting_module():
                self.logger.info("Reporting panel heading is visible..")
                self.status.append(True)
            else:
                self.logger.error("Reporting panel heading is not visible..")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_close_panel_button_by_xpath()).is_displayed():
                self.logger.info("Close panel button is visible.!!!")
                self.status.append(True)
            else:
                self.logger.error("Close panel button is not visible.!!!")
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_close_panel_button_by_xpath()).is_enabled():
                self.logger.info("Close panel button is clickable.!!!")
                self.status.append(True)
            else:
                self.logger.error("Close panel button is not clickable.!!!")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_003.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_003.png")
                return False
            else:
                return True

            logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_003_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_003_exception.png")
            self.logger.error(f"TC_Reporting_003 got exception as: {ex}")

    def verify_report_selection_text_chart_icon_select_report_criteria_text_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_004 started **********")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_reporting_module_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_report_selection_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                               get_report_selection_text_on_heading_by_xpath()).text
            self.logger.info(f"actual text: {actual_report_selection_text}")
            self.logger.info(f"expected text: {Reporting_read_ini().get_expected_report_selection_text()}")
            if actual_report_selection_text == Reporting_read_ini().get_expected_report_selection_text():
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_chart_icon_beside_report_selection_text_by_xpath()
                                   ).is_displayed():
                self.logger.info("Chart icon beside Report selection text is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_select_report_criteria_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                     get_select_report_criteria_text_by_xpath()).text
            self.logger.info(f"actual text: {actual_select_report_criteria_text}")
            self.logger.info(f"expected text: {Reporting_read_ini().get_expected_select_report_criteria_text()}")
            if actual_select_report_criteria_text == Reporting_read_ini().get_expected_select_report_criteria_text():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_004.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_004.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_004_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_004_exception.png")
            self.logger.error(f"TC_Reporting_004 got exception as: {ex}")

    def verify_report_the_text_and_dropdown_beside_it_is_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_005 started **********")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_reporting_module_by_xpath()).click()
            time.sleep(web_driver.one_second)
            actual_report_the_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                         get_report_the_text_by_xpath()).text
            self.logger.info(f"actual text: {actual_report_the_text}")
            self.logger.info(f"expected text: {Reporting_read_ini().get_expected_report_the_text()}")
            if actual_report_the_text == Reporting_read_ini().get_expected_report_the_text():
                self.status.append(True)
            else:
                self.status.append(False)
            report_field1_dropdown = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                         get_report_field1_dropdown_by_xpath())
            if report_field1_dropdown.is_displayed():
                self.logger.info("Report field1 dropdown is visible !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            if report_field1_dropdown.is_enabled():
                self.logger.info("Report field1 dropdown is clickable !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            report_field1_dropdown.click()
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_005.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_005.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_005_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_005_exception.png")
            self.logger.error(f"TC_Reporting_005 got exception as: {ex}")

    def click_on_report_the_dropdown_and_verify_options_inside_dropdown_are_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_006 started **********")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_reporting_module_by_xpath()).click()
            time.sleep(web_driver.two_second)
            report_field1_dropdown = self.d.find_element(By.XPATH,
                                                         Reporting_read_ini().get_report_field1_dropdown_by_xpath())
            report_field1_dropdown.click()
            time.sleep(web_driver.one_second)
            x = Reporting_read_ini().get_expected_report_field1_list_items()
            expected_report_field1_option_list = x.split(',')
            report_field1_dropdown_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                                get_report_field1_dropdown_items_by_xpath())
            time.sleep(web_driver.one_second)
            if len(report_field1_dropdown_items) > 0:
                self.logger.info(f"'Report the' dropdown contains options. Length: {len(report_field1_dropdown_items)}")
                for x in range(len(report_field1_dropdown_items)):
                    option = report_field1_dropdown_items[x]
                    if option.is_displayed():
                        self.status.append(True)
                    else:
                        self.status.append(False)
                    if option.is_enabled():
                        self.status.append(True)
                    else:
                        self.status.append(False)
                    if option.text == expected_report_field1_option_list[x]:
                        self.status.append(True)
                    else:
                        self.status.append(False)

            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_006.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_006.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_006_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_006_exception.png")
            self.logger.error(f"TC_Reporting_006 got exception as: {ex}")

    def click_on_dropdown_followed_by_report_the_and_select_number_of_events_option_verify_new_dropdown_is_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_007 started **********")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_reporting_module_by_xpath()).click()
            time.sleep(web_driver.three_second)
            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            field1.select_by_visible_text('number of probable match events')
            print(field1.select_by_visible_text('number of probable match events'))
            time.sleep(web_driver.one_second)
            self.logger.info("Number of events selected from dropdown...")
            field2_dropdown = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                  get_report_field2_dropdown_for_events_by_xpath())
            time.sleep(web_driver.one_second)
            if field2_dropdown.is_displayed():
                self.logger.info("Second dropdown is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if field2_dropdown.is_enabled():
                self.logger.info("Second dropdown is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            field2_dropdown.click()
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_007.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_007.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_007_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_007_exception.png")
            self.logger.error(f"TC_Reporting_007 got exception as: {ex}")

    def verify_by_text_is_visible_click_on_by_dropdown_and_verify_options_inside_dropdown_are_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_008 started **********")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_reporting_module_by_xpath()).click()
            time.sleep(web_driver.two_second)

            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            field1.select_by_visible_text('number of probable match events')
            time.sleep(web_driver.one_second)
            actual_by_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_by_text_xpath()).text
            self.logger.info(f"actual text: {actual_by_text}")
            expected_by_text = Reporting_read_ini().get_expected_by_text()
            self.logger.info(f"expected text: {expected_by_text}")
            if actual_by_text == expected_by_text:
                self.status.append(True)
            else:
                self.status.append(False)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field2_dropdown_for_events_by_xpath()).click()
            time.sleep(web_driver.one_second)

            y = Reporting_read_ini().get_expected_report_field2_for_events_list_items()
            expected_report_field2_options_for_events = y.split(',')

            report_field2_for_events_dropdown_items = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_report_field2_dropdown_items_for_events_by_xpath())
            time.sleep(web_driver.one_second)
            if len(report_field2_for_events_dropdown_items) > 0:
                time.sleep(web_driver.one_second)
                self.logger.info(f"'by' dropdown for events contains options. Length: "
                                 f"{len(report_field2_for_events_dropdown_items)}")
                for y in range(len(report_field2_for_events_dropdown_items)):
                    option = report_field2_for_events_dropdown_items[y]
                    if option.is_displayed():
                        self.status.append(True)
                    else:
                        self.status.append(False)
                    if option.is_enabled():
                        self.status.append(True)
                    else:
                        self.status.append(False)
                    if option.text == expected_report_field2_options_for_events[y]:
                        self.status.append(True)
                    else:
                        self.status.append(False)

            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_008.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_008.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_008_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_008_exception.png")
            self.logger.error(f"TC_Reporting_008 got exception as: {ex}")

    def Click_on_close_panel_button_and_verify_Reporting_panel_is_closing(self):
        try:
            self.logger.info("*********** TC_Reporting_009 started **********")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_reporting_module_by_xpath()).click()
            time.sleep(web_driver.one_second)
            reporting_module = self.d.find_element(By.XPATH, Reporting_read_ini().get_reporting_module_by_xpath())
            if reporting_module.is_displayed():
                self.status.append(False)
            else:
                self.logger.info("Reporting panel opened......")
                self.status.append(True)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_close_panel_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            if reporting_module.is_displayed():
                self.logger.info("Reporting panel closed......")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_009.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_009.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_009_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_009_exception.png")
            self.logger.error(f"TC_Reporting_009 got exception as: {ex}")

    def select_number_of_visitors_by_hour_of_day(self):
        try:
            time.sleep(web_driver.one_second)
            field1 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath())
            field2 = self.d.find_element(By.XPATH, Reporting_read_ini().get_field2_dropdown_for_visitors_by_xpath())
            if field2.is_displayed():
                pass
            else:
                field1_dropdown = Select(field1)
                time.sleep(web_driver.one_second)
                field1_dropdown.select_by_visible_text('number of visitors')
                field2_dropdown = Select(field2)
                time.sleep(web_driver.one_second)
                field2_dropdown.select_by_visible_text('hour of day')
                time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def for_number_of_visitors_by_hour_of_day_verify_number_of_visitors_from_report_field1_and_hour_of_day_from_report_field2_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_018 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            time.sleep(web_driver.one_second)
            field1.select_by_visible_text('number of visitors')
            value1 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()). \
                get_attribute('value')
            self.logger.info(f"Value1: {value1}")
            if Reporting_read_ini().get_expected_second_text_from_field1() in value1:
                self.logger.info("Selected 'number of visitors' from report field1 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            field2 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_field2_dropdown_for_visitors_by_xpath()))
            field2.select_by_visible_text('hour of day')

            value2 = self.d.find_element(By.XPATH, Reporting_read_ini().get_field2_dropdown_for_visitors_by_xpath()). \
                get_attribute('value')
            self.logger.info(f"Value2: {value2}")
            if Reporting_read_ini().get_expected_first_text_from_field2() in value2:
                self.logger.info("Selected 'hour of day' from report field2 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_018.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_018.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_018_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_018_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_018 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_date_and_time_range_text_to_text_and_horizontal_text_line_below_calender_box_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_019 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_day()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_019.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_019.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_019_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_019_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_019 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_020 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_day()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_020.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_020.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_020_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_020_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_020 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_021 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_day()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_021.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_021.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_021_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_021_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_021 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_022 started **********")
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_day()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_022.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_022.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_022_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_022_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_022 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_023 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_day()
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
            self.logger.info(f"End calender disable status after click: {end_date_calender_box.get_attribute('disabled')}")
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_023.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_023.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_023_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_023_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_023 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox(self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_024 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_day()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_024.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_024.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_024_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_024_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_024 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_optional_filters_age_range_to_number_of_ages_to_group_totals_by_texts_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_025 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_day()
            actual_optional_filters_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                               get_optional_filters_text_by_xpath()).text
            self.logger.info(f"actual optional filters text: {actual_optional_filters_text}")
            expected_optional_filters_text = Reporting_read_ini().get_expected_optional_filters_text()
            self.logger.info(f"expected optional filters text: {expected_optional_filters_text}")
            if actual_optional_filters_text == expected_optional_filters_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_age_range_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_age_range_text_by_xpath()).text
            self.logger.info(f"Age range text: {actual_age_range_text}")
            expected_age_range_text = Reporting_read_ini().get_expected_age_range_text()
            self.logger.info(f"expected Age range text: {expected_age_range_text}")
            if actual_age_range_text == expected_age_range_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_to_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_to_text_by_xpath()).text
            self.logger.info(f"Actual 'to' text: {actual_to_text}")
            expected_to_text = Reporting_read_ini().get_expected_to_text()
            self.logger.info(f"expected 'to' text: {expected_to_text}")
            if actual_to_text == expected_to_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_number_of_ages_to_group_total_by_text = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_number_of_ages_to_group_totals_by_text_by_xpath()).text
            self.logger.info(f"actual nuber of ages to group totals by text: "
                             f"{actual_number_of_ages_to_group_total_by_text}")
            expected_number_of_ages_to_group_totals_by_text = Reporting_read_ini(). \
                get_expected_number_of_ages_to_group_totals_by_text()
            self.logger.info(f"expected nuber of ages to group totals by text: "
                             f"{expected_number_of_ages_to_group_totals_by_text}")
            if actual_number_of_ages_to_group_total_by_text == expected_number_of_ages_to_group_totals_by_text:
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_025.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_025.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_025_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_025_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_025 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_start_age_dropdown_end_age_dropdown_and_number_of_ages_to_group_totals_by_dropdown_are_visible_and_clickable_click_on_dropdowns(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_026 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_day()
            start_age_dropdown = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_age_dropdown_by_xpath())
            end_age_dropdown = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_age_dropdown_by_xpath())
            number_age_group_totals_dropdown = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_number_of_ages_to_group_totals_by_dropdown_by_xpath())
            if start_age_dropdown.is_displayed():
                self.logger.info("Start age dropdown is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if start_age_dropdown.is_enabled():
                self.logger.info("Start age dropdown is clickable...")
                start_age_dropdown.click()
                time.sleep(web_driver.one_second)
                start_age_dropdown.click()
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            start_age_dropdown_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                            get_start_age_dropdown_items_by_xpath())
            if len(start_age_dropdown_items) > 0:
                self.logger.info("Start age dropdown items are visible...")
                for x in range(len(start_age_dropdown_items) - 1):
                    options = start_age_dropdown_items[x + 1]
                    if int(options.text) == x + 1:
                        self.status.append(True)
                    else:
                        self.status.append(False)

            time.sleep(web_driver.one_second)
            if end_age_dropdown.is_displayed():
                self.logger.info("End age dropdown is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if end_age_dropdown.is_enabled():
                self.logger.info("End age dropdown is clickable...")
                end_age_dropdown.click()
                time.sleep(web_driver.one_second)
                end_age_dropdown.click()
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            end_age_dropdown_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                          get_end_age_dropdown_items_by_xpath())
            if len(end_age_dropdown_items) > 0:
                self.logger.info("End age dropdown items are visible...")
                for y in range(len(end_age_dropdown_items) - 1):
                    options = end_age_dropdown_items[y + 1]
                    if int(options.text) == y + 1:
                        self.status.append(True)
                    else:
                        self.status.append(False)

            time.sleep(web_driver.one_second)
            if number_age_group_totals_dropdown.is_displayed():
                self.logger.info("'Number age group totals by' dropdown is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if number_age_group_totals_dropdown.is_enabled():
                self.logger.info("'Number age group totals by' dropdown is clickable...")
                number_age_group_totals_dropdown.click()
                time.sleep(web_driver.one_second)
                number_age_group_totals_dropdown.click()
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            age_bucket_dropdown_items = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_number_of_ages_to_group_totals_by_dropdown_items())

            if len(age_bucket_dropdown_items) > 0:
                self.logger.info("'Number of age to group totals by' dropdown items are visible...")
                for z in range(len(age_bucket_dropdown_items) - 1):
                    options = age_bucket_dropdown_items[z + 1]
                    if int(options.text) == z + 2:
                        self.status.append(True)
                    else:
                        self.status.append(False)

            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"count: {len(self.status)}    \nstatus: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_026.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_026.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_026_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_026_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_026 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_gender_and_male_texts_are_visible_male_checkbox_is_visible_and_clickable_and_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_027 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_day()
            actual_gender_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_gender_text_by_xpath()).text
            self.logger.info(f"actual gender text: {actual_gender_text}")
            expected_gender_text = Reporting_read_ini().get_expected_gender_text()
            self.logger.info(f"expected text: {expected_gender_text}")
            if actual_gender_text == expected_gender_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_male_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_text_by_xpath()).text
            self.logger.info(f"actual male text: {actual_male_text}")
            expected_male_text = Reporting_read_ini().get_expected_male_text()
            self.logger.info(f"expected text: {expected_male_text}")
            if actual_male_text == expected_male_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_displayed():
                self.logger.info("Male checkbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if male_checkbox.is_enabled():
                self.logger.info("Male checkbox is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if male_checkbox.is_selected():
                self.logger.info("Male checkbox is selected by default !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_027.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_027.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_027_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_027_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_027 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_female_text_is_visible_female_checkbox_is_visible_and_clickable_and_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_028 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_day()
            actual_female_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_text_by_xpath()).text
            self.logger.info(f"actual female text: {actual_female_text}")
            expected_female_text = Reporting_read_ini().get_expected_female_text()
            self.logger.info(f"expected text: {expected_female_text}")
            if actual_female_text == expected_female_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_displayed():
                self.logger.info("Female checkbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if female_checkbox.is_enabled():
                self.logger.info("Female checkbox is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if female_checkbox.is_selected():
                self.logger.info("Female checkbox is selected by default !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_028.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_028.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_028_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_028_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_028 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_unknown_text_is_visible_unknown_gender_checkbox_is_visible_and_clickable_and_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_029 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_day()
            actual_unknown_gender_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                             get_unknown_gender_text_by_xpath()).text
            self.logger.info(f"actual unknown gender text: {actual_unknown_gender_text}")
            expected_unknown_gender_text = Reporting_read_ini().get_expected_unknown_gender_text()
            self.logger.info(f"expected unknown gender text: {expected_unknown_gender_text}")
            if actual_unknown_gender_text == expected_unknown_gender_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_displayed():
                self.logger.info("Unknown gender checkbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if unknown_gender_checkbox.is_enabled():
                self.logger.info("Unknown gender checkbox is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if unknown_gender_checkbox.is_selected():
                self.logger.info("Unknown gender checkbox is selected by default !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_029.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_029.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_029_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_029_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_029 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_select_zone_filter_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible_text_on_right_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_030 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_day()
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
            actual_text_beside_select_zone_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_text_beside_select_zone_filter_button_by_xpath()).text
            self.logger.info(f"actual text beside select zone button: {actual_text_beside_select_zone_button}")
            expected_text_beside_select_zone_button = Reporting_read_ini(). \
                get_expected_text_beside_select_zone_filter_button()
            self.logger.info(f"expected text beside select zone button: {expected_text_beside_select_zone_button}")
            if actual_text_beside_select_zone_button == expected_text_beside_select_zone_button:
                self.logger.info("text beside select zone filter button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)

            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_030.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_030.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_030_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_030_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_030 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_generate_report_button_is_visible_and_clickable_generate_report_text_and_chart_icon_both_are_visible_on_button(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_031 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_day()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_031.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_031.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_031_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_031_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_031 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_in_select_zone_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_032 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_day()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_032.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_032.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_032_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_032_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_032 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_search_zones_textbox_is_visible_and_clickable_label_on_it_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_033 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_day()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_033.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_033.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_033_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_033_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_033 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_zone_list_below_search_zones_textbox_is_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_034 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_day()
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
            WebDriverWait(self.d, 30).until(EC.presence_of_element_located((By.XPATH, Reporting_read_ini().
                                                                            get_zone_item_list_from_zone_panel_by_xpath())))
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_034.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_034.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_034_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_034_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_034 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_select_all_button_is_visible_and_clickable_and_text_on_it_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_035 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_day()
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
                self.logger.info("Select all button is enabled !!")
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_035.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_035.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_035_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_035_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_035 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_selected_zone_list_title_and_default_text_below_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_036 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_day()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_036.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_036.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_036_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_036_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_036 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_close_zone_menu_button_is_visible_and_clickable_and_text_on_it_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_037 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_day()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_037.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_037.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_037_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_037_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_037 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_click_on_select_all_button_and_verify_all_selected_zones_are_visible_in_selected_zone_list(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_038 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_day()
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
            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_zone_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_038.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_038.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_038_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_038_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_038 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_click_on_select_all_button_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_039 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_day()
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
            clear_all_button.click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_039.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_039.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_039_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_039_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_039 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_click_on_select_all_button_and_verify_save_zone_selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_040 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_day()
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
            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_zone_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_040.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_040.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_040_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_040_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_040 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_select_one_zone_from_zone_list_and_verify_selected_zone_is_visible_in_selected_zone_list_verify_save_zone_selection_button_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_041 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_day()
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
            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_zone_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_041.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_041.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_041_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_041_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_041 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_click_on_save_zone_selection_button_with_at_least_one_zone_selected_and_verify_View_and_edit_zones_button_is_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_042 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_day()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_042.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_042.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_042_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_042_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_042 got exception as: {ex}")

    def for_number_of_visitors_by_hour_of_day_verify_text_and_numeric_value_of_number_of_selected_zones_on_view_and_edit_zones_button_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_043 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_day()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_043.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_043.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_043_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_043_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_043 got exception as: {ex}")

    def select_age_range_from_dropdowns(self):
        try:
            self.get_age_range()
            start_age_dropdown = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_age_dropdown_by_xpath())
            start_age_dropdown.click()
            time.sleep(web_driver.one_second)
            start_age_dropdown_items = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().get_start_age_dropdown_items_by_xpath())
            for i in range(len(self.start_age)):
                for items in start_age_dropdown_items:
                    if str(items.text) == str(self.start_age[i]):
                        items.click()
                        self.logger.info(f"Selected start age as: {str(self.start_age[i])}")
                        self.status.append(True)
                        break
            time.sleep(web_driver.one_second)
            end_age_dropdown = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_age_dropdown_by_xpath())
            end_age_dropdown.click()
            time.sleep(web_driver.one_second)
            end_age_dropdown_items = self.d.find_elements(By.XPATH,
                                                          Reporting_read_ini().get_end_age_dropdown_items_by_xpath())
            for i in range(len(self.end_age)):
                for items in end_age_dropdown_items:
                    if str(items.text) == str(self.end_age[i]):
                        items.click()
                        self.logger.info(f"Selected end age as: {str(self.end_age[i])}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            age_bucket_dropdown = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_number_of_ages_to_group_totals_by_dropdown_by_xpath())
            age_bucket_dropdown.click()
            time.sleep(web_driver.one_second)
            age_bucket_dropdown_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                             get_number_of_ages_to_group_totals_by_dropdown_items())
            for i in range(len(self.age_bucket)):
                for items in age_bucket_dropdown_items:
                    if str(items.text) == str(self.age_bucket[i]):
                        items.click()
                        self.logger.info(f"Selected number of ages to group totals by as: {str(self.age_bucket[i])}")
                        self.status.append(True)
                break
        except Exception as ex:
            self.logger.error(ex)

    def verify_report_for_number_of_visitors_by_hour_of_day_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_044 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_day()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                self.logger.info("Male checkbox is selected...")
                pass
            else:
                male_checkbox.click()
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_044.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_044.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_044_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_044_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_044 got exception as: {ex}")

    def verify_report_for_number_of_visitors_by_hour_of_day_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_045 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_day()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                self.logger.info("Female checkbox is selected...")
                pass
            else:
                female_checkbox.click()
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_045.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_045.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_045_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_045_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_045 got exception as: {ex}")

    def verify_report_for_number_of_visitors_by_hour_of_day_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_046 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_day()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                self.logger.info("Unknown gender checkbox is selected...")
                pass
            else:
                unknown_gender_checkbox.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_046.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_046.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_046_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_046_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_046 got exception as: {ex}")

    def verify_report_for_number_of_visitors_by_hour_of_day_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_047 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_day()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            self.logger.info("Selected all genders by default...")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_047.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_047.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_047_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_047_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_047 got exception as: {ex}")

    def verify_report_for_number_of_visitors_by_hour_of_day_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_204 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_day()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                self.logger.info("Male checkbox is selected...")
                pass
            else:
                male_checkbox.click()
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_204.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_204.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_204_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_204_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_204 got exception as: {ex}")

    def verify_report_for_number_of_visitors_by_hour_of_day_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_205 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_day()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                self.logger.info("Female checkbox is selected...")
                pass
            else:
                female_checkbox.click()
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_205.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_205.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_205_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_205_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_205 got exception as: {ex}")

    def verify_report_for_number_of_visitors_by_hour_of_day_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_206 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_day()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                self.logger.info("Unknown gender checkbox is selected...")
                pass
            else:
                unknown_gender_checkbox.click()

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_206.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_206.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_206_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_206_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_206 got exception as: {ex}")

    def verify_report_for_number_of_visitors_by_hour_of_day_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HD_207 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_day()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            self.logger.info("Selected all genders by default...")
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_207.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_207.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HD_207_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HD_207_exception.png")
            self.logger.error(f"TC_Reporting_VS_HD_207 got exception as: {ex}")

    def select_number_of_visitors_by_day_of_week(self):
        try:
            time.sleep(web_driver.one_second)
            field1 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath())
            field2 = self.d.find_element(By.XPATH, Reporting_read_ini().get_field2_dropdown_for_visitors_by_xpath())
            if field2.is_displayed():
                pass
            field1_dropdown = Select(field1)
            time.sleep(web_driver.one_second)
            field1_dropdown.select_by_visible_text('number of visitors')
            field2_dropdown = Select(field2)
            time.sleep(web_driver.one_second)
            field2_dropdown.select_by_visible_text('day of week')
            time.sleep(web_driver.one_second)

        except Exception as ex:
            self.logger.error(ex)

    def for_number_of_visitors_by_day_of_week_verify_number_of_visitors_from_report_field1_and_day_of_week_from_report_field2_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_060 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            time.sleep(web_driver.one_second)
            field1.select_by_visible_text('number of visitors')

            value1 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()). \
                get_attribute('value')
            self.logger.info(f"value1: {value1}")
            if Reporting_read_ini().get_expected_second_text_from_field1() in value1:
                self.logger.info("Selected 'number of visitors' from report field1 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            field2 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_field2_dropdown_for_visitors_by_xpath()))
            field2.select_by_visible_text('day of week')

            value2 = self.d.find_element(By.XPATH, Reporting_read_ini().get_field2_dropdown_for_visitors_by_xpath()). \
                get_attribute('value')
            self.logger.info(f"value2: {value2}")
            if Reporting_read_ini().get_expected_second_text_from_field2() in value2:
                self.logger.info("Selected 'day of week' from report field2 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_060.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_060.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_060_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_060_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_060 got an exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_box_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_061 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_day_of_week()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_061.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_061.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_061_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_061_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_061 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_062 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_day_of_week()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_062.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_062.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_062_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_062_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_062 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_063 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_day_of_week()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_063.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_063.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_063_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_063_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_063 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_064 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_day_of_week()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_064.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_064.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_064_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_064_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_064 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_065 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_day_of_week()
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
            self.logger.info(
                f"End calender disable status after click: {end_date_calender_box.get_attribute('disabled')}")
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_065.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_065.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_065_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_065_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_065 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox(self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_066 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_day_of_week()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_066.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_066.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_066_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_066_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_066 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_Optional_Filters_Age_Range_to_Number_of_ages_to_group_totals_by_text_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_067 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_day_of_week()
            actual_optional_filters_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                               get_optional_filters_text_by_xpath()).text
            self.logger.info(f"actual optional filters text: {actual_optional_filters_text}")
            expected_optional_filters_text = Reporting_read_ini().get_expected_optional_filters_text()
            self.logger.info(f"expected optional filters text: {expected_optional_filters_text}")
            if actual_optional_filters_text == expected_optional_filters_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_age_range_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_age_range_text_by_xpath()).text
            self.logger.info(f"Age range text: {actual_age_range_text}")
            expected_age_range_text = Reporting_read_ini().get_expected_age_range_text()
            self.logger.info(f"expected Age range text: {expected_age_range_text}")
            if actual_age_range_text == expected_age_range_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_to_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_to_text_by_xpath()).text
            self.logger.info(f"Actual 'to' text: {actual_to_text}")
            expected_to_text = Reporting_read_ini().get_expected_to_text()
            self.logger.info(f"expected 'to' text: {expected_to_text}")
            if actual_to_text == expected_to_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_number_of_ages_to_group_total_by_text = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_number_of_ages_to_group_totals_by_text_by_xpath()).text
            self.logger.info(f"actual nuber of ages to group totals by text: "
                             f"{actual_number_of_ages_to_group_total_by_text}")
            expected_number_of_ages_to_group_totals_by_text = Reporting_read_ini(). \
                get_expected_number_of_ages_to_group_totals_by_text()
            self.logger.info(f"expected nuber of ages to group totals by text: "
                             f"{expected_number_of_ages_to_group_totals_by_text}")
            if actual_number_of_ages_to_group_total_by_text == expected_number_of_ages_to_group_totals_by_text:
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_067.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_067.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_067_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_067_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_067 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_start_age_dropdown_end_age_dropdown_and_number_to_age_group_totals_by_dropdown_are_visible_and_clickable_click_on_dropdowns(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_068 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_day_of_week()
            start_age_dropdown = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_age_dropdown_by_xpath())
            end_age_dropdown = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_age_dropdown_by_xpath())
            number_age_group_totals_dropdown = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_number_of_ages_to_group_totals_by_dropdown_by_xpath())
            if start_age_dropdown.is_displayed():
                self.logger.info("Start age dropdown is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if start_age_dropdown.is_enabled():
                self.logger.info("Start age dropdown is clickable...")
                start_age_dropdown.click()
                time.sleep(web_driver.one_second)
                start_age_dropdown.click()
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            start_age_dropdown_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                            get_start_age_dropdown_items_by_xpath())
            if len(start_age_dropdown_items) > 0:
                self.logger.info("Start age dropdown items are visible...")
                for x in range(len(start_age_dropdown_items) - 1):
                    options = start_age_dropdown_items[x + 1]
                    if int(options.text) == x + 1:
                        self.status.append(True)
                    else:
                        self.status.append(False)

            time.sleep(web_driver.one_second)
            if end_age_dropdown.is_displayed():
                self.logger.info("End age dropdown is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if end_age_dropdown.is_enabled():
                self.logger.info("End age dropdown is clickable...")
                end_age_dropdown.click()
                time.sleep(web_driver.one_second)
                end_age_dropdown.click()
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            end_age_dropdown_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                          get_end_age_dropdown_items_by_xpath())
            if len(end_age_dropdown_items) > 0:
                self.logger.info("End age dropdown items are visible...")
                for y in range(len(end_age_dropdown_items) - 1):
                    options = end_age_dropdown_items[y + 1]
                    if int(options.text) == y + 1:
                        self.status.append(True)
                    else:
                        self.status.append(False)

            time.sleep(web_driver.one_second)
            if number_age_group_totals_dropdown.is_displayed():
                self.logger.info("'Number age group totals by' dropdown is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if number_age_group_totals_dropdown.is_enabled():
                self.logger.info("'Number age group totals by' dropdown is clickable...")
                number_age_group_totals_dropdown.click()
                time.sleep(web_driver.one_second)
                number_age_group_totals_dropdown.click()
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            age_bucket_dropdown_items = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_number_of_ages_to_group_totals_by_dropdown_items())

            if len(age_bucket_dropdown_items) > 0:
                self.logger.info("'Number of age to group totals by' dropdown items are visible...")
                for z in range(len(age_bucket_dropdown_items) - 1):
                    options = age_bucket_dropdown_items[z + 1]
                    if int(options.text) == z + 2:
                        self.status.append(True)
                    else:
                        self.status.append(False)

            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"count: {len(self.status)}  \nstatus: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_068.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_068.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_068_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_068_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_068 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_gender_and_male_texts_are_visible_male_checkbox_is_visible_and_clickable_and_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_069 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_day_of_week()
            actual_gender_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_gender_text_by_xpath()).text
            self.logger.info(f"actual gender text: {actual_gender_text}")
            expected_gender_text = Reporting_read_ini().get_expected_gender_text()
            self.logger.info(f"expected text: {expected_gender_text}")
            if actual_gender_text == expected_gender_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_male_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_text_by_xpath()).text
            self.logger.info(f"actual male text: {actual_male_text}")
            expected_male_text = Reporting_read_ini().get_expected_male_text()
            self.logger.info(f"expected text: {expected_male_text}")
            if actual_male_text == expected_male_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_displayed():
                self.logger.info("Male checkbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if male_checkbox.is_enabled():
                self.logger.info("Male checkbox is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if male_checkbox.is_selected():
                self.logger.info("Male checkbox is selected by default !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_069.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_069.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_069_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_069_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_069 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_female_text_is_visible_female_checkbox_is_visible_and_clickable_and_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_070 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_day_of_week()
            actual_female_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_text_by_xpath()).text
            self.logger.info(f"actual female text: {actual_female_text}")
            expected_female_text = Reporting_read_ini().get_expected_female_text()
            self.logger.info(f"expected text: {expected_female_text}")
            if actual_female_text == expected_female_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_displayed():
                self.logger.info("Female checkbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if female_checkbox.is_enabled():
                self.logger.info("Female checkbox is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if female_checkbox.is_selected():
                self.logger.info("Female checkbox is selected by default !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_070.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_070.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_070_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_070_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_070 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_unknown_text_is_visible_unknown_gender_checkbox_is_visible_and_clickable_and_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_071 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_day_of_week()
            actual_unknown_gender_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                             get_unknown_gender_text_by_xpath()).text
            self.logger.info(f"actual unknown gender text: {actual_unknown_gender_text}")
            expected_unknown_gender_text = Reporting_read_ini().get_expected_unknown_gender_text()
            self.logger.info(f"expected unknown gender text: {expected_unknown_gender_text}")
            if actual_unknown_gender_text == expected_unknown_gender_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_displayed():
                self.logger.info("Unknown gender checkbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if unknown_gender_checkbox.is_enabled():
                self.logger.info("Unknown gender checkbox is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if unknown_gender_checkbox.is_selected():
                self.logger.info("Unknown gender checkbox is selected by default !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_071.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_071.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_071_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_071_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_071 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_select_zone_filter_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible_text_on_right_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_072 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_day_of_week()
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
            actual_text_beside_select_zone_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_text_beside_select_zone_filter_button_by_xpath()).text
            self.logger.info(f"actual text beside select zone button: {actual_text_beside_select_zone_button}")
            expected_text_beside_select_zone_button = Reporting_read_ini(). \
                get_expected_text_beside_select_zone_filter_button()
            self.logger.info(f"expected text beside select zone button: {expected_text_beside_select_zone_button}")
            if actual_text_beside_select_zone_button == expected_text_beside_select_zone_button:
                self.logger.info("text beside select zone filter button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_072.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_072.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_072_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_072_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_072 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_generate_report_button_is_visible_and_clickable_generate_report_text_and_chart_icon_both_are_visible_on_button(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_073 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_day_of_week()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_073.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_073.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_073_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_073_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_073 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_in_select_zone_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_074 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_day_of_week()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_074.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_074.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_074_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_074_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_074 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_search_zones_textbox_is_visible_and_clickable_label_on_it_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_075 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_day_of_week()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_075.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_075.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_075_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_075_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_075 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_zone_list_below_search_zones_textbox_is_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_076 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_day_of_week()
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
            WebDriverWait(self.d, 30).until(EC.presence_of_element_located((By.XPATH, Reporting_read_ini().
                                                                            get_zone_item_list_from_zone_panel_by_xpath())))
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_076.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_076.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_076_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_076_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_076 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_select_all_button_is_visible_and_clickable_and_text_on_it_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_077 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_day_of_week()
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
            if actual_text_on_select_all_button_in_zone_filter == Reporting_read_ini(). \
                    get_expected_text_on_select_all_button():
                self.logger.info("text on select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_077.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_077.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_077_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_077_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_077 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_selected_zone_list_title_and_default_text_below_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_078 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_day_of_week()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_078.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_078.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_078_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_078_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_078 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_close_zone_menu_button_is_visible_and_clickable_and_text_on_it_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_079 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_day_of_week()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_079.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_079.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_079_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_079_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_079 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_click_on_select_all_button_and_verify_all_selected_zones_are_visible_in_selected_zone_list(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_080 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_day_of_week()
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
            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_zone_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_080.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_080.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_080_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_080_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_080 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_click_on_select_all_button_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_081 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_day_of_week()
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
            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_zone_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_081.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_081.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_081_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_081_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_081 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_click_on_select_all_button_and_verify_save_zone_selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_082 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_day_of_week()
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
            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_zone_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_082.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_082.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_082_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_082_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_082 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_select_one_zone_from_zone_list_and_verify_selected_zone_is_visible_in_selected_zone_list_verify_save_zone_selection_button_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_083 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_day_of_week()
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
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_first_zone_name_in_selected_zone_list_by_xpath()).text
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
            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_zone_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_083.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_083.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_083_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_083_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_083 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_click_on_save_zone_selection_button_with_at_least_one_zone_selected_and_verify_View_and_edit_zones_button_is_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_084 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_day_of_week()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_084.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_084.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_084_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_084_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_084 got exception as: {ex}")

    def for_number_of_visitors_by_day_of_week_verify_text_and_numeric_value_of_number_of_selected_zones_on_view_and_edit_zones_button_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_085 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_day_of_week()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                             get_zone_items_list_below_search_zone_textbox_by_xpath())
            zone_list[0].click()
            self.logger.info("Selected first zone from zone list...")
            zone_list[1].click()
            self.logger.info("Selected second zone from zone list...")
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_085.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_085.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_085_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_085_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_085 got exception as: {ex}")

    def verify_report_for_number_of_visitors_by_day_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_048 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_day_of_week()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                self.logger.info("Male checkbox is selected...")
                pass
            else:
                male_checkbox.click()
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_048.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_048.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_048_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_048_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_048 got exception as: {ex}")

    def verify_report_for_number_of_visitors_by_day_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_049 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_day_of_week()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                self.logger.info("Female checkbox is selected...")
                pass
            else:
                female_checkbox.click()
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_049.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_049.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_049_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_049_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_049 got exception as: {ex}")

    def verify_report_for_number_of_visitors_by_day_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_050 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_day_of_week()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                self.logger.info("Unknown gender checkbox is selected...")
                pass
            else:
                unknown_gender_checkbox.click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_050.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_050.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_050_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_050_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_050 got exception as: {ex}")

    def verify_report_for_number_of_visitors_by_day_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_051 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_day_of_week()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            self.logger.info("Selected all genders by default...")
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_051.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_051.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_051_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_051_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_051 got exception as: {ex}")

    def verify_report_for_number_of_visitors_by_day_of_week_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_208 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_day_of_week()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                self.logger.info("Male checkbox is selected...")
                pass
            else:
                male_checkbox.click()
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_208.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_208.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_208_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_208_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_208 got exception as: {ex}")

    def verify_report_for_number_of_visitors_by_day_of_week_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_209 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_day_of_week()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                self.logger.info("Female checkbox is selected...")
                pass
            else:
                female_checkbox.click()
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_209.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_209.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_209_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_209_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_209 got exception as: {ex}")

    def verify_report_for_number_of_visitors_by_day_of_week_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_210 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_day_of_week()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                self.logger.info("Unknown gender checkbox is selected...")
                pass
            else:
                unknown_gender_checkbox.click()

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_210.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_210.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_210_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_210_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_210 got exception as: {ex}")

    def verify_report_for_number_of_visitors_by_day_of_week_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_DW_211 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_day_of_week()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            self.logger.info("Selected all genders by default...")
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_211.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_211.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_DW_211_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_DW_211_exception.png")
            self.logger.error(f"TC_Reporting_VS_DW_211 got exception as: {ex}")

    def select_number_of_visitors_by_hour_of_week(self):
        try:
            time.sleep(web_driver.one_second)
            field1 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath())
            field2 = self.d.find_element(By.XPATH, Reporting_read_ini().get_field2_dropdown_for_visitors_by_xpath())
            if field2.is_displayed():
                pass
            else:
                field1_dropdown = Select(field1)
                time.sleep(web_driver.one_second)
                field1_dropdown.select_by_visible_text('number of visitors')
                field2_dropdown = Select(field2)
                time.sleep(web_driver.one_second)
                field2_dropdown.select_by_visible_text('hour of week')
                time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def for_number_of_visitors_by_hour_of_week_verify_number_of_visitors_from_report_field1_and_hour_of_week_from_report_field2_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_086 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            time.sleep(web_driver.one_second)
            field1.select_by_visible_text('number of visitors')

            value1 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()). \
                get_attribute('value')
            self.logger.info(f"value1: {value1}")
            if Reporting_read_ini().get_expected_second_text_from_field1() in value1:
                self.logger.info("Selected 'number of visitors' from report field1 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            field2 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_field2_dropdown_for_visitors_by_xpath()))
            field2.select_by_visible_text('hour of week')

            value2 = self.d.find_element(By.XPATH, Reporting_read_ini().get_field2_dropdown_for_visitors_by_xpath()). \
                get_attribute('value')
            self.logger.info(f"value2: {value2}")
            if Reporting_read_ini().get_expected_third_text_from_field2() in value2:
                self.logger.info("Selected 'hour of week' from report field2 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_086.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_086.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_086_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_086_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_086 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_box_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_087 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_week()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_087.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_087.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_087_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_087_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_087 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_088 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_week()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_088.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_088.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_088_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_088_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_088 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_089 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_week()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_089.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_089.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_089_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_089_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_089 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_090 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_week()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_090.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_090.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_090_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_090_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_090 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_091 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_week()
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
            self.logger.info(
                f"End calender disable status after click: {end_date_calender_box.get_attribute('disabled')}")
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_091.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_091.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_091_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_091_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_091 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox(self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_092 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_week()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_092.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_092.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_092_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_092_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_092 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_Optional_Filters_Age_Range_to_Number_of_ages_to_group_totals_by_text_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_093 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_week()
            actual_optional_filters_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                               get_optional_filters_text_by_xpath()).text
            self.logger.info(f"actual optional filters text: {actual_optional_filters_text}")
            expected_optional_filters_text = Reporting_read_ini().get_expected_optional_filters_text()
            self.logger.info(f"expected optional filters text: {expected_optional_filters_text}")
            if actual_optional_filters_text == expected_optional_filters_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_age_range_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_age_range_text_by_xpath()).text
            self.logger.info(f"Age range text: {actual_age_range_text}")
            expected_age_range_text = Reporting_read_ini().get_expected_age_range_text()
            self.logger.info(f"expected Age range text: {expected_age_range_text}")
            if actual_age_range_text == expected_age_range_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_to_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_to_text_by_xpath()).text
            self.logger.info(f"Actual 'to' text: {actual_to_text}")
            expected_to_text = Reporting_read_ini().get_expected_to_text()
            self.logger.info(f"expected 'to' text: {expected_to_text}")
            if actual_to_text == expected_to_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_number_of_ages_to_group_total_by_text = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_number_of_ages_to_group_totals_by_text_by_xpath()).text
            self.logger.info(f"actual nuber of ages to group totals by text: "
                             f"{actual_number_of_ages_to_group_total_by_text}")
            expected_number_of_ages_to_group_totals_by_text = Reporting_read_ini(). \
                get_expected_number_of_ages_to_group_totals_by_text()
            self.logger.info(f"expected nuber of ages to group totals by text: "
                             f"{expected_number_of_ages_to_group_totals_by_text}")
            if actual_number_of_ages_to_group_total_by_text == expected_number_of_ages_to_group_totals_by_text:
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_093.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_093.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_093_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_093_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_093 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_start_age_dropdown_end_age_dropdown_and_number_to_age_group_totals_by_dropdown_are_visible_and_clickable_click_on_dropdowns(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_094 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_week()
            start_age_dropdown = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_age_dropdown_by_xpath())
            end_age_dropdown = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_age_dropdown_by_xpath())
            number_age_group_totals_dropdown = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_number_of_ages_to_group_totals_by_dropdown_by_xpath())
            if start_age_dropdown.is_displayed():
                self.logger.info("Start age dropdown is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if start_age_dropdown.is_enabled():
                self.logger.info("Start age dropdown is clickable...")
                start_age_dropdown.click()
                time.sleep(web_driver.one_second)
                start_age_dropdown.click()
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            start_age_dropdown_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                            get_start_age_dropdown_items_by_xpath())
            if len(start_age_dropdown_items) > 0:
                self.logger.info("Start age dropdown items are visible...")
                for x in range(len(start_age_dropdown_items) - 1):
                    options = start_age_dropdown_items[x + 1]
                    if int(options.text) == x + 1:
                        self.status.append(True)
                    else:
                        self.status.append(False)

            time.sleep(web_driver.one_second)
            if end_age_dropdown.is_displayed():
                self.logger.info("End age dropdown is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if end_age_dropdown.is_enabled():
                self.logger.info("End age dropdown is clickable...")
                end_age_dropdown.click()
                time.sleep(web_driver.one_second)
                end_age_dropdown.click()
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            end_age_dropdown_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                          get_end_age_dropdown_items_by_xpath())
            if len(end_age_dropdown_items) > 0:
                self.logger.info("End age dropdown items are visible...")
                for y in range(len(end_age_dropdown_items) - 1):
                    options = end_age_dropdown_items[y + 1]
                    if int(options.text) == y + 1:
                        self.status.append(True)
                    else:
                        self.status.append(False)

            time.sleep(web_driver.one_second)
            if number_age_group_totals_dropdown.is_displayed():
                self.logger.info("'Number age group totals by' dropdown is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if number_age_group_totals_dropdown.is_enabled():
                self.logger.info("'Number age group totals by' dropdown is clickable...")
                number_age_group_totals_dropdown.click()
                time.sleep(web_driver.one_second)
                number_age_group_totals_dropdown.click()
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            age_bucket_dropdown_items = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_number_of_ages_to_group_totals_by_dropdown_items())

            if len(age_bucket_dropdown_items) > 0:
                self.logger.info("'Number of age to group totals by' dropdown items are visible...")
                for z in range(len(age_bucket_dropdown_items) - 1):
                    options = age_bucket_dropdown_items[z + 1]
                    if int(options.text) == z + 2:
                        self.status.append(True)
                    else:
                        self.status.append(False)

            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"count: {len(self.status)}  \nstatus: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_094.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_094.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_094_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_094_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_094 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_gender_and_male_texts_are_visible_male_checkbox_is_visible_and_clickable_and_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_095 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_week()
            actual_gender_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_gender_text_by_xpath()).text
            self.logger.info(f"actual gender text: {actual_gender_text}")
            expected_gender_text = Reporting_read_ini().get_expected_gender_text()
            self.logger.info(f"expected text: {expected_gender_text}")
            if actual_gender_text == expected_gender_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_male_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_text_by_xpath()).text
            self.logger.info(f"actual male text: {actual_male_text}")
            expected_male_text = Reporting_read_ini().get_expected_male_text()
            self.logger.info(f"expected text: {expected_male_text}")
            if actual_male_text == expected_male_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_displayed():
                self.logger.info("Male checkbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if male_checkbox.is_enabled():
                self.logger.info("Male checkbox is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if male_checkbox.is_selected():
                self.logger.info("Male checkbox is selected by default !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_095.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_095.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_095_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_095_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_095 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_female_text_is_visible_female_checkbox_is_visible_and_clickable_and_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_096 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_week()
            actual_female_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_text_by_xpath()).text
            self.logger.info(f"actual female text: {actual_female_text}")
            expected_female_text = Reporting_read_ini().get_expected_female_text()
            self.logger.info(f"expected text: {expected_female_text}")
            if actual_female_text == expected_female_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_displayed():
                self.logger.info("Female checkbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if female_checkbox.is_enabled():
                self.logger.info("Female checkbox is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if female_checkbox.is_selected():
                self.logger.info("Female checkbox is selected by default !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_096.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_096.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_096_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_096_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_096 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_unknown_text_is_visible_unknown_gender_checkbox_is_visible_and_clickable_and_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_097 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_week()
            actual_unknown_gender_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                             get_unknown_gender_text_by_xpath()).text
            self.logger.info(f"actual unknown gender text: {actual_unknown_gender_text}")
            expected_unknown_gender_text = Reporting_read_ini().get_expected_unknown_gender_text()
            self.logger.info(f"expected unknown gender text: {expected_unknown_gender_text}")
            if actual_unknown_gender_text == expected_unknown_gender_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_displayed():
                self.logger.info("Unknown gender checkbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if unknown_gender_checkbox.is_enabled():
                self.logger.info("Unknown gender checkbox is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if unknown_gender_checkbox.is_selected():
                self.logger.info("Unknown gender checkbox is selected by default !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_097.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_097.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_097_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_097_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_097 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_select_zone_filter_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible_text_on_right_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_098 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_week()
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
            actual_text_beside_select_zone_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_text_beside_select_zone_filter_button_by_xpath()).text
            self.logger.info(f"actual text beside select zone button: {actual_text_beside_select_zone_button}")
            expected_text_beside_select_zone_button = Reporting_read_ini(). \
                get_expected_text_beside_select_zone_filter_button()
            self.logger.info(f"expected text beside select zone button: {expected_text_beside_select_zone_button}")
            if actual_text_beside_select_zone_button == expected_text_beside_select_zone_button:
                self.logger.info("text beside select zone filter button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_098.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_098.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_098_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_098_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_098 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_generate_report_button_is_visible_and_clickable_generate_report_text_and_chart_icon_both_are_visible_on_button(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_099 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_week()
            generate_report_button = self.d.find_element(By.XPATH,
                                                         Reporting_read_ini().get_generate_report_button_by_xpath())
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
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_chart_icon_on_generate_report_button_by_xpath()). \
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_099.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_099.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_099_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_099_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_099 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_in_select_zone_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_100 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_week()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_100.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_100.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_100_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_100_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_100 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_search_zones_textbox_is_visible_and_clickable_label_on_it_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_101 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_101.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_101.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_101_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_101_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_101 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_zone_list_below_search_zones_textbox_is_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_102 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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
            WebDriverWait(self.d, 30).until(EC.presence_of_element_located((By.XPATH, Reporting_read_ini().
                                                         get_zone_item_list_from_zone_panel_by_xpath())))
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

            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_102.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_102.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_102_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_102_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_102 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_select_all_button_is_visible_and_clickable_and_text_on_it_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_103 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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
            if actual_text_on_select_all_button_in_zone_filter == Reporting_read_ini(). \
                    get_expected_text_on_select_all_button():
                self.logger.info("text on select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_103.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_103.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_103_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_103_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_103 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_selected_zone_list_title_and_default_text_below_is_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_104 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_104.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_104.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_104_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_104_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_104 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_close_zone_menu_button_is_visible_and_clickable_and_text_on_it_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_105 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_105.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_105.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_105_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_105_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_105 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_click_on_select_all_button_and_verify_all_selected_zones_are_visible_in_selected_zone_list(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_106 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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
            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_zone_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_106.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_106.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_106_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_106_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_106 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_click_on_select_all_button_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_107 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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
            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_zone_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_107.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_107.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_107_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_107_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_107 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_click_on_select_all_button_and_verify_save_zone_selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_108 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_dot_circle_icon_on_save_zone_selection_button()). \
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
            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_zone_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_108.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_108.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_108_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_108_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_108 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_select_one_zone_from_zone_list_and_verify_selected_zone_is_visible_in_selected_zone_list_verify_save_zone_selection_button_is_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_109 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_first_zone_name_in_selected_zone_list_by_xpath()).text
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
            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_zone_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_109.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_109.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_109_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_109_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_109 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_click_on_save_zone_selection_button_with_at_least_one_zone_selected_and_verify_View_and_edit_zones_button_is_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_110 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_110.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_110.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_110_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_110_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_110 got an exception as: {ex}")

    def for_number_of_visitors_by_hour_of_week_verify_text_and_numeric_value_of_number_of_selected_zones_on_view_and_edit_zones_button_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_111 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_hour_of_week()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                             get_zone_items_list_below_search_zone_textbox_by_xpath())
            zone_list[0].click()
            self.logger.info("Selected first zone from zone list...")
            zone_list[1].click()
            self.logger.info("Selected second zone from zone list...")
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_111.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_111.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_111_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_111_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_111 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_hour_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_052 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_week()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                self.logger.info("Male checkbox is selected...")
                pass
            else:
                male_checkbox.click()
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_052.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_052.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_052_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_052_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_052 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_hour_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_053 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_week()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                self.logger.info("Female checkbox is selected...")
                pass
            else:
                female_checkbox.click()
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_053.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_053.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_053_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_053_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_053 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_hour_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_054 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_week()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                self.logger.info("Unknown gender checkbox is selected...")
                pass
            else:
                unknown_gender_checkbox.click()

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")

            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_054.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_054.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_054_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_054_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_054 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_hour_of_week_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_055 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_week()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            self.logger.info("Selected all genders by default...")
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_055.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_055.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_055_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_055_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_055 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_hour_of_week_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_212 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_week()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                self.logger.info("Male checkbox is selected...")
                pass
            else:
                male_checkbox.click()
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_212.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_212.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_212_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_212_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_212 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_hour_of_week_with_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_213 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_week()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                self.logger.info("Female checkbox is selected...")
                pass
            else:
                female_checkbox.click()
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_213.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_213.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_213_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_213_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_213 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_hour_of_week_with_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_214 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_week()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                self.logger.info("Unknown gender checkbox is selected...")
                pass
            else:
                unknown_gender_checkbox.click()

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_214.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_214.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_214_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_214_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_214 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_hour_of_week_with_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_and_zone_as_All_devices(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_HW_215 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_hour_of_week()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            self.logger.info("Selected all genders by default...")
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            for i in range(len(self.zones)):
                for items in zone_items_list:
                    if str(items.text) == str(self.zones[i]):
                        items.click()
                        self.logger.info(f"Selected zone as: {str(self.zones[i])}")
                        self.status.append(True)
                break

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_zone_selection_button_by_xpath()).click()
            self.logger.info("Clicked on 'Save zone selection' button..")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_215.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_215.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_HW_215_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_HW_215_exception.png")
            self.logger.error(f"TC_Reporting_VS_HW_215 got an exception as: {ex}")

    def select_number_of_visitors_by_zone(self):
        try:
            time.sleep(web_driver.one_second)
            field1 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath())
            field2 = self.d.find_element(By.XPATH, Reporting_read_ini().get_field2_dropdown_for_visitors_by_xpath())
            if field2.is_displayed():
                pass
            else:
                field1_dropdown = Select(field1)
                field1_dropdown.select_by_visible_text('number of visitors')
                time.sleep(web_driver.one_second)
                field2_dropdown = Select(field2)
                field2_dropdown.select_by_visible_text('zone')
                time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def for_number_of_visitors_by_zone_verify_number_of_visitors_from_report_field1_and_zone_from_report_field2_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_112 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            time.sleep(web_driver.one_second)
            field1.select_by_visible_text('number of visitors')

            value1 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()). \
                get_attribute('value')
            self.logger.info(f"value1: {value1}")
            if Reporting_read_ini().get_expected_second_text_from_field1() in value1:
                self.logger.info("Selected 'number of visitors' from report field1 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            field2 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_field2_dropdown_for_visitors_by_xpath()))
            field2.select_by_visible_text('zone')

            value2 = self.d.find_element(By.XPATH, Reporting_read_ini().
                                         get_field2_dropdown_for_visitors_by_xpath()).get_attribute('value')
            self.logger.info(f"value2: {value2}")
            if Reporting_read_ini().get_expected_fourth_text_from_field2() in value2:
                self.logger.info("Selected 'zone' from report field2 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_112.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_112.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_112_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_112_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_112 got an exception as: {ex}")

    def for_number_of_visitors_by_zone_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_box_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_113 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_zone()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_113.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_113.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_113_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_113_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_113 got an exception as: {ex}")

    def for_number_of_visitors_by_zone_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_114 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_zone()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_114.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_114.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_114_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_114_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_114 got an exception as: {ex}")

    def for_number_of_visitors_by_zone_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_115 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_zone()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_115.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_115.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_115_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_115_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_115 got an exception as: {ex}")

    def for_number_of_visitors_by_zone_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_116 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_zone()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_116.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_116.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_116_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_116_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_116 got an exception as: {ex}")

    def for_number_of_visitors_by_zone_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_117 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_zone()
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
            self.logger.info(
                f"End calender disable status after click: {end_date_calender_box.get_attribute('disabled')}")
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_117.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_117.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_117_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_117_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_117 got an exception as: {ex}")

    def for_number_of_visitors_by_zone_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox(self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_118 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_zone()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_118.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_118.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_118_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_118_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_118 got an exception as: {ex}")

    def for_number_of_visitors_by_zone_verify_Optional_Filters_Age_Range_to_Number_of_ages_to_group_totals_by_text_are_visible(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_119 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_zone()
            actual_optional_filters_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                               get_optional_filters_text_by_xpath()).text
            self.logger.info(f"actual optional filters text: {actual_optional_filters_text}")
            expected_optional_filters_text = Reporting_read_ini().get_expected_optional_filters_text()
            self.logger.info(f"expected optional filters text: {expected_optional_filters_text}")
            if actual_optional_filters_text == expected_optional_filters_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_age_range_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_age_range_text_by_xpath()).text
            self.logger.info(f"Age range text: {actual_age_range_text}")
            expected_age_range_text = Reporting_read_ini().get_expected_age_range_text()
            self.logger.info(f"expected Age range text: {expected_age_range_text}")
            if actual_age_range_text == expected_age_range_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_to_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_to_text_by_xpath()).text
            self.logger.info(f"Actual 'to' text: {actual_to_text}")
            expected_to_text = Reporting_read_ini().get_expected_to_text()
            self.logger.info(f"expected 'to' text: {expected_to_text}")
            if actual_to_text == expected_to_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_number_of_ages_to_group_total_by_text = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_number_of_ages_to_group_totals_by_text_by_xpath()).text
            self.logger.info(f"actual nuber of ages to group totals by text: "
                             f"{actual_number_of_ages_to_group_total_by_text}")
            expected_number_of_ages_to_group_totals_by_text = Reporting_read_ini(). \
                get_expected_number_of_ages_to_group_totals_by_text()
            self.logger.info(f"expected nuber of ages to group totals by text: "
                             f"{expected_number_of_ages_to_group_totals_by_text}")
            if actual_number_of_ages_to_group_total_by_text == expected_number_of_ages_to_group_totals_by_text:
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_119.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_119.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_119_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_119_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_119 got an exception as: {ex}")

    def for_number_of_visitors_by_zone_verify_start_age_dropdown_end_age_dropdown_and_number_to_age_group_totals_by_dropdown_are_visible_and_clickable_click_on_dropdowns(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_120 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_zone()
            start_age_dropdown = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_age_dropdown_by_xpath())
            end_age_dropdown = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_age_dropdown_by_xpath())
            number_age_group_totals_dropdown = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_number_of_ages_to_group_totals_by_dropdown_by_xpath())
            if start_age_dropdown.is_displayed():
                self.logger.info("Start age dropdown is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if start_age_dropdown.is_enabled():
                self.logger.info("Start age dropdown is clickable...")
                start_age_dropdown.click()
                time.sleep(web_driver.one_second)
                start_age_dropdown.click()
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            start_age_dropdown_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                            get_start_age_dropdown_items_by_xpath())
            if len(start_age_dropdown_items) > 0:
                self.logger.info("Start age dropdown items are visible...")
                for x in range(len(start_age_dropdown_items) - 1):
                    options = start_age_dropdown_items[x + 1]
                    if int(options.text) == x + 1:
                        self.status.append(True)
                    else:
                        self.status.append(False)

            time.sleep(web_driver.one_second)
            if end_age_dropdown.is_displayed():
                self.logger.info("End age dropdown is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if end_age_dropdown.is_enabled():
                self.logger.info("End age dropdown is clickable...")
                end_age_dropdown.click()
                time.sleep(web_driver.one_second)
                end_age_dropdown.click()
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            end_age_dropdown_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                          get_end_age_dropdown_items_by_xpath())
            if len(end_age_dropdown_items) > 0:
                self.logger.info("End age dropdown items are visible...")
                for y in range(len(end_age_dropdown_items) - 1):
                    options = end_age_dropdown_items[y + 1]
                    if int(options.text) == y + 1:
                        self.status.append(True)
                    else:
                        self.status.append(False)

            time.sleep(web_driver.one_second)
            if number_age_group_totals_dropdown.is_displayed():
                self.logger.info("'Number age group totals by' dropdown is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if number_age_group_totals_dropdown.is_enabled():
                self.logger.info("'Number age group totals by' dropdown is clickable...")
                number_age_group_totals_dropdown.click()
                time.sleep(web_driver.one_second)
                number_age_group_totals_dropdown.click()
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            age_bucket_dropdown_items = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_number_of_ages_to_group_totals_by_dropdown_items())

            if len(age_bucket_dropdown_items) > 0:
                self.logger.info("'Number of age to group totals by' dropdown items are visible...")
                for z in range(len(age_bucket_dropdown_items) - 1):
                    options = age_bucket_dropdown_items[z + 1]
                    if int(options.text) == z + 2:
                        self.status.append(True)
                    else:
                        self.status.append(False)

            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"count: {len(self.status)}  \nstatus: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_120.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_120.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_120_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_120_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_120 got an exception as: {ex}")

    def for_number_of_visitors_by_zone_verify_gender_and_male_texts_are_visible_male_checkbox_is_visible_and_clickable_and_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_121 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_zone()
            actual_gender_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_gender_text_by_xpath()).text
            self.logger.info(f"actual gender text: {actual_gender_text}")
            expected_gender_text = Reporting_read_ini().get_expected_gender_text()
            self.logger.info(f"expected text: {expected_gender_text}")
            if actual_gender_text == expected_gender_text:
                self.status.append(True)
            else:
                self.status.append(False)
            actual_male_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_text_by_xpath()).text
            self.logger.info(f"actual male text: {actual_male_text}")
            expected_male_text = Reporting_read_ini().get_expected_male_text()
            self.logger.info(f"expected text: {expected_male_text}")
            if actual_male_text == expected_male_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_displayed():
                self.logger.info("Male checkbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if male_checkbox.is_enabled():
                self.logger.info("Male checkbox is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if male_checkbox.is_selected():
                self.logger.info("Male checkbox is selected by default !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_121.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_121.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_121_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_121_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_121 got an exception as: {ex}")

    def for_number_of_visitors_by_zone_verify_female_text_is_visible_female_checkbox_is_visible_and_clickable_and_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_122 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_zone()
            actual_female_text = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_text_by_xpath()).text
            self.logger.info(f"actual female text: {actual_female_text}")
            expected_female_text = Reporting_read_ini().get_expected_female_text()
            self.logger.info(f"expected text: {expected_female_text}")
            if actual_female_text == expected_female_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_displayed():
                self.logger.info("Female checkbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if female_checkbox.is_enabled():
                self.logger.info("Female checkbox is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if female_checkbox.is_selected():
                self.logger.info("Female checkbox is selected by default !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_122.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_122.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_122_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_122_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_122 got an exception as: {ex}")

    def for_number_of_visitors_by_zone_verify_unknown_text_is_visible_unknown_gender_checkbox_is_visible_and_clickable_and_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_123 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_zone()
            actual_unknown_gender_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                             get_unknown_gender_text_by_xpath()).text
            self.logger.info(f"actual unknown gender text: {actual_unknown_gender_text}")
            expected_unknown_gender_text = Reporting_read_ini().get_expected_unknown_gender_text()
            self.logger.info(f"expected unknown gender text: {expected_unknown_gender_text}")
            if actual_unknown_gender_text == expected_unknown_gender_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_displayed():
                self.logger.info("Unknown gender checkbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if unknown_gender_checkbox.is_enabled():
                self.logger.info("Unknown gender checkbox is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if unknown_gender_checkbox.is_selected():
                self.logger.info("Unknown gender checkbox is selected by default !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_123.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_123.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_123_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_123_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_123 got an exception as: {ex}")

    def for_number_of_visitors_by_zone_verify_generate_report_button_is_visible_and_clickable_generate_report_text_and_chart_icon_both_are_visible_on_button(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_124 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_visitors_by_zone()
            generate_report_button = self.d.find_element(By.XPATH,
                                                         Reporting_read_ini().get_generate_report_button_by_xpath())
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
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_chart_icon_on_generate_report_button_by_xpath()). \
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_124.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_124.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_124_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_124_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_124 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_zone_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_all_zones_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_056 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_zone()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                self.logger.info("Male checkbox is selected...")
                pass
            else:
                male_checkbox.click()
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_056.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_056.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_056_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_056_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_056 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_zone_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_all_zones_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_057 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_zone()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                self.logger.info("Female checkbox is selected...")
                pass
            else:
                female_checkbox.click()
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_057.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_057.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_057_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_057_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_057 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_zone_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_all_zones_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_058 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_zone()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                self.logger.info("Unknown gender checkbox is selected...")
                pass
            else:
                unknown_gender_checkbox.click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_058.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_058.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_058_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_058_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_058 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_zone_with_default_dates_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_all_zones_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_059 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_zone()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            self.logger.info("Selected all genders by default...")

            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_059.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_059.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_059_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_059_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_059 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_zone_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_male_and_all_zones_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_216 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_zone()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                self.logger.info("Male checkbox is selected...")
                pass
            else:
                male_checkbox.click()
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_216.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_216.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_216_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_216_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_216 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_zone_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_female_and_all_zones_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_217 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_zone()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                self.logger.info("Female checkbox is selected...")
                pass
            else:
                female_checkbox.click()
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                unknown_gender_checkbox.click()
            else:
                pass

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_217.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_217.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_217_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_217_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_217 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_zone_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_gender_as_unknown_and_all_zones_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_218 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_zone()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            male_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_male_filter_checkbox())
            if male_checkbox.is_selected():
                male_checkbox.click()
            else:
                pass
            female_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_female_filter_checkbox())
            if female_checkbox.is_selected():
                female_checkbox.click()
            else:
                pass
            unknown_gender_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_unknown_gender_filter_checkbox())
            if unknown_gender_checkbox.is_selected():
                self.logger.info("Unknown gender checkbox is selected...")
                pass
            else:
                unknown_gender_checkbox.click()

            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on 'Generate report' button..")

            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_218.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_218.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_218_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_218_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_218 got an exception as: {ex}")

    def verify_report_for_number_of_visitors_by_zone_with_date_range_from_json_and_age_range_20_to_60_and_age_to_group_totals_by_10_and_all_gender_selected_and_all_zones_selected_by_default(
            self):
        try:
            self.logger.info("*********** TC_Reporting_VS_ZN_219 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_visitors_by_zone()
            self.get_start_date()
            self.get_end_date()
            time.sleep(web_driver.one_second)
            self.select_age_range_from_dropdowns()
            time.sleep(web_driver.one_second)
            self.logger.info("Selected all genders by default...")

            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            self.logger.info("Clicked on 'Generate report' button..")
            time.sleep(web_driver.two_second)
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info("Report panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_219.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_219.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_VS_ZN_219_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_VS_ZN_219_exception.png")
            self.logger.error(f"TC_Reporting_VS_ZN_219 got an exception as: {ex}")

    def select_number_of_enrollments_by_zone(self):
        try:
            time.sleep(web_driver.one_second)
            field1 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath())
            field2 = self.d.find_element(By.XPATH, Reporting_read_ini().get_field2_dropdown_for_enrollments_by_xpath())
            if field2.is_displayed():
                pass
            else:
                field1_dropdown = Select(field1)
                field1_dropdown.select_by_visible_text('number of enrollments')
                time.sleep(web_driver.one_second)
                field2_dropdown = Select(field2)
                field2_dropdown.select_by_visible_text('zone')
                time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def for_number_of_enrollments_by_zone_verify_number_of_enrollments_from_report_field1_and_zone_from_report_field2_texts_are_visible_on_dropdown(self):
        try:
            self.logger.info("*********** TC_Reporting_EN_ZN_125 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            time.sleep(web_driver.one_second)
            field1.select_by_visible_text('number of enrollments')
            time.sleep(web_driver.one_second)
            value1 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()). \
                get_attribute('value')
            self.logger.info(f"Value1: {value1}")
            if Reporting_read_ini().get_expected_third_text_from_field1() in value1:
                self.logger.info("Selected 'number of enrollments' from report field1 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)
            field2 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_field2_dropdown_for_enrollments_by_xpath()))
            time.sleep(web_driver.one_second)
            field2.select_by_visible_text('zone')
            value2 = self.d.find_element(By.XPATH, Reporting_read_ini().
                                         get_field2_dropdown_for_enrollments_by_xpath()).get_attribute('value')
            self.logger.info(f"Value2: {value2}")
            if Reporting_read_ini().get_expected_fourth_text_from_field2() in value2:
                self.logger.info("Selected 'zone' from report field2 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_125.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_125.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_125_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_125_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_125 got an exception as: {ex}")

    def for_number_of_enrollments_by_zone_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_box_are_visible(self):
        try:
            self.logger.info("*********** TC_Reporting_EN_ZN_126 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            self.select_number_of_enrollments_by_zone()
            time.sleep(web_driver.one_second)
            actual_date_and_time_range_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                  get_date_and_time_range_text_by_xpath()).text
            self.logger.info(f"actual date & time range text: {actual_date_and_time_range_text}")
            expected_date_range_text = Reporting_read_ini().get_expected_date_and_time_range_text()
            self.logger.info(f"expected date & time range text: {expected_date_range_text}")
            if actual_date_and_time_range_text == expected_date_range_text:
                time.sleep(web_driver.one_second)
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
            time.sleep(web_driver.one_second)
            self.logger.info(f"actual horizontal line below calenders: {actual_horizontal_line_below_calenders}")
            expected_horizontal_line_below_calenders = Reporting_read_ini(). \
                get_expected_horizontal_line_below_calenders()
            self.logger.info(f"expected horizontal line below calenders: {expected_horizontal_line_below_calenders}")
            if actual_horizontal_line_below_calenders == expected_horizontal_line_below_calenders:
                time.sleep(web_driver.one_second)
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_126.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_126.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_126_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_126_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_126 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("*********** TC_Reporting_EN_ZN_127 started **********")
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            self.select_number_of_enrollments_by_zone()
            time.sleep(web_driver.one_second)
            start_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                          get_start_date_calender_box_by_xpath())
            if start_date_calender_box.is_displayed():
                time.sleep(web_driver.one_second)
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
            time.sleep(web_driver.one_second)
            if start_date_checkbox.is_displayed():
                time.sleep(web_driver.one_second)
                self.logger.info("Start date checkbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if start_date_checkbox.is_enabled():
                time.sleep(web_driver.one_second)
                self.logger.info("Start date checkbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_127.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_127.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_127_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_127_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_127 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_128 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            self.select_number_of_enrollments_by_zone()
            time.sleep(web_driver.one_second)
            end_date_calender_box = self.d.find_element(By.XPATH,
                                                        Reporting_read_ini().get_end_date_calender_box_by_xpath())
            time.sleep(web_driver.one_second)
            if end_date_calender_box.is_displayed():
                time.sleep(web_driver.one_second)
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
            time.sleep(web_driver.one_second)
            if end_date_checkbox.is_displayed():
                time.sleep(web_driver.one_second)
                self.logger.info("End date checkbox is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if end_date_checkbox.is_enabled():
                time.sleep(web_driver.one_second)
                self.logger.info("End date checkbox is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_128.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_128.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_128_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_128_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_128 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_129 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            self.select_number_of_enrollments_by_zone()
            time.sleep(web_driver.one_second)
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            time.sleep(web_driver.one_second)
            start_date_calender_box = self.d.find_element(By.XPATH,
                                                          Reporting_read_ini().get_start_date_calender_box_by_xpath())
            time.sleep(web_driver.one_second)
            start_calender_disabled_status = start_date_calender_box.get_attribute("disabled")
            time.sleep(web_driver.one_second)
            if start_date_checkbox.is_selected():
                time.sleep(web_driver.one_second)
                start_date_checkbox.click()
                time.sleep(web_driver.one_second)
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
            time.sleep(web_driver.one_second)
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
                time.sleep(web_driver.one_second)
            else:
                pass
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_129.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_129.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_129_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_129_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_129 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_130 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            self.select_number_of_enrollments_by_zone()
            time.sleep(web_driver.one_second)
            end_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_end_date_calender_box_by_xpath())
            time.sleep(web_driver.one_second)
            end_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_end_date_checkbox_by_xpath())
            time.sleep(web_driver.one_second)
            end_calender_disabled_status = end_date_calender_box.get_attribute("disabled")
            time.sleep(web_driver.one_second)
            if end_date_checkbox.is_selected():
                time.sleep(web_driver.one_second)
                end_date_checkbox.click()
                time.sleep(web_driver.one_second)
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
            time.sleep(web_driver.one_second)
            self.logger.info(f"End calender disable status after click: "
                             f"{end_date_calender_box.get_attribute('disabled')}")
            if end_date_calender_box.get_attribute("disabled") is None:
                self.logger.info("End calender enabled !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            if end_date_checkbox.is_selected():
                time.sleep(web_driver.one_second)
                end_date_checkbox.click()
                time.sleep(web_driver.one_second)
            else:
                pass
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_130.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_130.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_130_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_130_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_130 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_131 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            self.select_number_of_enrollments_by_zone()
            time.sleep(web_driver.one_second)
            action = ActionChains(self.d)
            time.sleep(web_driver.one_second)
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            time.sleep(web_driver.one_second)
            start_checkbox_hover = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                       get_include_in_search_hover_on_start_checkbox_by_xpath())
            time.sleep(web_driver.one_second)
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
            time.sleep(web_driver.one_second)
            if end_checkbox_hover.get_attribute("aria-describedby"):
                self.logger.info("'Include In Search' hover is visible for end date checkbox !!")
                self.status.append(True)
            else:
                self.logger.error("'Include In Search' hover is not visible for end date checkbox !!")
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_131.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_131.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_131_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_131_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_131 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_verify_Optional_Filter_text_is_visible_text_beside_Select_group_filter_button_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_132 started **********")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            self.select_number_of_enrollments_by_zone()
            time.sleep(web_driver.one_second)
            actual_optional_filter_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                              get_optional_filters_text_by_xpath()).text
            time.sleep(web_driver.one_second)
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_132.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_132.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_132_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_132_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_132 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_verify_Select_group_filter_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_133 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            self.select_number_of_enrollments_by_zone()
            time.sleep(web_driver.one_second)
            select_group_filter_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                             get_select_group_filter_button_by_xpath())
            time.sleep(web_driver.one_second)
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
            actual_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                              get_select_group_filter_text_on_button_by_xpath()).text
            time.sleep(web_driver.one_second)
            self.logger.info(f"actual text on Select group filter button: {actual_text}")
            expected_text = Reporting_read_ini().get_expected_text_on_select_group_filter_button()
            time.sleep(web_driver.one_second)
            self.logger.info(f"expected text on Select group filter button: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            group_icon_on_select_grp_btn = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                               get_group_icon_on_select_group_filter_button_by_xpath())
            time.sleep(web_driver.one_second)
            if group_icon_on_select_grp_btn.is_displayed():
                self.logger.info("group icon on Select group filter button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_133.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_133.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_133_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_133_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_133 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_verify_Generate_Report_button_is_visible_and_clickable_text_and_chart_icon_on_button_are_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_134 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            self.select_number_of_enrollments_by_zone()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            generate_report_button = self.d.find_element(By.XPATH,
                                                         Reporting_read_ini().get_generate_report_button_by_xpath())
            time.sleep(web_driver.one_second)
            if generate_report_button.is_displayed():
                time.sleep(web_driver.one_second)
                self.logger.info("Generate report button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if generate_report_button.is_enabled():
                time.sleep(web_driver.one_second)
                self.logger.info("Generate report button is clickable !!")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_chart_icon_on_generate_report_button_by_xpath()).\
                    is_displayed():
                time.sleep(web_driver.one_second)
                self.logger.info("chart icon on Generate report button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text_on_generate_report_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_text_on_button_by_xpath()).text
            time.sleep(web_driver.one_second)
            self.logger.info(f"actual text on Generate report button: {actual_text_on_generate_report_button}")
            expected_text_on_generate_report_button = Reporting_read_ini().get_expected_generate_report_text_on_button()
            time.sleep(web_driver.one_second)
            self.logger.info(f"expected text on Generate report button: {expected_text_on_generate_report_button}")
            if actual_text_on_generate_report_button == expected_text_on_generate_report_button:
                time.sleep(web_driver.one_second)
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_134.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_134.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_134_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_134_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_134 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_in_Select_group_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_135 started **********")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            self.select_number_of_enrollments_by_zone()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            actual_horizontal_line_below_reporting_panel_heading = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_horizontal_line_below_reporting_panel_heading_for_group_by_xpath()).text
            time.sleep(web_driver.one_second)
            self.logger.info(f"actual horizontal line below panel heading: "
                             f"{actual_horizontal_line_below_reporting_panel_heading}")
            expected_horizontal_line_below_reporting_panel_heading = Reporting_read_ini(). \
                get_expected_horizontal_line_below_reporting_panel_heading_for_group()
            time.sleep(web_driver.one_second)
            self.logger.info(f"expected horizontal line below panel heading: "
                             f"{expected_horizontal_line_below_reporting_panel_heading}")
            if actual_horizontal_line_below_reporting_panel_heading == \
                    expected_horizontal_line_below_reporting_panel_heading:
                time.sleep(web_driver.one_second)
                self.logger.info("Horizontal line below panel heading is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_135.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_135.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_135_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_135_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_135 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_verify_filter_group_list_below_textbox_is_visible_and_clickable_label_on_textbox_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_136 started **********")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            time.sleep(web_driver.one_second)
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_enrollments_by_zone()
                time.sleep(web_driver.one_second)
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            filter_group_list_textbox = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                            get_filter_group_list_textbox_by_xpath())
            if filter_group_list_textbox.is_displayed():
                time.sleep(web_driver.one_second)
                self.logger.info("'filter group list below..' textbox is visible")
                self.status.append(True)
            else:
                self.status.append(False)
            if filter_group_list_textbox.is_enabled():
                time.sleep(web_driver.one_second)
                self.logger.info("'filter group list below..' textbox is clickable")
                self.status.append(True)
            else:
                self.status.append(False)
            filter_group_list_textbox.click()
            time.sleep(web_driver.one_second)
            actual_label_on_textbox = filter_group_list_textbox.get_attribute('placeholder')
            self.logger.info(f"actual label on textbox: {actual_label_on_textbox}")
            time.sleep(web_driver.one_second)
            expected_label_on_textbox = Reporting_read_ini().get_expected_label_on_filter_group_list_below_textbox()
            self.logger.info(f"expected label on textbox: {expected_label_on_textbox}")
            if actual_label_on_textbox == expected_label_on_textbox:
                time.sleep(web_driver.one_second)
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_136.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_136.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_136_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_136_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_136 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_verify_group_list_below_filter_group_list_textbox_is_visible_and_clickable(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_137 started **********")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_enrollments_by_zone()
                time.sleep(web_driver.one_second)
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                    get_group_items_list_below_filter_group_list_textbox())
            self.logger.info(f"Group items below 'filter group list' textbox: {len(group_items_list)}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH,
                                Reporting_read_ini().get_enrollment_groups_module_on_dashboard_by_xpath()).click()
            time.sleep(web_driver.three_second)
            actual_group_list_items = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                           get_group_item_list_from_enrollment_group_panel_by_xpath())
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
            self.close_reporting_module()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_137.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_137.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_137_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_137_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_137 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_verify_select_all_button_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_138 started **********")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            time.sleep(web_driver.one_second)
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_enrollments_by_zone()
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
            time.sleep(web_driver.one_second)
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
            time.sleep(web_driver.one_second)
            if actual_text_on_select_all_button == Reporting_read_ini().get_expected_text_on_select_all_button():
                self.logger.info("text on Select all button is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_138.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_138.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_138_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_138_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_138 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_verify_selected_group_list_title_and_default_text_below_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_139 started **********")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            time.sleep(web_driver.one_second)
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_enrollments_by_zone()
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
            time.sleep(web_driver.one_second)
            actual_first_horizontal_line = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_first_default_te_below_selected_group_list_title_by_xpath()).text
            self.logger.info(f"actual first horizontal line: {actual_first_horizontal_line}")
            expected_first_horizontal_line = \
                Reporting_read_ini().get_expected_first_default_text_line_below_selected_group_list_title()
            self.logger.info(f"expected first horizontal line: {expected_first_horizontal_line}")
            time.sleep(web_driver.one_second)
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
            time.sleep(web_driver.one_second)
            if actual_second_horizontal_line == expected_second_horizontal_line:
                self.logger.info("Second default text line below selected group list title is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_139.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_139.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_139_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_139_exception.png")
            self.logger.error(f"TC_Reporting_EV_ZN_139 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_verify_close_group_menu_button_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_140 started **********")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_enrollments_by_zone()
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
            time.sleep(web_driver.one_second)
            if close_group_menu_button.is_enabled():
                self.logger.info("'Close group menu' button is enabled !!")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_text_on_close_group_menu_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_text_on_close_group_menu_button_by_xpath()).text
            self.logger.info(f"actual text on close menu btn: {actual_text_on_close_group_menu_button}")
            expected_text_on_close_group_button = Reporting_read_ini().get_expected_text_on_close_group_menu_button()
            self.logger.info(f"expected text on close menu btn: {expected_text_on_close_group_button}")
            time.sleep(web_driver.one_second)
            if actual_text_on_close_group_menu_button == expected_text_on_close_group_button:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            # self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_140.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_140.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_140_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_140_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_140 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_click_on_select_all_button_and_verify_all_selected_groups_are_visible_in_selected_group_list(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_141 started **********")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            time.sleep(web_driver.one_second)
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_enrollments_by_zone()
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
            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_group_by_xpath()).\
                click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_141.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_141.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_141_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_141_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_141 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_click_on_select_all_button_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_142 started **********")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            time.sleep(web_driver.one_second)
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_enrollments_by_zone()
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
            time.sleep(web_driver.one_second)
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
            time.sleep(web_driver.one_second)
            if actual_text_on_button == Reporting_read_ini().get_expected_clear_all_text():
                self.logger.info("text on 'Clear all' button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_group_by_xpath()).\
                click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_142.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_142.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_142_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_142_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_142 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_click_on_select_all_button_and_verify_save_group_selection_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_143 started **********")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            time.sleep(web_driver.one_second)
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_enrollments_by_zone()
                time.sleep(web_driver.one_second)
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath()).click()
            time.sleep(web_driver.one_second)
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_143.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_143.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_143_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_143_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_143 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_select_one_group_from_group_list_and_verify_selected_group_is_visible_in_selected_group_list_verify_save_group_selection_button_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_144 started **********")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_enrollments_by_zone()
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            group_list = \
                self.d.find_elements(By.XPATH, Reporting_read_ini().
                                     get_group_items_list_below_filter_group_list_textbox())
            first_group_name = group_list[0].text
            group_list[0].click()
            self.logger.info("Selected first group from group list...")
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_144.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_144.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_144_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_144_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_144 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_click_on_save_group_selection_button_with_at_least_one_group_selected_and_verify_View_and_edit_groups_button_is_visible_and_clickable(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_145 started **********")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.load_reporting_module()
            time.sleep(web_driver.one_second)
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_enrollments_by_zone()
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)

            group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                              get_group_items_list_below_filter_group_list_textbox())
            group_list[0].click()
            time.sleep(web_driver.one_second)
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_145.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_145.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_145_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_145_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_145 got exception as: {ex}")

    def for_number_of_enrollments_by_zone_verify_text_and_numeric_value_of_number_of_selected_groups_on_view_and_edit_groups_button_are_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_146 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_enrollments_by_zone()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_146.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_146.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_146_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_146_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_146 got exception as: {ex}")

    def select_number_of_zones_by_enrollment(self):
        try:
            self.status.clear()
            time.sleep(web_driver.one_second)
            field1 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath())
            field2 = self.d.find_element(By.XPATH, Reporting_read_ini().get_field2_dropdown_for_zones_by_xpath())
            if field2.is_displayed():
                pass
            else:
                field1_dropdown = Select(field1)
                field1_dropdown.select_by_visible_text('number of zones')
                time.sleep(web_driver.one_second)
                field2_dropdown = Select(field2)
                field2_dropdown.select_by_visible_text('enrollment')
                time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def for_number_of_zones_by_enrollment_verify_number_of_zones_from_report_field1_and_enrollment_from_report_field2_texts_are_visible_on_dropdown(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_158 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            field1 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()))
            time.sleep(web_driver.one_second)
            field1.select_by_visible_text('number of zones')
            time.sleep(web_driver.one_second)
            value1 = self.d.find_element(By.XPATH, Reporting_read_ini().get_report_field1_dropdown_by_xpath()). \
                get_attribute('value')
            self.logger.info(f"Value1: {value1}")
            if Reporting_read_ini().get_expected_fourth_text_from_field1() in value1:
                self.logger.info("Selected 'number of zones' from report field1 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)
            field2 = Select(self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_field2_dropdown_for_zones_by_xpath()))
            time.sleep(web_driver.one_second)
            field2.select_by_visible_text('enrollment')
            value2 = self.d.find_element(By.XPATH, Reporting_read_ini().get_field2_dropdown_for_zones_by_xpath()). \
                get_attribute('value')
            self.logger.info(f"Value2: {value2}")
            if Reporting_read_ini().get_expected_value_for_zones_by_enrollment_from_field2() in value2:
                self.logger.info("Selected 'enrollment' from report field2 dropdown...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_158.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_158.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_158_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_158_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_158 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_Date_and_Time_Range_text_to_text_and_horizontal_text_line_below_calender_box_are_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_159 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_zones_by_enrollment()
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
            expected_horizontal_line_below_calenders = Reporting_read_ini().\
                get_expected_horizontal_line_below_calenders()
            self.logger.info(f"expected horizontal line below calenders: {expected_horizontal_line_below_calenders}")
            if actual_horizontal_line_below_calenders == expected_horizontal_line_below_calenders:
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_159.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_159.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_159_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_159_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_159 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_start_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_160 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_zones_by_enrollment()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_160.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_160.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_160_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_160_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_160 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_end_date_calender_box_and_checkbox_beside_it_are_visible_and_clickable(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_161 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_zones_by_enrollment()
            end_date_calender_box = self.d.find_element(By.XPATH,
                                                        Reporting_read_ini().get_end_date_calender_box_by_xpath())
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_161.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_161.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_161_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_161_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_161 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_start_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_162 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_zones_by_enrollment()
            start_date_checkbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_checkbox_by_xpath())
            start_date_calender_box = \
                self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_calender_box_by_xpath())
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_162.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_162.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_162_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_162_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_162 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_end_date_calender_box_enable_and_disable_status_with_check_box_selected_and_without_check_box_selected(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_163 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_zones_by_enrollment()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_163.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_163.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_163_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_163_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_163 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_hover_text_on_start_date_checkbox_and_end_date_checkbox(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_164 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_zones_by_enrollment()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_164.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_164.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_164_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_164_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_164 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_Optional_Filter_text_is_visible_text_beside_Select_group_filter_button_and_that_of_Select_zone_filter_button_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_165 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_zones_by_enrollment()
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
            actual_text_beside_group_filter_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_text_beside_select_group_filter_button_by_xpath()).text
            self.logger.info(f"actual text beside group filter button: {actual_text_beside_group_filter_button}")
            expected_text_beside_group_filter_btn = Reporting_read_ini().\
                get_expected_text_beside_select_group_filter_button()
            self.logger.info(f"expected text: {expected_text_beside_group_filter_btn}")
            if actual_text_beside_group_filter_button == expected_text_beside_group_filter_btn:
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_165.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_165.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_165_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_165_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_165 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_Select_group_filter_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_166 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_zones_by_enrollment()
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
            actual_text = self.d.find_element(By.XPATH, Reporting_read_ini().
                                              get_select_group_filter_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on Select group filter button: {actual_text}")
            expected_text = Reporting_read_ini().get_expected_text_on_select_group_filter_button()
            self.logger.info(f"expected text on Select group filter button: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            group_icon_on_select_grp_btn = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                               get_group_icon_on_select_group_filter_button_by_xpath())
            if group_icon_on_select_grp_btn.is_displayed():
                self.logger.info("group icon on Select group filter button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_166.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_166.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_166_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_166_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_166 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_Select_zone_filter_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_167 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_zones_by_enrollment()
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
            actual_text_on_select_zone_button = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_select_zone_filter_text_on_button_by_xpath()).text
            self.logger.info(f"actual text on 'Select zone filter' button: {actual_text_on_select_zone_button}")
            expected_text_on_select_zone_button = Reporting_read_ini().get_expected_text_on_select_zone_filter_button()
            self.logger.info(f"expected text on 'Select zone filter' button: {expected_text_on_select_zone_button}")
            if actual_text_on_select_zone_button == expected_text_on_select_zone_button:
                self.logger.info(" text on select zone button is visible !!!")
                self.status.append(True)
            else:
                self.status.append(False)
            if self.d.find_element(By.XPATH,
                                   Reporting_read_ini().get_dot_circle_icon_for_zone_by_xpath()).is_displayed():
                self.logger.info(" dot circle zone icon on button is visible !!!")
                self.status.append(True)
            else:
                self.status.append(False)

            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_167.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_167.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_167_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_167_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_167 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_Generate_Report_button_is_visible_and_clickable_text_and_chart_icon_on_button_are_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_168 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_zones_by_enrollment()
            generate_report_button = self.d.find_element(By.XPATH,
                                                         Reporting_read_ini().get_generate_report_button_by_xpath())
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_168.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_168.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_168_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_168_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_168 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_in_Select_group_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_169 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_zones_by_enrollment()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_169.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_169.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_169_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_169_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_169 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_filter_group_list_below_textbox_is_visible_and_clickable_label_on_textbox_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_170 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_zones_by_enrollment()
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_170.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_170.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_170_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_170_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_170 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_group_list_below_filter_group_list_textbox_is_visible_and_clickable(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_171 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_zones_by_enrollment()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_171.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_171.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_171_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_171_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_171 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_select_all_button_in_group_filter_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_172 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_zones_by_enrollment()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_172.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_172.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_172_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_172_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_172 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_selected_group_list_title_and_default_text_below_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_173 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_zones_by_enrollment()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_173.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_173.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_173_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_173_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_173 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_close_group_menu_button_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_174 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_zones_by_enrollment()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_174.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_174.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_174_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_174_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_174 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_click_on_select_all_button_and_verify_all_selected_groups_are_visible_in_selected_group_list(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_175 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_zones_by_enrollment()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_175.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_175.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_175_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_175_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_175 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_click_on_select_all_button_in_group_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_176 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_zones_by_enrollment()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_176.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_176.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_176_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_176_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_176 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_click_on_select_all_button_and_verify_save_group_selection_button_is_visible_and_clickable_text_and_group_icon_on_button_are_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_177 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_zones_by_enrollment()
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
                                   Reporting_read_ini().get_group_icon_on_save_group_selection_button_by_xpath()). \
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_177.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_177.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_177_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_177_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_177 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_select_one_group_from_group_list_and_verify_selected_group_is_visible_in_selected_group_list_verify_save_group_selection_button_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_178 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_zones_by_enrollment()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_178.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_178.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_178_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_178_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_178 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_click_on_save_group_selection_button_with_at_least_one_group_selected_and_verify_View_and_edit_groups_button_is_visible_and_clickable(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_179 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_group_menu = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                   get_close_group_menu_button_by_xpath())
            if close_group_menu.is_displayed():
                pass
            else:
                self.select_number_of_zones_by_enrollment()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_179.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_179.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_179_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_179_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_179 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_text_and_numeric_value_of_number_of_selected_groups_on_view_and_edit_groups_button_are_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_180 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_zones_by_enrollment()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_180.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_180.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_180_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_180_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_180 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_in_select_zone_filter_verify_horizontal_line_below_reporting_panel_heading_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_181 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_zones_by_enrollment()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_181.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_181.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_181_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_181_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_181 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_search_zones_textbox_is_visible_and_clickable_label_on_it_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_182 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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

            actual_label_on_search_zone_textbox = \
                self.d.find_element(By.XPATH, Reporting_read_ini().
                                    get_search_zone_textbox_by_xpath()).get_attribute("placeholder")
            self.logger.info(f"actual label on search zone textbox: {actual_label_on_search_zone_textbox}")
            expected_label_on_search_zone_textbox = Reporting_read_ini().get_expected_label_on_search_zone_textbox()
            self.logger.info(f"expected label on search zone textbox: {expected_label_on_search_zone_textbox}")
            if actual_label_on_search_zone_textbox == expected_label_on_search_zone_textbox:
                self.logger.info("'Search zone...' label on textbox is visible !!")
                self.status.append(True)
            else:
                self.status.append(False)
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_182.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_182.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_182_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_182_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_182 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_zone_list_below_search_zones_textbox_is_visible_and_clickable(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_183 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
                self.d.find_element(By.XPATH, Reporting_read_ini().get_select_zone_filter_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            self.logger.info(f"Zone items below 'Search zone' textbox: {len(zone_items_list)}")
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_zone_module_on_dashboard_by_xpath()).click()
            time.sleep(web_driver.two_second)
            actual_zone_item_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                         get_zone_item_list_from_zone_panel_by_xpath())
            WebDriverWait(self.d, 30).until(EC.presence_of_element_located((By.XPATH, Reporting_read_ini().
                                                                            get_zone_item_list_from_zone_panel_by_xpath())))
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_183.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_183.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_183_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_183_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_183 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_select_all_button_in_zone_filter_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_184 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_184.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_184.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_184_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_184_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_184 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_selected_zone_list_title_and_default_text_below_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_185 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_185.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_185.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_185_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_185_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_185 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_close_zone_menu_button_is_visible_and_clickable_and_text_on_it_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_186 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_186.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_186.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_186_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_186_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_186 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_click_on_select_all_button_and_verify_all_selected_zones_are_visible_in_selected_zone_list(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_187 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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

            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_zone_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_187.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_187.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_187_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_187_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_187 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_click_on_select_all_button_in_zone_filter_and_verify_clear_all_button_is_visible_and_clickable_text_on_button_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_188 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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

            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_zone_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_188.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_188.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_188_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_188_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_188 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_click_on_select_all_button_and_verify_save_zone_selection_button_is_visible_and_clickable_text_and_dot_circle_icon_on_button_are_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_189 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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
            if self.d.find_element(By.XPATH, Reporting_read_ini().get_dot_circle_icon_on_save_zone_selection_button()). \
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

            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_zone_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_189.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_189.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_189_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_189_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_189 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_select_one_zone_from_zone_list_and_verify_selected_zone_is_visible_in_selected_zone_list_verify_save_zone_selection_button_is_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_190 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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

            self.d.find_element(By.XPATH, Reporting_read_ini().get_clear_all_button_on_selected_zone_by_xpath()).click()
            # time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_190.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_190.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_190_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_190_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_190 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_click_on_save_zone_selection_button_with_at_least_one_zone_selected_and_verify_View_and_edit_zones_button_is_visible_and_clickable(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_191 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            close_zone_menu = self.d.find_element(By.XPATH, Reporting_read_ini().get_close_zone_menu_button_by_xpath())
            if close_zone_menu.is_displayed():
                pass
            else:
                self.select_number_of_visitors_by_hour_of_week()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_191.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_191.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_191_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_191_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_191 got exception as: {ex}")

    def for_number_of_zones_by_enrollment_verify_text_and_numeric_value_of_number_of_selected_zones_on_view_and_edit_zones_button_are_visible(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_192 started **********")
            login().login_to_cloud_if_not_done(self.d)
            self.load_reporting_module()
            self.select_number_of_zones_by_enrollment()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_192.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_192.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_192_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_192_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_192 got exception as: {ex}")

    def verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_and_with_group_selected_as_SOE(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_147 started **********")
            self.load_reporting_module_for_admin()
            time.sleep(web_driver.one_second)
            self.select_number_of_enrollments_by_zone()
            time.sleep(web_driver.one_second)
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
                    time.sleep(web_driver.one_second)
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_soe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            self.logger.info("Clicked on Generate report button")
            time.sleep(web_driver.two_second)
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_147.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_147.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_147_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_147_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_147 got exception as: {ex}")

    def verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_and_with_group_selected_as_ABE(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_148 started **********")
            self.load_reporting_module_for_admin()
            time.sleep(web_driver.one_second)
            self.select_number_of_enrollments_by_zone()
            time.sleep(web_driver.one_second)
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
                    time.sleep(web_driver.one_second)
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_abe_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            self.logger.info("Clicked on Generate report button")
            time.sleep(web_driver.two_second)
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_148.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_148.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_148_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_148_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_148 got exception as: {ex}")

    def verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_and_with_group_selected_as_PTE(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_149 started **********")
            self.load_reporting_module_for_admin()
            time.sleep(web_driver.one_second)
            self.select_number_of_enrollments_by_zone()
            time.sleep(web_driver.one_second)
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
                    time.sleep(web_driver.one_second)
                    self.logger.info(f"Selected group as: {Reporting_read_ini().get_pte_enrollment_group()}")
                    self.status.append(True)
                    break
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            self.logger.info("Clicked on Generate report button")
            time.sleep(web_driver.two_second)
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_149.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_149.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_149_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_149_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_149 got exception as: {ex}")

    def verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_and_with_group_selected_as_FRAUDE(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_150 started **********")
            self.load_reporting_module_for_admin()
            time.sleep(web_driver.one_second)
            self.select_number_of_enrollments_by_zone()
            time.sleep(web_driver.one_second)
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
            self.logger.info("Clicked on Generate report button")
            time.sleep(web_driver.two_second)
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_150.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_150.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_150_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_150_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_150 got exception as: {ex}")

    def verify_report_for_number_of_enrollments_by_zone_with_default_dates_1_month_and_with_group_selected_as_VIPE(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_151 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_enrollments_by_zone()
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
            self.logger.info("Clicked on Generate report button")
            time.sleep(web_driver.two_second)
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_151.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_151.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_151_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_151_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_151 got exception as: {ex}")

    def get_start_date(self):
        try:

            self.get_date_range_from_json()
            time.sleep(web_driver.one_second)
            start_date_calender_box = self.d.find_element(By.XPATH, Reporting_read_ini().get_start_date_calender_box_by_xpath())
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
                        self.logger.info(F"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
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
                        self.logger.info(F"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
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
                            self.logger.info(F"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
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
                            self.logger.info(F"Start date selected as:- {input_s_date}/{input_s_month}/{input_s_year}")
                            status = False
                else:
                    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        except Exception as ex:
            self.logger.error("start date method exception")
            self.logger.error(ex)

    def get_end_date(self):
        try:
            self.get_date_range_from_json()
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

    def verify_report_for_number_of_enrollments_by_zone_with_date_range_from_json_file_with_group_selected_as_SOE(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_152 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_enrollments_by_zone()
            # self.get_age_range()
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
            self.logger.info("Clicked on Generate report button")
            time.sleep(web_driver.two_second)
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_152.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_152.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_152_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_152_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_152 got exception as: {ex}")

    def verify_report_for_number_of_enrollments_by_zone_with_date_range_from_json_file_with_group_selected_as_ABE(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_153 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_enrollments_by_zone()
            # self.get_age_range()
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
            self.logger.info("Clicked on Generate report button")
            time.sleep(web_driver.two_second)
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_153.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_153.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_153_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_153_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_153 got exception as: {ex}")

    def verify_report_for_number_of_enrollments_by_zone_with_date_range_from_json_file_with_group_selected_as_PTE(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_154 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_enrollments_by_zone()
            # self.get_age_range()
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
            self.logger.info("Clicked on Generate report button")
            time.sleep(web_driver.two_second)
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_154.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_154.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_154_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_154_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_154 got exception as: {ex}")

    def verify_report_for_number_of_enrollments_by_zone_with_date_range_from_json_file_with_group_selected_as_FRAUDE(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_155 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_enrollments_by_zone()
            # self.get_age_range()
            self.get_start_date()
            self.get_end_date()
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on 'Select group filter' button..")
            # time.sleep(web_driver.one_second)
            # group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
            #                                   get_group_items_list_below_filter_group_list_textbox())
            # time.sleep(web_driver.one_second)
            # for items in group_list:
            #     if items.text == self.groups[3]:
            #         items.click()
            #         self.logger.info(f"Selected group as: {self.groups[3]}")
            #         self.status.append(True)
            #         break
            time.sleep(web_driver.one_second)
            select_all_groups_btn = self.d.find_element(By.XPATH, Reporting_read_ini().get_select_all_button_in_group_filter_by_xpath())
            select_all_groups_btn.click()
            self.logger.info("clicked on select all")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
            time.sleep(web_driver.two_second)

            self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
            self.logger.info("Clicked on Generate report button")
            time.sleep(web_driver.two_second)
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_155.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_155.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_155_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_155_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_155 got exception as: {ex}")

    def verify_report_for_number_of_enrollments_by_zone_with_date_range_from_json_file_with_group_selected_as_VIPE(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_156 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_enrollments_by_zone()
            # self.get_age_range()
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
            self.logger.info("Clicked on Generate report button")
            time.sleep(web_driver.two_second)
            new_reporting_panel = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                      get_new_reporting_panel_heading())
            time.sleep(web_driver.one_second)
            if new_reporting_panel.is_displayed():
                self.logger.info(f"title on the report panel:- {new_reporting_panel.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_156.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_156.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_156_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_156_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_156 got exception as: {ex}")

    def verify_individual_report_for_number_of_enrollments_by_zone_with_date_range_from_json_file_with_group_selected_as_SOE_ABE_PTE_FRAUDE_and_VIPE(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_EN_ZN_157 started **********")
            self.load_reporting_module_for_admin()
            self.logger.info("executed load_reporting_module_for_admin")
            web_driver.implicit_wait(self, 10, self.d)
            self.select_number_of_enrollments_by_zone()
            self.logger.info("executed select_number_of_enrollments_by_zone")
            # self.get_age_range()
            self.logger.info("executed get_age_range")
            self.get_start_date()
            self.logger.info("executed get_start_date")
            self.get_end_date()
            self.logger.info("executed get_end_date")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.logger.info("Clicked on get_select_group_filter_button_by_xpath..")
            time.sleep(web_driver.one_second)
            self.groups_list = [Reporting_read_ini().get_abe_enrollment_group(),
                                Reporting_read_ini().get_soe_enrollment_group(),
                                Reporting_read_ini().get_pte_enrollment_group(),
                                Reporting_read_ini().get_fraude_enrollment_group(),
                                Reporting_read_ini().get_vipe_enrollment_group()]

            for i in range(len(self.groups_list)):
                time.sleep(web_driver.one_second)
                group_filter_textbox = self.d.find_element(By.XPATH, Reporting_read_ini().get_filter_group_list_textbox_by_xpath())
                group_filter_textbox.click()
                self.logger.info("Clicked on get_filter_group_list_textbox_by_xpath...")
                group_filter_textbox.send_keys(self.groups_list[i])
                group_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                  get_group_items_list_below_filter_group_list_textbox())

                for items in group_list:
                    if items.text.upper() == self.groups_list[i].upper():
                        items.click()
                        self.logger.info(f"Selected group as: {self.groups_list[i]}")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
                        self.logger.info("Clicked on get_generate_report_button_by_xpath..")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Reporting_read_ini().get_generate_report_button_by_xpath()).click()
                        time.sleep(web_driver.one_second)
                        self.logger.info("Clicked on generate report button...")
                        self.d.find_element(By.XPATH, Reporting_read_ini().
                                            get_view_and_edit_groups_button_by_xpath()).click()
                        self.logger.info("Clicked on get_view_and_edit_groups_button_by_xpath..")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH, Reporting_read_ini().
                                            get_clear_all_button_on_selected_group_by_xpath()).click()
                        self.logger.info("Clicked on get_clear_all_button_on_selected_group_by_xpath..")
                        self.status.append(True)
                        time.sleep(web_driver.one_second)

            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_157.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_157.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_EN_ZN_157_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_EN_ZN_157_exception.png")
            self.logger.error(f"TC_Reporting_EN_ZN_157 got exception as: {ex}")

    def verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_193 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_zones_by_enrollment()
            # self.get_age_range()
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
            self.zones = Reporting_read_ini().get_all_zones().split(',')
            self.explicit_wait(5, "XPATH", Reporting_read_ini().get_zone_items_list_below_search_zone_textbox_by_xpath(), self.d)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().get_zone_items_list_below_search_zone_textbox_by_xpath())
            self.logger.info(f"expected zone list: {self.zones}")

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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_193.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_193.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_193_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_193_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_193 got exception as: {ex}")

    def verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_194 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_zones_by_enrollment()
            # self.get_age_range()
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
            self.logger.info(f"expected zones: {self.zones}")
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_194.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_194.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_194_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_194_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_194 got exception as: {ex}")

    def verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_195 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_zones_by_enrollment()
            # self.get_age_range()
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
            self.logger.info(f"expected zones: {self.zones}")
            time.sleep(web_driver.one_second)
            zone_items_list = self.d.find_elements(By.XPATH, Reporting_read_ini().
                                                   get_zone_items_list_below_search_zone_textbox_by_xpath())
            zones = []
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_195.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_195.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_195_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_195_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_195 got exception as: {ex}")

    def verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_196 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_zones_by_enrollment()
            # self.get_age_range()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_196.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_196.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_196_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_196_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_196 got exception as: {ex}")

    def verify_report_for_number_of_zones_by_enrollment_with_default_dates_last_1_month_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_197 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_zones_by_enrollment()
            # self.get_age_range()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_197.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_197.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_197_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_197_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_197 got exception as: {ex}")

    def verify_report_for_number_of_zones_by_enrollment_with_date_range_from_json_file_and_with_group_selected_as_ABE_and_zone_selected_as_All_devices(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_198 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_zones_by_enrollment()
            # self.get_age_range()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_198.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_198.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_198_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_198_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_198 got exception as: {ex}")

    def verify_report_for_number_of_zones_by_enrollment_with_date_range_from_json_file_and_with_group_selected_as_PTE_and_zone_selected_as_All_devices(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_199 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_zones_by_enrollment()
            # self.get_age_range()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_199.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_199.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_199_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_199_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_199 got exception as: {ex}")

    def verify_report_for_number_of_zones_by_enrollment_with_date_range_from_json_file_and_with_group_selected_as_SOE_and_zone_selected_as_All_devices(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_200 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_zones_by_enrollment()
            # self.get_age_range()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_200.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_200.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_200_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_200_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_200 got exception as: {ex}")

    def verify_report_for_number_of_zones_by_enrollment_with_date_range_from_json_file_and_with_group_selected_as_VIPE_and_zone_selected_as_All_devices(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_201 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_zones_by_enrollment()
            # self.get_age_range()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_201.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_201.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_201_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_201_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_201 got exception as: {ex}")

    def verify_report_for_number_of_zones_by_enrollment_with_date_range_from_json_file_and_with_group_selected_as_FRAUDE_and_zone_selected_as_All_devices(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_202 started **********")
            self.load_reporting_module_for_admin()
            self.select_number_of_zones_by_enrollment()
            # self.get_age_range()
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
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_202.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_202.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_202_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_202_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_202 got exception as: {ex}")

    def verify_individual_report_for_number_of_zones_by_enrollment_with_date_range_from_json_file_and_with_groups_as_SOE_ABE_PTE_FRAUDE_VIPE_and_zone_selected_as_All_devices(self):
        try:
            self.status.clear()
            self.logger.info("*********** TC_Reporting_ZN_EN_203 started **********")
            self.load_reporting_module_for_admin()
            self.logger.info("executed load_reporting_module_for_admin")
            self.select_number_of_zones_by_enrollment()
            self.logger.info("executed select_number_of_zones_by_enrollment")
            # self.get_age_range()
            self.logger.info("executed get_age_range")
            self.get_start_date()
            self.logger.info("executed get_start_date")
            self.get_end_date()
            self.logger.info("executed get_end_date")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Reporting_read_ini().get_select_group_filter_button_by_xpath()).click()
            self.zone_list = [Reporting_read_ini().get_zones()]
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
                    if items.text == self.groups_list[i]:
                        time.sleep(web_driver.one_second)
                        items.click()
                        self.logger.info(f"Selected group as: {self.groups_list[i]}")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Reporting_read_ini().get_save_group_selection_button_by_xpath()).click()
                        time.sleep(web_driver.one_second)
                        self.logger.info("clicked on save_group_selection_button_by_xpath")
                        view_and_edit_zones_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                         get_view_and_edit_zones_button_by_xpath())
                        self.logger.info(f"view_and_edit_zones_button display: {view_and_edit_zones_button.is_displayed()}")
                        if view_and_edit_zones_button.is_displayed():
                            view_and_edit_zones_button.click()
                            self.d.find_element(By.XPATH, Reporting_read_ini().
                                                get_clear_all_button_on_selected_zone_by_xpath()).click()
                        else:
                            pass
                        select_zone_filter_button = self.d.find_element(By.XPATH, Reporting_read_ini().
                                                                        get_select_zone_filter_button_by_xpath())
                        self.logger.info(f"select_zone_filter_button display: {select_zone_filter_button.is_displayed()}")
                        if select_zone_filter_button.is_displayed():
                            select_zone_filter_button.click()
                        else:
                            pass
                        # self.zone_list = (Reporting_read_ini().get_zones()).split(',')
                        # self.logger.info(f"zone list: {self.zone_list}")

                        for j in range(len(self.zone_list)):
                            time.sleep(web_driver.one_second)
                            self.d.find_element(By.XPATH, Reporting_read_ini().get_search_zone_textbox_by_xpath()). \
                                send_keys(self.zone_list[j])
                            zone_list = self.d.find_elements(By.XPATH, Reporting_read_ini().get_zone_items_list_below_search_zone_textbox_by_xpath())
                            for Items in zone_list:
                                if Items.text.upper() == self.zone_list[j].upper():
                                    time.sleep(web_driver.one_second)
                                    Items.click()
                                    self.logger.info(f"Selected zone as: {self.zone_list[j]}")
                                    time.sleep(web_driver.one_second)
                                    self.d.find_element(By.XPATH, Reporting_read_ini().
                                                        get_save_zone_selection_button_by_xpath()).click()
                                    self.logger.info("clicked on save_zone_selection_button_by_xpath")
                                    time.sleep(web_driver.one_second)

                        self.d.find_element(By.XPATH, Reporting_read_ini().get_generate_report_button_by_xpath()).click()
                        # generate_report_btn = web_driver.explicit_wait(self, 10, "XPATH", Reporting_read_ini().get_generate_report_button_by_xpath(), self.d)
                        # generate_report_btn.click()
                        self.logger.info("Clicked on Generate report button...")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH,
                                            Reporting_read_ini().get_view_and_edit_groups_button_by_xpath()).click()
                        self.logger.info("clicked on view_and_edit_groups_button_by_xpath")
                        time.sleep(web_driver.one_second)
                        self.d.find_element(By.XPATH, Reporting_read_ini().
                                            get_clear_all_button_on_selected_group_by_xpath()).click()
                        self.logger.info("Clicked on clear_all_button_on_selected_group_by_xpath")
                        self.status.append(True)
                        time.sleep(web_driver.one_second)

            time.sleep(web_driver.one_second)
            self.close_reporting_module()
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_203.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_203.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_Reporting_ZN_EN_203_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_Reporting_ZN_EN_203_exception.png")
            self.logger.error(f"TC_Reporting_ZN_EN_203 got exception as: {ex}")
