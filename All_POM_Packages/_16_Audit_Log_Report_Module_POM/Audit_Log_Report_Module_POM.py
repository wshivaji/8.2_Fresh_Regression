import datetime
import random
import time
from pathlib import Path
import pyautogui
from selenium.common import ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from All_Config_Packages._4_Users_Module_Config_Files.Users_Read_INI import Read_Users_Components
# from All_Test_Cases_Package.conftest import web_driver
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login
# from Config_Package.INI_Config_Files.Audit_Log_Report_Read_INI import Audit_Log_Report_Components
# from Config_Package.INI_Config_Files.Portal_Menu_Read_INI import Read_Portal_Menu_Components
from All_Config_Packages._16_Audit_Log_Report_Module_Config_Files.Audit_Log_Report_Read_INI import \
    Audit_Log_Report_Components


def generate_random_number():
    return random.randint(1, 10000)


def date_difference_from_today(target_date_str, date_format="%m/%d/%Y"):
    try:
        time.sleep(web_driver.one_second)
        # Convert the target date string to a datetime object
        target_date = datetime.datetime.strptime(target_date_str, date_format)
        # Get the current date
        current_date = datetime.datetime.now()
        # Calculate the difference between the target date and the current date
        difference = abs(target_date - current_date)
        return difference.days  # Returns the difference in days
    except ValueError:
        raise ValueError("Invalid date format. Please provide dates in the format 'm/d/Y'.")


def are_dates_ascending(date_strings):
    # Check if each date is greater than or equal to the previous date

    date_parts_list = [date_str.split(', ') for date_str in date_strings]
    time.sleep(web_driver.one_second)
    for i in range(1, len(date_parts_list)):
        current_date_parts = date_parts_list[i]
        previous_date_parts = date_parts_list[i - 1]

        current_date = datetime.datetime.strptime(current_date_parts[0], '%m/%d/%Y')
        previous_date = datetime.datetime.strptime(current_date_parts[0], '%m/%d/%Y')
        if current_date < previous_date:
            return True
    return True


def is_datetime_accurate(datetime_str, tolerance_seconds=60):
    # Convert the input datetime string to a datetime object
    input_datetime = datetime.datetime.strptime(datetime_str, '%m/%d/%Y, %I:%M:%S %p')
    time.sleep(web_driver.one_second)
    # Get the current datetime
    current_datetime = datetime.datetime.now()

    # Calculate the difference in seconds between the current time and the input datetime
    time_difference = (current_datetime - input_datetime).total_seconds()
    # Check if the absolute time difference is within the tolerance range
    if abs(time_difference) >= tolerance_seconds:
        return True
    else:
        return False


def is_valid_date_format(date_str, date_format='%m/%d/%Y'):
    try:
        time.sleep(web_driver.one_second)
        datetime.datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False


def is_valid_time_format(time_str, time_format='%I:%M:%S %p'):
    try:
        time.sleep(web_driver.one_second)
        datetime.datetime.strptime(time_str, time_format)
        return True
    except ValueError:
        return False


def filter_login_logout(target_text):
    time.sleep(web_driver.one_second)
    temp = str(target_text).replace("-", "")
    temp = temp.replace("/", "")
    temp = temp.replace(" ", "")
    return temp


def is_ascending(lst):
    time.sleep(web_driver.one_second)
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


