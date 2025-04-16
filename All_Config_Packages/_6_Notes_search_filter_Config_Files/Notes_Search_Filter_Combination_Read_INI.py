import configparser
from pathlib import Path


class Read_notes_search_filter_combination:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            portal_menu_ini_file_path = f'{Path(__file__).parent.parent.parent}\\All_Test_Data\\6_Notes_search_filter_Module\\Data_From_INI\\Notes_Search_Filter_Combination.ini'

            self.config.read(portal_menu_ini_file_path)
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def notes_menu_button_by_xpath(self):
        try:
            notes_menu_button_by_xpath = self.config.get("LOCATORS", "notes_menu_button")
            return notes_menu_button_by_xpath
        except Exception as ex:
            print("notes_menu_button_by_xpath : ", ex)

    def close_panel_one_by_one_list(self):
        try:
            ele = self.config.get("LOCATORS", "close_panel_one_by_one_list")
            return ele
        except Exception as ex:
            print("close_panel_one_by_one_list : ", ex)

    def logout_btn_by_xpath(self):
        try:
            logout_btn_by_xpath = self.config.get("LOCATORS", "logout_btn_by_xpath")
            return logout_btn_by_xpath
        except Exception as ex:
            print("copyright_btn_by_xpath : ", ex)

    def notes_search_button_by_xpath(self):
        try:
            notes_search_button_by_xpath = self.config.get("LOCATORS", "notes_search_button")
            return notes_search_button_by_xpath
        except Exception as ex:
            print("notes_search_button_by_xpath : ", ex)

    def search_dropdown_description_option_by_xpath(self):
        try:
            search_dropdown_description_option_by_xpath = self.config.get("LOCATORS",
                                                                          "search_dropdown_description_option")
            return search_dropdown_description_option_by_xpath
        except Exception as ex:
            print("search_dropdown_description_option_by_xpath : ", ex)

    def location_or_store_input_field_by_xpath(self):
        try:
            location_or_store_input_field_by_xpath = self.config.get("LOCATORS", "location_or_store_input_field")
            return location_or_store_input_field_by_xpath
        except Exception as ex:
            print("location_or_store_input_field_by_xpath : ", ex)

    def case_or_subject_input_field_by_xpath(self):
        try:
            case_or_subject_input_field_by_xpath = self.config.get("LOCATORS", "case_or_subject_input_field")
            return case_or_subject_input_field_by_xpath
        except Exception as ex:
            print("case_or_subject_input_field_by_xpath : ", ex)

    def sort_by_dropdown_by_xpath(self):
        try:
            sort_by_dropdown_by_xpath = self.config.get("LOCATORS", "sort_by_dropdown")
            return sort_by_dropdown_by_xpath
        except Exception as ex:
            print("sort_by_dropdown_by_xpath : ", ex)

    def option_location_or_store_by_xpath(self):
        try:
            option_location_or_store_by_xpath = self.config.get("LOCATORS", "option_location_or_store")
            return option_location_or_store_by_xpath
        except Exception as ex:
            print("option_location_or_store_by_xpath : ", ex)

    def option_case_or_subject_by_xpath(self):
        try:
            option_case_or_subject_by_xpath = self.config.get("LOCATORS", "option_case_or_subject")
            return option_case_or_subject_by_xpath
        except Exception as ex:
            print("option_case_or_subject_by_xpath : ", ex)

    def notes_filter_search_button_by_xpath(self):
        try:
            notes_filter_search_button_by_xpath = self.config.get("LOCATORS", "notes_filter_search_button")
            return notes_filter_search_button_by_xpath
        except Exception as ex:
            print("notes_filter_search_button_by_xpath : ", ex)

    def notes_filter_search_clear_button_by_xpath(self):
        try:
            notes_filter_search_clear_button_by_xpath = self.config.get("LOCATORS", "notes_filter_search_clear_button")
            return notes_filter_search_clear_button_by_xpath
        except Exception as ex:
            print("notes_filter_search_clear_button_by_xpath : ", ex)

    def location_or_store_search_result_validation_by_xpath(self):
        try:
            location_or_store_search_result_validation_by_xpath = self.config.get(
                "VALIDATION", "location_or_store_search_result_validation")
            return location_or_store_search_result_validation_by_xpath
        except Exception as ex:
            print("location_or_store_search_result_validation_by_xpath : ", ex)

    def case_or_subject_search_result_validation_by_xpath(self):
        try:
            case_or_subject_search_result_validation_by_xpath = self.config.get(
                "VALIDATION", "case_or_subject_search_result_validation")
            return case_or_subject_search_result_validation_by_xpath
        except Exception as ex:
            print("case_or_subject_search_result_validation_by_xpath : ", ex)

    def sort_by_result_validation_by_xpath(self):
        try:
            sort_by_result_validation_by_xpath = self.config.get(
                "VALIDATION", "sort_by_result_validation")
            return sort_by_result_validation_by_xpath
        except Exception as ex:
            print("sort_by_result_validation_by_xpath : ", ex)

    def get_location_or_store(self):
        try:
            get_location_or_store = self.common_test_data_config.get("Notes_Search_Filter_Combination_Data", "location_or_store")
            return get_location_or_store
        except Exception as ex:
            print("get_location_or_store : ", ex)

    def get_case_or_subject(self):
        try:
            get_case_or_subject = self.common_test_data_config.get("Notes_Search_Filter_Combination_Data", "case_or_subject")
            return get_case_or_subject
        except Exception as ex:
            print("get_case_or_subject : ", ex)

    def get_sort_by_location_or_store(self):
        try:
            get_sort_by = self.common_test_data_config.get("Notes_Search_Filter_Combination_Data", "sort_by_location_or_store")
            return get_sort_by
        except Exception as ex:
            print("get_sort_by : ", ex)

    def get_sort_by_case_or_subject(self):
        try:
            get_sort_by = self.common_test_data_config.get("Notes_Search_Filter_Combination_Data", "sort_by_case_or_subject")
            return get_sort_by
        except Exception as ex:
            print("get_sort_by : ", ex)
