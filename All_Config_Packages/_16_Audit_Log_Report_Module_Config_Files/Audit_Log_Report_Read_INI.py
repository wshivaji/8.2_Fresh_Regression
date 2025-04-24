import configparser
from pathlib import Path
from datetime import datetime as dt


class Audit_Log_Report_Components:
    def __init__(self):

        self.config = configparser.RawConfigParser()

        try:
            audit_log_report_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\16_Audit_Log_Report_Module\\Data_From_INI\\Audit_Log_Report.ini"
            self.config.read(audit_log_report_ini_file_path)
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def audit_log_report_menu_btn(self):
        try:
            ele = self.config.get('LOCATORS', 'audit_log_report_menu_btn')
            return ele
        except Exception as ex:
            print(ex)

    def audit_menu_text_validation(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'audit_menu_text_validation')
            return ele
        except Exception as ex:
            print(ex)

    def audit_log_report_icon(self):
        try:
            ele = self.config.get('LOCATORS', 'audit_log_report_icon')
            return ele
        except Exception as ex:
            print(ex)

    def enrollment_list_by_xpath(self):
        try:
            enrollment_list_by_xpath = self.config.get("LOCATORS", "enrollment_list_by_xpath")
            return enrollment_list_by_xpath
        except Exception as ex:
            print(ex)

    def select_report_criteria_text_xpath(self):
        try:
            ele = self.config.get('LOCATORS', 'select_report_criteria_text_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def report_type_select(self):
        try:
            ele = self.config.get('LOCATORS', 'report_type_select')
            return ele
        except Exception as ex:
            print(ex)

    def filter_by_select(self):
        try:
            ele = self.config.get('LOCATORS', 'filter_by_select')
            return ele
        except Exception as ex:
            print(ex)

    def report_type_text(self):
        try:
            ele = self.config.get('LOCATORS', 'report_type_text')
            return ele
        except Exception as ex:
            print(ex)

    def filter_by_text(self):
        try:
            ele = self.config.get('LOCATORS', 'filter_by_text')
            return ele
        except Exception as ex:
            print(ex)

    def users_text(self):
        try:
            ele = self.config.get('LOCATORS', 'users_text')
            return ele
        except Exception as ex:
            print(ex)

    def users_select(self):
        try:
            ele = self.config.get('LOCATORS', 'users_select')
            return ele
        except Exception as ex:
            print(ex)

    def select_user_after_one_selection(self):
        try:
            ele = self.config.get('LOCATORS', 'select_user_after_one_selection')
            return ele
        except Exception as ex:
            print(ex)

    def submit_report_button(self):
        try:
            ele = self.config.get('LOCATORS', 'submit_report_button')
            return ele
        except Exception as ex:
            print(ex)

    def report_type_text_validation(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'report_type_text_validation')
            return ele
        except Exception as ex:
            print(ex)

    def filter_by_text_validation(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'filter_by_text_validation')
            return ele
        except Exception as ex:
            print(ex)

    def users_text_validation(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'users_text_validation')
            return ele
        except Exception as ex:
            print(ex)

    def logout_btn_by_xpath(self):
        try:
            ele = self.config.get('LOCATORS', 'logout_btn_by_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def report_list_xpath(self):
        try:
            ele = self.config.get('LOCATORS', 'report_list_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def user_list_xpath(self):
        try:
            ele = self.config.get('LOCATORS', 'user_list_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def report_generated_validation(self):
        try:
            ele = self.config.get('LOCATORS', 'report_generated_validation')
            return ele
        except Exception as ex:
            print(ex)

    def report_option_1(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'report_option_1')
            return ele
        except Exception as ex:
            print(ex)

    def report_option_2(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'report_option_2')
            return ele
        except Exception as ex:
            print(ex)

    def report_option_3(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'report_option_3')
            return ele
        except Exception as ex:
            print(ex)

    def report_option_4(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'report_option_4')
            return ele
        except Exception as ex:
            print(ex)

    def report_option_5(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'report_option_5')
            return ele
        except Exception as ex:
            print(ex)

    def report_option_6(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'report_option_6')
            return ele
        except Exception as ex:
            print(ex)

    def filter_option_1(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'filter_option_1')
            return ele
        except Exception as ex:
            print(ex)

    def filter_option_2(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'filter_option_2')
            return ele
        except Exception as ex:
            print(ex)

    def filter_option_3(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'filter_option_3')
            return ele
        except Exception as ex:
            print(ex)

    def filter_option_4(self):
        try:
            ele = self.config.get('VALIDATION_DATA', 'filter_option_4')
            return ele
        except Exception as ex:
            print(ex)

    def filter_option_5(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'filter_option_5')
            return ele
        except Exception as ex:
            print(ex)

    def filter_option_6(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'filter_option_6')
            return ele
        except Exception as ex:
            print(ex)

    def filter_option_7(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'filter_option_7')
            return ele
        except Exception as ex:
            print(ex)

    def filter_option_8(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'filter_option_8')
            return ele
        except Exception as ex:
            print(ex)

    def get_select_report_type(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'select_report_type')
            return ele
        except Exception as ex:
            print(ex)

    def get_select_users(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'select_users')
            return ele
        except Exception as ex:
            print(ex)

    def get_select_filter_by(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'select_filter_by')
            return ele
        except Exception as ex:
            print(ex)

    def report_type_validation(self):
        try:
            ele = self.config.get('LOCATORS', 'report_type_validation')
            return ele
        except Exception as ex:
            print(ex)

    def filter_by_and_users_validation(self):
        try:
            ele = self.config.get('LOCATORS', 'filter_by_and_users_validation')
            return ele
        except Exception as ex:
            print(ex)

    def generated_report_page_select_dropdown(self):
        try:
            ele = self.config.get('LOCATORS', 'generated_report_page_select_dropdown')
            return ele
        except Exception as ex:
            print(ex)

    def user_name_list_report(self):
        try:
            ele = self.config.get('LOCATORS', 'user_name_list_report')
            return ele
        except Exception as ex:
            print(ex)

    def user_name_list_report_1(self):
        try:
            ele = self.config.get('LOCATORS', 'user_name_list_report_1')
            return ele
        except Exception as ex:
            print(ex)

    def next_btn_report(self):
        try:
            ele = self.config.get('LOCATORS', 'next_btn_report')
            return ele
        except Exception as ex:
            print(ex)

    def csv_button(self):
        try:
            ele = self.config.get('LOCATORS', 'csv_download_option')
            return ele
        except Exception as ex:
            print(ex)

    def user_enrollment_col_list(self):
        try:
            ele = self.config.get('LOCATORS', 'user_enrollments_report_display_col')
            return ele
        except Exception as ex:
            print(ex)

    def approver_enrollments_report_display_col(self):
        try:
            ele = self.config.get('LOCATORS', 'approver_enrollments_report_display_col')
            return ele
        except Exception as ex:
            print(ex)

    def total_pages_number(self):
        try:
            ele = self.config.get('LOCATORS', 'total_pages_number')
            return ele
        except Exception as ex:
            print(ex)

    def users_portal_menu(self):
        try:
            ele = self.config.get('LOCATORS', 'users_portal_menu')
            return ele
        except Exception as ex:
            print(ex)

    def user_name_list(self):
        try:
            ele = self.config.get('LOCATORS', 'user_name_list')
            return ele
        except Exception as ex:
            print(ex)

    def details_button_list(self):
        try:
            ele = self.config.get('LOCATORS', 'details_button_list')
            return ele
        except Exception as ex:
            print(ex)

    def user_role_hyperlink(self):
        try:
            ele = self.config.get('LOCATORS', 'user_role_hyperlink')
            return ele
        except Exception as ex:
            print(ex)

    def user_role_action_button(self):
        try:
            ele = self.config.get('LOCATORS', 'user_role_action_button')
            return ele
        except Exception as ex:
            print(ex)

    def edit_user_role_button(self):
        try:
            ele = self.config.get('LOCATORS', 'edit_user_role_button')
            return ele
        except Exception as ex:
            print(ex)

    def audit_log_user_role_checkbox(self):
        try:
            ele = self.config.get('LOCATORS', 'audi_log_user_role_checkbox')
            return ele
        except Exception as ex:
            print(ex)

    def enrollment_review_role_status(self):
        try:
            ele = self.config.get('LOCATORS', 'enrollment_review_role_status')
            return ele
        except Exception as ex:
            print(ex)

    def number_of_user_on_panel(self):
        try:
            ele = self.config.get('LOCATORS', 'number_of_user_on_panel')
            return ele
        except Exception as ex:
            print(ex)

    def load_more_button_users(self):
        try:
            ele = self.config.get('LOCATORS', 'load_more_button_users')
            return ele
        except Exception as ex:
            print(ex)

    def save_user_role_btn(self):
        try:
            ele = self.config.get('LOCATORS', 'save_user_role_btn')
            return ele
        except Exception as ex:
            print(ex)

    def user_name(self, user_name):
        try:
            ele = self.config.get('DYNAMIC_XPATH', 'user_name')
            return ele.format(user_name)
        except Exception as ex:
            print(ex)

    def user_name_data(self):
        try:
            ele = self.config.get('DYNAMIC_XPATH_DATA', 'user_name_data')
            return ele
        except Exception as ex:
            print(ex)

    def audit_report_delete_permission_uncheck(self):
        try:
            ele = self.config.get('LOCATORS', 'audit_report_delete_permission_uncheck')
            return ele
        except Exception as ex:
            print(ex)

    def report_data_rows_by_xpath(self):
        try:
            ele = self.config.get('LOCATORS', 'report_data_rows_by_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def user_name_text_list(self):
        try:
            ele = self.config.get('LOCATORS', 'user_name_text_list')
            return ele
        except Exception as ex:
            print(ex)

    def user_name_text(self, number):
        try:
            ele = self.config.get('DYNAMIC_XPATH', 'select_option')
            return ele.format(number)
        except Exception as ex:
            print(ex)

    def approved_datetime_list(self):
        try:
            ele = self.config.get('LOCATORS', 'approved_datetime_list')
            return ele
        except Exception as ex:
            print(ex)

    def enrollment_groups_user_name(self):
        try:
            ele = self.config.get('LOCATORS', 'enrollment_groups_user_name')
            return ele
        except Exception as ex:
            print(ex)

    def log_report_approved_enrollment_group(self):
        try:
            ele = self.config.get('LOCATORS', 'log_report_approved_enrollment_group')
            return ele
        except Exception as ex:
            print(ex)

    def reported_loss_list(self):
        try:
            ele = self.config.get('LOCATORS', 'reported_loss_list')
            return ele
        except Exception as ex:
            print(ex)

    def case_event_type_list_in_report(self):
        try:
            ele = self.config.get('LOCATORS', 'case_event_type_list_in_report')
            return ele
        except Exception as ex:
            print(ex)

    def approver_name_list_in_report(self):
        try:
            ele = self.config.get('LOCATORS', 'approver_name_list_in_report')
            return ele
        except Exception as ex:
            print(ex)

    def activity_type_list_in_report(self):
        try:
            ele = self.config.get('LOCATORS', 'activity_type_list_in_report')
            return ele
        except Exception as ex:
            print(ex)

    def report_generate_wait(self):
        try:
            ele = self.config.get('LOCATORS', 'report_generate_wait')
            return ele
        except Exception as ex:
            print(ex)

    def enrollment_status_list_in_report(self):
        try:
            ele = self.config.get('LOCATORS', 'enrollment_status_list_in_report')
            return ele
        except Exception as ex:
            print(ex)

    def user_enrollment_status_list(self):
        try:
            ele = self.config.get('LOCATORS', 'user_enrollment_status_list')
            return ele
        except Exception as ex:
            print(ex)

    #### new changes

    def identify_and_enroll_link_by_xpath(self):
        try:
            identify_and_enroll_link_by_xpath = self.config.get("LOCATORS", "identify_and_enroll_link_by_xpath")
            return identify_and_enroll_link_by_xpath
        except Exception as ex:
            print("identify_and_enroll_link_by_xpath : ", ex)

    def upload_image_by_xpath(self):
        try:
            upload_image_by_xpath = self.config.get("LOCATORS", "upload_image_by_xpath")
            return upload_image_by_xpath
        except Exception as ex:
            print("upload_image_by_xpath : ", ex)

    def identify_enroll_panel_identify_enroll_btn_by_xpath(self):
        try:
            identify_enroll_btn = self.config.get("LOCATORS", "identify_enroll_panel_identify_enroll_btn_by_xpath")
            return identify_enroll_btn
        except Exception as ex:
            print("identify_enroll_panel_identify_enroll_btn_by_xpath : ", ex)

    def identifying_photo_wait_by_xpath(self):
        try:
            identifying_photo_wait_by_xpath = self.config.get("LOCATORS", "identifying_photo_wait_by_xpath")
            return identifying_photo_wait_by_xpath
        except Exception as ex:
            print("identifying_photo_wait_by_xpath : ", ex)

    def enrollment_group_by_xpath(self):
        try:
            enrollment_group_by_xpath = self.config.get("LOCATORS", "enrollment_group_by_xpath")
            return enrollment_group_by_xpath
        except Exception as ex:
            print("enrollment_group_by_xpath : ", ex)

    def location_store_inpt_bx_by_xpath(self):
        try:
            location_store_inpt_bx_by_xpath = self.config.get("LOCATORS", "location_store_inpt_bx_by_xpath")
            return location_store_inpt_bx_by_xpath
        except Exception as ex:
            print("location_store_inpt_bx_by_xpath : ", ex)

    def location_store_data(self):
        try:
            location_store_data = self.common_test_data_config.get("common_data", "add_details_location_store_data_input")
            return location_store_data
        except Exception as ex:
            print("location_store_data : ", ex)

    def case_subject_inpt_bx_by_xpath(self):
        try:
            case_subject_inpt_bx_by_xpath = self.config.get("LOCATORS", "case_subject_inpt_bx_by_xpath")
            return case_subject_inpt_bx_by_xpath
        except Exception as ex:
            print("case_subject_inpt_bx_by_xpath : ", ex)

    def case_subject_data(self):
        try:
            case_subject_data = self.common_test_data_config.get("Enrollments_Data", "case_subject_data")
            return case_subject_data
        except Exception as ex:
            print("case_subject_data : ", ex)

    def reported_loss_inpt_bx_by_xpath(self):
        try:
            reported_loss_inpt_bx_by_xpath = self.config.get("LOCATORS", "reported_loss_inpt_bx_by_xpath")
            return reported_loss_inpt_bx_by_xpath
        except Exception as ex:
            print("reported_loss_inpt_bx_by_xpath : ", ex)

    def reported_loss_data(self):
        try:
            reported_loss_data = self.common_test_data_config.get("Enrollments_Data", "reported_loss_data")
            return reported_loss_data
        except Exception as ex:
            print("reported_loss_data : ", ex)

    def date_incident_inpt_bx_by_xpath(self):
        try:
            date_incident_inpt_bx_by_xpath = self.config.get("LOCATORS", "date_incident_inpt_bx_by_xpath")
            return date_incident_inpt_bx_by_xpath
        except Exception as ex:
            print("date_incident_inpt_bx_by_xpath : ", ex)

    def date_incident_data(self):
        try:
            date_incident_data = self.common_test_data_config.get("Enrollments_Data", "date_incident_data")
            day = date_incident_data[0:2]
            month = date_incident_data[3:5]
            year = date_incident_data[6:]
            print(f"day: {day}, month: {month}, year: {year}, type day: {type(day)}, month: {type(month)}, year: {type(year)}")
            day = int(day)
            month = int(month)
            year = int(year)
            datetime = dt.now()
            if day < 31:
                print("day is valid")
                if datetime.month == 2:
                    if month == datetime.month:
                        if day > 29:
                            day = datetime.day
                        else:
                            print(f" valid day: {day}")

            else:
                print(f"day: {datetime.day}")
                day = datetime.day

            if month > 12:
                print("invalid month provided")
            elif month > datetime.month:
                month = datetime.month
                print(f"month: {month}")
            else:
                month = datetime.month
                print(f"month: {month}")
            if year > datetime.year:
                print("invalid year provided")
            else:
                year = datetime.year
                print(f"year: {year}")
            if day < 10:
                day = "0" + str(day)
            if month < 10:
                month = "0" + str(month)
            print(
                f"day: {day}, month: {month}, year: {year}, type day: {type(day)}, month: {type(month)}, year: {type(year)}")
            date_incident_data = str(day) + "-" + str(month) + "-" + str(year)
            print(f"date incident: {date_incident_data}")
            return date_incident_data
        except Exception as ex:
            print("date_incident_data : ", ex)

    def action_inpt_bx_by_xpath(self):
        try:
            action_inpt_bx_by_xpath = self.config.get("LOCATORS", "action_inpt_bx_by_xpath")
            return action_inpt_bx_by_xpath
        except Exception as ex:
            print("action_inpt_bx_by_xpath : ", ex)

    def action_input_data(self):
        try:
            action_input_data = self.common_test_data_config.get("Enrollments_Data", "action_input_data")
            return action_input_data
        except Exception as ex:
            print("action_input_data : ", ex)

    def case_event_type_dropdown(self):
        try:
            ele = self.config.get("LOCATORS", "case_event_type_dropdown")
            return ele
        except Exception as ex:
            print("case_event_type_dropdown : ", ex)

    def activity_type_dropdown(self):
        try:
            ele = self.config.get("LOCATORS", "activity_type_dropdown")
            return ele
        except Exception as ex:
            print("activity_type_dropdown : ", ex)

    def method_of_offence_by_xpath(self):
        try:
            method_of_offence_by_xpath = self.config.get("LOCATORS", "method_of_offence_by_xpath")
            return method_of_offence_by_xpath
        except Exception as ex:
            print("method_of_offence_by_xpath : ", ex)

    def gender_dropdown(self):
        try:
            ele = self.config.get("LOCATORS", "gender_dropdown")
            return ele
        except Exception as ex:
            print("gender_dropdown : ", ex)

    def height_type_dropdown(self):
        try:
            ele = self.config.get("LOCATORS", "height_type_dropdown")
            return ele
        except Exception as ex:
            print("height_type_dropdown : ", ex)

    def reported_by_input(self):
        try:
            ele = self.config.get("LOCATORS", "reported_by_input")
            return ele
        except Exception as ex:
            print("reported_by_input : ", ex)

    def reported_by_data(self):
        try:
            reported_by_data = self.common_test_data_config\
                .get("common_data", "reported_by_data")
            return reported_by_data
        except Exception as ex:
            print("reported_by_data : ", ex)

    def build_input(self):
        try:
            ele = self.config.get("LOCATORS", "build_input")
            return ele
        except Exception as ex:
            print("build_input : ", ex)

    def build_data(self):
        try:
            build_data = self.common_test_data_config.get("common_data", "build_data")
            return build_data
        except Exception as ex:
            print("build_data : ", ex)

    def body_markings_input(self):
        try:
            ele = self.config.get("LOCATORS", "body_markings_input")
            return ele
        except Exception as ex:
            print("body_markings_input : ", ex)

    def body_markings_data(self):
        try:
            body_markings_data = self.common_test_data_config.get("common_data", "body_markings_data")
            return body_markings_data
        except Exception as ex:
            print("body_markings_data : ", ex)

    def narrative_Desc_input(self):
        try:
            ele = self.config.get("LOCATORS", "narrative_Desc_input")
            return ele
        except Exception as ex:
            print("narrative_Desc_input : ", ex)

    def narratives_data(self):
        try:
            narratives_data = self.common_test_data_config.get("common_data", "narratives_data")
            return narratives_data
        except Exception as ex:
            print("narratives_data : ", ex)

    def add_details_save_btn_by_xpath(self):
        try:
            add_details_save_btn_by_xpath = self.config.get("LOCATORS", "add_details_save_btn_by_xpath")
            return add_details_save_btn_by_xpath
        except Exception as ex:
            print("add_details_save_btn_by_xpath : ", ex)

    def enrollment_success_loader(self):
        try:
            enrollment_success_loader = self.config.get("LOCATORS", "enrollment_success_loader")
            return enrollment_success_loader
        except Exception as ex:
            print("enrollment_success_loader : ", ex)

    def enrollment_success_msg_xpath(self):
        try:
            enrollment_success_msg_xpath = self.config.get("LOCATORS", "enrollment_success_msg_xpath")
            return enrollment_success_msg_xpath
        except Exception as ex:
            print("enrollment_success_msg_xpath : ", ex)

    def add_details_submit_for_review_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "add_details_submit_for_review_btn_by_xpath")
            return ele
        except Exception as ex:
            print("add_details_submit_for_review_btn_by_xpath : ", ex)

    def enrollments_portal_menu(self):
        try:
            ele = self.config.get("LOCATORS", "enrollments_portal_menu")
            return ele
        except Exception as ex:
            print("enrollments_portal_menu : ", ex)

    def filter_btn(self):
        try:
            ele = self.config.get("LOCATORS", "filter_btn")
            return ele
        except Exception as ex:
            print("filter_btn : ", ex)

    def pending_for_review(self):
        try:
            ele = self.config.get("LOCATORS", "pending_for_review")
            return ele
        except Exception as ex:
            print("pending_for_review : ", ex)

    def disable_filter_btn(self):
        try:
            ele = self.config.get("LOCATORS", "disable_filter_btn")
            return ele
        except Exception as ex:
            print("disable_filter_btn : ", ex)

    def select_first_pending_enrollment(self):
        try:
            ele = self.config.get("LOCATORS", "select_first_pending_enrollment")
            return ele
        except Exception as ex:
            print("select_first_pending_enrollment : ", ex)

    def action_button(self):
        try:
            ele = self.config.get("LOCATORS", "action_button")
            return ele
        except Exception as ex:
            print("action_button : ", ex)

    def approve_selected_enrollment(self):
        try:
            ele = self.config.get("LOCATORS", "approve_selected_enrollment")
            return ele
        except Exception as ex:
            print("approve_selected_enrollment : ", ex)

    def enable_selected_enrollment(self):
        try:
            ele = self.config.get("LOCATORS", "enable_selected_enrollment")
            return ele
        except Exception as ex:
            print("enable_selected_enrollment : ", ex)

    def enrollment_group_list(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_group_list")
            return ele
        except Exception as ex:
            print("enrollment_group_list : ", ex)

    def enrollment_group_menu(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_group_menu")
            return ele
        except Exception as ex:
            print("enrollment_group_menu : ", ex)

    def user_enrollment_enrollment_group_list_in_report(self):
        try:
            ele = self.config.get("LOCATORS", "user_enrollment_enrollment_group_list_in_report")
            return ele
        except Exception as ex:
            print("user_enrollment_enrollment_group_list_in_report : ", ex)

    def user_enrollment_enrolled_datetime_list_in_report(self):
        try:
            ele = self.config.get("LOCATORS", "user_enrollment_enrolled_datetime_list_in_report")
            return ele
        except Exception as ex:
            print("user_enrollment_enrolled_datetime_list_in_report : ", ex)

    def user_enrollment_location_store_list_in_report(self):
        try:
            ele = self.config.get("LOCATORS", "user_enrollment_location_store_list_in_report")
            return ele
        except Exception as ex:
            print("user_enrollment_location_store_list_in_report : ", ex)

    def user_enrollment_approve_by_list_in_report(self):
        try:
            ele = self.config.get("LOCATORS", "user_enrollment_approve_by_list_in_report")
            return ele
        except Exception as ex:
            print("user_enrollment_approve_by_list_in_report : ", ex)

    def user_enrollment_status_list_in_report(self):
        try:
            ele = self.config.get("LOCATORS", "user_enrollment_status_list_in_report")
            return ele
        except Exception as ex:
            print("user_enrollment_status_list_in_report : ", ex)

    def user_enrollment_date_list_in_report(self):
        try:
            ele = self.config.get("LOCATORS", "user_enrollment_date_list_in_report")
            return ele
        except Exception as ex:
            print("user_enrollment_date_list_in_report : ", ex)

    def login_logout_report_column_list(self):
        try:
            ele = self.config.get("LOCATORS", "login_logout_report_column_list")
            return ele
        except Exception as ex:
            print("login_logout_report_column_list : ", ex)

    def login_logout_date_column_list(self):
        try:
            ele = self.config.get("LOCATORS", "login_logout_date_column_list")
            return ele
        except Exception as ex:
            print("login_logout_date_column_list : ", ex)

    def login_logout_time_column_list(self):
        try:
            ele = self.config.get("LOCATORS", "login_logout_time_column_list")
            return ele
        except Exception as ex:
            print("login_logout_time_column_list : ", ex)

    def login_logout_total_count_list(self):
        try:
            ele = self.config.get("LOCATORS", "login_logout_total_count_list")
            return ele
        except Exception as ex:
            print("login_logout_total_count_list : ", ex)

    def login_logout_ip_address_list(self):
        try:
            ele = self.config.get("LOCATORS", "login_logout_ip_address_list")
            return ele
        except Exception as ex:
            print("login_logout_ip_address_list : ", ex)

    def threshold_change_report_column_list(self):
        try:
            ele = self.config.get("LOCATORS", "threshold_change_report_column_list")
            return ele
        except Exception as ex:
            print("threshold_change_report_column_list : ", ex)

    def user_threshold_change_enrollment_group_list_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "user_threshold_change_enrollment_group_list_by_xpath")
            return ele
        except Exception as ex:
            print("user_threshold_change_enrollment_group_list_by_xpath : ", ex)

    def threshold_change_changed_date_colum_list(self):
        try:
            ele = self.config.get("LOCATORS", "threshold_change_changed_date_colum_list")
            return ele
        except Exception as ex:
            print("threshold_change_changed_date_colum_list : ", ex)

    def threshold_change_changed_time_column_list(self):
        try:
            ele = self.config.get("LOCATORS", "threshold_change_changed_time_column_list")
            return ele
        except Exception as ex:
            print("threshold_change_changed_time_column_list : ", ex)

    def enrollment_groups_action_drop_down(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_groups_action_drop_down")
            return ele
        except Exception as ex:
            print("enrollment_groups_action_drop_down : ", ex)

    def create_enrollment_group_option(self):
        try:
            ele = self.config.get("LOCATORS", "create_enrollment_group_option")
            return ele
        except Exception as ex:
            print("create_enrollment_group_option : ", ex)

    def enrollment_groups_details_name_input_bx(self):
        try:
            ele = self.config.get("LOCATORS", "enrollment_groups_details_name_input_bx")
            return ele
        except Exception as ex:
            print("enrollment_groups_details_name_input_bx : ", ex)

    def extend_menu(self, name):
        try:
            ele = self.config.get('DYNAMIC_XPATH', 'extend_menu')
            return ele.format(name)
        except Exception as ex:
            print(ex)

    def details_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "details_by_xpath")
            return ele
        except Exception as ex:
            print("details_by_xpath : ", ex)

    def face_threshold_input_bx(self):
        try:
            ele = self.config.get("LOCATORS", "face_threshold_input_bx")
            return ele
        except Exception as ex:
            print("face_threshold_input_bx : ", ex)

    def save_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "save_btn_by_xpath")
            return ele
        except Exception as ex:
            print("save_btn_by_xpath : ", ex)

    def details_action_drop_down(self):
        try:
            ele = self.config.get("LOCATORS", "details_action_drop_down")
            return ele
        except Exception as ex:
            print("details_action_drop_down : ", ex)

    def edit_option(self):
        try:
            ele = self.config.get("LOCATORS", "edit_option")
            return ele
        except Exception as ex:
            print("edit_option : ", ex)

    def threshold_change_column_list(self):
        try:
            ele = self.config.get("LOCATORS", "threshold_change_column_list")
            return ele
        except Exception as ex:
            print("threshold_change_column_list : ", ex)

    def threshold_change_report_data(self, name):
        try:
            ele = self.config.get('DYNAMIC_XPATH', 'threshold_change_report_data')
            return ele.format(name)
        except Exception as ex:
            print(ex)

    def threshold_change_ip_address_list(self):
        try:
            ele = self.config.get("LOCATORS", "threshold_change_ip_address_list")
            return ele
        except Exception as ex:
            print("threshold_change_ip_address_list : ", ex)

    def masked_face_threshold_input_bx(self):
        try:
            ele = self.config.get("LOCATORS", "masked_face_threshold_input_bx")
            return ele
        except Exception as ex:
            print("masked_face_threshold_input_bx : ", ex)

    def threshold_change_threshold_type_column_list(self):
        try:
            ele = self.config.get("LOCATORS", "threshold_change_threshold_type_column_list")
            return ele
        except Exception as ex:
            print("threshold_change_threshold_type_column_list : ", ex)

    def threshold_change_threshold_type(self, name):
        try:
            ele = self.config.get('DYNAMIC_XPATH', 'threshold_change_threshold_type')
            return ele.format(name)
        except Exception as ex:
            print(ex)

    def threshold_change_change_result(self, name):
        try:
            ele = self.config.get('DYNAMIC_XPATH', 'threshold_change_change_result')
            return ele.format(name)
        except Exception as ex:
            print(ex)

    def serious_offender_drop_down(self):
        try:
            ele = self.config.get("LOCATORS", "serious_offender_drop_down")
            return ele
        except Exception as ex:
            print("serious_offender_drop_down : ", ex)

    def threshold_change_serious_offender(self, name):
        try:
            ele = self.config.get('DYNAMIC_XPATH', 'threshold_change_serious_offender')
            return ele.format(name)
        except Exception as ex:
            print(ex)

    def threshold_change_changed_date(self):
        try:
            ele = self.config.get("LOCATORS", "threshold_change_changed_date")
            return ele
        except Exception as ex:
            print("threshold_change_changed_date : ", ex)

    def threshold_change_user_name(self):
        try:
            ele = self.config.get("LOCATORS", "threshold_change_user_name")
            return ele
        except Exception as ex:
            print("threshold_change_user_name : ", ex)

    def close_all_panel_one_by_one(self):
        try:
            ele = self.config.get("LOCATORS", "close_panel_one_by_one_list")
            return ele
        except Exception as ex:
            print("close_all_panel_one_by_one : ", ex)

    def report_type_User_Enrollments(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'report_type_User_Enrollments')
            return ele
        except Exception as ex:
            print(ex)

    def select_core_user(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'select_core_user')
            return ele
        except Exception as ex:
            print(ex)

    def report_type_Approver_Enrollments(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'report_type_Approver_Enrollments')
            return ele
        except Exception as ex:
            print(ex)

    def report_type_Log_in_Log_out(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'report_type_Log_in_Log_out')
            return ele
        except Exception as ex:
            print(ex)

    def report_type_Threshold_changes(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'report_type_Threshold_changes')
            return ele
        except Exception as ex:
            print(ex)

    def select_All_users(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'select_All_users')
            return ele
        except Exception as ex:
            print(ex)

    def last_7_days_select(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'last_7_days_select')
            return ele
        except Exception as ex:
            print(ex)

    def last_14_days_select(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'last_14_days_select')
            return ele
        except Exception as ex:
            print(ex)

    def select_Month_to_date(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'select_Month_to_date')
            return ele
        except Exception as ex:
            print(ex)

    def select_Year_to_date(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'select_Year_to_date')
            return ele
        except Exception as ex:
            print(ex)

    def select_users(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'select_users')
            return ele
        except Exception as ex:
            print(ex)

    def select_core_users(self):
        try:
            ele = self.common_test_data_config.get('Login_Logout_Data', 'username')
            return ele
        except Exception as ex:
            print(ex)

    def select_one_user(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'select_one_user')
            return ele
        except Exception as ex:
            print(ex)

    def select_quater_to_date(self):
        try:
            ele = self.common_test_data_config.get('Audit_Log_Report_Data', 'select_quater_to_date')
            return ele
        except Exception as ex:
            print(ex)

    def audi_log_user_role_change(self):
        try:
            ele = self.config.get('LOCATORS', 'audi_log_user_role_change')
            return ele
        except Exception as ex:
            print(ex)

    def create_audit_log_role_checkbox(self):
        try:
            ele = self.config.get('LOCATORS', 'create_audit_log_role_checkbox')
            return ele
        except Exception as ex:
            print(ex)

    def read_audit_log_role_checkbox(self):
        try:
            ele = self.config.get('LOCATORS', 'read_audit_log_role_checkbox')
            return ele
        except Exception as ex:
            print(ex)

    def edite_audit_log_role_checkbox(self):
        try:
            ele = self.config.get('LOCATORS', 'edite_audit_log_role_checkbox')
            return ele
        except Exception as ex:
            print(ex)

    def close_all_panel_list(self):
        try:
            ele = self.config.get('LOCATORS', 'close_all_panel_list')
            return ele
        except Exception as ex:
            print(ex)

    def user_close_panel_and_discard_Changes(self):
        try:
            ele = self.config.get('LOCATORS', 'user_close_panel_and_discard_Changes')
            return ele
        except Exception as ex:
            print(ex)

    def face_first_logo(self):
        try:
            ele = self.config.get('LOCATORS', 'face_first_logo')
            return ele
        except Exception as ex:
            print(ex)

    def select_user_input_box(self):
        try:
            ele = self.config.get('LOCATORS', 'select_user_input_box')
            return ele
        except Exception as ex:
            print(ex)

    def get_loginButton(self):
        try:
            login_btn = self.config.get('LOCATORS', 'portal_login_page_loginBtn_by_xpath')
            # Base_Class.logger.info("URL read successfully : ", url)
            return login_btn
        except Exception as ex:
            print(ex)

    def portal_menu_enrollments_groups_btn_by_xpath(self):
        try:
            enrollments_groups_btn_by_xpath = self.config.get("LOCATORS", "enrollment_groups_btn_by_xpath")
            return enrollments_groups_btn_by_xpath
        except Exception as ex:
            print("portal_menu_enrollments_groups_btn_by_xpath : ", ex)

    def there_is_no_record_msg_by_xpath(self):
        there_is_no_record_msg_by_xpath = self.config.get("LOCATORS", "there_is_no_record_msg_by_xpath")
        return there_is_no_record_msg_by_xpath

    def there_is_no_record_msg(self):
        there_is_no_record_msg = self.common_test_data_config.get("Audit_Log_Report_Data", "there_is_no_record_msg")
        return there_is_no_record_msg

    def enrollment_basis_by_xpath(self):
        try:
            enrollment_basis_by_xpath = self.config.get("LOCATORS", "enrollment_basis_by_xpath")
            return enrollment_basis_by_xpath
        except Exception as ex:
            print("enrollment_basis_by_xpath : ", ex)

    # def date_incident_data(self):
    #     try:
    #         date_incident_data = self.common_test_data_config.get("Audit_Log_Report_Data", "date_incident_data")
    #         return date_incident_data
    #     except Exception as ex:
    #         print("date_incident_data : ", ex)

    def date_incident_time(self):
        try:
            datetime = dt.now()
            date_incident_time_am_pm = self.common_test_data_config.get("Audit_Log_Report_Data", "date_incident_time")
            hr = date_incident_time_am_pm[:2]
            min = date_incident_time_am_pm[2:4]
            print(f"hr: {hr}, min: {min}")
            hr = int(hr)
            min = int(min)
            if hr > 12:
                if datetime.hour < 10:
                    hr = datetime.hour
                    hr = "0" + str(hr)
                else:
                    hr = datetime.hour
                    hr = str(hr)
            elif 12 > hr > 10:
                hr = str(hr)
            else:
                hr = "0" + str(hr)
            if min > 59:
                if datetime.hour < 10:
                    min = "0" + str(datetime.hour)
                else:
                    min = str(datetime.hour)
            elif 59 > min > 10:
                min = str(min)
            else:
                min = "0" + str(min)
            date_incident_time_am_pm = hr + ":" + min
            print(f"time sending: {date_incident_time_am_pm}")
            return date_incident_time_am_pm
        except Exception as ex:
            print(ex.args)

    def date_incident_am_pm(self):
        try:
            date_incident_am_pm = self.common_test_data_config.get("Audit_Log_Report_Data", "date_incident_am_pm")
            return date_incident_am_pm
        except Exception as ex:
            print(ex.args)

    def edge_name_list(self):
        try:
            edge_name_list = self.config.get("LOCATORS", "edge_name_list")
            return edge_name_list
        except Exception as ex:
            print(ex.args)

    def edge_name(self):
        try:
            edge_name = self.common_test_data_config.get("Audit_Log_Report_Data", "edge_name")
            return edge_name
        except Exception as ex:
            print(ex.args)

    def region_btn_by_xpath(self):
        try:
            region_btn_by_xpath = self.config.get("LOCATORS", "region_btn_by_xpath")
            return region_btn_by_xpath
        except Exception as ex:
            print(ex.args)

    def description_textbox_on_user_role_details_panel_by_xpath(self):
        description_textbox_on_user_role_details_panel_by_xpath = self.config.get("LOCATORS", "description_textbox_on_user_role_details_panel_by_xpath")
        return description_textbox_on_user_role_details_panel_by_xpath

    def user_roles_details_description(self):
        user_roles_details_description = self.common_test_data_config.get("Audit_Log_Report_Data", "user_roles_details_description")
        return user_roles_details_description
# print(Audit_Log_Report_Components().face_first_logo())

    def get_user_first_name(self):
        try:
            get_user_first_name = self.config.get("LOCATORS", "user_first_name_xpath")
            return get_user_first_name
        except Exception as ex:
            print(ex.args)

    def get_user_last_name(self):
        try:
            get_user_last_name = self.config.get("LOCATORS", "user_last_name_xpath")
            return get_user_last_name
        except Exception as ex:
            print(ex.args)

    def user_profile_xpath(self):
        try:
            get_user_last_name = self.config.get("LOCATORS", "user_profile_xpath")
            return get_user_last_name
        except Exception as ex:
            print(ex.args)

