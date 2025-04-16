import configparser
from pathlib import Path


class Read_Users_Components:
    def __init__(self):

        self.config = configparser.RawConfigParser()
        self.common_test_data_config = configparser.RawConfigParser()

        try:
            users_ini_file_path = f'{Path(__file__).parent.parent.parent}\\All_Test_Data\\4_Users_Module\\Data_From_INI\\Users.ini'
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"

            self.common_test_data_config.read(common_test_data_ini_file_path)
            self.config.read(users_ini_file_path)
        except Exception as ex:
            print("config file got an exception", ex)

    def logout_btn_by_xpath(self):
        try:
            logout_btn_by_xpath = self.config.get("LOCATORS", "logout_btn_by_xpath")
            return logout_btn_by_xpath
        except Exception as ex:
            print(ex)

    def users_cloud_menu_by_xpath(self):
        try:
            users_cloud_menu_by_xpath = self.config.get("LOCATORS", "users_cloud_menu_by_xpath")
            return users_cloud_menu_by_xpath
        except Exception as ex:
            print(ex)

    def users_cloud_menu_validation_text(self):
        try:
            users_cloud_menu_validation_text = self.common_test_data_config.get("Users_Data", "users_cloud_menu_validation_text")
            return users_cloud_menu_validation_text
        except Exception as ex:
            print(ex)

    def users_panel_title_by_xpath(self):
        try:
            users_panel_title_by_xpath = self.config.get("LOCATORS", "users_panel_title_by_xpath")
            return users_panel_title_by_xpath
        except Exception as ex:
            print(ex)

    def users_panel_title_validation_text(self):
        try:
            users_panel_title_validation_text = self.common_test_data_config.get("Users_Data", "users_panel_title_validation_text")
            return users_panel_title_validation_text
        except Exception as ex:
            print(ex)

    def action_dropdown_by_xpath(self):
        try:
            action_dropdown_by_xpath = self.config.get("LOCATORS", "action_dropdown_by_xpath")
            return action_dropdown_by_xpath
        except Exception as ex:
            print(ex)

    def refresh_by_xpath(self):
        try:
            refresh_by_xpath = self.config.get("LOCATORS", "refresh_by_xpath")
            return refresh_by_xpath
        except Exception as ex:
            print(ex)

    def action_dropdown_validation_text(self):
        try:
            action_dropdown_validation_text = self.common_test_data_config.get("Users_Data", "action_dropdown_validation_text")
            return action_dropdown_validation_text
        except Exception as ex:
            print(ex)

    def refresh_validation_text(self):
        try:
            refresh_validation_text = self.common_test_data_config.get("Users_Data", "refresh_validation_text")
            return refresh_validation_text
        except Exception as ex:
            print(ex)

    def create_user_by_xpath(self):
        try:
            create_user_by_xpath = self.config.get("LOCATORS", "create_user_by_xpath")
            return create_user_by_xpath
        except Exception as ex:
            print(ex)

    def create_user_validation_text(self):
        try:
            create_user_validation_text = self.common_test_data_config.get("Users_Data", "create_user_validation_text")
            return create_user_validation_text
        except Exception as ex:
            print(ex)

    def delete_selected_user_by_xpath(self):
        try:
            delete_selected_user_by_xpath = self.config.get("LOCATORS", "delete_selected_user_by_xpath")
            return delete_selected_user_by_xpath
        except Exception as ex:
            print(ex)

    def delete_selected_user_validation_text(self):
        try:
            delete_selected_user_validation_text = self.common_test_data_config.get("Users_Data", "delete_selected_user_validation_text")
            return delete_selected_user_validation_text
        except Exception as ex:
            print(ex)

    def updating_indicator_by_xpath(self):
        try:
            updating_indicator_by_xpath = self.config.get("LOCATORS", "updating_indicator_by_xpath")
            return updating_indicator_by_xpath
        except Exception as ex:
            print(ex)

    def user_panel_title_by_xpath(self):
        try:
            user_panel_title_by_xpath = self.config.get("LOCATORS", "user_panel_title_by_xpath")
            return user_panel_title_by_xpath
        except Exception as ex:
            print(ex)

    def user_panel_title_validation_text(self):
        try:
            user_panel_title_validation_text = self.common_test_data_config.get("Users_Data", "user_panel_title_validation_text")
            return user_panel_title_validation_text
        except Exception as ex:
            print(ex)

    def user_panel_header_by_xpath(self):
        try:
            user_panel_header_by_xpath = self.config.get("LOCATORS", "user_panel_header_by_xpath")
            return user_panel_header_by_xpath
        except Exception as ex:
            print(ex)

    def user_panel_header_validation_text(self):
        try:
            user_panel_header_validation_text = self.common_test_data_config.get("Users_Data", "user_panel_header_validation_text")
            return user_panel_header_validation_text
        except Exception as ex:
            print(ex)

    def user_panel_cancel_button_by_xpath(self):
        try:
            user_panel_cancel_button_by_xpath = self.config.get("LOCATORS", "user_panel_cancel_button_by_xpath")
            return user_panel_cancel_button_by_xpath
        except Exception as ex:
            print(ex)

    def user_panel_cancel_btn_validation_text(self):
        try:
            user_panel_cancel_btn_validation_text = self.common_test_data_config.get("Users_Data", "user_panel_cancel_btn_validation_text")
            return user_panel_cancel_btn_validation_text
        except Exception as ex:
            print(ex)

    def user_panel_save_button_by_xpath(self):
        try:
            user_panel_save_button_by_xpath = self.config.get("LOCATORS", "user_panel_save_button_by_xpath")
            return user_panel_save_button_by_xpath
        except Exception as ex:
            print(ex)

    def user_panel_save_btn_validation_text(self):
        try:
            user_panel_save_btn_validation_text = self.common_test_data_config.get("Users_Data", "user_panel_save_btn_validation_text")
            return user_panel_save_btn_validation_text
        except Exception as ex:
            print(ex)

    def user_name_by_xpath(self):
        try:
            user_name_by_xpath = self.config.get("LOCATORS", "user_name_by_xpath")
            return user_name_by_xpath
        except Exception as ex:
            print(ex)

    def user_name_error_msg_by_xpath(self):
        try:
            user_name_error_msg_by_xpath = self.config.get("LOCATORS", "user_name_error_msg_by_xpath")
            return user_name_error_msg_by_xpath
        except Exception as ex:
            print(ex)

    def user_name_error_msg_validation_text(self):
        try:
            user_name_error_msg_validation_text = self.common_test_data_config.get("Users_Data", "user_name_error_msg_validation_text")
            return user_name_error_msg_validation_text
        except Exception as ex:
            print(ex)

    def user_role_by_xpath(self):
        try:
            user_role_by_xpath = self.config.get("LOCATORS", "user_role_by_xpath")
            return user_role_by_xpath
        except Exception as ex:
            print(ex)

    def user_role_error_msg(self):
        try:
            user_role_error_msg = self.config.get("LOCATORS", "user_role_error_msg")
            return user_role_error_msg
        except Exception as ex:
            print(ex)

    def user_role_error_msg_validation_text(self):
        try:
            user_role_error_msg_validation_text = self.common_test_data_config.get("Users_Data", "user_role_error_msg_validation_text")
            return user_role_error_msg_validation_text
        except Exception as ex:
            print(ex)

    def new_password_by_xpath(self):
        try:
            new_password_by_xpath = self.config.get("LOCATORS", "new_password_by_xpath")
            return new_password_by_xpath
        except Exception as ex:
            print(ex)

    def new_password_error_msg_by_xpath(self):
        try:
            new_password_error_msg_by_xpath = self.config.get("LOCATORS", "new_password_error_msg_by_xpath")
            return new_password_error_msg_by_xpath
        except Exception as ex:
            print(ex)

    def new_password_error_msg_validation_text(self):
        try:
            new_password_error_msg_validation_text = self.common_test_data_config.get("Users_Data", "new_password_error_msg_validation_text")
            return new_password_error_msg_validation_text
        except Exception as ex:
            print(ex)

    def confirm_password_by_xpath(self):
        try:
            confirm_password_by_xpath = self.config.get("LOCATORS", "confirm_password_by_xpath")
            return confirm_password_by_xpath
        except Exception as ex:
            print(ex)

    def confirm_password_error_msg_by_xpath(self):
        try:
            confirm_password_error_msg_by_xpath = self.config.get("LOCATORS", "confirm_password_error_msg_by_xpath")
            return confirm_password_error_msg_by_xpath
        except Exception as ex:
            print(ex)

    def confirm_password_error_msg_validation_text(self):
        try:
            confirm_password_error_msg_validation_text = self.common_test_data_config.get("Users_Data", "confirm_password_error_msg_validation_text")
            return confirm_password_error_msg_validation_text
        except Exception as ex:
            print(ex)

    def region_by_xpath(self):
        try:
            region_by_xpath = self.config.get("LOCATORS", "region_by_xpath")
            return region_by_xpath
        except Exception as ex:
            print(ex)

    def region_error_msg_by_xpath(self):
        try:
            region_error_msg_by_xpath = self.config.get("LOCATORS", "region_error_msg_by_xpath")
            return region_error_msg_by_xpath
        except Exception as ex:
            print(ex)

    def region_error_msg_validation_text(self):
        try:
            region_error_msg_validation_text = self.common_test_data_config.get("Users_Data", "region_error_msg_validation_text")
            return region_error_msg_validation_text
        except Exception as ex:
            print(ex)

    def email_by_xpath(self):
        try:
            email_by_xpath = self.config.get("LOCATORS", "email_by_xpath")
            return email_by_xpath
        except Exception as ex:
            print(ex)

    def email_error_msg_by_xpath(self):
        try:
            email_error_msg_by_xpath = self.config.get("LOCATORS", "email_error_msg_by_xpath")
            return email_error_msg_by_xpath
        except Exception as ex:
            print(ex)

    def email_error_msg_validation_text(self):
        try:
            email_error_msg_validation_text = self.common_test_data_config.get("Users_Data", "email_error_msg_validation_text")
            return email_error_msg_validation_text
        except Exception as ex:
            print(ex)

    def time_zone_by_xpath(self):
        try:
            time_zone_by_xpath = self.config.get("LOCATORS", "time_zone_by_xpath")
            return time_zone_by_xpath
        except Exception as ex:
            print(ex)

    def time_zone_error_msg_by_xpath(self):
        try:
            time_zone_error_msg_by_xpath = self.config.get("LOCATORS", "time_zone_error_msg_by_xpath")
            return time_zone_error_msg_by_xpath
        except Exception as ex:
            print(ex)

    def time_zone_error_msg_validation_text(self):
        try:
            time_zone_error_msg_validation_text = self.common_test_data_config.get("Users_Data", "time_zone_error_msg_validation_text")
            return time_zone_error_msg_validation_text
        except Exception as ex:
            print(ex)

    def enabled_by_xpath(self):
        try:
            enabled_by_xpath = self.config.get("LOCATORS", "enabled_by_xpath")
            return enabled_by_xpath
        except Exception as ex:
            print(ex)

    def disabled_by_xpath(self):
        try:
            disabled_by_xpath = self.config.get("LOCATORS", "disabled_by_xpath")
            return disabled_by_xpath
        except Exception as ex:
            print(ex)

    def first_name_by_xpath(self):
        try:
            first_name_by_xpath = self.config.get("LOCATORS", "first_name_by_xpath")
            return first_name_by_xpath
        except Exception as ex:
            print(ex)

    def last_name_by_xpath(self):
        try:
            last_name_by_xpath = self.config.get("LOCATORS", "last_name_by_xpath")
            return last_name_by_xpath
        except Exception as ex:
            print(ex)

    def user_role_input_data(self):
        try:
            user_role_input_data = self.common_test_data_config.get("Users_Data", "so_user_role")
            return user_role_input_data
        except Exception as ex:
            print(ex)

    def company_by_xpath(self):
        try:
            company_by_xpath = self.config.get("LOCATORS", "company_by_xpath")
            return company_by_xpath
        except Exception as ex:
            print(ex)

    def title_by_xpath(self):
        try:
            title_by_xpath = self.config.get("LOCATORS", "title_by_xpath")
            return title_by_xpath
        except Exception as ex:
            print(ex)

    def region_list_by_xpath(self):
        try:
            region_list_by_xpath = self.config.get("LOCATORS", "region_list_by_xpath")
            return region_list_by_xpath
        except Exception as ex:
            print(ex)

    def region_save_btn_by_xpath(self):
        try:
            region_save_btn_by_xpath = self.config.get("LOCATORS", "region_save_btn_by_xpath")
            return region_save_btn_by_xpath
        except Exception as ex:
            print(ex)

    def region_selected_by_xpath(self):
        try:
            region_selected_by_xpath = self.config.get("LOCATORS", "region_selected_by_xpath")
            return region_selected_by_xpath
        except Exception as ex:
            print(ex)

    def department_by_xpath(self):
        try:
            department_by_xpath = self.config.get("LOCATORS", "department_by_xpath")
            return department_by_xpath
        except Exception as ex:
            print(ex)

    def alert_email_by_xpath(self):
        try:
            alert_email_by_xpath = self.config.get("LOCATORS", "alert_email_by_xpath")
            return alert_email_by_xpath
        except Exception as ex:
            print(ex)

    def alert_phone_number_by_xpath(self):
        try:
            alert_phone_number_by_xpath = self.config.get("LOCATORS", "alert_phone_number_by_xpath")
            return alert_phone_number_by_xpath
        except Exception as ex:
            print(ex)

    def address_by_xpath(self):
        try:
            address_by_xpath = self.config.get("LOCATORS", "address_by_xpath")
            return address_by_xpath
        except Exception as ex:
            print(ex)

    def address2_by_xpath(self):
        try:
            address2_by_xpath = self.config.get("LOCATORS", "address2_by_xpath")
            return address2_by_xpath
        except Exception as ex:
            print(ex)

    def city_by_xpath(self):
        try:
            city_by_xpath = self.config.get("LOCATORS", "city_by_xpath")
            return city_by_xpath
        except Exception as ex:
            print(ex)

    def state_by_xpath(self):
        try:
            state_by_xpath = self.config.get("LOCATORS", "state_by_xpath")
            return state_by_xpath
        except Exception as ex:
            print(ex)

    def postal_code_by_xpath(self):
        try:
            postal_code_by_xpath = self.config.get("LOCATORS", "postal_code_by_xpath")
            return postal_code_by_xpath
        except Exception as ex:
            print(ex)

    def home_phone_number_by_xpath(self):
        try:
            home_phone_number_by_xpath = self.config.get("LOCATORS", "home_phone_number_by_xpath")
            return home_phone_number_by_xpath
        except Exception as ex:
            print(ex)

    def work_phone_number_by_xpath(self):
        try:
            work_phone_number_by_xpath = self.config.get("LOCATORS", "work_phone_number_by_xpath")
            return work_phone_number_by_xpath
        except Exception as ex:
            print(ex)

    def fax_phone_number_by_xpath(self):
        try:
            fax_phone_number_by_xpath = self.config.get("LOCATORS", "fax_phone_number_by_xpath")
            return fax_phone_number_by_xpath
        except Exception as ex:
            print(ex)

    def phone_type_by_xpath(self):
        try:
            phone_type_by_xpath = self.config.get("LOCATORS", "phone_type_by_xpath")
            return phone_type_by_xpath
        except Exception as ex:
            print(ex)

    def phone_provider_drop_dwn_by_xpath(self):
        try:
            phone_provider_drop_dwn_by_xpath = self.config.get("LOCATORS", "phone_provider_drop_dwn_by_xpath")
            return phone_provider_drop_dwn_by_xpath
        except Exception as ex:
            print(ex)

    def alert_schedule_btn_by_xpath(self):
        try:
            alert_schedule_btn_by_xpath = self.config.get("LOCATORS", "alert_schedule_btn_by_xpath")
            return alert_schedule_btn_by_xpath
        except Exception as ex:
            print(ex)

    def notification_groups_btn_by_xpath(self):
        try:
            notification_groups_btn_by_xpath = self.config.get("LOCATORS", "notification_groups_btn_by_xpath")
            return notification_groups_btn_by_xpath
        except Exception as ex:
            print(ex)

    def close_panel_list_by_xpath(self):
        try:
            close_panel_list_by_xpath = self.config.get("LOCATORS", "close_panel_list_by_xpath")
            return close_panel_list_by_xpath
        except Exception as ex:
            print(ex)

    def users_panel_close_panel_btn(self):
        try:
            users_panel_close_panel_btn = self.config.get("LOCATORS", "users_panel_close_panel_btn")
            return users_panel_close_panel_btn
        except Exception as ex:
            print(ex)

    def first_name_input_data(self):
        try:
            first_name_input_data = self.common_test_data_config.get("Users_Data", "first_name_input_data")
            return first_name_input_data
        except Exception as ex:
            print(ex)

    def last_name_input_data(self):
        try:
            last_name_input_data = self.common_test_data_config.get("Users_Data", "last_name_input_data")
            return last_name_input_data
        except Exception as ex:
            print(ex)

    def error_message_by_xpath(self):
        try:
            error_message_by_xpath = self.config.get("LOCATORS", "error_message_by_xpath")
            return error_message_by_xpath
        except Exception as ex:
            print(ex)

    def error_msg_validation_text(self):
        try:
            error_msg_validation_text = self.common_test_data_config.get("Users_Data", "error_msg_validation_text")
            return error_msg_validation_text
        except Exception as ex:
            print(ex)

    def time_zone_input_data(self):
        try:
            time_zone_input_data = self.common_test_data_config.get("Users_Data", "time_zone_input_data")
            return time_zone_input_data
        except Exception as ex:
            print(ex)

    def email_input_data(self):
        try:
            email_input_data = self.common_test_data_config.get("Users_Data", "email_input_data")
            return email_input_data
        except Exception as ex:
            print(ex)

    def region_data_input(self):
        try:
            region_data_input = self.common_test_data_config.get("Users_Data", "region_data_input")
            return region_data_input
        except Exception as ex:
            print(ex)

    def password_data_input(self):
        try:
            password_data_input = self.common_test_data_config.get("Users_Data", "password_data_input")
            return password_data_input
        except Exception as ex:
            print(ex)

    def user_name_input_data(self):
        try:
            user_name_input_data = self.common_test_data_config.get("Users_Data", "user_name_input_data")
            return user_name_input_data
        except Exception as ex:
            print(ex)

    def user_role_options_by_xpath(self):
        try:
            user_role_options_by_xpath = self.config.get("LOCATORS", "user_role_options_by_xpath")
            return user_role_options_by_xpath
        except Exception as ex:
            print(ex)

    def time_zone_options_by_xpath(self):
        try:
            time_zone_options_by_xpath = self.config.get("LOCATORS", "time_zone_options_by_xpath")
            return time_zone_options_by_xpath
        except Exception as ex:
            print(ex)

    def company_input_data(self):
        try:
            company_input_data = self.common_test_data_config.get("Users_Data", "company_input_data")
            return company_input_data
        except Exception as ex:
            print(ex)

    def title_input_data(self):
        try:
            title_input_data = self.common_test_data_config.get("Users_Data", "title_input_data")
            return title_input_data
        except Exception as ex:
            print(ex)

    def department_input_data(self):
        try:
            department_input_data = self.common_test_data_config.get("Users_Data", "department_input_data")
            return department_input_data
        except Exception as ex:
            print(ex)

    def alert_email_input_data(self):
        try:
            alert_email_input_data = self.common_test_data_config.get("Users_Data", "alert_email_input_data")
            return alert_email_input_data
        except Exception as ex:
            print(ex)

    def alert_phone_no_input_data(self):
        try:
            alert_phone_no_input_data = self.common_test_data_config.get("Users_Data", "alert_phone_no_input_data")
            return alert_phone_no_input_data
        except Exception as ex:
            print(ex)

    def address_input_data(self):
        try:
            address_input_data = self.common_test_data_config.get("Users_Data", "address_input_data")
            return address_input_data
        except Exception as ex:
            print(ex)

    def address2_input_data(self):
        try:
            address2_input_data = self.common_test_data_config.get("Users_Data", "address2_input_data")
            return address2_input_data
        except Exception as ex:
            print(ex)

    def city_input_data(self):
        try:
            city_input_data = self.common_test_data_config.get("Users_Data", "city_input_data")
            return city_input_data
        except Exception as ex:
            print(ex)

    def state_input_data(self):
        try:
            state_input_data = self.common_test_data_config.get("Users_Data", "state_input_data")
            return state_input_data
        except Exception as ex:
            print(ex)

    def postal_code_input_data(self):
        try:
            postal_code_input_data = self.common_test_data_config.get("Users_Data", "postal_code_input_data")
            return postal_code_input_data
        except Exception as ex:
            print(ex)

    def home_phone_no_input_data(self):
        try:
            home_phone_no_input_data = self.common_test_data_config.get("Users_Data", "home_phone_no_input_data")
            return home_phone_no_input_data
        except Exception as ex:
            print(ex)

    def work_phone_no_input_data(self):
        try:
            work_phone_no_input_data = self.common_test_data_config.get("Users_Data", "work_phone_no_input_data")
            return work_phone_no_input_data
        except Exception as ex:
            print(ex)

    def fax_phone_no_input_data(self):
        try:
            fax_phone_no_input_data = self.common_test_data_config.get("Users_Data", "fax_phone_no_input_data")
            return fax_phone_no_input_data
        except Exception as ex:
            print(ex)

    def phone_type_input_data(self):
        try:
            phone_type_input_data = self.common_test_data_config.get("Users_Data", "phone_type_input_data")
            return phone_type_input_data
        except Exception as ex:
            print(ex)

    def success_message_by_xpath(self):
        try:
            success_message_by_xpath = self.config.get("LOCATORS", "success_message_by_xpath")
            return success_message_by_xpath
        except Exception as ex:
            print(ex)

    def success_msg_validation_text(self):
        try:
            success_msg_validation_text = self.common_test_data_config.get("Users_Data", "success_msg_validation_text")
            return success_msg_validation_text
        except Exception as ex:
            print(ex)

    def users_list_board_username_by_xpath(self):
        try:
            users_list_board_username_by_xpath = self.config.get("LOCATORS", "users_list_board_username_by_xpath")
            return users_list_board_username_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_username_by_xpath(self):
        try:
            user_details_username_by_xpath = self.config.get("LOCATORS", "user_details_username_by_xpath")
            return user_details_username_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_first_name_by_xpath(self):
        try:
            user_details_first_name_by_xpath = self.config.get("LOCATORS", "user_details_first_name_by_xpath")
            return user_details_first_name_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_last_name_by_xpath(self):
        try:
            user_details_last_name_by_xpath = self.config.get("LOCATORS", "user_details_last_name_by_xpath")
            return user_details_last_name_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_user_role_by_xpath(self):
        try:
            user_details_user_role_by_xpath = self.config.get("LOCATORS", "user_details_user_role_by_xpath")
            return user_details_user_role_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_region_by_xpath(self):
        try:
            user_details_region_by_xpath = self.config.get("LOCATORS", "user_details_region_by_xpath")
            return user_details_region_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_email_by_xpath(self):
        try:
            user_details_email_by_xpath = self.config.get("LOCATORS", "user_details_email_by_xpath")
            return user_details_email_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_timezone_by_xpath(self):
        try:
            user_details_timezone_by_xpath = self.config.get("LOCATORS", "user_details_timezone_by_xpath")
            return user_details_timezone_by_xpath
        except Exception as ex:
            print(ex)

    def phone_provider_input_data(self):
        try:
            phone_provider_input_data = self.common_test_data_config.get("Users_Data", "phone_provider_input_data")
            return phone_provider_input_data
        except Exception as ex:
            print(ex)

    def search_box_by_xpath(self):
        try:
            search_box_by_xpath = self.config.get("LOCATORS", "search_box_by_xpath")
            return search_box_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_company_by_xpath(self):
        try:
            user_details_company_by_xpath = self.config.get("LOCATORS", "user_details_company_by_xpath")
            return user_details_company_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_title_by_xpath(self):
        try:
            user_details_title_by_xpath = self.config.get("LOCATORS", "user_details_title_by_xpath")
            return user_details_title_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_department_by_xpath(self):
        try:
            user_details_department_by_xpath = self.config.get("LOCATORS", "user_details_department_by_xpath")
            return user_details_department_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_alert_email_by_xpath(self):
        try:
            user_details_alert_email_by_xpath = self.config.get("LOCATORS", "user_details_alert_email_by_xpath")
            return user_details_alert_email_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_alert_ph_no_by_xpath(self):
        try:
            user_details_alert_ph_no_by_xpath = self.config.get("LOCATORS", "user_details_alert_ph_no_by_xpath")
            return user_details_alert_ph_no_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_address_by_xpath(self):
        try:
            user_details_address_by_xpath = self.config.get("LOCATORS", "user_details_address_by_xpath")
            return user_details_address_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_address2_by_xpath(self):
        try:
            user_details_address2_by_xpath = self.config.get("LOCATORS", "user_details_address2_by_xpath")
            return user_details_address2_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_city_by_xpath(self):
        try:
            user_details_city_by_xpath = self.config.get("LOCATORS", "user_details_city_by_xpath")
            return user_details_city_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_state_by_xpath(self):
        try:
            user_details_state_by_xpath = self.config.get("LOCATORS", "user_details_state_by_xpath")
            return user_details_state_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_postal_code_by_xpath(self):
        try:
            user_details_postal_code_by_xpath = self.config.get("LOCATORS", "user_details_postal_code_by_xpath")
            return user_details_postal_code_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_home_ph_no_by_xpath(self):
        try:
            user_details_home_ph_no_by_xpath = self.config.get("LOCATORS", "user_details_home_ph_no_by_xpath")
            return user_details_home_ph_no_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_work_ph_no_by_xpath(self):
        try:
            user_details_work_ph_no_by_xpath = self.config.get("LOCATORS", "user_details_work_ph_no_by_xpath")
            return user_details_work_ph_no_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_fax_ph_no_by_xpath(self):
        try:
            user_details_fax_ph_no_by_xpath = self.config.get("LOCATORS", "user_details_fax_ph_no_by_xpath")
            return user_details_fax_ph_no_by_xpath
        except Exception as ex:
            print(ex)

    def user_details_enabled_by_xpath(self):
        try:
            user_details_enabled_by_xpath = self.config.get("LOCATORS", "user_details_enabled_by_xpath")
            return user_details_enabled_by_xpath
        except Exception as ex:
            print(ex)

    def users_list_board_enabled_by_xpath(self):
        try:
            users_list_board_enabled_by_xpath = self.config.get("LOCATORS", "users_list_board_enabled_by_xpath")
            return users_list_board_enabled_by_xpath
        except Exception as ex:
            print(ex)

    def users_details_disabled_by_xpath(self):
        try:
            users_details_disabled_by_xpath = self.config.get("LOCATORS", "users_details_disabled_by_xpath")
            return users_details_disabled_by_xpath
        except Exception as ex:
            print(ex)

    def users_list_board_disabled_by_xpath(self):
        try:
            users_list_board_disabled_by_xpath = self.config.get("LOCATORS", "users_list_board_disabled_by_xpath")
            return users_list_board_disabled_by_xpath
        except Exception as ex:
            print(ex)

    def alert_panel_title_by_xpath(self):
        try:
            alert_panel_title_by_xpath = self.config.get("LOCATORS", "alert_panel_title_by_xpath")
            return alert_panel_title_by_xpath
        except Exception as ex:
            print(ex)

    def notification_group_title_by_xpath(self):
        try:
            notification_group_title_by_xpath = self.config.get("LOCATORS", "notification_group_title_by_xpath")
            return notification_group_title_by_xpath
        except Exception as ex:
            print(ex)

    def notification_group_title_validation_text(self):
        try:
            notification_group_title_validation_text = self.common_test_data_config.get("Users_Data", "notification_group_title_validation_text")
            return notification_group_title_validation_text
        except Exception as ex:
            print(ex)

    def users_list_board_first_and_last_name_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "users_list_board_first_and_last_name_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def users_list_board_email_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "users_list_board_email_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def notification_group_icon_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "notification_group_icon_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def notification_group_icon_hover_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "notification_group_icon_hover_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def notification_group_icon_hover_validation_text(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "notification_group_icon_hover_validation_text")
            return ele
        except Exception as ex:
            print(ex)

    def details_icon_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "details_icon_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def details_icon_hover_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "details_icon_hover_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def details_icon_hover_validation_text(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "details_icon_hover_validation_text")
            return ele
        except Exception as ex:
            print(ex)

    def alert_schedule_icon_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "alert_schedule_icon_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def alert_schedule_icon_hover_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "alert_schedule_icon_hover_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def alert_schedule_icon_hover_validation_text(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "alert_schedule_icon_hover_validation_text")
            return ele
        except Exception as ex:
            print(ex)

    def alert_panel_sub_title_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "alert_panel_sub_title_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def alert_panel_sub_title_validation_text(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "alert_panel_sub_title_validation_text")
            return ele
        except Exception as ex:
            print(ex)

    def user_details_action_btn(self):
        try:
            ele = self.config.get("LOCATORS", "user_details_action_btn")
            return ele
        except Exception as ex:
            print(ex)

    def user_details_action_edit_user(self):
        try:
            ele = self.config.get("LOCATORS", "user_details_action_edit_user")
            return ele
        except Exception as ex:
            print(ex)

    def user_details_action_alert_schedule(self):
        try:
            ele = self.config.get("LOCATORS", "user_details_action_alert_schedule")
            return ele
        except Exception as ex:
            print(ex)

    def update_email_input_data(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "update_email_input_data")
            return ele
        except Exception as ex:
            print(ex)

    def users_check_box_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "users_check_box_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def filter_message_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "filter_message_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def filter_msg_validation_text(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "filter_msg_validation_text")
            return ele
        except Exception as ex:
            print(ex)

    def delete_confirmation_yes_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "delete_confirmation_yes_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def user_name_exists_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "user_name_exists_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def user_name_exists_validation_text(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "user_name_exists_validation_text")
            return ele
        except Exception as ex:
            print(ex)

    def confirm_password_data_input(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "confirm_password_data_input")
            return ele
        except Exception as ex:
            print(ex)

    def password_mis_match_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "password_mis_match_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def password_mis_match_validation_text(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_mis_match_validation_text")
            return ele
        except Exception as ex:
            print(ex)

    def user_close_panel_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "user_close_panel_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def close_pop_up_go_back_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "close_pop_up_go_back_btn_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def close_panel_and_discard_changes_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "close_panel_and_discard_changes_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def close_pop_up_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "close_pop_up_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def close_panel_pop_validation_text(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "close_panel_pop_validation_text")
            return ele
        except Exception as ex:
            print(ex)

    def close_panel_one_by_one_list(self):
        try:
            ele = self.config.get("LOCATORS", "close_panel_one_by_one_list")
            return ele
        except Exception as ex:
            print(ex)

    def user_close_panel_and_discard_Changes(self):
        try:
            ele = self.config.get("LOCATORS", "user_close_panel_and_discard_Changes")
            return ele
        except Exception as ex:
            print(ex)

    def face_first_logo(self):
        try:
            ele = self.config.get("LOCATORS", "face_first_logo")
            return ele
        except Exception as ex:
            print(ex)

    def notification_groups_filter_drop_dwn(self):
        try:
            ele = self.config.get("LOCATORS", "notification_groups_filter_drop_dwn")
            return ele
        except Exception as ex:
            print(ex)

    def notification_groups_action_drop_dwn(self):
        try:
            ele = self.config.get("LOCATORS", "notification_groups_action_drop_dwn")
            return ele
        except Exception as ex:
            print(ex)

    def option_linked_notification_groups(self):
        try:
            ele = self.config.get("LOCATORS", "option_linked_notification_groups")
            return ele
        except Exception as ex:
            print(ex)

    def option_unlinked_notification_groups(self):
        try:
            ele = self.config.get("LOCATORS", "option_unlinked_notification_groups")
            return ele
        except Exception as ex:
            print(ex)

    def option_remove_from_user(self):
        try:
            ele = self.config.get("LOCATORS", "option_remove_from_user")
            return ele
        except Exception as ex:
            print(ex)

    def option_add_to_user(self):
        try:
            ele = self.config.get("LOCATORS", "option_add_to_user")
            return ele
        except Exception as ex:
            print(ex)

    def option_create_notification_group(self):
        try:
            ele = self.config.get("LOCATORS", "option_create_notification_group")
            return ele
        except Exception as ex:
            print(ex)

    def option_delete_notification_group(self):
        try:
            ele = self.config.get("LOCATORS", "option_delete_notification_group")
            return ele
        except Exception as ex:
            print(ex)

    def notification_groups_option_refresh(self):
        try:
            ele = self.config.get("LOCATORS", "notification_groups_option_refresh")
            return ele
        except Exception as ex:
            print(ex)

    def notification_groups_search_bar(self):
        try:
            ele = self.config.get("LOCATORS", "notification_groups_search_bar")
            return ele
        except Exception as ex:
            print(ex)

    def notification_groups_details_name_input(self):
        try:
            ele = self.config.get("LOCATORS", "notification_groups_details_name_input")
            return ele
        except Exception as ex:
            print(ex)

    def notification_groups_details_description(self):
        try:
            ele = self.config.get("LOCATORS", "notification_groups_details_description")
            return ele
        except Exception as ex:
            print(ex)

    def notification_group_name(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "notification_group_name")
            return ele
        except Exception as ex:
            print(ex)

    def notification_groups_details_save_btn(self):
        try:
            ele = self.config.get("LOCATORS", "notification_groups_details_save_btn")
            return ele
        except Exception as ex:
            print(ex)

    def notification_groups_details_close_panel(self):
        try:
            ele = self.config.get("LOCATORS", "notification_groups_details_close_panel")
            return ele
        except Exception as ex:
            print(ex)

    def notification_groups_select_all_checkbox(self):
        try:
            ele = self.config.get("LOCATORS", "notification_groups_select_all_checkbox")
            return ele
        except Exception as ex:
            print(ex)

    def notification_groups_close_panel(self):
        try:
            ele = self.config.get("LOCATORS", "notification_groups_close_panel")
            return ele
        except Exception as ex:
            print(ex)

    def notification_groups_name_list(self):
        try:
            ele = self.config.get("LOCATORS", "notification_groups_name_list")
            return ele
        except Exception as ex:
            print(ex)

    def notification_groups_no_linked_alerts(self):
        try:
            ele = self.config.get("LOCATORS", "notification_groups_no_linked_alerts")
            return ele
        except Exception as ex:
            print(ex)

    def company_error_msg(self):
        try:
            ele = self.config.get("LOCATORS", "company_error_msg")
            return ele
        except Exception as ex:
            print(ex)

    def company_error_msg_validation_text(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "company_error_msg_validation_text")
            return ele
        except Exception as ex:
            print(ex)

    def password_requirement_un_fn_ln_msg(self):
        try:
            ele = self.config.get("LOCATORS", "password_requirement_un_fn_ln_msg")
            return ele
        except Exception as ex:
            print(ex)

    def password_requirement_un_fn_ln_msg_validation_text(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_requirement_un_fn_ln_msg_validation_text")
            return ele
        except Exception as ex:
            print(ex)

    def password_7_character_data(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_7_character_data")
            return ele
        except Exception as ex:
            print(ex)

    def password_21_character_data(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_21_character_data")
            return ele
        except Exception as ex:
            print(ex)

    def password_only_alphabet_data(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_only_alphabet_data")
            return ele
        except Exception as ex:
            print(ex)

    def password_only_number_data(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_only_number_data")
            return ele
        except Exception as ex:
            print(ex)

    def password_only_special_symbol_data(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_only_special_symbol_data")
            return ele
        except Exception as ex:
            print(ex)

    def password_only_alphabet_number_data(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_only_alphabet_number_data")
            return ele
        except Exception as ex:
            print(ex)

    def password_only_alphabet_special_symbol_data(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_only_alphabet_special_symbol_data")
            return ele
        except Exception as ex:
            print(ex)

    def password_only_number_special_symbol_data(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_only_number_special_symbol_data")
            return ele
        except Exception as ex:
            print(ex)

    def password_less_than_8_characters_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_less_than_8_characters_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def password_greater_than_20_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_greater_than_20_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def password_only_alphabet_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_only_alphabet_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def password_only_numeric_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_only_numeric_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def password_only_special_symbol_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_only_special_symbol_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def password_only_alphanumeric_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_only_alphanumeric_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def password_only_alphabet_sp_symbol_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_only_alphabet_sp_symbol_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def password_only_number_sp_symbol_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "password_only_number_sp_symbol_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def constant_user_name(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "constant_user_name")
            return ele
        except Exception as ex:
            print(ex)

    def alert_panel_sub_title_schedule_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "alert_panel_sub_title_schedule_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def alert_schedule_sub_title_schedule_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "alert_schedule_sub_title_schedule_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def alert_panel_settings_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "alert_panel_settings_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def alert_schedule_settings_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "alert_schedule_settings_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def settings_username_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_username_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_username_value_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_username_value_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_timezone_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_timezone_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_timezone_value_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_timezone_value_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_timezone_id_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_timezone_id_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_timezone_id_value_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_timezone_id_value_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_send_sms_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_send_sms_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_send_sms_value_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_send_sms_value_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_send_mms_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_send_mms_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_send_mms_value_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_send_mms_value_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_send_email_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_send_email_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_send_email_value_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_send_email_value_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_send_in_app_notifications_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_send_in_app_notifications_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_send_in_app_value_notifications_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_send_in_app_value_notifications_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_enable_alerts_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_enable_alerts_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_enable_alerts_value_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "settings_enable_alerts_value_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def settings_username_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "settings_username_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def settings_timezone_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "settings_timezone_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def settings_timezone_id_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "settings_timezone_id_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def settings_send_sms_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "settings_send_sms_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def settings_send_mms_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "settings_send_mms_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def settings_send_email_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "settings_send_email_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def settings_send_in_app_notifications_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "settings_send_in_app_notifications_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def settings_enable_alerts_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "settings_enable_alerts_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def schedule_day_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "schedule_day_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def schedule_time_range_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "schedule_time_range_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def alert_schedule_action_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "alert_schedule_action_btn_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def alert_schedule_action_option_edit_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "alert_schedule_action_option_edit_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def alert_schedule_save_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "alert_schedule_save_btn_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def alert_schedule_cancel_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "alert_schedule_cancel_btn_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def send_sms_yes_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "send_sms_yes_btn_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def send_sms_no_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "send_sms_no_btn_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def send_mms_yes_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "send_mms_yes_btn_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def send_mms_no_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "send_mms_no_btn_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def send_email_yes_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "send_email_yes_btn_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def send_email_no_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "send_email_no_btn_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def send_in_app_notification_yes_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "send_in_app_notification_yes_btn_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def send_in_app_notification_no_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "send_in_app_notification_no_btn_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def enable_alerts_yes_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enable_alerts_yes_btn_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def enable_alerts_no_btn_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "enable_alerts_no_btn_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def schedule_day_checkbox_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "schedule_day_checkbox_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def schedule_time_range_slider_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "schedule_time_range_slider_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def alert_schedule_close_panel_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "alert_schedule_close_panel_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def close_panel_hover_text_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "close_panel_hover_text_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def close_panel_hover_validation_txt(self):
        try:
            ele = self.common_test_data_config.get("Users_Data", "close_panel_hover_validation_txt")
            return ele
        except Exception as ex:
            print(ex)

    def all_open_panel_titles_by_xpath(self):
        try:
            ele = self.config.get("LOCATORS", "all_open_panel_titles_by_xpath")
            return ele
        except Exception as ex:
            print(ex)

    def close_panel_and_discard_changes_warning_by_xpath(self):
        try:
            close_panel_and_discard_changes_warning_by_xpath = self.config.get("LOCATORS", "close_panel_and_discard_changes_warning_by_xpath")
            return close_panel_and_discard_changes_warning_by_xpath
        except Exception as ex:
            print(ex)

    def facefirst_user_xpath(self):
        try:
            user_xpath = self.config.get("LOCATORS", "facefirst_user_by_xpath")
            return user_xpath
        except Exception as ex:
            print(ex)

    def user_checkbox_by_xpath(self):
        try:
            checkbox = self.config.get("LOCATORS", "user_checkbox_by_xpath")
            return checkbox
        except Exception as ex:
            print(ex)

    def yes_delete_selected_button(self):
        try:
            button = self.config.get("LOCATORS", "yes_delete_selected")
            return button
        except Exception as ex:
            print(ex)

    def portal_menu_users_btn_by_xpath(self):
        try:
            users_btn_by_xpath = self.config.get("LOCATORS", "users_btn_by_xpath")
            return users_btn_by_xpath
        except Exception as ex:
            print("portal_menu_users_btn_by_xpath : ", ex)

    def user_created_success_by_xpath(self):
        try:
            user_created_success_by_xpath = self.config.get("LOCATORS", "user_created_success_by_xpath")
            return user_created_success_by_xpath
        except Exception as ex:
            print("user_created_success_by_xpath : ", ex)
