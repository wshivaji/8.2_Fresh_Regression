from pathlib import Path
import configparser
import datetime as dt

file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\System_Level_Test\\Data_From_INI\\system_level_test.ini"
print(file_path)


class system_level_test_read_ini:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
        self.common_test_data_config = configparser.RawConfigParser()
        self.common_test_data_config.read(common_test_data_ini_file_path)
        try:
            self.config.read(file_path)
        except Exception as ex:
            print(ex.args)

    def get_SO_user_role(self):
        try:
            SO_user_role = self.common_test_data_config.get("system_level_test_Data", "SO_user_role")
            print(f"SO_user_role: {SO_user_role}")
            return SO_user_role
        except Exception as ex:
            print(ex.args)

    def get_SO_user_role_description(self):
        try:
            SO_user_role_description = self.common_test_data_config.get("system_level_test_Data", "SO_user_role_description")
            print(f"SO_user_role_description: {SO_user_role_description}")
            return SO_user_role_description
        except Exception as ex:
            print(ex.args)

    def get_AB_user_role(self):
        try:
            AB_user_role = self.common_test_data_config.get("system_level_test_Data", "AB_user_role")
            print(f"AB_user_role: {AB_user_role}")
            return AB_user_role
        except Exception as ex:
            print(ex.args)

    def get_AB_user_role_description(self):
        try:
            AB_user_role_description = self.common_test_data_config.get("system_level_test_Data", "AB_user_role_description")
            print(f"AB_user_role_description: {AB_user_role_description}")
            return AB_user_role_description
        except Exception as ex:
            print(ex.args)

    def get_PT_user_role(self):
        try:
            PT_user_role = self.common_test_data_config.get("system_level_test_Data", "PT_user_role")
            print(f"PT_user_role: {PT_user_role}")
            return PT_user_role
        except Exception as ex:
            print(ex.args)

    def get_PT_user_role_description(self):
        try:
            PT_user_role_description = self.common_test_data_config.get("system_level_test_Data", "PT_user_role_description")
            print(f"PT_user_role_description: {PT_user_role_description}")
            return PT_user_role_description
        except Exception as ex:
            print(ex.args)

    def get_FRAUD_user_role(self):
        try:
            FRAUD_user_role = self.common_test_data_config.get("system_level_test_Data", "FRAUD_user_role")
            print(f"FRAUD_user_role: {FRAUD_user_role}")
            return FRAUD_user_role
        except Exception as ex:
            print(ex.args)

    def get_FRAUD_user_role_description(self):
        try:
            FRAUD_user_role_description = self.common_test_data_config.get("system_level_test_Data", "FRAUD_user_role_description")
            print(f"FRAUD_user_role_description: {FRAUD_user_role_description}")
            return FRAUD_user_role_description
        except Exception as ex:
            print(ex.args)

    def get_VIP_user_role(self):
        try:
            VIP_user_role = self.common_test_data_config.get("system_level_test_Data", "VIP_user_role")
            print(f"VIP_user_role: {VIP_user_role}")
            return VIP_user_role
        except Exception as ex:
            print(ex.args)

    def get_VIP_user_role_description(self):
        try:
            VIP_user_role_description = self.common_test_data_config.get("system_level_test_Data", "VIP_user_role_description")
            print(f"VIP_user_role_description: {VIP_user_role_description}")
            return VIP_user_role_description
        except Exception as ex:
            print(ex.args)

    def get_action_dropdown_on_users_panel_by_xpath(self):
        try:
            action_dropdown_on_users_panel_by_xpath = self.config.get("Integration", "action_dropdown_on_users_panel_by_xpath")
            print(f"action_dropdown_on_users_panel_by_xpath: {action_dropdown_on_users_panel_by_xpath}")
            return action_dropdown_on_users_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_create_user_by_xpath(self):
        try:
            create_user_by_xpath = self.config.get("Integration", "create_user_by_xpath")
            print(f"create_user_by_xpath: {create_user_by_xpath}")
            return create_user_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_name_input_data(self):
        try:
            user_name_input_data = self.common_test_data_config.get("system_level_test_Data", "user_name_input_data")
            print(f"user_name_input_data: {user_name_input_data}")
            return user_name_input_data
        except Exception as ex:
            print(ex.args)

    def get_user_name_integration(self):
        try:
            user_name_integration = self.common_test_data_config.get("system_level_test_Data", "user_name_integration")
            print(f"user_name_integration: {user_name_integration}")
            return user_name_integration
        except Exception as ex:
            print(ex.args)

    def get_dummy_enrollment_group_name(self):
        try:
            dummy_enrollment_group_name = self.common_test_data_config.get("system_level_test_Data", "dummy_enrollment_group_name")
            print(f"dummy_enrollment_group_name: {dummy_enrollment_group_name}")
            return dummy_enrollment_group_name
        except Exception as ex:
            print(ex.args)

    def get_dummy_notification_group_name(self):
        try:
            dummy_notification_group_name = self.common_test_data_config.get("system_level_test_Data", "dummy_notification_group_name")
            print(f"dummy_notification_group_name: {dummy_notification_group_name}")
            return dummy_notification_group_name
        except Exception as ex:
            print(ex.args)

    def get_user_name_textbox_by_xpath(self):
        try:
            user_name_textbox_by_xpath = self.config.get("Integration", "user_name_textbox_by_xpath")
            print(f"user_name_textbox_by_xpath: {user_name_textbox_by_xpath}")
            return user_name_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_first_name_input_data(self):
        try:
            first_name_input_data = self.common_test_data_config.get("system_level_test_Data", "first_name_input_data")
            print(f"first_name_input_data: {first_name_input_data}")
            return first_name_input_data
        except Exception as ex:
            print(ex.args)

    def get_last_name_input_data(self):
        try:
            last_name_input_data = self.common_test_data_config.get("system_level_test_Data", "last_name_input_data")
            print(f"last_name_input_data: {last_name_input_data}")
            return last_name_input_data
        except Exception as ex:
            print(ex.args)

    def get_password_data_input(self):
        try:
            password_data_input = self.common_test_data_config.get("Login_Logout_Data", "password")
            print(f"password_data_input: {password_data_input}")
            return password_data_input
        except Exception as ex:
            print(ex.args)

    def get_region_by_xpath(self):
        try:
            region_by_xpath = self.config.get("Integration", "region_by_xpath")
            print(f"region_by_xpath: {region_by_xpath}")
            return region_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_region_list_by_xpath(self):
        try:
            region_list_by_xpath = self.config.get("Integration", "region_list_by_xpath")
            return region_list_by_xpath
        except Exception as ex:
            print(ex)

    def get_region_save_btn_by_xpath(self):
        try:
            region_save_btn_by_xpath = self.config.get("Integration", "region_save_btn_by_xpath")
            return region_save_btn_by_xpath
        except Exception as ex:
            print(ex)

    def get_region_data_input(self):
        try:
            region_data_input = self.common_test_data_config.get("system_level_test_Data", "region_data_input")
            return region_data_input
        except Exception as ex:
            print(ex)

    def get_email_by_xpath(self):
        try:
            email_by_xpath = self.config.get("Integration", "email_by_xpath")
            return email_by_xpath
        except Exception as ex:
            print(ex)

    def get_email_input_data(self):
        try:
            email_input_data = self.common_test_data_config.get("system_level_test_Data", "email_input_data")
            return email_input_data
        except Exception as ex:
            print(ex)

    def get_time_zone_by_xpath(self):
        try:
            time_zone_by_xpath = self.config.get("Integration", "time_zone_by_xpath")
            return time_zone_by_xpath
        except Exception as ex:
            print(ex)

    def get_time_zone_input_data(self):
        try:
            time_zone_input_data = self.common_test_data_config.get("system_level_test_Data", "time_zone_input_data")
            return time_zone_input_data
        except Exception as ex:
            print(ex)

    def get_user_panel_save_button_by_xpath(self):
        try:
            user_panel_save_button_by_xpath = self.config.get("Integration", "user_panel_save_button_by_xpath")
            return user_panel_save_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_success_message_by_xpath(self):
        try:
            success_message_by_xpath = self.config.get("Integration", "success_message_by_xpath")
            return success_message_by_xpath
        except Exception as ex:
            print(ex)

    def get_success_msg_validation_text(self):
        try:
            success_msg_validation_text = self.common_test_data_config.get("system_level_test_Data", "success_msg_validation_text")
            return success_msg_validation_text
        except Exception as ex:
            print(ex)

    def get_notification_group_name(self):
        try:
            notification_group_name = self.common_test_data_config.get("system_level_test_Data", "notification_group_name")
            return notification_group_name
        except Exception as ex:
            print(ex)

    def get_notification_group_name_integration(self):
        try:
            notification_group_name = self.config.get("Integration", "notification_group_name")
            return notification_group_name
        except Exception as ex:
            print(ex)

    def get_dummy_notification_group_name(self):
        try:
            notification_group_name = self.common_test_data_config.get("system_level_test_Data", "dummy_notification_group_name")
            return notification_group_name
        except Exception as ex:
            print(ex)

    def get_dummy_notification_group_name_1(self):
        try:
            notification_group_name = self.common_test_data_config.get("system_level_test_Data", "dummy_notification_group_name_1")
            return notification_group_name
        except Exception as ex:
            print(ex)

    def get_notification_group_description(self):
        try:
            notification_group_description = self.common_test_data_config.get("system_level_test_Data", "notification_group_description")
            return notification_group_description
        except Exception as ex:
            print(ex)

    def get_create_enrollment_group_btn_by_xpath(self):
        try:
            create_enrollment_group_btn_by_xpath = self.config.get("Integration", "create_enrollment_group_btn_by_xpath")
            return create_enrollment_group_btn_by_xpath
        except Exception as ex:
            print(ex)

    def get_name_field_by_xpath(self):
        try:
            name_field_by_xpath = self.config.get("Integration", "name_field_by_xpath")
            return name_field_by_xpath
        except Exception as ex:
            print(ex)

    def get_enrollment_group_name(self):
        try:
            enrollment_group_name = self.common_test_data_config.get("system_level_test_Data", "enrollment_group_name")
            return enrollment_group_name
        except Exception as ex:
            print(ex)

    def get_enrollment_group_name_integration(self):
        try:
            enrollment_group_name = self.config.get("Integration", "enrollment_group_name")
            return enrollment_group_name
        except Exception as ex:
            print(ex)

    def get_enrollment_group_description(self):
        try:
            enrollment_group_description = self.common_test_data_config.get("system_level_test_Data", "enrollment_group_description")
            return enrollment_group_description
        except Exception as ex:
            print(ex)

    def get_description_field_by_xpath(self):
        try:
            description_field_by_xpath = self.config.get("Integration", "description_field_by_xpath")
            return description_field_by_xpath
        except Exception as ex:
            print(ex)

    def get_save_button_on_enrollment_group_by_xpath(self):
        try:
            save_button_on_enrollment_group_by_xpath = self.config.get("Integration", "save_button_on_enrollment_group_by_xpath")
            return save_button_on_enrollment_group_by_xpath
        except Exception as ex:
            print(ex)

    def get_enrollment_group_success_message_validation_text(self):
        try:
            enrollment_group_success_message_validation_text = self.common_test_data_config.get("system_level_test_Data", "enrollment_group_success_message_validation_text")
            return enrollment_group_success_message_validation_text
        except Exception as ex:
            print(ex)

    def get_enrollment_group_success_message_by_xpath(self):
        try:
            enrollment_group_success_message_by_xpath = self.config.get("Integration", "enrollment_group_success_message_by_xpath")
            return enrollment_group_success_message_by_xpath
        except Exception as ex:
            print(ex)

    def get_notification_group_button_on_users_panel_by_xpath(self):
        try:
            notification_group_button_on_users_panel_by_xpath = self.config.get("Integration", "notification_group_button_on_users_panel_by_xpath")
            return notification_group_button_on_users_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_filter_btn_on_notification_groups_panel_by_xpath(self):
        try:
            filter_btn_on_notification_groups_panel_by_xpath = self.config.get("Integration", "filter_btn_on_notification_groups_panel_by_xpath")
            return filter_btn_on_notification_groups_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_unlinked_notification_groups_btn_by_xpath(self):
        try:
            unlinked_notification_groups_btn_by_xpath = self.config.get("Integration", "unlinked_notification_groups_btn_by_xpath")
            return unlinked_notification_groups_btn_by_xpath
        except Exception as ex:
            print(ex)

    def get_add_to_user_option_in_action_dropdown_by_xpath(self):
        try:
            add_to_user_option_in_action_dropdown_by_xpath = self.config.get("Integration", "add_to_user_option_in_action_dropdown_by_xpath")
            return add_to_user_option_in_action_dropdown_by_xpath
        except Exception as ex:
            print(ex)

    def get_action_dropdown_on_notification_groups_panel_by_xpath(self):
        try:
            action_dropdown_on_notification_groups_panel_by_xpath = self.config.get("Integration", "action_dropdown_on_notification_groups_panel_by_xpath")
            return action_dropdown_on_notification_groups_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_enrollment_groups_btn_on_notification_panel_by_xpath(self):
        try:
            enrollment_groups_btn_on_notification_panel_by_xpath = self.config.get("Integration", "enrollment_groups_btn_on_notification_panel_by_xpath")
            return enrollment_groups_btn_on_notification_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_filter_dropdown_on_enrollment_groups_panel_by_xpath(self):
        try:
            filter_dropdown_on_enrollment_groups_panel_by_xpath = self.config.get("Integration", "filter_dropdown_on_enrollment_groups_panel_by_xpath")
            return filter_dropdown_on_enrollment_groups_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_unlinked_enrollment_groups_btn_by_xpath(self):
        try:
            unlinked_enrollment_groups_btn_by_xpath = self.config.get("Integration", "unlinked_enrollment_groups_btn_by_xpath")
            return unlinked_enrollment_groups_btn_by_xpath
        except Exception as ex:
            print(ex)

    def get_case_groups_list_by_xpath(self):
        try:
            case_groups_list_by_xpath = self.config.get("Integration", "case_groups_list_by_xpath")
            return case_groups_list_by_xpath
        except Exception as ex:
            print(ex)

    def get_add_alert_to_groups_btn_by_xpath(self):
        try:
            add_alert_to_groups_btn_by_xpath = self.config.get("Integration", "add_alert_to_groups_btn_by_xpath")
            return add_alert_to_groups_btn_by_xpath
        except Exception as ex:
            print(ex)

    def get_action_dropdown_on_enrollment_groups_panel_by_xpath(self):
        try:
            action_dropdown_on_enrollment_groups_panel_by_xpath = self.config.get("Integration", "action_dropdown_on_enrollment_groups_panel_by_xpath")
            return action_dropdown_on_enrollment_groups_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_checkboxes_on_enrollment_groups_panel_by_xpath(self):
        try:
            checkboxes_on_enrollment_groups_panel_by_xpath = self.config.get("Integration", "checkboxes_on_enrollment_groups_panel_by_xpath")
            return checkboxes_on_enrollment_groups_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_unlinked_enrollment_groups_by_xpath(self):
        try:
            unlinked_enrollment_groups_by_xpath = self.config.get("Integration", "unlinked_enrollment_groups_by_xpath")
            return unlinked_enrollment_groups_by_xpath
        except Exception as ex:
            print(ex)

    def get_linked_enrollment_groups_by_xpath(self):
        try:
            linked_enrollment_groups_by_xpath = self.config.get("Integration", "linked_enrollment_groups_by_xpath")
            return linked_enrollment_groups_by_xpath
        except Exception as ex:
            print(ex)

    def get_notification_group_btn_on_cases_panel_by_xpath(self):
        try:
            notification_group_btn_on_cases_panel_by_xpath = self.config.get("Integration", "notification_group_btn_on_cases_panel_by_xpath")
            return notification_group_btn_on_cases_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_add_to_enrollment_groups_option_by_xpath(self):
        try:
            add_to_enrollment_groups_option_by_xpath = self.config.get("Integration", "add_to_enrollment_groups_option_by_xpath")
            return add_to_enrollment_groups_option_by_xpath
        except Exception as ex:
            print(ex)

    def get_users_btn_on_notification_groups_panel_by_xpath(self):
        try:
            users_btn_on_notification_groups_panel_by_xpath = self.config.get("Integration", "users_btn_on_notification_groups_panel_by_xpath")
            return users_btn_on_notification_groups_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_users_btn_on_notification_group_details_panel_by_xpath(self):
        try:
            users_btn_on_notification_group_details_panel_by_xpath = self.config.get("Integration",
                                                                              "users_btn_on_notification_group_details_panel_by_xpath")
            return users_btn_on_notification_group_details_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_filter_btn_on_users_panel_by_xpath(self):
        try:
            filter_btn_on_users_panel_by_xpath = self.config.get("Integration", "filter_btn_on_users_panel_by_xpath")
            return filter_btn_on_users_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_users_list_by_xpath(self):
        try:
            users_list_by_xpath = self.config.get("Integration", "users_list_by_xpath")
            return users_list_by_xpath
        except Exception as ex:
            print(ex)

    def get_checkboxes_on_users_panel_by_xpath(self):
        try:
            checkboxes_on_users_panel_by_xpath = self.config.get("Integration", "checkboxes_on_users_panel_by_xpath")
            return checkboxes_on_users_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_add_users_to_alert_btn_by_xpath(self):
        try:
            add_users_to_alert_btn_by_xpath = self.config.get("Integration", "add_users_to_alert_btn_by_xpath")
            return add_users_to_alert_btn_by_xpath
        except Exception as ex:
            print(ex)

    def get_notification_group_icon_btn_on_users_panel_by_xpath(self):
        try:
            notification_group_icon_btn_on_users_panel_by_xpath = self.config.get("Integration", "notification_group_icon_btn_on_users_panel_by_xpath")
            return notification_group_icon_btn_on_users_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_success_message_on_alert_group_creation_by_xpath(self):
        try:
            success_message_on_alert_group_creation_by_xpath = self.config.get("Integration", "success_message_on_alert_group_creation_by_xpath")
            return success_message_on_alert_group_creation_by_xpath
        except Exception as ex:
            print(ex)

    def get_success_message_on_case_group_creation_by_xpath(self):
        try:
            success_message_on_case_group_creation_by_xpath = self.config.get("Integration", "success_message_on_case_group_creation_by_xpath")
            return success_message_on_case_group_creation_by_xpath
        except Exception as ex:
            print(ex)

    def get_photo_upload_container_by_xpath(self):
        try:
            photo_upload_container_by_xpath = self.config.get("Integration", "photo_upload_container_by_xpath")
            return photo_upload_container_by_xpath
        except Exception as ex:
            print("photo_upload_container_by_xpath : ", ex)

    def get_submit_search_button_by_xpath(self):
        try:
            submit_search_button_by_xpath = self.config.get("Integration", "submit_search_button_by_xpath")
            return submit_search_button_by_xpath
        except Exception as ex:
            print("submit_search_button_by_xpath : ", ex)

    def get_no_matches_found(self):
        try:
            ele = self.config.get("Integration", "no_matches_found")
            return ele
        except Exception as ex:
            print("nats_checkbox_xpath : ", ex)

    def get_auto_refresh_on_by_xpath(self):
        try:
            auto_refresh_on_by_xpath = self.config.get("Integration", "auto_refresh_on_by_xpath")
            return auto_refresh_on_by_xpath
        except Exception as ex:
            print("auto_refresh_on_by_xpath : ", ex)

    def get_auto_refresh_off_by_xpath(self):
        try:
            auto_refresh_off_by_xpath = self.config.get("Integration", "auto_refresh_off_by_xpath")
            return auto_refresh_off_by_xpath
        except Exception as ex:
            print("auto_refresh_off_by_xpath : ", ex)

    def get_image_match_list_by_xpath(self):
        try:
            image_match_list_by_xpath = self.config.get("Integration", "image_match_list_by_xpath")
            return image_match_list_by_xpath
        except Exception as ex:
            print("image_match_list_by_xpath : ", ex)

    def get_identify_within_enrollments_btn_by_xpath(self):
        try:
            identify_within_enrollments_btn_by_xpath = self.config.get("Integration", "identify_within_enrollments_btn_by_xpath")
            print(f"identify_within_enrollments_btn_by_xpath: {identify_within_enrollments_btn_by_xpath}")
            return identify_within_enrollments_btn_by_xpath
        except Exception as ex:
            print("image_match_list_by_xpath : ", ex)

    def vs_completed_banner_by_xpath(self):
        try:
            vs_completed_banner_by_xpath = self.config.get("Integration", "vs_completed_banner_by_xpath")
            print(f"identify_within_enrollments_btn_by_xpath: {vs_completed_banner_by_xpath}")
            return vs_completed_banner_by_xpath
        except Exception as ex:
            print("image_match_list_by_xpath : ", ex)

    def identifying_photo_wait_by_xpath(self):
        try:
            identifying_photo_wait_by_xpath = self.config.get("Integration", "identifying_photo_wait_by_xpath")
            print(f"identifying_photo_wait_by_xpath: {identifying_photo_wait_by_xpath}")
            return identifying_photo_wait_by_xpath
        except Exception as ex:
            print("identifying_photo_wait_by_xpath : ", ex)

    def enrollment_basis_by_xpath(self):
        try:
            enrollment_basis_by_xpath = self.config.get("Integration", "enrollment_basis_by_xpath")
            print(f"enrollment_basis_by_xpath: {enrollment_basis_by_xpath}")
            return enrollment_basis_by_xpath
        except Exception as ex:
            print("enrollment_basis_by_xpath : ", ex)

    def enrollment_group_by_xpath(self):
        try:
            enrollment_group_by_xpath = self.config.get("Integration", "enrollment_group_by_xpath")
            print(f"enrollment_group_by_xpath: {enrollment_group_by_xpath}")
            return enrollment_group_by_xpath
        except Exception as ex:
            print("enrollment_group_by_xpath : ", ex)

    def region_btn_by_xpath(self):
        try:
            region_btn_by_xpath = self.config.get("Integration", "region_btn_by_xpath")
            return region_btn_by_xpath
        except Exception as ex:
            print(ex.args)

    def edge_name_list(self):
        try:
            edge_name_list = self.config.get("Integration", "edge_name_list")
            return edge_name_list
        except Exception as ex:
            print(ex.args)

    def edge_name_input_data(self):
        try:
            edge_name_input_data = self.common_test_data_config.get("system_level_test_Data", "edge_name_input_data")
            print(f"edge name: {edge_name_input_data}")
            return edge_name_input_data
        except Exception as ex:
            print(ex.args)

    def save_btn_by_xpath(self):
        try:
            save_btn_by_xpath = self.config.get("Integration", "save_btn_by_xpath")
            print(f"save btn: {save_btn_by_xpath}")
            return save_btn_by_xpath
        except Exception as ex:
            print(ex.args)

    def location_store_inpt_bx_by_xpath(self):
        try:
            location_store_inpt_bx_by_xpath = self.config.get("Integration", "location_store_inpt_bx_by_xpath")
            return location_store_inpt_bx_by_xpath
        except Exception as ex:
            print("location_store_inpt_bx_by_xpath : ", ex)

    def case_subject_inpt_bx_by_xpath(self):
        try:
            case_subject_inpt_bx_by_xpath = self.config.get("Integration", "case_subject_inpt_bx_by_xpath")
            return case_subject_inpt_bx_by_xpath
        except Exception as ex:
            print("case_subject_inpt_bx_by_xpath : ", ex)

    def location_store_data(self):
        try:
            location_store_data = self.common_test_data_config \
                .get("system_level_test_Data", "location_store_data")
            return location_store_data
        except Exception as ex:
            print("location_store_data : ", ex)

    def case_subject_data(self):
        try:
            case_subject_data = self.common_test_data_config \
                .get("system_level_test_Data", "case_subject_data")
            return case_subject_data
        except Exception as ex:
            print("case_subject_data : ", ex)

    def date_incident_inpt_bx_by_xpath(self):
        try:
            date_incident_inpt_bx_by_xpath = self.config.get("Integration", "date_incident_inpt_bx_by_xpath")
            return date_incident_inpt_bx_by_xpath
        except Exception as ex:
            print("date_incident_inpt_bx_by_xpath : ", ex)

    def action_inpt_bx_by_xpath(self):
        try:
            action_inpt_bx_by_xpath = self.config.get("Integration", "action_inpt_bx_by_xpath")
            return action_inpt_bx_by_xpath
        except Exception as ex:
            print("action_inpt_bx_by_xpath : ", ex)

    def date_incident_data(self):
        try:
            date_incident_data = self.common_test_data_config.get("system_level_test_Data", "date_incident_data")
            day = date_incident_data[0:2]
            month = date_incident_data[3:5]
            year = date_incident_data[6:]
            print(
                f"day: {day}, month: {month}, year: {year}, type day: {type(day)}, month: {type(month)}, year: {type(year)}")
            day = int(day)
            month = int(month)
            year = int(year)
            datetime = dt.datetime.now()
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

    def date_incident_time(self):
        try:
            datetime = dt.datetime.now()
            date_incident_time_am_pm = self.common_test_data_config.get("system_level_test_Data", "date_incident_time")
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
            date_incident_am_pm = self.common_test_data_config.get("system_level_test_Data", "date_incident_am_pm")
            return date_incident_am_pm
        except Exception as ex:
            print(ex.args)

    def action_input_data(self):
        try:
            action_input_data = self.common_test_data_config \
                .get("system_level_test_Data", "action_input_data")
            return action_input_data
        except Exception as ex:
            print("action_input_data : ", ex)

    def reported_loss_inpt_bx_by_xpath(self):
        try:
            reported_loss_inpt_bx_by_xpath = self.config.get("Integration", "reported_loss_inpt_bx_by_xpath")
            return reported_loss_inpt_bx_by_xpath
        except Exception as ex:
            print("reported_loss_inpt_bx_by_xpath : ", ex)

    def reported_loss_data(self):
        try:
            reported_loss_data = self.common_test_data_config \
                .get("system_level_test_Data", "reported_loss_data")
            return reported_loss_data
        except Exception as ex:
            print("reported_loss_data : ", ex)

    def add_details_save_btn_by_xpath(self):
        try:
            add_details_save_btn_by_xpath = self.config.get("Integration", "add_details_save_btn_by_xpath")
            return add_details_save_btn_by_xpath
        except Exception as ex:
            print("add_details_save_btn_by_xpath : ", ex)

    def enrollment_success_loader(self):
        try:
            enrollment_success_loader = self.config.get("Integration", "enrollment_success_loader")
            return enrollment_success_loader
        except Exception as ex:
            print("enrollment_success_loader : ", ex)

    def enrollment_success_msg_xpath(self):
        try:
            enrollment_success_msg_xpath = self.config.get("Integration", "enrollment_success_msg_xpath")
            return enrollment_success_msg_xpath
        except Exception as ex:
            print("enrollment_success_msg_xpath : ", ex)

    def enrollment_success_msg_validation(self):
        try:
            enrollment_success_msg_validation = self.common_test_data_config \
                .get("system_level_test_Data", "enrollment_success_msg_validation")
            return enrollment_success_msg_validation
        except Exception as ex:
            print("enrollment_success_msg_validation : ", ex)

    def review_enrollment_details_btn_by_xpath(self):
        try:
            review_enrollment_details_btn_by_xpath = self.config \
                .get("Integration", "review_enrollment_details_btn_by_xpath")
            print(f"review_enrollment_details_btn_by_xpath: {review_enrollment_details_btn_by_xpath}")
            return review_enrollment_details_btn_by_xpath
        except Exception as ex:
            print("enrollment_success_msg_validation : ", ex)

    def enrolled_on_date_on_enrollment_details_panel_by_xpath(self):
        try:
            enrolled_on_date_on_enrollment_details_panel_by_xpath = self.config \
                .get("Integration", "enrolled_on_date_on_enrollment_details_panel_by_xpath")
            print(f"enrolled_on_date_on_enrollment_details_panel_by_xpath: {enrolled_on_date_on_enrollment_details_panel_by_xpath}")
            return enrolled_on_date_on_enrollment_details_panel_by_xpath
        except Exception as ex:
            print("enrollment_success_msg_validation : ", ex)

    def enrolled_on_date_on_enrollments_panel_by_xpath(self):
        try:
            enrolled_on_date_on_enrollments_panel_by_xpath = self.config \
                .get("Integration", "enrolled_on_date_on_enrollments_panel_by_xpath")
            print(f"enrolled_on_date_on_enrollments_panel_by_xpath: {enrolled_on_date_on_enrollments_panel_by_xpath}")
            return enrolled_on_date_on_enrollments_panel_by_xpath
        except Exception as ex:
            print("enrollment_success_msg_validation : ", ex)

    def location_store_and_case_subject_on_enrollments_panel_by_xpath(self):
        try:
            location_store_and_case_subject_on_enrollments_panel_by_xpath = self.config \
                .get("Integration", "location_store_and_case_subject_on_enrollments_panel_by_xpath")
            print(f"location_store_and_case_subject_on_enrollments_panel_by_xpath: {location_store_and_case_subject_on_enrollments_panel_by_xpath}")
            return location_store_and_case_subject_on_enrollments_panel_by_xpath
        except Exception as ex:
            print("enrollment_success_msg_validation : ", ex)

    def action_value_on_enrollments_panel_by_xpath(self):
        try:
            action_value_on_enrollments_panel_by_xpath = self.config \
                .get("Integration", "action_value_on_enrollments_panel_by_xpath")
            print(f"action_value_on_enrollments_panel_by_xpath: {action_value_on_enrollments_panel_by_xpath}")
            return action_value_on_enrollments_panel_by_xpath
        except Exception as ex:
            print("enrollment_success_msg_validation : ", ex)

    def meta_data_start_date(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_start_date")
            return ele
        except Exception as ex:
            print("meta_data_start_date : ", ex)

    def meta_data_start_month(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_start_month")
            return ele
        except Exception as ex:
            print("meta_data_start_month : ", ex)

    def meta_data_start_year(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_start_year")
            return ele
        except Exception as ex:
            print("meta_data_start_year : ", ex)

    def meta_data_start_hour(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_start_hour")
            return ele
        except Exception as ex:
            print("meta_data_start_hour : ", ex)

    def meta_data_start_minuet(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_start_minuet")
            return ele
        except Exception as ex:
            print("meta_data_start_minuet : ", ex)

    def meta_data_start_am_pm_period(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_start_am_pm_period")
            return ele
        except Exception as ex:
            print("meta_data_start_am_pm_period : ", ex)

    def meta_data_end_date(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_end_date")
            return ele
        except Exception as ex:
            print("meta_data_end_date : ", ex)

    def meta_data_end_month(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_end_month")
            return ele
        except Exception as ex:
            print("meta_data_end_month : ", ex)

    def meta_data_end_year(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_end_year")
            return ele
        except Exception as ex:
            print("meta_data_end_year : ", ex)

    def meta_data_end_hour(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_end_hour")
            return ele
        except Exception as ex:
            print("meta_data_end_hour : ", ex)

    def meta_data_end_minuet(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_end_minuet")
            return ele
        except Exception as ex:
            print("meta_data_end_minuet : ", ex)

    def meta_data_end_am_pm_period(self):
        try:
            ele = self.common_test_data_config.get("common_data", "meta_data_end_am_pm_period")
            return ele
        except Exception as ex:
            print("meta_data_end_am_pm_period : ", ex)

    def identify_enroll_panel_by_xpath(self):
        try:
            ele = self.config.get("Integration", "identify_enroll_panel_by_xpath")
            return ele
        except Exception as ex:
            print("identify_enroll_panel_by_xpath : ", ex)

    def enroll_pencil_button_by_xpath(self):
        try:
            ele = self.config.get("Integration", "enroll_pencil_button_by_xpath")
            return ele
        except Exception as ex:
            print("enroll_pencil_button_by_xpath : ", ex)

    def identify_results_panel_by_xpath(self):
        try:
            ele = self.config.get("Integration", "identify_results_panel_by_xpath")
            return ele
        except Exception as ex:
            print("identify_results_panel_by_xpath : ", ex)

    def add_details_panel_by_xpath(self):
        try:
            ele = self.config.get("Integration", "add_details_panel_by_xpath")
            return ele
        except Exception as ex:
            print("add_details_panel_by_xpath : ", ex)

    def warning_pop_up_close_and_discard_changes_btn_by_xpath(self):
        try:
            warning_pop_up_close_and_discard_changes_btn_by_xpath = self.config.get("Integration", "warning_pop_up_close_and_discard_changes_btn_by_xpath")
            return warning_pop_up_close_and_discard_changes_btn_by_xpath
        except Exception as ex:
            print("warning_pop_up_close_and_discard_changes_btn_by_xpath: ", ex)


