import configparser
from pathlib import Path

filepath = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\20_Insight_Dashboard_Module\\Data_From_INI\\Insight_Dashboard.ini"
print("configure filepath: ", filepath)
common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"


class insight_dashboard_read_ini:

    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            self.config.read(filepath)
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print(ex.args)

    def Insight_Dashboard_menu_by_xpath(self):
        try:
            Insight_Dashboard_menu_by_xpath = self.config.get("Insight_Dashboard_Locators", "Insight_Dashboard_menu_by_xpath")
            print("Insight_Dashboard_menu_by_xpath: ", Insight_Dashboard_menu_by_xpath)
            return Insight_Dashboard_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def overview_dashboard_label_by_xpath(self):
        try:
            overview_dashboard_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "overview_dashboard_label_by_xpath")
            print("overview_dashboard_label_by_xpath: ", overview_dashboard_label_by_xpath)
            return overview_dashboard_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def overview_dashboard_label_down_arrow_by_xpath(self):
        try:
            overview_dashboard_label_down_arrow_by_xpath = self.config.get("Insight_Dashboard_Locators", "overview_dashboard_label_down_arrow_by_xpath")
            print("overview_dashboard_label_by_xpath: ", overview_dashboard_label_down_arrow_by_xpath)
            return overview_dashboard_label_down_arrow_by_xpath
        except Exception as ex:
            print(ex.args)

    def total_loss_prevented_label_by_xpath(self):
        try:
            total_loss_prevented_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "total_loss_prevented_label_by_xpath")
            print("overview_dashboard_label_by_xpath: ", total_loss_prevented_label_by_xpath)
            return total_loss_prevented_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def total_loss_prevented_amount_by_xpath(self):
        try:
            total_loss_prevented_amount_by_xpath = self.config.get("Insight_Dashboard_Locators", "total_loss_prevented_amount_by_xpath")
            print("overview_dashboard_label_by_xpath: ", total_loss_prevented_amount_by_xpath)
            return total_loss_prevented_amount_by_xpath
        except Exception as ex:
            print(ex.args)

    def total_new_enrollments_label_by_xpath(self):
        try:
            total_new_enrollments_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "total_new_enrollments_label_by_xpath")
            print("overview_dashboard_label_by_xpath: ", total_new_enrollments_label_by_xpath)
            return total_new_enrollments_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def total_new_enrollments_count_by_xpath(self):
        try:
            total_new_enrollments_count_by_xpath = self.config.get("Insight_Dashboard_Locators", "total_new_enrollments_count_by_xpath")
            print("overview_dashboard_label_by_xpath: ", total_new_enrollments_count_by_xpath)
            return total_new_enrollments_count_by_xpath
        except Exception as ex:
            print(ex.args)

    def total_facefirst_enrollments_label_by_xpath(self):
        try:
            total_facefirst_enrollments_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "total_facefirst_enrollments_label_by_xpath")
            print("overview_dashboard_label_by_xpath: ", total_facefirst_enrollments_label_by_xpath)
            return total_facefirst_enrollments_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_filter_option_by_xpath(self):
        try:
            get_filter_option_by_xpath = self.config.get("Insight_Dashboard_Locators", "get_filter_option_by_xpath")
            print("overview_dashboard_label_by_xpath: ", get_filter_option_by_xpath)
            return get_filter_option_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_enabled_option_by_xpath(self):
        try:
            get_enabled_option_by_xpath = self.config.get("Insight_Dashboard_Locators", "get_enabled_option_by_xpath")
            print("overview_dashboard_label_by_xpath: ", get_enabled_option_by_xpath)
            return get_enabled_option_by_xpath
        except Exception as ex:
            print(ex.args)


    def total_facefirst_enrollments_count_by_xpath(self):
        try:
            total_facefirst_enrollments_count_by_xpath = self.config.get("Insight_Dashboard_Locators", "total_facefirst_enrollments_count_by_xpath")
            print("overview_dashboard_label_by_xpath: ", total_facefirst_enrollments_count_by_xpath)
            return total_facefirst_enrollments_count_by_xpath
        except Exception as ex:
            print(ex.args)

    def total_probable_match_events_label_by_xpath(self):
        try:
            total_probable_match_events_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "total_probable_match_events_count_by_xpath")
            print("overview_dashboard_label_by_xpath: ", total_probable_match_events_label_by_xpath)
            return total_probable_match_events_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def total_probable_match_events_count_by_xpath(self):
        try:
            total_probable_match_events_count_by_xpath = self.config.get("Insight_Dashboard_Locators", "total_probable_match_events_count_by_xpath")
            print("overview_dashboard_label_by_xpath: ", total_probable_match_events_count_by_xpath)
            return total_probable_match_events_count_by_xpath
        except Exception as ex:
            print(ex.args)

    def visitor_searches_label_by_xpath(self):
        try:
            visitor_searches_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "visitor_searches_label_by_xpath")
            print("overview_dashboard_label_by_xpath: ", visitor_searches_label_by_xpath)
            return visitor_searches_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def visitor_searches_count_by_xpath(self):
        try:
            visitor_searches_count_by_xpath = self.config.get("Insight_Dashboard_Locators", "visitor_searches_count_by_xpath")
            print("overview_dashboard_label_by_xpath: ", visitor_searches_count_by_xpath)
            return visitor_searches_count_by_xpath
        except Exception as ex:
            print(ex.args)

    def investigation_saving_time_label_by_xpath(self):
        try:
            investigation_saving_time_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "investigation_saving_time_label_by_xpath")
            print("overview_dashboard_label_by_xpath: ", investigation_saving_time_label_by_xpath)
            return investigation_saving_time_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def investigation_saving_time_count_by_xpath(self):
        try:
            investigation_saving_time_count_by_xpath = self.config.get("Insight_Dashboard_Locators", "investigation_saving_time_count_by_xpath")
            print("overview_dashboard_label_by_xpath: ", investigation_saving_time_count_by_xpath)
            return investigation_saving_time_count_by_xpath
        except Exception as ex:
            print(ex.args)

    def repeat_people_label_by_xpath(self):
        try:
            repeat_people_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "repeat_people_label_by_xpath")
            print("overview_dashboard_label_by_xpath: ", repeat_people_label_by_xpath)
            return repeat_people_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def repeat_people_count_by_xpath(self):
        try:
            repeat_people_count_by_xpath = self.config.get("Insight_Dashboard_Locators", "repeat_people_count_by_xpath")
            print("overview_dashboard_label_by_xpath: ", repeat_people_count_by_xpath)
            return repeat_people_count_by_xpath
        except Exception as ex:
            print(ex.args)

    def loss_prevented_by_enrollment_group_label_by_xpath(self):
        try:
            loss_prevented_by_enrollment_group_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "loss_prevented_by_enrollment_group_label_by_xpath")
            print("loss_prevented_by_enrollment_group_label_by_xpath: ", loss_prevented_by_enrollment_group_label_by_xpath)
            return loss_prevented_by_enrollment_group_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def loss_prevented_by_enrollment_group_chart_by_xpath(self):
        try:
            loss_prevented_by_enrollment_group_chart_by_xpath = self.config.get("Insight_Dashboard_Locators", "loss_prevented_by_enrollment_group_chart_by_xpath")
            print("loss_prevented_by_enrollment_group_label_by_xpath: ", loss_prevented_by_enrollment_group_chart_by_xpath)
            return loss_prevented_by_enrollment_group_chart_by_xpath
        except Exception as ex:
            print(ex.args)

    def possible_match_event_by_enrollment_action_label_by_xpath(self):
        try:
            possible_match_event_by_enrollment_action_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "possible_match_event_by_enrollment_action_label_by_xpath")
            print("possible_match_event_by_enrollment_action_label_by_xpath: ", possible_match_event_by_enrollment_action_label_by_xpath)
            return possible_match_event_by_enrollment_action_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def possible_match_event_by_enrollment_action_chart_by_xpath(self):
        try:
            possible_match_event_by_enrollment_action_chart_by_xpath = self.config.get("Insight_Dashboard_Locators", "possible_match_event_by_enrollment_action_chart_by_xpath")
            print("possible_match_event_by_enrollment_action_chart_by_xpath: ", possible_match_event_by_enrollment_action_chart_by_xpath)
            return possible_match_event_by_enrollment_action_chart_by_xpath
        except Exception as ex:
            print(ex.args)

    def enrollment_group_dropdown_by_xpath(self):
        try:
            enrollment_group_dropdown_by_xpath = self.config.get("Insight_Dashboard_Locators", "enrollment_group_dropdown_by_xpath")
            print("enrollment_group_dropdown_by_xpath: ", enrollment_group_dropdown_by_xpath)
            return enrollment_group_dropdown_by_xpath
        except Exception as ex:
            print(ex.args)

    def enrollment_group_list_by_xpath(self):
        try:
            enrollment_group_list_by_xpath = self.config.get("Insight_Dashboard_Locators", "enrollment_group_list_by_xpath")
            print("enrollment_group_list_by_xpath: ", enrollment_group_list_by_xpath)
            return enrollment_group_list_by_xpath
        except Exception as ex:
            print(ex.args)

    def dashboard_select_dropdown_by_xpath(self):
        try:
            dashboard_select_dropdown_by_xpath = self.config.get("Insight_Dashboard_Locators", "dashboard_select_dropdown_by_xpath")
            print("dashboard_select_dropdown_by_xpath: ", dashboard_select_dropdown_by_xpath)
            return dashboard_select_dropdown_by_xpath
        except Exception as ex:
            print(ex.args)

    def options_inside_dashboard_select_dropdown_by_xpath(self):
        try:
            options_inside_dashboard_select_dropdown_by_xpath = self.config.get("Insight_Dashboard_Locators", "options_inside_dashboard_select_dropdown_by_xpath")
            print("options_inside_dashboard_select_dropdown_by_xpath: ", options_inside_dashboard_select_dropdown_by_xpath)
            return options_inside_dashboard_select_dropdown_by_xpath
        except Exception as ex:
            print(ex.args)

    def Probable_Match_Events_by_Enrollment_Group_label_by_xpath(self):
        try:
            Probable_Match_Events_by_Enrollment_Group_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "Probable_Match_Events_by_Enrollment_Group_label_by_xpath")
            print("Probable_Match_Events_by_Enrollment_Group_label_by_xpath: ", Probable_Match_Events_by_Enrollment_Group_label_by_xpath)
            return Probable_Match_Events_by_Enrollment_Group_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def Probable_Match_Events_by_Enrollment_Group_chart_by_xpath(self):
        try:
            Probable_Match_Events_by_Enrollment_Group_chart_by_xpath = self.config.get("Insight_Dashboard_Locators", "Probable_Match_Events_by_Enrollment_Group_chart_by_xpath")
            print("Probable_Match_Events_by_Enrollment_Group_chart_by_xpath: ", Probable_Match_Events_by_Enrollment_Group_chart_by_xpath)
            return Probable_Match_Events_by_Enrollment_Group_chart_by_xpath
        except Exception as ex:
            print(ex.args)

    def Cumulative_Enrollments_by_Date_label_by_xpath(self):
        try:
            Cumulative_Enrollments_by_Date_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "Cumulative_Enrollments_by_Date_label_by_xpath")
            print("Cumulative_Enrollments_by_Date_label_by_xpath: ", Cumulative_Enrollments_by_Date_label_by_xpath)
            return Cumulative_Enrollments_by_Date_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def Cumulative_probable_match_events_by_date_label_by_xpath(self):
        try:
            Cumulative_probable_match_events_by_date_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "Cumulative_probable_match_events_by_date_label_by_xpath")
            print("Cumulative_probable_match_events_by_date_label_by_xpath: ", Cumulative_probable_match_events_by_date_label_by_xpath)
            return Cumulative_probable_match_events_by_date_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def Cumulative_probable_match_events_by_date_chart_by_xpath(self):
        try:
            Cumulative_probable_match_events_by_date_chart_by_xpath = self.config.get("Insight_Dashboard_Locators", "Cumulative_probable_match_events_by_date_chart_by_xpath")
            print("Cumulative_probable_match_events_by_date_chart_by_xpath: ", Cumulative_probable_match_events_by_date_chart_by_xpath)
            return Cumulative_probable_match_events_by_date_chart_by_xpath
        except Exception as ex:
            print(ex.args)

    def Tagged_vs_Untagged_Probable_Match_Events_label_bt_xpath(self):
        try:
            Tagged_vs_Untagged_Probable_Match_Events_label_bt_xpath = self.config.get("Insight_Dashboard_Locators", "Tagged_vs_Untagged_Probable_Match_Events_label_bt_xpath")
            print("Tagged_vs_Untagged_Probable_Match_Events_label_bt_xpath: ", Tagged_vs_Untagged_Probable_Match_Events_label_bt_xpath)
            return Tagged_vs_Untagged_Probable_Match_Events_label_bt_xpath
        except Exception as ex:
            print(ex.args)

    def Tagged_vs_Untagged_Probable_Match_Events_chart_bt_xpath(self):
        try:
            Tagged_vs_Untagged_Probable_Match_Events_chart_bt_xpath = self.config.get("Insight_Dashboard_Locators", "Tagged_vs_Untagged_Probable_Match_Events_chart_bt_xpath")
            print("Tagged_vs_Untagged_Probable_Match_Events_chart_bt_xpath: ", Tagged_vs_Untagged_Probable_Match_Events_chart_bt_xpath)
            return Tagged_vs_Untagged_Probable_Match_Events_chart_bt_xpath
        except Exception as ex:
            print(ex.args)

    def Tagged_Probable_Match_Events_by_Tag_Type_label_by_xpath(self):
        try:
            Tagged_Probable_Match_Events_by_Tag_Type_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "Tagged_Probable_Match_Events_by_Tag_Type_label_by_xpath")
            print("Tagged_Probable_Match_Events_by_Tag_Type_label_by_xpath: ", Tagged_Probable_Match_Events_by_Tag_Type_label_by_xpath)
            return Tagged_Probable_Match_Events_by_Tag_Type_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def Tagged_Probable_Match_Events_by_Tag_Type_chart_by_xpath(self):
        try:
            Tagged_Probable_Match_Events_by_Tag_Type_chart_by_xpath = self.config.get("Insight_Dashboard_Locators", "Tagged_Probable_Match_Events_by_Tag_Type_chart_by_xpath")
            print("Tagged_Probable_Match_Events_by_Tag_Type_chart_by_xpath: ", Tagged_Probable_Match_Events_by_Tag_Type_chart_by_xpath)
            return Tagged_Probable_Match_Events_by_Tag_Type_chart_by_xpath
        except Exception as ex:
            print(ex.args)

    def Deterred_Probable_Match_Events_label_by_xpath(self):
        try:
            Deterred_Probable_Match_Events_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "Deterred_Probable_Match_Events_label_by_xpath")
            print("Deterred_Probable_Match_Events_label_by_xpath: ", Deterred_Probable_Match_Events_label_by_xpath)
            return Deterred_Probable_Match_Events_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def Deterred_Probable_Match_Events_count_by_xpath(self):
        try:
            Deterred_Probable_Match_Events_count_by_xpath = self.config.get("Insight_Dashboard_Locators", "Deterred_Probable_Match_Events_count_by_xpath")
            print("Deterred_Probable_Match_Events_count_by_xpath: ", Deterred_Probable_Match_Events_count_by_xpath)
            return Deterred_Probable_Match_Events_count_by_xpath
        except Exception as ex:
            print(ex.args)

    def Total_Tagged_Probable_Match_Events_label_by_xpath(self):
        try:
            Total_Tagged_Probable_Match_Events_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "Total_Tagged_Probable_Match_Events_label_by_xpath")
            print("Total_Tagged_Probable_Match_Events_label_by_xpath: ", Total_Tagged_Probable_Match_Events_label_by_xpath)
            return Total_Tagged_Probable_Match_Events_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def Total_Tagged_Probable_Match_Events_count_by_xpath(self):
        try:
            Total_Tagged_Probable_Match_Events_count_by_xpath = self.config.get("Insight_Dashboard_Locators", "Total_Tagged_Probable_Match_Events_count_by_xpath")
            print("Total_Tagged_Probable_Match_Events_count_by_xpath: ", Total_Tagged_Probable_Match_Events_count_by_xpath)
            return Total_Tagged_Probable_Match_Events_count_by_xpath
        except Exception as ex:
            print(ex.args)

    def Serious_Offender_Tagged_Probable_Match_Events_label_by_xpath(self):
        try:
            Serious_Offender_Tagged_Probable_Match_Events_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "Serious_Offender_Tagged_Probable_Match_Events_label_by_xpath")
            print("Total_Tagged_Probable_Match_Events_count_by_xpath: ", Serious_Offender_Tagged_Probable_Match_Events_label_by_xpath)
            return Serious_Offender_Tagged_Probable_Match_Events_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def Serious_Offender_Tagged_Probable_Match_Events_count_by_xpath(self):
        try:
            Serious_Offender_Tagged_Probable_Match_Events_count_by_xpath = self.config.get("Insight_Dashboard_Locators", "Serious_Offender_Tagged_Probable_Match_Events_count_by_xpath")
            print("Serious_Offender_Tagged_Probable_Match_Events_count_by_xpath: ", Serious_Offender_Tagged_Probable_Match_Events_count_by_xpath)
            return Serious_Offender_Tagged_Probable_Match_Events_count_by_xpath
        except Exception as ex:
            print(ex.args)

    def Total_Probable_Match_Events_label_by_xpath_1(self):
        try:
            Total_Probable_Match_Events_label_by_xpath = self.config.get("Insight_Dashboard_Locators", "Total_Probable_Match_Events_label_by_xpath")
            print("Total_Probable_Match_Events_label_by_xpath: ", Total_Probable_Match_Events_label_by_xpath)
            return Total_Probable_Match_Events_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def Total_Probable_Match_Events_count_by_xpath_1(self):
        try:
            Total_Probable_Match_Events_count_by_xpath = self.config.get("Insight_Dashboard_Locators", "Total_Probable_Match_Events_count_by_xpath")
            print("Total_Probable_Match_Events_count_by_xpath: ", Total_Probable_Match_Events_count_by_xpath)
            return Total_Probable_Match_Events_count_by_xpath
        except Exception as ex:
            print(ex.args)

    def Cumulative_Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath(self):
        try:
            Cumulative_Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath = self.config.get("Insight_Dashboard_Locators", "Cumulative_Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath")
            print("Cumulative_Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath: ", Cumulative_Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath)
            return Cumulative_Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath
        except Exception as ex:
            print(ex.args)

    def Cumulative_Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath(self):
        try:
            Cumulative_Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath = self.config.get("Insight_Dashboard_Locators", "Cumulative_Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath")
            print("Cumulative_Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath: ", Cumulative_Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath)
            return Cumulative_Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath
        except Exception as ex:
            print(ex.args)

    def Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath(self):
        try:
            Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath = self.config.get("Insight_Dashboard_Locators", "Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath")
            print("Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath: ", Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath)
            return Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath
        except Exception as ex:
            print(ex.args)

    def Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath(self):
        try:
            Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath = self.config.get("Insight_Dashboard_Locators", "Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath")
            print("Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath: ", Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath)
            return Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath
        except Exception as ex:
            print(ex.args)

    def enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath(self):
        try:
            enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath = self.config.get("Insight_Dashboard_Locators", "enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath")
            print("enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath: ", enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath)
            return enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath
        except Exception as ex:
            print(ex.args)

    def enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath(self):
        try:
            enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath = self.config.get("Insight_Dashboard_Locators", "enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath")
            print("enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath: ", enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath)
            return enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath
        except Exception as ex:
            print(ex.args)

    def Enrollments_by_Week_label_on_enrollment_dashboard_by_xpath(self):
        try:
            Enrollments_by_Week_label_on_enrollment_dashboard_by_xpath = self.config.get("Insight_Dashboard_Locators", "Enrollments_by_Week_label_on_enrollment_dashboard_by_xpath")
            print("Enrollments_by_Week_label_on_enrollment_dashboard_by_xpath: ", Enrollments_by_Week_label_on_enrollment_dashboard_by_xpath)
            return Enrollments_by_Week_label_on_enrollment_dashboard_by_xpath
        except Exception as ex:
            print(ex.args)

    def Enrollments_by_Week_chart_on_enrollment_dashboard_by_xpath(self):
        try:
            Enrollments_by_Week_chart_on_enrollment_dashboard_by_xpath = self.config.get("Insight_Dashboard_Locators", "Enrollments_by_Week_chart_on_enrollment_dashboard_by_xpath")
            print("Enrollments_by_Week_chart_on_enrollment_dashboard_by_xpath: ", Enrollments_by_Week_chart_on_enrollment_dashboard_by_xpath)
            return Enrollments_by_Week_chart_on_enrollment_dashboard_by_xpath
        except Exception as ex:
            print(ex.args)

    def Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath(self):
        try:
            Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath = self.config.get("Insight_Dashboard_Locators", "Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath")
            print("Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath: ", Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath)
            return Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath
        except Exception as ex:
            print(ex.args)

    def Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath(self):
        try:
            Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath = self.config.get("Insight_Dashboard_Locators", "Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath")
            print("Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath: ", Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath)
            return Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath
        except Exception as ex:
            print(ex.args)

    def cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath_1(self):
        try:
            cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath = self.config.get("Insight_Dashboard_Locators", "cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath_1")
            print("cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath: ", cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath)
            return cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath
        except Exception as ex:
            print(ex.args)

    def cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath_1(self):
        try:
            cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath = self.config.get("Insight_Dashboard_Locators", "cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath_1")
            print("cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath: ", cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath)
            return cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath
        except Exception as ex:
            print(ex.args)

    # ************************************* test data read ini *****************************************

    def overview_dashboard_option_text(self):
        try:
            overview_dashboard_option_text = self.common_test_data_config.get("Insights_Dashboard_Data", "overview_dashboard_option_text")
            print("overview_dashboard_option_text: ", overview_dashboard_option_text)
            return overview_dashboard_option_text
        except Exception as ex:
            print(ex.args)

    def probable_match_events_dashboard_option_text(self):
        try:
            probable_match_events_dashboard_option_text = self.common_test_data_config.get("Insights_Dashboard_Data", "probable_match_events_dashboard_option_text")
            print("probable_match_events_dashboard_option_text: ", probable_match_events_dashboard_option_text)
            return probable_match_events_dashboard_option_text
        except Exception as ex:
            print(ex.args)

    def enrollments_dashboard_text(self):
        try:
            enrollments_dashboard_text = self.common_test_data_config.get("Insights_Dashboard_Data", "enrollments_dashboard_text")
            print("enrollments_dashboard_text: ", enrollments_dashboard_text)
            return enrollments_dashboard_text
        except Exception as ex:
            print(ex.args)

    def total_enrollments_count(self):
        try:
            total_enrollments_count = self.common_test_data_config.get("Insights_Dashboard_Data", "total_enrollments_count")
            print("total_enrollments_count: ", total_enrollments_count)
            return total_enrollments_count
        except Exception as ex:
            print(ex.args)

    def total_events_count(self):
        try:
            total_events_count = self.common_test_data_config.get("Insights_Dashboard_Data", "total_events_count")
            print("total_events_count: ", total_events_count)
            return total_events_count
        except Exception as ex:
            print(ex.args)

    def total_visitor_search_count(self):
        try:
            total_visitor_search_count = self.common_test_data_config.get("Insights_Dashboard_Data", "total_visitor_search_count")
            print("total_visitor_search_count: ", total_visitor_search_count)
            return total_visitor_search_count
        except Exception as ex:
            print(ex.args)


    def enrollments_menu_item_by_xpath(self):
        try:
            enrollments_menu_item_by_xpath = self.config.get("Insight_Dashboard_Locators", "enrollments_menu_item_by_xpath")
            print("enrollments_menu_item_by_xpath: ", enrollments_menu_item_by_xpath)
            return enrollments_menu_item_by_xpath
        except Exception as ex:
            print(ex.args)

    def total_enrollments_text_on_enrollments_panel_by_xpath(self):
        try:
            total_enrollments_text_on_enrollments_panel_by_xpath = self.config.get("Insight_Dashboard_Locators", "total_enrollments_text_on_enrollments_panel_by_xpath")
            print("total_enrollments_text_on_enrollments_panel_by_xpath: ", total_enrollments_text_on_enrollments_panel_by_xpath)
            return total_enrollments_text_on_enrollments_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def visitor_search_jobs_menu_item_by_xpath(self):
        try:
            visitor_search_jobs_menu_item_by_xpath = self.config.get("Insight_Dashboard_Locators", "visitor_search_jobs_menu_item_by_xpath")
            print("visitor_search_jobs_menu_item_by_xpath: ", visitor_search_jobs_menu_item_by_xpath)
            return visitor_search_jobs_menu_item_by_xpath
        except Exception as ex:
            print(ex.args)

    def search_dropdown_on_vsj_penal_by_xpath(self):
        try:
            search_dropdown_on_vsj_penal_by_xpath = self.config.get("Insight_Dashboard_Locators", "search_dropdown_on_vsj_penal_by_xpath")
            print("visitor_search_jobs_menu_item_by_xpath: ", search_dropdown_on_vsj_penal_by_xpath)
            return search_dropdown_on_vsj_penal_by_xpath
        except Exception as ex:
            print(ex.args)

    def search_btn_on_search_panel_by_xpath(self):
        try:
            search_btn_on_search_panel_by_xpath = self.config.get("Insight_Dashboard_Locators", "search_btn_on_search_panel_by_xpath")
            print("visitor_search_jobs_menu_item_by_xpath: ", search_btn_on_search_panel_by_xpath)
            return search_btn_on_search_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def select_all_users_option_by_xpath(self):
        try:
            select_all_users_option_by_xpath = self.config.get("Insight_Dashboard_Locators", "select_all_users_option_by_xpath")
            print("visitor_search_jobs_menu_item_by_xpath: ", select_all_users_option_by_xpath)
            return select_all_users_option_by_xpath
        except Exception as ex:
            print(ex.args)

    def visitor_search_count_text_on_vsj_panel(self):
        try:
            visitor_search_count_text_on_vsj_panel = self.config.get("Insight_Dashboard_Locators", "visitor_search_count_text_on_vsj_panel")
            print("visitor_search_count_text_on_vsj_panel: ", visitor_search_count_text_on_vsj_panel)
            return visitor_search_count_text_on_vsj_panel
        except Exception as ex:
            print(ex.args)

    def probable_match_events_menu_item_by_xpath(self):
        try:
            probable_match_events_menu_item_by_xpath = self.config.get("Insight_Dashboard_Locators", "probable_match_events_menu_item_by_xpath")
            print("visitor_search_count_text_on_vsj_panel: ", probable_match_events_menu_item_by_xpath)
            return probable_match_events_menu_item_by_xpath
        except Exception as ex:
            print(ex.args)

    def probable_match_events_text_on_events_panel_by_xpath(self):
        try:
            probable_match_events_text_on_events_panel_by_xpath = self.config.get("Insight_Dashboard_Locators", "probable_match_events_text_on_events_panel_by_xpath")
            print("probable_match_events_text_on_events_panel_by_xpath: ", probable_match_events_text_on_events_panel_by_xpath)
            return probable_match_events_text_on_events_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def cloud_menu_by_xpath(self):
        try:
            cloud_menu_by_xpath = self.config.get("Insight_Dashboard_Locators", "cloud_menu_by_xpath")
            print("cloud_menu_by_xpath: ", cloud_menu_by_xpath)
            return cloud_menu_by_xpath
        except Exception as ex:
            print(ex.args)



