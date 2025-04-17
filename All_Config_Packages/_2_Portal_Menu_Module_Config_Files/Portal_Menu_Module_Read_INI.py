import configparser
from pathlib import Path

filepath = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\2_Portal_Menu_Module\\Data_From_INI\\Portal_Menu_Module.ini"
print("configure filepath: ", filepath)
common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"

class Portal_Menu_Module_read_ini:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            self.config.read(filepath)
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print(ex.args)

    def get_portal_url(self):
        try:
            portal_url = self.common_test_data_config.get("Login_Logout_Data", "cloud_login_url")
            print("portal page url: ", portal_url)
            return portal_url
        except Exception as ex:
            print(ex.args)

    def get_portal_title(self):
        try:
            portal_title = self.common_test_data_config.get("Login_Logout_Data", "portal_title")
            print("portal title: ", portal_title)
            return portal_title
        except Exception as ex:
            print(ex.args)

    def get_portal_login_username_textbox_by_xpath(self):
        try:
            portal_login_username_texbox = self.config.get("Portal_Login_Page",
                                                           "portal_login_username_textbox_by_xpath")
            print("portal username textbox: ", portal_login_username_texbox)
            return portal_login_username_texbox
        except Exception as ex:
            print(ex.args)

    def get_portal_login_username(self):
        try:
            portal_login_username = self.common_test_data_config.get("Login_Logout_Data", "username")
            print("username: ", portal_login_username)
            return portal_login_username
        except Exception as ex:
            print(ex.args)

    def get_portal_login_password_textbox_by_xpath(self):
        try:
            portal_login_password_textbox = self.config.get("Portal_Login_Page",
                                                            "portal_login_password_textbox_by_xpath")
            print("portal password textbox: ", portal_login_password_textbox)
            return portal_login_password_textbox
        except Exception as ex:
            print(ex.args)

    def get_portal_login_password(self):
        try:
            portal_login_password = self.common_test_data_config.get("Login_Logout_Data", "password")
            print("password: ", portal_login_password)
            return portal_login_password
        except Exception as ex:
            print(ex.args)

    def get_cloud_login_button_on_portal_by_xpath(self):
        try:
            cloud_login_button_on_portal = self.config.get("Portal_Login_Page", "cloud_login_button_on_portal_by_xpath")
            print("cloud login button on portal: ", cloud_login_button_on_portal)
            return cloud_login_button_on_portal
        except Exception as ex:
            print(ex.args)

    def get_logout_button_on_portal_by_xpath(self):
        try:
            logout_button_on_portal = self.config.get("Portal_Login_Page", "logout_button_on_portal_by_xpath")
            print("logout button on portal: ", logout_button_on_portal)
            return logout_button_on_portal
        except Exception as ex:
            print(ex.args)

    def get_executive_menus(self):
        try:
            executive_menus = self.config.get("Portal Menu", "executive_menus")
            print("expected executive_menus: ", executive_menus)
            return executive_menus
        except Exception as ex:
            print(ex.args)

    def get_it_admin_menus(self):
        try:
            it_admin_menus = self.config.get("Portal Menu", "it_admin_menus")
            print("expected it_admin_menus: ", it_admin_menus)
            return it_admin_menus
        except Exception as ex:
            print(ex.args)

    def get_close_panel_button_by_xpath(self):
        try:
            close_panel_button = self.config.get("Portal Menu", "close_panel_button_by_xpath")
            print("close_panel_button_by_xpath: ", close_panel_button)
            return close_panel_button
        except Exception as ex:
            print(ex)

    def get_events_menu_by_xpath(self):
        try:
            events_menu = self.config.get("Portal Menu", "Events_menu_by_xpath")
            print("events_menu_by_xpath: ", events_menu)
            return events_menu
        except Exception as ex:
            print(ex.args)

    def get_title_on_Events_panel_by_xpath(self):
        try:
            events_title_on_events_panel = self.config.get("Portal Menu", "title_on_Events_panel_by_xpath")
            print("title_on_Events_panel_by_xpath: ", events_title_on_events_panel)
            return events_title_on_events_panel
        except Exception as ex:
            print(ex.args)

    def get_expected_events_text(self):
        try:
            expected_events_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_events_text")
            print("expected_events_text: ", expected_events_text)
            return expected_events_text
        except Exception as ex:
            print(ex.args)

    def get_Tags_menu_by_xpath(self):
        try:
            Tags_menu_by_xpath = self.config.get("Portal Menu", "Tags_menu_by_xpath")
            print("Tags_menu_by_xpath: ", Tags_menu_by_xpath)
            return Tags_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Tags_panel_by_xpath(self):
        try:
            title_on_Tags_panel_by_xpath = self.config.get("Portal Menu", "title_on_Tags_panel_by_xpath")
            print("title_on_Tags_panel_by_xpath: ", title_on_Tags_panel_by_xpath)
            return title_on_Tags_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_tags_text(self):
        try:
            expected_tags_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_tags_text")
            print("expected_tags_text: ", expected_tags_text)
            return expected_tags_text
        except Exception as ex:
            print(ex.args)

    def get_Identify_and_Enroll_menu_by_xpath(self):
        try:
            Identify_and_Enroll_menu_by_xpath = self.config.get("Portal Menu", "Identify_and_Enroll_menu_by_xpath")
            print("Identify_and_Enroll_menu_by_xpath: ", Identify_and_Enroll_menu_by_xpath)
            return Identify_and_Enroll_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Identify_Enroll_panel_by_xpath(self):
        try:
            title_on_Identify_Enroll_panel_by_xpath = self.config.get("Portal Menu",
                                                                      "title_on_Identify_Enroll_panel_by_xpath")
            print("title_on_Identify_Enroll_panel_by_xpath: ", title_on_Identify_Enroll_panel_by_xpath)
            return title_on_Identify_Enroll_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_identify_enroll_text(self):
        try:
            expected_identify_enroll_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_identify_enroll_text")
            print("expected_identify_enroll_text: ", expected_identify_enroll_text)
            return expected_identify_enroll_text
        except Exception as ex:
            print(ex.args)

    def get_Detect_Faces_menu_by_xpath(self):
        try:
            Detect_Faces_menu_by_xpath = self.config.get("Portal Menu", "Detect_Faces_menu_by_xpath")
            print("Detect_Faces_menu_by_xpath: ", Detect_Faces_menu_by_xpath)
            return Detect_Faces_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Detect_Faces_panel_by_xpath(self):
        try:
            title_on_Detect_Faces_panel_by_xpath = self.config.get("Portal Menu",
                                                                   "title_on_Detect_Faces_panel_by_xpath")
            print("title_on_Detect_Faces_panel_by_xpath: ", title_on_Detect_Faces_panel_by_xpath)
            return title_on_Detect_Faces_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_detect_faces_text(self):
        try:
            expected_detect_faces_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_detect_faces_text")
            print("expected_detect_faces_text: ", expected_detect_faces_text)
            return expected_detect_faces_text
        except Exception as ex:
            print(ex.args)

    def get_Enrollments_menu_by_xpath(self):
        try:
            Enrollments_menu_by_xpath = self.config.get("Portal Menu", "Enrollments_menu_by_xpath")
            print("Enrollments_menu_by_xpath: ", Enrollments_menu_by_xpath)
            return Enrollments_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Enrollments_panel_by_xpath(self):
        try:
            title_on_Enrollments_panel_by_xpath = self.config.get("Portal Menu", "title_on_Enrollments_panel_by_xpath")
            print("title_on_Enrollments_panel_by_xpath: ", title_on_Enrollments_panel_by_xpath)
            return title_on_Enrollments_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_enrollments_text(self):
        try:
            expected_enrollments_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_enrollments_text")
            print("expected_enrollments_text: ", expected_enrollments_text)
            return expected_enrollments_text
        except Exception as ex:
            print(ex.args)

    def get_Enrollment_Groups_menu_by_xpath(self):
        try:
            Enrollment_Groups_menu_by_xpath = self.config.get("Portal Menu", "Enrollment_Groups_menu_by_xpath")
            print("Enrollment_Groups_menu_by_xpath: ", Enrollment_Groups_menu_by_xpath)
            return Enrollment_Groups_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Enrollment_Groups_panel_by_xpath(self):
        try:
            title_on_Enrollment_Groups_panel_by_xpath = self.config.get("Portal Menu",
                                                                        "title_on_Enrollment_Groups_panel_by_xpath")
            print("title_on_Enrollment_Groups_panel_by_xpath: ", title_on_Enrollment_Groups_panel_by_xpath)
            return title_on_Enrollment_Groups_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_enrollment_groups_text(self):
        try:
            expected_enrollment_groups_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_enrollment_groups_text")
            print("expected_enrollment_groups_text: ", expected_enrollment_groups_text)
            return expected_enrollment_groups_text
        except Exception as ex:
            print(ex.args)

    def get_Notification_Groups_menu_by_xpath(self):
        try:
            Notification_Groups_menu_by_xpath = self.config.get("Portal Menu", "Notification_Groups_menu_by_xpath")
            print("Notification_Groups_menu_by_xpath: ", Notification_Groups_menu_by_xpath)
            return Notification_Groups_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Notification_Groups_panel_by_xpath(self):
        try:
            title_on_Notification_Groups_panel_by_xpath = self.config.get("Portal Menu",
                                                                          "title_on_Notification_Groups_panel_by_xpath")
            print("title_on_Notification_Groups_panel_by_xpath: ", title_on_Notification_Groups_panel_by_xpath)
            return title_on_Notification_Groups_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_notification_groups_text(self):
        try:
            expected_notification_groups_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_notification_groups_text")
            print("expected_notification_groups_text: ", expected_notification_groups_text)
            return expected_notification_groups_text
        except Exception as ex:
            print(ex.args)

    def get_Visitor_Search_menu_by_xpath(self):
        try:
            Visitor_Search_menu_by_xpath = self.config.get("Portal Menu", "Visitor_Search_menu_by_xpath")
            print("Visitor_Search_menu_by_xpath: ", Visitor_Search_menu_by_xpath)
            return Visitor_Search_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Visitor_Search_panel_by_xpath(self):
        try:
            title_on_Visitor_Search_panel_by_xpath = self.config.get("Portal Menu",
                                                                     "title_on_Visitor_Search_panel_by_xpath")
            print("title_on_Visitor_Search_panel_by_xpath: ", title_on_Visitor_Search_panel_by_xpath)
            return title_on_Visitor_Search_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_visitor_search_text(self):
        try:
            expected_visitor_search_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_visitor_search_text")
            print("expected_visitor_search_text: ", expected_visitor_search_text)
            return expected_visitor_search_text
        except Exception as ex:
            print(ex.args)

    def get_Visitor_Search_Jobs_menu_by_xpath(self):
        try:
            Visitor_Search_Jobs_menu_by_xpath = self.config.get("Portal Menu", "Visitor_Search_Jobs_menu_by_xpath")
            print("Visitor_Search_Jobs_menu_by_xpath: ", Visitor_Search_Jobs_menu_by_xpath)
            return Visitor_Search_Jobs_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Visitor_Search_Jobs_panel_by_xpath(self):
        try:
            title_on_Visitor_Search_Jobs_panel_by_xpath = self.config.get("Portal Menu",
                                                                          "title_on_Visitor_Search_Jobs_panel_by_xpath")
            print("title_on_Visitor_Search_Jobs_panel_by_xpath: ", title_on_Visitor_Search_Jobs_panel_by_xpath)
            return title_on_Visitor_Search_Jobs_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_visitor_search_jobs_text(self):
        try:
            expected_visitor_search_jobs_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_visitor_search_jobs_text")
            print("expected_visitor_search_jobs_text: ", expected_visitor_search_jobs_text)
            return expected_visitor_search_jobs_text
        except Exception as ex:
            print(ex.args)

    def get_Notes_menu_by_xpath(self):
        try:
            Notes_menu_by_xpath = self.config.get("Portal Menu", "Notes_menu_by_xpath")
            print("Notes_menu_by_xpath: ", Notes_menu_by_xpath)
            return Notes_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Notes_panel_by_xpath(self):
        try:
            title_on_Notes_panel_by_xpath = self.config.get("Portal Menu", "title_on_Notes_panel_by_xpath")
            print("title_on_Notes_panel_by_xpath: ", title_on_Notes_panel_by_xpath)
            return title_on_Notes_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_notes_text(self):
        try:
            expected_notes_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_notes_text")
            print("expected_notes_text: ", expected_notes_text)
            return expected_notes_text
        except Exception as ex:
            print(ex.args)

    def get_Locations_menu_by_xpath(self):
        try:
            Locations_menu_by_xpath = self.config.get("Portal Menu", "Locations_menu_by_xpath")
            print("Locations_menu_by_xpath: ", Locations_menu_by_xpath)
            return Locations_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Locations_panel_by_xpath(self):
        try:
            title_on_Locations_panel_by_xpath = self.config.get("Portal Menu", "title_on_Locations_panel_by_xpath")
            print("title_on_Locations_panel_by_xpath: ", title_on_Locations_panel_by_xpath)
            return title_on_Locations_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_cancel_button_on_location_panel_by_xpath(self):
        try:
            cancel_button_on_location_panel_by_xpath = self.config.get("Portal Menu",
                                                                       "cancel_button_on_location_panel_by_xpath")
            print("cancel_button_on_location_panel_by_xpath: ", cancel_button_on_location_panel_by_xpath)
            return cancel_button_on_location_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_locations_text(self):
        try:
            expected_locations_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_locations_text")
            print("expected_locations_text: ", expected_locations_text)
            return expected_locations_text
        except Exception as ex:
            print(ex.args)

    def get_Users_menu_by_xpath(self):
        try:
            Users_menu_by_xpath = self.config.get("Portal Menu", "Users_menu_by_xpath")
            print("Users_menu_by_xpath: ", Users_menu_by_xpath)
            return Users_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Users_panel_by_xpath(self):
        try:
            title_on_Users_panel_by_xpath = self.config.get("Portal Menu", "title_on_Users_panel_by_xpath")
            print("title_on_Users_panel_by_xpath: ", title_on_Users_panel_by_xpath)
            return title_on_Users_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_users_text(self):
        try:
            expected_users_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_users_text")
            print("expected_users_text: ", expected_users_text)
            return expected_users_text
        except Exception as ex:
            print(ex.args)

    def get_User_Roles_menu_by_xpath(self):
        try:
            User_Roles_menu_by_xpath = self.config.get("Portal Menu", "User_Roles_menu_by_xpath")
            print("User_Roles_menu_by_xpath: ", User_Roles_menu_by_xpath)
            return User_Roles_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_User_Roles_panel_by_xpath(self):
        try:
            title_on_User_Roles_panel_by_xpath = self.config.get("Portal Menu", "title_on_User_Roles_panel_by_xpath")
            print("title_on_User_Roles_panel_by_xpath: ", title_on_User_Roles_panel_by_xpath)
            return title_on_User_Roles_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_user_roles_text(self):
        try:
            expected_user_roles_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_user_roles_text")
            print("expected_user_roles_text: ", expected_user_roles_text)
            return expected_user_roles_text
        except Exception as ex:
            print(ex.args)

    def get_Zones_menu_by_xpath(self):
        try:
            Zones_menu_by_xpath = self.config.get("Portal Menu", "Zones_menu_by_xpath")
            print("Zones_menu_by_xpath: ", Zones_menu_by_xpath)
            return Zones_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Zones_panel_by_xpath(self):
        try:
            title_on_Zones_panel_by_xpath = self.config.get("Portal Menu", "title_on_Zones_panel_by_xpath")
            print("title_on_Zones_panel_by_xpath: ", title_on_Zones_panel_by_xpath)
            return title_on_Zones_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_zones_text(self):
        try:
            expected_zones_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_zones_text")
            print("expected_zones_text: ", expected_zones_text)
            return expected_zones_text
        except Exception as ex:
            print(ex.args)

    def get_Account_menu_by_xpath(self):
        try:
            Account_menu_by_xpath = self.config.get("Portal Menu", "Account_menu_by_xpath")
            print("Account_menu_by_xpath: ", Account_menu_by_xpath)
            return Account_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Account_panel_by_xpath(self):
        try:
            title_on_Account_panel_by_xpath = self.config.get("Portal Menu", "title_on_Account_panel_by_xpath")
            print("title_on_Account_panel_by_xpath: ", title_on_Account_panel_by_xpath)
            return title_on_Account_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_account_text(self):
        try:
            expected_account_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_account_text")
            print("expected_account_text: ", expected_account_text)
            return expected_account_text
        except Exception as ex:
            print(ex.args)

    def get_Reporting_menu_by_xpath(self):
        try:
            Reporting_menu_by_xpath = self.config.get("Portal Menu", "Reporting_menu_by_xpath")
            print("Reporting_menu_by_xpath: ", Reporting_menu_by_xpath)
            return Reporting_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Reporting_panel_by_xpath(self):
        try:
            title_on_Reporting_panel_by_xpath = self.config.get("Portal Menu", "title_on_Reporting_panel_by_xpath")
            print("title_on_Reporting_panel_by_xpath: ", title_on_Reporting_panel_by_xpath)
            return title_on_Reporting_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_reporting_text(self):
        try:
            expected_reporting_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_reporting_text")
            print("expected_reporting_text: ", expected_reporting_text)
            return expected_reporting_text
        except Exception as ex:
            print(ex.args)

    def get_Dashboard_menu_by_xpath(self):
        try:
            Dashboard_menu_by_xpath = self.config.get("Portal Menu", "Insight_Dashboard_menu_by_xpath")
            print("Dashboard_menu_by_xpath: ", Dashboard_menu_by_xpath)
            return Dashboard_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Dashboard_panel_by_xpath(self):
        try:
            title_on_Dashboard_panel_by_xpath = self.config.get("Portal Menu", "title_on_Dashboard_panel_by_xpath")
            print("title_on_Dashboard_panel_by_xpath: ", title_on_Dashboard_panel_by_xpath)
            return title_on_Dashboard_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_fidusvision_text(self):
        try:
            expected_fidusvision_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_fidusvision_text")
            print("expected_fidusvision_text: ", expected_fidusvision_text)
            return expected_fidusvision_text
        except Exception as ex:
            print(ex.args)

    def get_expected_dashboard_text(self):
        try:
            expected_dashboard_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_dashboard_text")
            print("expected_dashboard_text: ", expected_dashboard_text)
            return expected_dashboard_text
        except Exception as ex:
            print(ex.args)

    def get_Notifier_menu_by_xpath(self):
        try:
            Notifier_menu_by_xpath = self.config.get("Portal Menu", "Notifier_menu_by_xpath")
            print("Notifier_menu_by_xpath: ", Notifier_menu_by_xpath)
            return Notifier_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Notifier_panel_by_xpath(self):
        try:
            title_on_Notifier_panel_by_xpath = self.config.get("Portal Menu", "title_on_Notifier_panel_by_xpath")
            print("title_on_Notifier_panel_by_xpath: ", title_on_Notifier_panel_by_xpath)
            return title_on_Notifier_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_close_notifier_button_by_xpath(self):
        try:
            close_notifier_button_by_xpath = self.config.get("Portal Menu", "close_notifier_button_by_xpath")
            print("close_notifier_button_by_xpath: ", close_notifier_button_by_xpath)
            return close_notifier_button_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_notifier_text(self):
        try:
            expected_notifier_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_notifier_text")
            print("expected_notifier_text: ", expected_notifier_text)
            return expected_notifier_text
        except Exception as ex:
            print(ex.args)

    def get_Audit_Log_Report_menu_by_xpath(self):
        try:
            Audit_Log_Report_menu_by_xpath = self.config.get("Portal Menu", "Audit_Log_Report_menu_by_xpath")
            print("Audit_Log_Report_menu_by_xpath: ", Audit_Log_Report_menu_by_xpath)
            return Audit_Log_Report_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_Audit_Log_Report_panel_by_xpath(self):
        try:
            title_on_Audit_Log_Report_panel_by_xpath = self.config.get("Portal Menu",
                                                                       "title_on_Audit_Log_Report_panel_by_xpath")
            print("title_on_Audit_Log_Report_panel_by_xpath: ", title_on_Audit_Log_Report_panel_by_xpath)
            return title_on_Audit_Log_Report_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_select_report_criteria_heading_by_xpath(self):
        try:
            select_report_criteria_heading_by_xpath = self.config.get("Portal Menu",
                                                                       "select_report_criteria_heading_by_xpath")
            print("select_report_criteria_heading_by_xpath: ", select_report_criteria_heading_by_xpath)
            return select_report_criteria_heading_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_audit_log_report_text(self):
        try:
            expected_audit_log_report_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_audit_log_report_text")
            print("expected_audit_log_report_text: ", expected_audit_log_report_text)
            return expected_audit_log_report_text
        except Exception as ex:
            print(ex.args)

    def get_select_report_criteria_heading(self):
        try:
            select_report_criteria_heading = self.common_test_data_config.get("Portal_Menu_Module_Data", "select_report_criteria_heading")
            print("select_report_criteria_heading: ", select_report_criteria_heading)
            return select_report_criteria_heading
        except Exception as ex:
            print(ex.args)

    def get_CLOUD_MENU_button_by_xpath(self):
        try:
            CLOUD_MENU_button_by_xpath = self.config.get("Portal Menu", "CLOUD_MENU_button_by_xpath")
            print("CLOUD_MENU_button_by_xpath: ", CLOUD_MENU_button_by_xpath)
            return CLOUD_MENU_button_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_close_all_panels_menu_by_xpath(self):
        try:
            close_all_panels_menu_by_xpath = self.config.get("Portal Menu", "close_all_panels_menu_by_xpath")
            print("close_all_panels_menu_by_xpath: ", close_all_panels_menu_by_xpath)
            return close_all_panels_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_close_all_panels_text(self):
        try:
            expected_close_all_panels_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_close_all_panels_text")
            print("expected_close_all_panels_text: ", expected_close_all_panels_text)
            return expected_close_all_panels_text
        except Exception as ex:
            print(ex.args)

    def get_icon_on_close_all_panels_menu_by_xpath(self):
        try:
            icon_on_close_all_panels_menu_by_xpath = self.config.get("Portal Menu",
                                                                     "icon_on_close_all_panels_menu_by_xpath")
            print("icon_on_close_all_panels_menu_by_xpath: ", icon_on_close_all_panels_menu_by_xpath)
            return icon_on_close_all_panels_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_copyright_text_by_xpath(self):
        try:
            copy_right_text_by_xpath = self.config.get("Portal Menu", "copy_right_text_by_xpath")
            print("copy_right_text_by_xpath: ", copy_right_text_by_xpath)
            return copy_right_text_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_face_first_copyright(self):
        try:
            expected_face_first_copyright = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_face_first_copyright")
            print("expected_face_first_copyright: ", expected_face_first_copyright)
            return expected_face_first_copyright
        except Exception as ex:
            print(ex.args)

    def get_title_on_version_information_panel_by_xpath(self):
        try:
            title_on_version_information_panel_by_xpath = self.config.get("Portal Menu",
                                                                          "title_on_version_information_panel_by_xpath")
            print("title_on_version_information_panel_by_xpath: ", title_on_version_information_panel_by_xpath)
            return title_on_version_information_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_version_information_text(self):
        try:
            expected_version_information_text = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_version_information_text")
            print("expected_version_information_text: ", expected_version_information_text)
            return expected_version_information_text
        except Exception as ex:
            print(ex.args)

    def get_face_first_logo_on_version_info_panel_by_xpath(self):
        try:
            face_first_logo_on_version_info_panel_by_xpath = self.config.get("Portal Menu", "face_first_logo_on_version_info_panel_by_xpath")
            print("face_first_logo_on_version_info_panel_by_xpath: ", face_first_logo_on_version_info_panel_by_xpath)
            return face_first_logo_on_version_info_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_face_first_copyright_on_version_info_panel_by_xpath(self):
        try:
            face_first_copyright_on_version_info_panel_by_xpath = self.config.get("Portal Menu", "face_first_copyright_on_version_info_panel_by_xpath")
            print("face_first_copyright_on_version_info_panel_by_xpath: ", face_first_copyright_on_version_info_panel_by_xpath)
            return face_first_copyright_on_version_info_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_WebAPI_text_on_version_info_by_xpath(self):
        try:
            WebAPI_text_on_version_info = self.config.get("Portal Menu", "WebAPI_text_on_version_info_by_xpath")
            print("webapi text on version info: ", WebAPI_text_on_version_info)
            return WebAPI_text_on_version_info
        except Exception as ex:
            print(ex)

    def get_expected_webapi_text_on_version_info(self):
        try:
            webapi_text_on_version_info = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_webapi_text_on_version_info")
            print("expected webapi text on version info: ", webapi_text_on_version_info)
            return webapi_text_on_version_info
        except Exception as ex:
            print(ex)

    def get_Server_text_on_version_info_by_xpath(self):
        try:
            Server_text_on_version_info = self.config.get("Portal Menu", "Server_text_on_version_info_by_xpath")
            print("server text on version info: ", Server_text_on_version_info)
            return Server_text_on_version_info
        except Exception as ex:
            print(ex)

    def get_expected_server_text_on_version_info(self):
        try:
            server_text_on_version_info = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_server_text_on_version_info")
            print("expected server text on version info: ", server_text_on_version_info)
            return server_text_on_version_info
        except Exception as ex:
            print(ex)

    def get_webapi_version_info_by_xpath(self):
        try:
            webapi_version_info = self.config.get("Portal Menu", "webapi_version_info_by_xpath")
            print("webapi version info: ", webapi_version_info)
            return webapi_version_info
        except Exception as ex:
            print(ex)

    def get_expected_webapi_version_number(self):
        try:
            webapi_version_number = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_webapi_version_number")
            print("expected webapi version number: ", webapi_version_number)
            return webapi_version_number
        except Exception as ex:
            print(ex)

    def get_portal_version_number_by_xpath(self):
        try:
            actual_portal_version_number = self.config.get("Portal Menu", "portal_version_number_by_xpath")
            print("portal version number: ", actual_portal_version_number)
            return actual_portal_version_number
        except Exception as ex:
            print(ex)

    def get_expected_portal_version_number(self):
        try:
            portal_version_number = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_portal_version_number")
            print("expected portal version number: ", portal_version_number)
            return portal_version_number
        except Exception as ex:
            print(ex)

    def get_user_name_on_taskbar_by_xpath(self):
        try:
            user_name_on_taskbar_by_xpath = self.config.get("Portal Menu", "user_name_on_taskbar_by_xpath")
            print("user_name_on_taskbar_by_xpath: ", user_name_on_taskbar_by_xpath)
            return user_name_on_taskbar_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_logo_by_xpath(self):
        try:
            user_logo_by_xpath = self.config.get("Portal Menu", "user_logo_by_xpath")
            print("user_logo_by_xpath: ", user_logo_by_xpath)
            return user_logo_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_panel_by_xpath(self):
        try:
            user_panel_by_xpath = self.config.get("Portal Menu", "user_panel_by_xpath")
            print("user_panel_by_xpath: ", user_panel_by_xpath)
            return user_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_heading_on_user_panel_by_xpath(self):
        try:
            heading_on_user_panel_by_xpath = self.config.get("Portal Menu", "heading_on_user_panel_by_xpath")
            print("heading_on_user_panel_by_xpath: ", heading_on_user_panel_by_xpath)
            return heading_on_user_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_heading_on_user_panel(self):
        try:
            expected_heading_on_user_panel = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_heading_on_user_panel")
            print("expected_heading_on_user_panel: ", expected_heading_on_user_panel)
            return expected_heading_on_user_panel
        except Exception as ex:
            print(ex.args)

    def get_icon_by_xpath(self):
        try:
            icon_by_xpath = self.config.get("Portal Menu", "icon_by_xpath")
            print("icon_by_xpath: ", icon_by_xpath)
            return icon_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_action_dropdown_by_xpath(self):
        try:
            action_dropdown_by_xpath = self.config.get("Portal Menu", "action_dropdown_by_xpath")
            print("action_dropdown_by_xpath: ", action_dropdown_by_xpath)
            return action_dropdown_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_options_inside_action_dropdown_on_user_panel_by_xpath(self):
        try:
            options_inside_action_dropdown_on_user_panel_by_xpath = \
                self.config.get("Portal Menu", "options_inside_action_dropdown_on_user_panel_by_xpath")
            print("options_inside_action_dropdown_on_user_panel_by_xpath: ",
                  options_inside_action_dropdown_on_user_panel_by_xpath)
            return options_inside_action_dropdown_on_user_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_alert_schedule_button_on_user_panel_by_xpath(self):
        try:
            alert_schedule_button_on_user_panel_by_xpath = \
                self.config.get("Portal Menu", "alert_schedule_button_on_user_panel_by_xpath")
            print("alert_schedule_button_on_user_panel_by_xpath: ", alert_schedule_button_on_user_panel_by_xpath)
            return alert_schedule_button_on_user_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_heading_on_alert_schedule_panel_by_xpath(self):
        try:
            heading_on_alert_schedule_panel_by_xpath = \
                self.config.get("Portal Menu", "heading_on_alert_schedule_panel_by_xpath")
            print("heading_on_alert_schedule_panel_by_xpath: ", heading_on_alert_schedule_panel_by_xpath)
            return heading_on_alert_schedule_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_heading_on_alert_schedule_panel(self):
        try:
            expected_heading_on_alert_schedule_panel = \
                self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_heading_on_alert_schedule_panel")
            print("expected_heading_on_alert_schedule_panel: ", expected_heading_on_alert_schedule_panel)
            return expected_heading_on_alert_schedule_panel
        except Exception as ex:
            print(ex.args)

    def get_notification_groups_button_on_user_panel_by_xpath(self):
        try:
            notification_groups_button_on_user_panel_by_xpath = \
                self.config.get("Portal Menu", "notification_groups_button_on_user_panel_by_xpath")
            print("notification_groups_button_on_user_panel_by_xpath: ",
                  notification_groups_button_on_user_panel_by_xpath)
            return notification_groups_button_on_user_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_notification_groups_panel_by_xpath(self):
        try:
            notification_groups_panel_by_xpath = self.config.get("Portal Menu", "notification_groups_panel_by_xpath")
            print("notification_groups_panel_by_xpath: ", notification_groups_panel_by_xpath)
            return notification_groups_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_logout_btn_by_xpath(self):
        try:
            logout_btn_by_xpath = self.config.get("Portal Menu", "logout_btn_by_xpath")
            print("logout_btn_by_xpath: ", logout_btn_by_xpath)
            return logout_btn_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_login_btn_by_xpath(self):
        try:
            login_btn_by_xpath = self.config.get("Portal Menu", "login_btn_by_xpath")
            print("login_btn_by_xpath: ", login_btn_by_xpath)
            return login_btn_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_dollar_icon_on_dashboard_menu_by_xpath(self):
        try:
            dollar_icon_on_dashboard_menu_by_xpath = self.config.get("Portal Menu",
                                                                     "dollar_icon_on_dashboard_menu_by_xpath")
            print("dollar_icon_on_dashboard_menu_by_xpath: ", dollar_icon_on_dashboard_menu_by_xpath)
            return dollar_icon_on_dashboard_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_shield_icon_on_alr_menu_by_xpath(self):
        try:
            shield_icon_on_alr_menu_by_xpath = self.config.get("Portal Menu", "shield_icon_on_alr_menu_by_xpath")
            print("shield_icon_on_alr_menu_by_xpath: ", shield_icon_on_alr_menu_by_xpath)
            return shield_icon_on_alr_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_current_password_textbox_by_xpath(self):
        try:
            current_password_textbox_by_xpath = self.config.get("Portal Menu", "current_password_textbox_by_xpath")
            print("current_password_textbox_by_xpath: ", current_password_textbox_by_xpath)
            return current_password_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_new_password_textbox_by_xpath(self):
        try:
            new_password_textbox_by_xpath = self.config.get("Portal Menu", "new_password_textbox_by_xpath")
            print("new_password_textbox_by_xpath: ", new_password_textbox_by_xpath)
            return new_password_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_confirm_password_textbox_by_xpath(self):
        try:
            confirm_password_textbox_by_xpath = self.config.get("Portal Menu", "confirm_password_textbox_by_xpath")
            print("confirm_password_textbox_by_xpath: ", confirm_password_textbox_by_xpath)
            return confirm_password_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_new_password(self):
        try:
            new_password = self.common_test_data_config.get("Portal_Menu_Module_Data", "new_password")
            print("new_password: ", new_password)
            return new_password
        except Exception as ex:
            print(ex.args)

    def get_first_name(self):
        try:
            first_name = self.common_test_data_config.get("Portal_Menu_Module_Data", "first_name")
            print("first_name: ", first_name)
            return first_name
        except Exception as ex:
            print(ex.args)

    def get_last_name(self):
        try:
            last_name = self.common_test_data_config.get("Portal_Menu_Module_Data", "last_name")
            print("new_password: ", last_name)
            return last_name
        except Exception as ex:
            print(ex.args)

    def get_first_name_textbox_by_xpath(self):
        try:
            first_name_textbox_by_xpath = self.config.get("Portal Menu", "first_name_textbox_by_xpath")
            print("first_name_textbox_by_xpath: ", first_name_textbox_by_xpath)
            return first_name_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_last_name_textbox_by_xpath(self):
        try:
            last_name_textbox_by_xpath = self.config.get("Portal Menu", "last_name_textbox_by_xpath")
            print("last_name_textbox_by_xpath: ", last_name_textbox_by_xpath)
            return last_name_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_save_button_on_user_panel_by_xpath(self):
        try:
            save_button_on_user_panel_by_xpath = self.config.get("Portal Menu", "save_button_on_user_panel_by_xpath")
            print("save_button_on_user_panel_by_xpath: ", save_button_on_user_panel_by_xpath)
            return save_button_on_user_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_success_message_to_user_by_xpath(self):
        try:
            success_message_to_user_by_xpath = self.config.get("Portal Menu", "success_message_to_user_by_xpath")
            print("success_message_to_user_by_xpath: ", success_message_to_user_by_xpath)
            return success_message_to_user_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expected_success_message_to_user(self):
        try:
            expected_success_message_to_user = self.common_test_data_config.get("Portal_Menu_Module_Data", "expected_success_message_to_user")
            print("expected_success_message_to_user: ", expected_success_message_to_user)
            return expected_success_message_to_user
        except Exception as ex:
            print(ex.args)

# Portal_Menu_Module_read_ini().get_expected_webapi_text_on_version_info()