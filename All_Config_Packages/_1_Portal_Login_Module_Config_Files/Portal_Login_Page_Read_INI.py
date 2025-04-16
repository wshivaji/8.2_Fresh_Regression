import configparser
from pathlib import Path

file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\1_Portal_Login_Module\\Data_From_INI\\Portal_Login_Page.ini"
print("configure filepath: ", file_path)
common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"


class Portal_login_page_read_ini:
    def __init__(self):
        self.config = configparser.RawConfigParser()

        self.common_test_data_config = configparser.RawConfigParser()
        self.common_test_data_config.read(common_test_data_ini_file_path)
        try:
            self.config.read(file_path)
        except Exception as ex:
            print(ex)

    def get_portal_url(self):
        try:
            portal_url = self.common_test_data_config.get("Login_Logout_Data", "cloud_login_url")
            print("portal page url: ", portal_url)
            return portal_url
        except Exception as ex:
            print(ex)

    def get_portal_title(self):
        try:
            portal_title = self.common_test_data_config.get("Login_Logout_Data", "portal_title")
            print("portal title: ", portal_title)
            return portal_title
        except Exception as ex:
            print(ex)

    def get_advance_btn_by_xpath(self):
        try:
            advance_btn_by_xpath = self.common_test_data_config.get("Login_Logout_Data", "advance_btn_by_xpath")
            print("portal title: ", advance_btn_by_xpath)
            return advance_btn_by_xpath
        except Exception as ex:
            print(ex)

    def get_proceed_link_by_xpath(self):
        try:
            proceed_link_by_xpath = self.common_test_data_config.get("Login_Logout_Data", "proceed_link_by_xpath")
            print("portal title: ", proceed_link_by_xpath)
            return proceed_link_by_xpath
        except Exception as ex:
            print(ex)

    def get_face_first_company_logo_by_xpath(self):
        try:
            face_first_company_logo = self.config.get("Portal_Login_Page", "face_first_company_logo_by_xpath")
            print("face first logo on portal login page: ", face_first_company_logo)
            return face_first_company_logo
        except Exception as ex:
            print(ex)

    def get_dashboard_menu_by_xpath(self):
        try:
            dashboard_menu_by_xpath = self.config.get("Portal_Login_Page", "dashboard_menu_by_xpath")
            print("dashboard menu: ", dashboard_menu_by_xpath)
            return dashboard_menu_by_xpath
        except Exception as ex:
            print(ex)

    def get_portal_login_username_textbox_by_xpath(self):
        try:
            portal_login_username_texbox = self.config.get("Portal_Login_Page",
                                                           "portal_login_username_textbox_by_xpath")
            print("portal username textbox: ", portal_login_username_texbox)
            return portal_login_username_texbox
        except Exception as ex:
            print(ex)

    def get_portal_username_label_on_username_textbox(self):
        try:
            portal_username_label_on_username_textbox = \
                self.common_test_data_config.get("Portal_Login_module_data", "portal_username_label_on_username_textbox")
            print("username label on username textbox: ", portal_username_label_on_username_textbox)
            return portal_username_label_on_username_textbox
        except Exception as ex:
            print(ex)

    def get_valid_login_username(self):
        try:
            valid_login_username = self.common_test_data_config.get("Login_Logout_Data", "username")
            print("username: ", valid_login_username)
            return valid_login_username
        except Exception as ex:
            print(ex)

    def get_portal_login_username(self):
        try:
            portal_login_username = self.common_test_data_config.get("Login_Logout_Data", "username")
            print("username: ", portal_login_username)
            return portal_login_username
        except Exception as ex:
            print(ex)

    def get_portal_login_invalid_username(self):
        try:
            portal_login_invalid_username = self.common_test_data_config.get("Portal_Login_module_data", "portal_login_invalid_username")
            print("invalid username: ", portal_login_invalid_username)
            return portal_login_invalid_username
        except Exception as ex:
            print(ex)

    def get_expected_missing_username_error_text(self):
        try:
            expected_missing_username_error_text = self.common_test_data_config.get("Portal_Login_module_data", "expected_missing_username_error_text")
            print("missing username: ", expected_missing_username_error_text)
            return expected_missing_username_error_text
        except Exception as ex:
            print(ex)

    def get_expected_missing_password_error_text(self):
        try:
            expected_missing_password_error_text = self.common_test_data_config.get("Portal_Login_module_data", "expected_missing_password_error_text")
            print("missing password: ", expected_missing_password_error_text)
            return expected_missing_password_error_text
        except Exception as ex:
            print(ex)

    def get_portal_login_invalid_password(self):
        try:
            portal_login_invalid_password = self.common_test_data_config.get("Portal_Login_module_data", "portal_login_invalid_password")
            print("invalid password: ", portal_login_invalid_password)
            return portal_login_invalid_password
        except Exception as ex:
            print(ex)

    def get_portal_password_label_on_password_textbox(self):
        try:
            portal_password_label_on_password_textbox = self.common_test_data_config.get("Portal_Login_module_data", "portal_password_label_on_password_textbox")
            print("password label on password textbox: ", portal_password_label_on_password_textbox)
            return portal_password_label_on_password_textbox
        except Exception as ex:
            print(ex)

    def get_portal_login_password_textbox_by_xpath(self):
        try:
            portal_login_password_textbox = self.config.get("Portal_Login_Page", "portal_login_password_textbox_by_xpath")
            print("portal password textbox: ", portal_login_password_textbox)
            return portal_login_password_textbox
        except Exception as ex:
            print(ex)

    def get_portal_login_password(self):
        try:
            portal_login_password = self.common_test_data_config.get("Login_Logout_Data", "password")
            print("password: ", portal_login_password)
            return portal_login_password
        except Exception as ex:
            print(ex)

    def get_cloud_menu_on_dashboard_by_xpath(self):
        try:
            dashboard_menu_container = self.config.get("Portal_Login_Page", "cloud_menu_on_dashboard_by_xpath")
            print("dashboard menu container: ", dashboard_menu_container)
            return dashboard_menu_container
        except Exception as ex:
            print(ex)

    def get_cloud_login_button_on_portal_by_xpath(self):
        try:
            cloud_login_button_on_portal = self.config.get("Portal_Login_Page", "cloud_login_button_on_portal_by_xpath")
            print("cloud login button on portal: ", cloud_login_button_on_portal)
            return cloud_login_button_on_portal
        except Exception as ex:
            print(ex)

    def get_cloud_text_on_cloud_login_button_by_xpath(self):
        try:
            cloud_text_on_cloud_login_button = self.config.get("Portal_Login_Page", "cloud_text_on_cloud_login_button_by_xpath")
            print("cloud text on cloud login button: ", cloud_text_on_cloud_login_button)
            return cloud_text_on_cloud_login_button
        except Exception as ex:
            print(ex)

    def get_expected_cloud_text_on_button(self):
        try:
            expected_cloud_text_on_button = self.common_test_data_config.get("Portal_Login_module_data", "cloud_text_on_button")
            print("expected cloud text on button: ", expected_cloud_text_on_button)
            return expected_cloud_text_on_button
        except Exception as ex:
            print(ex)

    def get_login_text_on_cloud_login_button_by_xpath(self):
        try:
            login_text_on_cloud_login_button = self.config.get("Portal_Login_Page", "login_text_on_cloud_login_button_by_xpath")
            print("login text on cloud login button: ", login_text_on_cloud_login_button)
            return login_text_on_cloud_login_button
        except Exception as ex:
            print(ex)

    def get_expected_login_text_on_button(self):
        try:
            expected_login_text_on_button = self.common_test_data_config.get("Portal_Login_module_data", "login_text_on_button")
            print("expected login text on button: ", expected_login_text_on_button)
            return expected_login_text_on_button
        except Exception as ex:
            print(ex)

    def get_local_menu_button_by_xpath(self):
        try:
            local_menu_button = self.config.get("Portal_Login_Page", "local_menu_button_by_xpath")
            print("local menu button: ", local_menu_button)
            return local_menu_button
        except Exception as ex:
            print(ex)

    def get_current_user_info_by_xpath(self):
        try:
            current_user_info = self.config.get("Portal_Login_Page", "current_user_info_by_xpath")
            print("current user info: ", current_user_info)
            return current_user_info
        except Exception as ex:
            print(ex)

    def get_events_button_on_portal_by_xpath(self):
        try:
            events_button_on_portal = self.config.get("Portal_Login_Page", "events_button_on_portal_by_xpath")
            print("events button on portal: ", events_button_on_portal)
            return events_button_on_portal
        except Exception as ex:
            print(ex)

    def get_exclamation_mark_icon_on_events_button_by_xpath(self):
        try:
            exclamation_mark_icon_on_events_button = self.config.get("Portal_Login_Page", "exclamation_mark_icon_on_events_button_by_xpath")
            print("exclamation mark on events button: ", exclamation_mark_icon_on_events_button)
            return exclamation_mark_icon_on_events_button
        except Exception as ex:
            print(ex)

    def get_events_text_on_events_button_by_xpath(self):
        try:
            events_text_on_events_button = self.config.get("Portal_Login_Page", "events_text_on_events_button_by_xpath")
            print("events text on events button: ", events_text_on_events_button)
            return events_text_on_events_button
        except Exception as ex:
            print(ex)

    def get_events_heading_on_events_panel_by_xpath(self):
        try:
            events_heading_on_events_panel = self.config.get("Portal_Login_Page", "events_heading_on_events_panel_by_xpath")
            print("events heading on events panel: ", events_heading_on_events_panel)
            return events_heading_on_events_panel
        except Exception as ex:
            print(ex)

    def get_expected_text_events_on_button(self):
        try:
            expected_text_events_on_button = self.common_test_data_config.get("Portal_Login_module_data", "events_text_on_button")
            print("expected text on events button: ", expected_text_events_on_button)
            return expected_text_events_on_button
        except Exception as ex:
            print(ex)

    def get_identify_enroll_button_by_xpath(self):
        try:
            identify_enroll_button = self.config.get("Portal_Login_Page", "identify_enroll_button_by_xpath")
            print("identify & enroll button: ", identify_enroll_button)
            return identify_enroll_button
        except Exception as ex:
            print(ex)

    def get_camera_icon_on_identify_enroll_button_by_xpath(self):
        try:
            camera_icon_on_identify_enroll_button = self.config.get("Portal_Login_Page", "camera_icon_on_identify_enroll_button_by_xpath")
            print("camera icon on identify enroll button: ", camera_icon_on_identify_enroll_button)
            return camera_icon_on_identify_enroll_button
        except Exception as ex:
            print(ex)

    def get_identify_enroll_text_on_identify_enroll_button_by_xpath(self):
        try:
            identify_enroll_text_on_identify_enroll_button = self.config.get("Portal_Login_Page", "identify_enroll_text_on_identify_enroll_button_by_xpath")
            print("identify & enroll text on button: ", identify_enroll_text_on_identify_enroll_button)
            return identify_enroll_text_on_identify_enroll_button
        except Exception as ex:
            print(ex)

    def get_expected_text_on_identify_enroll_button(self):
        try:
            expected_text_on_identify_enroll_button = self.common_test_data_config.get("Portal_Login_module_data", "identify_enroll_text_on_button")
            print("expected text on identify enroll :", expected_text_on_identify_enroll_button)
            return expected_text_on_identify_enroll_button
        except Exception as ex:
            print(ex)

    def get_identify_enroll_panel_heading_by_xpath(self):
        try:
            identify_enroll_panel_heading = self.config.get("Portal_Login_Page", "identify_enroll_panel_heading_by_xpath")
            print("heading on identify & enroll: ", identify_enroll_panel_heading)
            return identify_enroll_panel_heading
        except Exception as ex:
            print(ex)

    def get_users_button_by_xpath(self):
        try:
            users_button = self.config.get("Portal_Login_Page", "users_button_by_xpath")
            print("users button: ", users_button)
            return users_button
        except Exception as ex:
            print(ex)

    def get_male_icon_on_users_button_by_xpath(self):
        try:
            male_icon_on_users_button = self.config.get("Portal_Login_Page", "male_icon_on_users_button_by_xpath")
            print("male icon on users button: ", male_icon_on_users_button)
            return male_icon_on_users_button
        except Exception as ex:
            print(ex)

    def get_users_text_on_users_button_by_xpath(self):
        try:
            users_text_on_users_button = self.config.get("Portal_Login_Page", "users_text_on_users_button_by_xpath")
            print("users text on users button: ", users_text_on_users_button)
            return users_text_on_users_button
        except Exception as ex:
            print(ex)

    def get_expected_text_on_users_button(self):
        try:
            users_text_on_button = self.common_test_data_config.get("Portal_Login_module_data", "users_text_on_button")
            print("expected text on users button: ", users_text_on_button)
            return users_text_on_button
        except Exception as ex:
            print(ex)

    def get_users_heading_on_panel_by_xpath(self):
        try:
            users_heading_on_panel = self.config.get("Portal_Login_Page", "users_heading_on_panel_by_xpath")
            print("heading on users panel: ", users_heading_on_panel)
            return users_heading_on_panel
        except Exception as ex:
            print(ex)

    def get_account_button_by_xpath(self):
        try:
            account_button = self.config.get("Portal_Login_Page", "account_button_by_xpath")
            print("account button: ", account_button)
            return account_button
        except Exception as ex:
            print(ex)

    def get_lock_icon_on_account_button_by_xpath(self):
        try:
            lock_icon_on_account_button = self.config.get("Portal_Login_Page", "lock_icon_on_account_button_by_xpath")
            print("lock icon on account button: ", lock_icon_on_account_button)
            return lock_icon_on_account_button
        except Exception as ex:
            print(ex)

    def get_account_text_on_account_button_by_xpath(self):
        try:
            account_text_on_account_button = self.config.get("Portal_Login_Page", "account_text_on_account_button_by_xpath")
            print("account text on account button: ", account_text_on_account_button)
            return account_text_on_account_button
        except Exception as ex:
            print(ex)

    def get_expected_text_on_account_button(self):
        try:
            account_text_on_button = self.common_test_data_config.get("Portal_Login_module_data", "account_text_on_button")
            print("expected text on users button: ", account_text_on_button)
            return account_text_on_button
        except Exception as ex:
            print(ex)

    def get_account_heading_on_account_panel_by_xpath(self):
        try:
            account_heading_on_account_panel = self.config.get("Portal_Login_Page", "account_heading_on_account_panel_by_xpath")
            print("heading on account panel: ", account_heading_on_account_panel)
            return account_heading_on_account_panel
        except Exception as ex:
            print(ex)

    def get_switch_language_button_by_xpath(self):
        try:
            switch_language_button = self.config.get("Portal_Login_Page", "switch_language_button_by_xpath")
            print("switch language button: ", switch_language_button)
            return switch_language_button
        except Exception as ex:
            print(ex)

    def get_switch_language_text_on_switch_language_button_by_xpath(self):
        try:
            switch_language_text_on_switch_language_button = self.config.get("Portal_Login_Page", "switch_language_text_on_switch_language_button_by_xpath")
            print("actual switch language text on button: ", switch_language_text_on_switch_language_button)
            return switch_language_text_on_switch_language_button
        except Exception as ex:
            print(ex)

    def get_expected_switch_language_text_in_portuguese(self):
        try:
            switch_language_text_in_portuguese = self.common_test_data_config.get("Portal_Login_module_data", "switch_language_text_in_portuguese")
            print("expected text in portuguese: ", switch_language_text_in_portuguese)
            return switch_language_text_in_portuguese
        except Exception as ex:
            print(ex)

    def get_expected_switch_language_text_in_spanish(self):
        try:
            switch_language_text_in_spanish = self.common_test_data_config.get("Portal_Login_module_data", "switch_language_text_in_spanish")
            print("expected text in spanish: ", switch_language_text_in_spanish)
            return switch_language_text_in_spanish
        except Exception as ex:
            print(ex)

    def get_expected_switch_language_text_in_arabic(self):
        try:
            switch_language_text_in_arabic = self.common_test_data_config.get("Portal_Login_module_data", "switch_language_text_in_arabic")
            print("expected text in arabic: ", switch_language_text_in_arabic)
            return switch_language_text_in_arabic
        except Exception as ex:
            print(ex)

    def get_expected_text_on_switch_language_button(self):
        try:
            switch_language_text_on_button = self.common_test_data_config.get("Portal_Login_module_data", "switch_language_text_on_button")
            print("expected text on switch language button: ", switch_language_text_on_button)
            return switch_language_text_on_button
        except Exception as ex:
            print(ex)

    def get_expected_heading_of_switch_language_dialog_box(self):
        try:
            heading_on_switch_language_dialog_box = self.common_test_data_config.get("Portal_Login_module_data", "SWITCH_LANGUAGE_heading_on_dialog_box")
            print("heading on switch language dialog box:", heading_on_switch_language_dialog_box)
            return heading_on_switch_language_dialog_box
        except Exception as ex:
            print(ex)

    def get_switch_language_dialog_box_heading_by_xpath(self):
        try:
            switch_language_dialog_box_heading_by_xpath = self.config.get("Portal_Login_Page", "switch_language_dialog_box_heading_by_xpath")
            print("actual heading on switch language dialog box: ", switch_language_dialog_box_heading_by_xpath)
            return switch_language_dialog_box_heading_by_xpath
        except Exception as ex:
            print(ex)

    def get_english_language(self):
        try:
            english_language = self.common_test_data_config.get("Portal_Login_module_data", "english_language")
            print("english: ", english_language)
            return english_language
        except Exception as ex:
            print(ex)

    def get_english_language_on_dialog_box_by_xpath(self):
        try:
            english_language_on_dialog_box = self.config.get("Portal_Login_Page", "english_language_on_dialog_box_by_xpath")
            print("english language on dialog box :", english_language_on_dialog_box)
            return english_language_on_dialog_box
        except Exception as ex:
            print(ex)

    def get_english_radio_button_by_xpath(self):
        try:
            english_radio_button = self.config.get("Portal_Login_Page", "english_radio_button_by_xpath")
            print("english radio button: ", english_radio_button)
            return english_radio_button
        except Exception as ex:
            print(ex)

    def get_spanish_language(self):
        try:
            spanish_language = self.common_test_data_config.get("Portal_Login_module_data", "spanish_language")
            print("spanish: ", spanish_language)
            return spanish_language
        except Exception as ex:
            print(ex)

    def get_spanish_language_on_dialog_box_by_xpath(self):
        try:
            spanish_language_on_dialog_box = self.config.get("Portal_Login_Page", "spanish_language_on_dialog_box_by_xpath")
            print("spanish language on dialog box: ", spanish_language_on_dialog_box)
            return spanish_language_on_dialog_box
        except Exception as ex:
            print(ex)

    def get_spanish_radio_button_by_xpath(self):
        try:
            spanish_radio_button = self.config.get("Portal_Login_Page", "spanish_radio_button_by_xpath")
            print("spanish radio button: ", spanish_radio_button)
            return spanish_radio_button
        except Exception as ex:
            print(ex)

    def get_arabic_language(self):
        try:
            arabic_language = self.common_test_data_config.get("Portal_Login_module_data", "arabic_language")
            print("arabic: ", arabic_language)
            return arabic_language
        except Exception as ex:
            print(ex)

    def get_arabic_language_on_dialog_box_by_xpath(self):
        try:
            arabic_language_on_dialog_box = self.config.get("Portal_Login_Page", "arabic_language_on_dialog_box_by_xpath")
            print("arabic language on dialog box: ", arabic_language_on_dialog_box)
            return arabic_language_on_dialog_box
        except Exception as ex:
            print(ex)

    def get_arabic_radio_button_by_xpath(self):
        try:
            arabic_radio_button = self.config.get("Portal_Login_Page", "arabic_radio_button_by_xpath")
            print("arabic radio button: ", arabic_radio_button)
            return arabic_radio_button
        except Exception as ex:
            print(ex)

    def get_portuguese_language(self):
        try:
            portuguese_language = self.common_test_data_config.get("Portal_Login_module_data", "portuguese_language")
            print("portuguese: ", portuguese_language)
            return portuguese_language
        except Exception as ex:
            print(ex)

    def get_portuguese_language_on_dialog_box_by_xpath(self):
        try:
            portuguese_language_on_dialog_box = self.config.get("Portal_Login_Page", "portuguese_language_on_dialog_box_by_xpath")
            print("portuguese language on dialog box: ", portuguese_language_on_dialog_box)
            return portuguese_language_on_dialog_box
        except Exception as ex:
            print(ex)

    def get_portuguese_radio_button_by_xpath(self):
        try:
            portuguese_radio_button = self.config.get("Portal_Login_Page", "portuguese_radio_button_by_xpath")
            print("portuguese radio button: ", portuguese_radio_button)
            return portuguese_radio_button
        except Exception as ex:
            print(ex)

    def get_cancel_button_on_switch_language_dialog_box_by_xpath(self):
        try:
            cancel_button_on_switch_language_dialog_box = self.config.get("Portal_Login_Page", "cancel_button_on_switch_language_dialog_box_by_xpath")
            print("cancel button on switch language dialog box: ", cancel_button_on_switch_language_dialog_box)
            return cancel_button_on_switch_language_dialog_box
        except Exception as ex:
            print(ex)

    def get_expected_text_on_cancel_button(self):
        try:
            cancel_text_on_cancel_button = self.common_test_data_config.get("Portal_Login_module_data", "cancel_text_on_cancel_button")
            print("expected text an cancel button: ", cancel_text_on_cancel_button)
            return cancel_text_on_cancel_button
        except Exception as ex:
            print(ex)

    def get_face_first_copyright_text_by_xpath(self):
        try:
            face_first_copyright_text = self.config.get("Portal_Login_Page", "face_first_copyright_text_by_xpath")
            print("face first copyright text: ", face_first_copyright_text)
            return face_first_copyright_text
        except Exception as ex:
            print(ex)

    def get_expected_copyright_text(self):
        try:
            expected_copyright_text = self.common_test_data_config.get("Portal_Login_module_data", "copyright_text")
            print("expected copyright text: ", expected_copyright_text)
            return expected_copyright_text
        except Exception as ex:
            print(ex)

    def get_copyright_on_display_version_page(self):
        try:
            copyright_on_display_version_page = self.config.get("Portal_Login_Page", "copyright_on_display_version_page_by_xpath")
            print("copyright on version display page: ", copyright_on_display_version_page)
            return copyright_on_display_version_page
        except Exception as ex:
            print(ex)

    def get_WebAPI_text_on_version_info_by_xpath(self):
        try:
            WebAPI_text_on_version_info = self.config.get("Portal_Login_Page", "WebAPI_text_on_version_info_by_xpath")
            print("webapi text on version info: ", WebAPI_text_on_version_info)
            return WebAPI_text_on_version_info
        except Exception as ex:
            print(ex)

    def get_expected_webapi_text_on_version_info(self):
        try:
            webapi_text_on_version_info = self.common_test_data_config.get("Portal_Login_module_data", "webapi_text_on_version_info")
            print("expected webapi text on version info: ", webapi_text_on_version_info)
            return webapi_text_on_version_info
        except Exception as ex:
            print(ex)

    def get_Server_text_on_version_info_by_xpath(self):
        try:
            Server_text_on_version_info = self.config.get("Portal_Login_Page", "Server_text_on_version_info_by_xpath")
            print("server text on version info: ", Server_text_on_version_info)
            return Server_text_on_version_info
        except Exception as ex:
            print(ex)

    def get_expected_server_text_on_version_info(self):
        try:
            server_text_on_version_info = self.common_test_data_config.get("Portal_Login_module_data", "server_text_on_version_info")
            print("expected server text on version info: ", server_text_on_version_info)
            return server_text_on_version_info
        except Exception as ex:
            print(ex)

    def get_webapi_version_info_by_xpath(self):
        try:
            webapi_version_info = self.config.get("Portal_Login_Page", "webapi_version_info_by_xpath")
            print("webapi version info: ", webapi_version_info)
            return webapi_version_info
        except Exception as ex:
            print(ex)

    def get_expected_webapi_version_number(self):
        try:
            webapi_version_number = self.common_test_data_config.get("Portal_Login_Page_Data", "webapi_version_number")
            print("expected webapi version number: ", webapi_version_number)
            return webapi_version_number
        except Exception as ex:
            print(ex)

    def get_portal_version_number_by_xpath(self):
        try:
            actual_portal_version_number = self.config.get("Portal_Login_Page", "portal_version_number_by_xpath")
            print("portal version number: ", actual_portal_version_number)
            return actual_portal_version_number
        except Exception as ex:
            print(ex)

    def get_expected_portal_version_number(self):
        try:
            portal_version_number = self.common_test_data_config.get("Portal_Login_Page_Data", "portal_version_number")
            print("expected portal version number: ", portal_version_number)
            return portal_version_number
        except Exception as ex:
            print(ex)

    def get_close_button_on_version_info_by_xpath(self):
        try:
            close_button_on_version_info = self.config.get("Portal_Login_Page", "close_button_on_version_info_by_xpath")
            print("close button on version info: ", close_button_on_version_info)
            return close_button_on_version_info
        except Exception as ex:
            print(ex)

    def get_expected_text_on_close_button_on_version_info(self):
        try:
            close_text_on_close_button_on_version_info = self.common_test_data_config.get("Portal_Login_module_data", "close_text_on_close_button_on_version_info")
            print("expected text on close button in version info: ", close_text_on_close_button_on_version_info)
            return close_text_on_close_button_on_version_info
        except Exception as ex:
            print(ex)

    def get_missing_username_text_on_error_alert_by_xpath(self):
        try:
            missing_username_text_on_error_alert = self.config.get("Portal_Login_Page", "missing_username_text_on_error_alert_by_xpath")
            print("missing username text on alert: ", missing_username_text_on_error_alert)
            return missing_username_text_on_error_alert
        except Exception as ex:
            print(ex)

    def get_close_missing_username_alert_by_xpath(self):
        try:
            close_missing_username_alert = self.config.get("Portal_Login_Page", "close_missing_username_alert_by_xpath")
            print("close missing username alert: ", close_missing_username_alert)
            return close_missing_username_alert
        except Exception as ex:
            print(ex)

    def get_missing_password_text_on_error_alert_by_xpath(self):
        try:
            missing_password_text_on_error_alert = self.config.get("Portal_Login_Page", "missing_password_text_on_error_alert_by_xpath")
            print("missing password text on alert: ", missing_password_text_on_error_alert)
            return missing_password_text_on_error_alert
        except Exception as ex:
            print(ex)

    def get_close_missing_password_alert_by_xpath(self):
        try:
            close_missing_password_alert = self.config.get("Portal_Login_Page", "close_missing_password_alert_by_xpath")
            print("close missing password alert: ", close_missing_password_alert)
            return close_missing_password_alert
        except Exception as ex:
            print(ex)

    def get_invalid_username_text_on_alert_by_xpath(self):
        try:
            invalid_username_text_on_alert = self.config.get("Portal_Login_Page", "invalid_username_text_on_alert_by_xpath")
            print("invalid username text on alert: ", invalid_username_text_on_alert)
            return invalid_username_text_on_alert
        except Exception as ex:
            print(ex)

    def get_expected_invalid_username_error_text(self):
        try:
            expected_invalid_username_error_text = self.common_test_data_config.get("Portal_Login_module_data", "expected_invalid_username_error_text")
            print("invalid username error msg: ", expected_invalid_username_error_text)
            return expected_invalid_username_error_text
        except Exception as ex:
            print(ex)

    def get_expected_invalid_password_error_text(self):
        try:
            expected_invalid_password_error_text = self.common_test_data_config.get("Portal_Login_module_data", "expected_invalid_password_error_text")
            print("invalid password error msg: ", expected_invalid_password_error_text)
            return expected_invalid_password_error_text
        except Exception as ex:
            print(ex)

    def get_close_invalid_username_alert_by_xpath(self):
        try:
            close_invalid_username_alert = self.config.get("Portal_Login_Page", "close_invalid_username_alert_by_xpath")
            print("close invalid username alert: ", close_invalid_username_alert)
            return close_invalid_username_alert
        except Exception as ex:
            print(ex)

    def get_invalid_password_text_on_alert_by_xpath(self):
        try:
            invalid_password_text_on_alert = self.config.get("Portal_Login_Page", "invalid_password_text_on_alert_by_xpath")
            print("invalid password text on alert: ", invalid_password_text_on_alert)
            return invalid_password_text_on_alert
        except Exception as ex:
            print(ex)

    def get_close_invalid_password_alert_by_xpath(self):
        try:
            close_invalid_password_alert = self.config.get("Portal_Login_Page", "close_invalid_password_alert_by_xpath")
            print("close invalid password alert: ", close_invalid_password_alert)
            return close_invalid_password_alert
        except Exception as ex:
            print(ex)

    def get_account_blocked_message_after_entering_invalid_password_six_times(self):
        try:
            account_blocked_message_after_entering_invalid_password_six_times = self.common_test_data_config.get("Portal_Login_module_data", "account_blocked_message_after_entering_invalid_password_six_times")
            print("account blocked message: ", account_blocked_message_after_entering_invalid_password_six_times)
            return account_blocked_message_after_entering_invalid_password_six_times
        except Exception as ex:
            print(ex)

    def get_logout_button_on_portal_by_xpath(self):
        try:
            logout_button_on_portal = self.config.get("Portal_Login_Page", "logout_button_on_portal_by_xpath")
            print("logout button on portal: ", logout_button_on_portal)
            return logout_button_on_portal
        except Exception as ex:
            print(ex)

    def get_expected_password_not_match(self):
        try:
            expected_password_not_match = self.common_test_data_config.get("Portal_Login_module_data", "expected_password_not_match")
            print(f"expected_password_not_match: {expected_password_not_match}")
            return expected_password_not_match

        except Exception as ex:
            print(ex.args)

    def Expected_dimensions_of_logo(self):
        try:
            logo_dimension = self.common_test_data_config.get("Portal_Login_module_data", "Expected_dimensions")
            print("logo dimensions are ", logo_dimension)
            return logo_dimension
        except Exception as ex:
            print(ex)

    def Blue_color_rgba(self):
        try:
            blue_color = self.common_test_data_config.get("Portal_Login_module_data", "blue_colour_rgba_value")
            print("blue colour rgba value is ", blue_color)
            return blue_color
        except Exception as ex:
            print(ex)

    def white_color_rgba(self):
        try:
            white_colour = self.common_test_data_config.get("Portal_Login_module_data", "white_colour_rgba_value")
            print("white color rgba value is ", white_colour)
            return white_colour
        except Exception as ex:
            print(ex)

    def black_color_rgba(self):
        try:
            black_colour = self.common_test_data_config.get("Portal_Login_module_data", "black_colour_rgba_value")
            return black_colour
        except Exception as ex:
            print(ex)

    def font_type(self):
        try:
            font_type = self.common_test_data_config.get("Portal_Login_module_data", "font_type")
            return font_type
        except Exception as ex:
            print(ex)

    def diabled_username(self):
        try:
            disabled = self.common_test_data_config.get("Portal_Login_module_data", "disabled_username")
            return disabled
        except Exception as ex:
            print(ex)

    def disabled_error_message(self):
        try:
            dis_err_msg = self.config.get("Portal_Login_Page", "disabled_error_message")
            return dis_err_msg
        except Exception as ex:
            print(ex)

