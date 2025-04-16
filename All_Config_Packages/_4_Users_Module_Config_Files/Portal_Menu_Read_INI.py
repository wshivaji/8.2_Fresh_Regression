import configparser
from pathlib import Path


class Read_Portal_Menu_Components:
    def __init__(self):

        self.config = configparser.RawConfigParser()

        try:
            portal_menu_ini_file_path = f'{Path(__file__).parent.parent.parent}\\Test_Data\\Data_From_INI' \
                                        f'\\Portal_Menu.ini'
            # Base_Class.logger.info("File location: ", deployment_manager_ini_file_path)
            self.config.read(portal_menu_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def get_usernameField(self):
        try:
            username = self.config.get('LOCATORS', 'portal_login_page_usernameField_by_xpath')
            # Base_Class.logger.info("URL read successfully : ", url)
            return username
        except Exception as ex:
            print(ex)

    def get_passwordField(self):
        try:
            password = self.config.get('LOCATORS', 'portal_login_page_passwordField_by_xpath')
            # Base_Class.logger.info("URL read successfully : ", url)
            return password
        except Exception as ex:
            print(ex)

    def get_loginButton(self):
        try:
            login_btn = self.config.get('LOCATORS', 'portal_login_page_loginBtn_by_xpath')
            # Base_Class.logger.info("URL read successfully : ", url)
            return login_btn
        except Exception as ex:
            print(ex)

    def get_username(self):
        try:
            username = self.config.get('PORTAL_LOGIN_PAGE_DATA', 'username')
            # Base_Class.logger.info("URL read successfully : ", url)
            return username
        except Exception as ex:
            print(ex)

    def get_password(self):
        try:
            password = self.config.get('PORTAL_LOGIN_PAGE_DATA', 'password')
            # Base_Class.logger.info("URL read successfully : ", url)
            return password
        except Exception as ex:
            print(ex)

    def get_url(self):
        try:
            url = self.config.get('URL', 'portal_menu_url')
            # Base_Class.logger.info("URL read successfully : ", url)
            return url
        except Exception as ex:
            print(ex)

    def logo_by_xpath(self):
        try:
            logo_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "logo_by_xpath")
            return logo_xpath
        except Exception as ex:
            print(ex)

    def portal_menu_event_btn_by_xpath(self):
        try:
            event_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "event_btn_by_xpath")
            return event_btn_by_xpath
        except Exception as ex:
            print("portal_menu_event_btn_by_xpath : ", ex)

    def portal_menu_event_validation_by_xpath(self):
        try:
            event_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS", "event_validation_by_xpath")
            return event_validation_by_xpath
        except Exception as ex:
            print("portal_menu_event_validation_by_xpath : ", ex)

    def portal_menu_tags_btn_by_xpath(self):
        try:
            tags_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "tags_btn_by_xpath")
            return tags_btn_by_xpath
        except Exception as ex:
            print("portal_menu_tags_btn_by_xpath : ", ex)

    def portal_menu_tags_validation_by_xpath(self):
        try:
            tags_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS", "tags_validation_by_xpath")
            return tags_validation_by_xpath
        except Exception as ex:
            print("portal_menu_tags_validation_by_xpath : ", ex)

    def portal_menu_identify_enroll_btn_by_xpath(self):
        try:
            identify_enroll_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "identifyEnroll_btn_by_xpath")
            return identify_enroll_btn_by_xpath
        except Exception as ex:
            print("portal_menu_indentify_enroll_btn_by_xpath : ", ex)

    def portal_menu_indentify_enroll_validation_by_xpath(self):
        try:
            indentify_enroll_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                   "identify_and_enroll_validation_by_xpath")
            return indentify_enroll_validation_by_xpath
        except Exception as ex:
            print("portal_menu_indentify_enroll_validation_by_xpath : ", ex)

    def portal_menu_detect_faces_btn_by_xpath(self):
        try:
            detect_faces_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "detect_faces_btn_by_xpath")
            return detect_faces_btn_by_xpath
        except Exception as ex:
            print("portal_menu_detect_faces_btn_by_xpath : ", ex)

    def portal_menu_detect_faces_validation_by_xpath(self):
        try:
            detect_faces_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                               "detect_faces_validation_by_xpath")
            return detect_faces_validation_by_xpath
        except Exception as ex:
            print("portal_menu_detect_faces_validation_by_xpath : ", ex)

    def portal_menu_enrollments_btn_by_xpath(self):
        try:
            enrollments_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "enrollment_btn_by_xpath")
            return enrollments_btn_by_xpath
        except Exception as ex:
            print("portal_menu_enrollments_btn_by_xpath : ", ex)

    def portal_menu_enrollments_validation_by_xpath(self):
        try:
            enrollments_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                              "enrollments_validation_by_xpath")
            return enrollments_validation_by_xpath
        except Exception as ex:
            print("portal_menu_enrollments_validation_by_xpath : ", ex)

    def portal_menu_enrollments_groups_btn_by_xpath(self):
        try:
            enrollments_groups_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS",
                                                              "enrollment_groups_btn_by_xpath")
            return enrollments_groups_btn_by_xpath
        except Exception as ex:
            print("portal_menu_enrollments_groups_btn_by_xpath : ", ex)

    def portal_menu_enrollments_groups_validation_by_xpath(self):
        try:
            enrollments_groups_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                     "enrollments_groups_validation_by_xpath")
            return enrollments_groups_validation_by_xpath
        except Exception as ex:
            print("portal_menu_enrollments_groups_validation_by_xpath : ", ex)

    def portal_menu_notification_groups_btn_by_xpath(self):
        try:
            notification_groups_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS",
                                                               "notification_Groups_btn_by_xpath")
            return notification_groups_btn_by_xpath
        except Exception as ex:
            print("portal_menu_notification_groups_btn_by_xpath : ", ex)

    def portal_menu_notification_groups_validation_by_xpath(self):
        try:
            notification_groups_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                      "notification_groups_validation_by_xpath")
            return notification_groups_validation_by_xpath
        except Exception as ex:
            print("portal_menu_notification_groups_validation_by_xpath : ", ex)

    def portal_menu_visitors_btn_by_xpath(self):
        try:
            visitors_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "visitors_btn_by_xpath")
            return visitors_btn_by_xpath
        except Exception as ex:
            print("portal_menu_visitors_btn_by_xpath : ", ex)

    def portal_menu_visitors_validation_by_xpath(self):
        try:
            visitors_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                           "visitors_validation_by_xpath")
            return visitors_validation_by_xpath
        except Exception as ex:
            print("portal_menu_visitors_validation_by_xpath : ", ex)

    def portal_menu_visitors_search_btn_by_xpath(self):
        try:
            visitors_search_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS",
                                                           "visitors_search_btn_by_xpath")
            return visitors_search_btn_by_xpath
        except Exception as ex:
            print("portal_menu_visitors_search_btn_by_xpath : ", ex)

    def portal_menu_visitors_search_validation_by_xpath(self):
        try:
            visitors_search_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                  "visitors_search_validation_by_xpath")
            return visitors_search_validation_by_xpath
        except Exception as ex:
            print("portal_menu_visitors_search_validation_by_xpath : ", ex)

    def portal_menu_visitors_search_job_btn_by_xpath(self):
        try:
            visitors_search_job_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS",
                                                               "visitors_search_job_btn_by_xpath")
            return visitors_search_job_btn_by_xpath
        except Exception as ex:
            print("portal_menu_visitors_search_job_btn_by_xpath : ", ex)

    def portal_menu_visitors_search_job_validation_by_xpath(self):
        try:
            visitors_search_job_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                      "visitors_search_job_validation_by_xpath")
            return visitors_search_job_validation_by_xpath
        except Exception as ex:
            print("portal_menu_visitors_search_job_validation_by_xpath : ", ex)

    def portal_menu_notes_btn_by_xpath(self):
        try:
            notes_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "notes_btn_by_xpath")
            return notes_btn_by_xpath
        except Exception as ex:
            print("portal_menu_notes_btn_by_xpath : ", ex)

    def portal_menu_notes_validation_by_xpath(self):
        try:
            notes_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS", "notes_validation_by_xpath")
            return notes_validation_by_xpath
        except Exception as ex:
            print("portal_menu_notes_validation_by_xpath : ", ex)

    def portal_menu_locations_btn_by_xpath(self):
        try:
            locations_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "locations_btn_by_xpath")
            return locations_btn_by_xpath
        except Exception as ex:
            print("portal_menu_locations_btn_by_xpath : ", ex)

    def portal_menu_locations_validation_by_xpath(self):
        try:
            locations_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                            "locations_validation_by_xpath")
            return locations_validation_by_xpath
        except Exception as ex:
            print("portal_menu_locations_validation_by_xpath : ", ex)

    def portal_menu_users_btn_by_xpath(self):
        try:
            users_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "users_btn_by_xpath")
            return users_btn_by_xpath
        except Exception as ex:
            print("portal_menu_users_btn_by_xpath : ", ex)

    def portal_menu_users_validation_by_xpath(self):
        try:
            users_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS", "users_validation_by_xpath")
            return users_validation_by_xpath
        except Exception as ex:
            print("portal_menu_users_validation_by_xpath : ", ex)

    def portal_menu_users_roles_btn_by_xpath(self):
        try:
            users_roles_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "users_role_btn_by_xpath")
            return users_roles_btn_by_xpath
        except Exception as ex:
            print("portal_menu_users_roles_btn_by_xpath : ", ex)

    def portal_menu_users_roles_validation_by_xpath(self):
        try:
            users_roles_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                              "user_role_validation_by_xpath")
            return users_roles_validation_by_xpath
        except Exception as ex:
            print("portal_menu_users_roles_validation_by_xpath : ", ex)

    def portal_menu_zones_btn_by_xpath(self):
        try:
            zones_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "zones_btn_by_xpath")
            return zones_btn_by_xpath
        except Exception as ex:
            print("portal_menu_zones_btn_by_xpath : ", ex)

    def portal_menu_zones_validation_by_xpath(self):
        try:
            zones_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS", "zones_validation_by_xpath")
            return zones_validation_by_xpath
        except Exception as ex:
            print("portal_menu_zones_validation_by_xpath : ", ex)

    def portal_menu_account_btn_by_xpath(self):
        try:
            account_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "account_btn_by_xpath")
            return account_btn_by_xpath
        except Exception as ex:
            print("portal_menu_account_btn_by_xpath : ", ex)

    def portal_menu_account_validation_by_xpath(self):
        try:
            account_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                          "account_validation_by_xpath")
            return account_validation_by_xpath
        except Exception as ex:
            print("portal_menu_account_validation_by_xpath : ", ex)

    def portal_menu_reporting_btn_by_xpath(self):
        try:
            reporting_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "reporting_btn_by_xpath")
            return reporting_btn_by_xpath
        except Exception as ex:
            print("portal_menu_reporting_btn_by_xpath : ", ex)

    def portal_menu_reporting_validation_by_xpath(self):
        try:
            reporting_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                            "reporting_validation_by_xpath")
            return reporting_validation_by_xpath
        except Exception as ex:
            print("portal_menu_reporting_validation_by_xpath : ", ex)

    def portal_menu_notifier_btn_by_xpath(self):
        try:
            notifier_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "notifier_btn_by_xpath")
            return notifier_btn_by_xpath
        except Exception as ex:
            print("portal_menu_notifier_btn_by_xpath : ", ex)

    def portal_menu_notifier_validation_by_xpath(self):
        try:
            notifier_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                           "notifier_validation_by_xpath")
            return notifier_validation_by_xpath
        except Exception as ex:
            print("portal_menu_notifier_validation_by_xpath : ", ex)

    def portal_menu_dashboard_btn_by_xpath(self):
        try:
            dashboard_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "dashboard_btn_by_xpath")
            return dashboard_btn_by_xpath
        except Exception as ex:
            print("portal_menu_dashboard_btn_by_xpath : ", ex)

    def portal_menu_dashboard_validation_by_xpath(self):
        try:
            dashboard_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                            "dashboard_validation_by_xpath")
            return dashboard_validation_by_xpath
        except Exception as ex:
            print("portal_menu_dashboard_validation_by_xpath : ", ex)

    def copyright_btn_by_xpath(self):
        try:
            copyright_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "copyright_btn_by_xpath")
            return copyright_btn_by_xpath
        except Exception as ex:
            print("copyright_btn_by_xpath : ", ex)

    def copyright_validation_by_xpath(self):
        try:
            copyright_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                            "copyright_validation_by_xpath")
            return copyright_validation_by_xpath
        except Exception as ex:
            print("copyright_validation_by_xpath : ", ex)

    def profile_btn_by_xpath(self):
        try:
            profile_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "profile_btn_by_xpath")
            return profile_btn_by_xpath
        except Exception as ex:
            print("profile_btn_by_xpath : ", ex)

    def profile_validation_by_xpath(self):
        try:
            profile_validation_by_xpath = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                          "profile_validation_by_xpath")
            return profile_validation_by_xpath
        except Exception as ex:
            print("profile_validation_by_xpath : ", ex)

    def logout_btn_by_xpath(self):
        try:
            logout_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "logout_btn_by_xpath")
            return logout_btn_by_xpath
        except Exception as ex:
            print("copyright_btn_by_xpath : ", ex)

    def logout_validation_by_xpath(self):
        try:
            logout_validation_by_xpath = self.config.get("LOCATORS", "portal_login_page_usernameField_by_xpath")
            return logout_validation_by_xpath
        except Exception as ex:
            print("logout_validation_by_xpath : ", ex)

    def user_profile_action_btn_by_xpath(self):
        try:
            user_profile_action_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS",
                                                               "user_profile_action_btn_by_xpath")
            return user_profile_action_btn_by_xpath
        except Exception as ex:
            print("user_profile_action_btn_by_xpath : ", ex)

    def user_profile_edit_btn_by_xpath(self):
        try:
            user_profile_edit_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "profile_edit_btn_by_xpath")
            return user_profile_edit_btn_by_xpath
        except Exception as ex:
            print("user_profile_edit_btn_by_xpath : ", ex)

    def current_password_filed_by_xpath(self):
        try:
            current_password_filed_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS",
                                                              "current_password_field_by_xpath")
            return current_password_filed_by_xpath
        except Exception as ex:
            print("current_password_filed_by_xpath : ", ex)

    def new_password_filed_by_xpath(self):
        try:
            new_password_filed_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "new_password_field_by_xpath")
            return new_password_filed_by_xpath
        except Exception as ex:
            print("new_password_filed_by_xpath : ", ex)

    def confirm_password_filed_by_xpath(self):
        try:
            confirm_password_filed_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS",
                                                              "confirm_new_password_by_xpath")
            return confirm_password_filed_by_xpath
        except Exception as ex:
            print("confirm_password_filed_by_xpath : ", ex)

    def new_password(self):
        try:
            new_password = self.config.get("PORTAL_LOGIN_PAGE_DATA", "new_password")
            return new_password
        except Exception as ex:
            print("new_password : ", ex)

    def confirm_new_password(self):
        try:
            confirm_new_password = self.config.get("PORTAL_LOGIN_PAGE_DATA", "confirm_new_password")
            return confirm_new_password
        except Exception as ex:
            print("confirm_new_password : ", ex)

    def save_new_password(self):
        try:
            save_new_password = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "save_new_password")
            return save_new_password
        except Exception as ex:
            print("save_new_password : ", ex)

    def password_change_validation(self):
        try:
            password_change_validation = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                         "password_change_validation")
            return password_change_validation
        except Exception as ex:
            print("password_change_validation : ", ex)

    def rest_password_first_name_input(self):
        try:
            rest_password_first_name_input = self.config.get("PORTAL_MENU_BUTTON_LOCATORS",
                                                             "rest_password_first_name_input")
            return rest_password_first_name_input
        except Exception as ex:
            print("rest_password_first_name_input : ", ex)

    def rest_password_last_name_input(self):
        try:
            rest_password_last_name_input = self.config.get("PORTAL_MENU_BUTTON_LOCATORS",
                                                            "rest_password_last_name_input")
            return rest_password_last_name_input
        except Exception as ex:
            print("rest_password_last_name_input : ", ex)

    def portal_menu_closed_all_btn_by_xpath(self):
        try:
            closed_all_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "closeAll_btn_by_xpath")
            return closed_all_btn_by_xpath
        except Exception as ex:
            print("portal_menu_closed_all_btn_by_xpath : ", ex)

    def portal_menu_cloud_menu_btn_by_xpath(self):
        try:
            cloud_menu_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "cloud_menu_btn_by_xpath")
            return cloud_menu_btn_by_xpath
        except Exception as ex:
            print("portal_menu_cloud_menu_btn_by_xpath : ", ex)

    def portal_menu_close_notifier_btn_by_xpath(self):
        try:
            close_notifier_btn_by_xpath = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "closed_notifier_btn_xpath")
            return close_notifier_btn_by_xpath
        except Exception as ex:
            print("portal_menu_closed_notifier_btn_by_xpath : ", ex)

    def portal_menu_copyright_expected_text(self):
        try:
            portal_menu_copyright_expected_text = self.config.get("ASSERTIONS", "copyright_expected_text")
            return portal_menu_copyright_expected_text
        except Exception as ex:
            print("portal_menu_copyright_expected_text : ", ex)

    def current_and_new_password_not_same_validation(self):
        try:
            current_and_new_password_not_same_validation = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                           "current_and_new_password_not_same")
            return current_and_new_password_not_same_validation
        except Exception as ex:
            print("current_and_new_password_not_same_validation : ", ex)

    def user_panel_cancel_btn(self):
        try:
            user_panel_cancel_btn = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "user_panel_cancel_btn")
            return user_panel_cancel_btn
        except Exception as ex:
            print("user_panel_cancel_btn : ", ex)

    def user_panel_close_btn(self):
        try:
            user_panel_close_btn = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "user_panel_close_btn")
            return user_panel_close_btn
        except Exception as ex:
            print("user_panel_close_btn : ", ex)

    def get_upper_case_password(self):
        try:
            get_upper_case_password = self.config.get("PORTAL_LOGIN_PAGE_DATA", "upper_case_password")
            return get_upper_case_password
        except Exception as ex:
            print("get_upper_case_password : ", ex)

    def get_lower_case_password(self):
        try:
            get_lower_case_password = self.config.get("PORTAL_LOGIN_PAGE_DATA", "lower_case_password")
            return get_lower_case_password
        except Exception as ex:
            print("get_lower_case_password : ", ex)

    def get_special_character_password(self):
        try:
            get_special_character_password = self.config.get("PORTAL_LOGIN_PAGE_DATA", "special_character_password")
            return get_special_character_password
        except Exception as ex:
            print("get_special_character_password : ", ex)

    def get_less_than_eight_character_password(self):
        try:
            get_less_than_eight_character_password = self.config.get("PORTAL_LOGIN_PAGE_DATA",
                                                                     "less_than_eight_character")
            return get_less_than_eight_character_password
        except Exception as ex:
            print("get_less_than_eight_character_password : ", ex)

    def less_than_eight_character_validation_password(self):
        try:
            less_than_eight_character_validation_password = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                            "password_less_than_eight_validation")
            return less_than_eight_character_validation_password
        except Exception as ex:
            print("less_than_eight_character_validation_password : ", ex)

    def event_panel_validation_text(self):
        try:
            event_panel_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                          "event_panel_validation_text")
            return event_panel_validation_text
        except Exception as ex:
            print("event_panel_validation_text : ", ex)

    def tags_panel_validation_text(self):
        try:
            tags_panel_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                         "tags_panel_validation_text")
            return tags_panel_validation_text
        except Exception as ex:
            print("tags_panel_validation_text : ", ex)

    def identify_and_enroll_panel_validation_text(self):
        try:
            identify_and_enroll_panel_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                        "identify_and_enroll_panel_validation_text")
            return identify_and_enroll_panel_validation_text
        except Exception as ex:
            print("identify_and_enroll_panel_validation_text : ", ex)

    def detect_faces_validation_text(self):
        try:
            detect_faces_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                           "detect_faces_validation_text")
            return detect_faces_validation_text
        except Exception as ex:
            print("detect_faces_validation_text : ", ex)

    def enrollments_panel_validation_text(self):
        try:
            enrollments_panel_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                "enrollments_panel_validation_text")
            return enrollments_panel_validation_text
        except Exception as ex:
            print("enrollments_panel_validation_text : ", ex)

    def enrollments_groups_panel_validation_text(self):
        try:
            enrollments_groups_panel_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                       "enrollments_groups_panel_validation_text")
            return enrollments_groups_panel_validation_text
        except Exception as ex:
            print("enrollments_groups_panel_validation_text : ", ex)

    def visitors_panel_validation_text(self):
        try:
            visitors_panel_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                             "visitors_panel_validation_text")
            return visitors_panel_validation_text
        except Exception as ex:
            print("visitors_panel_validation_text : ", ex)

    def visitor_search_panel_validation_text(self):
        try:
            visitor_search_panel_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                   "visitor_search_panel_validation_text")
            return visitor_search_panel_validation_text
        except Exception as ex:
            print("visitor_search_panel_validation_text : ", ex)

    def close_all_panel_list(self):
        try:
            close_all_panel_list = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "close_all_panel_list")
            return close_all_panel_list
        except Exception as ex:
            print("close_all_panel_list : ", ex)

    def notification_groups_panel_validation_text(self):
        try:
            notification_groups_panel_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                        "notification_groups_panel_validation_text")
            return notification_groups_panel_validation_text
        except Exception as ex:
            print("notification_groups_panel_validation_text : ", ex)

    def visitor_search_jobs_panel_text(self):
        try:
            visitor_search_jobs_panel_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                             "visitor_search_jobs_panel_text")
            return visitor_search_jobs_panel_text
        except Exception as ex:
            print("visitor_search_jobs_panel_text : ", ex)

    def notes_panel_validation_text(self):
        try:
            notes_panel_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                          "notes_panel_validation_text")
            return notes_panel_validation_text
        except Exception as ex:
            print("notes_panel_validation_text : ", ex)

    def locations_panel_validation_text(self):
        try:
            locations_panel_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                              "locations_panel_validation_text")
            return locations_panel_validation_text
        except Exception as ex:
            print("locations_panel_validation_text : ", ex)

    def user_panel_validation_text(self):
        try:
            user_panel_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                         "user_panel_validation_text")
            return user_panel_validation_text
        except Exception as ex:
            print("user_panel_validation_text : ", ex)

    def user_roles_validation_text(self):
        try:
            user_roles_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                         "user_roles_validation_text")
            return user_roles_validation_text
        except Exception as ex:
            print("user_roles_validation_text : ", ex)

    def zones_panel_validation_text(self):
        try:
            zones_panel_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                          "zones_panel_validation_text")
            return zones_panel_validation_text
        except Exception as ex:
            print("zones_panel_validation_text : ", ex)

    def account_panel_validation_text(self):
        try:
            account_panel_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                            "account_panel_validation_text")
            return account_panel_validation_text
        except Exception as ex:
            print("account_panel_validation_text : ", ex)

    def reporting_validation_text(self):
        try:
            reporting_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS", "reporting_validation_text")
            return reporting_validation_text
        except Exception as ex:
            print("reporting_validation_text : ", ex)

    def dashboard_panel_validation_text(self):
        try:
            dashboard_panel_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                              "dashboard_panel_validation_text")
            return dashboard_panel_validation_text
        except Exception as ex:
            print("dashboard_panel_validation_text : ", ex)

    def notifier_panel_validation_text(self):
        try:
            notifier_panel_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                             "notifier_panel_validation_text")
            return notifier_panel_validation_text
        except Exception as ex:
            print("notifier_panel_validation_text : ", ex)

    def validation_user_panel_text(self):
        try:
            validation_user_panel_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                         "validation_user_panel_text")
            return validation_user_panel_text
        except Exception as ex:
            print("validation_user_panel_text : ", ex)

    def copyright_version_text_validation(self):
        try:
            copyright_version_text_validation = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                "copyright_version_text_validation")
            return copyright_version_text_validation
        except Exception as ex:
            print("copyright_version_text_validation : ", ex)

    def copyright_year_text_validation(self):
        try:
            copyright_year_text_validation = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                             "copyright_year_text_validation")
            return copyright_year_text_validation
        except Exception as ex:
            print("copyright_year_text_validation : ", ex)

    def first_name(self):
        try:
            first_name = self.config.get("PORTAL_LOGIN_PAGE_DATA", "first_name")
            return first_name
        except Exception as ex:
            print("first_name : ", ex)

    def last_name(self):
        try:
            last_name = self.config.get("PORTAL_LOGIN_PAGE_DATA", "last_name")
            return last_name
        except Exception as ex:
            print("last_name : ", ex)

    def close_all_panel_expected_text(self):
        try:
            close_all_panel_expected_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                            "close_all_panel_expected_text")
            return close_all_panel_expected_text
        except Exception as ex:
            print("close_all_panel_expected_text : ", ex)

    def logout_button_expected_text(self):
        try:
            logout_button_expected_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                          "logout_button_expected_text")
            return logout_button_expected_text
        except Exception as ex:
            print("logout_button_expected_text : ", ex)

    def reset_password_first_name_validation(self):
        try:
            reset_password_first_name_validation = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                   "reset_password_first_name_validation")
            return reset_password_first_name_validation
        except Exception as ex:
            print("reset_password_first_name_validation : ", ex)

    def reset_password_last_name_validation(self):
        try:
            reset_password_last_name_validation = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                  "reset_password_last_name_validation")
            return reset_password_last_name_validation
        except Exception as ex:
            print("reset_password_last_name_validation : ", ex)

    def first_and_last_name_required_validation(self):
        try:
            first_and_last_name_required_validation = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                      "first_and_last_name_required_validation")
            return first_and_last_name_required_validation
        except Exception as ex:
            print("first_and_last_name_required_validation : ", ex)

    def rest_password_success_msg_validation_text(self):
        try:
            rest_password_success_msg_validation_text = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                        "rest_password_success_msg_validation_text")
            return rest_password_success_msg_validation_text
        except Exception as ex:
            print("rest_password_success_msg_validation_text : ", ex)

    def current_psw_and_new_psw_not_same_validation(self):
        try:
            current_psw_and_new_psw_not_same_validation = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                          "current_psw_and_new_psw_not_same_validation")
            return current_psw_and_new_psw_not_same_validation
        except Exception as ex:
            print("current_psw_and_new_psw_not_same_validation : ", ex)

    def less_than_eight_char_password_validation(self):
        try:
            less_than_eight_char_password_validation = self.config.get("Portal_Menu_Validation_LOCATORS",
                                                                       "less_than_eight_char_password_validation")
            return less_than_eight_char_password_validation
        except Exception as ex:
            print("less_than_eight_char_password_validation : ", ex)

    def audit_log_reports_btn_xpath(self):
        try:
            ele = self.config.get("PORTAL_MENU_BUTTON_LOCATORS",
                                  "audit_log_reports")
            return ele
        except Exception as ex:
            print(" audit_log_reports_btn_xpath : ", ex)

    def audit_log_reports_validation(self):
        try:
            ele = self.config.get("Portal_Menu_Validation_LOCATORS", "audit_log_report_btn_validation")
            return ele
        except Exception as ex:
            print("audit_log_report_btn_validation : ", ex)

    def location_cancel_button(self):
        try:
            ele = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "location_cancel_button")
            return ele
        except Exception as ex:
            print("location_cancel_button : ", ex)

    def notifier_close_button(self):
        try:
            ele = self.config.get("PORTAL_MENU_BUTTON_LOCATORS", "notifier_close_button")
            return ele
        except Exception as ex:
            print("notifier_close_button : ", ex)
