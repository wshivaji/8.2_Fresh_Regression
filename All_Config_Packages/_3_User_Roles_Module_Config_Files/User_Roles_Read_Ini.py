from pathlib import Path
import configparser

file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\3_User_Roles_Module\\Data_From_INI\\User_Roles.ini"
print(file_path)
common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"


class user_roles_read_ini:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        try:
            self.config.read(file_path)
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print(ex.args)

    def get_core_url(self):
        try:
            core_url = self.common_test_data_config.get("Login_Logout_Data", "cloud_login_url")
            print(f"core_url: {core_url}")
            return core_url
        except Exception as ex:
            print(ex.args)

    def get_local_login_url(self):
        try:
            local_login_url = self.config.get("user_roles", "local_login_url")
            print(f"core_url: {local_login_url}")
            return local_login_url
        except Exception as ex:
            print(ex.args)

    def get_username_by_id(self):
        try:
            username_by_id = self.config.get("user_roles", "username_by_id")
            print(f"username_by_id: {username_by_id}")
            return username_by_id
        except Exception as ex:
            print(ex.args)

    def get_password_by_id(self):
        try:
            password_by_id = self.config.get("user_roles", "password_by_id")
            print(f"password_by_id: {password_by_id}")
            return password_by_id
        except Exception as ex:
            print(ex.args)

    def get_login_btn_link_by_xpath(self):
        try:
            login_btn_link_by_xpath = self.config.get("user_roles", "login_btn_link_by_xpath")
            print(f"login_btn_link_by_xpath: {login_btn_link_by_xpath}")
            return login_btn_link_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_logout_btn_link_by_xpath(self):
        try:
            logout_btn_link_by_xpath = self.config.get("user_roles", "logout_btn_link_by_xpath")
            print(f"login_btn_link_by_xpath: {logout_btn_link_by_xpath}")
            return logout_btn_link_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_admin_username(self):
        try:
            admin_username = self.common_test_data_config.get("Login_Logout_Data", "username")
            print(f"admin_username: {admin_username}")
            return admin_username
        except Exception as ex:
            print(ex.args)

    def get_admin_password(self):
        try:
            admin_password = self.common_test_data_config.get("Login_Logout_Data", "password")
            print(f"admin_password: {admin_password}")
            return admin_password
        except Exception as ex:
            print(ex.args)

    def get_cloud_menu_by_xpath(self):
        try:
            cloud_menu_by_id = self.config.get("user_roles", "cloud_menu_by_xpath")
            print(f"cloud_menu_by_id: {cloud_menu_by_id}")
            return cloud_menu_by_id
        except Exception as ex:
            print(ex.args)

    def get_cloud_menu_text(self):
        try:
            cloud_menu_text = self.common_test_data_config.get("User_Roles_Data", "cloud_menu_text")
            print(f"cloud_menu_text: {cloud_menu_text}")
            return cloud_menu_text
        except Exception as ex:
            print(ex.args)

    def get_menu_items_inside_cloud_menu_by_xpath(self):
        try:
            menu_items_inside_cloud_menu_by_xpath = self.config.get("user_roles",
                                                                    "menu_items_inside_cloud_menu_by_xpath")
            print(f"menu_items_inside_cloud_menu_by_xpath: {menu_items_inside_cloud_menu_by_xpath}")
            return menu_items_inside_cloud_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_role_menu_item_text(self):
        try:
            user_role_menu_item_text = self.common_test_data_config.get("User_Roles_Data", "user_role_menu_item_text")
            print(f"user_role_menu_item_text: {user_role_menu_item_text}")
            return user_role_menu_item_text
        except Exception as ex:
            print(ex.args)

    def get_user_role_menu_item_by_xpath(self):
        try:
            user_role_menu_item_by_xpath = self.config.get("user_roles", "user_role_menu_item_by_xpath")
            print(f"user_role_menu_item_by_xpath: {user_role_menu_item_by_xpath}")
            return user_role_menu_item_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_role_menu_item_symbol_by_xpath(self):
        try:
            user_role_menu_item_symbol_by_xpath = self.config.get("user_roles", "user_role_menu_item_symbol_by_xpath")
            print(f"user_role_menu_item_symbol_by_xpath: {user_role_menu_item_symbol_by_xpath}")
            return user_role_menu_item_symbol_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_roles_panel_title_by_xpath(self):
        try:
            user_roles_panel_title_by_xpath = self.config.get("user_roles", "user_roles_panel_title_by_xpath")
            print(f"user_roles_panel_title_by_xpath: {user_roles_panel_title_by_xpath}")
            return user_roles_panel_title_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_action_dropdown_by_xpath(self):
        try:
            action_dropdown_by_xpath = self.config.get("user_roles", "action_dropdown_by_xpath")
            print(f"action_dropdown_by_xpath: {action_dropdown_by_xpath}")
            return action_dropdown_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_action_dropdown_text(self):
        try:
            action_dropdown_text = self.common_test_data_config.get("User_Roles_Data", "action_dropdown_text")
            print(f"action_dropdown_text: {action_dropdown_text}")
            return action_dropdown_text
        except Exception as ex:
            print(ex.args)

    def get_options_inside_action_dropdown_by_xpath(self):
        try:
            options_inside_action_dropdown_by_xpath = self.config.get("user_roles",
                                                                      "options_inside_action_dropdown_by_xpath")
            print(f"options_inside_action_dropdown_by_xpath: {options_inside_action_dropdown_by_xpath}")
            return options_inside_action_dropdown_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_panel_container_outside_click_by_xpath(self):
        try:
            panel_container_outside_click_by_xpath = self.config.get("user_roles", "panel_container_outside_click_by_xpath")
            print(f"panel_container_outside_click_by_xpath: {panel_container_outside_click_by_xpath}")
            return panel_container_outside_click_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_select_all_label_by_xpath(self):
        try:
            select_all_label_by_xpath = self.config.get("user_roles", "select_all_label_by_xpath")
            print(f"select_all_label_by_xpath: {select_all_label_by_xpath}")
            return select_all_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_select_all_label(self):
        try:
            select_all_label = self.common_test_data_config.get("User_Roles_Data", "select_all_label")
            print(f"select_all_label: {select_all_label}")
            return select_all_label
        except Exception as ex:
            print(ex.args)

    def get_select_all_check_box_by_xpath(self):
        try:
            select_all_check_box_by_xpath = self.config.get("user_roles", "select_all_check_box_by_xpath")
            print(f"select_all_check_box_by_xpath: {select_all_check_box_by_xpath}")
            return select_all_check_box_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_roles_profiles_list_by_xpath(self):
        try:
            user_roles_profiles_list_by_xpath = self.config.get("user_roles", "user_roles_profiles_list_by_xpath")
            print(f"user_roles_profiles_list_by_xpath: {user_roles_profiles_list_by_xpath}")
            return user_roles_profiles_list_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_roles_profiles_name_list_by_xpath(self):
        try:
            user_roles_profiles_name_list_by_xpath = self.config.get("user_roles", "user_roles_profiles_name_list_by_xpath")
            print(f"user_roles_profiles_name_list_by_xpath: {user_roles_profiles_name_list_by_xpath}")
            return user_roles_profiles_name_list_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_roles_profiles_description_list_by_xpath(self):
        try:
            user_roles_profiles_description_list_by_xpath = \
                self.config.get("user_roles", "user_roles_profiles_description_list_by_xpath")
            print(f"user_roles_profiles_description_list_by_xpath: {user_roles_profiles_description_list_by_xpath}")
            return user_roles_profiles_description_list_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_roles_profiles_enable_disable_list_by_xpath(self):
        try:
            user_roles_profiles_enable_disable_list_by_xpath = \
                self.config.get("user_roles", "user_roles_profiles_enable_disable_list_by_xpath")
            print(f"user_roles_profiles_enable_disable_list_by_xpath: "
                  f"{user_roles_profiles_enable_disable_list_by_xpath}")
            return user_roles_profiles_enable_disable_list_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_roles_profiles_checkbox_list_by_xpath(self):
        try:
            user_roles_profiles_checkbox_list_by_xpath = self.config.get("user_roles", "user_roles_profiles_checkbox_list_by_xpath")
            print(f"user_roles_profiles_checkbox_list_by_xpath: {user_roles_profiles_checkbox_list_by_xpath}")
            return user_roles_profiles_checkbox_list_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_roles_profiles_menu_btn_list_by_xpath(self):
        try:
            user_roles_profiles_menu_btn_list_by_xpath = self.config.get("user_roles",
                                                                         "user_roles_profiles_menu_btn_list_by_xpath")
            print(f"user_roles_profiles_menu_btn_list_by_xpath: {user_roles_profiles_menu_btn_list_by_xpath}")
            return user_roles_profiles_menu_btn_list_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_refresh_option_text_inside_action_dropdown(self):
        try:
            refresh_option_text_inside_action_dropdown = self.common_test_data_config.get("User_Roles_Data",
                                                                         "refresh_option_text_inside_action_dropdown")
            print(f"refresh_option_text_inside_action_dropdown: {refresh_option_text_inside_action_dropdown}")
            return refresh_option_text_inside_action_dropdown
        except Exception as ex:
            print(ex.args)

    def get_create_user_role_option_text_inside_action_dropdown(self):
        try:
            create_user_role_option_text_inside_action_dropdown = self.common_test_data_config.get("User_Roles_Data", "create_user_role_option_text_inside_action_dropdown")
            print(f"create_user_role_option_text_inside_action_dropdown: {create_user_role_option_text_inside_action_dropdown}")
            return create_user_role_option_text_inside_action_dropdown
        except Exception as ex:
            print(ex.args)

    def get_delete_user_role_option_text_inside_action_dropdown(self):
        try:
            delete_user_role_option_text_inside_action_dropdown = \
                self.common_test_data_config.get("User_Roles_Data", "delete_user_role_option_text_inside_action_dropdown")
            print(f"delete_user_role_option_text_inside_action_dropdown: "
                  f"{delete_user_role_option_text_inside_action_dropdown}")
            return delete_user_role_option_text_inside_action_dropdown
        except Exception as ex:
            print(ex.args)

    def get_number_of_panels_list_by_xpath(self):
        try:
            number_of_panels_list_by_xpath = self.config.get("user_roles", "number_of_panels_list_by_xpath")
            print(f"number_of_panels_list_by_xpath: {number_of_panels_list_by_xpath}")
            return number_of_panels_list_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_role_panel_title_by_xpath(self):
        try:
            user_role_panel_title_by_xpath = self.config.get("user_roles", "user_role_panel_title_by_xpath")
            print(f"user_role_panel_title_by_xpath: {user_role_panel_title_by_xpath}")
            return user_role_panel_title_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_role_panel_title_text(self):
        try:
            user_role_panel_title_text = self.common_test_data_config.get("User_Roles_Data", "user_role_panel_title_text")
            print(f"user_role_panel_title_text: {user_role_panel_title_text}")
            return user_role_panel_title_text
        except Exception as ex:
            print(ex.args)

    def get_cancel_btn_by_xpath(self):
        try:
            cancel_btn_by_xpath = self.config.get("user_roles", "cancel_btn_by_xpath")
            print(f"cancel_btn_by_xpath: {cancel_btn_by_xpath}")
            return cancel_btn_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_save_btn_by_xpath(self):
        try:
            save_btn_by_xpath = self.config.get("user_roles", "save_btn_by_xpath")
            print(f"save_btn_by_xpath: {save_btn_by_xpath}")
            return save_btn_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_new_in_heading_by_xpath(self):
        try:
            new_in_heading_by_xpath = self.config.get("user_roles", "new_in_heading_by_xpath")
            print(f"new_in_heading_by_xpath: {new_in_heading_by_xpath}")
            return new_in_heading_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_new_in_heading_text(self):
        try:
            new_in_heading_text = self.common_test_data_config.get("User_Roles_Data", "new_in_heading_text")
            print(f"new_in_heading_text: {new_in_heading_text}")
            return new_in_heading_text
        except Exception as ex:
            print(ex.args)

    def get_user_role_details_in_heading_by_xpath(self):
        try:
            user_role_details_in_heading_by_xpath = self.config.get("user_roles",
                                                                    "user_role_details_in_heading_by_xpath")
            print(f"user_role_details_in_heading_by_xpath: {user_role_details_in_heading_by_xpath}")
            return user_role_details_in_heading_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_role_details_in_heading(self):
        try:
            user_role_details_in_heading = self.common_test_data_config.get("User_Roles_Data", "user_role_details_in_heading")
            print(f"user_role_details_in_heading: {user_role_details_in_heading}")
            return user_role_details_in_heading
        except Exception as ex:
            print(ex.args)

    def get_user_role_details_logo_symbol_by_xpath(self):
        try:
            user_role_details_logo_symbol_by_xpath = self.config.get("user_roles",
                                                                     "user_role_details_logo_symbol_by_xpath")
            print(f"user_role_details_logo_symbol_by_xpath: {user_role_details_logo_symbol_by_xpath}")
            return user_role_details_logo_symbol_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_rolename_label_by_xpath(self):
        try:
            rolename_label_by_xpath = self.config.get("user_roles", "rolename_label_by_xpath")
            print(f"rolename_label_by_xpath: {rolename_label_by_xpath}")
            return rolename_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_rolename_label(self):
        try:
            rolename_label = self.common_test_data_config.get("User_Roles_Data", "rolename_label")
            print(f"rolename_label: {rolename_label}")
            return rolename_label
        except Exception as ex:
            print(ex.args)

    def get_rolename_textbox_by_xpath(self):
        try:
            rolename_textbox_by_xpath = self.config.get("user_roles", "rolename_textbox_by_xpath")
            print(f"rolename_textbox_by_xpath: {rolename_textbox_by_xpath}")
            return rolename_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_description_label_by_xpath(self):
        try:
            description_label_by_xpath = self.config.get("user_roles", "description_label_by_xpath")
            print(f"description_label_by_xpath: {description_label_by_xpath}")
            return description_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_description_label(self):
        try:
            description_label = self.common_test_data_config.get("User_Roles_Data", "description_label")
            print(f"description_label: {description_label}")
            return description_label
        except Exception as ex:
            print(ex.args)

    def get_description_textbox_by_xpath(self):
        try:
            description_textbox_by_xpath = self.config.get("user_roles", "description_textbox_by_xpath")
            print(f"description_textbox_by_xpath: {description_textbox_by_xpath}")
            return description_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_disabled_label_by_xpath(self):
        try:
            disabled_label_by_xpath = self.config.get("user_roles", "disabled_label_by_xpath")
            print(f"disabled_label_by_xpath: {disabled_label_by_xpath}")
            return disabled_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_disabled_label(self):
        try:
            disabled_label = self.common_test_data_config.get("User_Roles_Data", "disabled_label")
            print(f"disabled_label: {disabled_label}")
            return disabled_label
        except Exception as ex:
            print(ex.args)

    def get_disabled_option_btn_by_xpath(self):
        try:
            disabled_option_btn_by_xpath = self.config.get("user_roles", "disabled_option_btn_by_xpath")
            print(f"disabled_option_btn_by_xpath: {disabled_option_btn_by_xpath}")
            return disabled_option_btn_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_disabled_status_input_by_xpath(self):
        try:
            disabled_status_input_by_xpath = self.config.get("user_roles", "disabled_status_input_by_xpath")
            print(f"disabled_status_input_by_xpath: {disabled_status_input_by_xpath}")
            return disabled_status_input_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_enabled_label_by_xpath(self):
        try:
            enabled_label_by_xpath = self.config.get("user_roles", "enabled_label_by_xpath")
            print(f"enabled_label_by_xpath: {enabled_label_by_xpath}")
            return enabled_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_enabled_label(self):
        try:
            enabled_label = self.common_test_data_config.get("User_Roles_Data", "enabled_label")
            print(f"enabled_label: {enabled_label}")
            return enabled_label
        except Exception as ex:
            print(ex.args)

    def get_enabled_option_btn_by_xpath(self):
        try:
            enabled_option_btn_by_xpath = self.config.get("user_roles", "enabled_option_btn_by_xpath")
            print(f"enabled_option_btn_by_xpath: {enabled_option_btn_by_xpath}")
            return enabled_option_btn_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_enabled_disabled_class_text(self):
        try:
            enabled_disabled_class_text = self.common_test_data_config.get("User_Roles_Data", "enabled_disabled_class_text")
            print(f"enabled_disabled_class_text: {enabled_disabled_class_text}")
            return enabled_disabled_class_text
        except Exception as ex:
            print(ex.args)

    def get_permissions_label_by_xpath(self):
        try:
            permissions_label_by_xpath = self.config.get("user_roles", "permissions_label_by_xpath")
            print(f"permissions_label_by_xpath: {permissions_label_by_xpath}")
            return permissions_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_permissions_label(self):
        try:
            permissions_label = self.common_test_data_config.get("User_Roles_Data", "permissions_label")
            print(f"permissions_label: {permissions_label}")
            return permissions_label
        except Exception as ex:
            print(ex.args)

    def get_table_headings_by_xpath(self):
        try:
            table_headings_by_xpath = self.config.get("user_roles", "table_headings_by_xpath")
            print(f"table_headings_by_xpath: {table_headings_by_xpath}")
            return table_headings_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_table_row_heading_by_xpath(self):
        try:
            table_row_heading_by_xpath = self.config.get("user_roles", "table_row_heading_by_xpath")
            print(f"table_row_heading_by_xpath: {table_row_heading_by_xpath}")
            return table_row_heading_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_info_symbol_besides_table_row_heading_by_xpath(self):
        try:
            info_symbol_besides_table_row_heading_by_xpath = \
                self.config.get("user_roles", "info_symbol_besides_table_row_heading_by_xpath")
            print(f"info_symbol_besides_table_row_heading_by_xpath: {info_symbol_besides_table_row_heading_by_xpath}")
            return info_symbol_besides_table_row_heading_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_checkbox_after_table_row_heading_by_xpath(self):
        try:
            checkbox_after_table_row_heading_by_xpath = self.config.get("user_roles",
                                                                        "checkbox_after_table_row_heading_by_xpath")
            print(f"checkbox_after_table_row_heading_by_xpath: {checkbox_after_table_row_heading_by_xpath}")
            return checkbox_after_table_row_heading_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_create_column_checkbox_by_xpath(self):
        try:
            create_column_checkbox_by_xpath = self.config.get("user_roles", "create_column_checkbox_by_xpath")
            print(f"create_column_checkbox_by_xpath: {create_column_checkbox_by_xpath}")
            return create_column_checkbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_read_column_checkbox_by_xpath(self):
        try:
            read_column_checkbox_by_xpath = self.config.get("user_roles", "read_column_checkbox_by_xpath")
            print(f"read_column_checkbox_by_xpath: {read_column_checkbox_by_xpath}")
            return read_column_checkbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_edit_column_checkbox_by_xpath(self):
        try:
            edit_column_checkbox_by_xpath = self.config.get("user_roles", "edit_column_checkbox_by_xpath")
            print(f"edit_column_checkbox_by_xpath: {edit_column_checkbox_by_xpath}")
            return edit_column_checkbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_delete_column_checkbox_by_xpath(self):
        try:
            delete_column_checkbox_by_xpath = self.config.get("user_roles", "delete_column_checkbox_by_xpath")
            print(f"delete_column_checkbox_by_xpath: {delete_column_checkbox_by_xpath}")
            return delete_column_checkbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_ng_not_empty_in_checkbox_class(self):
        try:
            ng_not_empty_in_checkbox_class = self.common_test_data_config.get("User_Roles_Data", "ng_not_empty_in_checkbox_class")
            print(f"ng_not_empty_in_checkbox_class: {ng_not_empty_in_checkbox_class}")
            return ng_not_empty_in_checkbox_class
        except Exception as ex:
            print(ex.args)

    def get_rolename_text_box_to_enter_data_by_xpath(self):
        try:
            rolename_text_box_to_enter_data_by_xpath = self.config.get("user_roles",
                                                                       "rolename_text_box_to_enter_data_by_xpath")
            print(f"rolename_text_box_to_enter_data_by_xpath: {rolename_text_box_to_enter_data_by_xpath}")
            return rolename_text_box_to_enter_data_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_description_text_box_to_enter_data_by_xpath(self):
        try:
            description_text_box_to_enter_data_by_xpath = self.config.get("user_roles",
                                                                          "description_text_box_to_enter_data_by_xpath")
            print(f"description_text_box_to_enter_data_by_xpath: {description_text_box_to_enter_data_by_xpath}")
            return description_text_box_to_enter_data_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_so_user_role(self):
        try:
            so_user = self.common_test_data_config.get("Users_Data", "so_user_role")
            print(f"so_user_role: {so_user}")
            return so_user
        except Exception as ex:
            print(ex.args)

    def get_so_user_role_so(self):
        try:
            so_user = self.common_test_data_config.get("User_Roles_Data", "so_user_role")
            print(f"so_user_role: {so_user}")
            return so_user
        except Exception as ex:
            print(ex.args)


    def get_test_user_role(self):
        try:
            test_user = self.common_test_data_config.get("User_Roles_Data", "test_user_role")
            print(f"test_user_role: {test_user}")
            return test_user
        except Exception as ex:
            print(ex.args)

    def get_user_role_for_deletion(self):
        try:
            delete_user = self.common_test_data_config.get("User_Roles_Data", "user_role_for_deletion")
            print(f"user_role_for_deletion: {delete_user}")
            return delete_user
        except Exception as ex:
            print(ex.args)

    def get_so_user_role_description(self):
        try:
            so_user_description = self.common_test_data_config.get("User_Roles_Data", "so_user_role_description")
            print(f"so_user_role_description: {so_user_description}")
            return so_user_description
        except Exception as ex:
            print(ex.args)
    def get_test_user_role_description(self):
        try:
            test_user_description = self.common_test_data_config.get("User_Roles_Data", "test_user_role_description")
            print(f"so_user_role_description: {test_user_description}")
            return test_user_description
        except Exception as ex:
            print(ex.args)

    def get_rights_checkbox_by_xpath(self):
        try:
            rights_checkbox_by_xpath = self.config.get("user_roles", "rights_checkbox_by_xpath")
            print(f"rights_checkbox_by_xpath: {rights_checkbox_by_xpath}")
            return rights_checkbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_click_to_save_msg_by_xpath(self):
        try:
            click_to_save_msg_by_xpath = self.config.get("user_roles", "click_to_save_msg_by_xpath")
            print(f"click_to_save_msg_by_xpath: {click_to_save_msg_by_xpath}")
            return click_to_save_msg_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_click_to_save_msg(self):
        try:
            click_to_save_msg = self.common_test_data_config.get("User_Roles_Data", "click_to_save_msg")
            print(f"click_to_save_msg: {click_to_save_msg}")
            return click_to_save_msg
        except Exception as ex:
            print(ex.args)

    def get_message_after_user_created_by_xpath(self):
        try:
            message_after_user_created_by_xpath = self.config.get("user_roles", "message_after_user_created_by_xpath")
            print(f"message_after_user_created_by_xpath: {message_after_user_created_by_xpath}")
            return message_after_user_created_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_close_all_panels_menu_item_text(self):
        try:
            close_all_panels_menu_item_text = self.common_test_data_config.get("User_Roles_Data", "close_all_panels_menu_item_text")
            print(f"close_all_panels_menu_item_text: {close_all_panels_menu_item_text}")
            return close_all_panels_menu_item_text
        except Exception as ex:
            print(ex.args)

    def get_users_sub_menu_item_by_xpath(self):
        try:
            users_sub_menu_item_by_xpath = self.config.get("user_roles", "users_sub_menu_item_by_xpath")
            print(f"users_sub_menu_item_by_xpath: {users_sub_menu_item_by_xpath}")
            return users_sub_menu_item_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_users_sub_menu_item_text(self):
        try:
            users_sub_menu_item_text = self.common_test_data_config.get("User_Roles_Data", "users_sub_menu_item_text")
            print(f"users_sub_menu_item_text: {users_sub_menu_item_text}")
            return users_sub_menu_item_text
        except Exception as ex:
            print(ex.args)

    def get_users_sub_menu_symbol_by_xpath(self):
        try:
            users_sub_menu_symbol_by_xpath = self.config.get("user_roles", "users_sub_menu_symbol_by_xpath")
            print(f"users_sub_menu_symbol_by_xpath: {users_sub_menu_symbol_by_xpath}")
            return users_sub_menu_symbol_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_first_name_textbox_by_xpath(self):
        try:
            first_name_textbox_by_xpath = self.config.get("user_roles", "first_name_textbox_by_xpath")
            print(f"first_name_textbox_by_xpath: {first_name_textbox_by_xpath}")
            return first_name_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_panel_title_by_xpath(self):
        try:
            user_panel_title_by_xpath = self.config.get("user_roles", "user_panel_title_by_xpath")
            print(f"user_panel_title_by_xpath: {user_panel_title_by_xpath}")
            return user_panel_title_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_panel_title(self):
        try:
            user_panel_title = self.common_test_data_config.get("User_Roles_Data", "user_panel_title")
            print(f"user_panel_title: {user_panel_title}")
            return user_panel_title
        except Exception as ex:
            print(ex.args)

    def get_action_dropdown_user_panel_by_xpath(self):
        try:
            action_dropdown_user_panel_by_xpath = self.config.get("user_roles", "action_dropdown_user_panel_by_xpath")
            print(f"action_dropdown_user_panel_by_xpath: {action_dropdown_user_panel_by_xpath}")
            return action_dropdown_user_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_filter_text_box_by_xpath(self):
        try:
            filter_text_box_by_xpath = self.config.get("user_roles", "filter_text_box_by_xpath")
            print(f"filter_text_box_by_xpath: {filter_text_box_by_xpath}")
            return filter_text_box_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_new_in_user_panel_heading_by_xpath(self):
        try:
            new_in_user_panel_heading_by_xpath = self.config.get("user_roles", "new_in_user_panel_heading_by_xpath")
            print(f"new_in_user_panel_heading_by_xpath: {new_in_user_panel_heading_by_xpath}")
            return new_in_user_panel_heading_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_new_in_user_panel_heading(self):
        try:
            new_in_user_panel_heading = self.common_test_data_config.get("User_Roles_Data", "new_in_user_panel_heading")
            print(f"new_in_user_panel_heading: {new_in_user_panel_heading}")
            return new_in_user_panel_heading
        except Exception as ex:
            print(ex.args)

    def get_user_details_in_user_panel_hading_by_xpath(self):
        try:
            user_role_details_in_user_panel_hading_by_xpath = \
                self.config.get("user_roles", "user_details_in_user_panel_hading_by_xpath")
            print(f"user_details_in_user_panel_hading_by_xpath: {user_role_details_in_user_panel_hading_by_xpath}")
            return user_role_details_in_user_panel_hading_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_details_in_user_panel_heading(self):
        try:
            user_role_details_in_user_panel_heading = self.common_test_data_config.get("User_Roles_Data", "user_details_in_user_panel_heading")
            print(f"user_details_in_user_panel_heading: {user_role_details_in_user_panel_heading}")
            return user_role_details_in_user_panel_heading
        except Exception as ex:
            print(ex.args)

    def get_user_details_in_user_panel_heading_symbol_by_xpath(self):
        try:
            user_role_details_in_user_panel_heading_symbol_by_xpath = \
                self.config.get("user_roles", "user_details_in_user_panel_heading_symbol_by_xpath")
            print(f"user_details_in_user_panel_heading_symbol_by_xpath: "
                  f"{user_role_details_in_user_panel_heading_symbol_by_xpath}")
            return user_role_details_in_user_panel_heading_symbol_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_username_label_by_xpath(self):
        try:
            username_label_by_xpath = self.config.get("user_roles", "username_label_by_xpath")
            print(f"username_label_by_xpath: {username_label_by_xpath}")
            return username_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_username_label(self):
        try:
            username_label = self.common_test_data_config.get("User_Roles_Data", "username_label")
            print(f"username_label: {username_label}")
            return username_label
        except Exception as ex:
            print(ex.args)

    def get_username_textbox_by_xpath(self):
        try:
            username_textbox_by_xpath = self.config.get("user_roles", "username_textbox_by_xpath")
            print(f"username_textbox_by_xpath: {username_textbox_by_xpath}")
            return username_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_first_name_label_by_xpath(self):
        try:
            first_name_label_by_xpath = self.config.get("user_roles", "first_name_label_by_xpath")
            print(f"first_name_label_by_xpath: {first_name_label_by_xpath} ")
            return first_name_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_first_name_label(self):
        try:
            first_name_label = self.common_test_data_config.get("User_Roles_Data", "first_name_label")
            print(f"first_name_label: {first_name_label}")
            return first_name_label
        except Exception as ex:
            print(ex.args)

    def get_user_page_panel_title_by_xpath(self):
        try:
            user_page_panel_title_by_xpath = self.config.get("user_roles", "user_page_panel_title_by_xpath")
            print(f"user_page_panel_title_by_xpath: {user_page_panel_title_by_xpath}")
            return user_page_panel_title_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_page_panel_title(self):
        try:
            user_page_panel_title = self.common_test_data_config.get("User_Roles_Data", "user_page_panel_title")
            print(f"user_page_panel_title: {user_page_panel_title}")
            return user_page_panel_title
        except Exception as ex:
            print(ex.args)

    def get_lastname_label_by_xpath(self):
        try:
            lastname_label_by_xpath = self.config.get("user_roles", "lastname_label_by_xpath")
            print(f"lastname_label_by_xpath: {lastname_label_by_xpath}")
            return lastname_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_lastname_label(self):
        try:
            lastname_label = self.common_test_data_config.get("User_Roles_Data", "lastname_label")
            print(f"lastname_label: {lastname_label}")
            return lastname_label
        except Exception as ex:
            print(ex.args)

    def get_lastname_textbox_by_xpath(self):
        try:
            lastname_textbox_by_xpath = self.config.get("user_roles", "lastname_textbox_by_xpath")
            print(f"lastname_textbox_by_xpath: {lastname_textbox_by_xpath}")
            return lastname_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_enabled_option_btn_on_user_panel_by_xpath(self):
        try:
            enabled_option_btn_on_user_panel_by_xpath = self.config.get("user_roles",
                                                                        "enabled_option_btn_on_user_panel_by_xpath")
            print(f"enabled_option_btn_on_user_panel_by_xpath: {enabled_option_btn_on_user_panel_by_xpath}")
            return enabled_option_btn_on_user_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_disabled_option_btn_on_user_panel_by_xpath(self):
        try:
            disabled_option_btn_on_user_panel_by_xpath = self.config.get("user_roles",
                                                                         "disabled_option_btn_on_user_panel_by_xpath")
            print(f"disabled_option_btn_on_user_panel_by_xpath: {disabled_option_btn_on_user_panel_by_xpath}")
            return disabled_option_btn_on_user_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_role_dropdown_label_by_xpath(self):
        try:
            user_role_label_by_xpath = self.config.get("user_roles", "user_role_dropdown_label_by_xpath")
            print(f"user_role_label_by_xpath: {user_role_label_by_xpath}")
            return user_role_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_role_dropdown_label(self):
        try:
            user_role_dropdown_label = self.common_test_data_config.get("User_Roles_Data", "user_role_dropdown_label")
            print(f"user_role_dropdown_label: {user_role_dropdown_label}")
            return user_role_dropdown_label
        except Exception as ex:
            print(ex.args)

    def get_user_role_dropdown_by_xpath(self):
        try:
            user_role_dropdown_by_xpath = self.config.get("user_roles", "user_role_dropdown_by_xpath")
            print(f"user_role_dropdown_by_xpath: {user_role_dropdown_by_xpath}")
            return user_role_dropdown_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_label_inside_dropdown_by_xpath(self):
        try:
            label_inside_dropdown_by_xpath = self.config.get("user_roles", "label_inside_dropdown_by_xpath")
            print(f"label_inside_dropdown_by_xpath: {label_inside_dropdown_by_xpath}")
            return label_inside_dropdown_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_label_inside_dropdown(self):
        try:
            label_inside_dropdown = self.common_test_data_config.get("User_Roles_Data", "label_inside_dropdown")
            print(f"label_inside_dropdown: {label_inside_dropdown}")
            return label_inside_dropdown
        except Exception as ex:
            print(ex.args)

    def get_role_option_in_user_role_dropdown_by_xpath(self):
        try:
            role_option_in_user_role_dropdown_by_xpath = self.config.get("user_roles",
                                                                         "role_option_in_user_role_dropdown_by_xpath")
            print(f"role_option_in_user_role_dropdown_by_xpath: {role_option_in_user_role_dropdown_by_xpath}")
            return role_option_in_user_role_dropdown_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_role_required_text_by_xpath(self):
        try:
            user_role_required_text_by_xpath = self.config.get("user_roles", "user_role_required_text_by_xpath")
            print(f"user_role_required_text_by_xpath: {user_role_required_text_by_xpath}")
            return user_role_required_text_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_role_required_text(self):
        try:
            user_role_required_text = self.common_test_data_config.get("User_Roles_Data", "user_role_required_text")
            print(f"user_role_required_text: {user_role_required_text}")
            return user_role_required_text
        except Exception as ex:
            print(ex.args)

    def get_password_label_by_xpath(self):
        try:
            password_label_by_xpath = self.config.get("user_roles", "password_label_by_xpath")
            print(f"password_label_by_xpath: {password_label_by_xpath}")
            return password_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_password_label(self):
        try:
            password_label = self.common_test_data_config.get("User_Roles_Data", "password_label")
            print(f"password_label: {password_label}")
            return password_label
        except Exception as ex:
            print(ex.args)

    def get_password_textbox_by_xpath(self):
        try:
            password_textbox_by_xpath = self.config.get("user_roles", "password_textbox_by_xpath")
            print(f"password_textbox_by_xpath: {password_textbox_by_xpath}")
            return password_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_password_required_text_by_xpath(self):
        try:
            password_required_text_by_xpath = self.config.get("user_roles", "password_required_text_by_xpath")
            print(f"password_required_text_by_xpath: {password_required_text_by_xpath}")
            return password_required_text_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_password_required_text(self):
        try:
            password_required_text = self.common_test_data_config.get("User_Roles_Data", "password_required_text")
            print(f"password_required_text: {password_required_text}")
            return password_required_text
        except Exception as ex:
            print(ex.args)

    def get_region_text(self):
        try:
            region_text = self.common_test_data_config.get("User_Roles_Data", "region")
            print(f"password_required_text: {region_text}")
            return region_text
        except Exception as ex:
            print(ex.args)

    def get_confirm_password_textbox_by_xpath(self):
        try:
            confirm_password_textbox_by_xpath = self.config.get("user_roles", "confirm_password_textbox_by_xpath")
            print(f"confirm_password_textbox_by_xpath: {confirm_password_textbox_by_xpath}")
            return confirm_password_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_confirm_password_required_text_by_xpath(self):
        try:
            confirm_password_required_text_by_xpath = self.config.get("user_roles",
                                                                      "confirm_password_required_text_by_xpath")
            print(f"confirm_password_required_text_by_xpath: {confirm_password_required_text_by_xpath}")
            return confirm_password_required_text_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_confirm_password_required_text(self):
        try:
            confirm_password_required_text = self.common_test_data_config.get("User_Roles_Data", "confirm_password_required_text")
            print(f"confirm_password_required_text: {confirm_password_required_text}")
            return confirm_password_required_text
        except Exception as ex:
            print(ex.args)

    def get_company_label_by_xpath(self):
        try:
            company_label_by_xpath = self.config.get("user_roles", "company_label_by_xpath")
            print(f"company_label_by_xpath: {company_label_by_xpath}")
            return company_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_company_label(self):
        try:
            company_label = self.common_test_data_config.get("User_Roles_Data", "company_label")
            print(f"company_label: {company_label}")
            return company_label
        except Exception as ex:
            print(ex.args)

    def get_company_textbox_by_xpath(self):
        try:
            company_textbox_by_xpath = self.config.get("user_roles", "company_textbox_by_xpath")
            print(f"company_textbox_by_xpath: {company_textbox_by_xpath}")
            return company_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_label_by_xpath(self):
        try:
            title_label_by_xpath = self.config.get("user_roles", "title_label_by_xpath")
            print(f"title_label_by_xpath: {title_label_by_xpath}")
            return title_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_label(self):
        try:
            title_label = self.common_test_data_config.get("User_Roles_Data", "title_label")
            print(f"title_label: {title_label}")
            return title_label
        except Exception as ex:
            print(ex.args)

    def get_title_textbox_by_xpath(self):
        try:
            title_textbox_by_xpath = self.config.get("user_roles", "title_textbox_by_xpath")
            print(f"title_textbox_by_xpath: {title_textbox_by_xpath}")
            return title_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_region_label_by_xpath(self):
        try:
            region_label_by_xpath = self.config.get("user_roles", "region_label_by_xpath")
            print(f"region_label_by_xpath: {region_label_by_xpath}")
            return region_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_region_label(self):
        try:
            region_label = self.common_test_data_config.get("User_Roles_Data", "region_label")
            print(f"region_label: {region_label}")
            return region_label
        except Exception as ex:
            print(ex.args)

    def get_region_selection_button_by_xpath(self):
        try:
            region_selection_button_by_xpath = self.config.get("user_roles", "region_selection_button_by_xpath")
            print(f"region_selection_button_by_xpath: {region_selection_button_by_xpath}")
            return region_selection_button_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_region_selection_button_text_by_xpath(self):
        try:
            region_selection_button_text_by_xpath = self.config.get("user_roles",
                                                                    "region_selection_button_text_by_xpath")
            print(f"region_selection_button_text_by_xpath: {region_selection_button_text_by_xpath}")
            return region_selection_button_text_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_region_selection_button_text(self):
        try:
            region_selection_button_text = self.common_test_data_config.get("User_Roles_Data", "region_selection_button_text")
            print(f"region_selection_button_text: {region_selection_button_text}")
            return region_selection_button_text
        except Exception as ex:
            print(ex.args)

    def get_region_required_text_by_xpath(self):
        try:
            region_required_text_by_xpath = self.config.get("user_roles", "region_required_text_by_xpath")
            print(f"region_required_text_by_xpath: {region_required_text_by_xpath}")
            return region_required_text_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_region_required_text(self):
        try:
            region_required_text = self.common_test_data_config.get("User_Roles_Data", "region_required_text")
            print(f"region_required_text: {region_required_text}")
            return region_required_text
        except Exception as ex:
            print(ex.args)

    def get_region_tree_dialog_box_by_xpath(self):
        try:
            region_tree_dialog_box_by_xpath = self.config.get("user_roles", "region_tree_dialog_box_by_xpath")
            print(f"region_tree_dialog_box_by_xpath: {region_tree_dialog_box_by_xpath}")
            return region_tree_dialog_box_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_close_btn_on_region_tree_dialog_box_by_xpath(self):
        try:
            close_btn_on_region_tree_dialog_box_by_xpath = self.config.get("user_roles", "close_btn_on_region_tree_dialog_box_by_xpath")
            print(f"close_btn_on_region_tree_dialog_box_by_xpath: {close_btn_on_region_tree_dialog_box_by_xpath}")
            return close_btn_on_region_tree_dialog_box_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_save_btn_on_region_tree_dialog_box_by_xpath(self):
        try:
            save_btn_on_region_tree_dialog_box_by_xpath = self.config.get("user_roles", "save_btn_on_region_tree_dialog_box_by_xpath")
            print(f"save_btn_on_region_tree_dialog_box_by_xpath: {save_btn_on_region_tree_dialog_box_by_xpath}")
            return save_btn_on_region_tree_dialog_box_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_expand_all_btn_on_region_tree_dialog_box_by_xpath(self):
        try:
            expand_all_btn_on_region_tree_dialog_box_by_xpath = self.config.get("user_roles", "expand_all_btn_on_region_tree_dialog_box_by_xpath")
            print(f"expand_all_btn_on_region_tree_dialog_box_by_xpath: {expand_all_btn_on_region_tree_dialog_box_by_xpath}")
            return expand_all_btn_on_region_tree_dialog_box_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_collapse_all_btn_on_region_tree_dialog_box_by_xpath(self):
        try:
            collapse_all_btn_on_region_tree_dialog_box_by_xpath = self.config.get("user_roles", "collapse_all_btn_on_region_tree_dialog_box_by_xpath")
            print(f"collapse_all_btn_on_region_tree_dialog_box_by_xpath: {collapse_all_btn_on_region_tree_dialog_box_by_xpath}")
            return collapse_all_btn_on_region_tree_dialog_box_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_search_text_box_on_region_tree_dialog_box_by_xpath(self):
        try:
            search_text_box_on_region_tree_dialog_box_by_xpath = self.config.get("user_roles", "search_text_box_on_region_tree_dialog_box_by_xpath")
            print(f"search_text_box_on_region_tree_dialog_box_by_xpath: {search_text_box_on_region_tree_dialog_box_by_xpath}")
            return search_text_box_on_region_tree_dialog_box_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_region_in_regions_by_xpath(self):
        try:
            region_in_regions_by_xpath = self.config.get("user_roles", "region_in_regions_by_xpath")
            print(f"region_in_regions_by_xpath: {region_in_regions_by_xpath}")
            return region_in_regions_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_region_children_by_xpath(self):
        try:
            region_children_by_xpath = self.config.get("user_roles", "region_children_by_xpath")
            print(f"region_children_by_xpath: {region_children_by_xpath}")
            return region_children_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_department_label_by_xpath(self):
        try:
            department_label_by_xpath = self.config.get("user_roles", "department_label_by_xpath")
            print(f"department_label_by_xpath: {department_label_by_xpath}")
            return department_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_department_label(self):
        try:
            department_label = self.common_test_data_config.get("User_Roles_Data", "department_label")
            print(f"department_label: {department_label}")
            return department_label
        except Exception as ex:
            print(ex.args)

    def get_department_textbox_by_xpath(self):
        try:
            department_textbox_by_xpath = self.config.get("user_roles", "department_textbox_by_xpath")
            print(f"department_textbox_by_xpath: {department_textbox_by_xpath}")
            return department_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_email_label_by_xpath(self):
        try:
            email_label_by_xpath = self.config.get("user_roles", "email_label_by_xpath")
            print(f"email_label_by_xpath: {email_label_by_xpath}")
            return email_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_email_label(self):
        try:
            email_label = self.common_test_data_config.get("User_Roles_Data", "email_label")
            print(f"email_label: {email_label}")
            return email_label
        except Exception as ex:
            print(ex.args)

    def get_email_textbox_by_xpath(self):
        try:
            email_textbox_by_xpath = self.config.get("user_roles", "email_textbox_by_xpath")
            print(f"email_textbox_by_xpath: {email_textbox_by_xpath}")
            return email_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_email_required_text_by_xpath(self):
        try:
            email_required_text_by_xpath = self.config.get("user_roles", "email_required_text_by_xpath")
            print(f"email_required_text_by_xpath: {email_required_text_by_xpath}")
            return email_required_text_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_email_required_text(self):
        try:
            email_required_text = self.common_test_data_config.get("User_Roles_Data", "email_required_text")
            print(f"email_required_text: {email_required_text}")
            return email_required_text
        except Exception as ex:
            print(ex.args)

    def get_alert_email_label_by_xpath(self):
        try:
            alert_email_label_by_xpath = self.config.get("user_roles", "alert_email_label_by_xpath")
            print(f"alert_email_label_by_xpath: {alert_email_label_by_xpath}")
            return alert_email_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_alert_email_label(self):
        try:
            alert_email_label = self.common_test_data_config.get("User_Roles_Data", "alert_email_label")
            print(f"alert_email_label : {alert_email_label}")
            return alert_email_label
        except Exception as ex:
            print(ex.args)

    def get_alert_email_textbox_by_xpath(self):
        try:
            alert_email_textbox_by_xpath = self.config.get("user_roles", "alert_email_textbox_by_xpath")
            print(f"alert_email_textbox_by_xpath: {alert_email_textbox_by_xpath}")
            return alert_email_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_alert_phone_number_label_by_xpath(self):
        try:
            alert_phone_number_label_by_xpath = self.config.get("user_roles", "alert_phone_number_label_by_xpath")
            print(f"alert_email_textbox_by_xpath: {alert_phone_number_label_by_xpath}")
            return alert_phone_number_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_alert_phone_number_label(self):
        try:
            alert_phone_number_label = self.common_test_data_config.get("User_Roles_Data", "alert_phone_number_label")
            print(f"alert_phone_number_label: {alert_phone_number_label}")
            return alert_phone_number_label
        except Exception as ex:
            print(ex.args)

    def get_alert_phone_number_textbox_by_xpath(self):
        try:
            alert_phone_number_textbox_by_xpath = self.config.get("user_roles", "alert_phone_number_textbox_by_xpath")
            print(f"alert_phone_number_textbox_by_xpath: {alert_phone_number_textbox_by_xpath}")
            return alert_phone_number_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_timezone_label_by_xpath(self):
        try:
            timezone_label_by_xpath = self.config.get("user_roles", "timezone_label_by_xpath")
            print(f"timezone_label_by_xpath: {timezone_label_by_xpath}")
            return timezone_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_timezone_label(self):
        try:
            timezone_label = self.common_test_data_config.get("User_Roles_Data", "timezone_label")
            print(f"timezone_label: {timezone_label}")
            return timezone_label
        except Exception as ex:
            print(ex.args)

    def get_timezone_dropdown_by_xpath(self):
        try:
            timezone_dropdown_by_xpath = self.config.get("user_roles", "timezone_dropdown_by_xpath")
            print(f"timezone_dropdown_by_xpath: {timezone_dropdown_by_xpath}")
            return timezone_dropdown_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_timezone_required_text_below_dropdown(self):
        try:
            timezone_required_text_below_dropdown = self.config.get("user_roles", "timezone_required_text_below_dropdown")
            print(f"timezone_required_text_below_dropdown: {timezone_required_text_below_dropdown}")
            return timezone_required_text_below_dropdown
        except Exception as ex:
            print(ex.args)

    def get_timezone_required_text(self):
        try:
            timezone_required_text = self.common_test_data_config.get("User_Roles_Data", "timezone_required_text")
            print(f"timezone_required_text: {timezone_required_text}")
            return timezone_required_text
        except Exception as ex:
            print(ex.args)

    def get_timezone_dropdown_options_by_xpath(self):
        try:
            timezone_dropdown_options_by_xpath = self.config.get("user_roles", "timezone_dropdown_options_by_xpath")
            print(f"timezone_dropdown_options_by_xpath: {timezone_dropdown_options_by_xpath}")
            return timezone_dropdown_options_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_address_label_by_xpath(self):
        try:
            address_label_by_xpath = self.config.get("user_roles", "address_label_by_xpath")
            print(f"address_label_by_xpath : {address_label_by_xpath }")
            return address_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_address_label(self):
        try:
            address_label = self.common_test_data_config.get("User_Roles_Data", "address_label")
            print(f"address_label: {address_label}")
            return address_label
        except Exception as ex:
            print(ex.args)

    def get_address_textbox_by_xpath(self):
        try:
            address_textbox_by_xpath = self.config.get("user_roles", "address_textbox_by_xpath")
            print(f"address_textbox_by_xpath: {address_textbox_by_xpath}")
            return address_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_address_2_label_by_xpath(self):
        try:
            address_2_label_by_xpath = self.config.get("user_roles", "address_2_label_by_xpath")
            print(f"address_2_label_by_xpath: {address_2_label_by_xpath}")
            return address_2_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_address_2_label(self):
        try:
            address_2_label = self.common_test_data_config.get("User_Roles_Data", "address_2_label")
            print(f"address_2_label: {address_2_label}")
            return address_2_label
        except Exception as ex:
            print(ex.args)

    def get_address_2_textbox_by_xpath(self):
        try:
            address_2_textbox_by_xpath = self.config.get("user_roles", "address_2_textbox_by_xpath")
            print(f"address_2_textbox_by_xpath: {address_2_textbox_by_xpath}")
            return address_2_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_city_label_by_xpath(self):
        try:
            city_label_by_xpath = self.config.get("user_roles", "city_label_by_xpath")
            print(f"city_label_by_xpath: {city_label_by_xpath}")
            return city_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_city_label(self):
        try:
            city_label = self.common_test_data_config.get("User_Roles_Data", "city_label")
            print(f"city_label: {city_label}")
            return city_label
        except Exception as ex:
            print(ex.args)

    def get_city_textbox_by_xpath(self):
        try:
            city_textbox_by_xpath = self.config.get("user_roles", "city_textbox_by_xpath")
            print(f"city_textbox_by_xpath: {city_textbox_by_xpath}")
            return city_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_state_label_by_xpath(self):
        try:
            state_label_by_xpath = self.config.get("user_roles", "state_label_by_xpath")
            print(f"state_label_by_xpath: {state_label_by_xpath}")
            return state_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_state_label(self):
        try:
            state_label = self.common_test_data_config.get("User_Roles_Data", "state_label")
            print(f"state_label: {state_label}")
            return state_label
        except Exception as ex:
            print(ex.args)

    def get_state_textbox_by_xpath(self):
        try:
            state_textbox_by_xpath = self.config.get("user_roles", "state_textbox_by_xpath")
            print(f"state_textbox_by_xpath: {state_textbox_by_xpath}")
            return state_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_postal_code_label_by_xpath(self):
        try:
            postal_code_label_by_xpath = self.config.get("user_roles", "postal_code_label_by_xpath")
            print(f"postal_code_label_by_xpath: {postal_code_label_by_xpath}")
            return postal_code_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_postal_code_label(self):
        try:
            postal_code_label = self.common_test_data_config.get("User_Roles_Data", "postal_code_label")
            print(f"postal_code_label: {postal_code_label}")
            return postal_code_label
        except Exception as ex:
            print(ex.args)

    def get_postal_code_textbox_by_xpath(self):
        try:
            postal_code_textbox_by_xpath = self.config.get("user_roles","postal_code_textbox_by_xpath")
            print(f"postal_code_textbox_by_xpath: {postal_code_textbox_by_xpath}")
            return postal_code_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_home_phone_number_label_by_xpath(self):
        try:
            home_phone_number_label_by_xpath = self.config.get("user_roles", "home_phone_number_label_by_xpath")
            print(f"home_phone_number_label_by_xpath: {home_phone_number_label_by_xpath}")
            return home_phone_number_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_home_phone_number_label(self):
        try:
            home_phone_number_label = self.common_test_data_config.get("User_Roles_Data", "home_phone_number_label")
            print(f"home_phone_number_label: {home_phone_number_label}")
            return home_phone_number_label
        except Exception as ex:
            print(ex.args)

    def get_home_phone_number_textbox_by_xpath(self):
        try:
            home_phone_number_textbox_by_xpath = self.config.get("user_roles", "home_phone_number_textbox_by_xpath")
            print(f"home_phone_number_textbox_by_xpath: {home_phone_number_textbox_by_xpath}")
            return home_phone_number_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_work_phone_number_label_by_xpath(self):
        try:
            work_phone_number_label_by_xpath = self.config.get("user_roles", "work_phone_number_label_by_xpath")
            print(f"work_phone_number_label_by_xpath: {work_phone_number_label_by_xpath}")
            return work_phone_number_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_work_phone_number_label(self):
        try:
            work_phone_number_label = self.common_test_data_config.get("User_Roles_Data", "work_phone_number_label")
            print(f"work_phone_number_label: {work_phone_number_label}")
            return work_phone_number_label
        except Exception as ex:
            print(ex.args)

    def get_work_phone_number_textbox_by_xpath(self):
        try:
            work_phone_number_textbox_by_xpath = self.config.get("user_roles", "work_phone_number_textbox_by_xpath")
            print(f"work_phone_number_textbox_by_xpath: {work_phone_number_textbox_by_xpath}")
            return work_phone_number_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_fax_phone_number_label_by_xpath(self):
        try:
            fax_phone_number_label_by_xpath = self.config.get("user_roles", "fax_phone_number_label_by_xpath")
            print(f"fax_phone_number_label_by_xpath: {fax_phone_number_label_by_xpath}")
            return fax_phone_number_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_fax_phone_number_label(self):
        try:
            fax_phone_number_label = self.common_test_data_config.get("User_Roles_Data", "fax_phone_number_label")
            print(f"fax_phone_number_label: {fax_phone_number_label}")
            return fax_phone_number_label
        except Exception as ex:
            print(ex.args)

    def get_fax_phone_number_textbox_by_xpath(self):
        try:
            fax_phone_number_textbox_by_xpath = self.config.get("user_roles", "fax_phone_number_textbox_by_xpath")
            print(f"fax_phone_number_textbox_by_xpath: {fax_phone_number_textbox_by_xpath}")
            return fax_phone_number_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_phone_type_label_by_xpath(self):
        try:
            phone_type_label_by_xpath = self.config.get("user_roles", "phone_type_label_by_xpath")
            print(f"phone_type_label_by_xpath : {phone_type_label_by_xpath}")
            return phone_type_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_phone_type_label(self):
        try:
            phone_type_label = self.common_test_data_config.get("User_Roles_Data", "phone_type_label")
            print(f"phone_type_label: {phone_type_label}")
            return phone_type_label
        except Exception as ex:
            print(ex.args)

    def get_phone_type_textbox_by_xpath(self):
        try:
            phone_type_textbox_by_xpath = self.config.get("user_roles", "phone_type_textbox_by_xpath")
            print(f"phone_type_textbox_by_xpath: {phone_type_textbox_by_xpath}")
            return phone_type_textbox_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_phone_provider_label_by_xpath(self):
        try:
            phone_provider_label_by_xpath = self.config.get("user_roles", "phone_provider_label_by_xpath")
            print(f"phone_provider_label_by_xpath: {phone_provider_label_by_xpath}")
            return phone_provider_label_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_phone_provider_label(self):
        try:
            phone_provider_label = self.common_test_data_config.get("User_Roles_Data", "phone_provider_label")
            print(f"phone_provider_label: {phone_provider_label}")
            return phone_provider_label
        except Exception as ex:
            print(ex.args)

    def get_phone_provider_dropdown_by_xpath(self):
        try:
            phone_provider_dropdown_by_xpath = self.config.get("user_roles", "phone_provider_dropdown_by_xpath")
            print(f"phone_provider_dropdown_by_xpath: {phone_provider_dropdown_by_xpath}")
            return phone_provider_dropdown_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_option_inside_phone_provider_dropdown_by_xpath(self):
        try:
            option_inside_phone_provider_dropdown_by_xpath = self.config.get("user_roles", "option_inside_phone_provider_dropdown_by_xpath")
            print(f"option_inside_phone_provider_dropdown_by_xpath: {option_inside_phone_provider_dropdown_by_xpath}")
            return option_inside_phone_provider_dropdown_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_alert_schedule_button_by_xpath(self):
        try:
            alert_schedule_button_by_xpath = self.config.get("user_roles", "alert_schedule_button_by_xpath")
            print(f"alert_schedule_button_by_xpath: {alert_schedule_button_by_xpath}")
            return alert_schedule_button_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_alert_schedule_button_text(self):
        try:
            alert_schedule_button_text = self.common_test_data_config.get("User_Roles_Data", "alert_schedule_button_text")
            print(f"alert_schedule_button_text: {alert_schedule_button_text}")
            return alert_schedule_button_text
        except Exception as ex:
            print(ex.args)

    def get_notification_groups_button_by_xpath(self):
        try:
            notification_groups_button_by_xpath = self.config.get("user_roles", "notification_groups_button_by_xpath")
            print(f"notification_groups_button_by_xpath: {notification_groups_button_by_xpath}")
            return notification_groups_button_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_form_xpath(self):
        try:
            user_form_xpath = self.config.get("user_roles", "user_form_xpath")
            print(f"user_form_xpath: {user_form_xpath}")
            return user_form_xpath
        except Exception as ex:
            print(ex.args)

    def get_notification_groups_button_at_end_by_xpath(self):
        try:
            notification_groups_button_by_xpath = self.config.get("user_roles", "notification_groups_button_at_end_by_xpath")
            print(f"notification_groups_button_by_xpath: {notification_groups_button_by_xpath}")
            return notification_groups_button_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_notification_groups_button_at_end(self):
        try:
            notification_groups_button_at_end = self.common_test_data_config.get("User_Roles_Data", "notification_groups_button_at_end")
            print(f"notification_groups_button_at_end: {notification_groups_button_at_end}")
            return notification_groups_button_at_end
        except Exception as ex:
            print(ex.args)

    def get_username(self):
        try:
            username = self.common_test_data_config.get("User_Roles_Data", "username")
            print(f"username: {username}")
            return username
        except Exception as ex:
            print(ex.args)

    def get_first_name(self):
        try:
            first_name = self.common_test_data_config.get("User_Roles_Data", "first_name")
            print(f"first_name: {first_name}")
            return first_name
        except Exception as ex:
            print(ex.args)

    def get_last_name(self):
        try:
            last_name = self.common_test_data_config.get("User_Roles_Data", "last_name")
            print(f"last_name: {last_name}")
            return last_name
        except Exception as ex:
            print(ex.args)

    def get_user_role(self):
        try:
            user_role = self.common_test_data_config.get("User_Roles_Data", "user_role")
            print(f"user_role: {user_role}")
            return user_role
        except Exception as ex:
            print(ex.args)

    def get_password(self):
        try:
            password = self.common_test_data_config.get("User_Roles_Data", "password")
            print(f"password: {password}")
            return password
        except Exception as ex:
            print(ex.args)

    def get_company(self):
        try:
            company = self.common_test_data_config.get("User_Roles_Data", "company")
            print(f"company: {company}")
            return company
        except Exception as ex:
            print(ex.args)

    def get_title(self):
        try:
            title = self.common_test_data_config.get("User_Roles_Data", "title")
            print(f"title: {title}")
            return title
        except Exception as ex:
            print(ex.args)

    def get_department(self):
        try:
            department = self.common_test_data_config.get("User_Roles_Data", "department")
            print(f"department : {department}")
            return department
        except Exception as ex:
            print(ex.args)

    def get_email(self):
        try:
            email = self.common_test_data_config.get("User_Roles_Data", "email")
            print(f"email: {email}")
            return email
        except Exception as ex:
            print(ex.args)

    def get_alert_phone_number(self):
        try:
            alert_phone_number = self.common_test_data_config.get("User_Roles_Data", "alert_phone_number")
            print(f"alert_phone_number: {alert_phone_number}")
            return alert_phone_number
        except Exception as ex:
            print(ex.args)

    def get_time_zone(self):
        try:
            time_zone = self.common_test_data_config.get("User_Roles_Data", "time_zone")
            print(f"time_zone: {time_zone}")
            return time_zone
        except Exception as ex:
            print(ex.args)

    def get_address(self):
        try:
            address = self.common_test_data_config.get("User_Roles_Data", "address")
            print(f"address: {address}")
            return address
        except Exception as ex:
            print(ex.args)

    def get_address_2(self):
        try:
            address_2 = self.common_test_data_config.get("User_Roles_Data", "address_2")
            print(f"address_2: {address_2}")
            return address_2
        except Exception as ex:
            print(ex.args)

    def get_city(self):
        try:
            city = self.common_test_data_config.get("User_Roles_Data", "city")
            print(f"city: {city}")
            return city
        except Exception as ex:
            print(ex.args)

    def get_state(self):
        try:
            state = self.common_test_data_config.get("User_Roles_Data", "state")
            print(f"state: {state}")
            return state
        except Exception as ex:
            print(ex.args)

    def get_postal_code(self):
        try:
            postal_code = self.common_test_data_config.get("User_Roles_Data", "postal_code")
            print(f"postal_code: {postal_code}")
            return postal_code
        except Exception as ex:
            print(ex.args)

    def get_home_phone_number(self):
        try:
            home_phone_number = self.common_test_data_config.get("User_Roles_Data", "home_phone_number")
            print(f"home_phone_number: {home_phone_number}")
            return home_phone_number
        except Exception as ex:
            print(ex.args)

    def get_work_phone_number(self):
        try:
            work_phone_number = self.common_test_data_config.get("User_Roles_Data", "work_phone_number")
            return work_phone_number
        except Exception as ex:
            print(ex.args)

    def get_fax_phone_number(self):
        try:
            fax_phone_number = self.common_test_data_config.get("User_Roles_Data", "fax_phone_number")
            print(f"fax_phone_number: {fax_phone_number}")
            return fax_phone_number
        except Exception as ex:
            print(ex.args)

    def get_phone_type(self):
        try:
            phone_type = self.common_test_data_config.get("User_Roles_Data", "phone_type")
            print(f"phone_type: {phone_type}")
            return phone_type
        except Exception as ex:
            print(ex.args)

    def get_phone_provider(self):
        try:
            phone_provider = self.common_test_data_config.get("User_Roles_Data", "phone_provider")
            print(f"phone_provider: {phone_provider}")
            return phone_provider
        except Exception as ex:
            print(ex.args)

    def get_region_option_in_region_by_xpath(self):
        try:
            region_option_in_region_by_xpath = self.config.get("user_roles", "region_option_in_region_by_xpath")
            print(f"region_option_in_region_by_xpath: {region_option_in_region_by_xpath}")
            return region_option_in_region_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_user_roles_checkboxes_by_xpath(self):
        try:
            user_roles_checkboxes_by_xpath = self.config.get("user_roles", "user_roles_checkboxes_by_xpath")
            return user_roles_checkboxes_by_xpath
        except Exception as ex:
            print(ex)

    def get_yes_delete_user_role_button_by_xpath(self):
        try:
            yes_delete_user_role_button_by_xpath = self.config.get("user_roles", "yes_delete_user_role_button_by_xpath")
            return yes_delete_user_role_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_user_role_panel_cancel_btn(self):
        try:
            user_role_panel_cancel_btn = self.config.get("user_roles", "user_role_panel_cancel_btn")
            return user_role_panel_cancel_btn
        except Exception as ex:
            print(ex)