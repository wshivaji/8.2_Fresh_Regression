import configparser
from pathlib import Path


class sspr_read_ini:

    def __init__(self):
        file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\21_SSPR_Module\\Data_From_INI\\sspr.ini"
        common_data_file = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
        self.config = configparser.RawConfigParser()
        self.common_test_data_config = configparser.RawConfigParser()
        try:
            self.config.read(file_path)
            self.common_test_data_config.read(common_data_file)
        except Exception as ex:
            print(ex)

    def get_username_text_box_by_xpath(self):
        try:
            get_username_text_box_by_xpath = self.config.get("locators", "username_textbox_by_xpath")
            print(f"get_username_text_box_by_xpath: {get_username_text_box_by_xpath}")
            return get_username_text_box_by_xpath
        except Exception as ex:
            print("get_username_text_box_by_xpath", ex.args)

    def password_textbox_by_xpath(self):
        try:
            password_textbox_by_xpath = self.config.get("locators", "password_textbox_by_xpath")
            print(f"password_textbox_by_xpath: {password_textbox_by_xpath}")
            return password_textbox_by_xpath
        except Exception as ex:
            print("password_textbox_by_xpath", ex.args)

    def login_link_by_xpath(self):
        try:
            login_link_by_xpath = self.config.get("locators", "login_link_by_xpath")
            print(f"login_link_by_xpath: {login_link_by_xpath}")
            return login_link_by_xpath
        except Exception as ex:
            print("password_textbox_by_xpath", ex.args)

    def cloud_or_local_menu_by_xpath(self):
        try:
            cloud_or_local_menu_by_xpath = self.config.get("locators", "cloud_or_local_menu_by_xpath")
            print(f"cloud_or_local_menu_by_xpath: {cloud_or_local_menu_by_xpath}")
            return cloud_or_local_menu_by_xpath
        except Exception as ex:
            print("cloud_or_local_menu_by_xpath", ex.args)

    def close_all_panels_menu_by_xpath(self):
        try:
            close_all_panels_menu_by_xpath = self.config.get("locators", "close_all_panels_menu_by_xpath")
            print(f"close_all_panels_menu_by_xpath: {close_all_panels_menu_by_xpath}")
            return close_all_panels_menu_by_xpath
        except Exception as ex:
            print("close_all_panels_menu_by_xpath", ex.args)

    def logout_btn_by_xpath(self):
        try:
            logout_btn_by_xpath = self.config.get("locators", "logout_btn_by_xpath")
            print(f"logout_btn_by_xpath: {logout_btn_by_xpath}")
            return logout_btn_by_xpath
        except Exception as ex:
            print("logout_btn_by_xpath", ex.args)

    def change_password_popup_by_xpath(self):
        try:
            change_password_popup_by_xpath = self.config.get("locators", "change_password_popup_by_xpath")
            print(f"change_password_popup_by_xpath: {change_password_popup_by_xpath}")
            return change_password_popup_by_xpath
        except Exception as ex:
            print("change_password_popup_by_xpath ", ex.args)

    def heading_text_on_popup_by_xpath(self):
        try:
            heading_text_on_popup_by_xpath = self.config.get("locators", "heading_text_on_popup_by_xpath")
            print(f"heading_text_on_popup_by_xpath: {heading_text_on_popup_by_xpath}")
            return heading_text_on_popup_by_xpath
        except Exception as ex:
            print("heading_text_on_popup_by_xpath ", ex.args)

    def old_password_textbox_by_xpath(self):
        try:
            old_password_textbox_by_xpath = self.config.get("locators", "old_password_textbox_by_xpath")
            print(f"old_password_textbox_by_xpath: {old_password_textbox_by_xpath}")
            return old_password_textbox_by_xpath
        except Exception as ex:
            print("old_password_textbox_by_xpath ", ex.args)

    def new_password_textbox_by_xpath(self):
        try:
            new_password_textbox_by_xpath = self.config.get("locators", "new_password_textbox_by_xpath")
            print(f"new_password_textbox_by_xpath: {new_password_textbox_by_xpath}")
            return new_password_textbox_by_xpath
        except Exception as ex:
            print("new_password_textbox_by_xpath ", ex.args)

    def confirm_password_text_box_by_xpath(self):
        try:
            confirm_password_text_box_by_xpath = self.config.get("locators", "confirm_password_text_box_by_xpath")
            print(f"confirm_password_text_box_by_xpath: {confirm_password_text_box_by_xpath}")
            return confirm_password_text_box_by_xpath
        except Exception as ex:
            print("confirm_password_text_box_by_xpath ", ex.args)

    def cancel_btn_on_popup_by_xpath(self):
        try:
            cancel_btn_on_popup_by_xpath = self.config.get("locators", "cancel_btn_on_popup_by_xpath")
            print(f"cancel_btn_on_popup_by_xpath: {cancel_btn_on_popup_by_xpath}")
            return cancel_btn_on_popup_by_xpath
        except Exception as ex:
            print("cancel_btn_on_popup_by_xpath ", ex.args)

    def submit_btn_on_popup_by_xpath(self):
        try:
            submit_btn_on_popup_by_xpath = self.config.get("locators", "submit_btn_on_popup_by_xpath")
            print(f"submit_btn_on_popup_by_xpath: {submit_btn_on_popup_by_xpath}")
            return submit_btn_on_popup_by_xpath
        except Exception as ex:
            print("submit_btn_on_popup_by_xpath ", ex.args)

    def password_must_contain_8to20_characters_error_msg_by_xpath(self):
        try:
            password_must_contain_8to20_characters_error_msg_by_xpath = self.config.get("locators", "password_must_contain_8to20_characters_error_msg_by_xpath")
            print(f"password_must_contain_8to20_characters_error_msg_by_xpath: {password_must_contain_8to20_characters_error_msg_by_xpath}")
            return password_must_contain_8to20_characters_error_msg_by_xpath
        except Exception as ex:
            print("password_must_contain_8to20_characters_error_msg_by_xpath ", ex.args)

    def password_change_success_message_by_xpath(self):
        try:
            password_change_success_message_by_xpath = self.config.get("locators", "password_change_success_message_by_xpath")
            print(f"password_change_success_message_by_xpath: {password_change_success_message_by_xpath}")
            return password_change_success_message_by_xpath
        except Exception as ex:
            print("password_change_success_message_by_xpath ", ex.args)

    # *********************** Common Data ******************************

    def get_username(self):
        try:
            username = self.common_test_data_config.get("Login_Logout_Data", "sspr_username")
            print("username: ", username)
            return username
        except Exception as ex:
            print("enter_username_password_and_click_on_login ", {ex.args})

    def get_password(self):
        try:
            password = self.common_test_data_config.get("Login_Logout_Data", "sspr_password")
            print("password: ", {password})
            return password
        except Exception as ex:
            print("password ex: ", {ex.args})

    def get_new_password(self):
        try:
            new_password = self.common_test_data_config.get("Login_Logout_Data", "new_password")
            print("new_password: ", {new_password})
            return new_password
        except Exception as ex:
            print("new_password ex: ", {ex.args})

    def get_cloud_url(self):
        try:
            url = self.common_test_data_config.get("Login_Logout_Data", "cloud_login_url")
            print(f"url {url}")
            return url
        except Exception as ex:
            print("get cloud url ex: ", {ex.args})
