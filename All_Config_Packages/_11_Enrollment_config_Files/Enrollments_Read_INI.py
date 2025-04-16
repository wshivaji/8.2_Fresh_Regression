import configparser
from pathlib import Path


class Read_Enrollments_Components:
    def __init__(self):

        self.config = configparser.RawConfigParser()

        try:
            portal_menu_ini_file_path = f'{Path(__file__).parent.parent.parent}\\All_Test_Data\\11_Enrollment_Module\\Data_From_INI\\Enrollments.ini'
            # Base_Class.logger.info("File location: ", deployment_manager_ini_file_path)
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.config.read(portal_menu_ini_file_path)
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def get_Launching_url(self):
        url = self.common_test_data_config.get("Login_Logout_Data", "cloud_login_url")
        print("launching webportal login page", url)
        return url

    def get_expecting_title_webportal_login(self):
        expected_title = self.common_test_data_config.get("Login_Logout_Data", "portal_title")
        print("expected title of webportal login page", expected_title)
        return expected_title

    def get_logo_is_visible_on_login_page(self):
        logo = self.config.get("login_locators", "logo_image_by_xpath")
        print("logo of webportal login page", logo)
        return logo

    def get_username_textbox(self):
        username = self.config.get("login_locators", "username_textbox_by_xpath")
        print("username texbox", username)
        return username

    def get_password_textbox(self):
        password = self.config.get("login_locators", "password_textbox_by_xpath")
        print("password textbox", password)
        return password

    def get_cloudlogin_button(self):
        cloud_menu = self.config.get("login_locators", "cloudlogin_button_by_xpath")
        print("cloud menu button", cloud_menu)
        return cloud_menu

    def get_valid_username(self):
        valid_username = self.common_test_data_config.get("Login_Logout_Data", "username")
        print("valid username is", valid_username)
        return valid_username

    def get_valid_password(self):
        valid_password = self.common_test_data_config.get("Login_Logout_Data", "password")
        print("valid password is", valid_password)
        return valid_password

    def get_cloud_menu(self):
        cloud_menu = self.config.get("login_locators", "cloud_menu")
        print("cloud menu is displayed", cloud_menu)
        return cloud_menu

    def enrollments_link_by_xpath(self):
        try:
            enrollments_link_by_xpath = self.config.get("LOCATORS", "enrollments_link_by_xpath")
            return enrollments_link_by_xpath
        except Exception as ex:
            print("enrollments_link_by_xpath : ", ex)

    def expiration_start_date_check_bx_by_xpath(self):
        try:
            expiration_start_date_check_bx_by_xpath = self.config.get("LOCATORS",
                                                                      "expiration_start_date_check_bx_by_xpath")
            return expiration_start_date_check_bx_by_xpath
        except Exception as ex:
            print("expiration_start_date_check_bx_by_xpath : ", ex)

    def expiration_end_date_check_bx_by_xpath(self):
        try:
            expiration_end_date_check_bx_by_xpath = self.config.get("LOCATORS", "expiration_end_date_check_bx_by_xpath")
            return expiration_end_date_check_bx_by_xpath
        except Exception as ex:
            print("expiration_end_date_check_bx_by_xpath : ", ex)

    def expiration_start_date_input_bx_by_xpath(self):
        try:
            expiration_start_date_input_bx_by_xpath = self.config.get("LOCATORS",
                                                                      "expiration_start_date_input_bx_by_xpath")
            return expiration_start_date_input_bx_by_xpath
        except Exception as ex:
            print("expiration_start_date_input_bx_by_xpath : ", ex)

    def expiration_end_date_input_bx_by_xpath(self):
        try:
            expiration_end_date_input_bx_by_xpath = self.config.get("LOCATORS", "expiration_end_date_input_bx_by_xpath")
            return expiration_end_date_input_bx_by_xpath
        except Exception as ex:
            print("expiration_end_date_input_bx_by_xpath : ", ex)

    def expiration_filter_result_by_xpath(self):
        try:
            expiration_filter_result_by_xpath = self.config.get("LOCATORS", "expiration_filter_result_by_xpath")
            print(expiration_filter_result_by_xpath)
            return expiration_filter_result_by_xpath
        except Exception as ex:
            print("expiration_filter_result_by_xpath : ", ex)

    def search_drop_down_by_xpath(self):
        try:
            search_drop_down_by_xpath = self.config.get("LOCATORS", "search_drop_down_by_xpath")
            return search_drop_down_by_xpath
        except Exception as ex:
            print("search_drop_down_by_xpath : ", ex)

    def location_store_txt_bx_by_xpath(self):
        try:
            location_store_txt_bx_by_xpath = self.config.get("LOCATORS", "location_store_txt_bx_by_xpath")
            return location_store_txt_bx_by_xpath
        except Exception as ex:
            print("location_store_txt_bx_by_xpath : ", ex)

    def case_subject_txt_bx_by_xpath(self):
        try:
            case_subject_txt_bx_by_xpath = self.config.get("LOCATORS", "case_subject_txt_bx_by_xpath")
            return case_subject_txt_bx_by_xpath
        except Exception as ex:
            print("case_subject_txt_bx_by_xpath : ", ex)

    def exact_text_search_check_bx_by_xpath(self):
        try:
            exact_text_search_check_bx_by_xpath = self.config.get("LOCATORS", "exact_text_search_check_bx_by_xpath")
            return exact_text_search_check_bx_by_xpath
        except Exception as ex:
            print("exact_text_search_check_bx_by_xpath : ", ex)

    def enrollment_start_date_check_bx_by_xpath(self):
        try:
            enrollment_start_date_check_bx_by_xpath = self.config\
                .get("LOCATORS", "enrollment_start_date_check_bx_by_xpath")
            return enrollment_start_date_check_bx_by_xpath
        except Exception as ex:
            print("enrollment_start_date_check_bx_by_xpath : ", ex)

    def enrollment_end_date_check_bx_by_xpath(self):
        try:
            enrollment_end_date_check_bx_by_xpath = self.config.get("LOCATORS", "enrollment_end_date_check_bx_by_xpath")
            return enrollment_end_date_check_bx_by_xpath
        except Exception as ex:
            print("enrollment_end_date_check_bx_by_xpath : ", ex)

    def enroll_start_date_check_bx_by_xpath(self):
        try:
            enroll_start_date_check_bx_by_xpath = self.config\
                .get("LOCATORS", "enroll_start_date_check_bx_by_xpath")
            return enroll_start_date_check_bx_by_xpath
        except Exception as ex:
            print("enroll_start_date_check_bx_by_xpath : ", ex)

    def enroll_end_date_check_bx_by_xpath(self):
        try:
            enroll_end_date_check_bx_by_xpath = self.config.get("LOCATORS", "enroll_end_date_check_bx_by_xpath")
            return enroll_end_date_check_bx_by_xpath
        except Exception as ex:
            print("enroll_end_date_check_bx_by_xpath : ", ex)

    def enrollment_start_date_input_bx_by_xpath(self):
        try:
            enrollment_start_date_input_bx_by_xpath = self.config\
                .get("LOCATORS", "enrollment_start_date_input_bx_by_xpath")
            return enrollment_start_date_input_bx_by_xpath
        except Exception as ex:
            print("enrollment_start_date_input_bx_by_xpath : ", ex)

    def enrollment_end_date_input_bx_by_xpath(self):
        try:
            enrollment_end_date_input_bx_by_xpath = self.config.get("LOCATORS", "enrollment_end_date_input_bx_by_xpath")
            return enrollment_end_date_input_bx_by_xpath
        except Exception as ex:
            print("enrollment_end_date_input_bx_by_xpath : ", ex)

    def enroll_start_date_input_bx_by_xpath(self):
        try:
            enroll_start_date_input_bx_by_xpath = self.config\
                .get("LOCATORS", "enroll_start_date_input_bx_by_xpath")
            return enroll_start_date_input_bx_by_xpath
        except Exception as ex:
            print("enroll_start_date_input_bx_by_xpath : ", ex)

    def enroll_end_date_input_bx_by_xpath(self):
        try:
            enroll_end_date_input_bx_by_xpath = self.config.get("LOCATORS", "enroll_end_date_input_bx_by_xpath")
            return enroll_end_date_input_bx_by_xpath
        except Exception as ex:
            print("enroll_end_date_input_bx_by_xpath : ", ex)

    def sort_by_by_xpath(self):
        try:
            sort_by_by_xpath = self.config.get("LOCATORS", "sort_by_by_xpath")
            return sort_by_by_xpath
        except Exception as ex:
            print("sort_by_by_xpath : ", ex)

    def clear_btn_by_xpath(self):
        try:
            clear_btn_by_xpath = self.config.get("LOCATORS", "clear_btn_by_xpath")
            return clear_btn_by_xpath
        except Exception as ex:
            print("clear_btn_by_xpath : ", ex)

    def search_btn_by_xpath(self):
        try:
            search_btn_by_xpath = self.config.get("LOCATORS", "search_btn_by_xpath")
            return search_btn_by_xpath
        except Exception as ex:
            print("search_btn_by_xpath : ", ex)

    def location_store_filter_result_by_xpath(self):
        try:
            location_store_filter_result_by_xpath = self.config.get("LOCATORS", "location_store_filter_result_by_xpath")
            return location_store_filter_result_by_xpath
        except Exception as ex:
            print("location_store_filter_result_by_xpath : ", ex)

    def case_subject_filter_result_by_xpath(self):
        try:
            case_subject_filter_result_by_xpath = self.config.get("LOCATORS", "case_subject_filter_result_by_xpath")
            return case_subject_filter_result_by_xpath
        except Exception as ex:
            print("case_subject_filter_result_by_xpath : ", ex)

    def enrolled_filter_result_by_xpath(self):
        try:
            enrolled_filter_result_by_xpath = self.config.get("LOCATORS", "enrolled_filter_result_by_xpath")
            return enrolled_filter_result_by_xpath
        except Exception as ex:
            print("enrolled_filter_result_by_xpath : ", ex)

    def enroll_filter_result_by_xpath(self):
        try:
            enroll_filter_result_by_xpath = self.config.get("LOCATORS", "enroll_filter_result_by_xpath")
            return enroll_filter_result_by_xpath
        except Exception as ex:
            print("enroll_filter_result_by_xpath : ", ex)

    def calender_timer_icon_by_xpath(self):
        try:
            calender_timer_icon_by_xpath = self.config.get("LOCATORS", "calender_timer_icon_by_xpath")
            return calender_timer_icon_by_xpath
        except Exception as ex:
            print("calender_timer_icon_by_xpath : ", ex)

    def period_by_xpath(self):
        try:
            period_by_xpath = self.config.get("LOCATORS", "period_by_xpath")
            return period_by_xpath
        except Exception as ex:
            print("period_by_xpath : ", ex)

    def calender_tick_icon_by_xpath(self):
        try:
            calender_tick_icon_by_xpath = self.config.get("LOCATORS", "calender_tick_icon_by_xpath")
            return calender_tick_icon_by_xpath
        except Exception as ex:
            print("calender_tick_icon_by_xpath : ", ex)

    def calender_back_button_by_xpath(self):
        try:
            calender_back_button_by_xpath = self.config.get("LOCATORS", "calender_back_button_by_xpath")
            return calender_back_button_by_xpath
        except Exception as ex:
            print("calender_back_button_by_xpath : ", ex)

    def calender_month_year_by_xpath(self):
        try:
            calender_month_year_by_xpath = self.config.get("LOCATORS", "calender_month_year_by_xpath")
            return calender_month_year_by_xpath
        except Exception as ex:
            print("calender_month_year_by_xpath : ", ex)

    def calender_forward_button_by_xpath(self):
        try:
            calender_forward_button_by_xpath = self.config.get("LOCATORS", "calender_forward_button_by_xpath")
            return calender_forward_button_by_xpath
        except Exception as ex:
            print("calender_forward_button_by_xpath : ", ex)

    def current_minute_element_by_xpath(self):
        try:
            current_minute_element_by_xpath = self.config.get("LOCATORS", "current_minute_element_by_xpath")
            return current_minute_element_by_xpath
        except Exception as ex:
            print("current_minute_element_by_xpath : ", ex)

    def current_hour_ele_by_xpath(self):
        try:
            current_hour_ele_by_xpath = self.config.get("LOCATORS", "current_hour_ele")
            return current_hour_ele_by_xpath
        except Exception as ex:
            print("current_hour_ele_by_xpath : ", ex)

    def hour_down_by_xpath(self):
        try:
            hour_down_by_xpath = self.config.get("LOCATORS", "hour_down_by_xpath")
            return hour_down_by_xpath
        except Exception as ex:
            print("hour_down_by_xpath : ", ex)

    def clock_min_down_button_by_xpath(self):
        try:
            clock_min_down_button_by_xpath = self.config.get("LOCATORS", "clock_min_down_button_by_xpath")
            return clock_min_down_button_by_xpath
        except Exception as ex:
            print("clock_min_down_button_by_xpath : ", ex)

    def clock_min_up_button_by_xpath(self):
        try:
            clock_min_up_button_by_xpath = self.config.get("LOCATORS", "clock_min_up_button_by_xpath")
            return clock_min_up_button_by_xpath
        except Exception as ex:
            print("clock_min_up_button_by_xpath : ", ex)

    def enroll_get_start_date(self):
        try:
            enroll_get_start_date = self.common_test_data_config.get("common_data", "start_date")
            return enroll_get_start_date
        except Exception as ex:
            print("enroll_get_start_date : ", ex)

    def enroll_get_start_month(self):
        try:
            enroll_get_start_month = self.common_test_data_config.get("common_data", "start_month")
            return enroll_get_start_month
        except Exception as ex:
            print("enroll_get_start_month : ", ex)

    def enroll_get_start_year(self):
        try:
            enroll_get_start_year = self.common_test_data_config.get("common_data", "start_year")
            return enroll_get_start_year
        except Exception as ex:
            print("enroll_get_start_year : ", ex)

    def enroll_get_start_hour(self):
        try:
            enroll_get_start_hour = self.common_test_data_config.get("common_data", "start_hour")
            return enroll_get_start_hour
        except Exception as ex:
            print("enroll_get_start_hour : ", ex)

    def enroll_get_start_minuet(self):
        try:
            enroll_get_start_minuet = self.common_test_data_config.get("common_data", "start_minuet")
            return enroll_get_start_minuet
        except Exception as ex:
            print("enroll_get_start_minuet : ", ex)

    def enroll_get_start_am_pm_period(self):
        try:
            enroll_get_start_am_pm_period = self.common_test_data_config.get("common_data", "start_am_pm_period")
            return enroll_get_start_am_pm_period
        except Exception as ex:
            print("enroll_get_start_am_pm_period : ", ex)

    def enroll_get_end_date(self):
        try:
            enroll_get_end_date = self.common_test_data_config.get("common_data", "end_date")
            return enroll_get_end_date
        except Exception as ex:
            print("enroll_get_end_date : ", ex)

    def enroll_get_end_month(self):
        try:
            enroll_get_end_month = self.common_test_data_config.get("common_data", "end_month")
            return enroll_get_end_month
        except Exception as ex:
            print("enroll_get_end_month : ", ex)

    def enroll_get_end_year(self):
        try:
            enroll_get_end_year = self.common_test_data_config.get("common_data", "end_year")
            return enroll_get_end_year
        except Exception as ex:
            print("enroll_get_end_year : ", ex)

    def enroll_get_end_hour(self):
        try:
            enroll_get_end_hour = self.common_test_data_config.get("common_data", "end_hour")
            return enroll_get_end_hour
        except Exception as ex:
            print("enroll_get_end_hour : ", ex)

    def enroll_get_end_minuet(self):
        try:
            enroll_get_end_minuet = self.common_test_data_config.get("common_data", "end_minuet")
            return enroll_get_end_minuet
        except Exception as ex:
            print("enroll_get_end_minuet : ", ex)

    def enroll_get_end_am_pm_period(self):
        try:
            enroll_get_end_am_pm_period = self.common_test_data_config.get("common_data", "end_am_pm_period")
            return enroll_get_end_am_pm_period
        except Exception as ex:
            print("enroll_get_end_am_pm_period : ", ex)

    def expiration_get_start_date(self):
        try:
            expiration_get_start_date = self.common_test_data_config.get("common_data", "expiration_start_date")
            return expiration_get_start_date
        except Exception as ex:
            print("expiration_get_start_date : ", ex)

    def expiration_get_start_month(self):
        try:
            expiration_get_start_month = self.common_test_data_config.get("common_data", "expiration_start_month")
            return expiration_get_start_month
        except Exception as ex:
            print("expiration_get_start_month : ", ex)

    def expiration_get_start_year(self):
        try:
            expiration_get_start_year = self.common_test_data_config.get("common_data", "expiration_start_year")
            return expiration_get_start_year
        except Exception as ex:
            print("expiration_get_start_year : ", ex)

    def expiration_get_start_hour(self):
        try:
            expiration_get_start_hour = self.common_test_data_config.get("common_data", "expiration_start_hour")
            return expiration_get_start_hour
        except Exception as ex:
            print("expiration_get_start_hour : ", ex)

    def expiration_get_start_minuet(self):
        try:
            expiration_get_start_minuet = self.common_test_data_config.get("common_data", "expiration_start_minuet")
            return expiration_get_start_minuet
        except Exception as ex:
            print("expiration_get_start_minuet : ", ex)

    def expiration_get_start_am_pm_period(self):
        try:
            expiration_get_start_am_pm_period = self.common_test_data_config.get("common_data", "expiration_start_am_pm_period")
            return expiration_get_start_am_pm_period
        except Exception as ex:
            print("expiration_get_start_am_pm_period : ", ex)

    def expiration_get_end_date(self):
        try:
            expiration_get_end_date = self.common_test_data_config.get("common_data", "expiration_end_date")
            return expiration_get_end_date
        except Exception as ex:
            print("expiration_get_end_date : ", ex)

    def expiration_get_end_month(self):
        try:
            expiration_get_end_month = self.common_test_data_config.get("common_data", "expiration_end_month")
            return expiration_get_end_month
        except Exception as ex:
            print("expiration_get_end_month : ", ex)

    def expiration_get_end_year(self):
        try:
            expiration_get_end_year = self.common_test_data_config.get("common_data", "expiration_end_year")
            return expiration_get_end_year
        except Exception as ex:
            print("expiration_get_end_year : ", ex)

    def expiration_get_end_hour(self):
        try:
            expiration_get_end_hour = self.common_test_data_config.get("common_data", "expiration_end_hour")
            return expiration_get_end_hour
        except Exception as ex:
            print("expiration_get_end_hour : ", ex)

    def expiration_get_end_minuet(self):
        try:
            expiration_get_end_minuet = self.common_test_data_config.get("common_data", "expiration_end_minuet")
            return expiration_get_end_minuet
        except Exception as ex:
            print("expiration_get_end_minuet : ", ex)

    def expiration_get_end_am_pm_period(self):
        try:
            expiration_get_end_am_pm_period = self.common_test_data_config.get("common_data", "expiration_end_am_pm_period")
            return expiration_get_end_am_pm_period
        except Exception as ex:
            print("expiration_get_end_am_pm_period : ", ex)

    def location_store_data_input(self):
        try:
            location_store_data_input = self.common_test_data_config.get("Enrollments_Data", "location_store_data_input")
            return location_store_data_input
        except Exception as ex:
            print("location_store_data_input : ", ex)

    def case_subject_data_input(self):
        try:
            case_subject_data_input = self.common_test_data_config.get("Enrollments_Data", "case_subject_data_input")
            return case_subject_data_input
        except Exception as ex:
            print("case_subject_data_input : ", ex)

    def no_match_search_filter_message(self):
        try:
            no_match_search_filter_message = self.config.get("LOCATORS", "no_match_search_filter_message")
            return no_match_search_filter_message
        except Exception as ex:
            print("no_match_search_filter_message : ", ex)

    def match_list_enrolled_output(self):
        try:
            match_list_enrolled_output = self.config.get("LOCATORS", "match_list_enrolled_output")
            return match_list_enrolled_output
        except Exception as ex:
            print("match_list_enrolled_output : ", ex)

    def match_list_location_store_case_subject_output(self):
        try:
            match_list_location_store_case_subject_output = self.config\
                .get("LOCATORS", "match_list_location_store_case_subject_output")
            return match_list_location_store_case_subject_output
        except Exception as ex:
            print("match_list_location_store_case_subject_output : ", ex)

    def match_list_action_output(self):
        try:
            match_list_action_output = self.config.get("LOCATORS", "match_list_action_output")
            return match_list_action_output
        except Exception as ex:
            print("match_list_action_output : ", ex)

    def match_list_image_by_xpath(self):
        try:
            match_list_image_by_xpath = self.config.get("LOCATORS", "match_list_image_by_xpath")
            return match_list_image_by_xpath
        except Exception as ex:
            print("match_list_image_by_xpath : ", ex)

    def sort_by_data_input_LOCATION_STORE(self):
        try:
            sort_by_data_input = self.common_test_data_config.get("Enrollments_Data", "sort_by_data_input_LOCATION_STORE")
            return sort_by_data_input
        except Exception as ex:
            print("sort_by_data_input_LOCATION_STORE : ", ex)

    def sort_by_data_input_Enrolled_On(self):
        try:
            sort_by_data_input = self.common_test_data_config.get("Enrollments_Data", "sort_by_data_input_Enrolled_On")
            return sort_by_data_input
        except Exception as ex:
             print("sort_by_data_input_Enrolled_On : ", ex)

    def sort_by_data_input_CASE_SUBJECT(self):
        try:
            sort_by_data_input = self.common_test_data_config.get("Enrollments_Data", "sort_by_data_input_CASE_SUBJECT")
            return sort_by_data_input
        except Exception as ex:
            print("sort_by_data_input_CASE_SUBJECT : ", ex)

    def sort_key_by_xpath(self):
        try:
            sort_key_by_xpath = self.config.get("LOCATORS", "sort_key_by_xpath")
            return sort_key_by_xpath
        except Exception as ex:
            print("sort_key_by_xpath : ", ex)

    def close_panel_one_by_one_list(self):
        try:
            close_panel_one_by_one_list = self.config.get("LOCATORS", "close_panel_one_by_one_list")
            return close_panel_one_by_one_list
        except Exception as ex:
            print("close_panel_one_by_one_list : ", ex)

    def Error_message_on_enrollments(self):
        try:
            error = self.config.get("LOCATORS", "Error_message")
            return error
        except Exception as ex:
            print("error message visible",ex)

    def message_to_user_if_search_is_failed(self):
        try:
            search = self.config.get("LOCATORS", "message_to_user_there_are_no_enrollments")
            return search
        except Exception as ex:
            print("message to user", ex)

# print(Read_Enrollments_Components().enrollments_link_by_xpath())