# Portal_login_page_read_ini().get_portal_url()
# Portal_login_page_read_ini().get_portal_login_username_textbox_by_xpath()
# Portal_login_page_read_ini().get_portal_login_password_textbox_by_xpath()
# Portal_login_page_read_ini().get_cloud_login_button_on_portal_by_xpath()
# Portal_login_page_read_ini().get_cloud_text_on_cloud_login_button_by_xpath()
# Portal_login_page_read_ini().get_login_text_on_cloud_login_button_by_xpath()
# Portal_login_page_read_ini().get_events_button_on_portal_by_xpath()
# Portal_login_page_read_ini().get_exclamation_mark_icon_on_events_button_by_xpath()
# Portal_login_page_read_ini().get_events_text_on_events_button_by_xpath()
# Portal_login_page_read_ini().get_identify_enroll_button_by_xpath()
# Portal_login_page_read_ini().get_camera_icon_on_identify_enroll_button_by_xpath()
# Portal_login_page_read_ini().get_identify_enroll_text_on_identify_enroll_button_by_xpath()
# Portal_login_page_read_ini().get_users_button_by_xpath()
# Portal_login_page_read_ini().get_male_icon_on_users_button_by_xpath()
# Portal_login_page_read_ini().get_users_text_on_users_button_by_xpath()
# Portal_login_page_read_ini().get_account_button_by_xpath()
# Portal_login_page_read_ini().get_lock_icon_on_account_button_by_xpath()
# Portal_login_page_read_ini().get_account_text_on_account_button_by_xpath()
# Portal_login_page_read_ini().get_switch_language_button_by_xpath()
# Portal_login_page_read_ini().get_switch_language_text_on_switch_language_button_by_xpath()
# Portal_login_page_read_ini().get_face_first_copyright_text_by_xpath()
# Portal_login_page_read_ini().get_missing_username_text_on_error_alert_by_xpath()
# Portal_login_page_read_ini().get_missing_password_text_on_error_alert_by_xpath()
# Portal_login_page_read_ini().get_close_missing_username_alert_by_xpath()
# Portal_login_page_read_ini().get_close_missing_password_alert_by_xpath()
# Portal_login_page_read_ini().get_invalid_username_text_on_alert_by_xpath()
# Portal_login_page_read_ini().get_invalid_password_text_on_alert_by_xpath()
# Portal_login_page_read_ini().get_close_invalid_username_alert_by_xpath()
# Portal_login_page_read_ini().get_close_invalid_password_alert_by_xpath()
# Portal_login_page_read_ini().get_logout_button_on_portal_by_xpath()
