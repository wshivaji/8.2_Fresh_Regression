import configparser
from pathlib import Path

filepath = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\18_Reporting_Module\\Data_From_INI\\Reporting.ini"
print("configure filepath: ", filepath)


class Reporting_read_ini:
    def __init__(self):
        try:
            self.config = configparser.RawConfigParser()
            self.config.read(filepath)
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print(ex)

    def get_core_username(self):
        try:
            core_username = self.common_test_data_config.get("Login_Logout_Data", "username")
            print("core username:", core_username)
            return core_username
        except Exception as ex:
            print(ex)

    def get_core_password(self):
        try:
            core_password = self.common_test_data_config.get("Login_Logout_Data", "password")
            print("core password: ", core_password)
            return core_password
        except Exception as ex:
            print(ex)

    def get_all_zones(self):
        try:
            all_zones = self.common_test_data_config.get("Reporting_Data", "all_zones")
            print("core password: ", all_zones)
            return all_zones
        except Exception as ex:
            print(ex)

    def get_dashboard_menu_items_by_xpath(self):
        try:
            dashboard_menu_items = self.config.get("Reporting", "dashboard_menu_items_by_xpath")
            print("dashboard items: ", dashboard_menu_items)
            return dashboard_menu_items
        except Exception as ex:
            print(ex)

    def get_reporting_module(self):
        try:
            reporting_module_name = self.common_test_data_config.get("Reporting_Data", "reporting_module")
            print("reporting module name: ", reporting_module_name)
            return reporting_module_name
        except Exception as ex:
            print(ex)

    def get_reporting_module_by_xpath(self):
        try:
            reporting_module = self.config.get("Reporting", "reporting_module_by_xpath")
            print("reporting module: ", reporting_module)
            return reporting_module
        except Exception as ex:
            print(ex)

    def get_reporting_panel_heading_by_xpath(self):
        try:
            reporting_panel_heading = self.config.get("Reporting", "reporting_panel_heading_by_xpath")
            print("reporting panel heading: ", reporting_panel_heading)
            return reporting_panel_heading
        except Exception as ex:
            print(ex)

    def get_close_panel_button_by_xpath(self):
        try:
            close_panel_button = self.config.get("Reporting", "close_panel_button_by_xpath")
            print("Close Panel button: ", close_panel_button)
            return close_panel_button
        except Exception as ex:
            print(ex)

    def get_report_selection_text_on_heading_by_xpath(self):
        try:
            report_selection_text_on_heading = self.config.get("Reporting", "report_selection_text_on_heading_by_xpath")
            print("REPORT SELECTION text: ", report_selection_text_on_heading)
            return report_selection_text_on_heading
        except Exception as ex:
            print(ex)

    def get_expected_report_selection_text(self):
        try:
            report_selection_text = self.common_test_data_config.get("Reporting_Data", "report_selection_text")
            print("expected REPORT SELECTION text: ", report_selection_text)
            return report_selection_text
        except Exception as ex:
            print(ex)

    def get_chart_icon_beside_report_selection_text_by_xpath(self):
        try:
            chart_icon_beside_report_selection_text = self.config.get("Reporting", "chart_icon_beside_report_selection_text_by_xpath")
            print("Chart icon: ", chart_icon_beside_report_selection_text)
            return chart_icon_beside_report_selection_text
        except Exception as ex:
            print(ex)

    def get_select_report_criteria_text_by_xpath(self):
        try:
            select_report_criteria_text_by_xpath = self.config.get("Reporting", "select_report_criteria_text_by_xpath")
            print("'Select report criteria:' text: ", select_report_criteria_text_by_xpath)
            return select_report_criteria_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_select_report_criteria_text(self):
        try:
            select_report_criteria_text = self.common_test_data_config.get("Reporting_Data", "select_report_criteria_text")
            print("expected Select report criteria: text: ", select_report_criteria_text)
            return select_report_criteria_text
        except Exception as ex:
            print(ex)

    def get_report_the_text_by_xpath(self):
        try:
            report_the_text_by_xpath = self.config.get("Reporting", "report_the_text_by_xpath")
            print("'Report the' text: ", report_the_text_by_xpath)
            return report_the_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_report_the_text(self):
        try:
            report_the_text = self.common_test_data_config.get("Reporting_Data", "report_the_text")
            print("expected Report the text: ", report_the_text)
            return report_the_text
        except Exception as ex:
            print(ex)

    def get_report_field1_dropdown_by_xpath(self):
        try:
            report_field1_dropdown = self.config.get("Reporting", "report_field1_dropdown_by_xpath")
            print("report field1 dropdown: ", report_field1_dropdown)
            return report_field1_dropdown
        except Exception as ex:
            print(ex)

    def get_report_field1_dropdown_items_by_xpath(self):
        try:
            report_field1_dropdown_items = self.config.get("Reporting", "report_field1_dropdown_items_by_xpath")
            print("report field1 dropdown items: ", report_field1_dropdown_items)
            return report_field1_dropdown_items
        except Exception as ex:
            print(ex)

    def get_expected_report_field_items(self):
        try:
            report_field_items = self.config.get("Reporting", "report_field_items")
            print("expected report field items: ", report_field_items)
            return report_field_items
        except Exception as ex:
            print(ex)

    def get_expected_first_text_from_field1(self):
        try:
            expected_first_text_from_field1 = self.common_test_data_config.get("Reporting_Data", "expected_first_text_from_field1")
            print("expected first text from field1: ", expected_first_text_from_field1)
            return expected_first_text_from_field1
        except Exception as ex:
            print(ex)

    def get_expected_second_text_from_field1(self):
        try:
            expected_second_text_from_field1 = self.common_test_data_config.get("Reporting_Data", "expected_second_text_from_field1")
            print("expected second text from field1: ", expected_second_text_from_field1)
            return expected_second_text_from_field1
        except Exception as ex:
            print(ex)

    def get_expected_third_text_from_field1(self):
        try:
            expected_third_text_from_field1 = self.common_test_data_config.get("Reporting_Data", "expected_third_text_from_field1")
            print("expected third text from field1: ", expected_third_text_from_field1)
            return expected_third_text_from_field1
        except Exception as ex:
            print(ex)

    def get_report_field2_dropdown_for_events_by_xpath(self):
        try:
            report_field2_dropdown = self.config.get("Reporting", "field2_dropdown_for_events_by_xpath")
            print("report field2 dropdown: ", report_field2_dropdown)
            return report_field2_dropdown
        except Exception as ex:
            print(ex)

    def get_report_field2_dropdown_items_for_events_by_xpath(self):
        try:
            report_field2_dropdown_items = self.config.get("Reporting", "field2_dropdown_items_for_events_by_xpath")
            print("expected report field2 items: ", report_field2_dropdown_items)
            return report_field2_dropdown_items
        except Exception as ex:
            print(ex)

    def get_by_text_xpath(self):
        try:
            by_text_xpath = self.config.get("Reporting", "by_text_xpath")
            print("'by' text:" , by_text_xpath)
            return by_text_xpath
        except Exception as ex:
            print(ex)

    def get_expected_by_text(self):
        try:
            expected_by_text = self.common_test_data_config.get("Reporting_Data", "expected_by_text")
            print("expected 'by' text: ", expected_by_text)
            return expected_by_text
        except Exception as ex:
            print(ex)

    def get_field2_dropdown_for_visitors_by_xpath(self):
        try:
            field2_dropdown_for_visitors = self.config.get("Reporting", "field2_dropdown_for_visitors_by_xpath")
            print("field2 dropdown for visitors: ", field2_dropdown_for_visitors)
            return field2_dropdown_for_visitors
        except Exception as ex:
            print(ex)

    def get_field2_dropdown_items_for_visitors_by_xpath(self):
        try:
            field2_dropdown_items_for_visitors = self.config.get("Reporting", "field2_dropdown_items_for_visitors_by_xpath")
            print("field2 dropdown items for visitors: ", field2_dropdown_items_for_visitors)
            return field2_dropdown_items_for_visitors
        except Exception as ex:
            print(ex)

    def get_field2_dropdown_for_enrollments_by_xpath(self):
        try:
            field2_dropdown_for_enrollments = self.config.get("Reporting", "field2_dropdown_for_enrollments_by_xpath")
            print("field2 dropdown for enrollments: ", field2_dropdown_for_enrollments)
            return field2_dropdown_for_enrollments
        except Exception as ex:
            print(ex)

    def get_field2_dropdown_items_for_enrollments_by_xpath(self):
        try:
            field2_dropdown_items_for_enrollments = self.config.get("Reporting", "field2_dropdown_items_for_enrollments_by_xpath")
            print("field2 dropdown items for enrollments: ", field2_dropdown_items_for_enrollments)
            return field2_dropdown_items_for_enrollments
        except Exception as ex:
            print(ex)

    def get_expected_enrollment_text_from_field2(self):
        try:
            expected_enrollment_text_from_field2 = self.common_test_data_config.get("Reporting_Data", "expected_enrollment_text_from_field2")
            print("expected enrollment text from field2: ", expected_enrollment_text_from_field2)
            return expected_enrollment_text_from_field2
        except Exception as ex:
            print(ex)

    def get_expected_first_text_from_field2(self):
        try:
            expected_first_text_from_field2 = self.common_test_data_config.get("Reporting_Data", "expected_first_text_from_field2")
            print("expected first text from field2: ", "expected_first_text_from_field2")
            return expected_first_text_from_field2
        except Exception as ex:
            print(ex)

    def get_expected_second_text_from_field2(self):
        try:
            expected_second_text_from_field2 = self.common_test_data_config.get("Reporting_Data", "expected_second_text_from_field2")
            print("expected second text from field2: ", expected_second_text_from_field2)
            return expected_second_text_from_field2
        except Exception as ex:
            print(ex)

    def get_expected_third_text_from_field2(self):
        try:
            expected_third_text_from_field2 = self.common_test_data_config.get("Reporting_Data", "expected_third_text_from_field2")
            print("expected third text from field2: ", expected_third_text_from_field2)
            return expected_third_text_from_field2
        except Exception as ex:
            print(ex)

    def get_expected_fourth_text_from_field2(self):
        try:
            expected_fourth_text_from_field2 = self.common_test_data_config.get("Reporting_Data", "expected_fourth_text_from_field2")
            print("expected fourth text from field2: ", expected_fourth_text_from_field2)
            return expected_fourth_text_from_field2
        except Exception as ex:
            print(ex)

    def get_date_range_text_by_xpath(self):
        try:
            date_range_text = self.config.get("Reporting", "date_range_text_by_xpath")
            print("date range text: ", date_range_text)
            return date_range_text
        except Exception as ex:
            print(ex)

    def get_expected_date_range_text(self):
        try:
            expected_date_range_text = self.common_test_data_config.get("Reporting_Data", "expected_date_range_text")
            print("expected date range text: ", expected_date_range_text)
            return expected_date_range_text
        except Exception as ex:
            print(ex)

    def get_date_and_time_range_text_by_xpath(self):
        try:
            date_and_time_range_text = self.config.get("Reporting", "date_and_time_range_text_by_xpath")
            print("date & time range text: ", date_and_time_range_text)
            return date_and_time_range_text
        except Exception as ex:
            print(ex)

    def get_expected_date_and_time_range_text(self):
        try:
            expected_date_and_time_range_text = self.common_test_data_config.get("Reporting_Data", "expected_date_and_time_range_text")
            print("expected date & time range text: ", expected_date_and_time_range_text)
            return expected_date_and_time_range_text
        except Exception as ex:
            print(ex)

    def get_between_text_by_xpath(self):
        try:
            between_text_by_xpath = self.config.get("Reporting", "between_text_by_xpath")
            print("between text: ", between_text_by_xpath)
            return between_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_between_text(self):
        try:
            expected_between_text = self.common_test_data_config.get("Reporting_Data", "expected_between_text")
            print("expected between text: ", expected_between_text)
            return expected_between_text
        except Exception as ex:
            print(ex)

    def get_to_text_by_xpath(self):
        try:
            to_text_by_xpath = self.config.get("Reporting", "to_text_by_xpath")
            print("to text: ", to_text_by_xpath)
            return to_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_to_text(self):
        try:
            expected_to_text = self.common_test_data_config.get("Reporting_Data", "expected_to_text")
            print("expected to text: ", expected_to_text)
            return expected_to_text
        except Exception as ex:
            print(ex)

    def get_horizontal_line_below_calenders_by_xpath(self):
        try:
            horizontal_line_below_calenders_by_xpath = self.config.get("Reporting", "horizontal_line_below_calenders_by_xpath")
            print("horizontal line below calenders: ", horizontal_line_below_calenders_by_xpath)
            return horizontal_line_below_calenders_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_horizontal_line_below_calenders(self):
        try:
            expected_horizontal_line_below_calenders = self.common_test_data_config.get("Reporting_Data", "expected_horizontal_line_below_calenders")
            print("expected horizontal line below calenders: ", expected_horizontal_line_below_calenders)
            return expected_horizontal_line_below_calenders
        except Exception as ex:
            print(ex)

    def get_start_date_calender_box_by_xpath(self):
        try:
            start_date_calender_box_by_xpath = self.config.get("Reporting", "start_date_calender_box_by_xpath")
            print("start date calender box: ", start_date_calender_box_by_xpath)
            return start_date_calender_box_by_xpath
        except Exception as ex:
            print(ex)

    def get_start_date_checkbox_by_xpath(self):
        try:
            start_date_checkbox_by_xpath = self.config.get("Reporting", "start_date_checkbox_by_xpath")
            print("start date checkbox: ", start_date_checkbox_by_xpath)
            return start_date_checkbox_by_xpath
        except Exception as ex:
            print(ex)

    def get_start_date_label_on_calender_box(self):
        try:
            start_date_label_on_calender_box = self.common_test_data_config.get("Reporting_Data", "start_date_label_on_calender_box")
            print("start date label on calender box: ", start_date_label_on_calender_box)
            return start_date_label_on_calender_box
        except Exception as ex:
            print(ex)

    def get_end_date_calender_box_by_xpath(self):
        try:
            end_date_calender_box_by_xpath = self.config.get("Reporting", "end_date_calender_box_by_xpath")
            print("end date calender box: ", end_date_calender_box_by_xpath)
            return end_date_calender_box_by_xpath
        except Exception as ex:
            print(ex)

    def get_end_date_checkbox_by_xpath(self):
        try:
            end_date_checkbox_by_xpath = self.config.get("Reporting", "end_date_checkbox_by_xpath")
            print("end date checkbox: ", end_date_checkbox_by_xpath)
            return end_date_checkbox_by_xpath
        except Exception as ex:
            print(ex)

    def get_end_date_label_on_calender_box(self):
        try:
            end_date_label_on_calender_box = self.common_test_data_config.get("Reporting_Data", "end_date_label_on_calender_box")
            print("end date label on calender box: ", end_date_label_on_calender_box)
            return end_date_label_on_calender_box
        except Exception as ex:
            print(ex)

    def get_optional_filters_text_by_xpath(self):
        try:
            optional_filters_text_by_xpath = self.config.get("Reporting", "optional_filters_text_by_xpath")
            print("optional filters text xpath: ", optional_filters_text_by_xpath)
            return optional_filters_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_optional_filters_text(self):
        try:
            expected_optional_filters_text = self.common_test_data_config.get("Reporting_Data", "expected_optional_filters_text")
            print("expected optional filters text: ", expected_optional_filters_text)
            return expected_optional_filters_text
        except Exception as ex:
            print(ex)

    def get_age_range_text_by_xpath(self):
        try:
            age_range_text_by_xpath = self.config.get("Reporting", "age_range_text_by_xpath")
            print("age range text: ", age_range_text_by_xpath)
            return age_range_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_age_range_text(self):
        try:
            expected_age_range_text = self.common_test_data_config.get("Reporting_Data", "expected_age_range_text")
            print("expected age range text: ", expected_age_range_text)
            return expected_age_range_text
        except Exception as ex:
            print(ex)

    def get_start_age_dropdown_by_xpath(self):
        try:
            start_age_dropdown_by_xpath = self.config.get("Reporting", "start_age_dropdown_by_xpath")
            print("start age dropdown: ", start_age_dropdown_by_xpath)
            return start_age_dropdown_by_xpath
        except Exception as ex:
            print(ex)

    def get_start_age_dropdown_items_by_xpath(self):
        try:
            start_age_dropdown_items_by_xpath = self.config.get("Reporting", "start_age_dropdown_items_by_xpath")
            print(f"start age dropdown items: {start_age_dropdown_items_by_xpath}")
            return start_age_dropdown_items_by_xpath
        except Exception as ex:
            print(ex)

    def get_end_age_dropdown_by_xpath(self):
        try:
            end_age_dropdown_by_xpath = self.config.get("Reporting", "end_age_dropdown_by_xpath")
            print("end age dropdown: ", end_age_dropdown_by_xpath)
            return end_age_dropdown_by_xpath
        except Exception as ex:
            print(ex)

    def get_end_age_dropdown_items_by_xpath(self):
        try:
            end_age_dropdown_items_by_xpath = self.config.get("Reporting", "end_age_dropdown_items_by_xpath")
            print(f"end age dropdown items: {end_age_dropdown_items_by_xpath}")
            return end_age_dropdown_items_by_xpath
        except Exception as ex:
            print(ex)

    def get_number_of_ages_to_group_totals_by_text_by_xpath(self):
        try:
            number_of_ages_to_group_totals_by_text_by_xpath = self.config.get("Reporting", "number_of_ages_to_group_totals_by_text_by_xpath")
            print("number of ages to group totals by text: ", number_of_ages_to_group_totals_by_text_by_xpath)
            return number_of_ages_to_group_totals_by_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_number_of_ages_to_group_totals_by_text(self):
        try:
            expected_number_of_ages_to_group_totals_by_text = self.common_test_data_config.get("Reporting_Data", "expected_number_of_ages_to_group_totals_by_text")
            print("expected number of ages to group totals by text: ", expected_number_of_ages_to_group_totals_by_text)
            return expected_number_of_ages_to_group_totals_by_text
        except Exception as ex:
            print(ex)

    def get_number_of_ages_to_group_totals_by_dropdown_by_xpath(self):
        try:
            number_of_ages_to_group_totals_by_dropdown = self.config.get("Reporting", "number_of_ages_to_group_totals_by_dropdown_by_xpath")
            print("number of ages to group totals by dropdown: ", number_of_ages_to_group_totals_by_dropdown)
            return number_of_ages_to_group_totals_by_dropdown
        except Exception as ex:
            print(ex)

    def get_number_of_ages_to_group_totals_by_dropdown_items(self):
        try:
            number_of_ages_to_group_totals_by_dropdown_items = self.config.get("Reporting", "number_of_ages_to_group_totals_by_dropdown_items_by_xpath")
            print(f"age bucket dropdown items: {number_of_ages_to_group_totals_by_dropdown_items}")
            return number_of_ages_to_group_totals_by_dropdown_items
        except Exception as ex:
            print(ex)

    def get_include_in_search_hover_on_start_checkbox_by_xpath(self):
        try:
            include_in_search_hover_on_start_checkbox_by_xpath = self.config.get("Reporting", "include_in_search_hover_on_start_checkbox_by_xpath")
            print("include in search hover on start checkbox: ", include_in_search_hover_on_start_checkbox_by_xpath)
            return include_in_search_hover_on_start_checkbox_by_xpath
        except Exception as ex:
            print(ex)

    def get_include_in_search_hover_on_end_checkbox_by_xpath(self):
        try:
            include_in_search_hover_on_end_checkbox_by_xpath = self.config.get("Reporting", "include_in_search_hover_on_end_checkbox_by_xpath")
            print("include in search hover on end checkbox: ", include_in_search_hover_on_end_checkbox_by_xpath)
            return include_in_search_hover_on_end_checkbox_by_xpath
        except Exception as ex:
            print(ex)

    def get_gender_text_by_xpath(self):
        try:
            gender_text_by_xpath = self.config.get("Reporting", "gender_text_by_xpath")
            print("gender text: ", gender_text_by_xpath)
            return gender_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_gender_text(self):
        try:
            expected_gender_text = self.common_test_data_config.get("Reporting_Data", "expected_gender_text")
            print("expected gender text: ", expected_gender_text)
            return expected_gender_text
        except Exception as ex:
            print(ex)

    def get_male_text_by_xpath(self):
        try:
            male_text_by_xpath = self.config.get("Reporting", "male_text_by_xpath")
            print("male text: ", male_text_by_xpath)
            return male_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_male_text(self):
        try:
            expected_male_text = self.common_test_data_config.get("Reporting_Data", "expected_male_text")
            print("expected male text: ", expected_male_text)
            return expected_male_text
        except Exception as ex:
            print(ex)

    def get_female_text_by_xpath(self):
        try:
            female_text_by_xpath = self.config.get("Reporting", "female_text_by_xpath")
            print("female text: ", female_text_by_xpath)
            return female_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_female_text(self):
        try:
            expected_female_text = self.common_test_data_config.get("Reporting_Data", "expected_female_text")
            print("expected female text: ", expected_female_text)
            return expected_female_text
        except Exception as ex:
            print(ex)

    def get_unknown_gender_text_by_xpath(self):
        try:
            unknown_gender_text_by_xpath = self.config.get("Reporting", "unknown_gender_text_by_xpath")
            print("unknown gender text: ", unknown_gender_text_by_xpath)
            return unknown_gender_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_unknown_gender_text(self):
        try:
            expected_unknown_gender_text = self.common_test_data_config.get("Reporting_Data", "expected_unknown_gender_text")
            print("expected unknown gender text: ", expected_unknown_gender_text)
            return expected_unknown_gender_text
        except Exception as ex:
            print(ex)

    def get_male_filter_checkbox(self):
        try:
            male_filter_checkbox = self.config.get("Reporting", "male_filter_checkbox")
            print("male filter checkbox: ", male_filter_checkbox)
            return male_filter_checkbox
        except Exception as ex:
            print(ex)

    def get_female_filter_checkbox(self):
        try:
            female_filter_checkbox = self.config.get("Reporting", "female_filter_checkbox")
            print("female filter checkbox: ", female_filter_checkbox)
            return female_filter_checkbox
        except Exception as ex:
            print(ex)

    def get_unknown_gender_filter_checkbox(self):
        try:
            unknown_gender_filter_checkbox = self.config.get("Reporting", "unknown_gender_filter_checkbox")
            print("unknown gender filter checkbox: ", unknown_gender_filter_checkbox)
            return unknown_gender_filter_checkbox
        except Exception as ex:
            print(ex)

    def get_select_group_filter_button_by_xpath(self):
        try:
            select_group_filter_button_by_xpath = self.config.get("Reporting", "select_group_filter_button_by_xpath")
            print("select group filter button: ", select_group_filter_button_by_xpath)
            return select_group_filter_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_group_icon_on_select_group_filter_button_by_xpath(self):
        try:
            group_icon_on_select_group_filter_button_by_xpath = self.config.get("Reporting", "group_icon_on_select_group_filter_button_by_xpath")
            print("group icon on select group filter button: ", group_icon_on_select_group_filter_button_by_xpath)
            return group_icon_on_select_group_filter_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_select_group_filter_text_on_button_by_xpath(self):
        try:
            select_group_filter_text_on_button_by_xpath = self.config.get("Reporting", "select_group_filter_text_on_button_by_xpath")
            print("select group filter text on button: ", select_group_filter_text_on_button_by_xpath)
            return select_group_filter_text_on_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_select_group_filter_button(self):
        try:
            expected_text_on_select_group_filter_button = self.common_test_data_config.get("Reporting_Data", "expected_text_on_select_group_filter_button")
            print("expected text on select group filter button: ", expected_text_on_select_group_filter_button)
            return expected_text_on_select_group_filter_button
        except Exception as ex:
            print(ex)

    def get_horizontal_line_below_reporting_panel_heading_for_group_by_xpath(self):
        try:
            horizontal_line_below_reporting_panel_heading_for_group = self.config.get("Reporting", "horizontal_line_below_reporting_panel_heading_for_group_by_xpath")
            print("horizontal line in select group filter panel: ", horizontal_line_below_reporting_panel_heading_for_group)
            return horizontal_line_below_reporting_panel_heading_for_group
        except Exception as ex:
            print(ex)

    def get_expected_horizontal_line_below_reporting_panel_heading_for_group(self):
        try:
            expected_horizontal_line_below_reporting_panel_heading_for_group = self.common_test_data_config.get("Reporting_Data", "expected_horizontal_line_below_reporting_panel_heading_for_group")
            print("expected heading for select filter result panel: ", expected_horizontal_line_below_reporting_panel_heading_for_group)
            return expected_horizontal_line_below_reporting_panel_heading_for_group
        except Exception as ex:
            print(ex)

    def get_filter_group_list_textbox_by_xpath(self):
        try:
            filter_group_list_textbox_by_xpath = self.config.get("Reporting", "filter_group_list_textbox_by_xpath")
            print("filter group list textbox: ", filter_group_list_textbox_by_xpath)
            return filter_group_list_textbox_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_label_on_filter_group_list_below_textbox(self):
        try:
            expected_label_on_filter_group_list_below_textbox = self.common_test_data_config.get("Reporting_Data", "expected_label_on_filter_group_list_below_textbox")
            print("expected label on 'filter group list below...' textbox: ", expected_label_on_filter_group_list_below_textbox)
            return expected_label_on_filter_group_list_below_textbox
        except Exception as ex:
            print(ex)

    def get_group_items_list_below_filter_group_list_textbox(self):
        try:
            group_items_list_below_filter_group_list_textbox = self.config.get("Reporting", "group_items_list_below_filter_group_list_textbox")
            print("group items below filter group list textbox: ", group_items_list_below_filter_group_list_textbox)
            return group_items_list_below_filter_group_list_textbox
        except Exception as ex:
            print(ex)

    def get_enrollment_groups_module_on_dashboard_by_xpath(self):
        try:
            enrollment_groups_module_on_dashboard_by_xpath = self.config.get("Reporting", "enrollment_groups_module_on_dashboard_by_xpath")
            print("enrollment groups module: ", enrollment_groups_module_on_dashboard_by_xpath)
            return enrollment_groups_module_on_dashboard_by_xpath
        except Exception as ex:
            print(ex)

    def get_group_item_list_from_enrollment_group_panel_by_xpath(self):
        try:
            group_item_list_from_enrollment_group_panel_by_xpath = self.config.get("Reporting", "group_item_list_from_enrollment_group_panel_by_xpath")
            print("group items list from enrollment groups panel: ", group_item_list_from_enrollment_group_panel_by_xpath)
            return group_item_list_from_enrollment_group_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_select_all_button_in_group_filter_by_xpath(self):
        try:
            select_all_button_in_group_filter_by_xpath = self.config.get("Reporting", "select_all_button_in_group_filter_by_xpath")
            print("select all button in group filter: ", select_all_button_in_group_filter_by_xpath)
            return select_all_button_in_group_filter_by_xpath
        except Exception as ex:
            print(ex)

    def get_select_zone_filter_button_by_xpath(self):
        try:
            select_zone_filter_button_by_xpath = self.config.get("Reporting", "select_zone_filter_button_by_xpath")
            print("'Select zone filter' button: ", select_zone_filter_button_by_xpath)
            return select_zone_filter_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_dot_circle_icon_for_zone_by_xpath(self):
        try:
            dot_circle_icon_for_zone_by_xpath = self.config.get("Reporting", "dot_circle_icon_for_zone_by_xpath")
            print("dot circle icon for zone: ", dot_circle_icon_for_zone_by_xpath)
            return dot_circle_icon_for_zone_by_xpath
        except Exception as ex:
            print(ex)

    def get_select_zone_filter_text_on_button_by_xpath(self):
        try:
            select_zone_filter_text_on_button_by_xpath = self.config.get("Reporting", "select_zone_filter_text_on_button_by_xpath")
            print("'Select zone filter' text on button: ", select_zone_filter_text_on_button_by_xpath)
            return select_zone_filter_text_on_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_select_zone_filter_button(self):
        try:
            expected_text_on_select_zone_filter_button = self.common_test_data_config.get("Reporting_Data", "expected_text_on_select_zone_filter_button")
            print("expected text on select zone filter button: ", expected_text_on_select_zone_filter_button)
            return expected_text_on_select_zone_filter_button
        except Exception as ex:
            print(ex)

    def get_text_beside_select_zone_filter_button_by_xpath(self):
        try:
            text_beside_select_zone_filter_button_by_xpath = self.config.get("Reporting", "text_beside_select_zone_filter_button_by_xpath")
            print("text beside select zone filter button: ", text_beside_select_zone_filter_button_by_xpath)
            return text_beside_select_zone_filter_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_beside_select_zone_filter_button(self):
        try:
            expected_text_beside_select_zone_filter_button = self.common_test_data_config.get("Reporting_Data", "expected_text_beside_select_zone_filter_button")
            print("expected text beside select zone filter button:", expected_text_beside_select_zone_filter_button)
            return expected_text_beside_select_zone_filter_button
        except Exception as ex:
            print(ex)

    def get_text_beside_select_group_filter_button_by_xpath(self):
        try:
            text_beside_select_group_filter_button_by_xpath = self.config.get("Reporting", "text_beside_select_group_filter_button_by_xpath")
            print("text beside select group filter button: ", text_beside_select_group_filter_button_by_xpath)
            return text_beside_select_group_filter_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_beside_select_group_filter_button(self):
        try:
            expected_text_beside_select_group_filter_button = self.common_test_data_config.get("Reporting_Data", "expected_text_beside_select_group_filter_button")
            print("expected text beside select group filter button: ", expected_text_beside_select_group_filter_button)
            return expected_text_beside_select_group_filter_button
        except Exception as ex:
            print(ex)

    def get_generate_report_button_by_xpath(self):
        try:
            generate_report_button_by_xpath = self.config.get("Reporting", "generate_report_button_by_xpath")
            print("generate report button: ", generate_report_button_by_xpath)
            return generate_report_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_chart_icon_on_generate_report_button_by_xpath(self):
        try:
            chart_icon_on_generate_report_button_by_xpath = self.config.get("Reporting", "chart_icon_on_generate_report_button_by_xpath")
            print("chart icon on generate report button: ", chart_icon_on_generate_report_button_by_xpath)
            return chart_icon_on_generate_report_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_generate_report_text_on_button_by_xpath(self):
        try:
            generate_report_text_on_button_by_xpath = self.config.get("Reporting", "generate_report_text_on_button_by_xpath")
            print("generate report text on button: ", generate_report_text_on_button_by_xpath)
            return generate_report_text_on_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_generate_report_text_on_button(self):
        try:
            expected_generate_report_text_on_button = self.common_test_data_config.get("Reporting_Data", "expected_generate_report_text_on_button")
            print("expected generate report text on button: ", expected_generate_report_text_on_button)
            return expected_generate_report_text_on_button
        except Exception as ex:
            print(ex)

    def get_search_zone_textbox_by_xpath(self):
        try:
            search_zone_text_box_by_xpath = self.config.get("Reporting", "search_zone_text_box_by_xpath")
            print("search zone... textbox: ", search_zone_text_box_by_xpath)
            return search_zone_text_box_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_label_on_search_zone_textbox(self):
        try:
            expected_label_on_search_zone_textbox = self.common_test_data_config.get("Reporting_Data", "expected_label_on_search_zone_textbox")
            print("expected label on search zone textbox: ", expected_label_on_search_zone_textbox)
            return expected_label_on_search_zone_textbox
        except Exception as ex:
            print(ex)

    def get_zone_items_list_below_search_zone_textbox_by_xpath(self):
        try:
            zone_items_list_below_search_zone_textbox_by_xpath = self.config.get("Reporting", "zone_items_list_below_search_zone_textbox_by_xpath")
            print("zone items list below search zone textbox: ", zone_items_list_below_search_zone_textbox_by_xpath)
            return zone_items_list_below_search_zone_textbox_by_xpath
        except Exception as ex:
            print(ex)

    def get_zone_module_on_dashboard_by_xpath(self):
        try:
            zone_module_on_dashboard_by_xpath = self.config.get("Reporting", "zone_module_on_dashboard_by_xpath")
            print("zone module on dashboard: ", zone_module_on_dashboard_by_xpath)
            return zone_module_on_dashboard_by_xpath
        except Exception as ex:
            print(ex)

    def get_zone_item_list_from_zone_panel_by_xpath(self):
        try:
            zone_item_list_from_zone_panel_by_xpath = self.config.get("Reporting", "zone_item_list_from_zone_panel_by_xpath")
            print("actual zone item list from zone panel: ", zone_item_list_from_zone_panel_by_xpath)
            return zone_item_list_from_zone_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_selected_zone_list_items_by_xpath(self):
        try:
            selected_zone_list_items_by_xpath = self.config.get("Reporting", "selected_zone_list_items_by_xpath")
            print("selected zone list items: ", selected_zone_list_items_by_xpath)
            return selected_zone_list_items_by_xpath
        except Exception as ex:
            print(ex)

    def get_horizontal_line_below_reporting_panel_heading_by_xpath(self):
        try:
            horizontal_line_below_reporting_panel_heading_by_xpath = self.config.get("Reporting", "horizontal_line_below_reporting_panel_heading_by_xpath")
            print("horizontal line below reporting panel heading: ", horizontal_line_below_reporting_panel_heading_by_xpath)
            return horizontal_line_below_reporting_panel_heading_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_horizontal_line_below_reporting_panel_heading(self):
        try:
            expected_horizontal_line_below_reporting_panel_heading = self.common_test_data_config.get("Reporting_Data", "expected_horizontal_line_below_reporting_panel_heading")
            print("expected horizontal line below reporting panel heading: ", expected_horizontal_line_below_reporting_panel_heading)
            return expected_horizontal_line_below_reporting_panel_heading
        except Exception as ex:
            print(ex)

    def get_select_all_button_in_zone_filter_by_xpath(self):
        try:
            select_all_button_in_zone_filter_by_xpath = self.config.get("Reporting", "select_all_button_in_zone_filter_by_xpath")
            print("select all button: ", select_all_button_in_zone_filter_by_xpath)
            return select_all_button_in_zone_filter_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_select_all_button(self):
        try:
            expected_text_on_select_all_button = self.common_test_data_config.get("Reporting_Data", "expected_text_on_select_all_button")
            print("expected text on select all button: ", expected_text_on_select_all_button)
            return expected_text_on_select_all_button
        except Exception as ex:
            print(ex)

    def get_selected_group_list_title_by_xpath(self):
        try:
            selected_group_list_title_by_xpath = self.config.get("Reporting", "selected_group_list_title_by_xpath")
            print("selected group list title: ", selected_group_list_title_by_xpath)
            return selected_group_list_title_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_selected_group_list_title(self):
        try:
            expected_selected_group_list_title = self.common_test_data_config.get("Reporting_Data", "expected_selected_group_list_title")
            print("expected selected group list title: ", expected_selected_group_list_title)
            return expected_selected_group_list_title
        except Exception as ex:
            print(ex)

    def get_expected_first_default_text_line_below_selected_group_list_title(self):
        try:
            expected_first_default_text_line_below_selected_group_list_title = self.common_test_data_config.get("Reporting_Data", "expected_first_default_text_line_below_selected_group_list_title")
            print("expected first default line below selected group list: ", expected_first_default_text_line_below_selected_group_list_title)
            return expected_first_default_text_line_below_selected_group_list_title
        except Exception as ex:
            print(ex)

    def get_expected_second_default_text_line_below_selected_group_list_title(self):
        try:
            expected_second_default_text_line_below_selected_group_list_title = self.common_test_data_config.get("Reporting_Data", "expected_second_default_text_line_below_selected_group_list_title")
            print("second default line below selected group list: ", expected_second_default_text_line_below_selected_group_list_title)
            return expected_second_default_text_line_below_selected_group_list_title
        except Exception as ex:
            print(ex)

    def get_close_group_menu_button_by_xpath(self):
        try:
            close_group_menu_button_by_xpath = self.config.get("Reporting", "close_group_menu_button_by_xpath")
            print("close group menu button: ", close_group_menu_button_by_xpath)
            return close_group_menu_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_close_group_menu_button(self):
        try:
            expected_text_on_close_group_menu_button = self.common_test_data_config.get("Reporting_Data", "expected_text_on_close_group_menu_button")
            print("expected text on close group menu button: ", expected_text_on_close_group_menu_button)
            return expected_text_on_close_group_menu_button
        except Exception as ex:
            print(ex)

    def get_text_on_close_group_menu_button_by_xpath(self):
        try:
            text_on_close_group_menu_button_by_xpath = self.config.get("Reporting", "text_on_close_group_menu_button_by_xpath")
            print("text on close group menu button: ", text_on_close_group_menu_button_by_xpath)
            return text_on_close_group_menu_button_by_xpath
        except Exception as ex:
            print(ex)
    def get_first_default_te_below_selected_group_list_title_by_xpath(self):
        try:
            first_default_te_below_selected_group_list_title_by_xpath = self.config.get("Reporting", "first_default_te_below_selected_group_list_title_by_xpath")
            print("first default text below selected group list title: ", first_default_te_below_selected_group_list_title_by_xpath)
            return first_default_te_below_selected_group_list_title_by_xpath
        except Exception as ex:
            print(ex)

    def get_second_default_text_below_selected_group_list_title_by_xpath(self):
        try:
            second_default_text_below_selected_group_list_title_by_xpath = self.config.get("Reporting", "second_default_text_below_selected_group_list_title_by_xpath")
            print("second default text below selected group list title: ", second_default_text_below_selected_group_list_title_by_xpath)
            return second_default_text_below_selected_group_list_title_by_xpath
        except Exception as ex:
            print(ex)

    def get_selected_group_list_items_by_xpath(self):
        try:
            selected_group_list_items_by_xpath = self.config.get("Reporting", "selected_group_list_items_by_xpath")
            print("selected group list items: ", selected_group_list_items_by_xpath)
            return selected_group_list_items_by_xpath
        except Exception as ex:
            print(ex)

    def get_clear_all_button_on_selected_group_by_xpath(self):
        try:
            clear_all_button_on_selected_group_by_xpath = self.config.get("Reporting", "clear_all_button_on_selected_group_by_xpath")
            print("clear all button on selected group: ", clear_all_button_on_selected_group_by_xpath)
            return clear_all_button_on_selected_group_by_xpath
        except Exception as ex:
            print(ex)

    def get_save_group_selection_button_by_xpath(self):
        try:
            save_group_selection_button_by_xpath = self.config.get("Reporting", "save_group_selection_button_by_xpath")
            print("save group selection button: ", save_group_selection_button_by_xpath)
            return save_group_selection_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_group_icon_on_save_group_selection_button_by_xpath(self):
        try:
            group_icon_on_save_group_selection_button_by_xpath = self.config.get("Reporting", "group_icon_on_save_group_selection_button_by_xpath")
            print("group icon on save group selection button: ", group_icon_on_save_group_selection_button_by_xpath)
            return group_icon_on_save_group_selection_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_save_group_selection_text_by_xpath(self):
        try:
            save_group_selection_text_by_xpath = self.config.get("Reporting", "save_group_selection_text_by_xpath")
            print("save group selection text: ", save_group_selection_text_by_xpath)
            return save_group_selection_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_save_group_selection_button(self):
        try:
            expected_save_group_selection_text = self.common_test_data_config.get("Reporting_Data", "expected_save_group_selection_text")
            print("expected text on save group selection button: ", expected_save_group_selection_text)
            return expected_save_group_selection_text
        except Exception as ex:
            print(ex)

    def get_selected_zone_list_title_by_xpath(self):
        try:
            selected_zone_list_title_by_xpath = self.config.get("Reporting", "selected_zone_list_title_by_xpath")
            print("selected zone list title: ", selected_zone_list_title_by_xpath)
            return selected_zone_list_title_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_selected_zone_list_title(self):
        try:
            expected_selected_zone_list_title = self.common_test_data_config.get("Reporting_Data", "expected_selected_zone_list_title")
            print("expected title selected zone list: ", expected_selected_zone_list_title)
            return expected_selected_zone_list_title
        except Exception as ex:
            print(ex)

    def get_first_default_text_line_below_selected_zone_list_title_by_xpath(self):
        try:
            first_default_text_line_below_selected_zone_list_title_by_xpath = self.config.get("Reporting", "first_default_text_line_below_selected_zone_list_title_by_xpath")
            print("first default horizontal line below selected zone list title: ", first_default_text_line_below_selected_zone_list_title_by_xpath)
            return first_default_text_line_below_selected_zone_list_title_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_first_default_text_line_below_selected_zone_list_title(self):
        try:
            expected_first_default_text_line_below_selected_zone_list_title = self.common_test_data_config.get("Reporting_Data", "expected_first_default_text_line_below_selected_zone_list_title")
            print("expected first default horizontal line below selected zone list title: ", expected_first_default_text_line_below_selected_zone_list_title)
            return expected_first_default_text_line_below_selected_zone_list_title
        except Exception as ex:
            print(ex)

    def get_second_default_text_line_below_selected_zone_list_title_by_xpath(self):
        try:
            second_default_text_line_below_selected_zone_list_title_by_xpath = self.config.get("Reporting", "second_default_text_line_below_selected_zone_list_title_by_xpath")
            print("second default horizontal line below selected zone list title: ", second_default_text_line_below_selected_zone_list_title_by_xpath)
            return second_default_text_line_below_selected_zone_list_title_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_second_default_text_line_below_selected_zone_list_title(self):
        try:
            expected_second_default_text_line_below_selected_zone_list_title = self.common_test_data_config.get("Reporting_Data", "expected_second_default_text_line_below_selected_zone_list_title")
            print("expected second default text line below selected zone list title: ", expected_second_default_text_line_below_selected_zone_list_title)
            return expected_second_default_text_line_below_selected_zone_list_title
        except Exception as ex:
            print(ex)

    def get_close_zone_menu_button_by_xpath(self):
        try:
            close_zone_menu_button_by_xpath = self.config.get("Reporting", "close_zone_menu_button_by_xpath")
            print("close zone menu button: ", close_zone_menu_button_by_xpath)
            return close_zone_menu_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_text_on_close_zone_menu_button_by_xpath(self):
        try:
            text_on_close_zone_menu_button_by_xpath = self.config.get("Reporting", "text_on_close_zone_menu_button_by_xpath")
            print("text on close zone menu button: ", text_on_close_zone_menu_button_by_xpath)
            return text_on_close_zone_menu_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_close_zone_menu_button(self):
        try:
            expected_text_on_close_zone_menu_button = self.common_test_data_config.get("Reporting_Data", "expected_text_on_close_zone_menu_button")
            print("expected text on close zone menu button: ", expected_text_on_close_zone_menu_button)
            return expected_text_on_close_zone_menu_button
        except Exception as ex:
            print(ex)

    def get_expected_report_field1_list_items(self):
        try:
            expected_report_field1_list_items = self.common_test_data_config.get("Reporting_Data", "expected_report_field1_list_items")
            print(f"report field1 items list: {expected_report_field1_list_items}")
            return expected_report_field1_list_items
        except Exception as ex:
            print(ex)

    def get_expected_report_field2_for_events_list_items(self):
        try:
            expected_report_field2_for_events_list_items = self.common_test_data_config.get("Reporting_Data", "expected_report_field2_for_events_list_items")
            print(f"report field2 for events item list: {expected_report_field2_for_events_list_items}")
            return expected_report_field2_for_events_list_items
        except Exception as ex:
            print(ex)

    def get_clear_all_button_on_selected_zone_by_xpath(self):
        try:
            clear_all_button_on_selected_zone_by_xpath = self.config.get("Reporting", "clear_all_button_on_selected_zone_by_xpath")
            print("clear all button: ", clear_all_button_on_selected_zone_by_xpath)
            return clear_all_button_on_selected_zone_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_clear_all_text(self):
        try:
            expected_clear_all_text = self.common_test_data_config.get("Reporting_Data", "expected_clear_all_text")
            print("expected clear all text: ", expected_clear_all_text)
            return expected_clear_all_text
        except Exception as ex:
            print(ex)

    def get_save_zone_selection_button_by_xpath(self):
        try:
            save_zone_selection_button_by_xpath = self.config.get("Reporting", "save_zone_selection_button_by_xpath")
            print("save zone selection button: ", save_zone_selection_button_by_xpath)
            return save_zone_selection_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_dot_circle_icon_on_save_zone_selection_button(self):
        try:
            dot_circle_icon_on_button = self.config.get("Reporting", "dot_circle_icon_on_button")
            print("dot circle icon on button: ", dot_circle_icon_on_button)
            return dot_circle_icon_on_button
        except Exception as ex:
            print(ex)

    def get_save_zone_selection_text_by_xpath(self):
        try:
            save_zone_selection_text_by_xpath = self.config.get("Reporting", "save_zone_selection_text_by_xpath")
            print("save zone selection text: ", save_zone_selection_text_by_xpath)
            return save_zone_selection_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_save_zone_selection_text(self):
        try:
            expected_save_zone_selection_text = self.common_test_data_config.get("Reporting_Data", "expected_save_zone_selection_text")
            print("expected save zone selection text: ", expected_save_zone_selection_text)
            return expected_save_zone_selection_text
        except Exception as ex:
            print(ex)

    def get_first_zone_in_search_zone_list_by_xpath(self):
        try:
            first_zone_in_search_zone_list_by_xpath = self.config.get("Reporting", "first_zone_in_search_zone_list_by_xpath")
            print("first zone in search zone list: ", first_zone_in_search_zone_list_by_xpath)
            return first_zone_in_search_zone_list_by_xpath
        except Exception as ex:
            print(ex)

    def get_first_zone_name_in_selected_zone_list_by_xpath(self):
        try:
            first_zone_name_in_selected_zone_list_by_xpath = self.config.get("Reporting", "first_zone_name_in_selected_zone_list_by_xpath")
            print("first name in selected zone list: ", first_zone_name_in_selected_zone_list_by_xpath)
            return first_zone_name_in_selected_zone_list_by_xpath
        except Exception as ex:
            print(ex)

    def get_view_and_edit_zones_button_by_xpath(self):
        try:
            view_and_edit_zones_button_by_xpath = self.config.get("Reporting", "view_&_edit_zones_button_by_xpath")
            print("view & edit zones button: ", view_and_edit_zones_button_by_xpath)
            return view_and_edit_zones_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_view_and_edit_zones_text_on_button_by_xpath(self):
        try:
            view_and_edit_zones_text_on_button_by_xpath = self.config.get("Reporting", "view_&_edit_zones_text_on_button_by_xpath")
            print("view and edit text on button: ", view_and_edit_zones_text_on_button_by_xpath)
            return view_and_edit_zones_text_on_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_view_and_edit_zones_text(self):
        try:
            expected_view_and_edit_zones_text = self.common_test_data_config.get("Reporting_Data", "expected_view_&_edit_zones_text")
            print("expected view & edit zones text: ", expected_view_and_edit_zones_text)
            return expected_view_and_edit_zones_text
        except Exception as ex:
            print(ex)

    def get_view_and_edit_groups_button_by_xpath(self):
        try:
            view_and_edit_groups_button_by_xpath = self.config.get("Reporting", "view_&_edit_groups_button_by_xpath")
            print("view and edit groups button: ", view_and_edit_groups_button_by_xpath)
            return view_and_edit_groups_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_view_and_edit_groups_text_on_button_by_xpath(self):
        try:
            view_and_edit_groups_text_on_button_by_xpath = self.config.get("Reporting", "view_&_edit_groups_text_on_button_by_xpath")
            print("view and edit groups text on button: ", view_and_edit_groups_text_on_button_by_xpath)
            return view_and_edit_groups_text_on_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_view_and_edit_groups_button(self):
        try:
            expected_view_and_edit_groups_text = self.common_test_data_config.get("Reporting_Data", "expected_view_&_edit_groups_text")
            print("expected text on view and edit groups button: ", expected_view_and_edit_groups_text)
            return expected_view_and_edit_groups_text
        except Exception as ex:
            print(ex)

    def get_new_reporting_panel_heading(self):
        try:
            new_reporting_panel_heading_for_visitors_by_hour_of_day = self.config.get("Reporting", "new_reporting_panel_heading_for_visitors_by_hour_of_day")
            print("new reporting panel heading: ", new_reporting_panel_heading_for_visitors_by_hour_of_day)
            return new_reporting_panel_heading_for_visitors_by_hour_of_day
        except Exception as ex:
            print(ex)

    def get_field2_dropdown_for_zones_by_xpath(self):
        try:
            field2_dropdown_for_zones_by_xpath = self.config.get("Reporting", "field2_dropdown_for_zones_by_xpath")
            print("field2 dropdown for zones: ", field2_dropdown_for_zones_by_xpath)
            return field2_dropdown_for_zones_by_xpath
        except Exception as ex:
            print(ex)

    def get_field2_dropdown_items_for_zones_by_xpath(self):
        try:
            field2_dropdown_items_for_zones_by_xpath = self.config.get("Reporting", "field2_dropdown_items_for_zones_by_xpath")
            print("field2 dropdown items for zones: ", field2_dropdown_items_for_zones_by_xpath)
            return field2_dropdown_items_for_zones_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_fourth_text_from_field1(self):
        try:
            expected_fourth_text_from_field1 = self.common_test_data_config.get("Reporting_Data", "expected_fourth_text_from_field1")
            print("expected fourth text from field1: ", expected_fourth_text_from_field1)
            return expected_fourth_text_from_field1
        except Exception as ex:
            print(ex)

    def get_expected_value_for_zones_by_enrollment_from_field2(self):
        try:
            expected_value_for_zones_by_enrollment_from_field2 = self.common_test_data_config.get("Reporting_Data", "expected_value_for_zones_by_enrollment_from_field2")
            print("expected value for zones by enrollment from field2: ", expected_value_for_zones_by_enrollment_from_field2)
            return expected_value_for_zones_by_enrollment_from_field2
        except Exception as ex:
            print(ex)

    def get_body_by_xpath(self):
        try:
            body_by_xpath = self.config.get("Reporting", "body_by_xpath")
            print("body: ", body_by_xpath)
            return body_by_xpath
        except Exception as ex:
            print(ex)

    def get_close_all_panels_button_on_dashboard_by_xpath(self):
        try:
            close_all_panels_button_on_dashboard_by_xpath = self.config.get("Reporting", "close_all_panels_button_on_dashboard_by_xpath")
            print("Close all panels button on dashboard: ", close_all_panels_button_on_dashboard_by_xpath)
            return close_all_panels_button_on_dashboard_by_xpath
        except Exception as ex:
            print(ex)


    def get_abe_enrollment_group(self):
        try:
            get_abe_enrollment_group = self.common_test_data_config.get("Notifier_Data", "abe_enrollment_group")
            print("get_abe_enrollment_group: ", get_abe_enrollment_group)
            return get_abe_enrollment_group
        except Exception as ex:
            print(ex)

    def get_vipe_enrollment_group(self):
        try:
            get_vipe_enrollment_group = self.common_test_data_config.get("Notifier_Data", "vipe_enrollment_group")
            print("get_vipe_enrollment_group: ", get_vipe_enrollment_group)
            return get_vipe_enrollment_group
        except Exception as ex:
            print(ex)

    def get_soe_enrollment_group(self):
        try:
            get_soe_enrollment_group = self.common_test_data_config.get("Notifier_Data", "soe_enrollment_group")
            print("get_soe_enrollment_group: ", get_soe_enrollment_group)
            return get_soe_enrollment_group
        except Exception as ex:
            print(ex)

    def get_pte_enrollment_group(self):
        try:
            get_pte_enrollment_group = self.common_test_data_config.get("Notifier_Data", "pte_enrollment_group")
            print("get_pte_enrollment_group: ", get_pte_enrollment_group)
            return get_pte_enrollment_group
        except Exception as ex:
            print(ex)

    def get_fraude_enrollment_group(self):
        try:
            get_fraude_enrollment_group = self.common_test_data_config.get("Notifier_Data", "fraude_enrollment_group")
            print("get_fraude_enrollment_group: ", get_fraude_enrollment_group)
            return get_fraude_enrollment_group
        except Exception as ex:
            print(ex)

    def get_camera0(self):
        try:
            get_camera0 = self.common_test_data_config.get("Notifier_Data", "camera0")
            print("get_camera0: ", get_camera0)
            return get_camera0
        except Exception as ex:
            print(ex)

    def get_camera1(self):
        try:
            get_camera1 = self.common_test_data_config.get("Notifier_Data", "camera1")
            print("get_camera1: ", get_camera1)
            return get_camera1
        except Exception as ex:
            print(ex)

    def get_zones(self):
        try:
            zones = self.common_test_data_config.get("Notifier_Data", "zones")
            print("zones: ", zones)
            return zones
        except Exception as ex:
            print(ex)