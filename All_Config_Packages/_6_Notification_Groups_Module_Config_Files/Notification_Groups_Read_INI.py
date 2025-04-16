from pathlib import Path
import configparser

file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\6_Notification_Groups\\Data_From_INI\\Notification_Groups.ini"
print(file_path)


class Read_Notification_Groups_Components:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.common_test_data_config = configparser.RawConfigParser()
        try:
            self.config.read(file_path)
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print(ex.args)

    def get_so_user_role_description(self):
        try:
            so_user_description = self.common_test_data_config.get("User_Roles_Data", "so_user_role_description")
            print(f"so_user_role_description: {so_user_description}")
            return so_user_description
        except Exception as ex:
            print(ex.args)

    def get_role_option_in_user_role_dropdown_by_xpath(self):
        try:
            role_option_in_user_role_dropdown_by_xpath = self.config.get("LOCATORS",
                                                                         "role_option_in_user_role_dropdown_by_xpath")
            print(f"role_option_in_user_role_dropdown_by_xpath: {role_option_in_user_role_dropdown_by_xpath}")
            return role_option_in_user_role_dropdown_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_CLOUD_MENU_button_by_xpath(self):
        try:
            CLOUD_MENU_button_by_xpath = self.config.get("LOCATORS", "CLOUD_MENU_button_by_xpath")
            print("CLOUD_MENU_button_by_xpath: ", CLOUD_MENU_button_by_xpath)
            return CLOUD_MENU_button_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_close_all_panels_menu_by_xpath(self):
        try:
            close_all_panels_menu_by_xpath = self.config.get("LOCATORS", "close_all_panels_menu_by_xpath")
            print("close_all_panels_menu_by_xpath: ", close_all_panels_menu_by_xpath)
            return close_all_panels_menu_by_xpath
        except Exception as ex:
            print(ex.args)


    def get_close_panel_button_by_xpath(self):
        try:
            close_panel_button = self.config.get("LOCATORS", "close_panel_button_by_xpath")
            print("close_panel_button_by_xpath: ", close_panel_button)
            return close_panel_button
        except Exception as ex:
            print(ex)

    def notification_groups_title_by_xpath(self):
        try:
            notification_groups_title_by_xpath = self.config.get("LOCATORS", "notification_groups_title_by_xpath")
            return notification_groups_title_by_xpath
        except Exception as ex:
            print("notification_groups_title_by_xpath : ", ex)

    def notification_groups_button_by_xpath(self):
        try:
            notification_groups_button_by_xpath = self.config.get("LOCATORS", "notification_groups_button_by_xpath")
            return notification_groups_button_by_xpath
        except Exception as ex:
            print("notification_groups_button_by_xpath : ", ex)

    def notification_group_title_validation_text(self):
        try:
            notification_group_title_validation_text = self.common_test_data_config.get("Notification_Groups_Data", "notification_group_title_validation_text")
            return notification_group_title_validation_text
        except Exception as ex:
            print("notification_group_title_validation_text : ", ex)

    def action_dropdown_button_by_xpath(self):
        try:
            action_dropdown_button_by_xpath = self.config.get("LOCATORS", "action_dropdown_button_by_xpath")
            return action_dropdown_button_by_xpath
        except Exception as ex:
            print("action_dropdown_menu_by_xpath : ", ex)

    def create_notification_group_btn_by_xpath(self):
        try:
            create_notification_group_btn_by_xpath = self \
                .config.get("LOCATORS", "create_notification_group_btn_by_xpath")
            return create_notification_group_btn_by_xpath
        except Exception as ex:
            print("create_notification_group_btn_by_xpath : ", ex)

    def delete_button_by_xpath(self):
        try:
            delete_button_by_xpath = self.config.get("LOCATORS", "delete_button_by_xpath")
            return delete_button_by_xpath
        except Exception as ex:
            print("delete_button_by_xpath : ", ex)

    def delete_popup_yes_btn_by_xpath(self):
        try:
            delete_popup_yes_btn_by_xpath = self.config.get("LOCATORS", "delete_popup_yes_btn_by_xpath")
            return delete_popup_yes_btn_by_xpath
        except Exception as ex:
            print("delete_popup_yes_btn_by_xpath : ", ex)

    def refresh_button_by_xpath(self):
        try:
            refresh_button_by_xpath = self.config.get("LOCATORS", "refresh_button_by_xpath")
            return refresh_button_by_xpath
        except Exception as ex:
            print("refresh_button_by_xpath : ", ex)

    def events_refresh_button_by_xpath(self):
        try:
            events_refresh_button_by_xpath = self.config.get("LOCATORS", "events_refresh_button_by_xpath")
            return events_refresh_button_by_xpath
        except Exception as ex:
            print("events_refresh_button_by_xpath : ", ex)

    def notification_groups_details_validation_text(self):
        try:
            notification_groups_details_validation_text = self.common_test_data_config \
                .get("Notification_Groups_Data", "notification_groups_details_validation_text")
            return notification_groups_details_validation_text
        except Exception as ex:
            print("notification_groups_details_validation_text : ", ex)

    def notification_group_details_by_xpath(self):
        try:
            notification_group_details_by_xpath = self.config \
                .get("LOCATORS", "notification_group_details_by_xpath")
            return notification_group_details_by_xpath
        except Exception as ex:
            print("notification_group_details_by_xpath : ", ex)

    def notification_group_details_sub_title_validation_text(self):
        try:
            notification_group_details_sub_title_validation_text = self.common_test_data_config \
                .get("Notification_Groups_Data", "notification_group_details_sub_title_validation_text")
            return notification_group_details_sub_title_validation_text
        except Exception as ex:
            print("notification_group_details_sub_title_validation_text : ", ex)

    def notification_group_details_sub_title_by_xpath(self):
        try:
            notification_group_details_sub_title_by_xpath = self.config \
                .get("LOCATORS", "notification_group_details_sub_title_by_xpath")
            return notification_group_details_sub_title_by_xpath
        except Exception as ex:
            print("notification_group_details_sub_title_by_xpath : ", ex)

    def cancel_button_validation_text(self):
        try:
            cancel_button_validation_text = self.common_test_data_config \
                .get("Notification_Groups_Data", "cancel_button_validation_text")
            return cancel_button_validation_text
        except Exception as ex:
            print("cancel_button_validation_text : ", ex)

    def cancel_button_by_xpath(self):
        try:
            cancel_button_by_xpath = self.config \
                .get("LOCATORS", "cancel_button_by_xpath")
            return cancel_button_by_xpath
        except Exception as ex:
            print("cancel_button_by_xpath : ", ex)

    def save_button_validation_text(self):
        try:
            save_button_validation_text = self.common_test_data_config \
                .get("Notification_Groups_Data", "save_button_validation_text")
            return save_button_validation_text
        except Exception as ex:
            print("save_button_validation_text : ", ex)

    def save_button_by_xpath(self):
        try:
            save_button_by_xpath = self.config \
                .get("LOCATORS", "save_button_by_xpath")
            return save_button_by_xpath
        except Exception as ex:
            print("save_button_by_xpath : ", ex)

    def name_field_validation_text(self):
        try:
            name_field_validation_text = self.common_test_data_config \
                .get("Notification_Groups_Data", "name_field_validation_text")
            return name_field_validation_text
        except Exception as ex:
            print("name_field_validation_text : ", ex)

    def name_field_by_xpath(self):
        try:
            name_field_by_xpath = self.config \
                .get("LOCATORS", "name_field_by_xpath")
            return name_field_by_xpath
        except Exception as ex:
            print("name_field_by_xpath : ", ex)

    def name_field_data(self):
        try:
            name_field_data = self.common_test_data_config \
                .get("Notification_Groups_Data", "name")
            return name_field_data
        except Exception as ex:
            print("name_field_data : ", ex)

    def description_field_by_xpath(self):
        try:
            description_field_by_xpath = self.config \
                .get("LOCATORS", "description_field_by_xpath")
            return description_field_by_xpath
        except Exception as ex:
            print("description_field_by_xpath : ", ex)

    def description_title_name_validation(self):
        try:
            description_field_by_xpath = self.common_test_data_config \
                .get("Notification_Groups_Data", "description_title_name_validation")
            return description_field_by_xpath
        except Exception as ex:
            print("description_field_by_xpath : ", ex)

    def description_field_data(self):
        try:
            description_field_data = self.common_test_data_config \
                .get("Notification_Groups_Data", "description")
            return description_field_data
        except Exception as ex:
            print("description_field_data : ", ex)

    def user_close_panel_and_discard_changes(self):
        try:
            ele = self.config.get('LOCATORS', 'user_close_panel_and_discard_Changes_by_xpath')
            return ele
        except Exception as ex:
            print(ex)

    def alert_group_list_by_xpath(self):
        try:
            alert_group_list_by_xpath = self.config.get("LOCATORS", "alert_group_list_by_xpath")
            return alert_group_list_by_xpath
        except Exception as ex:
            print(ex.args)

    def alert_checkbox_by_xpath(self):
        try:
            alert_checkbox_by_xpath = self.config.get("LOCATORS", "alert_checkbox_by_xpath")
            return alert_checkbox_by_xpath
        except Exception as ex:
            print(ex.args)
    def error_message_by_xpath(self):
        try:
            error_message_by_xpath = self.config \
                .get("LOCATORS", "error_message_by_xpath")
            return error_message_by_xpath
        except Exception as ex:
            print("error_message_by_xpath : ", ex)

    def error_message_validation_text(self):
        try:
            error_message_validation_text = self.common_test_data_config \
                .get("Notification_Groups_Data", "error_message_validation_text")
            return error_message_validation_text
        except Exception as ex:
            print("error_message_validation_text : ", ex)

    def success_message_by_xpath(self):
        try:
            success_message_by_xpath = self.config \
                .get("LOCATORS", "success_message_by_xpath")
            return success_message_by_xpath
        except Exception as ex:
            print("success_message_by_xpath : ", ex)

    def success_message_validation_text(self):
        try:
            success_message_validation_text = self.common_test_data_config \
                .get("Notification_Groups_Data", "success_message_validation_text")
            return success_message_validation_text
        except Exception as ex:
            print("success_message_validation_text : ", ex)

    def user_button_by_xpath(self):
        try:
            user_button_by_xpath = self.config \
                .get("LOCATORS", "user_button_by_xpath")
            return user_button_by_xpath
        except Exception as ex:
            print("validation_error_message_by_xpath : ", ex)

    def enrollment_group_btn_by_xpath(self):
        try:
            enrollment_group_btn_by_xpath = self.config \
                .get("LOCATORS", "enrollment_group_btn_by_xpath")
            return enrollment_group_btn_by_xpath
        except Exception as ex:
            print("validation_error_message_by_xpath : ", ex)

    def event_button_by_xpath(self):
        try:
            event_button_by_xpath = self.config \
                .get("LOCATORS", "event_button_by_xpath")
            return event_button_by_xpath
        except Exception as ex:
            print("validation_error_message_by_xpath : ", ex)

    def delete_selected_option_validation_text(self):
        try:
            delete_selected_option_validation_text = self.common_test_data_config \
                .get("Notification_Groups_Data", "delete_selected_option_validation_text")
            return delete_selected_option_validation_text
        except Exception as ex:
            print("delete_selected_option_validation_text : ", ex)

    def delete_selected_option_by_xpath(self):
        try:
            delete_selected_option_by_xpath = self.config \
                .get("LOCATORS", "delete_selected_option_by_xpath")
            return delete_selected_option_by_xpath
        except Exception as ex:
            print("delete_selected_option_by_xpath : ", ex)

    def checkbox_by_xpath(self):
        try:
            checkbox_by_xpath = self.config \
                .get("LOCATORS", "checkbox_by_xpath")
            return checkbox_by_xpath
        except Exception as ex:
            print("checkbox_by_xpath : ", ex)

    def select_all_by_xpath(self):
        try:
            select_all_by_xpath = self.config \
                .get("LOCATORS", "select_all_by_xpath")
            return select_all_by_xpath
        except Exception as ex:
            print("select_all_by_xpath : ", ex)

    def select_checkbox_by_xpath(self):
        try:
            select_checkbox_by_xpath = self.config \
                .get("LOCATORS", "select_checkbox_by_xpath")
            return select_checkbox_by_xpath
        except Exception as ex:
            print("select_checkbox_by_xpath : ", ex)

    def check_box_list_by_xpath(self):
        try:
            check_box_list_by_xpath = self.config \
                .get("LOCATORS", "check_box_list_by_xpath")
            return check_box_list_by_xpath
        except Exception as ex:
            print("check_box_list_by_xpath : ", ex)

    def notification_groups_details_action_dropdown_button_by_xpath(self):
        try:
            notification_groups_details_action_dropdown_button_by_xpath = self.config \
                .get("LOCATORS", "notification_groups_details_action_dropdown_button_by_xpath")
            return notification_groups_details_action_dropdown_button_by_xpath
        except Exception as ex:
            print("notification_groups_details_action_dropdown_button_by_xpath : ", ex)

    def edit_button_by_xpath(self):
        try:
            edit_button_by_xpath = self.config \
                .get("LOCATORS", "edit_button_by_xpath")
            return edit_button_by_xpath
        except Exception as ex:
            print("edit_button_by_xpath : ", ex)

    def validation_error_message_validation_text(self):
        try:
            ele = self.common_test_data_config.get('Notification_Groups_Data', 'error_message_validation_text')
            return ele
        except Exception as ex:
            print(ex)

    def validation_error_message_by_xpath(self):
        try:
            validation_error_message_by_xpath = self.config \
                .get("LOCATORS", "error_message_by_xpath")
            return validation_error_message_by_xpath
        except Exception as ex:
            print("error_message_by_xpath : ", ex)

    def description_field_new_data(self):
        try:
            description_field_new_data = self.common_test_data_config \
                .get("Notification_Groups_Data", "new description")
            return description_field_new_data
        except Exception as ex:
            print("description_field_data : ", ex)

    def new_name_field_data(self):
        try:
            new_name_field_data = self.common_test_data_config \
                .get("Notification_Groups_Data", "new name")
            return new_name_field_data
        except Exception as ex:
            print("new_name_field_data : ", ex)

    def new_second_action_dropdown_button_by_xpath(self):
        try:
            second_action_dropdown_button_by_xpath = self.config \
                .get("LOCATORS", "second_action_dropdown_button_by_xpath")
            return second_action_dropdown_button_by_xpath
        except Exception as ex:
            print("new_second_action_dropdown_button_by_xpath : ", ex)

    def create_users_by_xpath(self):
        try:
            create_users_by_xpath = self.config \
                .get("LOCATORS", "create_users_by_xpath")
            return create_users_by_xpath
        except Exception as ex:
            print("create_users_by_xpath : ", ex)

    def create_enrollment_group_by_xpath(self):
        try:
            create_enrollment_group_by_xpath = self.config \
                .get("LOCATORS", "create_enrollment_group_by_xpath")
            return create_enrollment_group_by_xpath
        except Exception as ex:
            print("create_enrollment_group_by_xpath : ", ex)

    def user_action_drpdwn_button_by_xpath(self):
        try:
            user_action_drpdwn_button_by_xpath = self.config \
                .get("LOCATORS", "user_action_drpdwn_button_by_xpath")
            return user_action_drpdwn_button_by_xpath
        except Exception as ex:
            print("user_action_drpdwn_button_by_xpath : ", ex)

    def users_panel_title_by_xpath(self):
        try:
            users_panel_title_by_xpath = self.config.get("LOCATORS", "users_panel_title_by_xpath")
            return users_panel_title_by_xpath
        except Exception as ex:
            print(ex)

    def users_panel_title_validation_text(self):
        try:
            users_panel_title_validation_text = self.common_test_data_config.get("Notification_Groups_Data", "users_panel_title_validation_text")
            return users_panel_title_validation_text
        except Exception as ex:
            print(ex)

    def third_action_dropdown_button_by_xpath(self):
        try:
            third_action_dropdown_button_by_xpath = self.config \
                .get("LOCATORS", "third_action_dropdown_button_by_xpath")
            return third_action_dropdown_button_by_xpath
        except Exception as ex:
            print("third_action_dropdown_button_by_xpath : ", ex)

    def user_name_by_xpath(self):
        try:
            user_name_by_xpath = self.config.get("LOCATORS", "user_name_by_xpath")
            return user_name_by_xpath
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
            user_role_input_data = self.common_test_data_config.get("Notification_Groups_Data", "user_role_input_data")
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

    def user_role_by_xpath(self):
        try:
            user_role_by_xpath = self.config.get("LOCATORS", "user_role_by_xpath")
            return user_role_by_xpath
        except Exception as ex:
            print(ex)

    def new_password_by_xpath(self):
        try:
            new_password_by_xpath = self.config.get("LOCATORS", "new_password_by_xpath")
            return new_password_by_xpath
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

    def first_name_input_data(self):
        try:
            first_name_input_data = self.common_test_data_config.get("Notification_Groups_Data", "first_name_input_data")
            return first_name_input_data
        except Exception as ex:
            print(ex)

    def last_name_input_data(self):
        try:
            last_name_input_data = self.common_test_data_config.get("Notification_Groups_Data", "last_name_input_data")
            return last_name_input_data
        except Exception as ex:
            print(ex)

    # def error_message_by_xpath(self):
    #     try:
    #         error_message_by_xpath = self.config.get("LOCATORS", "error_message_by_xpath")
    #         return error_message_by_xpath
    #     except Exception as ex:
    #         print(ex)

    def error_msg_validation_text(self):
        try:
            error_msg_validation_text = self.common_test_data_config.get("Notification_Groups_Data", "error_msg_validation_text")
            return error_msg_validation_text
        except Exception as ex:
            print(ex)

    def time_zone_by_xpath(self):
        try:
            time_zone_by_xpath = self.config.get("LOCATORS", "time_zone_by_xpath")
            return time_zone_by_xpath
        except Exception as ex:
            print(ex)

    def time_zone_input_data(self):
        try:
            time_zone_input_data = self.common_test_data_config.get("Notification_Groups_Data", "time_zone_input_data")
            return time_zone_input_data
        except Exception as ex:
            print(ex)

    def email_input_data(self):
        try:
            email_input_data = self.common_test_data_config.get("Notification_Groups_Data", "email_input_data")
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
            password_data_input = self.common_test_data_config.get("Notification_Groups_Data", "password_data_input")
            return password_data_input
        except Exception as ex:
            print(ex)

    def user_name_input_data(self):
        try:
            user_name_input_data = self.common_test_data_config.get("Notification_Groups_Data", "user_name_input_data")
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

    def user_details_user_role_by_xpath(self):
        try:
            user_details_user_role_by_xpath = self.config.get("LOCATORS", "user_details_user_role_by_xpath")
            return user_details_user_role_by_xpath
        except Exception as ex:
            print(ex)

    def region_by_xpath(self):
        try:
            region_by_xpath = self.config.get("LOCATORS", "region_by_xpath")
            return region_by_xpath
        except Exception as ex:
            print(ex)

    def confirm_password_by_xpath(self):
        try:
            confirm_password_by_xpath = self.config.get("LOCATORS", "confirm_password_by_xpath")
            return confirm_password_by_xpath
        except Exception as ex:
            print(ex)

    def company_input_data(self):
        try:
            company_input_data = self.common_test_data_config.get("Notification_Groups_Data", "company_input_data")
            return company_input_data
        except Exception as ex:
            print(ex)

    def title_input_data(self):
        try:
            title_input_data = self.common_test_data_config.get("Notification_Groups_Data", "title_input_data")
            return title_input_data
        except Exception as ex:
            print(ex)

    def department_input_data(self):
        try:
            department_input_data = self.common_test_data_config.get("Notification_Groups_Data", "department_input_data")
            return department_input_data
        except Exception as ex:
            print(ex)

    def alert_email_input_data(self):
        try:
            alert_email_input_data = self.common_test_data_config.get("Notification_Groups_Data", "alert_email_input_data")
            return alert_email_input_data
        except Exception as ex:
            print(ex)

    def alert_phone_no_input_data(self):
        try:
            alert_phone_no_input_data = self.common_test_data_config.get("Notification_Groups_Data", "alert_phone_no_input_data")
            return alert_phone_no_input_data
        except Exception as ex:
            print(ex)

    def address_input_data(self):
        try:
            address_input_data = self.common_test_data_config.get("Notification_Groups_Data", "address_input_data")
            return address_input_data
        except Exception as ex:
            print(ex)

    def address2_input_data(self):
        try:
            address2_input_data = self.common_test_data_config.get("Notification_Groups_Data", "address2_input_data")
            return address2_input_data
        except Exception as ex:
            print(ex)

    def city_input_data(self):
        try:
            city_input_data = self.common_test_data_config.get("Notification_Groups_Data", "city_input_data")
            return city_input_data
        except Exception as ex:
            print(ex)

    def state_input_data(self):
        try:
            state_input_data = self.common_test_data_config.get("Notification_Groups_Data", "state_input_data")
            return state_input_data
        except Exception as ex:
            print(ex)

    def postal_code_input_data(self):
        try:
            postal_code_input_data = self.common_test_data_config.get("Notification_Groups_Data", "postal_code_input_data")
            return postal_code_input_data
        except Exception as ex:
            print(ex)

    def home_phone_no_input_data(self):
        try:
            home_phone_no_input_data = self.common_test_data_config.get("Notification_Groups_Data", "home_phone_no_input_data")
            return home_phone_no_input_data
        except Exception as ex:
            print(ex)

    def work_phone_no_input_data(self):
        try:
            work_phone_no_input_data = self.common_test_data_config.get("Notification_Groups_Data", "work_phone_no_input_data")
            return work_phone_no_input_data
        except Exception as ex:
            print(ex)

    def fax_phone_no_input_data(self):
        try:
            fax_phone_no_input_data = self.common_test_data_config.get("Notification_Groups_Data", "fax_phone_no_input_data")
            return fax_phone_no_input_data
        except Exception as ex:
            print(ex)

    def phone_type_input_data(self):
        try:
            phone_type_input_data = self.common_test_data_config.get("Notification_Groups_Data", "phone_type_input_data")
            return phone_type_input_data
        except Exception as ex:
            print(ex)

    def phone_provider_input_data(self):
        try:
            phone_provider_input_data = self.common_test_data_config.get("Notification_Groups_Data", "phone_provider_input_data")
            return phone_provider_input_data
        except Exception as ex:
            print(ex)

    def success_msg_validation_text(self):
        try:
            success_msg_validation_text = self.common_test_data_config.get("Notification_Groups_Data", "success_msg_validation_text")
            return success_msg_validation_text
        except Exception as ex:
            print(ex)

    def user_email_by_xpath(self):
        try:
            user_email_by_xpath = self.config.get("LOCATORS", "user_email_by_xpath")
            return user_email_by_xpath
        except Exception as ex:
            print(ex)

    def second_save_button_by_xpath(self):
        try:
            second_save_button_by_xpath = self.config.get("LOCATORS", "second_save_button_by_xpath")
            return second_save_button_by_xpath
        except Exception as ex:
            print(ex)

    def search_box_by_xpath(self):
        try:
            search_box_by_xpath = self.config.get("LOCATORS", "search_box_by_xpath")
            return search_box_by_xpath
        except Exception as ex:
            print(ex)

    def users_list_board_username_by_xpath(self):
        try:
            users_list_board_username_by_xpath = self.config.get("LOCATORS", "users_list_board_username_by_xpath")
            return users_list_board_username_by_xpath
        except Exception as ex:
            print(ex)

    def events_action_dropdown_button_by_xpath(self):
        try:
            events_action_dropdown_button_by_xpath = self.config.get("LOCATORS",
                                                                     "events_action_dropdown_button_by_xpath")
            return events_action_dropdown_button_by_xpath
        except Exception as ex:
            print(ex)

    def users_filter_button_by_xpath(self):
        try:
            users_filter_button_by_xpath = self.config.get("LOCATORS", "users_filter_button_by_xpath")
            return users_filter_button_by_xpath
        except Exception as ex:
            print(ex)

    def user_filter_drp_dwn_button_by_xpath(self):
        try:
            user_filter_drp_dwn_button_by_xpath = self.config.get("LOCATORS",
                                                                  "user_filter_drp_dwn_button_by_xpath")
            return user_filter_drp_dwn_button_by_xpath
        except Exception as ex:
            print(ex)

    def users_search_box_by_xpath(self):
        try:
            users_search_box_by_xpath = self.config.get("LOCATORS", "users_search_box_by_xpath")
            return users_search_box_by_xpath
        except Exception as ex:
            print(ex)

    def users_select_check_box_by_xpath(self):
        try:
            users_select_check_box_by_xpath = self.config.get("LOCATORS",
                                                              "users_select_check_box_by_xpath")
            return users_select_check_box_by_xpath
        except Exception as ex:
            print(ex)

    def add_users_by_xpath(self):
        try:
            add_users_by_xpath = self.config.get("LOCATORS","add_users_by_xpath")
            return add_users_by_xpath
        except Exception as ex:
            print(ex)

    def register_username_by_xpath(self):
        try:
            register_username_by_xpath = self.config.get("LOCATORS", "register_username_by_xpath")
            return register_username_by_xpath
        except Exception as ex:
            print(ex)

    def register_username_validation_text(self):
        try:
            register_username_validation_text = self.common_test_data_config.get("Notification_Groups_Data", "register_username_validation_text")
            return register_username_validation_text
        except Exception as ex:
            print(ex)

    def unlinked_enrollment_group_by_xpath(self):
        try:
            unlinked_enrollment_group_by_xpath = self.config.get("LOCATORS",
                                                                 "unlinked_enrollment_group_by_xpath")
            return unlinked_enrollment_group_by_xpath
        except Exception as ex:
            print(ex)

    def enrollment_name(self, enrollment_name):
        try:
            ele = self.config.get("DYNAMIC_XPATH", "enrollment_name")
            return ele.format(enrollment_name)
        except Exception as ex:
            print(ex)

    def notification_group_name_delete(self, notification_group_name_delete):
        try:
            ele = self.config.get("DYNAMIC_XPATH", "notification_group_name_delete")
            return ele.format(notification_group_name_delete)
        except Exception as ex:
            print(ex)


    def name_field_by_xpath_enrolment(self):
        try:
            name_field_by_xpath_enrolment = self.config.get("LOCATORS","name_field_by_xpath_enrolment")
            return name_field_by_xpath_enrolment
        except Exception as ex:
            print(ex)

    def add_alert_to_groups(self):
        try:
            add_alert_to_groups = self.config.get("LOCATORS","add_alert_to_groups")
            return add_alert_to_groups
        except Exception as ex:
            print(ex)

    def registered_enrollment_groups(self):
        try:
            registered_enrollment_groups = self.config.get("LOCATORS","registered_enrollment_groups")
            return registered_enrollment_groups
        except Exception as ex:
            print(ex)

    def delete_selected_notification_groups(self):
        try:
            delete_selected_notification_groups = self.config.get("LOCATORS","delete_selected_notification_groups")
            return delete_selected_notification_groups
        except Exception as ex:
            print(ex)

    def refreshing_panel_validation_by_xpath(self):
        try:
            refreshing_panel_validation_by_xpath = self.config.get("LOCATORS", "refreshing_panel_validation_by_xpath")
            return refreshing_panel_validation_by_xpath
        except Exception as ex:
            print(ex.args)





