import configparser
from pathlib import Path


class Read_Visitor_Search_Components:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.common_test_data_config = configparser.RawConfigParser()
        try:
            portal_menu_ini_file_path = f'{Path(__file__).parent.parent.parent}\\All_Test_Data\\7_Visitor_Search_Module\\Data_From_INI\\Visitor_Search.ini'
            # Base_Class.logger.info("File location: ", deployment_manager_ini_file_path)
            self.config.read(portal_menu_ini_file_path)
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def configure_search_by_xpath(self):
        try:
            configure_search_by_xpath = self.config.get("LOCATORS", "configure_search_by_xpath")
            return configure_search_by_xpath
        except Exception as ex:
            print("configure_search_by_xpath : ", ex)

    def re_select_photo_by_xpath(self):
        try:
            re_select_photo_by_xpath = self.config.get("LOCATORS", "re_select_photo_by_xpath")
            return re_select_photo_by_xpath
        except Exception as ex:
            print("re_select_photo_by_xpath : ", ex)

    def crop_photo_by_xpath(self):
        try:
            crop_photo_by_xpath = self.config.get("LOCATORS", "crop_photo_by_xpath")
            return crop_photo_by_xpath
        except Exception as ex:
            print("crop_photo_by_xpath : ", ex)

    def rotate_image_by_xpath(self):
        try:
            rotate_image_by_xpath = self.config.get("LOCATORS", "rotate_image_by_xpath")
            return rotate_image_by_xpath
        except Exception as ex:
            print("rotate_image_by_xpath : ", ex)

    def select_a_photo_validation_by_xpath(self):
        try:
            select_a_photo_validation_by_xpath = self.config.get("LOCATORS", "select_a_photo_validation_by_xpath")
            return select_a_photo_validation_by_xpath
        except Exception as ex:
            print("select_a_photo_validation_by_xpath : ", ex)

    def select_photo_instructions_by_xpath(self):
        try:
            select_photo_instructions_by_xpath = self.config.get("LOCATORS", "select_photo_instructions_by_xpath")
            return select_photo_instructions_by_xpath
        except Exception as ex:
            print("select_photo_instructions_by_xpath : ", ex)

    def photo_upload_container_by_xpath(self):
        try:
            photo_upload_container_by_xpath = self.config.get("LOCATORS", "photo_upload_container_by_xpath")
            return photo_upload_container_by_xpath
        except Exception as ex:
            print("photo_upload_container_by_xpath : ", ex)

    def search_button_panel_photo_validation_by_xpath(self):
        try:
            search_button_panel_photo_validation_by_xpath = self.config.\
                get("LOCATORS", "search_button_panel_photo_validation_by_xpath")
            return search_button_panel_photo_validation_by_xpath
        except Exception as ex:
            print("search_button_panel_photo_validation_by_xpath : ", ex)

    def optional_constraints_to_narrow_search_text_validation_by_xpath(self):
        try:
            optional_constraints_to_narrow_search_text_validation_by_xpath = self.config.\
                get("LOCATORS", "optional_constraints_to_narrow_search_text_validation_by_xpath")
            return optional_constraints_to_narrow_search_text_validation_by_xpath
        except Exception as ex:
            print("optional_constraints_to_narrow_search_text_validation_by_xpath : ", ex)

    def start_date_by_xpath(self):
        try:
            start_date_by_xpath = self.config.get("LOCATORS", "start_date_by_xpath")
            return start_date_by_xpath
        except Exception as ex:
            print("start_date_by_xpath : ", ex)

    def start_date_checkbox_by_xpath(self):
        try:
            start_date_checkbox_by_xpath = self.config.get("LOCATORS", "start_date_checkbox_by_xpath")
            return start_date_checkbox_by_xpath
        except Exception as ex:
            print("start_date_checkbox_by_xpath : ", ex)

    def end_date_by_xpath(self):
        try:
            end_date_by_xpath = self.config.get("LOCATORS", "end_date_by_xpath")
            return end_date_by_xpath
        except Exception as ex:
            print("end_date_by_xpath : ", ex)

    def end_date_checkbox_by_xpath(self):
        try:
            end_date_checkbox_by_xpath = self.config.get("LOCATORS", "end_date_checkbox_by_xpath")
            return end_date_checkbox_by_xpath
        except Exception as ex:
            print("end_date_checkbox_by_xpath : ", ex)

    def age_range_text_validation_by_xpath(self):
        try:
            age_range_text_validation_by_xpath = self.config.get("LOCATORS", "age_range_text_validation_by_xpath")
            return age_range_text_validation_by_xpath
        except Exception as ex:
            print("age_range_text_validation_by_xpath : ", ex)

    def start_age_by_xpath(self):
        try:
            start_age_by_xpath = self.config.get("LOCATORS", "start_age_by_xpath")
            return start_age_by_xpath
        except Exception as ex:
            print("start_age_by_xpath : ", ex)

    def end_age_by_xpath(self):
        try:
            end_age_by_xpath = self.config.get("LOCATORS", "end_age_by_xpath")
            return end_age_by_xpath
        except Exception as ex:
            print("end_age_by_xpath : ", ex)

    def select_gender_by_xpath(self):
        try:
            select_gender_by_xpath = self.config.get("LOCATORS", "select_gender_by_xpath")
            return select_gender_by_xpath
        except Exception as ex:
            print("select_gender_by_xpath : ", ex)

    def zone_by_xpath(self):
        try:
            zone_by_xpath = self.config.get("LOCATORS", "zone_by_xpath")
            return zone_by_xpath
        except Exception as ex:
            print("zone_by_xpath : ", ex)

    def zone_name_by_xpath(self):
        try:
            zone_name_by_xpath = self.config.get("LOCATORS", "zone_name_by_xpath")
            return zone_name_by_xpath
        except Exception as ex:
            print("zone_name_by_xpath : ", ex)

    def threshold_slider_by_xpath(self):
        try:
            threshold_slider_by_xpath = self.config.get("LOCATORS", "threshold_slider_by_xpath")
            return threshold_slider_by_xpath
        except Exception as ex:
            print("threshold_slider_by_xpath : ", ex)

    def max_of_matches_by_xpath(self):
        try:
            max_of_matches_by_xpath = self.config.get("LOCATORS", "max_of_matches_by_xpath")
            return max_of_matches_by_xpath
        except Exception as ex:
            print("max_of_matches_by_xpath : ", ex)

    def sort_A_to_Z_by_xpath(self):
        try:
            sort_A_to_Z_by_xpath = self.config.get("LOCATORS", "sort_A_to_Z_by_xpath")
            return sort_A_to_Z_by_xpath
        except Exception as ex:
            print("sort_A_to_Z_by_xpath : ", ex)

    def sort_Z_to_A_by_xpath(self):
        try:
            sort_Z_to_A_by_xpath = self.config.get("LOCATORS", "sort_Z_to_A_by_xpath")
            return sort_Z_to_A_by_xpath
        except Exception as ex:
            print("sort_Z_to_A_by_xpath : ", ex)

    def clear_by_xpath(self):
        try:
            clear_by_xpath = self.config.get("LOCATORS", "clear_by_xpath")
            return clear_by_xpath
        except Exception as ex:
            print("clear_by_xpath : ", ex)

    def submit_search_button_by_xpath(self):
        try:
            submit_search_button_by_xpath = self.config.get("LOCATORS", "submit_search_button_by_xpath")
            return submit_search_button_by_xpath
        except Exception as ex:
            print("submit_search_button_by_xpath : ", ex)

    def search_result_validation_by_xpath(self):
        try:
            search_result_validation_by_xpath = self.config.get("LOCATORS", "search_result_validation_by_xpath")
            return search_result_validation_by_xpath
        except Exception as ex:
            print("search_result_validation_by_xpath : ", ex)

    def close_visitor_search_panel_by_xpath(self):
        try:
            close_visitor_search_panel_by_xpath = self.config.get("LOCATORS", "close_visitor_search_panel_by_xpath")
            return close_visitor_search_panel_by_xpath
        except Exception as ex:
            print("close_visitor_search_panel_by_xpath : ", ex)

    def submit_search_button_panel_by_xpath(self):
        try:
            submit_search_button_panel_by_xpath = self.config.get("LOCATORS", "submit_search_button_panel_by_xpath")
            return submit_search_button_panel_by_xpath
        except Exception as ex:
            print("submit_search_button_panel_by_xpath : ", ex)

    def visitor_search_result_panel_by_xpath(self):
        try:
            visitor_search_result_panel_by_xpath = self.config.get("LOCATORS", "visitor_search_result_panel_by_xpath")
            return visitor_search_result_panel_by_xpath
        except Exception as ex:
            print("visitor_search_result_panel_by_xpath : ", ex)

    def visitor_search_result_by_xpath(self):
        try:
            visitor_search_result_by_xpath = self.config.get("LOCATORS", "visitor_search_result_by_xpath")
            return visitor_search_result_by_xpath
        except Exception as ex:
            print("visitor_search_result_by_xpath : ", ex)

    def view_dropdown_by_xpath(self):
        try:
            view_dropdown_by_xpath = self.config.get("LOCATORS", "view_dropdown_by_xpath")
            return view_dropdown_by_xpath
        except Exception as ex:
            print("view_dropdown_by_xpath : ", ex)

    def view_drop_down_list_by_xpath(self):
        try:
            view_drop_down_list_by_xpath = self.config.get("LOCATORS", "view_drop_down_list_by_xpath")
            return view_drop_down_list_by_xpath
        except Exception as ex:
            print("view_drop_down_list_by_xpath : ", ex)

    def action_drop_down_by_xpath(self):
        try:
            action_drop_down_by_xpath = self.config.get("LOCATORS", "action_drop_down_by_xpath")
            return action_drop_down_by_xpath
        except Exception as ex:
            print("action_drop_down_by_xpath : ", ex)

    def action_drop_down_list_by_xpath(self):
        try:
            action_drop_down_list_by_xpath = self.config.get("LOCATORS", "action_drop_down_list_by_xpath")
            return action_drop_down_list_by_xpath
        except Exception as ex:
            print("action_drop_down_list_by_xpath : ", ex)

    def visitor_search_result_photo_by_xpath(self):
        try:
            visitor_search_result_photo_by_xpath = self.config.get("LOCATORS", "visitor_search_result_photo_by_xpath")
            return visitor_search_result_photo_by_xpath
        except Exception as ex:
            print("visitor_search_result_photo_by_xpath : ", ex)

    def visitor_search_complete_title_by_xpath(self):
        try:
            visitor_search_complete_title_by_xpath = self.config.get("LOCATORS",
                                                                     "visitor_search_complete_title_by_xpath")
            return visitor_search_complete_title_by_xpath
        except Exception as ex:
            print("visitor_search_complete_title_by_xpath : ", ex)

    def visitor_jobs_processed_heading_by_xpath(self):
        try:
            visitor_jobs_processed_heading_by_xpath = self.config.get("LOCATORS",
                                                                      "visitor_jobs_processed_heading_by_xpath")
            return visitor_jobs_processed_heading_by_xpath
        except Exception as ex:
            print("visitor_jobs_processed_heading_by_xpath : ", ex)

    def search_constraints_by_xpath(self):
        try:
            search_constraints_by_xpath = self.config.get("LOCATORS", "search_constraints_by_xpath")
            return search_constraints_by_xpath
        except Exception as ex:
            print("search_constraints_by_xpath : ", ex)

    def matches_found_by_xpath(self):
        try:
            matches_found_by_xpath = self.config.get("LOCATORS", "matches_found_by_xpath")
            return matches_found_by_xpath
        except Exception as ex:
            print("matches_found_by_xpath : ", ex)

    def matches_list_by_xpath(self):
        try:
            matches_list_by_xpath = self.config.get("LOCATORS", "matches_list_by_xpath")
            return matches_list_by_xpath
        except Exception as ex:
            print("matches_list_by_xpath : ", ex)

    def matches_count_data_input(self):
        try:
            matches_count_data_input = self.common_test_data_config.get("common_data", "matches_count_data_input")
            return matches_count_data_input
        except Exception as ex:
            print("matches_count_data_input : ", ex)

    def refresh_icon_by_xpath(self):
        try:
            refresh_icon_by_xpath = self.config.get("LOCATORS", "refresh_icon_by_xpath")
            return refresh_icon_by_xpath
        except Exception as ex:
            print("refresh_icon_by_xpath : ", ex)

    def slider_value_data_input(self):
        try:
            slider_value_data_input = self.common_test_data_config.get("common_data", "slider_value_data_input")
            return slider_value_data_input
        except Exception as ex:
            print("slider_value_data_input : ", ex)

    def score_by_xpath(self):
        try:
            score_by_xpath = self.config.get("LOCATORS", "score_by_xpath")
            return score_by_xpath
        except Exception as ex:
            print("score_by_xpath : ", ex)

    def matches_gender_by_xpath(self):
        try:
            matches_gender_by_xpath = self.config.get("LOCATORS", "matches_gender_by_xpath")
            return matches_gender_by_xpath
        except Exception as ex:
            print("matches_gender_by_xpath : ", ex)

    def gender_data_input(self):
        try:
            gender_data_input = self.common_test_data_config.get("common_data", "gender_data_input")
            return gender_data_input
        except Exception as ex:
            print("gender_data_input : ", ex)

    def slider_icon_by_xpath(self):
        try:
            slider_icon_by_xpath = self.config.get("LOCATORS", "slider_icon_by_xpath")
            return slider_icon_by_xpath
        except Exception as ex:
            print("slider_icon_by_xpath : ", ex)

    def start_age_data_input(self):
        try:
            start_age_data_input = self.common_test_data_config.get("common_data", "start_age_data_input")
            return start_age_data_input
        except Exception as ex:
            print("start_age_data_input : ", ex)

    def end_age_data_input(self):
        try:
            end_age_data_input = self.common_test_data_config.get("common_data", "end_age_data_input")
            return end_age_data_input
        except Exception as ex:
            print("end_age_data_input : ", ex)

    def zone_data_input(self):
        try:
            zone_data_input = self.common_test_data_config.get("common_data", "zone_data_input")
            return zone_data_input
        except Exception as ex:
            print("zone_data_input : ", ex)

    def zone_data_input1(self):
        try:
            zone_data_input1 = self.common_test_data_config.get("common_data", "zone_data_input1")
            return zone_data_input1
        except Exception as ex:
            print("zone_data_input : ", ex)

    def zone_data_input2(self):
        try:
            zone_data_input2 = self.common_test_data_config.get("common_data", "zone_data_input2")
            return zone_data_input2
        except Exception as ex:
            print("zone_data_input : ", ex)

    def close_all_visitor_search_panel_by_xpath(self):
        try:
            close_all_visitor_search_panel_by_xpath = self.config.get("LOCATORS",
                                                                      "close_all_visitor_search_panel_by_xpath")
            return close_all_visitor_search_panel_by_xpath
        except Exception as ex:
            print("close_all_visitor_search_panel_by_xpath : ", ex)

    def calender_month_year_by_xpath(self):
        try:
            calender_month_year_by_xpath = self.config.get("LOCATORS", "calender_month_year_by_xpath")
            return calender_month_year_by_xpath
        except Exception as ex:
            print("calender_month_year_by_xpath : ", ex)

    def calender_back_button_by_xpath(self):
        try:
            calender_back_button_by_xpath = self.config.get("LOCATORS", "calender_back_button_by_xpath")
            return calender_back_button_by_xpath
        except Exception as ex:
            print("calender_back_button_by_xpath : ", ex)

    def calender_forward_button_by_xpath(self):
        try:
            calender_forward_button_by_xpath = self.config.get("LOCATORS", "calender_forward_button_by_xpath")
            return calender_forward_button_by_xpath
        except Exception as ex:
            print("calender_forward_button_by_xpath : ", ex)

    def calender_timer_icon_by_xpath(self):
        try:
            calender_timer_icon_by_xpath = self.config.get("LOCATORS", "calender_timer_icon_by_xpath")
            return calender_timer_icon_by_xpath
        except Exception as ex:
            print("calender_timer_icon_by_xpath : ", ex)

    def calender_tick_icon_by_xpath(self):
        try:
            calender_tick_icon_by_xpath = self.config.get("LOCATORS", "calender_tick_icon_by_xpath")
            return calender_tick_icon_by_xpath
        except Exception as ex:
            print("calender_tick_icon_by_xpath : ", ex)

    def calender_select_date_by_xpath(self):
        try:
            calender_select_date_by_xpath = self.config.get("LOCATORS", "calender_select_date_by_xpath")
            return calender_select_date_by_xpath
        except Exception as ex:
            print("calender_select_date_by_xpath : ", ex)

    def calender_clock_hour_up_button_by_xpath(self):
        try:
            calender_clock_hour_up_button_by_xpath = self.config.get("LOCATORS",
                                                                     "calender_clock_hour_up_button_by_xpath")
            return calender_clock_hour_up_button_by_xpath
        except Exception as ex:
            print("calender_clock_hour_up_button_by_xpath : ", ex)

    def calender_clock_current_hour_by_xpath(self):
        try:
            calender_clock_current_hour_by_xpath = self.config.get("LOCATORS", "calender_clock_current_hour_by_xpath")
            return calender_clock_current_hour_by_xpath
        except Exception as ex:
            print("calender_clock_current_hour_by_xpath : ", ex)

    def current_hours_element_by_xpath(self):
        try:
            current_hours_element_by_xpath = self.config.get("LOCATORS", "current_hours_element_by_xpath")
            return current_hours_element_by_xpath
        except Exception as ex:
            print("current_hours_element_by_xpath : ", ex)

    def current_minute_element_by_xpath(self):
        try:
            current_minute_element_by_xpath = self.config.get("LOCATORS", "current_minute_element_by_xpath")
            return current_minute_element_by_xpath
        except Exception as ex:
            print("current_minute_element_by_xpath : ", ex)

    def clock_min_up_button_by_xpath(self):
        try:
            clock_min_up_button_by_xpath = self.config.get("LOCATORS", "clock_min_up_button")
            return clock_min_up_button_by_xpath
        except Exception as ex:
            print("clock_min_up_button_by_xpath : ", ex)

    def am_pm_toggle_period_element_by_xpath(self):
        try:
            am_pm_toggle_period_element_by_xpath = self.config.get("LOCATORS", "am_pm_toggle_period_element_by_xpath")
            return am_pm_toggle_period_element_by_xpath
        except Exception as ex:
            print("am_pm_toggle_period_element_by_xpath : ", ex)

    def get_start_date(self):
        try:
            get_start_date = self.common_test_data_config.get("common_data", "start_date")
            return get_start_date
        except Exception as ex:
            print("get_start_date : ", ex)

    def get_start_month(self):
        try:
            get_start_month = self.common_test_data_config.get("common_data", "start_month")
            return get_start_month
        except Exception as ex:
            print("get_start_month : ", ex)

    def get_start_year(self):
        try:
            get_start_year = self.common_test_data_config.get("common_data", "start_year")
            return get_start_year
        except Exception as ex:
            print("get_start_year : ", ex)

    def get_start_hour(self):
        try:
            get_start_hour = self.common_test_data_config.get("common_data", "start_hour")
            return get_start_hour
        except Exception as ex:
            print("get_start_hour : ", ex)

    def get_start_minuet(self):
        try:
            get_start_minuet = self.common_test_data_config.get("common_data", "start_minuet")
            return get_start_minuet
        except Exception as ex:
            print("get_start_minuet : ", ex)

    def get_start_am_pm_period(self):
        try:
            get_start_am_pm_period = self.common_test_data_config.get("common_data", "start_am_pm_period")
            return get_start_am_pm_period
        except Exception as ex:
            print("get_start_am_pm_period : ", ex)

    def get_end_date(self):
        try:
            get_end_date = self.common_test_data_config.get("common_data", "end_date")
            return get_end_date
        except Exception as ex:
            print("get_end_date : ", ex)

    def get_end_month(self):
        try:
            get_end_month = self.common_test_data_config.get("common_data", "end_month")
            return get_end_month
        except Exception as ex:
            print("get_end_month : ", ex)

    def get_end_year(self):
        try:
            get_end_year = self.common_test_data_config.get("common_data", "end_year")
            return get_end_year
        except Exception as ex:
            print("get_end_year : ", ex)

    def get_end_hour(self):
        try:
            get_end_hour = self.common_test_data_config.get("common_data", "end_hour")
            return get_end_hour
        except Exception as ex:
            print("get_end_hour : ", ex)

    def get_end_minuet(self):
        try:
            get_end_minuet = self.common_test_data_config.get("common_data", "end_minuet")
            return get_end_minuet
        except Exception as ex:
            print("get_end_minuet : ", ex)

    def get_end_am_pm_period(self):
        try:
            get_end_am_pm_period = self.common_test_data_config.get("common_data", "end_am_pm_period")
            return get_end_am_pm_period
        except Exception as ex:
            print("get_end_am_pm_period : ", ex)

    def close_all_panel_one_by_one(self):
        try:
            close_all_panel_one_by_one = self.config.get("LOCATORS", "close_panel_one_by_one_list")
            return close_all_panel_one_by_one
        except Exception as ex:
            print("close_all_panel_one_by_one : ", ex)

    def logout_btn_by_xpath(self):
        try:
            logout_btn_by_xpath = self.config.get("LOCATORS", "logout_btn_by_xpath")
            return logout_btn_by_xpath
        except Exception as ex:
            print("copyright_btn_by_xpath : ", ex)

    def image_match_list_by_xpath(self):
        try:
            image_match_list_by_xpath = self.config.get("LOCATORS", "image_match_list_by_xpath")
            return image_match_list_by_xpath
        except Exception as ex:
            print("image_match_list_by_xpath : ", ex)

    def image_match_by_xpath(self):
        try:
            image_match_list_by_xpath = self.config.get("LOCATORS", "image_match_by_xpath")
            return image_match_list_by_xpath
        except Exception as ex:
            print("image_match_list_by_xpath : ", ex)

    def start_date_inbox_by_xpath(self):
        try:
            start_date_inbox_by_xpath = self.config.get("LOCATORS", "start_date_inbox")
            return start_date_inbox_by_xpath
        except Exception as ex:
            print("start_date_inbox_by_xpath : ", ex)

    def match_region_by_xpath(self):
        try:
            match_region_by_xpath = self.config.get("LOCATORS", "match_region_by_xpath")
            return match_region_by_xpath
        except Exception as ex:
            print("match_region_by_xpath : ", ex)

    def actual_start_date_by_xpath(self):
        try:
            actual_start_date_by_xpath = self.config.get("LOCATORS", "actual_start_date")
            return actual_start_date_by_xpath
        except Exception as ex:
            print("actual_start_date_by_xpath : ", ex)

    def period_by_xpath(self):
        try:
            period_by_xpath = self.config.get("LOCATORS", "period_by_xpath")
            return period_by_xpath
        except Exception as ex:
            print("period_by_xpath : ", ex)

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

    def hour_down_ele_by_xpath(self):
        try:
            hour_down_ele_by_xpath = self.config.get("LOCATORS", "hour_down_ele")
            return hour_down_ele_by_xpath
        except Exception as ex:
            print("hour_down_ele_by_xpath : ", ex)

    def match_date_list_by_xpath(self):
        try:
            match_date_list_by_xpath = self.config.get("LOCATORS", "match_date_list_by_xpath")
            return match_date_list_by_xpath
        except Exception as ex:
            print("match_date_list_by_xpath : ", ex)

    def clock_min_down_button_by_xpath(self):
        try:
            clock_min_down_button_by_xpath = self.config.get("LOCATORS", "clock_min_down_button")
            return clock_min_down_button_by_xpath
        except Exception as ex:
            print("clock_min_down_button_by_xpath : ", ex)

    def no_match_found_by_xpath(self):
        try:
            no_match_found_by_xpath = self.config.get("LOCATORS", "no_match_found_by_xpath")
            return no_match_found_by_xpath
        except Exception as ex:
            print("no_match_found_by_xpath : ", ex)

    def root_selection_xpath(self):
        try:
            root_selection_xpath = self.config.get("LOCATORS", "root_selection_xpath")
            return root_selection_xpath
        except Exception as ex:
            print("root_selection_xpath : ", ex)

    def zone_save_button_xpath(self):
        try:
            zone_save_button_xpath = self.config.get("LOCATORS", "zone_save_button_xpath")
            return zone_save_button_xpath
        except Exception as ex:
            print("zone_save_button_xpath : ", ex)

    def start_end_date_validation_msg_verify_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "start_end_date_validation_msg_verify_xpath")
            return ele
        except Exception as ex:
            print("start_end_date_validation_msg_verify_xpath : ", ex)

    def submitting_archive_search_wait_icon(self):
        try:
            ele = self.config.get("LOCATORS", "submitting_archive_search_wait_icon")
            return ele
        except Exception as ex:
            print("submitting_archive_search_wait_icon : ", ex)

    def meta_data_without_date_validation_msg(self):
        try:
            ele = self.common_test_data_config.get("Visitor_Search_Data", "meta_data_without_date_validation_msg")
            return ele
        except Exception as ex:
            print("meta_data_without_date_validation_msg : ", ex)

    def no_search_criteria_msg(self):
        try:
            ele = self.common_test_data_config.get("Visitor_Search_Data", "no_search_criteria_msg")
            return ele
        except Exception as ex:
            print("no_search_criteria_msg : ", ex)
    def meta_data_without_date_validation_msg_tc_vs_002(self):
        try:
            ele1 = self.common_test_data_config.get("Visitor_Search_Data", "meta_data_without_date_validation_msg_tc_vs_002")
            return ele1
        except Exception as ex:
            print("meta_data_without_date_validation_msg_tc_vs_002 : ", ex)

    def meta_data_without_date_validation_msg_tc_vs_003(self):
        try:
            ele1 = self.common_test_data_config.get("Visitor_Search_Data", "meta_data_without_date_validation_msg_tc_vs_003")
            return ele1
        except Exception as ex:
            print("meta_data_without_date_validation_msg_tc_vs_003 : ", ex)

    def zone_text_list_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "zone_text_list_xpath")
            return ele
        except Exception as ex:
            print("zone_text_list_xpath : ", ex)

    def limited_to_30_min_interval_validation(self):
        try:
            ele = self.config.get("LOCATORS", "limited_to_30_min_interval_validation")
            return ele
        except Exception as ex:
            print("limited_to_30_min_interval_validation : ", ex)

    def limited_to_30_meta_data_search_validation(self):
        try:
            ele = self.common_test_data_config.get("Visitor_Search_Data", "limited_to_30_meta_data_search_validation")
            return ele
        except Exception as ex:
            print("limited_to_30_meta_data_search_validation : ", ex)

    def meta_data_start_date(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_start_date")
            return ele
        except Exception as ex:
            print("meta_data_start_date : ", ex)

    def meta_data_start_month(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_start_month")
            return ele
        except Exception as ex:
            print("meta_data_start_month : ", ex)

    def meta_data_start_year(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_start_year")
            return ele
        except Exception as ex:
            print("meta_data_start_year : ", ex)

    def meta_data_start_hour(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_start_hour")
            return ele
        except Exception as ex:
            print("meta_data_start_hour : ", ex)

    def meta_data_start_minuet(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_start_minuet")
            return ele
        except Exception as ex:
            print("meta_data_start_minuet : ", ex)

    def meta_data_start_am_pm_period(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_start_am_pm_period")
            return ele
        except Exception as ex:
            print("meta_data_start_am_pm_period : ", ex)

    def meta_data_end_date(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_end_date")
            return ele
        except Exception as ex:
            print("meta_data_end_date : ", ex)

    def meta_data_end_month(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_end_month")
            return ele
        except Exception as ex:
            print("meta_data_end_month : ", ex)

    def meta_data_end_year(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_end_year")
            return ele
        except Exception as ex:
            print("meta_data_end_year : ", ex)

    def meta_data_end_hour(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_end_hour")
            return ele
        except Exception as ex:
            print("meta_data_end_hour : ", ex)

    def meta_data_end_minuet(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_end_minuet")
            return ele
        except Exception as ex:
            print("meta_data_end_minuet : ", ex)

    def meta_data_end_am_pm_period(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_end_am_pm_period")
            return ele
        except Exception as ex:
            print("meta_data_end_am_pm_period : ", ex)

    def nats_checkbox_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "nats_checkbox_xpath")
            return ele
        except Exception as ex:
            print("nats_checkbox_xpath : ", ex)

    def no_matches_found(self):
        try:
            ele = self.config.get("LOCATORS", "no_matches_found")
            return ele
        except Exception as ex:
            print("nats_checkbox_xpath : ", ex)

    def connection_error(self):
        try:
            ele = self.common_test_data_config.get("common_data", "connection_error")
            return ele
        except Exception as ex:
            print("connection_error : ", ex)

    def start_date_mmddyyyy(self):
        start_date_mmddyyyy = self.common_test_data_config.get("common_data", "start_date_mmddyyyy")
        return start_date_mmddyyyy

    def start_time_hhmm(self):
        start_time_hhmm = self.common_test_data_config.get("common_data", "start_time_hhmm")
        return start_time_hhmm

    def start_am_pm(self):
        start_am_pm = self.common_test_data_config.get("common_data", "start_am_pm")
        return start_am_pm

    def get_loginButton(self):
        try:
            login_btn = self.config.get('LOCATORS', 'portal_login_page_loginBtn_by_xpath')
            # Base_Class.logger.info("URL read successfully : ", url)
            return login_btn
        except Exception as ex:
            print(ex)

    def portal_menu_visitors_search_btn_by_xpath(self):
        try:
            visitors_search_btn_by_xpath = self.config.get("LOCATORS", "visitors_search_btn_by_xpath")
            return visitors_search_btn_by_xpath
        except Exception as ex:
            print("portal_menu_visitors_search_btn_by_xpath : ", ex)

    def auto_refresh_on_by_xpath(self):
        try:
            auto_refresh_on_by_xpath = self.config.get("LOCATORS", "auto_refresh_on_by_xpath")
            return auto_refresh_on_by_xpath
        except Exception as ex:
            print("auto_refresh_on_by_xpath : ", ex)

    def auto_refresh_off_by_xpath(self):
        try:
            auto_refresh_off_by_xpath = self.config.get("LOCATORS", "auto_refresh_off_by_xpath")
            return auto_refresh_off_by_xpath
        except Exception as ex:
            print("auto_refresh_off_by_xpath : ", ex)

    def vs_start_date_check_bx(self):
        try:
            vs_start_date_check_bx = self.config.get("LOCATORS", "vs_start_date_check_bx")
            return vs_start_date_check_bx
        except Exception as ex:
            print("vs_start_date_check_bx : ", ex)

    def vs_end_date_check_bx(self):
        try:
            vs_end_date_check_bx = self.config.get("LOCATORS", "vs_end_date_check_bx")
            return vs_end_date_check_bx
        except Exception as ex:
            print("vs_end_date_check_bx : ", ex)

    def get_start_date_calender_box_by_xpath(self):
        try:
            get_start_date_calender_box_by_xpath = self.config.get("LOCATORS", "start_date_calender_box_by_xpath")
            return get_start_date_calender_box_by_xpath
        except Exception as ex:
            print("get_start_date_calender_box_by_xpath : ", ex)

    def get_end_date_calender_box_by_xpath(self):
        try:
            get_end_date_calender_box_by_xpath = self.config.get("LOCATORS", "end_date_calender_box_by_xpath")
            return get_end_date_calender_box_by_xpath
        except Exception as ex:
            print("get_end_date_calender_box_by_xpath : ", ex)

