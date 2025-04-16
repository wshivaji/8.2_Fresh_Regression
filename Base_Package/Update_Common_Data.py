import configparser
from pathlib import Path


class update_common_data:

    def __init__(self):

        self.login_logout_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\0_Login_Logout_Data\\Data_From_INI\\login_logout.ini"
        print(f"login_logout file path: {self.login_logout_ini_file_path}")
        self.portal_login_module_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\1_Portal_Login_Module\\Data_From_INI\\Portal_Login_module.ini"
        self.portal_login_page_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\1_Portal_Login_Module\\Data_From_INI\\Portal_Login_Page.ini"
        self.portal_menu_module_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\2_Portal_Menu_Module\\Data_From_INI\\Portal_Menu_Module.ini"
        self.user_roles_module_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\3_User_Roles_Module\\Data_From_INI\\User_Roles.ini"
        self.user_roles_functional_module_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\3_User_Roles_Module\\Data_From_INI\\User_Roles_Test_Cases_Functional.ini"
        self.users_module_module_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\4_Users_Module\\Data_From_INI\\Users.ini"
        self.enrollment_groups_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\5_Enrollment_Groups_Module\\Data_From_INI\\Enrollment_Groups.ini"
        self.notes_module_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\6_Notes_Module\\Data_From_INI\\Notes_module.ini"
        self.notes_search_filter_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\6_Notes_search_filter_Module\\Data_From_INI\\Notes_Search_Filter_Combination.ini"
        self.notification_groups_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\6_Notification_Groups\\Data_From_INI\\Notification_Groups.ini"
        self.visitor_search_module_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\7_Visitor_Search_Module\\Data_From_INI\\Visitor_Search.ini"
        self.detect_faces_module_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\8_Detect_Faces_Module\\Data_From_INI\\Detect_Faces_module.ini"
        self.visitor_search_job_module_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\8_Visitor_Search_Jobs_Module\\Data_From_INI\\Visitor_Search_Jobs.ini"
        self.tags_module_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\9_tags_module\\Data_From_INI\\Tags.ini"
        self.accounts_module_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\10_Account_Module\\Data_From_INI\\Account_Module.ini"
        self.enrollment_module_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\11_Enrollment_Module\\Data_From_INI\\Enrollments.ini"
        self.identify_and_enroll_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\12_Identify_and_Enroll_Module\\Data_From_INI\\Identify_and_Enroll.ini"
        self.audit_log_report_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\16_Audit_Log_Report_Module\\Data_From_INI\\Audit_Log_Report.ini"
        self.notifier_module_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\17_Notifier_Module\\Data_From_INI\\Notifier.ini"
        self.reporting_module_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\18_Reporting_Module\\Data_From_INI\\Reporting.ini"
        self.system_level_test_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\System_Level_Test\\Data_From_INI\\system_level_test.ini"

        self.common_test_data_ini_file_path = f"{Path(__file__).parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
        self.common_test_data_config = configparser.RawConfigParser()
        self.common_test_data_config.read(self.common_test_data_ini_file_path)
        # print(self.common_test_data_config.get("Login_Logout_Data", "cloud_login_url"))

        self.login_logout_ini_file_path_config = configparser.RawConfigParser()
        self.login_logout_ini_file_path_config.read(self.login_logout_ini_file_path)
        print(self.login_logout_ini_file_path_config.get("login_urls", "cloud_login_url"))

        cloud_login_url = self.common_test_data_config.get("Login_Logout_Data", "cloud_login_url")
        username = self.common_test_data_config.get("Login_Logout_Data", "username")
        password = self.common_test_data_config.get("Login_Logout_Data", "password")
        logout_on_each_test = self.common_test_data_config.get("Login_Logout_Data", "logout_on_each_test")

        webapi_version_number = self.common_test_data_config.get("Portal_Login_Page_Data", "webapi_version_number")
        portal_version_number = self.common_test_data_config.get("Portal_Login_Page_Data", "portal_version_number")


        new_password = self.common_test_data_config.get("Portal_Menu_Module_Data", "new_password")
        expected_events_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_events_text")
        expected_tags_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_tags_text")
        expected_identify_enroll_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_identify_enroll_text")
        expected_detect_faces_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_detect_faces_text")
        expected_enrollments_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_enrollments_text")
        expected_enrollment_groups_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_enrollment_groups_text")
        expected_notification_groups_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_notification_groups_text")
        expected_visitor_search_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_visitor_search_text")
        expected_visitor_search_jobs_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_visitor_search_jobs_text")
        expected_notes_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_notes_text")
        expected_locations_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_notes_text")
        expected_users_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_users_text")
        expected_user_roles_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_user_roles_text")
        expected_zones_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_zones_text")
        expected_account_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_account_text")
        expected_reporting_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_reporting_text")
        expected_dashboard_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_dashboard_text")
        expected_fidusvision_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_fidusvision_text")
        expected_notifier_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_notifier_text")
        expected_audit_log_report_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_audit_log_report_text")
        expected_close_all_panels_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_close_all_panels_text")
        expected_face_first_copyright = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_face_first_copyright")
        expected_version_information_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_version_information_text")
        expected_webapi_text_on_version_info = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_webapi_text_on_version_info")
        expected_server_text_on_version_info = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_server_text_on_version_info")
        expected_webapi_version_number = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_webapi_version_number")
        expected_portal_version_number = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_portal_version_number")
        expected_heading_on_user_panel = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_heading_on_user_panel")
        expected_heading_on_alert_schedule_panel = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_heading_on_alert_schedule_panel")
        expected_success_message_to_user = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_success_message_to_user")

        so_user_role = self.common_test_data_config.get("User_Roles_Data", "so_user_role")
        so_user_role_description = self.common_test_data_config.get("User_Roles_Data", "so_user_role_description")
        so_username = self.common_test_data_config.get("User_Roles_Data", "username")
        first_name = self.common_test_data_config.get("User_Roles_Data", "first_name")
        last_name = self.common_test_data_config.get("User_Roles_Data", "last_name")
        user_role = so_user_role
        company = self.common_test_data_config.get("User_Roles_Data", "company")
        title = self.common_test_data_config.get("User_Roles_Data", "title")
        department = self.common_test_data_config.get("User_Roles_Data", "department")
        user_role = so_user_role
        email = self.common_test_data_config.get("User_Roles_Data", "email")
        alert_phone_number = self.common_test_data_config.get("User_Roles_Data", "alert_phone_number")
        time_zone = self.common_test_data_config.get("User_Roles_Data", "time_zone")
        address = self.common_test_data_config.get("User_Roles_Data", "address")
        address_2 = self.common_test_data_config.get("User_Roles_Data", "address_2")
        city = self.common_test_data_config.get("User_Roles_Data", "city")
        state = self.common_test_data_config.get("User_Roles_Data", "state")
        postal_code = self.common_test_data_config.get("User_Roles_Data", "postal_code")
        home_phone_number = self.common_test_data_config.get("User_Roles_Data", "home_phone_number")
        work_phone_number = self.common_test_data_config.get("User_Roles_Data", "work_phone_number")
        fax_phone_number = self.common_test_data_config.get("User_Roles_Data", "fax_phone_number")
        phone_type = self.common_test_data_config.get("User_Roles_Data", "phone_type")
        phone_provider = self.common_test_data_config.get("User_Roles_Data", "phone_provider")

        Table_Column_Heading1 = self.common_test_data_config.get("User_Roles_Data", "Table Column Heading1")
        Table_Column_Heading2 = self.common_test_data_config.get("User_Roles_Data", "Table Column Heading2")
        Table_Column_Heading3 = self.common_test_data_config.get("User_Roles_Data", "Table Column Heading3")
        Table_Column_Heading4 = self.common_test_data_config.get("User_Roles_Data", "Table Column Heading4")
        Table_Column_Heading5 = self.common_test_data_config.get("User_Roles_Data", "Table Column Heading5")

        Table_Row_Heading1 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading1")
        Table_Row_Heading2 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading2")
        Table_Row_Heading3 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading3")
        Table_Row_Heading4 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading4")
        Table_Row_Heading5 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading5")
        Table_Row_Heading6 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading6")
        Table_Row_Heading7 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading7")
        Table_Row_Heading8 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading8")
        Table_Row_Heading9 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading9")
        Table_Row_Heading10 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading10")
        Table_Row_Heading11 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading11")
        Table_Row_Heading12 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading12")
        Table_Row_Heading13 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading13")
        Table_Row_Heading14 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading14")
        Table_Row_Heading15 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading15")
        Table_Row_Heading16 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading16")
        Table_Row_Heading17 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading17")
        Table_Row_Heading18 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading18")
        Table_Row_Heading19 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading19")
        Table_Row_Heading20 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading20")
        Table_Row_Heading21 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading21")
        Table_Row_Heading22 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading22")
        Table_Row_Heading23 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading23")
        Table_Row_Heading24 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading24")
        Table_Row_Heading25 = self.common_test_data_config.get("User_Roles_Data", "Table Row Heading25")




        print(cloud_login_url, username)






update_common_data()
