import configparser
from pathlib import Path

file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Store_Groups_Module\\Data_From_INI\\store_groups_ini"
print("configure filepath: ", file_path)
common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"


class store_group_page_read_ini:
    def __init__(self):
        self.config = configparser.RawConfigParser()

        self.common_test_data_config = configparser.RawConfigParser()
        self.common_test_data_config.read(common_test_data_ini_file_path)
        try:
            self.config.read(file_path)
        except Exception as ex:
            print(ex)

    def get_store_groups_menu_by_xpath(self):
        try:
            store_group_menu_by_xpath = self.config.get("Store_Groups", "store_group_menu_by_xpath")
            print(f"store_group_menu_by_xpath: {store_group_menu_by_xpath}")
            return store_group_menu_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_action_dropdown_on_store_groups_panel_by_xpath(self):
        try:
            action_dropdown_on_store_groups_panel_by_xpath = \
                self.config.get("Store_Groups", "action_dropdown_on_store_groups_panel_by_xpath")
            print(f"action_dropdown_on_store_groups_panel_by_xpath: {action_dropdown_on_store_groups_panel_by_xpath}")
            return action_dropdown_on_store_groups_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_title_on_store_groups_panel_by_xpath(self):
        try:
            title_on_store_groups_panel_by_xpath = \
                self.config.get("Store_Groups", "title_on_store_groups_panel_by_xpath")
            print(f"title_on_store_groups_panel_by_xpath: {title_on_store_groups_panel_by_xpath}")
            return title_on_store_groups_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_create_store_group_option_by_xpath(self):
        try:
            create_store_group_option_by_xpath = \
                self.config.get("Store_Groups", "create_store_group_option_by_xpath")
            print(f"create_store_group_option_by_xpath: {create_store_group_option_by_xpath}")
            return create_store_group_option_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_name_field_for_creating_store_group_by_xpath(self):
        try:
            name_textbox_for_creating_store_group_by_xpath = \
                self.config.get("Store_Groups", "name_field_for_creating_store_group_by_xpath")
            print(f"name_field_for_creating_store_group_by_xpath: {name_textbox_for_creating_store_group_by_xpath}")
            return name_textbox_for_creating_store_group_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_description_field_by_xpath(self):
        try:
            description_field_by_xpath = self.config.get("Store_Groups", "description_field_by_xpath")
            print(f"description_field_by_xpath: {description_field_by_xpath}")
            return description_field_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_org_selection_button_by_xpath(self):
        try:
            org_selection_button_by_xpath = self.config.get("Store_Groups", "org_selection_button_by_xpath")
            print(f"org_selection_button_by_xpath: {org_selection_button_by_xpath}")
            return org_selection_button_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_save_button_on_store_group_creation_panel_by_xpath(self):
        try:
            save_button_on_store_group_creation_panel_by_xpath = \
                self.config.get("Store_Groups", "save_button_on_store_group_creation_panel_by_xpath")
            print(f"save_button_on_store_group_creation_panel_by_xpath: "
                  f"{save_button_on_store_group_creation_panel_by_xpath}")
            return save_button_on_store_group_creation_panel_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_store_group_creation_success_message_by_xpath(self):
        try:
            store_group_creation_success_message_by_xpath = \
                self.config.get("Store_Groups", "store_group_creation_success_message_by_xpath")
            print(f"store_group_creation_success_message_by_xpath: "
                  f"{store_group_creation_success_message_by_xpath}")
            return store_group_creation_success_message_by_xpath
        except Exception as ex:
            print(ex.args)

    def get_success_message_after_store_group_creation(self):
        try:
            success_message_after_store_group_creation = \
                self.config.get("Store_Groups", "success_message_after_store_group_creation")
            print(f"success_message_after_store_group_creation: "
                  f"{success_message_after_store_group_creation}")
            return success_message_after_store_group_creation
        except Exception as ex:
            print(ex.args)

    def get_store_group_name(self):
        try:
            store_group_name = self.common_test_data_config.get("system_level_test_Data", "store_group_name")
            print(f"store_group_name: {store_group_name}")
            return store_group_name
        except Exception as ex:
            print(ex.args)

    def get_store_group_description(self):
        try:
            store_group_description = self.common_test_data_config.get("system_level_test_Data", "store_group_description")
            print(f"store_group_description: {store_group_description}")
            return store_group_description
        except Exception as ex:
            print(ex.args)

    def get_root_region_input(self):
        try:
            root_region_input = self.common_test_data_config.get("common_data", "root_region_input")
            print(f"root_region_input: {root_region_input}")
            return root_region_input
        except Exception as ex:
            print(ex.args)