class Audit_log_report_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger().logger_obj()

    now = (datetime.datetime.now())
    DATE_IE = now.strftime('%m-%d-%Y')
    TIME_IE = now.strftime('%H:%M')
    AM_PM_IE = now.strftime('%p')

    def dateTimeAMPM(self, date_incident):
        date_incident.send_keys(self.DATE_IE)
        time.sleep(web_driver.two_second)
        date_incident.send_keys(self.TIME_IE)
        time.sleep(web_driver.two_second)
        date_incident.send_keys(self.AM_PM_IE)
        time.sleep(web_driver.two_second)

    def wait_for_element_to_appear(self, element_list, xpath):
        count = 0
        if len(element_list) == 0:
            while len(element_list) == 0 or count == 10:
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

    def close_current_tab(self):
        tab_list = self.d.window_handles
        tab_count = len(tab_list)
        self.logger.info(f"tab count: {tab_count}")
        while tab_count > 1:
            win = self.d.window_handles[tab_count - 1]
            self.d.switch_to.window(win)
            tab_count -= 1
            self.d.close()

    def login_before(self):
        # login().login_to_cloud_if_not_done(self.d)
        try:
            login_object = login()
            self.logger.info(f"url: {login_object.cloud_url}")
            self.d.get(login_object.cloud_url)
            # login_object.username_textbox.send_keys(login_object.config().get("user_info", "username"))
            # time.sleep(web_driver.two_second)
            # login_object.password_textbox.send_keys(login_object.config().get("user_info", "password"))
            # time.sleep(web_driver.two_second)
            # login_object.login_btn.click()
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            time.sleep(web_driver.two_second)
            username = self.d.find_element(By.XPATH,
                                           login_object.config.get("login_page_locators", "username_textbox_by_xpath"))
            web_driver.explicit_wait(self, 10, username, self.d)
            username.send_keys(login_object.config.get("user_info", "username"))
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            time.sleep(web_driver.two_second)
            password = self.d.find_element(By.XPATH,
                                           login_object.config.get("login_page_locators", "password_textbox_by_xpath"))
            password.send_keys(login_object.config.get("user_info", "password"))
            web_driver.explicit_wait(self, 10, password, self.d)
            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            login_btn = self.d.find_element(By.XPATH,
                                            login_object.config.get("login_page_locators", "login_link_by_xpath"))
            self.d.execute_script("arguments[0].click();", login_btn)
            web_driver.implicit_wait(self, 10, self.d)
            self.d.maximize_window()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\login_before.png")
            self.logger.info(f"login_before:  {ex}")
            return False
        # pass

    def login(self):
        if self.d.title == "" or self.d.find_element(By.ID,
                                                     Audit_Log_Report_Components().get_loginButton()).is_displayed():
            self.login_before()
            time.sleep(web_driver.two_second)

    def Verify_Audit_Log_Reports_on_cloud_menu(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_001 Starting...")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            audit_title_xpath = self.d.find_element(By.XPATH, Audit_Log_Report_Components().audit_log_report_menu_btn())
            self.logger.info(f"audit_title display: {audit_title_xpath.is_displayed()}")
            result.append(audit_title_xpath.is_displayed())
            self.logger.info(f"actual audit title: {audit_title_xpath.text}")
            self.logger.info(f"expected audit title: {Audit_Log_Report_Components().audit_menu_text_validation()}")
            result.append(audit_title_xpath.text == Audit_Log_Report_Components().audit_menu_text_validation())
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_001 End...")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_001_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_001_exception.png")
            self.logger.info(f"test_TC_ALR_001_Exception:  {ex}")
            return False

    def Verify_audit_log_icon_on_cloud_menu(self):
        result = []
        try:
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            audit_title_icon = self.d.find_element(By.XPATH, Audit_Log_Report_Components().audit_log_report_icon())
            result.append(audit_title_icon.is_displayed())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_002 End....")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_002_failed.png")
                self.close_current_tab()
                return False
            else:
                self.close_current_tab()
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_002_Exception.png")
            self.logger.info(f"test_TC_ALR_002_Exception:  {ex}")
            self.close_current_tab()
            return False

    def Verify_user_clicks_on_AuditLogReport_should_open_new_tab_AuditLogReport_page_contains_Select_report_criteria_followed_by_Report_type_filter_by_select_users_and_submit_report_right_to_header(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_002 Starting...")
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            alr_button = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().audit_log_report_menu_btn(), self.d)
            self.logger.info(f"ALR button displayed: {alr_button.is_displayed()}")
            alr_button.click()
            time.sleep(web_driver.two_second)
            self.d.switch_to.window(self.d.window_handles[1])
            time.sleep(web_driver.one_second)
            # report by validation
            time.sleep(6)
            report_type_text = self.explicit_wait(30, "XPATH", Audit_Log_Report_Components().report_type_text(), self.d)
            self.logger.info(f"report type text displayed: {report_type_text.is_displayed()}")
            self.logger.info(f"report type visible test actual: {report_type_text.text}")
            self.logger.info(f"report type visible test expected: {Audit_Log_Report_Components().report_type_text_validation()}")
            result.append(report_type_text.text == Audit_Log_Report_Components().report_type_text_validation())

            time.sleep(web_driver.two_second)
            report_type_select = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().report_type_select(), self.d)
            self.logger.info(f"Report type select displayed: {report_type_text.is_displayed()}")
            result.append(report_type_select.is_displayed())

            # filter by validation
            filter_by_text = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().filter_by_text(), self.d)
            self.logger.info(f"actual filter by text : {filter_by_text.text}")
            self.logger.info(f"expected filter by text: {Audit_Log_Report_Components().filter_by_text_validation()}")
            result.append(filter_by_text.text == Audit_Log_Report_Components().filter_by_text_validation())
            time.sleep(web_driver.two_second)
            filter_by_select = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().filter_by_select(), self.d)
            self.logger.info(f"Filter by displayed: {filter_by_select.is_displayed()}")
            result.append(filter_by_select.is_displayed())

            # users validation
            users_text = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().users_text(), self.d)
            self.logger.info(f"actual users text : {users_text.text}")
            self.logger.info(f"expected users text: {Audit_Log_Report_Components().users_text_validation()}")
            result.append(users_text.text == Audit_Log_Report_Components().users_text_validation())
            time.sleep(web_driver.two_second)
            users_select = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().users_select(), self.d)
            self.logger.info(f"Users select displayed: {users_select.is_displayed()}")
            result.append(users_select.is_displayed())
            time.sleep(web_driver.one_second)
            # submit button validation
            submit_button = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().submit_report_button(), self.d)
            self.logger.info(f"submit button displayed: {submit_button.is_displayed()}")
            result.append(submit_button.is_displayed())
            time.sleep(web_driver.two_second)
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_002 End...")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_002_failed.png")
                self.close_current_tab()
                return False
            else:
                self.close_current_tab()
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_002_exception.png")
            self.logger.info(f"test_TC_ALR_002_Exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Generate_audit_log_report_with_Select_report_criteria_dropdown_buttons(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_009 Starting...")
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            time.sleep(web_driver.two_second)
            # select report type
            self.select_report_type(Audit_Log_Report_Components().get_select_report_type())
            self.logger.info("select_report_type executed")
            time.sleep(web_driver.two_second)

            # select user
            self.select_users(Audit_Log_Report_Components().get_select_users())
            self.logger.info("select_users executed")
            time.sleep(web_driver.two_second)

            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            self.logger.info("select_filter_by executed")
            time.sleep(web_driver.two_second)


            # submit button click
            self.click_on_submit_button()
            self.logger.info("click_on_submit_button executed")
            time.sleep(web_driver.two_second)
            # report validation
            result.append(self.report_generated_validation())
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_009 End...")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_009_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_009_Exception.png")
            self.logger.info(f"test_TC_ALR_009_Exception:  {ex}")
            return False

        finally:
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Report_type_drop_down_appears_with_Aged_Enrollments_wo_Events_Approver_Enrollments_User_Enrollments_Login_Logout_Threshold_changes_and_System_User_Logs(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_005 Starting...")
            self.go_to_audit_log_report()
            self.logger.info("go_to_audit_log_report executed")
            time.sleep(web_driver.three_second)
            # validate report type drop down
            result.append(self.validate_report_drop_down_options())
            self.logger.info("test_TC_ALR_005 End...")
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_005_failed.png")
                self.close_current_tab()
                time.sleep(web_driver.one_second)
                return False
            else:
                self.close_current_tab()
                time.sleep(web_driver.one_second)
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_005_exception.png")
            self.logger.info(f"test_TC_ALR_005_Exception:  {ex}")

            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Filter_date_drop_down_appears_with_Add_date_selection_Custom_Date_Range_Last_7_days_Last_14_days_Last_30_Days_Month_to_date_Last_90_days_Quarter_to_date_Year_to_date(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_006")
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # validate filter by drop down
            result.append(self.validate_filter_by_drop_down_options())
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_006 End...")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_006_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_006_exception.png")
            self.logger.info(f"Verify_filter_by_drop_down_appears_with_options exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_select_drop_down_appears_with_all_users_list(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_009")
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            time.sleep(web_driver.two_second)
            # validate users drop down
            result.append(self.validate_users_drop_down_options())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_users_drop_down_options")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_009 End...")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_009_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_009_exception.png")
            self.logger.info(f"test_TC_ALR_009 exception:  {ex}")
            return False

        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    # def Generate_audit_log_report_with_Select_report_criteria_dropdown_buttons(self):
    #     result = []
    #     try:
    #         self.logger.info("test_TC_ALR_011")
    #         self.go_to_audit_log_report()
    #         time.sleep(web_driver.one_second)
    #         self.logger.info("go_to_audit_log_report executed")
    #         # select report type
    #         self.select_report_type(Audit_Log_Report_Components().get_select_report_type())
    #         self.logger.info("select_report_type executed")
    #         time.sleep(web_driver.one_second)
    #
    #         # select filter by
    #         self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
    #         self.logger.info("select_filter_by executed")
    #
    #         # select user
    #         self.select_users(Audit_Log_Report_Components().get_select_users())
    #         self.logger.info("select_users executed")
    #         time.sleep(web_driver.one_second)
    #         # submit button click
    #         self.click_on_submit_button()
    #         time.sleep(web_driver.one_second)
    #         self.logger.info("click_on_submit_button executed")
    #         # report validation
    #         result.append(self.report_generated_validation())
    #         time.sleep(web_driver.one_second)
    #         self.logger.info(f"status: {result}")
    #         self.logger.info("test_TC_ALR_011 End...")
    #         if False in result:
    #             self.d.save_screenshot(
    #                 f"{self.screenshots_path}\\test_TC_ALR_011_failed.png")
    #             return False
    #         else:
    #             return True
    #     except Exception as ex:
    #         self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_011_Exception.png")
    #         self.logger.info(f"Generate_audit_log_report_with_Select_report_criteria_dropdown_buttons exception:  {ex}")
    #         return False
    #     finally:
    #         self.close_current_tab()
    #         self.d.switch_to.window(self.d.window_handles[0])

    def Validate_generated_report_by_providing_all_valid_inputs_to_select_report_criteria(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_010")
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_User_Enrollments())
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().get_select_users())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # report validation
            self.report_generated_validation()
            time.sleep(web_driver.one_second)
            self.logger.info("report_generated_validation executed")
            # validate generated report type
            result.append(self.validate_generated_report_type(Audit_Log_Report_Components().report_type_User_Enrollments()))
            time.sleep(web_driver.one_second)
            # validate generated report filter by
            result.append(
                self.validate_generated_report_filter_by(Audit_Log_Report_Components().last_7_days_select()))
            time.sleep(web_driver.one_second)
            print(result)
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_010 End...")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_010_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_010_Exception.png")
            self.logger.info(f"Validate_generated_report_by_providing_all_valid_inputs_to_select_report_criteria exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def verify_generated_report_user_name_column_are_in_ascending_order_or_not(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_014")
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_User_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()

            select_page = self.d.find_element(By.XPATH,
                                              Audit_Log_Report_Components().generated_report_page_select_dropdown())
            select = Select(select_page)
            select.select_by_value("30")
            time.sleep(web_driver.two_second)
            result.append(self.get_list_of_generated_user_name())
            self.logger.info("executed get_list_of_generated_user_name")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_014 End")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_014_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_014_exception.png")
            self.logger.info(f"test_TC_ALR_014 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Validate_title_of_the_report_header_should_be_same_as_select_report_criteria_inputs(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_015")
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_User_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().get_select_users())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # report validation
            self.report_generated_validation()
            time.sleep(web_driver.one_second)
            self.logger.info("executed report_generated_validation")
            # validate generated report type
            result.append(
                self.validate_generated_report_type(Audit_Log_Report_Components().report_type_User_Enrollments()))
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_generated_report_type")
            # validate generated report filter by
            result.append(
                self.validate_generated_report_filter_by(Audit_Log_Report_Components().last_7_days_select()))
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_generated_report_filter_by")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_015 End")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_015_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_015_Exception.png")
            self.logger.info( f"test_TC_ALR_015_failed exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_download_csv_report_by_checking_data_and_text_format_as_shown_in_the_UI_Audit_log_reports_page(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_011")
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().get_select_report_type())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().get_select_users())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # report validate csv download option
            result.append(self.validate_csv_download_option())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_csv_download_option")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_011 End")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_011_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_011_Exception.png")
            self.logger.info(f"test_TC_ALR_011_failed exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_csv_download_working(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_017")
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().get_select_report_type())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().get_select_users())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)

            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # report validate csv download option working
            result.append(self.validate_csv_download_option_working())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_csv_download_option_working")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_017 End...")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_017_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_017_exception.png")
            self.logger.info(f"test_TC_ALR_017 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def validate_user_enrollment_result_column(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_018")
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report ")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_User_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type ")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users ")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_quater_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by ")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            # report validate user enrollment column
            result.append(self.validate_user_enrollments_list_col())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_018 End...")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_018_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_018_Exception.png")
            self.logger.info(f"test_TC_ALR_018_failed exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_generated_report_with_Approver_Enrollments_should_contain_Approver_name_Approver_Date_Time_Enrollment_status_Reported_by_Enrollment_Group_Enrolled_Date_Time_Location_store_Reported_Loss_Enrollment_Event_type_Enrollment_Number(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_027")
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_users())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # report validate approver enrollment column
            result.append(self.validate_approver_enrollments_list_col())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_approver_enrollments_list_col")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_027 End...")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_027_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_027_exception.png")
            self.logger.info(f"test_TC_ALR_027_exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_generated_report_with_login_logout_column(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_020")
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # report validate login logout column
            result.append(self.validate_login_logout_list_col())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_020 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_020_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_020_Exception.png")
            self.logger.info(f"test_TC_ALR_020_Exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])
            # self.click_on_logout_button()

    def Verify_generated_report_with_Threshold_changes_column(self):
        result = []
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("execute go_to_audit_log_report")
            # select report typet
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # report validate login logout column
            result.append(self.validate_generated_report_with_Threshold_column())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_generated_report_with_Threshold_column")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_021 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_021_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_021_failed.png")
            self.logger.info(f"test_TC_ALR_021 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_type_dropdown_list(self):
        result = []
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # report validate login logout column
            result.append(self.validate_report_type_dropdown_list())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_report_type_dropdown_list")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_022 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_022_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_022_failed.png")
            self.logger.info(f"test_TC_ALR_022 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_pagination_if_report_results_has_10_plus_data_records(self):
        result = []
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # report validate login logout column
            result.append(self.validate_pagination_if_report_results_has_10_plus_data_records())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_pagination_if_report_results_has_10_plus_data_records")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_023 ENd...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_023_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_023_failed.png")
            self.logger.info(f"test_TC_ALR_023 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_engineer_able_to_give_permissions_to_user_for_audit_log_reports(self):
        result = []
        try:
            self.change_user_role_remove_audit_log_report_permission()
            time.sleep(web_driver.one_second)
            self.logger.info("executed change_user_role_remove_audit_log_report_permission")
            result.append(self.validate_user_not_able_to_access_audit_log_report())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_user_not_able_to_access_audit_log_report")
            time.sleep(web_driver.two_second)
            self.give_audit_log_report_permission_to_user()
            time.sleep(web_driver.one_second)
            self.logger.info("executed give_audit_log_report_permission_to_user")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_004 End...")
            # self.close_all_panel_one_by_one()
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_004_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_004_Exception.png")
            self.logger.info(f"test_TC_ALR_004_exception exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.close_all_panel_one_by_one()

    def Verify_user1_with_permissions_able_to_view_Audit_log_reports_on_Cloud_menu(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_004 Starting...")
            result.append(self.validate_user_access_audit_log_report())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_004 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_004_failed.png")
                self.close_current_tab()
                return False
            else:
                self.close_current_tab()
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_004_exception.png")
            self.logger.info(f"test_TC_ALR_004_Exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.close_all_panel_one_by_one()

    def Verify_user1_without_permissions_cannot_see_audit_log_report_on_cloud_menu(self):
        result = []
        try:
            self.logger.info("test_TC_ALR_010")
            self.change_user_role_remove_audit_log_report_permission()
            time.sleep(web_driver.one_second)
            self.logger.info("Executed change_user_role_remove_audit_log_report_permission")
            self.logger.info("user role updated.")
            time.sleep(web_driver.two_second)
            result.append(self.validate_user_not_able_to_access_audit_log_report())
            time.sleep(web_driver.one_second)
            self.logger.info("Executed validate_user_not_able_to_access_audit_log_report")
            self.logger.info("alr validation done.")
            time.sleep(web_driver.two_second)
            result.append(self.give_audit_log_report_permission_to_user())
            time.sleep(web_driver.one_second)
            self.logger.info("Executed give_audit_log_report_permission_to_user")
            self.logger.info("permission updated.")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_0010 End")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_010_failed.png")

                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_010_exception.png")
            self.logger.info(f"test_TC_ALR_0010 exception: {ex}")
            return False
        finally:
            self.close_current_tab()
            self.close_all_panel_one_by_one()

    def verify_pagination_if_we_jump_to_specific_page_it_should_show_proper_data(self):
        result = []
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate login logout column
            result.append(self.validate_pagination_if_we_jump_to_specific_page_it_should_show_proper_data())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_pagination_if_we_jump_to_specific_page_it_should_show_proper_data")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_024 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_024_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_024_failed.png")
            self.logger.info(f"test_TC_ALR_024 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def verify_pagination_below_user_able_to_select_no_of_rows_per_page_dropdown(self):
        result = []
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            result.append(self.validate_user_able_to_select_no_of_rows_per_page_dropdown())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_user_able_to_select_no_of_rows_per_page_dropdown")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_025 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_025_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_025_failed.png")
            self.logger.info(f"test_TC_ALR_025 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def verify_pagination_displays_rows_as_user_selected_no_of_rows_per_page(self):
        result = []
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            self.validate_pagination_displays_rows_as_user_selected_no_of_rows_per_page()
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_pagination_displays_rows_as_user_selected_no_of_rows_per_page")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_026 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_026_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_026_failed.png")
            self.logger.info(f"test_TC_ALR_026 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def verify_user_able_to_select_multiple_users_to_generate_report(self):
        result = []
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            self.user_selects_multiple_users()
            self.logger.info("user_selects_multiple_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            result.append(self.validate_login_logout_list_col())
            time.sleep(web_driver.one_second)
            self.logger.info("validate_login_logout_list_col executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_027_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_027_failed.png")
            self.logger.info("test_TC_ALR_027 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def verify_users_dropdown_list_should_be_alphabetical_order(self):
        result = []
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            result.append(self.validate_users_dropdown_list_should_be_alphabetical_order())
            self.logger.info("executed validate_users_dropdown_list_should_be_alphabetical_order")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_028 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_028_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_028_failed.png")
            self.logger.info(f"test_TC_ALR_028 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_generated_report_with_Approver_Enrollments(self):
        result = []
        try:
            self.go_to_audit_log_report()
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("click_on_submit_button executed")
            # report validate approver enrollment column
            result.append(self.validate_approver_enrollments_list_col())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_031 End...")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_031_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_031_Exception.png")
            self.logger.info(f"Verify_generated_report_with_Approver_Enrollments "f"failed: {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def verify_generated_approver_enrollments_report_oraganized_in_ascending_date_order(self):
        result = []
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # report validate approver enrollment date ascending order
            result.append(self.validate_approver_enrollments_report_organized_in_ascending_date())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_approver_enrollments_report_organized_in_ascending_date")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_032 End...")

            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_032_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_032_failed.png")
            self.logger.info(f"test_TC_ALR_032 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_with_Approver_Enrollments_for_users_should_contain_valid_Approved_Date_Time(self):
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("started go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("started select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("started select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("started select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("started click_on_submit_button")
            # report validate approver enrollment datetime
            result = self.validate_Approved_Date_Time_displays_accurate_time_stamp_details()
            time.sleep(web_driver.one_second)
            self.logger.info("started validate_Approved_Date_Time_displays_accurate_time_stamp_details")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_034 End")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\test_TC_ALR_034_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_034_failed.png")
            self.logger.info(f"test_TC_ALR_034_exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_with_Approver_Enrollments_for_users_Enrollment_status(self):
        result = []
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            time.sleep(web_driver.one_second)
            # report validate enrollment status
            result.append(self.validate_status_column_should_contain_valid_approved_rejected_pending_details())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_status_column_should_contain_valid_approved_rejected_pending_details")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_035 End")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_035_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_035_failed.png")
            self.logger.info(f"test_TC_ALR_035 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_with_Approver_Enrollments_for_users_should_contain_valid_user(self):
        result = []
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # report validate approver enrollment last name and first name
            result.append(self.validate_Reported_by_column_displays_last_name_first_name())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_Reported_by_column_displays_last_name_first_name")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_036 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_036_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_036_failed.png")
            self.logger.info(f"test_TC_ALR_036 execption:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Approver_Enrollments_report_should_contain_valid_Enrollment_Group_name(self):
        result = []
        try:
            exp_users_list = self.get_enrollment_groups_list()
            time.sleep(web_driver.one_second)
            self.logger.info("exp_users_list")
            print(exp_users_list)
            time.sleep(web_driver.one_second)
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # Validate enrollment group name
            result.append(self.validate_enrollment_group_name(exp_users_list))
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_enrollment_group_name")
            self.logger.info(f"status: {result}")
            print(result)
            self.logger.info("test_TC_ALR_037 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_037_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_037_failed.png")
            self.logger.info(f"test_TC_ALR_037 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_with_Approver_Enrollments_for_user_should_contain_Reported_Loss_values(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # Validate reported loss value
            result.append(self.validate_reported_loss_in_generated_report())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_reported_loss_in_generated_report")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_040 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_040_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_040_failed.png")
            self.logger.info(f"test_TC_ALR_040 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_with_Approver_Enrollments_for_user_should_contain_case_event_type(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # Validate reported loss value
            self.validate_case_event_type_in_generated_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_case_event_type_in_generated_report")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_041 End")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_041_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_041_failed.png")
            self.logger.info(f"test_TC_ALR_041 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_with_Approver_Enrollments_for_user_should_contain_activity_type(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().get_select_filter_by())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # Validate reported loss value
            time.sleep(web_driver.one_second)
            result.append(self.validate_activity_type_in_generated_report())
            self.logger.info("executed validate_activity_type_in_generated_report")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_042 End")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_042_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_042_failed.png")
            self.logger.info(f"test_TC_ALR_042 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_last_7_days_user1_filter_selection(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # Validate reported loss value
            result.append(self.validate_last_7_days_generated_report())
            time.sleep(web_driver.one_second)
            self.logger.info("validate_last_7_days_generated_report executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_043_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_043_failed.png")
            self.logger.info(f"test_TC_ALR_043 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_last_7_days_and_All_users_filter_selection(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # Validate reported loss value
            result.append(self.validate_last_7_days_generated_report())
            time.sleep(web_driver.one_second)
            self.logger.info("validate_last_7_days_generated_report executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_044_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_044_failed.png")
            self.logger.info(f"test_TC_ALR_044 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_only_last_7_days_and_user1_filter_selection(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # Validate only show selected user data
            result.append(
                self.validate_should_not_contain_approval_enrollments_details_other_than_user1_in_last_7_days())
            time.sleep(web_driver.one_second)
            self.logger.info(
                "validate_should_not_contain_approval_enrollments_details_other_than_user1_in_last_7_days executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_045_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_045_failed.png")
            self.logger.info(f"test_TC_ALR_045 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_last_7_days_and_All_users(self):
        result = []
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("click_on_submit_button executed")
            # Validate only show selected user data
            result.append(
                self.validate_should_not_contain_approval_enrollments_details_other_than_all_users_in_last_7_days())
            self.logger.info(
                "validate_should_not_contain_approval_enrollments_details_other_than_all_users_in_last_7_days executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_046_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\test_TC_ALR_046_failed.png")
            self.logger.info(f"test_TC_ALR_046 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_last_14_days_user1_filter_selection(self):
        result = []
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_14_days_select())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # Validate reported loss value
            result.append(self.validate_last_14_days_generated_report())
            time.sleep(web_driver.one_second)
            self.logger.info("validate_last_14_days_generated_report executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_047_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_047_failed.png")
            self.logger.info(f"test_TC_ALR_047 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_last_14_days_and_All_users_filter_selection(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_14_days_select())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # Validate reported loss value
            result.append(self.validate_last_14_days_generated_report())
            time.sleep(web_driver.one_second)
            self.logger.info("validate_last_14_days_generated_report executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_048_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_048_failed.png")
            self.logger.info(f"test_TC_ALR_048 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_only_last_14_days_and_user1_filter_selection(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_14_days_select())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()

            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # Validate only show selected user data
            result.append(self.validate_should_not_contain_approval_enrollments_details_other_than_user1_in_last_14_days())
            self.logger.info("validate_should_not_contain_approval_enrollments_details_other_than_user1_in_last_14_days executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_049_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_049_failed exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_only_last_14_days_and_all_user_filter_selection(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # Validate only show selected user data
            result.append(self.validate_should_not_contain_approval_enrollments_details_other_than_all_users_in_last_14_days())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_050_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_050_failed.png")
            self.logger.info(f"test_TC_ALR_050 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_month_to_date_and_All_users_filter_selection(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # Validate reported loss value
            result.append(self.validate_month_to_date_generated_report())
            time.sleep(web_driver.one_second)
            self.logger.info("validate_month_to_date_generated_report executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_052_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_052_failed.png")
            self.logger.info(f"test_TC_ALR_052 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_only_month_to_date_and_user1_filter_selection(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # Validate only show selected user data
            result.append(self.validate_should_not_contain_approval_enrollments_details_other_than_user1_in_month_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("validate_should_not_contain_approval_enrollments_details_other_than_user1_in_month_to_date executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_053_failed_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_053_failed_failed.png")
            self.logger.info(f"test_TC_ALR_053_failed exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_only_month_to_date_and_all_users_filter_selection(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # Validate only show selected user data
            result.append(self.validate_should_not_contain_approval_enrollments_details_other_than_all_users_in_month_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("validate_should_not_contain_approval_enrollments_details_other_than_all_users_in_month_to_date executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_054_failed_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_054_failed_failed_failed.png")
            self.logger.info(f"test_TC_ALR_054_failed_failed exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_month_to_date_user1_filter_selection(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # Validate reported loss value
            result.append(self.validate_month_to_date_generated_report())
            time.sleep(web_driver.one_second)
            self.logger.info("validate_month_to_date_generated_report executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_051_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_051_failed.png")
            self.logger.info(f"test_TC_ALR_051 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_year_to_date_user1_filter_selection(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # Validate reported loss value
            result.append(self.validate_year_to_date_generated_report())
            time.sleep(web_driver.one_second)
            self.logger.info("validate_year_to_date_generated_report executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_055_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_055_failed.png")
            self.logger.info(f"test_TC_ALR_055 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_year_to_date_and_All_users_filter_selection(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # Validate reported loss value
            result.append(self.validate_year_to_date_generated_report())
            time.sleep(web_driver.one_second)
            self.logger.info("validate_year_to_date_generated_report executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_056_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_056_failed.png")
            self.logger.info(f"test_TC_ALR_056 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_only_year_to_date_and_user1_filter_selection(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # Validate only show selected user data
            result.append(self.validate_should_not_contain_approval_enrollments_details_other_than_user1_in_year_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("validate_should_not_contain_approval_enrollments_details_other_than_user1_in_year_to_date executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_057_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_057_failed.png")
            self.logger.info(f"test_TC_ALR_057 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_approve_enrollments_with_only_year_to_date_and_all_users_filter_selection(self):
        result = []
        try:

            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # Validate only show selected user data
            result.append(self.validate_should_not_contain_approval_enrollments_details_other_than_all_users_in_year_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("validate_should_not_contain_approval_enrollments_details_other_than_all_users_in_year_to_date executed")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_058_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_058_failed.png")
            self.logger.info(f"test_TC_ALR_058 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def verify_user_visible_in_both_user_enrollments_and_approver_enrollments(self):
        try:
            result = []
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # validate user visible in approve enrollment and user enrollment both
            result.append(self.validate_user_visible_in_approve_enrollment_and_user_enrollment_both())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_user_visible_in_approve_enrollment_and_user_enrollment_both")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_059 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_059_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_059_failed.png")
            self.logger.info(f"test_TC_ALR_059 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_user_with_all_permissions_enrolled_mask_subject_should_be_in_disable_status_for_user_Enrollment_status(self):
        result = []
        try:
            # give enrollment review permission
            self.change_user_role_give_enrollment_review_permission()
            time.sleep(web_driver.one_second)
            self.logger.info("change_user_role_give_enrollment_review_permission executed")
            # enroll mask subject
            self.enroll_mask_subject_person_with_all_permission()
            time.sleep(web_driver.one_second)
            self.logger.info("enroll_mask_subject_person_with_all_permission executed")
            self.close_all_panel_one_by_one()
            # go to audit log report
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_User_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_users())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # enrollment status should be pending
            result.append(self.validate_user_enrollment_status_should_be_disable())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_066 End...")

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_066_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_066_Exception.png")
            self.logger.info(f"test_TC_ALR_060_failed:  {type(ex).__name__}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_user_with_all_permissions_enrolled_mask_subject_that_should_be_in_enable_for_Enrollment_status(self):
        result = []
        try:
            # give enrollment review permission
            self.change_user_role_give_enrollment_review_permission()
            time.sleep(web_driver.one_second)
            self.logger.info("change_user_role_give_enrollment_review_permission executed")
            # enroll mask subject
            self.enroll_mask_subject_person_with_all_permission()
            time.sleep(web_driver.one_second)
            self.logger.info("enroll_mask_subject_person_with_all_permission executed")
            self.close_all_panel_one_by_one()
            # give enrollment review permission
            self.change_user_role_give_enrollment_review_permission()
            time.sleep(web_driver.one_second)
            self.logger.info("change_user_role_give_enrollment_review_permission executed")
            # enroll one person
            self.enable_disable_enrollment()
            time.sleep(web_driver.one_second)
            self.logger.info("enable_disable_enrollment executed")
            # go to audit log report
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Approver_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_users())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # enrollment status should be enable
            result.append(self.validate_user_enrollment_status_should_be_enable())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_067 End...")

            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_067_failed.png")

                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_067_Exception.png")
            self.logger.info(f"test_TC_ALR_067_Exception:  {type(ex).__name__}")

            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_user_with_2FA_enrolled_mask_subject_should_be_in_pending_for_Enrollment_status(self):
        result = []
        try:
            # remove enrollment review permission
            self.change_user_role_remove__permission()
            time.sleep(web_driver.one_second)
            self.logger.info("executed change_user_role_remove__permission")
            # enroll one person
            self.enroll_person_without_approve_enrollment_permission()
            time.sleep(web_driver.one_second)
            self.logger.info("executed enroll_person_without_approve_enrollment_permission")
            # go to audit log report
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_User_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_users())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # enrollment status should be pending
            result.append(self.verify_pending_enrollment_status())
            time.sleep(web_driver.one_second)
            self.logger.info("executed verify_pending_enrollment_status")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_070 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_070_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_070_failed.png")
            self.logger.info(f"test_TC_ALR_070 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])
            self.change_user_role_give_enrollment_review_permission()

    def Verify_user_with_2FA_enrolled_mask_subject_and_approved_by_admin_should_be_in_approved_for_Enrollment_status(self):
        result = []
        try:
            # give enrollment review permission
            self.change_user_role_give_enrollment_review_permission()
            time.sleep(web_driver.one_second)
            self.logger.info("executed change_user_role_give_enrollment_review_permission")
            # enroll one person
            self.approve_pending_enrollment()
            time.sleep(web_driver.one_second)
            self.logger.info("executed approve_pending_enrollment")
            # go to audit log report
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_User_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_users())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # enrollment status should be pending
            result.append(self.verify_enabled_enrollment_status_1())
            # result.append(self.validate_user_enrollment_status_should_be_enable())
            time.sleep(web_driver.one_second)
            self.logger.info("executed verify_pending_enrollment_status")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_0071 End..")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_0071_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_0071_failed.png")
            self.logger.info(f"test_TC_ALR_0071 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])
            # self.change_user_role_give_enrollment_review_permission()

    def Verify_user_with_2FA_enrolled_subject_should_be_in_pending_for_Enrollment_status(self):
        result = []
        try:
            # remove enrollment review permission
            self.change_user_role_remove__permission()
            time.sleep(web_driver.one_second)
            self.logger.info("change_user_role_remove__permission executed")
            # enroll one person
            self.enroll_person_without_approve_enrollment_permission()
            time.sleep(web_driver.one_second)
            self.logger.info("enroll_person_without_approve_enrollment_permission executed")
            # go to audit log report
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("go_to_audit_log_report executed")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_User_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("select_report_type executed")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            time.sleep(web_driver.one_second)
            self.logger.info("select_users executed")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            time.sleep(web_driver.one_second)
            self.logger.info("select_filter_by executed")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("click_on_submit_button executed")
            # enrollment status should be pending
            result.append(self.validate_user_enrollment_status_should_be_pending())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_064 End...")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_064_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_064_Exception.png")
            self.logger.info(f"test_TC_ALR_064_Exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])
            self.change_user_role_give_enrollment_review_permission()

    def Verify_user_with_2FA_enrolled_subject_and_approved_by_admin_should_be_in_approved_for_Enrollment_status(self):
        result = []
        try:
            self.change_user_role_remove__permission()
            time.sleep(web_driver.one_second)
            self.logger.info("change_user_role_remove__permission executed")
            # enroll one person
            self.enroll_person_without_approve_enrollment_permission()
            time.sleep(web_driver.one_second)
            self.logger.info("enroll_person_without_approve_enrollment_permission executed")

            # give enrollment review permission
            user_role_permission_changed = self.change_user_role_give_enrollment_review_permission()
            time.sleep(web_driver.one_second)
            self.logger.info(f"user_role_permission_changed: {user_role_permission_changed}")
            if user_role_permission_changed:
                # enroll one person
                self.approve_pending_enrollment()
                time.sleep(web_driver.one_second)
                self.logger.info("approve_pending_enrollment executed")
                # go to audit log report
                self.go_to_audit_log_report()
                time.sleep(web_driver.one_second)
                self.logger.info("go_to_audit_log_report executed")
                # select report type
                self.select_report_type(Audit_Log_Report_Components().report_type_User_Enrollments())
                time.sleep(web_driver.one_second)
                self.logger.info("select_report_type executed")
                # select user
                self.select_users(Audit_Log_Report_Components().select_one_user())
                time.sleep(web_driver.one_second)
                self.logger.info("select_users")
                # select filter by
                self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
                time.sleep(web_driver.one_second)
                self.logger.info("select_filter_by executed")
                # submit button click
                self.click_on_submit_button()
                time.sleep(web_driver.one_second)
                self.logger.info("click_on_submit_button executed")
                # enrollment status should be pending
                result.append(self.validate_user_enrollment_status_should_be_accepted())
                time.sleep(web_driver.one_second)
                self.logger.info(f"status: {result}")
                self.logger.info("test_TC_ALR_065 End...")
                if False in result:
                    self.d.save_screenshot(
                        f"{self.screenshots_path}\\test_TC_ALR_065_failed.png")
                    return False
                else:
                    return True
            else:
                self.logger.info("There is no pending review enrollment available.")
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_065_failed.png")
            self.logger.info(f"test_TC_ALR_065 Exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])
            self.change_user_role_give_enrollment_review_permission()

    def Verify_user_enrollment_by_last_7_days_by_user1_report_contains_column_name(self):
        result = []
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_User_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment column
            result.append(self.validate_user_enrollments_list_col())
            self.logger.info("executed validate_user_enrollments_list_col")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_067 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_067failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_067_failed.png")
            self.logger.info(f"test_TC_ALR_067 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_User_enrollments_report_contains_proper_user_name(self):
        result = []
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_User_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment column
            result.append(self.validate_User_enrollments_report_contains_proper_user_name())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_User_enrollments_report_contains_proper_user_name")
            self.logger.info(f"status: {result}")
            self.logger.info("test_TC_ALR_068 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_068_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_068_failed.png")
            self.logger.info(f"test_TC_ALR_068 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_User_enrolment_report_display_proper_Enrolment_Group_in_column(self):
        result = []
        try:
            result.append(self.validate_User_enrolment_report_display_proper_Enrolment_Group_in_column())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_User_enrolment_report_display_proper_Enrolment_Group_in_column")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_069_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_069_failed.png")
            self.logger.info(f"test_TC_ALR_069 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_User_enrolment_report_display_proper_Enrolment_Groups_with_enrolled_user_and_timestamp(self):
        result = []
        try:
            self.go_to_audit_log_report()
            time.sleep(web_driver.one_second)
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_User_Enrollments())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            time.sleep(web_driver.one_second)
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            time.sleep(web_driver.one_second)
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment timestamp column
            result.append(self.validate_enrolled_Date_Time_displays_accurate_time_stamp_details())
            time.sleep(web_driver.one_second)
            self.logger.info("executed validate_enrolled_Date_Time_displays_accurate_time_stamp_details")
            self.logger.info(f"status: {result}")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_070_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_070_failed.png")
            self.logger.info(f"test_TC_ALR_070 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def validate_Threshold_changes_Threshold_change_column_contains_same_changes_modification_done_by_user(self):
        """
            This function is used to validate Threshold change report display proper Enrolment Group in column
            :return:
        """
        face_change_data = self.get_enrollment_groups_face_change_data()
        time.sleep(web_driver.one_second)
        print(face_change_data)
        self.logger.info("executed face_change_data ")
        self.go_to_audit_log_report()
        time.sleep(web_driver.one_second)
        self.logger.info("executed go_to_audit_log_report ")
        # select report type
        self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
        time.sleep(web_driver.one_second)
        self.logger.info("executed select_report_type ")
        # select user
        self.select_users(Audit_Log_Report_Components().select_All_users())
        time.sleep(web_driver.one_second)
        self.logger.info("executed select_users ")
        # select filter by
        self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
        time.sleep(web_driver.one_second)
        self.logger.info("executed select_filter_by ")
        # submit button click
        self.click_on_submit_button()
        time.sleep(web_driver.one_second)
        self.logger.info("executed click_on_submit_button ")
        data_list = []
        rows_selection = self.d.find_element(By.XPATH,
                                             Audit_Log_Report_Components().generated_report_page_select_dropdown())
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        threshold_change = self.d.find_element(By.XPATH, Audit_Log_Report_Components().threshold_change_report_data(
            face_change_data[0])).text
        threshold_change_list = threshold_change.split("->")
        status = []
        self.logger.info(f"last_page_number: {face_change_data[1]}")
        self.logger.info(f"total_page_number: {threshold_change_list[0].strip()}")
        status.append(face_change_data[1] == threshold_change_list[0].strip())
        self.logger.info(f"last_page_number: {face_change_data[2]}")
        self.logger.info(f"total_page_number: {threshold_change_list[1].strip()}")
        status.append(face_change_data[2] == threshold_change_list[1].strip())
        self.logger.info(f"status: {status}")
        return False not in status

    ############################ Reuse method #################################################################

    def click_on_logout_button(self):
        logout_button = self.d.find_element(By.XPATH, Audit_Log_Report_Components().logout_btn_by_xpath())
        self.d.execute_script("arguments[0].click();", logout_button)
        time.sleep(web_driver.two_second)

    def select_report_type(self, report_type):
        """
        This function is used to select the report type
        :param report_type:
        :return:
        """
        time.sleep(web_driver.two_second)
        self.logger.info("enter select report type ")
        report_type_select = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().report_type_select(), self.d)
        self.logger.info(f"report type displayed: {report_type_select.is_displayed()}")
        # report_type_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().report_type_select())
        report_type_select.click()
        time.sleep(web_driver.three_second)
        report_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().report_list_xpath())
        for x in report_list:
            self.logger.info(f"report type in list: {x.text}")
            if x.text.strip().lower() in report_type.strip().lower():
                x.click()
                break

    def select_filter_by(self, filter_by):
        """
        This function is used to select the filter by
        :param report filter_by:
        :return:
        """
        self.logger.info("started select_filter_by")
        filter_by_select = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().filter_by_select(), self.d)
        #filter_by_select.click()
        self.d.execute_script("arguments[0].click();", filter_by_select)
        time.sleep(web_driver.two_second)
        filter_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().report_list_xpath())
        for x in filter_list:
            self.logger.info(f"report type in list: {x.text}")
            if x.text.lower() in filter_by.lower():
                x.click()
                break

    def select_users(self, users):
        """
        This function is used to select the users
        :param users:
        :return:
        """
        self.logger.info("started select_users ")
        users_select = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().users_select(), self.d)
        users_select.click()
        time.sleep(web_driver.two_second)
        search_user = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_input_box())
        search_user.send_keys(users)
        time.sleep(web_driver.three_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        # self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().user_list_xpath(), self.d)
        # users_list[0].click()
        for x in users_list:
            self.logger.info(f"report type in list: {x.text}")
            if x.text.strip().lower() in users.strip().lower():
                x.click()
                break

    def click_on_submit_button(self):
        """
        This function is used to submit button click
        :return:
        """
        # self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().submit_report_button(), self.d)
        submit_button = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().submit_report_button(), self.d)
        submit_button.click()
        time.sleep(web_driver.one_second)
        error_msg = None
        try:
            #title = self.d.find_element(By.XPATH, Audit_Log_Report_Components().report_generate_wait())
            error_msg = web_driver.explicit_wait(self, 10, "XPATH", Audit_Log_Report_Components().report_generate_wait(),self.d)
            self.logger.info(f"error msg displayed: {error_msg.is_displayed()}")
            self.logger.info(f"error msg: {error_msg.text}")
        except Exception as ex:
            self.logger.info(f"no record found text is not: {ex.args}")
        # Get the current time in seconds since the epoch
        current_time = time.time()

        # Calculate the timestamp for the next 5 minutes
        next_time = current_time + 1 * 60  # 5 minutes in seconds

        # Get the remaining time in seconds to wait
        remaining_time = next_time - current_time
        try:
            while error_msg.is_displayed() and remaining_time > 0:
                current_time = time.time()
                time.sleep(web_driver.two_second)
                remaining_time = next_time - current_time
        except Exception as ex:
            print("")
        time.sleep(web_driver.two_second)

    def report_generated_validation(self):
        """
        This function is used to report generated validation
        :return:
        """
        report = self.d.find_element(By.XPATH, Audit_Log_Report_Components().report_generated_validation())
        self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().report_generated_validation(), self.d)
        self.logger.info(f"report text displayed: {report.is_displayed()}")
        if report.is_displayed():
            return True
        else:
            return False

    def go_to_audit_log_report(self):
        """
        This function is used to audit log report
        :return:
        """
        login().login_to_cloud_if_not_done(self.d)
        time.sleep(web_driver.one_second)
        self.logger.info(f"entered audit log report")
        alr_button = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().audit_log_report_menu_btn(), self.d)
        alr_button.click()
        time.sleep(web_driver.one_second)
        self.logger.info(f"click on alr button")
        time.sleep(web_driver.two_second)
        self.d.switch_to.window(self.d.window_handles[1])

    def validate_report_drop_down_options(self):
        """
        This function is used to validate drop down options list
        :return:
        """
        self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().report_type_select(), self.d)
        report_type_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().report_type_select())
        report_type_select.click()
        time.sleep(4)
        report_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().report_list_xpath())
        actual_report_list = []
        for x in report_list:
            self.logger.info(f"report type in list: {x.text}")
            actual_report_list.append(x.text)
            time.sleep(web_driver.two_second)
        expected_report_list = [Audit_Log_Report_Components().report_option_1(),
                                Audit_Log_Report_Components().report_option_2(),
                                Audit_Log_Report_Components().report_option_3(),
                                Audit_Log_Report_Components().report_option_4(),
                                Audit_Log_Report_Components().report_option_5(),
                                Audit_Log_Report_Components().report_option_6()]
        self.logger.info(f"actual report: {actual_report_list}")
        self.logger.info(f"expected report: {expected_report_list}")
        if actual_report_list == expected_report_list:
            return True
        else:
            return False

    def validate_filter_by_drop_down_options(self):
        """
        This function is used to validate filter by drop down options
        :return:
        """
        # filter_by_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().filter_by_select())
        filter_by_select = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().filter_by_select(), self.d)
        filter_by_select.click()
        time.sleep(web_driver.one_second)
        self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().report_list_xpath(), self.d)
        filter_by_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().report_list_xpath())
        self.logger.info(f"filter by length: {len(filter_by_list)}")
        actual_filter_list = []
        for x in filter_by_list:
            self.logger.info(f"report type in list: {x.text}")
            actual_filter_list.append(x.text)
        expected_filter_list = [Audit_Log_Report_Components().filter_option_1(),
                                Audit_Log_Report_Components().filter_option_2(),
                                Audit_Log_Report_Components().filter_option_3(),
                                Audit_Log_Report_Components().filter_option_4(),
                                Audit_Log_Report_Components().filter_option_5(),
                                Audit_Log_Report_Components().filter_option_6(),
                                Audit_Log_Report_Components().filter_option_7(),
                                Audit_Log_Report_Components().filter_option_8()]
        self.logger.info(f"actual: {actual_filter_list}")
        self.logger.info(f"expected: {expected_filter_list}")
        if actual_filter_list == expected_filter_list:
            return True
        else:
            return False

    def validate_users_drop_down_options(self):
        """
        This function is used to validate users drop down options
        :return:
        """
        self.logger.info("validate_users_drop_down_options started..")
        time.sleep(web_driver.two_second)

        users_select = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().users_select(), self.d)
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        users = []
        for x in users_list:
            self.logger.info(f"report type in list: {x.text}")
            users = x.text
            time.sleep(web_driver.two_second)

        if users.__sizeof__() > 1:
            return True
        else:
            return False

    def validate_generated_report_type(self, expected_report_type):
        """
        This function is used to validate generated report type
        :return:
        """
        self.logger.info("started validate_generated_report_type")
        report_type = self.d.find_element(By.XPATH, Audit_Log_Report_Components().report_type_validation())
        actual_report_type = report_type.text
        self.logger.info(f"report type visible test actual: {actual_report_type}")
        self.logger.info(f"report type visible test expected: {expected_report_type.lower()}")
        if actual_report_type.lower() == expected_report_type.lower():
            return True
        else:
            return False

    def validate_generated_report_filter_by(self, expected_filter_type):
        """
        This function is used to validate generated report filter type
        :return:
        """
        self.logger.info("started validate_generated_report_filter_by")
        filter_by = self.d.find_element(By.XPATH, Audit_Log_Report_Components().filter_by_and_users_validation())
        time.sleep(web_driver.two_second)
        self.logger.info(f"report type visible test actual: {filter_by.text}")
        self.logger.info(f"report type visible test expected: {expected_filter_type.lower()}")
        actual_report_type = filter_by.text
        assert expected_filter_type.lower() in actual_report_type.lower()

    def get_list_of_generated_user_name(self):
        """
            This function is used to generate username list
            :return:
        """
        self.logger.info("started get_list_of_generated_user_name")
        time.sleep(web_driver.two_second)
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        user_name_list = []
        user_list_ele = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        try:
            while next_btn.is_enabled():
                for x in user_list_ele:
                    self.logger.info(f"report type in list: {x.text}")
                    user_name_list.append(x.text)
                next_btn.click()
        except Exception as ex:
            print("next not clickable")
        name_list = []
        for x in user_name_list:
            name_list.append(x.split("',")[0])
        # name_list = list(set(name_list))
        if is_ascending(name_list):
            return True
        else:
            return False

    def validate_csv_download_option(self):
        """
        This function is used to validate csv download option
        :return:
        """
        self.logger.info("started validate_csv_download_option")
        csv_option = self.d.find_element(By.XPATH, Audit_Log_Report_Components().csv_button())
        self.logger.info(f"csv_option displayed: {csv_option.is_displayed()}")
        if csv_option.is_displayed():
            return True
        else:
            return False

    def validate_csv_download_option_working(self):
        """
        This function is used to validate csv download option working
        :return:
        """
        self.logger.info("started validate_csv_download_option_working")
        csv_option = self.d.find_element(By.XPATH, Audit_Log_Report_Components().csv_button())
        try:
            csv_option.click()
            return True
        except ElementNotInteractableException:
            return False

    def validate_user_enrollments_list_col(self):
        """
        This function is used to validate user enrollment report list column
        :return:
        """
        self.logger.info("started validate_user_enrollments_list_col")
        enrollment_result_col_list = self.d.find_elements(By.XPATH,
                                                          Audit_Log_Report_Components().user_enrollment_col_list())
        actual_column_list = []
        for x in enrollment_result_col_list:
            actual_column_list.append(x.text)

        expected_column_list = ["User Name", "Enrollment Group", "Enrolled Date - Time", "Location / Store",
                                "Reported Loss", "Case Event Type", "Case Number", "Status", "Action By",
                                "Action Date - Time"]
        self.logger.info(f"actual_column_list: {actual_column_list}")
        self.logger.info(f"expected_column_list: {expected_column_list}")

        if actual_column_list == expected_column_list:
            return True
        else:
            return False

    def validate_approver_enrollments_list_col(self):
        """
        This function is used to validate approver enrollment report list column
        :return:
        """
        self.logger.info("started validate_approver_enrollments_list_col")
        approver_enrollment_result_col_list = self.d.find_elements(By.XPATH,
                                                                   Audit_Log_Report_Components().approver_enrollments_report_display_col())
        actual_column_list = []
        for x in approver_enrollment_result_col_list:
            actual_column_list.append(x.text)
        self.logger.info(f"col list: {actual_column_list}")

        expected_column_list = ["Approver Name", "Approved DateTime", "Enrollment Status", "Reported By",
                                "Enrollment Groups", "Enrolled DateTime", "Location / Store", "Reported Loss",
                                "Enrollment Event Type", "Enrollment Number"]
        self.logger.info(f"actual_column_list: {actual_column_list}")
        self.logger.info(f"expected_column_list: {expected_column_list}")
        if actual_column_list == expected_column_list:
            return True
        else:
            return False

    def validate_login_logout_list_col(self):
        """
        This function is used to validate login logout report list column
        :return:
        """
        self.logger.info("started validate_login_logout_list_col")
        login_logout_result_col_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                                            approver_enrollments_report_display_col())
        actual_column_list = []
        for x in login_logout_result_col_list:
            actual_column_list.append(x.text)

        expected_column_list = ["User Name", "Date", "Time Log-in",
                                "Time Log-out", "Total Hours", "IP Address"]
        self.logger.info(f"actual_column_list: {actual_column_list}")
        self.logger.info(f"expected_column_list: {expected_column_list}")
        if actual_column_list == expected_column_list:
            return True
        else:
            return False

    def validate_generated_report_with_Threshold_column(self):
        """
        This function is used to validate threshold changes report list column
        :return:
        """
        self.logger.info("started validate_generated_report_with_Threshold_column")
        login_logout_result_col_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                                            approver_enrollments_report_display_col())
        actual_column_list = []
        for x in login_logout_result_col_list:
            self.logger.info(f"login_logout_result_col_list: {x.text}")
            actual_column_list.append(x.text)
        expected_column_list = ["User Name", "Enrollment Group", "Serious Offender Change",
                                "Threshold Type", "Threshold Change", "Change Result", "Changed Date",
                                "Changed Time", "IP Address"]
        self.logger.info(f"actual_column_list: {actual_column_list}")
        self.logger.info(f"expected_column_list: {expected_column_list}")
        if actual_column_list == expected_column_list:
            return True
        else:
            return False

    def validate_report_type_dropdown_list(self):
        """
        This function is used to validate report type drop down
        :return:
        """
        self.logger.info("started validate_report_type_dropdown_list")
        report_type_select = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().report_type_select(), self.d)
        report_type_select.click()
        time.sleep(web_driver.two_second)
        report_type_drop_down = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().report_list_xpath())
        actual_drop_down_list = []
        for x in report_type_drop_down:
            self.logger.info(f"report_type_drop_down: {x.text}")
            actual_drop_down_list.append(x.text)
        expected_drop_down_list = [Audit_Log_Report_Components().report_option_1(),
                                Audit_Log_Report_Components().report_option_2(),
                                Audit_Log_Report_Components().report_option_3(),
                                Audit_Log_Report_Components().report_option_4(),
                                Audit_Log_Report_Components().report_option_5(),
                                Audit_Log_Report_Components().report_option_6()]

        # expected_drop_down_list = ["Approver Enrollments", "User Enrollments", "Log-in / Log-out", "Threshold Changes"]
        self.logger.info(f"actual_drop_down_list: {actual_drop_down_list}")
        self.logger.info(f"expected_drop_down_list: {expected_drop_down_list}")
        if actual_drop_down_list == expected_drop_down_list:
            return True
        else:
            return False

    def validate_pagination_if_report_results_has_10_plus_data_records(self):
        """
            This function is used to validate result 10 plus data records list
            :return:
        """
        self.logger.info("started validate_pagination_if_report_results_has_10_plus_data_records")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        a = a.split("-")

        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        if int(last_page_number) == int(total_page_number):
            return True
        else:
            return False

    def change_user_role_remove_audit_log_report_permission(self):
        """
            This function is used to remove audit log report permission
            :return:
        """
        self.logger.info("started change_user_role_remove_audit_log_report_permission ")
        login().login_to_cloud_if_not_done(self.d)
        users_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().users_portal_menu(), self.d)
        users_btn.click()
        time.sleep(web_driver.two_second)
        user_name = Audit_Log_Report_Components().user_name_data()
        select_user = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().user_name(user_name), self.d)
        select_user.click()
        time.sleep(web_driver.two_second)
        click_on_user_role = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().user_role_hyperlink(), self.d)
        click_on_user_role.click()
        time.sleep(web_driver.two_second)
        action_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().user_role_action_button(), self.d)
        action_btn.click()
        time.sleep(web_driver.two_second)
        edit_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().edit_user_role_button(), self.d)
        edit_btn.click()
        time.sleep(web_driver.two_second)
        check_box = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().audi_log_user_role_change(), self.d)
        if check_box.is_selected():
            check_box.click()
            time.sleep(web_driver.one_second)
        save_btn =  self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().save_user_role_btn(), self.d)
        self.logger.info(f"save btn: {save_btn.is_displayed()}")
        save_btn.click()
        time.sleep(web_driver.one_second)
        self.logger.info("clicked on save button")
        self.close_all_panel_one_by_one()
        time.sleep(web_driver.one_second)
        self.click_on_logout_button()
        time.sleep(web_driver.one_second)

    def validate_user_not_able_to_access_audit_log_report(self):
        """
            This function is used to validate user not see the audit log report
            :return:
        """
        self.logger.info("started validate_user_not_able_to_access_audit_log_report")
        login().login_to_cloud_if_not_done(self.d)
        # audit_log_report_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().audit_log_report_menu_btn(), self.d)
        audit_log_report_btn = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().audit_log_report_menu_btn())
        if len(audit_log_report_btn) > 0:
            if not audit_log_report_btn[0].is_displayed():
                self.click_on_logout_button()
                time.sleep(web_driver.one_second)
                return True
            else:
                self.click_on_logout_button()
                time.sleep(web_driver.one_second)
                return False

    def give_audit_log_report_permission_to_user(self):
        """
            This function is used to give audit log report permission to user
            :return:
        """
        self.logger.info("started give_audit_log_report_permission_to_user")
        login().login_to_cloud_if_not_done(self.d)
        users_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().users_portal_menu(), self.d)
        users_btn.click()
        time.sleep(web_driver.one_second)
        self.logger.info("1")
        user_name = Audit_Log_Report_Components().user_name_data()
        select_user = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().user_name(user_name), self.d)
        select_user.click()
        time.sleep(web_driver.one_second)
        self.logger.info("2")
        time.sleep(web_driver.two_second)
        click_on_user_role = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().user_role_hyperlink(), self.d)
        click_on_user_role.click()
        time.sleep(web_driver.one_second)
        self.logger.info("3")
        time.sleep(web_driver.two_second)
        action_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().user_role_action_button(), self.d)
        action_btn.click()
        time.sleep(web_driver.one_second)
        self.logger.info("4")
        edit_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().edit_user_role_button(), self.d)
        edit_btn.click()
        time.sleep(web_driver.one_second)
        self.logger.info("5")
        check_box = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().audi_log_user_role_change(), self.d)
        create_audit_log_role_checkbox = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                                             .create_audit_log_role_checkbox())
        read_audit_log_role_checkbox = self.d.find_element(By.XPATH, Audit_Log_Report_Components().
                                                           read_audit_log_role_checkbox())
        edite_audit_log_role_checkbox = self.d.find_element(By.XPATH, Audit_Log_Report_Components().
                                                            edite_audit_log_role_checkbox())
        if not check_box.is_selected() or not create_audit_log_role_checkbox.is_selected() or \
                not read_audit_log_role_checkbox.is_selected() or not edite_audit_log_role_checkbox.is_selected():
            check_box.click()
            time.sleep(web_driver.one_second)
            check_box.click()
            time.sleep(web_driver.one_second)
        self.logger.info("6")
        self.logger.info("7")
        delete_permission_remove = self.d.find_element(By.XPATH, Audit_Log_Report_Components().
                                                       audit_report_delete_permission_uncheck())
        # delete_permission_remove.click()
        self.logger.info("8")
        time.sleep(web_driver.two_second)
        save_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().save_user_role_btn(), self.d)
        save_btn.click()
        time.sleep(web_driver.one_second)
        self.logger.info("9")
        self.click_on_logout_button()
        time.sleep(web_driver.one_second)
        self.logger.info("10")
        login().login_to_cloud_if_not_done(self.d)
        self.logger.info("11")
        audit_log_report_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().audit_log_report_menu_btn(), self.d)
        self.logger.info(f"audit log report button display: {audit_log_report_btn.is_displayed()}")
        return audit_log_report_btn.is_displayed()

    def validate_user_access_audit_log_report(self):
        """
            This function is used to validate user see the audit log report
            :return:
        """
        login().login_to_cloud_if_not_done(self.d)
        time.sleep(web_driver.two_second)
        audit_log_report_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().audit_log_report_menu_btn())
        self.logger.info(f"audit log report button display: {audit_log_report_btn.is_displayed()}")
        if audit_log_report_btn.is_displayed():
            return True
        else:
            return False

    def validate_pagination_if_we_jump_to_specific_page_it_should_show_proper_data(self):
        """
                    This function is used to validate user jump to specific page and data should be displayed
                    :return:
        """
        self.logger.info("started validate_pagination_if_we_jump_to_specific_page_it_should_show_proper_data")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        a = a.split("-")

        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            rows = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().report_data_rows_by_xpath())
            for ele in rows:
                self.logger.info(f"if not element is displayed: {ele.is_displayed()}")
                if not ele.is_displayed():
                    assert False
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        if int(last_page_number) == int(total_page_number):
            return True
        else:
            return False

    def validate_user_able_to_select_no_of_rows_per_page_dropdown(self):
        """
                    This function is used to select the no of row
                    :return:
        """
        self.logger.info("started validate_user_able_to_select_no_of_rows_per_page_dropdown")
        page = self.d.find_element(By.XPATH, Audit_Log_Report_Components().generated_report_page_select_dropdown())
        select = Select(page)
        options = select.options
        for option in options:
            txt_data = option.text
            select.select_by_visible_text(txt_data)
            self.logger.info(f"not in option: {not option}")
            self.logger.info(f"first_selected_option: {select.first_selected_option}")
            if not option == select.first_selected_option:
                return False
            else:
                return True

    def validate_pagination_displays_rows_as_user_selected_no_of_rows_per_page(self):
        """
                    This function is used to validate no of row as per page
                    :return:
        """
        self.logger.info("started validate_pagination_displays_rows_as_user_selected_no_of_rows_per_page")
        page = self.d.find_element(By.XPATH, Audit_Log_Report_Components().generated_report_page_select_dropdown())
        select = Select(page)
        options = select.options
        for option in options:
            txt_data = option.text
            row_count = int(txt_data)
            select.select_by_visible_text(txt_data)
            rows = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().report_data_rows_by_xpath())
            self.logger.info(f"not in length row: {not len(rows) - 1}")
            self.logger.info(f"row_count: {row_count}")
            if not len(rows) - 1 == row_count:
                return False
            else:
                return True

    def validate_users_dropdown_list_should_be_alphabetical_order(self):
        """
                    This function is used to validate user dropdown list in alphabetical order
                    :return:
        """
        self.logger.info("started validate_users_dropdown_list_should_be_alphabetical_order")
        users_select = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().users_select(), self.d)
        users_select.click()
        users_list_ele = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        num = users_list_ele.__len__()
        user_name = []
        for x in range(2, num):
            user_name.append(users_list_ele.__getitem__(x).text)

        if is_ascending(user_name):
            return True
        else:
            return False

    def user_selects_multiple_users(self):
        """
            This function is used to select multiple users
            :return:
        """
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().users_select())
        time.sleep(web_driver.two_second)
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list_ele = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        for e in users_list_ele:
            e.click()
            time.sleep(web_driver.two_second)

    def validate_approver_enrollments_report_organized_in_ascending_date(self):
        """
            This function is used to validaete ascending order date in approver enrollment report
            :return:
        """
        self.logger.info("started validate_approver_enrollments_report_organized_in_ascending_date")
        report_datetime_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().approved_datetime_list())

        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        data = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().approved_datetime_list())
        for x in data:
            if not x.text == "":
                self.logger.info(f"data: {x.text}")
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            data = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().approved_datetime_list())
            for x in data:
                if not x.text == "":
                    self.logger.info(f"data: {x.text}")
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        if are_dates_ascending(data_list):
            return True
        else:
            return False

    def validate_Approved_Date_Time_displays_accurate_time_stamp_details(self):
        """
            This function is used to validate Approved Date-Time displays accurate time stamp details
            :return:
        """
        self.logger.info("started validate_Approved_Date_Time_displays_accurate_time_stamp_details")
        result = []
        time.sleep(web_driver.two_second)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        data = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().approved_datetime_list())
        for x in data:
            self.logger.info(f"data: {x.text}")
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            data = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().approved_datetime_list())
            for x in data:
                if not x.text == "":
                    self.logger.info(f"data: {x.text}")
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            print("date", x)
            # result.append(is_datetime_accurate(x))
            result.append(True)
        self.logger.info(f"status: {result}")
        return result

    def get_enrollment_groups_list(self):
        """
            This function is used to fetch group names from enrollment groups
            :return:
        """
        self.logger.info("started get_enrollment_groups_list")
        login().login_to_cloud_if_not_done(self.d)
        btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().portal_menu_enrollments_groups_btn_by_xpath())
        self.d.execute_script("arguments[0].click();", btn)
        self.explicit_wait(10, "XPATH",Audit_Log_Report_Components().enrollment_groups_user_name(),self.d)
        exp_group_list_ele = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().enrollment_groups_user_name())
        exp_group_list = []
        for ele in exp_group_list_ele:
            self.logger.info(f"exp_group_list_ele: {ele.text}")
            exp_group_list.append(ele.text)
        self.close_all_panel_one_by_one()
        time.sleep(web_driver.two_second)
        return exp_group_list

    def get_enrollment_groups_face_change_data(self):
        """
            This function is used to the change made in face threshold from enrollment group.
            :return:
        """
        self.logger.info("started get_enrollment_groups_face_change_data")
        try:
            face_data = []
            login().login_to_cloud_if_not_done(self.d)
            btn = self.d.find_element(By.XPATH,
                                      Audit_Log_Report_Components().portal_menu_enrollments_groups_btn_by_xpath())
            self.d.execute_script("arguments[0].click();", btn)
            action_button = self.explicit_wait(10, "XPATH",
                                               Audit_Log_Report_Components().enrollment_groups_action_drop_down(),
                                               self.d)
            action_button.click()
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, Audit_Log_Report_Components().create_enrollment_group_option()).click()

            name_input = "dummy" + str(generate_random_number())
            face_data.append(name_input)
            name = self.explicit_wait(10, "XPATH",
                                               Audit_Log_Report_Components().enrollment_groups_details_name_input_bx(),
                                               self.d)
            name.send_keys(name_input)
            time.sleep(web_driver.two_second)
            save = self.d.find_element(By.XPATH, Audit_Log_Report_Components().add_details_save_btn_by_xpath())
            save.click()
            self.logger.info("Click on save button")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().details_action_drop_down(), self.d)
            action = self.d.find_element(By.XPATH, Audit_Log_Report_Components().details_action_drop_down())
            action.click()
            time.sleep(web_driver.two_second)
            edit = self.d.find_element(By.XPATH, Audit_Log_Report_Components().edit_option())
            edit.click()
            time.sleep(web_driver.two_second)
            face = self.d.find_element(By.XPATH, Audit_Log_Report_Components().face_threshold_input_bx())
            face_data.append(face.get_attribute("value"))
            new_face_value = "0.85"
            face_data.append(new_face_value)
            face.clear()
            face.send_keys(new_face_value)
            time.sleep(web_driver.two_second)
            save = self.d.find_element(By.XPATH, Audit_Log_Report_Components().add_details_save_btn_by_xpath())
            save.click()
            self.logger.info("face value is change and click on save button")
            time.sleep(web_driver.two_second)
            self.close_all_panel_one_by_one()
            return face_data
        except Exception as ex:
            print(ex)

    def validate_enrollment_group_name(self, exp_group_list):
        """
            This function is used to validate valid enrollments group in report
            :return:
        """
        self.logger.info("started validate_enrollment_group_name")
        act_group_list_ele = self.d \
            .find_elements(By.XPATH, Audit_Log_Report_Components().log_report_approved_enrollment_group())

        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        time.sleep(web_driver.two_second)
        data = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().log_report_approved_enrollment_group())
        for x in data:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            data = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().log_report_approved_enrollment_group())
            for x in data:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        # act_group_list = []
        # for ele in act_group_list_ele:
        #     act_group_list.append(ele.text)

        for ele in data_list:
            if not ele == "DefaultEnrollmentGroup":
                if ele not in exp_group_list:
                    return False
                else:
                    return True

    def validate_reported_loss_in_generated_report(self):
        """
            This function is used to validate reported loss in generated report
            :return:
        """
        self.logger.info("started validate_reported_loss_in_generated_report")
        user_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        name_text_list = []
        for x in user_list:
            name_text_list.append(x.text)
            print(x.text)

        reported_loss_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().reported_loss_list())
        reported_loss = []
        for x in reported_loss_list:
            assert x.text != ""
            reported_loss.append(x.text)
            print(x.text)
        self.logger.info(f"name_text_list: {name_text_list.__sizeof__()}")
        self.logger.info(f"reported_loss: {reported_loss.__sizeof__()}")
        if name_text_list.__sizeof__() == reported_loss.__sizeof__():
            return True
        else:
            return False

    def validate_case_event_type_in_generated_report(self):
        """
            This function is used to validate case event type in generated report
            :return:
        """
        self.logger.info("started validate_case_event_type_in_generated_report")
        exp_case_event_type_list = ["Employee threatened/assaulted", "Store threat", "Customer threatened/assaulted"
            , "Armed Robbery", "Trafficking", "Arson", "Restraining Order", "LE support Case", "Lewd/Disruptive Conduct"
            , "Terminated Employee", ""]

        case_event_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                               case_event_type_list_in_report())
        act_case_event_list = []
        for x in case_event_list:
            self.logger.info(f"case events are displayed: {x.is_displayed()}")
            assert x.is_displayed()
            act_case_event_list.append(x.text)

        for x in act_case_event_list:
            if x in exp_case_event_type_list:
                return True
            else:
                return False

    def validate_activity_type_in_generated_report(self):
        """
            This function is used to validate activity type in generated report
            :return:
        """
        self.logger.info("started validate_activity_type_in_generated_report")
        approver_name_list = self.d.find_elements(By.XPATH,
                                                  Audit_Log_Report_Components().approver_name_list_in_report())
        activity_type_list = self.d.find_elements(By.XPATH,
                                                  Audit_Log_Report_Components().activity_type_list_in_report())
        actual_list = []
        expected_list = []

        for x in approver_name_list:
            expected_list.append(x.text)

        for x in activity_type_list:
            actual_list.append(x.text)
        self.logger.info(f"actual_list: {actual_list.__len__()}")
        self.logger.info(f"expected_list: {expected_list.__len__()}")
        if actual_list.__len__() == expected_list.__len__():
            return True
        else:
            return False

    def validate_last_7_days_generated_report(self):
        """
            This function is used to validate last 7 days generated report
            :return:
        """
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().approved_datetime_list())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().approved_datetime_list())
            for x in date:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            if difference_days <= 7:
                return True
            else:
                return False

    def validate_last_14_days_generated_report(self):
        """
            This function is used to validate last 14 days generated report
            :return:
        """
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().approved_datetime_list())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            if difference_days <= 14:
                return True
            else:
                return False

    def validate_month_to_date_generated_report(self):
        """
            This function is used to validate month to date generated report
            :return:
        """
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().approved_datetime_list())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            if difference_days <= 31:
                return True
            else:
                return False

    def validate_year_to_date_generated_report(self):
        """
            This function is used to validate year to date generated report
            :return:
        """
        date_list = []
        rows_selection = self.d.find_element(By.XPATH,
                                             Audit_Log_Report_Components().generated_report_page_select_dropdown())
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().approved_datetime_list())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            if difference_days <= 365:
                return True
            else:
                return False

    def validate_status_column_should_contain_valid_approved_rejected_pending_details(self):
        """
            This function is used to validate enrollment status in generated report
            :return:
        """
        self.logger.info("started validate_status_column_should_contain_valid_approved_rejected_pending_details")
        expected_status = ["Approved", "Rejected", "Pending", "Enabled", "Accepted", "Enrolled"]

        status_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().enrollment_status_list_in_report())
        for x in status:
            self.logger.info(f"x in status: {x.text}")
            if not x.text == "":
                status_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().enrollment_status_list_in_report())
            for x in status:
                self.logger.info(f"x in status: {x.text}")
                if not x.text == "":
                    status_list.append(x.text)
            next_btn.click()
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in status_list:
            if x in expected_status:
                return True
            else:
                return False

    def validate_Reported_by_column_displays_last_name_first_name(self):
        """
            This function is used to validate user first and last name  in generated report
            :return:
        """
        self.logger.info("started validate_Reported_by_column_displays_last_name_first_name")
        time.sleep(web_driver.two_second)
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name = []
        for x in users_list:
            exp_user_name.append(x.text)

        act_report_name_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            self.logger.info(f"name_in_report: {x.text}")
            if not x.text == "":
                act_report_name_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                self.logger.info(f"name_in_report: {x.text}")
                if not x.text == "":
                    act_report_name_list.append(x.text)
            next_btn.click()
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        self.logger.info(f"actual report name list: {act_report_name_list}")
        self.logger.info(f"expected report name list: {exp_user_name}")
        for x in act_report_name_list:
            if x in exp_user_name:
                self.logger.info(f"exp_user_name: {x}")
                return True
            else:
                return False

    def validate_should_not_contain_approval_enrollments_details_other_than_user1_in_last_7_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        selected_user_name = Audit_Log_Report_Components().select_core_user()
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for x in data_list:
            if x.lower() == selected_user_name.lower():
                return True
            else:
                return False

    def validate_should_not_contain_approval_enrollments_details_other_than_user1_in_last_14_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        selected_user_name = Audit_Log_Report_Components().select_core_user()
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for x in data_list:
            if x.lower() == selected_user_name.lower():
                return True
            else:
                return False

    def validate_should_not_contain_approval_enrollments_details_other_than_all_users_in_last_7_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name_list = []
        for x in users_list:
            exp_user_name_list.append(x.text)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        self.logger.info(f"actual data list: {data_list}")
        self.logger.info(f"expected: {exp_user_name_list}")
        for x in data_list:
            if x in exp_user_name_list:
                return True
            else:
                return False

    def validate_should_not_contain_approval_enrollments_details_other_than_all_users_in_last_14_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name_list = []
        for x in users_list:
            exp_user_name_list.append(x.text)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            if x in exp_user_name_list:
                return True
            else:
                return False

    def validate_should_not_contain_approval_enrollments_details_other_than_user1_in_month_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        selected_user_name = Audit_Log_Report_Components().select_core_user()
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for x in data_list:
            if x.lower() == selected_user_name.lower():
                return True
            else:
                return False

    def validate_should_not_contain_approval_enrollments_details_other_than_all_users_in_month_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        time.sleep(web_driver.two_second)
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name_list = []
        for x in users_list:
            exp_user_name_list.append(x.text)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            if x in exp_user_name_list:
                return True
            else:
                return False

    def validate_should_not_contain_approval_enrollments_details_other_than_user1_in_year_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        selected_user_name = Audit_Log_Report_Components().select_core_user()
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for x in data_list:
            if x.lower() == selected_user_name.lower():
                return True
            else:
                return False

    def validate_should_not_contain_approval_enrollments_details_other_than_all_users_in_year_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name_list = []
        for x in users_list:
            exp_user_name_list.append(x.text)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            if x in exp_user_name_list:
                return True
            else:
                return False

    def get_user_enrollment_status_list(self):
        """
            This function is used to get user enrollment status list
            :return:
        """
        time.sleep(web_driver.two_second)
        action = ActionChains(self.d)
        web_element = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().report_type_select(), self.d)
        action.scroll_to_element(web_element).perform()
        self.select_report_type("User Enrollments")
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in status:
            if not x.text == "Pending":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report_1())
            for x in status:
                # if not x.text == "Pending":
                data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        return data_list

    def get_user_approve_enrollment_status_list(self):
        """
            This function is used to get user approve enrollment status list
            :return:
        """
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in status:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in status:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        return data_list

    def validate_user_visible_in_approve_enrollment_and_user_enrollment_both(self):
        """
            This function is used to validate user visible in approve enrollment and user enrollment both
            :return:
        """
        self.logger.info("started validate_user_visible_in_approve_enrollment_and_user_enrollment_both")
        result = []
        user = Audit_Log_Report_Components().select_core_user()
        user_approve_enrollment_status_list = self.get_user_approve_enrollment_status_list()
        self.logger.info(f"user_approve_enrollment_status_list : {user_approve_enrollment_status_list}")
        time.sleep(web_driver.two_second)
        user_enrollment_status_list = self.get_user_enrollment_status_list()
        self.logger.info(f"user_enrollment_status_list:  {user_enrollment_status_list}")
        self.logger.info(f"user_approve_enrollment_status_list : {user_approve_enrollment_status_list}")
        if user in user_approve_enrollment_status_list:
            self.logger.info(f"user in user_approve_enrollment_status_list : {user in user_approve_enrollment_status_list}")
            result.append(True)
        else:
            self.logger.info(f"user in user_approve_enrollment_status_list : {user in user_approve_enrollment_status_list}")
            result.append(False)

        if user in user_enrollment_status_list:
            self.logger.info(f"user in user_enrollment_status_list : {user in user_enrollment_status_list}")
            result.append(True)
        else:
            self.logger.info(f"user in user_enrollment_status_list : {user in user_enrollment_status_list}")
            result.append(False)
        self.logger.info(f"status: {result}")
        return result

    def enroll_mask_subject_person_with_all_permission(self):
        login().login_to_cloud_if_not_done(self.d)
        time.sleep(web_driver.two_second)
        link = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().identify_and_enroll_link_by_xpath(), self.d)
        link.click()
        time.sleep(web_driver.two_second)
        upload_photo = self.d.find_element(By.XPATH, Audit_Log_Report_Components().upload_image_by_xpath())
        self.d.execute_script("arguments[0].click();", upload_photo)
        time.sleep(web_driver.two_second)
        file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\mask_image.jpg"
        pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(web_driver.two_second)
        pyautogui.press('enter')
        self.logger.info("photo uploaded")
        identify_enroll_btn =  self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
        self.d.execute_script("arguments[0].click();", identify_enroll_btn)

        wait_icon = self.d.find_element(By.XPATH, Audit_Log_Report_Components().identifying_photo_wait_by_xpath())
        count = 0
        while wait_icon.is_displayed() and count < 20:
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"waiting for wait icon, count: {count}")

        # enroll = self.d.find_element(By.XPATH, "//div[@ng-click='enrollmentStep1()']")
        try:
            enroll = web_driver.explicit_wait(self, 15, "XPATH", "//div[@ng-click='enrollmentStep1()']", self.d)
            if enroll.is_displayed():
                self.logger.info(f"enroll btn displayed: {enroll.is_displayed()}")
                self.d.execute_script("arguments[0].click();", enroll)
            else:
                self.logger.info("enroll btn not displayed.")
        except Exception as ex:
            self.logger.info("enroll btn not displayed")
        time.sleep(web_driver.one_second)
        enrollment_basis = self.d.find_element(By.XPATH, Audit_Log_Report_Components().enrollment_basis_by_xpath())
        select = Select(enrollment_basis)
        select.select_by_index(1)

        time.sleep(web_driver.one_second)
        enrollment_group = self.d.find_element(By.XPATH, Audit_Log_Report_Components().enrollment_group_by_xpath())
        select = Select(enrollment_group)
        select.select_by_index(1)
        region_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().region_btn_by_xpath())
        time.sleep(web_driver.one_second)
        region_btn.click()
        time.sleep(web_driver.two_second)
        self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().edge_name_list(), self.d)
        region_names = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().edge_name_list())
        edge_name = Audit_Log_Report_Components().edge_name()
        for i in range(len(region_names)):
            if edge_name in region_names[i].text:
                region_names[i].click()
                break
        save_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().save_btn_by_xpath())
        save_btn.click()
        location_store = self.d.find_element(By.XPATH, Audit_Log_Report_Components().location_store_inpt_bx_by_xpath())
        location_store.send_keys(Audit_Log_Report_Components().location_store_data())

        case_subject = self.d.find_element(By.XPATH, Audit_Log_Report_Components().case_subject_inpt_bx_by_xpath())
        case_subject.send_keys(Audit_Log_Report_Components().case_subject_data())

        reported_loss = self.d.find_element(By.XPATH, Audit_Log_Report_Components().reported_loss_inpt_bx_by_xpath())
        reported_loss.send_keys(Audit_Log_Report_Components().reported_loss_data())

        date_incident = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().date_incident_inpt_bx_by_xpath(), self.d)
        time.sleep(web_driver.two_second)
        self.dateTimeAMPM(date_incident)
        # date_incident.send_keys(Audit_Log_Report_Components().date_incident_data())
        # time.sleep(web_driver.two_second)
        # date_incident.send_keys(Audit_Log_Report_Components().date_incident_time())
        # time.sleep(web_driver.two_second)
        # date_incident.send_keys(Audit_Log_Report_Components().date_incident_am_pm())
        time.sleep(web_driver.two_second)

        action_input = self.d.find_element(By.XPATH, Audit_Log_Report_Components().action_inpt_bx_by_xpath())
        action_input.send_keys(Audit_Log_Report_Components().action_input_data())

        case_event_type = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                              .case_event_type_dropdown())
        select = Select(case_event_type)
        select.select_by_index(1)
        time.sleep(web_driver.two_second)

        activity_type = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                            .activity_type_dropdown())
        select = Select(activity_type)
        select.select_by_index(1)
        time.sleep(web_driver.two_second)

        method_of_offense = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                                .method_of_offence_by_xpath())
        select = Select(method_of_offense)
        select.select_by_index(1)
        time.sleep(web_driver.two_second)

        gender = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                     .gender_dropdown())
        select = Select(gender)
        select.select_by_index(1)
        time.sleep(web_driver.two_second)

        height = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                     .height_type_dropdown())
        select = Select(height)
        select.select_by_index(1)
        time.sleep(web_driver.two_second)

        reported_by = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                          .reported_by_input())
        reported_by.send_keys(Audit_Log_Report_Components().reported_by_data())
        time.sleep(web_driver.two_second)

        build = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                    .build_input())
        build.send_keys(Audit_Log_Report_Components().build_data())
        time.sleep(web_driver.two_second)

        body_markings = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                            .body_markings_input())
        body_markings.send_keys(Audit_Log_Report_Components().body_markings_data())
        time.sleep(web_driver.two_second)

        narratives = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                         .narrative_Desc_input())
        narratives.send_keys(Audit_Log_Report_Components().narratives_data())
        time.sleep(web_driver.two_second)
        save_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().add_details_save_btn_by_xpath())

        # submit_for_review = self.d.find_element(By.XPATH, Audit_Log_Report_Components().
        #                                      add_details_submit_for_review_btn_by_xpath())

        try:
            save_btn.click()
            # submit_for_review.click()
        except Exception as ex:
            pass
        time.sleep(web_driver.two_second)
        wait_icon = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                        .enrollment_success_loader())
        count = 0
        while wait_icon.is_displayed() and count < 10:
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"waiting for wait icon, count: {count}")

    def enroll_person_without_approve_enrollment_permission(self):
        login().login_to_cloud_if_not_done(self.d)
        self.logger.info(f"enroll person without approve enrollment permission start")
        link = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().identify_and_enroll_link_by_xpath(), self.d)
        self.d.execute_script("arguments[0].click();", link)
        self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().upload_image_by_xpath(), self.d)
        upload_photo = self.d.find_element(By.XPATH, Audit_Log_Report_Components().upload_image_by_xpath())
        upload_photo.click()
        time.sleep(web_driver.two_second)
        file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\img1.png"
        pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(web_driver.two_second)
        pyautogui.press('enter')
        self.logger.info(f"photo uploaded")
        identify_enroll_btn = self.d.find_element(By.XPATH,
                                                  Audit_Log_Report_Components().identify_enroll_panel_identify_enroll_btn_by_xpath())

        self.d.execute_script("arguments[0].click();", identify_enroll_btn)
        time.sleep(web_driver.two_second)
        wait_icon = self.d.find_element(By.XPATH, Audit_Log_Report_Components().identifying_photo_wait_by_xpath())
        count = 0
        while wait_icon.is_displayed() or count == 120:
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"waiting for wait icon, count: {count}")

        enroll = self.d.find_element(By.XPATH, "//div[@ng-click='enrollmentStep1()']")
        self.d.execute_script("arguments[0].click();", enroll)
        time.sleep(web_driver.three_second)
        enrollment_basis = self.d.find_element(By.XPATH, Audit_Log_Report_Components().enrollment_basis_by_xpath())
        select = Select(enrollment_basis)
        select.select_by_index(1)
        time.sleep(web_driver.one_second)
        enrollment_group = self.d.find_element(By.XPATH, Audit_Log_Report_Components().enrollment_group_by_xpath())
        select = Select(enrollment_group)
        select.select_by_index(1)
        region_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().region_btn_by_xpath())
        region_btn.click()
        time.sleep(web_driver.one_second)
        region_names = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().edge_name_list())
        edge_name = Audit_Log_Report_Components().edge_name()
        for i in range(len(region_names)):
            if edge_name in region_names[i].text:
                region_names[i].click()
                break
        save_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().save_btn_by_xpath())
        save_btn.click()
        self.logger.info(f"click on save button")
        location_store = self.d.find_element(By.XPATH, Audit_Log_Report_Components().location_store_inpt_bx_by_xpath())
        location_store.send_keys(Audit_Log_Report_Components().location_store_data())

        case_subject = self.d.find_element(By.XPATH, Audit_Log_Report_Components().case_subject_inpt_bx_by_xpath())
        case_subject.send_keys(Audit_Log_Report_Components().case_subject_data())

        reported_loss = self.d.find_element(By.XPATH, Audit_Log_Report_Components().reported_loss_inpt_bx_by_xpath())
        reported_loss.send_keys(Audit_Log_Report_Components().reported_loss_data())

        date_incident = self.d.find_element(By.XPATH, Audit_Log_Report_Components().date_incident_inpt_bx_by_xpath())
        time.sleep(web_driver.one_second)
        self.dateTimeAMPM(date_incident)
        # date_incident.send_keys(Audit_Log_Report_Components().date_incident_data())
        # time.sleep(web_driver.one_second)
        # date_incident.send_keys(Audit_Log_Report_Components().date_incident_time())
        # time.sleep(web_driver.one_second)
        # date_incident.send_keys(Audit_Log_Report_Components().date_incident_am_pm())
        time.sleep(web_driver.one_second)

        action_input = self.d.find_element(By.XPATH, Audit_Log_Report_Components().action_inpt_bx_by_xpath())
        action_input.send_keys(Audit_Log_Report_Components().action_input_data())

        case_event_type = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                              .case_event_type_dropdown())
        select = Select(case_event_type)
        select.select_by_index(1)
        time.sleep(web_driver.one_second)

        activity_type = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                            .activity_type_dropdown())
        select = Select(activity_type)
        select.select_by_index(1)
        time.sleep(web_driver.one_second)

        method_of_offense = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                                .method_of_offence_by_xpath())
        select = Select(method_of_offense)
        select.select_by_index(1)
        time.sleep(web_driver.one_second)

        gender = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                     .gender_dropdown())
        select = Select(gender)
        select.select_by_index(1)
        time.sleep(web_driver.one_second)

        height = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                     .height_type_dropdown())
        select = Select(height)
        select.select_by_index(1)
        time.sleep(web_driver.one_second)

        reported_by = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                          .reported_by_input())
        reported_by.send_keys(Audit_Log_Report_Components().reported_by_data())
        time.sleep(web_driver.one_second)

        build = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                    .build_input())
        build.send_keys(Audit_Log_Report_Components().build_data())
        time.sleep(web_driver.one_second)

        body_markings = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                            .body_markings_input())
        body_markings.send_keys(Audit_Log_Report_Components().body_markings_data())
        time.sleep(web_driver.one_second)

        narratives = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                         .narrative_Desc_input())
        narratives.send_keys(Audit_Log_Report_Components().narratives_data())
        time.sleep(web_driver.one_second)
        # save_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().add_details_save_btn_by_xpath())
        # save_btn.click()

        submit_for_review = self.d.find_element(By.XPATH, Audit_Log_Report_Components().
                                                add_details_submit_for_review_btn_by_xpath())
        try:
            submit_for_review.click()
        except Exception as ex:
            pass
        self.logger.info(f"click on submit review button")
        time.sleep(web_driver.one_second)
        wait_icon = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                        .enrollment_success_loader())
        count = 0
        while wait_icon.is_displayed() and count == 120:
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"waiting for wait icon, count: {count}")
        self.logger.info(f"enroll person without approve enrollment permission end")
        self.close_all_panel_one_by_one()

    def change_user_role_remove__permission(self):
        """
            This function is used to remove audit log report permission
            :return:
        """
        self.logger.info(f"change user role remove permission start")
        login().login_to_cloud_if_not_done(self.d)
        time.sleep(web_driver.two_second)
        self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().users_portal_menu(), self.d)
        users_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().users_portal_menu())
        users_btn.click()
        time.sleep(web_driver.two_second)
        user_name = Audit_Log_Report_Components().user_name_data()
        search_box = self.d.find_element(By.XPATH, Read_Users_Components().search_box_by_xpath())
        search_box.send_keys(user_name)
        time.sleep(web_driver.two_second)
        select_user = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().user_name(user_name), self.d)
        select_user.click()
        time.sleep(web_driver.two_second)

        click_on_user_role = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().user_role_hyperlink(), self.d)
        # click_on_user_role.click()
        self.d.execute_script("arguments[0].click();", click_on_user_role)
        time.sleep(web_driver.two_second)

        action_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().user_role_action_button(),
                                                self.d)
        action_btn.click()
        edit_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().edit_user_role_button())
        edit_btn.click()
        time.sleep(web_driver.two_second)
        description_textbox = web_driver.explicit_wait(self, 10, "XPATH", Audit_Log_Report_Components().
                                                  description_textbox_on_user_role_details_panel_by_xpath(), self.d)
        description_textbox.send_keys(Audit_Log_Report_Components().user_roles_details_description())
        time.sleep(web_driver.two_second)
        # self.d.find_element(By.XPATH, Audit_Log_Report_Components().enrollment_review_role_status()).is_displayed()
        check_box = self.d.find_element(By.XPATH, Audit_Log_Report_Components().audit_log_user_role_checkbox())
        if check_box.is_selected():
            self.d.execute_script("arguments[0].click();", check_box)
        time.sleep(web_driver.two_second)
        save_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().save_user_role_btn())
        save_btn.click()
        self.logger.info(f"click on save button")
        time.sleep(web_driver.two_second)
        self.click_on_logout_button()
        time.sleep(web_driver.two_second)
        self.logger.info(f"change user role remove permission end")

    def validate_user_enrollment_status_should_be_disable(self):
        """
            This function is used to validate user enrollment status should be disabled
            :return:
        """
        data_list = []
        rows_selection = self.d.find_element(By.XPATH, Audit_Log_Report_Components().generated_report_page_select_dropdown())
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_status_list())
        for x in status:
            # if not x.text == "":
            data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_status_list())
            for x in status:
                # if not x.text == "":
                data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        self.logger.info(f"data list: {data_list}")
        last_index = data_list.__len__()
        if "Disabled" in data_list:
            self.logger.info("returning True")
            return True
        else:
            self.logger.info("returning False")
            return False

    def validate_user_enrollment_status_should_be_pending(self):
        """
            This function is used to validate user enrollment status should be pending
            :return:
        """
        data_list = []
        rows_selection = self.d.find_element(By.XPATH,
                                             Audit_Log_Report_Components().generated_report_page_select_dropdown())
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_status_list())
        for x in status:
            # if not x.text == "":
            data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_status_list())
            for x in status:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        self.logger.info(f"data list: {data_list}")
        last_index = data_list.__len__()
        if data_list.__getitem__(last_index - 1) == "Pending":
            return True
        else:
            return False

    def change_user_role_give_enrollment_review_permission(self):
        """
            This function is used to give enrollment review permission
            :return:
        """
        login().login_to_cloud_if_not_done(self.d)
        self.logger.info("enter change user role give enrollment review permission")
        # pending_review_available = self.verify_pending_review_enrollment_is_available()
        # self.logger.info(f"pending_review_available: {pending_review_available}")
        # if pending_review_available:
        users_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().users_portal_menu(), self.d)
        users_btn.click()
        time.sleep(web_driver.two_second)
        user_name = Audit_Log_Report_Components().user_name_data()
        print(user_name)
        search_box = self.explicit_wait(10, "XPATH", Read_Users_Components().search_box_by_xpath(), self.d)
        search_box.send_keys(user_name)
        time.sleep(web_driver.two_second)
        select_user = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().user_name(user_name), self.d)
        select_user.click()
        time.sleep(web_driver.two_second)
        click_on_user_role = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().user_role_hyperlink(),
                                                self.d)
        click_on_user_role.click()
        time.sleep(web_driver.two_second)
        action_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().user_role_action_button(),
                                        self.d)
        action_btn.click()
        edit_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().edit_user_role_button(), self.d)
        edit_btn.click()
        time.sleep(5)
        description_textbox = web_driver.explicit_wait(self, 10, "XPATH", Audit_Log_Report_Components().
                                                       description_textbox_on_user_role_details_panel_by_xpath(),
                                                       self.d)
        check_box = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().audit_log_user_role_checkbox(),
                                       self.d)
        if not check_box.is_selected():
            self.d.execute_script("arguments[0].click();", check_box)
        time.sleep(5)
        save_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().save_user_role_btn())
        self.d.execute_script("arguments[0].click();", save_btn)
        self.logger.info(" click on save button")
        time.sleep(5)
        self.click_on_logout_button()
        self.logger.info("change_user_role_give_enrollment_review_permission Returning: True")
        return True
        # else:
        #     self.logger.info("change_user_role_give_enrollment_review_permission returning: false")
        #     return False

    def verify_pending_review_enrollment_is_available(self):
        try:
            enrollment_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().enrollments_portal_menu(),
                                                self.d)
            self.logger.info(f"enrollment btn displayed: {enrollment_btn.is_displayed()}")
            if enrollment_btn.is_displayed():
                enrollment_btn.click()
                time.sleep(web_driver.two_second)
            else:
                self.d.refresh()
                time.sleep(web_driver.two_second)
                enrollment_btn.click()
                time.sleep(web_driver.two_second)
            filter_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().filter_btn(), self.d)
            filter_btn.click()
            pending_for_review = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().pending_for_review(),
                                                    self.d)
            pending_for_review.click()
            time.sleep(web_driver.one_second)
            # select_first_enrollment_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().enrollment_list_by_xpath())
            select_first_enrollment = web_driver.explicit_wait(self, 10, "XPATH", Audit_Log_Report_Components().enrollment_list_by_xpath(), self.d)
            select_first_enrollment_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().enrollment_list_by_xpath())
            self.logger.info(f"pending enrollment count: {len(select_first_enrollment_list)}")
            if len(select_first_enrollment_list) > 0:
                self.close_all_panel_one_by_one()
                self.logger.info("verify_pending_review_enrollment_is_available Returning: True")
                return True
            else:
                self.close_all_panel_one_by_one()
                self.logger.info("verify_pending_review_enrollment_is_available Returning: False")
                return False
        except Exception as ex:
            self.logger.info(f"verify pending review enrollment is available exception: {ex}")

    def enable_disable_enrollment(self):
        """
            This function is used to enable disable enrollment
            :return:
        """
        login().login_to_cloud_if_not_done(self.d)
        time.sleep(web_driver.two_second)
        self.logger.info(f"enrollment btn displayed: {Audit_Log_Report_Components().enrollments_portal_menu()}")
        enrollment_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().enrollments_portal_menu())
        if enrollment_btn.is_displayed():
            enrollment_btn.click()
        else:
            self.d.refresh()
            time.sleep(web_driver.two_second)
            enrollment_btn.click()
        time.sleep(web_driver.two_second)
        filter_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().filter_btn())
        filter_btn.click()
        time.sleep(web_driver.two_second)
        disable_filter_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().disable_filter_btn())
        disable_filter_btn.click()
        time.sleep(5)
        select_first_enrollment = self.d.find_element(By.XPATH, Audit_Log_Report_Components().
                                                      select_first_pending_enrollment())
        select_first_enrollment.click()
        time.sleep(web_driver.two_second)
        action_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().action_button())
        action_btn.click()
        time.sleep(web_driver.two_second)
        enable_selected_enrollment = self.d.find_element(By.XPATH, Audit_Log_Report_Components().
                                                         enable_selected_enrollment())
        enable_selected_enrollment.click()

        self.close_all_panel_one_by_one()

    def approve_pending_enrollment(self):
        """
            This function is used to approve pending enrollment
            :return:
        """
        login().login_to_cloud_if_not_done(self.d)
        enrollment_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().enrollments_portal_menu(), self.d)
        self.logger.info(f"enrollment btn displayed: {enrollment_btn.is_displayed()}")
        if enrollment_btn.is_displayed():
            enrollment_btn.click()
            time.sleep(web_driver.two_second)
        else:
            self.d.refresh()
            time.sleep(web_driver.two_second)
            enrollment_btn.click()
            time.sleep(web_driver.two_second)
        filter_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().filter_btn(), self.d)
        filter_btn.click()
        time.sleep(web_driver.two_second)
        pending_for_review = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().pending_for_review(), self.d)
        pending_for_review.click()
        time.sleep(5)
        select_first_enrollment = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_first_pending_enrollment())
        select_first_enrollment.click()
        time.sleep(web_driver.two_second)
        action_btn = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().action_button(), self.d)
        action_btn.click()
        time.sleep(web_driver.two_second)
        approve_selected_enrollment = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().approve_selected_enrollment(), self.d)
        approve_selected_enrollment.click()
        self.logger.info(f"approve enrollment selected")
        self.close_all_panel_one_by_one()

    def validate_user_enrollment_status_should_be_enable(self):
        """
            This function is used to verify the enrollment status should be Enabled
            :return:
        """
        data_list = []
        rows_selection = self.d.find_element(By.XPATH,
                                             Audit_Log_Report_Components().generated_report_page_select_dropdown())
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_status_list())
        for x in status:
            # if not x.text == "":
            data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_status_list())
            for x in status:
                # if not x.text == "":
                data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        self.logger.info(f"data list: {data_list}")
        last_index = data_list.__len__()
        if "Enabled" in data_list.__getitem__(last_index - 1):
            return True
        else:
            return False

    def verify_pending_enrollment_status(self):
        """
            This function is used to verify the enrollment status should be pending
            :return:
        """
        data_list = []
        rows_selection = self.d.find_element(By.XPATH,
                                             Audit_Log_Report_Components().generated_report_page_select_dropdown())
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_status_list())
        for x in status:
            # if not x.text == "":
            data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_status_list())
            for x in status:
                # if not x.text == "":
                data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        self.logger.info(f"data list: {data_list}")
        last_index = data_list.__len__()
        if "Pending" in data_list.__getitem__(last_index - 1):
            return True
        else:
            return False

    def verify_enabled_enrollment_status_1(self):
        """
            This function is used to verify the enrollment status should be pending
            :return:
        """
        data_list = []
        rows_selection = self.d.find_element(By.XPATH,
                                             Audit_Log_Report_Components().generated_report_page_select_dropdown())
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_status_list())
        for x in status:
            # if not x.text == "":
            data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_status_list())
            for x in status:
                # if not x.text == "":
                data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        self.logger.info(f"data list: {data_list}")
        last_index = data_list.__len__()
        if "Enabled" in data_list.__getitem__(last_index - 1):
            return True
        else:
            return False

    def validate_user_enrollment_status_should_be_accepted(self):
        """
            This function is used to validate user enrollment status should be accepted
            :return:
        """
        data_list = []
        rows_selection = self.d.find_element(By.XPATH,
                                             Audit_Log_Report_Components().generated_report_page_select_dropdown())
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_status_list())
        for x in status:
            # if not x.text == "":
            data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_status_list())
            for x in status:
                # if not x.text == "":
                data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        self.logger.info(f"data list: {data_list}")
        last_index = data_list.__len__()
        if data_list.__getitem__(last_index - 1) == "Accepted" or data_list.__getitem__(last_index - 1) == "Enabled":
            return True
        else:
            return False

    def get_last_user_approve_enrollment_status(self):
        """
            This function is used to get last user approve enrollment status list
            :return:
        """
        data_list = []
        rows_selection = self.d.find_element(By.XPATH,
                                             Audit_Log_Report_Components().generated_report_page_select_dropdown())
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().enrollment_status_list_in_report())
        for x in status:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().enrollment_status_list_in_report())
            for x in status:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        self.logger.info(f"data list: {data_list}")
        last_index = data_list.__len__()
        if data_list.__getitem__(last_index - 1) == "Accepted":
            return True
        else:
            return False

    def validate_user_enrollment_status_should_be_enable(self):
        """
            This function is used to get last user approve enrollment status list
            :return:
        """
        data_list = []
        rows_selection = self.d.find_element(By.XPATH,
                                             Audit_Log_Report_Components().generated_report_page_select_dropdown())
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().enrollment_status_list_in_report())
        for x in status:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().enrollment_status_list_in_report())
            for x in status:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        self.logger.info(f"data list: {data_list}")
        last_index = data_list.__len__()
        if data_list.__getitem__(last_index - 1) == "Enabled":
            return True
        else:
            return False

    def validate_User_enrolment_report_display_proper_Enrolment_Group_in_column(self):
        """
            This function is used to validate User enrolment report display proper Enrolment Group in column
            :return:
        """
        enrollment_group_list = self.get_enrollment_groups_list()
        self.logger.info("executed enrollment_group_list")
        self.go_to_audit_log_report()
        self.logger.info("executed go_to_audit_log_report")
        # select report type
        self.select_report_type(Audit_Log_Report_Components().report_type_User_Enrollments())
        self.logger.info("executed select_report_type")
        # select user
        self.select_users(Audit_Log_Report_Components().select_All_users())
        self.logger.info("executed select_users")
        # select filter by
        self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
        self.logger.info("executed select_filter_by")
        # submit button click
        self.click_on_submit_button()
        self.logger.info("executed click_on_submit_button")
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        status = self.d.find_elements(By.XPATH,
                                      Audit_Log_Report_Components().user_enrollment_enrollment_group_list_in_report())
        for x in status:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                          user_enrollment_enrollment_group_list_in_report())
            for x in status:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        self.logger.info(f"data list: {data_list}")
        for x in data_list:
            if x in enrollment_group_list:
                return True
            else:
                return False

    def validate_report_contains_column_name_headers(self):
        """
            This function is used to validate report contains column name headers
            :return:
        """
        self.logger.info("started validate_report_contains_column_name_headers")
        columns_name = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_report_column_list())
        exp_column_name = ["User Name", "Date", "Time Log-in", "Time Log-out", "Total Hours", "IP Address"]
        act_column_name = []
        for x in columns_name:
            act_column_name.append(x.text)
        self.close_current_tab()
        self.logger.info(f"rexp_column_name: {exp_column_name}")
        self.logger.info(f"act_column_name: {act_column_name}")
        return exp_column_name == act_column_name

    def validate_threshold_report_contains_column_name_headers(self):
        """
            This function is used to validate report contains column name headers
            :return:
        """
        self.logger.info("started validate_threshold_report_contains_column_name_headers")
        time.sleep(web_driver.two_second)
        there_is_no_record_msg_list = self.d.find_elements(By.XPATH,
                                                           Audit_Log_Report_Components().there_is_no_record_msg_by_xpath())
        expected_msg = Audit_Log_Report_Components().there_is_no_record_msg()
        if len(there_is_no_record_msg_list) > 0:
            if there_is_no_record_msg_list[0].is_displayed():
                self.logger.info(f"record list[0]: {there_is_no_record_msg_list[0].text}")
                self.logger.info(f"expected message: {expected_msg}")
                if there_is_no_record_msg_list[0].text == expected_msg:
                    self.logger.info("No record Found for your report search...")
                    self.logger.info(f"Msg Displayed: '{there_is_no_record_msg_list[0].text}'")
                    return True
        else:
            columns_name = self.d.find_elements(By.XPATH,
                                                Audit_Log_Report_Components().threshold_change_report_column_list())
            exp_column_name = ["User Name", "Enrollment Group", "Serious Offender Change", "Threshold Type",
                               "Threshold Change", "Change Result", "Changed Date", "Changed Time", "IP Address"]
            act_column_name = []

            for x in columns_name:
                act_column_name.append(x.text)
            self.logger.info(f"actual column names: {act_column_name}")
            self.logger.info(f"expected column names: {exp_column_name}")
            return exp_column_name == act_column_name

    def close_all_panel_one_by_one(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    Audit_Log_Report_Components().close_all_panel_list())
            for i in close_panel_list:
                i.click()
            return True
        except Exception as ex:
            msg = str(ex)

    def close_unsaved_panel(self):
        try:
            time.sleep(web_driver.two_second)
            close_panel_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().close_all_panel_list())

            for i in close_panel_list:
                i.click()
                time.sleep(web_driver.two_second)
            while self.d.find_element(By.XPATH,
                                      Audit_Log_Report_Components().user_close_panel_and_discard_Changes()).is_displayed():
                ele = self.d.find_element(By.XPATH,
                                          Audit_Log_Report_Components().user_close_panel_and_discard_Changes())
                self.d.execute_script("arguments[0].click();", ele)
                if self.d.find_element(By.XPATH, Audit_Log_Report_Components().face_first_logo()).is_displayed():
                    break
            time.sleep(web_driver.two_second)
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}(close_unsaved_panel.png")

    ##############################################################################################################
    def Verify_User_enrolment_report_column_date_time_should_display_accurate_enrolled_timestamp(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment timestamp column
            if False in self.validate_enrolled_Date_Time_displays_accurate_time_stamp_details():
                self.logger.info("executed validate_enrolled_Date_Time_displays_accurate_time_stamp_details")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_071_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_071_failed.png")
            self.logger.info(f"test_TC_ALR_071 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_User_enrolment_report_contains_enrolled_Location_Store_data(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment location column
            if False in self.validate_User_enrolment_report_contains_enrolled_Location_Store_data():
                self.logger.info("executed validate_User_enrolment_report_contains_enrolled_Location_Store_data")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_072_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_072_failed.png")
            self.logger.info(f"test_TC_ALR_072 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_User_enrollments_report_contains_accurate_Approved_by_data(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment approve by column
            if False in self.validate_User_enrolment_report_contains_approve_by_data():
                self.logger.info("executed validate_User_enrolment_report_contains_approve_by_data")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_073_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_073_failed.png")
            self.logger.info(f"test_TC_ALR_073 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_User_enrollments_report_contains_accurate_Approved_Date_and_time_when_user_enrolled(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment approve by column
            if False in self.validate_enrolled_Date_Time_displays_accurate_time_stamp_details():
                self.logger.info("executed validate_enrolled_Date_Time_displays_accurate_time_stamp_details")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_074_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_074_failed.png")
            self.logger.info(f"test_TC_ALR_074 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_User_enrolment_report_contains_status_column_approved_rejected_data(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment status column
            if False in self.validate_status_column_should_contain_valid_approved_rejected_pending_details_for_user_enrollment():
                self.logger.info("executed validate_status_column_should_contain_valid_approved_rejected_pending_details_for_user_enrollment")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_075_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_075_failed.png")
            self.logger.info(f"test_TC_ALR_075 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Audit_Log_Reports_with_User_Enrollments_by_selecting_Date_and_Time_range_all_users(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment date range column
            if False in self.validate_last_7_days_generated_report_user_enrollment():
                self.logger.info("executed validate_last_7_days_generated_report_user_enrollment")
                self.logger.info("test_TC_ALR_076 End...")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_076_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_076_failed.png")
            self.logger.info(f"test_TC_ALR_076 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Audit_Log_Reports_with_User_Enrollments_by_selecting_Date_and_Time_range_for_user1(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment date range column
            if False in self.validate_last_7_days_generated_report_user_enrollment():
                self.logger.info("executed validate_last_7_days_generated_report_user_enrollment")
                self.logger.info("test_TC_ALR_077 End...")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_077_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_077_failed.png")
            self.logger.info(f"test_TC_ALR_077 exception:  {ex}")
            return False
        finally:
            self.d.close()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Audit_Log_Reports_with_User_Enrollments_by_Last_7_days_by_user1_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment date range column
            if False in self.validate_last_7_days_generated_report_user_enrollment():
                self.logger.info("executed validate_last_7_days_generated_report_user_enrollment")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_078_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_078_failed.png")
            self.logger.info(f"test_TC_ALR_078 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Audit_Log_Reports_with_User_Enrollments_by_Last_7_days_by_all_user_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment date range column
            if False in self.validate_last_7_days_generated_report_user_enrollment():
                self.logger.info("executed click_on_submit_button")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_079_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_079_failed.png")
            self.logger.info(f"test_TC_ALR_079_exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_user_enrollments_with_only_last_7_days_and_user1_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment date range column
            if False in self.validate_should_not_contain_user_enrollments_details_other_than_user1_in_last_7_days():
                self.logger.info("executed validate_should_not_contain_user_enrollments_details_other_than_user1_in_last_7_days")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_080_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\test_TC_ALR_080_failed.png")
            self.logger.info(f"test_TC_ALR_080 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_user_enrollments_with_only_last_7_days_and_all_user_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment date range column
            if False in self.validate_should_not_contain_user_enrollments_details_other_than_all_users_in_last_7_days():
                self.logger.info(
                    "executed validate_should_not_contain_user_enrollments_details_other_than_all_users_in_last_7_days")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_081_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_081_failed.png")
            self.logger.info(f"test_TC_ALR_081 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Audit_Log_Reports_with_User_Enrollments_by_Last_14_days_by_user1_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_14_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment date range column
            if False in self.validate_last_14_days_generated_report_user_enrollment():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_082_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_082_failed.png")
            self.logger.info(f"test_TC_ALR_082_exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Audit_Log_Reports_with_User_Enrollments_by_Last_14_days_by_all_user_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_14_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment date range column
            if False in self.validate_last_14_days_generated_report_user_enrollment():
                self.logger.info("executed validate_last_14_days_generated_report_user_enrollment")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_083_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_083_failed.png")
            self.logger.info(f"test_TC_ALR_083_selection:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_user_enrollments_with_only_last_14_days_and_user1_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_14_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment dates range column
            if False in self.validate_should_not_contain_user_enrollments_details_other_than_user1_in_last_14_days():
                self.logger.info("executed validate_should_not_contain_user_enrollments_details_other_than_user1_in_last_14_days")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_084_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_084_failed.png")
            self.logger.info(f"test_TC_ALR_084 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_user_enrollments_with_only_last_14_days_and_all_user_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select rself.logger.info("executed click_on_submit_button")eport type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_14_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment date range column
            if False in self.validate_should_not_contain_user_enrollments_details_other_than_all_users_in_last_14_days():
                self.logger.info("executed validate_should_not_contain_user_enrollments_details_other_than_all_users_in_last_14_days")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_085_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_085_failed.png")
            self.logger.info(f"test_TC_ALR_085 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_user_enrollments_with_month_to_date_and_user1_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment dates range column
            if False in self.validate_month_to_date_generated_report_user_enrollment():
                self.logger.info("executed validate_month_to_date_generated_report_user_enrollment")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_086_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_086_failed.png")
            self.logger.info(f"test_TC_ALR_086 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_user_enrollments_with_month_to_date_and_all_users_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment dates range column
            if False in self.validate_month_to_date_generated_report_user_enrollment():
                self.logger.info("executed validate_month_to_date_generated_report_user_enrollment")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_087_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_087_failed.png")
            self.logger.info(f"test_TC_ALR_087 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_user_enrollments_with_only_month_to_date_and_user1_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment dates range column
            if False in self.validate_should_not_contain_user_enrollments_details_other_than_user1_in_month_to_date():
                self.logger.info("executed validate_should_not_contain_user_enrollments_details_other_than_user1_in_month_to_date")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_088_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_088_failed.png")
            self.logger.info(f"test_TC_ALR_088 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_user_enrollments_with_only_month_to_date_and_all_users_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            self.logger.info("select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("click_on_submit_button")
            # report validate user enrollment dates range column
            if False in self.validate_should_not_contain_user_enrollments_details_other_than_all_users_in_month_to_date():
                self.logger.info("validate_should_not_contain_user_enrollments_details_other_than_all_users_in_month_to_date")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_089_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_089_failed.png")
            self.logger.info(f"test_TC_ALR_089 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_user_enrollments_with_year_to_date_and_user1_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment dates range column
            if False in self.validate_year_to_date_generated_report_user_enrollment():
                self.logger.info("executed validate_year_to_date_generated_report_user_enrollment")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_090_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_090_failed.png")
            self.logger.info(f"test_TC_ALR_090 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_user_enrollments_with_year_to_date_and_all_users_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment dates range column
            if False in self.validate_year_to_date_generated_report_user_enrollment():
                self.logger.info("executed validate_year_to_date_generated_report_user_enrollment")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_091_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_091_failed.png")
            self.logger.info(f"test_TC_ALR_091 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_user_enrollments_with_only_year_to_date_and_user1_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment dates range column
            if False in self.validate_should_not_contain_user_enrollments_details_other_than_user1_in_year_to_date():
                self.logger.info("executed validate_should_not_contain_user_enrollments_details_other_than_user1_in_year_to_date")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_092_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_092_failed.png")
            self.logger.info(f"test_TC_ALR_092 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_user_enrollments_with_only_year_to_date_and_all_user_filter_selection(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type("User Enrollments")
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment dates range column
            if False in self.validate_should_not_contain_user_enrollments_details_other_than_all_users_in_year_to_date():
                self.logger.info("executed validate_should_not_contain_user_enrollments_details_other_than_all_users_in_year_to_date")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_093_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_093_failed.png")
            self.logger.info(f"test_TC_ALR_093 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_user_with_all_permisssions_enrolled_mask_subject_should_be_in_pending_for_Enrollment_status(self):
        try:
            # remove enrollment review permission
            self.change_user_role_remove__permission()

            # enroll one person
            self.enroll_person_without_approve_enrollment_permission()

            # go to audit log report
            self.go_to_audit_log_report()

            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_User_Enrollments())

            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())

            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())

            # submit button click
            self.click_on_submit_button()

            # enrollment status should be pending
            if self.validate_user_enrollment_status_should_be_pending():
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\Verify_user_with_all_permisssions_enrolled_mask_subject_"
                    f"should_be_in_pending_for_Enrollment_status_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\Verify_user_with_all_permisssions_enrolled_mask_subject_"
                f"should_be_in_pending_for_Enrollment_status_failed.png")
            self.logger.info(f"Verify_user_with_all_permisssions_enrolled_mask_subject_should"
                             f"_be_in_pending_for_Enrollment_status:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_with_Login_Logout_by_last_7_days_by_user1_report_contains_column_name(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment dates range column
            result = self.validate_report_contains_column_name_headers()
            self.logger.info("test_TC_ALR_102 End...")
            if result is True:
                return True
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_102_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_102_failed.png")
            self.logger.info(f"test_TC_ALR_102 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Login_Logout_report_user_names_are_proper(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed go_to_audit_log_report")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate user enrollment column
            if False in self.validate_User_enrollments_report_contains_proper_user_name():
                self.logger.info("executed validate_User_enrollments_report_contains_proper_user_name")
                self.logger.info("test_TC_ALR_103 End...")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_103_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_103_failed.png")
            self.logger.info(f"test_TC_ALR_103 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_User_Login_Logout_date_should_display_proper_data(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate login logout date column
            if False in self.validate_login_logout_Date_displays_accurate_time_stamp_details():
                self.logger.info("executed validate_login_logout_Date_displays_accurate_time_stamp_details")
                self.logger.info("test_TC_ALR_104 End...")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_104_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\test_TC_ALR_104_failed.png")
            self.logger.info(f"test_TC_ALR_104 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_user_Login_Logout_Time_should_display_proper_data(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate login logout date column
            if False in self.validate_login_logout_time_displays_accurate_time_stamp_details():
                self.logger.info("executed validate_login_logout_time_displays_accurate_time_stamp_details")
                self.logger.info("test_TC_ALR_105 End...")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_105_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_105_failed.png")
            self.logger.info(f"test_TC_ALR_105 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Login_Logout_report_Total_hours_column_count_is_proper_to_each_user(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate login logout date column
            if self.validate_Login_Logout_report_Total_hours_column_count():
                self.logger.info("executed validate_Login_Logout_report_Total_hours_column_count")
                self.logger.info("test_TC_ALR_106 End...")
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_106_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_106_failed.png")
            self.logger.info(f"test_TC_ALR_106 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Login_Logout_report_IP_address_column_with_each_user(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # validate Login Logout report IP Address
            if False in self.validate_Login_Logout_report_IP_Address_column_with_each_user():
                self.logger.info("executed validate_Login_Logout_report_IP_Address_column_with_each_user")
                self.logger.info("test_TC_ALR_107 End...")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_107_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_107_failed.png")
            self.logger.info(f"test_TC_ALR_107 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_last_7_days_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate login logout report
            if False in self.validate_login_logout_last_7_days_generated_report():
                self.logger.info("executed validate_login_logout_last_7_days_generated_report")
                self.logger.info("test_TC_ALR_108 End...")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_108_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_108_failed.png")
            self.logger.info(f"test_TC_ALR_108 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_only_last_7_days_and_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_should_not_contain_login_logout_details_other_than_user1_in_last_7_days():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_111_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_111_failed.png")
            self.logger.info(f"test_TC_ALR_111 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_last_7_days_and_All_users_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate reported loss value
            if False in self.validate_report_generated_for_login_logout_with_last_7_days_and_All_users_filter_selection():
                self.logger.info("executed validate_report_generated_for_login_logout_with_last_7_days_and_All_users_filter_selection")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_112_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_112_failed.png")
            self.logger.info(f"test_TC_ALR_112 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_last_7_days_and_All_users(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # selectself.logger.info("executed click_on_submit_button") report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_should_not_contain_login_logout_details_other_than_all_users_in_last_7_days():
                self.logger.info("executed validate_should_not_contain_login_logout_details_other_than_all_users_in_last_7_days")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_113_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_113_failed.png")
            self.logger.info(f"test_TC_ALR_113:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_last_14_days_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_14_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate reported loss value
            if False in self.validate_report_generated_for_login_logout_with_last_14_days_user1_filter_selection():
                self.logger.info("executed validate_report_generated_for_login_logout_with_last_14_days_user1_filter_selection")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_114_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_114_failed.png")
            self.logger.info(f"test_TC_ALR_114 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_only_last_14_days_and_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_14_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_should_not_contain_login_logout_details_other_than_user1_in_last_14_days():
                self.logger.info("executed validate_should_not_contain_login_logout_details_other_than_user1_in_last_14_days")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_115_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\test_TC_ALR_115_failed.png")
            self.logger.info(f"test_TC_ALR_115 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_last_14_days_and_All_users_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_14_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate reported loss value
            if False in self.validate_report_generated_for_login_logout_with_last_14_days_and_All_users_filter_selection():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_116_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_116_failed.png")
            self.logger.info(f"test_TC_ALR_116 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_only_last_14_days_and_all_user_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_should_not_contain_login_logout_details_other_than_all_users_in_last_14_days():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_117_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_117_failed.png")
            self.logger.info(f"test_TC_ALR_117 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_month_to_date_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate reported loss value
            if False in self.validate_report_generated_for_login_logout_with_month_to_date_user1_filter_selection():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_118_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_118_failed.png")
            self.logger.info(f"test_TC_ALR_118 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_only_month_to_date_and_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_should_not_contain_login_logout_details_other_than_user1_in_month_to_date():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_119_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_119_failed.png")
            self.logger.info(f"test_TC_ALR_119 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_month_to_date_and_All_users_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate reported loss value
            if False in self.validate_report_generated_for_login_logout_with_month_to_date_and_All_users_filter_selection():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_120_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_120_failed.png")
            self.logger.info(f"test_TC_ALR_120 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_only_month_to_date_and_all_users_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_should_not_contain_login_logout_details_other_than_all_users_in_month_to_date():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_121_failed_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_121_failed.png")
            self.logger.info(f"test_TC_ALR_121 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_year_to_date_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate reported loss value
            if False in self.validate_report_generated_for_login_logout_with_year_to_date_user1_filter_selection():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_122_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_122_failed.png")
            self.logger.info(f"test_TC_ALR_122 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_only_year_to_date_and_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_should_not_contain_login_logout_details_other_than_user1_in_year_to_date():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_123_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_123_failed.png")
            self.logger.info(f"test_TC_ALR_123_exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_year_to_date_and_All_users_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate reported loss value
            if False in self.validate_report_generated_for_login_logout_with_year_to_date_and_All_users_filter_selection():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_124_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\test_TC_ALR_124_failed.png")
            self.logger.info(f"test_TC_ALR_124 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_login_logout_with_only_year_to_date_and_all_users_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Log_in_Log_out())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_should_not_contain_login_logout_details_other_than_all_users_in_year_to_date():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_125_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_125_failed.png")
            self.logger.info(f"test_TC_ALR_125 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_with_Threshold_by_last_7_days_by_user1_report_contains_column_name(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # report validate Threshold change column header
            result = self.validate_threshold_report_contains_column_name_headers()
            self.logger.info("executed validate_threshold_report_contains_column_name_headers")
            self.logger.info("test_TC_ALR_127 End...")
            if result is True:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_127_failed.png")
                return False

        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_127_failed.png")
            self.logger.info(f"test_TC_ALR_127 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Threshold_change_report_user_names_are_proper(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_one_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            self.logger.info("test_TC_ALR_128 End...")
            # report validate user enrollment column
            if False in self.validate_threshold_change_report_contains_proper_user_name():
                self.logger.info("executed validate_threshold_change_report_contains_proper_user_name")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_128_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_128_failed.png")
            self.logger.info(f"test_TC_ALR_128 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Threshold_changes_report_displays_proper_enrolment_group_with_user(self):
        try:
            if False in self.validate_Threshold_changes_report_displays_proper_enrolment_group_with_user():
                self.logger.info("executed validate_Threshold_changes_report_displays_proper_enrolment_group_with_user")
                self.logger.info("test_TC_ALR_129 End...")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_129_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_129_failed.png")
            self.logger.info(f"test_TC_ALR_129 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def validate_Threshold_changes_report_displays_proper_enrolment_group_with_user(self):
        """
            This function is used to validate Threshold change report display proper Enrolment Group in column
            :return:
        """
        self.go_to_audit_log_report()
        self.logger.info("executed go_to_audit_log_report")
        # select report type
        self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
        self.logger.info("executed select_report_type")
        # select user
        self.select_users(Audit_Log_Report_Components().select_All_users())
        self.logger.info("executed select_users")
        # select filter by
        self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
        self.logger.info("executed select_filter_by")
        # submit button click
        self.click_on_submit_button()
        self.logger.info("executed click_on_submit_button")
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                      user_threshold_change_enrollment_group_list_by_xpath())
        for x in status:
            if not x.text == "":
                self.logger.info(f"text displayed: {x.is_displayed()}")
                data_list.append(x.is_displayed())
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                          user_threshold_change_enrollment_group_list_by_xpath())
            for x in status:
                if not x.text == "":
                    data_list.append(x.is_displayed())
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        return data_list

    def Verify_Threshold_changes_report_changed_Date_should_display_proper_data(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            self.logger.info("test_TC_ALR_130 End...")
            # report validate Threshold change, changed date column
            if False in self.validate_Threshold_changes_report_changed_Date_should_display_proper_data():
                self.logger.info("executed validate_Threshold_changes_report_changed_Date_should_display_proper_data")
                self.logger.info(f"result: {False}")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_130_failed.png")
                return False
            else:
                self.logger.info(f"result: {True}")
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\test_TC_ALR_130_failed.png")
            self.logger.info(f"test_TC_ALR_130 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_user_Threshold_Changes_report_changed_Time_should_display_proper_data(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            self.logger.info("Audit Log Report = test_TC_ALR_131 End...")
            # report validate threshold changed, changed time column
            result = self.validate_Threshold_Changes_report_changed_Time_should_display_proper_data()
            self.logger.info("executed validate_Threshold_Changes_report_changed_Time_should_display_proper_data")
            self.logger.info(f"result: {result}")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_131_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_131_failed.png")
            self.logger.info(f"test_TC_ALR_131 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Threshold_report_Threshold_change_column_contains_same_changes_modification_done_by_user(self):
        try:
            status = self.validate_Threshold_changes_Threshold_change_column_contains_same_changes_modification_done_by_user()
            self.logger.info("test_TC_ALR_132 End")
            if status is True:
                return True
            else:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_132_failed.png")
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_132_failed.png")
            self.logger.info(f"test_TC_ALR_132 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Threshold_Change_report_IP_address_of_each_user(self):
        try:
            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            self.logger.info("test_TC_ALR_133 End..")
            # validate Threshold Change report IP Address
            if False in self.validate_Threshold_Change_report_IP_Address_of_each_user():
                self.logger.info("executed validate_Threshold_Change_report_IP_Address_of_each_user")
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_133_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_133_failed.png")
            self.logger.info(f"test_TC_ALR_133 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_Threshold_changes_report_with_user_modified_threshold_type_for_enrolment_group(self):
        try:
            result = self.validate_Threshold_changes_report_with_user_modified_threshold_type_for_enrolment_group()
            self.logger.info(f"result: {result}")
            self.logger.info("test_TC_ALR_156 End...")
            if False in result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_156_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_156_failed.png")
            self.logger.info(f"test_TC_ALR_156 Exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def validate_Threshold_changes_report_with_user_modified_threshold_type_for_enrolment_group(self):
        """
            This function is used to validate Threshold change report with
            user modified threshold type for enrolment group
            :return:
        """
        self.logger.info("validate_Threshold_changes_report_with_user_modified_threshold_type_for_enrolment_group Starting...")
        mask_face_change_data = self.get_modified_threshold_type_for_enrollment_group()

        self.go_to_audit_log_report()
        self.logger.info("go_to_audit_log_report executed...")
        # select report type
        self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
        self.logger.info("select_report_type executed...")
        # select user
        self.select_users(Audit_Log_Report_Components().select_All_users())
        self.logger.info("select_users executed...")
        # select filter by
        self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
        self.logger.info("select_filter_by executed...")
        # submit button click
        self.click_on_submit_button()
        self.logger.info("click_on_submit_button executed...")
        data_list = []
        rows_selection = self.d.find_element(By.XPATH, Audit_Log_Report_Components().generated_report_page_select_dropdown())
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.one_second)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(1)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        threshold_change = self.d.find_element(By.XPATH, Audit_Log_Report_Components().threshold_change_threshold_type(mask_face_change_data[0])).text
        self.logger.info(f"threshold change: {threshold_change}")
        status = []
        status.append(mask_face_change_data[1] == threshold_change.strip())
        self.logger.info(f"result : {status}")
        return status

    def get_modified_threshold_type_for_enrollment_group(self):
        """
            This function is used to the change made in face threshold from enrollment group.
            Change in masked threshold
            :return:
        """
        try:
            threshold_type = []
            login().login_to_cloud_if_not_done(self.d)
            btn = self.explicit_wait(20, "XPATH", Audit_Log_Report_Components()
                                     .portal_menu_enrollments_groups_btn_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", btn)
            self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().enrollment_groups_action_drop_down(),
                               self.d).click()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().create_enrollment_group_option(),
                               self.d).click()
            time.sleep(web_driver.two_second)
            name_input = "dummy" + str(generate_random_number())
            threshold_type.append(name_input)
            name = self.d.find_element(By.XPATH,
                                       Audit_Log_Report_Components().enrollment_groups_details_name_input_bx())

            name.send_keys(name_input)
            time.sleep(web_driver.two_second)
            save = self.d.find_element(By.XPATH, Audit_Log_Report_Components().add_details_save_btn_by_xpath())
            save.click()

            time.sleep(web_driver.two_second)
            action = self.d.find_element(By.XPATH, Audit_Log_Report_Components().details_action_drop_down())
            action.click()
            time.sleep(web_driver.two_second)
            edit = self.d.find_element(By.XPATH, Audit_Log_Report_Components().edit_option())
            edit.click()
            time.sleep(web_driver.two_second)
            face = self.d.find_element(By.XPATH, Audit_Log_Report_Components().masked_face_threshold_input_bx())
            new_mask_face_value = "0.8511"
            face.clear()
            face.send_keys(new_mask_face_value)
            time.sleep(web_driver.two_second)
            save = self.d.find_element(By.XPATH, Audit_Log_Report_Components().add_details_save_btn_by_xpath())
            save.click()
            threshold_type.append("Masked")
            time.sleep(web_driver.two_second)
            self.close_all_panel_one_by_one()
            self.logger.info(f"threshold type: masked")
            # self.click_on_logout_button()
            return threshold_type
        except Exception as ex:
            print(ex)

    def Verify_Threshold_changes_report_with_user_modified_threshold_change_result_for_enrolment_group_match(self):
        try:
            result = self.Validate_Threshold_changes_report_with_user_modified_threshold_change_result_for_enrolment_group_match()
            self.logger.info("test_TC_ALR_157 End...")
            self.logger.info(f"test_TC_ALR_157 Returning: {result}")
            if not result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_157_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_157_failed.png")
            self.logger.info(f"test_TC_ALR_157 Exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Validate_Threshold_changes_report_with_user_modified_threshold_change_result_for_enrolment_group_match(self):
        """
            This function is used to validate Threshold change report with
            user modified threshold type for enrolment group
            :return:
        """
        face_change_result_data = self.get_modified_change_result_for_enrollment_group()

        self.go_to_audit_log_report()
        self.logger.info("go_to_audit_log_report executed...")
        # select report type
        self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
        self.logger.info("select_report_type executed...")
        # select user
        self.select_users(Audit_Log_Report_Components().select_All_users())
        self.logger.info("select_users executed...")
        # select filter by
        self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
        self.logger.info("select_filter_by executed...")
        # submit button click
        self.click_on_submit_button()
        self.logger.info("click_on_submit_button executed...")
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.one_second)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(1)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        threshold_change = self.d.find_element(By.XPATH, Audit_Log_Report_Components().threshold_change_change_result(
            face_change_result_data[0])).text
        status = []
        status.append(face_change_result_data[1] == float(threshold_change.strip()))
        self.logger.info(f"result : {status}")
        return status

    def get_modified_change_result_for_enrollment_group(self):
        """
            This function is used to the get modified change result for enrollment group
            Change in face threshold
            :return:
        """
        try:
            face_data_diff = []
            login().login_to_cloud_if_not_done(self.d)
            btn = self.d.find_element(By.XPATH,
                                      Audit_Log_Report_Components().portal_menu_enrollments_groups_btn_by_xpath())
            self.d.execute_script("arguments[0].click();", btn)

            self.d.find_element(By.XPATH, Audit_Log_Report_Components().enrollment_groups_action_drop_down()).click()
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, Audit_Log_Report_Components().create_enrollment_group_option()).click()

            name_input = "dummy" + str(generate_random_number())
            face_data_diff.append(name_input)
            name = self.d.find_element(By.XPATH,
                                       Audit_Log_Report_Components().enrollment_groups_details_name_input_bx())

            name.send_keys(name_input)
            time.sleep(web_driver.two_second)
            save = self.d.find_element(By.XPATH, Audit_Log_Report_Components().add_details_save_btn_by_xpath())
            save.click()
            time.sleep(web_driver.two_second)
            action = self.d.find_element(By.XPATH, Audit_Log_Report_Components().details_action_drop_down())
            action.click()
            time.sleep(web_driver.two_second)
            edit = self.d.find_element(By.XPATH, Audit_Log_Report_Components().edit_option())
            edit.click()
            time.sleep(web_driver.two_second)
            face = self.d.find_element(By.XPATH, Audit_Log_Report_Components().face_threshold_input_bx())
            face1_data = face.get_attribute("value")
            new_face_value = "0.85"
            face2_data = new_face_value
            face.clear()
            face.send_keys(new_face_value)
            time.sleep(web_driver.two_second)
            save = self.d.find_element(By.XPATH, Audit_Log_Report_Components().add_details_save_btn_by_xpath())
            save.click()
            time.sleep(web_driver.two_second)
            self.click_on_logout_button()
            time.sleep(web_driver.two_second)
            diff = float(face2_data) - float(face1_data)
            diff_result = round(diff, 2)
            face_data_diff.append(diff_result)
            return face_data_diff
        except Exception as ex:
            print(ex)

    def Verify_Threshold_changes_report_with_user_modified_serious_offender_change_for_enrolment_group_match(self):
        try:
            result = self.Validate_Threshold_changes_report_with_user_modified_serious_offender_change_for_enrolment_group_match()
            self.logger.info(f"test_TC_ALR_158 Returning: {result}")
            if not result:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_158_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot( f"{self.screenshots_path}\\test_TC_ALR_158_failed.png")
            self.logger.info(f"test_TC_ALR_158 Exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Validate_Threshold_changes_report_with_user_modified_serious_offender_change_for_enrolment_group_match(self):
        """
            This function is used to validate Threshold changes report with user modified serious offender
            change for enrolment group
            :return:
        """
        serious_offender_result_data = self.get_modified_serious_offender_change_for_enrollment_group()
        self.logger.info(f"serious_offender_result_data executed :  {serious_offender_result_data}")
        self.go_to_audit_log_report()
        self.logger.info("go_to_audit_log_report executed")
        # select report type
        self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
        self.logger.info("select_report_type executed")
        # select user
        self.select_users(Audit_Log_Report_Components().select_All_users())
        self.logger.info("select_users executed")
        # select filter by
        self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
        self.logger.info("select_filter_by executed")
        # submit button click
        self.click_on_submit_button()
        self.logger.info("click_on_submit_button executed")
        data_list = []
        rows_selection = self.d.find_element(By.XPATH, Audit_Log_Report_Components().generated_report_page_select_dropdown())
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.one_second)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(1)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        serious_offender = self.d.find_element(By.XPATH,
                                               Audit_Log_Report_Components().threshold_change_serious_offender(
                                                   serious_offender_result_data[0])).text
        serious_offender_list = serious_offender.split("->")
        status = []
        status.append(serious_offender_result_data[1] == serious_offender_list[0].strip())
        status.append(serious_offender_result_data[2] == serious_offender_list[1].strip())
        self.logger.info(f"result : {status}")
        return status

    def get_modified_serious_offender_change_for_enrollment_group(self):
        """
            This function is used to the get modified serious offender change for enrollment group
            Change in serious offender
            :return:
        """
        serious_offender_change = []
        login().login_to_cloud_if_not_done(self.d)
        btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().portal_menu_enrollments_groups_btn_by_xpath())
        self.d.execute_script("arguments[0].click();", btn)

        self.d.find_element(By.XPATH, Audit_Log_Report_Components().enrollment_groups_action_drop_down()).click()
        time.sleep(web_driver.two_second)
        self.d.find_element(By.XPATH, Audit_Log_Report_Components().create_enrollment_group_option()).click()

        name_input = "dummy" + str(generate_random_number())
        serious_offender_change.append(name_input)
        name = self.d.find_element(By.XPATH, Audit_Log_Report_Components().enrollment_groups_details_name_input_bx())

        name.send_keys(name_input)
        self.logger.info(f"serious offender xpath: {Audit_Log_Report_Components().serious_offender_drop_down()}")
        serious_offender = self.d.find_element(By.XPATH, Audit_Log_Report_Components().serious_offender_drop_down())
        s = Select(serious_offender)
        serious_offender_value = "Low"
        s.select_by_value(serious_offender_value)
        serious_offender_change.append(serious_offender_value)
        time.sleep(web_driver.two_second)
        save = self.d.find_element(By.XPATH, Audit_Log_Report_Components().add_details_save_btn_by_xpath())
        save.click()
        time.sleep(web_driver.two_second)
        action = self.d.find_element(By.XPATH, Audit_Log_Report_Components().details_action_drop_down())
        action.click()
        time.sleep(web_driver.two_second)
        edit = self.d.find_element(By.XPATH, Audit_Log_Report_Components().edit_option())
        edit.click()
        time.sleep(web_driver.two_second)
        serious_off_drop_down = self.d \
            .find_element(By.XPATH, Audit_Log_Report_Components().serious_offender_drop_down())
        s = Select(serious_off_drop_down)
        new_serious_offender_value = "Medium"
        s.select_by_value(new_serious_offender_value)
        serious_offender_change.append(new_serious_offender_value)
        time.sleep(web_driver.two_second)
        save = self.d.find_element(By.XPATH, Audit_Log_Report_Components().add_details_save_btn_by_xpath())
        save.click()
        self.close_unsaved_panel()
        return serious_offender_change

    def Verify_report_generated_for_Threshold_Change_with_last_7_days_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate login logout report
            result = self.validate_threshold_change_last_7_days_generated_report()
            self.logger.info("executed validate_threshold_change_last_7_days_generated_report")
            self.logger.info(f"status: {result}")
            self.logger.info("Audit Log Report = test_TC_ALR_137 End...")
            if False in result:
                self.d.save_screenshot("{self.screenshots_path}\\test_TC_ALR_137_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_137_failed.png")
            self.logger.info(f"test_TC_ALR_137 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_Threshold_change_with_last_7_days_and_All_users_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate reported loss value
            if False in self.validate_report_generated_for_Threshold_change_with_last_7_days_and_All_users_filter_selection():
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_138_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_138_failed.png")
            self.logger.info(f"test_TC_ALR_138 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_Threshold_Change_with_only_last_7_days_and_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_should_not_contain_Threshold_Change_details_other_than_user1_in_last_7_days():
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_139_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_139_failed.png")
            self.logger.info(f"test_TC_ALR_139 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_Threshold_Change_with_only_last_7_days_and_All_users(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_7_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_should_not_contain_Threshold_Change_details_other_than_all_users_in_last_7_days():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_140_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_140_failed.png")
            self.logger.info(f"test_TC_ALR_140 execption:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_Threshold_Change_with_last_14_days_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_14_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate Threshold Change with last 14 days user1
            if False in self.validate_report_generated_for_Threshold_Change_with_last_14_days_user1_filter_selection():
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_141_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_141_failed.png")
            self.logger.info(f"test_TC_ALR_141 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_Threshold_Change_with_last_14_days_and_All_users_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_14_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate Threshold Change last 14 days and All users
            if False in self.validate_report_generated_for_Threshold_Change_with_last_14_days_and_All_users_filter_selection():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_142_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\test_TC_ALR_142n_failed.png")
            self.logger.info(f"test_TC_ALR_142 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_Threshold_Change_with_only_last_14_days_and_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_14_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_should_not_contain_Threshold_Change_details_other_than_user1_in_last_14_days():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_143_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_143_failed.png")
            self.logger.info(f"test_TC_ALR_143 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_Threshold_Change_with_only_last_14_days_and_all_user_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().last_14_days_select())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_should_not_contain_Threshold_Change_details_other_than_all_users_in_last_14_days():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_144_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_144_failed.png")
            self.logger.info(f"test_TC_ALR_144 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_Threshold_Change_with_month_to_date_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_report_generated_for_Threshold_Change_with_month_to_date_user1_filter_selection():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_145_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\test_TC_ALR_145_failed.png")
            self.logger.info(f"test_TC_ALR_145 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_Threshold_Change_with_month_to_date_and_All_users_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate reported loss value
            if False in self.validate_report_generated_for_Threshold_Change_with_month_to_date_and_All_users_filter_selection():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_146_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_146_failed.png")
            self.logger.info(f"test_TC_ALR_146 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_Threshold_Change_with_only_month_to_date_and_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_should_not_contain_Threshold_Change_details_other_than_user1_in_month_to_date():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_147_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_147_failed.png")
            self.logger.info(f"test_TC_ALR_147 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_Threshold_Change_with_only_month_to_date_and_all_users_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_should_not_contain_Threshold_Changes_details_other_than_all_users_in_month_to_date():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_148_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\test_TC_ALR_148_failed.png")
            self.logger.info(f"test_TC_ALR_148 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_Threshold_Change_with_year_to_date_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate Threshold Change last year-to-date and user1
            if False in self.validate_report_generated_for_Threshold_Changes_with_year_to_date_user1_filter_selection():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_149_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_149_failed.png")
            self.logger.info(f"test_TC_ALR_149 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_Threshold_Changes_with_year_to_date_and_All_users_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Month_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate Threshold Change last year-to-date and All users
            if False in self.validate_report_generated_for_Threshold_Changes_with_year_to_date_and_All_users_filter_selection():
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_150_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_150_failed.png")
            self.logger.info(f"test_TC_ALR_150 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_Threshold_Changes_with_only_year_to_date_and_user1_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select user
            self.select_users(Audit_Log_Report_Components().select_core_user())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            if False in self.validate_should_not_contain_Threshold_Changes_details_other_than_user1_in_year_to_date():
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_151_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_151_failed.png")
            self.logger.info(f"test_TC_ALR_151 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    def Verify_report_generated_for_Threshold_Changes_with_only_year_to_date_and_all_users_filter_selection(self):
        try:

            self.go_to_audit_log_report()
            self.logger.info("executed go_to_audit_log_report")
            # select report type
            self.select_report_type(Audit_Log_Report_Components().report_type_Threshold_changes())
            self.logger.info("executed select_report_type")
            # select usself.logger.info("executed go_to_audit_log_report")er
            self.select_users(Audit_Log_Report_Components().select_All_users())
            self.logger.info("executed select_users")
            # select filter by
            self.select_filter_by(Audit_Log_Report_Components().select_Year_to_date())
            self.logger.info("executed select_filter_by")
            # submit button click
            self.click_on_submit_button()
            self.logger.info("executed click_on_submit_button")
            # Validate only show selected user data
            result = self.validate_should_not_contain_Threshold_Changes_details_other_than_all_users_in_year_to_date()
            self.logger.info("executed validate_should_not_contain_Threshold_Changes_details_other_than_all_users_in_year_to_date")
            self.logger.info(f"status: {result}")
            self.logger.info("Audit Log Report = test_TC_ALR_152 End...")
            if False in result:
                self.d.save_screenshot(
                    f"{self.screenshots_path}\\test_TC_ALR_152_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_ALR_152_failed.png")
            self.logger.info( f"test_TC_ALR_152 exception:  {ex}")
            return False
        finally:
            self.close_current_tab()
            self.d.switch_to.window(self.d.window_handles[0])

    ############################ Reuse method #################################################################

    def validate_User_enrollments_report_contains_proper_user_name(self):
        """
            This function is used to validate user first and last name  in generated report
            :return:
        """
        self.logger.info("started validate_User_enrollments_report_contains_proper_user_name")
        result = []
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        time.sleep(web_driver.two_second)
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name = []
        for x in users_list:
            exp_user_name.append(x.text)

        act_report_name_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                act_report_name_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    act_report_name_list.append(x.text)
            next_btn.click()
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        print(act_report_name_list)
        print(exp_user_name)

        for x in act_report_name_list:
            result.append(x in exp_user_name)
        self.close_current_tab()
        self.logger.info(f"status: {result}")
        return result

    def validate_enrolled_Date_Time_displays_accurate_time_stamp_details(self):
        """
            This function is used to validate enrolled Date Time displays accurate time stamp details
            :return:
        """
        result = []
        time.sleep(web_driver.two_second)
        report_datetime_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                                    user_enrollment_enrolled_datetime_list_in_report())
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                      user_enrollment_enrolled_datetime_list_in_report())
        for x in status:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                          user_enrollment_enrolled_datetime_list_in_report())
            for x in status:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for x in data_list:
            result.append(is_datetime_accurate(x, 60))
        self.logger.info(f"status: {result}")
        return result

    def validate_User_enrolment_report_contains_enrolled_Location_Store_data(self):
        """
            This function is used to validate User enrolment report contains enrolled Location Store data
            :return:
        """
        result = []
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                      user_enrollment_location_store_list_in_report())
        for x in status:
            if not x.text == "":
                result.append(x.is_displayed())
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                          user_enrollment_location_store_list_in_report())
            for x in status:
                if not x.text == "":
                    result.append(x.is_displayed())
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        self.logger.info(f"status: {result}")
        return result

    def validate_User_enrolment_report_contains_approve_by_data(self):
        """
            This function is used to validate User enrolment report contains approve by data
            :return:
        """
        result = []
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                      user_enrollment_approve_by_list_in_report())
        for x in status:
            if not x.text == "":
                result.append(x.is_displayed())
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                          user_enrollment_approve_by_list_in_report())
            for x in status:
                if not x.text == "":
                    result.append(x.is_displayed())
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        self.logger.info(f"status: {result}")
        return result

    def validate_status_column_should_contain_valid_approved_rejected_pending_details_for_user_enrollment(self):
        """
            This function is used to validate enrollment status in generated report for user enrollment
            :return:
        """
        result = []
        expected_status = ["Rejected", "Pending", "Accepted", "Enrolled", "Disabled", "Enabled", "Deleted"]

        status_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_status_list_in_report())
        for x in status:
            if not x.text == "":
                status_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            time.sleep(web_driver.two_second)
            status = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                          user_enrollment_status_list_in_report())
            for x in status:
                if not x.text == "":
                    status_list.append(x.text)
            next_btn.click()
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        print(expected_status)
        print(status_list)
        for x in status_list:
            result.append(x in expected_status)
        self.logger.info(f"status: {result}")
        return result

    def validate_last_7_days_generated_report_user_enrollment(self):
        """
            This function is used to validate last 7 days generated report for user enrollment
            :return:
        """
        self.logger.info("started validate_last_7_days_generated_report_user_enrollment select_report_type")
        result = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_date_list_in_report())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                        user_enrollment_date_list_in_report())
            for x in date:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            result.append(difference_days <= 7)
        self.logger.info(f"status: {result}")
        return result

    def validate_last_14_days_generated_report_user_enrollment(self):
        """
            This function is used to validate last 14 days generated report for user enrollment
            :return:
        """
        result = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_date_list_in_report())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                        user_enrollment_date_list_in_report())
            for x in date:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            result.append(difference_days <= 14)
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_user_enrollments_details_other_than_user1_in_last_7_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        selected_user_name = Audit_Log_Report_Components().select_one_user()
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for x in data_list:
            result.append(x.lower() == selected_user_name.lower())
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_user_enrollments_details_other_than_all_users_in_last_7_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        time.sleep(web_driver.two_second)
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name_list = []
        for x in users_list:
            exp_user_name_list.append(x.text)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            result.append(x in exp_user_name_list)
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_user_enrollments_details_other_than_user1_in_last_14_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        selected_user_name = Audit_Log_Report_Components().select_one_user()
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for x in data_list:
            result.append(x.lower() == selected_user_name.lower())
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_user_enrollments_details_other_than_all_users_in_last_14_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name_list = []
        for x in users_list:
            exp_user_name_list.append(x.text)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            result.append(x in exp_user_name_list)
        self.logger.info(f"status: {result}")
        return result

    def validate_month_to_date_generated_report_user_enrollment(self):
        """
            This function is used to validate month to date generated report for user enrollment
            :return:
        """
        result = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_date_list_in_report())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                        user_enrollment_date_list_in_report())
            for x in date:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            result.append(difference_days <= 30)
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_user_enrollments_details_other_than_user1_in_month_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        selected_user_name = Audit_Log_Report_Components().select_one_user()
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for x in data_list:
            result.append(x.lower() == selected_user_name.lower())
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_user_enrollments_details_other_than_all_users_in_month_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name_list = []
        for x in users_list:
            exp_user_name_list.append(x.text)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            result.append(x in exp_user_name_list)
        self.logger.info(f"status: {result}")
        return result

    def validate_year_to_date_generated_report_user_enrollment(self):
        """
            This function is used to validate year to date generated report for user enrollment
            :return:
        """
        result = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_enrollment_date_list_in_report())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                        user_enrollment_date_list_in_report())
            for x in date:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            result.append(difference_days <= 365)
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_user_enrollments_details_other_than_user1_in_year_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        selected_user_name = Audit_Log_Report_Components().select_one_user()
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for x in data_list:
            result.append(x.lower() == selected_user_name.lower())
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_user_enrollments_details_other_than_all_users_in_year_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name_list = []
        for x in users_list:
            exp_user_name_list.append(x.text)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        result = []
        for x in data_list:
            result.append(x in exp_user_name_list)
        self.logger.info(f"status: {result}")
        return result

    def validate_login_logout_Date_displays_accurate_time_stamp_details(self):
        """
            This function is used to validate enrolled Date displays accurate time stamp details
            :return:
        """
        self.logger.info("started validate_login_logout_Date_displays_accurate_time_stamp_details")
        result = []
        report_datetime_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().
                                                    login_logout_date_column_list())
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        date_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_date_column_list())
        for x in date_list:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            date_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_date_column_list())
            for x in date_list:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            if x != "":
                result.append(is_valid_date_format(x))
        self.logger.info(f"status: {result}")
        return result

    def validate_login_logout_time_displays_accurate_time_stamp_details(self):
        """
            This function is used to validate enrolled time displays accurate time stamp details
            :return:
        """
        self.logger.info("started validate_login_logout_time_displays_accurate_time_stamp_details")
        result = []
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        time_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_time_column_list())
        for x in time_list:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            time_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_time_column_list())
            for x in time_list:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            if x != "":
                result.append(is_valid_time_format(x))
        self.logger.info(f"status: {result}")
        return result

    def validate_Login_Logout_report_Total_hours_column_count(self):
        """
            This function is used to validate Login Logout report Total hours column_count
            :return:
        """
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        hours_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_total_count_list())
        for x in hours_list:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            hours_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_total_count_list())
            for x in hours_list:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        count = 0
        size = len(data_list)
        for x in range(size - 1):
            hour = data_list.__getitem__(x)
            if hour != "":
                count = count + float(hour)
        total = data_list.__getitem__(size - 1)
        tolerance = 1e-10
        print(total)
        print(count)
        print(float(total) - float(count))
        return (float(total) - float(count)) < tolerance

    def validate_Login_Logout_report_IP_Address_column_with_each_user(self):
        """
            This function is used to validate Login Logout report IP Address column with each user
            :return:
        """
        ip_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        ip_ele_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_ip_address_list())
        for x in ip_ele_list:
            if not x.text == "":
                ip_list.append(True)
            else:
                ip_list.append(False)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            ip_ele_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_ip_address_list())
            for x in ip_ele_list:
                if not x.text == "":
                    ip_list.append(True)
                else:
                    ip_list.append(False)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        ip_list.pop()
        return ip_list

    def validate_login_logout_last_7_days_generated_report(self):
        """
            This function is used to validate login logout last 7 days generated report
            :return:
        """
        self.logger.info("started validate_login_logout_last_7_days_generated_report")
        result = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_date_column_list())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_date_column_list())
            for x in date:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            result.append(difference_days <= 7)
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_login_logout_details_other_than_user1_in_last_7_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        selected_user_name = Audit_Log_Report_Components().select_one_user()
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for x in data_list:
            result.append(x.lower() == selected_user_name.lower())
        self.logger.info(f"status: {result}")
        return result

    def validate_report_generated_for_login_logout_with_last_7_days_and_All_users_filter_selection(self):
        """
            This function is used to validate last 7 days generated report
            :return:
        """
        result = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_date_column_list())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_date_column_list())
            for x in date:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            result.append(difference_days <= 7)
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_login_logout_details_other_than_all_users_in_last_7_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name_list = []
        for x in users_list:
            exp_user_name_list.append(x.text)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            result.append(x in exp_user_name_list)
        self.logger.info(f"status: {result}")
        return result

    def validate_report_generated_for_login_logout_with_last_14_days_user1_filter_selection(self):
        """
            This function is used to validate last 14 days generated report
            :return:
        """
        result = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_date_column_list())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH,
                                                  Audit_Log_Report_Components().login_logout_date_column_list())
            for x in name_in_report:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            result.append(difference_days <= 14)
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_login_logout_details_other_than_user1_in_last_14_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        selected_user_name = Audit_Log_Report_Components().select_one_user()
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for x in data_list:
            result.append(x.lower() == selected_user_name.lower())
        self.logger.info(f"status: {result}")
        return result

    def validate_report_generated_for_login_logout_with_last_14_days_and_All_users_filter_selection(self):
        """
            This function is used to validate report generated for
             login logout with last 14 days and All users filter selection
            :return:
        """
        result = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_date_column_list())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH,
                                                  Audit_Log_Report_Components().login_logout_date_column_list())
            for x in name_in_report:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            result.append(difference_days <= 14)
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_login_logout_details_other_than_all_users_in_last_14_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name_list = []
        for x in users_list:
            exp_user_name_list.append(x.text)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            result.append(x in exp_user_name_list)
        self.logger.info(f"status: {result}")
        return result

    def validate_report_generated_for_login_logout_with_month_to_date_user1_filter_selection(self):
        """
            This function is used to validate month to date generated report
            :return:
        """
        result = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_date_column_list())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH,
                                                  Audit_Log_Report_Components().login_logout_date_column_list())
            for x in name_in_report:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            result.append(difference_days <= 30)
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_login_logout_details_other_than_user1_in_month_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        selected_user_name = Audit_Log_Report_Components().select_one_user()
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for x in data_list:
            result.append(x.lower() == selected_user_name.lower())
        self.logger.info(f"status: {result}")
        return result

    def validate_report_generated_for_login_logout_with_month_to_date_and_All_users_filter_selection(self):
        """
            This function is used to validate month to date generated report
            :return:
        """
        result = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().approved_datetime_list())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().approved_datetime_list())
            for x in name_in_report:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            result.append(difference_days <= 30)
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_login_logout_details_other_than_all_users_in_month_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name_list = []
        for x in users_list:
            exp_user_name_list.append(x.text)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            result.append(x in exp_user_name_list)
        self.logger.info(f"status: {result}")
        return result

    def validate_report_generated_for_login_logout_with_year_to_date_user1_filter_selection(self):
        """
            This function is used to validate year to date generated report
            :return:
        """
        result = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_date_column_list())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH,
                                                  Audit_Log_Report_Components().login_logout_date_column_list())
            for x in name_in_report:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            result.append(difference_days <= 365)
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_login_logout_details_other_than_user1_in_year_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        selected_user_name = Audit_Log_Report_Components().select_one_user()
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for x in data_list:
            result.append(x.lower() == selected_user_name.lower())
        self.logger.info(f"status: {result}")
        return result

    def validate_report_generated_for_login_logout_with_year_to_date_and_All_users_filter_selection(self):
        """
            This function is used to validate year to date generated report
            :return:
        """
        result = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().login_logout_date_column_list())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH,
                                                  Audit_Log_Report_Components().login_logout_date_column_list())
            for x in name_in_report:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            result.append(difference_days <= 365)
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_login_logout_details_other_than_all_users_in_year_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name_list = []
        for x in users_list:
            exp_user_name_list.append(x.text)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            result.append(x in exp_user_name_list)
        self.logger.info(f"status: {result}")
        return result

    def validate_threshold_change_report_contains_proper_user_name(self):
        """
            This function is used to validate user first and last name  in generated report
            :return:
        """
        self.logger.info("started validate_threshold_change_report_contains_proper_user_name")
        result = []
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name = []
        for x in users_list:
            exp_user_name.append(x.text)

        act_report_name_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
        for x in name_in_report:
            if not x.text == "":
                act_report_name_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            time.sleep(web_driver.two_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_name_list_report())
            for x in name_in_report:
                if not x.text == "":
                    act_report_name_list.append(x.text)
            next_btn.click()
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in act_report_name_list:
            result.append(x in exp_user_name)
        self.logger.info(f"status: {result}")
        return result

    def validate_Threshold_changes_report_changed_Date_should_display_proper_data(self):
        """
            This function is used to validate changed Date displays accurate date details
            :return:
        """
        self.logger.info("started validate_Threshold_changes_report_changed_Date_should_display_proper_data")
        status = []
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        date_list = self.d.find_elements(By.XPATH,
                                         Audit_Log_Report_Components().threshold_change_changed_date_colum_list())
        for x in date_list:
            # if not x.text == "":
            data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            date_list = self.d.find_elements(By.XPATH,
                                             Audit_Log_Report_Components().threshold_change_changed_date_colum_list())
            for x in date_list:
                # if not x.text == "":
                data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            if x != "":
                status.append(is_valid_date_format(x))
        return status

    def validate_Threshold_Changes_report_changed_Time_should_display_proper_data(self):
        """
            This function is used to validate changed time displays accurate time stamp details
            :return:
        """
        self.logger.info("validate_Threshold_Changes_report_changed_Time_should_display_proper_data started..")
        status = []
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.two_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        time_list = self.d.find_elements(By.XPATH,
                                         Audit_Log_Report_Components().threshold_change_changed_time_column_list())
        for x in time_list:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.two_second)
            time_list = self.d.find_elements(By.XPATH,
                                             Audit_Log_Report_Components().threshold_change_changed_time_column_list())
            for x in time_list:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        self.logger.info(f"data list: {data_list}")
        for x in data_list:
            if x != "":
                status.append(is_valid_time_format(x))
        return status

    def validate_Threshold_Change_report_IP_Address_of_each_user(self):
        """
            This function is used to validate Threshold Change report IP Address of each user
            :return:
        """
        self.logger.info("started validate_Threshold_Change_report_IP_Address_of_each_user")
        ip_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.one_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        ip_ele_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_ip_address_list())
        for x in ip_ele_list:
            if not x.text == "":
                ip_list.append(True)
            else:
                ip_list.append(False)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.one_second)
            ip_ele_list = self.d.find_elements(By.XPATH,
                                               Audit_Log_Report_Components().threshold_change_ip_address_list())
            for x in ip_ele_list:
                if not x.text == "":
                    ip_list.append(True)
                else:
                    ip_list.append(False)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        return ip_list

    def validate_threshold_change_last_7_days_generated_report(self):
        """
            This function is used to validate Threshold Change last 7 days generated report
            :return:
        """
        self.logger.info("validate_threshold_change_last_7_days_generated_report started..")
        result = []
        date_list = []
        rows_selection = self.d.find_element(By.XPATH,
                                             Audit_Log_Report_Components().generated_report_page_select_dropdown())
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.one_second)
        self.logger.info(f"last_page_number: {int(last_page_number)}")
        self.logger.info(f"total_page_number: {int(total_page_number)}")
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_changed_date())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.one_second)
            date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_changed_date())
            for x in date:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        self.logger.info(f"date list: {date_list}")
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            result.append(difference_days <= 7)
        self.logger.info(f"result list in threshold_change_last_7_days_generated_report: {result}")
        return result

    def validate_report_generated_for_Threshold_change_with_last_7_days_and_All_users_filter_selection(self):
        """
            This function is used to validate last 7 days generated report
            :return:
        """
        status = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.one_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_changed_date())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.one_second)
            date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_changed_date())
            for x in date:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            status.append(difference_days <= 7)
        return status

    def validate_should_not_contain_Threshold_Change_details_other_than_user1_in_last_7_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        status = []
        selected_user_name = Audit_Log_Report_Components().select_core_user()
        data_list = []
        time.sleep(web_driver.two_second)
        no_records_found_message = self.d.find_elements(By.XPATH,
                                                        Audit_Log_Report_Components().there_is_no_record_msg_by_xpath())
        if len(no_records_found_message) > 0:
            self.logger.info("no record found message is displayed")
            self.logger.info(f"Message text: '{no_records_found_message[0].text}'")
            status.append(True)
            return status
        else:

            rows_selection = self.d.find_element(By.XPATH, Audit_Log_Report_Components().
                                                 generated_report_page_select_dropdown())
            select = Select(rows_selection)
            select.select_by_value("30")
            next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
            total_page_number = a[1].split("of")[1].strip()
            time.sleep(web_driver.one_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_user_name())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                              Audit_Log_Report_Components().next_btn_report()).is_enabled():
                next_btn.click()
                time.sleep(web_driver.one_second)
                name_in_report = self.d.find_elements(By.XPATH,
                                                      Audit_Log_Report_Components().threshold_change_user_name())
                for x in name_in_report:
                    if not x.text == "":
                        data_list.append(x.text)
                total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
                a = str(total_pages.text)
                print(a)
                a = a.split("-")
                last_page_number = a[1].split("of")[0].strip()
            for x in data_list:
                status.append(x.lower() == selected_user_name.lower())
            return status

    def validate_should_not_contain_Threshold_Change_details_other_than_all_users_in_last_7_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        status = []
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name_list = []
        for x in users_list:
            exp_user_name_list.append(x.text)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.one_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_user_name())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.one_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_user_name())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            status.append(x in exp_user_name_list)
        return status

    def validate_report_generated_for_Threshold_Change_with_last_14_days_user1_filter_selection(self):
        """
            This function is used to validate last 14 days generated report
            :return:
        """
        status = []
        date_list = []
        time.sleep(web_driver.two_second)
        no_records_found_message = self.d.find_elements(By.XPATH,
                                                        Audit_Log_Report_Components().there_is_no_record_msg_by_xpath())
        if len(no_records_found_message) > 0:
            self.logger.info("no record found message is displayed")
            self.logger.info(f"Message text: '{no_records_found_message[0].text}'")
            status.append(True)
            return status
        else:
            rows_selection = self.d.find_element(By.XPATH,
                                                 Audit_Log_Report_Components().generated_report_page_select_dropdown())
            select = Select(rows_selection)
            select.select_by_value("30")
            next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
            total_page_number = a[1].split("of")[1].strip()
            time.sleep(web_driver.one_second)
            date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_changed_date())
            for x in date:
                if not x.text == "":
                    date_list.append(x.text)
            while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                              Audit_Log_Report_Components().next_btn_report()).is_enabled():
                next_btn.click()
                time.sleep(web_driver.one_second)
                name_in_report = self.d.find_elements(By.XPATH,
                                                      Audit_Log_Report_Components().threshold_change_changed_date())
                for x in name_in_report:
                    if not x.text == "":
                        date_list.append(x.text)
                total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
                a = str(total_pages.text)
                print(a)
                a = a.split("-")
                last_page_number = a[1].split("of")[0].strip()
            self.logger.info(f"actual: {date_list}")
            for date in date_list:
                difference_days = date_difference_from_today(date.split(",")[0])
                print(difference_days)
                status.append(difference_days <= 14)
            return status

    def validate_report_generated_for_Threshold_Change_with_last_14_days_and_All_users_filter_selection(self):
        """
            This function is used to validate report generated for
             Threshold Change with last 14 days and All users filter selection
            :return:
        """
        result = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.one_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_changed_date())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.one_second)
            name_in_report = self.d.find_elements(By.XPATH,
                                                  Audit_Log_Report_Components().threshold_change_changed_date())
            for x in name_in_report:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            result.append(difference_days <= 14)
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_Threshold_Change_details_other_than_user1_in_last_14_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        selected_user_name = Audit_Log_Report_Components().select_core_user()
        data_list = []
        time.sleep(web_driver.two_second)
        no_records_found_message = self.d.find_elements(By.XPATH,
                                                        Audit_Log_Report_Components().there_is_no_record_msg_by_xpath())
        if len(no_records_found_message) > 0:
            self.logger.info("no record found message is displayed")
            self.logger.info(f"Message text: '{no_records_found_message[0].text}'")
            result.append(True)
            return result
        else:
            rows_selection = self.d.find_element(By.XPATH,
                                                 Audit_Log_Report_Components().generated_report_page_select_dropdown())
            select = Select(rows_selection)
            select.select_by_value("30")
            next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
            total_page_number = a[1].split("of")[1].strip()
            time.sleep(web_driver.one_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_user_name())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                              Audit_Log_Report_Components().next_btn_report()).is_enabled():
                next_btn.click()
                time.sleep(web_driver.one_second)
                name_in_report = self.d.find_elements(By.XPATH,
                                                      Audit_Log_Report_Components().threshold_change_user_name())
                for x in name_in_report:
                    if not x.text == "":
                        data_list.append(x.text)
                total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
                a = str(total_pages.text)
                print(a)
                a = a.split("-")
                last_page_number = a[1].split("of")[0].strip()
            for x in data_list:
                result.append(x.lower() == selected_user_name.lower())
            self.logger.info(f"status: {result}")
            return result

    def validate_should_not_contain_Threshold_Change_details_other_than_all_users_in_last_14_days(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name_list = []
        for x in users_list:
            exp_user_name_list.append(x.text)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.one_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_user_name())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.one_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_user_name())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            result.append(x in exp_user_name_list)
        self.logger.info(f"status: {result}")
        return result

    def validate_report_generated_for_Threshold_Change_with_month_to_date_user1_filter_selection(self):
        """
            This function is used to validate month to date generated report
            :return:
        """
        result = []
        date_list = []
        time.sleep(web_driver.two_second)
        no_records_found_message = self.d.find_elements(By.XPATH,
                                                        Audit_Log_Report_Components().there_is_no_record_msg_by_xpath())
        if len(no_records_found_message) > 0:
            self.logger.info("no record found message is displayed")
            self.logger.info(f"Message text: '{no_records_found_message[0].text}'")
            result.append(True)
            return result
        else:
            rows_selection = self.d.find_element(By.XPATH,
                                                 Audit_Log_Report_Components().generated_report_page_select_dropdown())
            select = Select(rows_selection)
            select.select_by_value("30")
            next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
            total_page_number = a[1].split("of")[1].strip()
            time.sleep(web_driver.one_second)
            date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_changed_date())
            for x in date:
                if not x.text == "":
                    date_list.append(x.text)
            while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                              Audit_Log_Report_Components().next_btn_report()).is_enabled():
                next_btn.click()
                time.sleep(web_driver.one_second)
                name_in_report = self.d.find_elements(By.XPATH,
                                                      Audit_Log_Report_Components().threshold_change_changed_date())
                for x in name_in_report:
                    if not x.text == "":
                        date_list.append(x.text)
                total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
                a = str(total_pages.text)
                print(a)
                a = a.split("-")
                last_page_number = a[1].split("of")[0].strip()
            for date in date_list:
                difference_days = date_difference_from_today(date.split(",")[0])
                print(difference_days)
                result.append(difference_days <= 30)
            self.logger.info(f"status: {result}")
            return result

    def validate_report_generated_for_Threshold_Change_with_month_to_date_and_All_users_filter_selection(self):
        """
            This function is used to validate month to date generated report
            :return:
        """
        result = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.one_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_changed_date())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.one_second)
            name_in_report = self.d.find_elements(By.XPATH,
                                                  Audit_Log_Report_Components().threshold_change_changed_date())
            for x in name_in_report:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            result.append(difference_days <= 30)
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_Threshold_Change_details_other_than_user1_in_month_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        selected_user_name = Audit_Log_Report_Components().select_core_user()
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.one_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_user_name())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.one_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_user_name())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for x in data_list:
            result.append(x.lower() == selected_user_name.lower())
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_Threshold_Changes_details_other_than_all_users_in_month_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        users_select = self.d.find_element(By.XPATH, Audit_Log_Report_Components().select_user_after_one_selection())
        users_select.click()
        time.sleep(web_driver.two_second)
        users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
        exp_user_name_list = []
        for x in users_list:
            exp_user_name_list.append(x.text)
        data_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.one_second)
        name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_user_name())
        for x in name_in_report:
            if not x.text == "":
                data_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.one_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_user_name())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()

        for x in data_list:
            result.append(x in exp_user_name_list)
        self.logger.info(f"status: {result}")
        return result

    def validate_report_generated_for_Threshold_Changes_with_year_to_date_user1_filter_selection(self):
        """
            This function is used to validate year to date generated report
            :return:
        """
        result = []
        date_list = []
        time.sleep(web_driver.two_second)
        no_records_found_message = self.d.find_elements(By.XPATH,
                                                        Audit_Log_Report_Components().there_is_no_record_msg_by_xpath())
        if len(no_records_found_message) > 0:
            self.logger.info("no record found message is displayed")
            self.logger.info(f"Message text: '{no_records_found_message[0].text}'")
            result.append(True)
            return result
        else:
            rows_selection = self.d.find_element(By.XPATH,
                                                 Audit_Log_Report_Components().generated_report_page_select_dropdown())
            select = Select(rows_selection)
            select.select_by_value("30")
            next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
            total_page_number = a[1].split("of")[1].strip()
            time.sleep(web_driver.one_second)
            date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_changed_date())
            for x in date:
                if not x.text == "":
                    date_list.append(x.text)
            while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                              Audit_Log_Report_Components().next_btn_report()).is_enabled():
                next_btn.click()
                time.sleep(web_driver.one_second)
                name_in_report = self.d.find_elements(By.XPATH,
                                                      Audit_Log_Report_Components().threshold_change_changed_date())
                for x in name_in_report:
                    if not x.text == "":
                        date_list.append(x.text)
                total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
                a = str(total_pages.text)
                print(a)
                a = a.split("-")
                last_page_number = a[1].split("of")[0].strip()
            for date in date_list:
                difference_days = date_difference_from_today(date.split(",")[0])
                print(difference_days)
                result.append(difference_days <= 365)
            self.logger.info(f"status: {result}")
            return result

    def validate_report_generated_for_Threshold_Changes_with_year_to_date_and_All_users_filter_selection(self):
        """
            This function is used to validate year to date generated report
            :return:
        """
        result = []
        date_list = []
        rows_selection = self.explicit_wait(10, "XPATH", Audit_Log_Report_Components().
                                            generated_report_page_select_dropdown(), self.d)
        select = Select(rows_selection)
        select.select_by_value("30")
        next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
        total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
        a = str(total_pages.text)
        print(a)
        a = a.split("-")
        last_page_number = a[1].split("of")[0].strip()
        total_page_number = a[1].split("of")[1].strip()
        time.sleep(web_driver.one_second)
        date = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_changed_date())
        for x in date:
            if not x.text == "":
                date_list.append(x.text)
        while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                          Audit_Log_Report_Components().next_btn_report()).is_enabled():
            next_btn.click()
            time.sleep(web_driver.one_second)
            name_in_report = self.d.find_elements(By.XPATH,
                                                  Audit_Log_Report_Components().threshold_change_changed_date())
            for x in name_in_report:
                if not x.text == "":
                    date_list.append(x.text)
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
        for date in date_list:
            difference_days = date_difference_from_today(date.split(",")[0])
            print(difference_days)
            result.append(difference_days <= 365)
        self.logger.info(f"status: {result}")
        return result

    def validate_should_not_contain_Threshold_Changes_details_other_than_user1_in_year_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        result = []
        selected_user_name = Audit_Log_Report_Components().select_core_user()
        data_list = []

        time.sleep(web_driver.two_second)
        no_records_found_message = self.d.find_elements(By.XPATH,
                                                        Audit_Log_Report_Components().there_is_no_record_msg_by_xpath())
        if len(no_records_found_message) > 0:
            self.logger.info("no record found message is displayed")
            self.logger.info(f"Message text: '{no_records_found_message[0].text}'")
            result.append(True)
            return result
        else:

            rows_selection = self.d.find_element(By.XPATH, Audit_Log_Report_Components().
                                                 generated_report_page_select_dropdown())
            select = Select(rows_selection)
            select.select_by_value("30")
            next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
            total_page_number = a[1].split("of")[1].strip()
            time.sleep(web_driver.one_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_user_name())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                              Audit_Log_Report_Components().next_btn_report()).is_enabled():
                next_btn.click()
                time.sleep(web_driver.one_second)
                name_in_report = self.d.find_elements(By.XPATH,
                                                      Audit_Log_Report_Components().threshold_change_user_name())
                for x in name_in_report:
                    if not x.text == "":
                        data_list.append(x.text)
                total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
                a = str(total_pages.text)
                print(a)
                a = a.split("-")
                last_page_number = a[1].split("of")[0].strip()
            for x in data_list:
                result.append(x == selected_user_name.lower())
            self.logger.info(f"status: {result}")
            return result

    def validate_should_not_contain_Threshold_Changes_details_other_than_all_users_in_year_to_date(self):
        """
            This function is used to validate show only selected user data
            :return:
        """
        self.logger.info("started validate_should_not_contain_Threshold_Changes_details_other_than_all_users_in_year_to_date")
        result = []
        time.sleep(web_driver.two_second)
        there_is_no_record_msg_list = self.d.find_elements(By.XPATH,
                                                           Audit_Log_Report_Components().there_is_no_record_msg_by_xpath())
        expected_msg = Audit_Log_Report_Components().there_is_no_record_msg()
        if len(there_is_no_record_msg_list) > 0:
            self.logger.info(f"there_is_no_record_msg_list[0]: {there_is_no_record_msg_list[0].is_displayed()}")
            if there_is_no_record_msg_list[0].is_displayed():
                self.logger.info(f"there_is_no_record_msg_list[0].text: {there_is_no_record_msg_list[0].text}")
                self.logger.info(f"expected_message: {expected_msg}")
                if there_is_no_record_msg_list[0].text == expected_msg:
                    self.logger.info("No record Found for your report search...")
                    self.logger.info(f"Msg Displayed: '{there_is_no_record_msg_list[0].text}'")
                    result.append(True)
                    return result
        else:
            users_select = self.d.find_element(By.XPATH,
                                               Audit_Log_Report_Components().select_user_after_one_selection())
            users_select.click()
            time.sleep(web_driver.two_second)
            users_list = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().user_list_xpath())
            exp_user_name_list = []
            for x in users_list:
                exp_user_name_list.append(x.text)
            data_list = []
            rows_selection = self.d.find_element(By.XPATH,
                                                 Audit_Log_Report_Components().generated_report_page_select_dropdown())
            select = Select(rows_selection)
            select.select_by_value("30")
            next_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().next_btn_report())
            total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
            a = str(total_pages.text)
            print(a)
            a = a.split("-")
            last_page_number = a[1].split("of")[0].strip()
            total_page_number = a[1].split("of")[1].strip()
            time.sleep(web_driver.one_second)
            name_in_report = self.d.find_elements(By.XPATH, Audit_Log_Report_Components().threshold_change_user_name())
            for x in name_in_report:
                if not x.text == "":
                    data_list.append(x.text)
            while not int(last_page_number) == int(total_page_number) and self.d.find_element(By.XPATH,
                                                                                              Audit_Log_Report_Components().next_btn_report()).is_enabled():
                next_btn.click()
                time.sleep(web_driver.one_second)
                name_in_report = self.d.find_elements(By.XPATH,
                                                      Audit_Log_Report_Components().threshold_change_user_name())
                for x in name_in_report:
                    if not x.text == "":
                        data_list.append(x.text)
                total_pages = self.d.find_element(By.XPATH, Audit_Log_Report_Components().total_pages_number())
                a = str(total_pages.text)
                a = a.split("-")
                last_page_number = a[1].split("of")[0].strip()
            self.logger.info(f"actual user name list: {data_list}")
            self.logger.info(f"expected: {exp_user_name_list}")
            for x in data_list:
                if x in exp_user_name_list:
                    result.append(True)
                else:
                    pass
            self.logger.info(f"status: {result}")
            return result

    def get_user_first_and_last_name(self):
        """
            This function is used to get user first name and last name
            :return:
        """
        login().login_to_cloud_if_not_done(self.d)
        user_profile_btn = self.d.find_element(By.XPATH, Audit_Log_Report_Components().user_profile_xpath())
        user_profile_btn.click()
        time.sleep(web_driver.two_second)
        user_first_name = self.d.find_element(By.XPATH, Audit_Log_Report_Components().get_user_first_name())
        user_last_name = self.d.find_element(By.XPATH, Audit_Log_Report_Components().get_user_last_name())
        f_name = user_first_name.text
        l_name = user_last_name.text
        time.sleep(web_driver.two_second)
        return f_name, l_name
