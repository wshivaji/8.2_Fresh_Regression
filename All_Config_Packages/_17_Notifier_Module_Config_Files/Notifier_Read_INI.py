import configparser
from pathlib import Path

filepath = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\17_Notifier_Module\\Data_From_INI\\Notifier.ini"
print("configure filepath: ", filepath)


class Notifier_Read_ini:
    def __init__(self):
        try:
            self.config = configparser.RawConfigParser()
            self.config.read(filepath)
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print(ex)

    def get_old_face_first_url(self):
        try:
            old_face_first_url = self.common_test_data_config.get("Login_Logout_Data", "cloud_login_url")
            print("ff01 url: ", old_face_first_url)
            return old_face_first_url
        except Exception as ex:
            print(ex)

    def get_notifier(self):
        try:
            notifier_module = self.common_test_data_config.get("Notifier_Data", "notifier_module")
            print("Notifier module: ", notifier_module)
            return notifier_module
        except Exception as ex:
            print(ex)

    def get_notifier_module_by_xpath(self):
        try:
            notifier_module_by_xpath = self.config.get("Notifier", "notifier_module_by_xpath")
            print("Notifier module xpath: ", notifier_module_by_xpath)
            return notifier_module_by_xpath
        except Exception as ex:
            print(ex)

    def get_notifier_panel_heading_by_xpath(self):
        try:
            notifier_panel_heading_by_xpath = self.config.get("Notifier", "notifier_panel_heading_by_xpath")
            print("Notifier panel heading: ", notifier_panel_heading_by_xpath)
            return notifier_panel_heading_by_xpath
        except Exception as ex:
            print(ex)

    def get_user_name_by_xpath(self):
        try:
            user_name_by_xpath = self.config.get("Notifier", "user_name_by_xpath")
            print("username info: ", user_name_by_xpath)
            return user_name_by_xpath
        except Exception as ex:
            print(ex)

    def get_close_notifier_button_on_dashboard_menu_by_xpath(self):
        try:
            close_notifier_button_on_dashboard_menu_by_xpath = \
                self.config.get("Notifier", "close_notifier_button_on_dashboard_menu_by_xpath")
            print("Close Notifier button on dashboard: ", close_notifier_button_on_dashboard_menu_by_xpath)
            return close_notifier_button_on_dashboard_menu_by_xpath
        except Exception as ex:
            print(ex)

    def get_bullhorn_icon_on_close_notifier_btn_by_xpath(self):
        try:
            bullhorn_icon_on_close_notifier_btn_by_xpath = \
                self.config.get("Notifier", "bullhorn_icon_on_close_notifier_btn_by_xpath")
            print("bullhorn icon on close notifier button: ", bullhorn_icon_on_close_notifier_btn_by_xpath)
            return bullhorn_icon_on_close_notifier_btn_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_close_notifier_button_on_dashboard(self):
        try:
            expected_text_on_close_notifier_button_on_dashboard = \
                self.common_test_data_config.get("Notifier_Data", "expected_text_on_close_notifier_button_on_dashboard")
            print("expected text on close notifier button: ", expected_text_on_close_notifier_button_on_dashboard)
            return expected_text_on_close_notifier_button_on_dashboard
        except Exception as ex:
            print(ex)

    def get_text_on_close_notifier_btn_on_dashboard_by_xpath(self):
        try:
            text_on_close_notifier_btn_on_dashboard_by_xpath = \
                self.config.get("Notifier", "text_on_close_notifier_btn_on_dashboard_by_xpath")
            print("text on 'close notifier' button on dashboard: ", text_on_close_notifier_btn_on_dashboard_by_xpath)
            return text_on_close_notifier_btn_on_dashboard_by_xpath
        except Exception as ex:
            print(ex)

    def get_enrollment_group_selection_button_by_xpath(self):
        try:
            enrollment_group_selection_button_by_xpath = self.config.get("Notifier",
                                                                         "enrollment_group_selection_button_by_xpath")
            print("Enrollment Group Selection button: ", enrollment_group_selection_button_by_xpath)
            return enrollment_group_selection_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_group_icon_on_enrollment_group_selection_button_by_xpath(self):
        try:
            group_icon_on_enrollment_group_selection_button_by_xpath = \
                self.config.get("Notifier", "group_icon_on_enrollment_group_selection_button_by_xpath")
            print("Group icon on Enrollment Group Selection button: ",
                  group_icon_on_enrollment_group_selection_button_by_xpath)
            return group_icon_on_enrollment_group_selection_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_text_on_enrollment_group_selection_button_by_xpath(self):
        try:
            text_on_enrollment_group_selection_button_by_xpath = \
                self.config.get("Notifier", "text_on_enrollment_group_selection_button_by_xpath")
            print("text on Enrollment Group Selection button: ", text_on_enrollment_group_selection_button_by_xpath)
            return text_on_enrollment_group_selection_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_enrollment_group_selection_button(self):
        try:
            expected_text_on_enrollment_group_selection_button = \
                self.common_test_data_config.get("Notifier_Data", "expected_text_on_enrollment_group_selection_button")
            print("expected text on Enrollment Group Selection button: ",
                  expected_text_on_enrollment_group_selection_button)
            return expected_text_on_enrollment_group_selection_button
        except Exception as ex:
            print(ex)

    def get_org_hierarchy_selection_button_by_xpath(self):
        try:
            org_hierarchy_selection_button_by_xpath = self.config.get("Notifier",
                                                                      "org_hierarchy_selection_button_by_xpath")
            print("Org/Hierarchy Selection button: ", org_hierarchy_selection_button_by_xpath)
            return org_hierarchy_selection_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_dot_circle_icon_on_org_hierarchy_selection_button_by_xpath(self):
        try:
            dot_circle_icon_on_org_hierarchy_selection_button_by_xpath = \
                self.config.get("Notifier", "dot_circle_icon_on_org_hierarchy_selection_button_by_xpath")
            print("dot circle icon on Org/Hierarchy Selection button: ",
                  dot_circle_icon_on_org_hierarchy_selection_button_by_xpath)
            return dot_circle_icon_on_org_hierarchy_selection_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_text_on_org_hierarchy_selection_button_by_xpath(self):
        try:
            text_on_org_hierarchy_selection_button_by_xpath = \
                self.config.get("Notifier", "text_on_org_hierarchy_selection_button_by_xpath")
            print("text on Org/Hierarchy Selection button: ", text_on_org_hierarchy_selection_button_by_xpath)
            return text_on_org_hierarchy_selection_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_region_list_in_org_hierarchy_selection_by_xpath(self):
        try:
            region_list_in_org_hierarchy_selection_by_xpath = \
                self.config.get("Notifier", "region_list_in_org_hierarchy_selection_by_xpath")
            print("region list in Org/Hierarchy selection button: ", region_list_in_org_hierarchy_selection_by_xpath)
            return region_list_in_org_hierarchy_selection_by_xpath
        except Exception as ex:
            print(ex)

    def get_checkbox_besides_region_names_in_org_hierarchy_selection_by_xpath(self):
        try:
            checkbox_besides_region_names_in_org_hierarchy_selection_by_xpath = \
                self.config.get("Notifier", "checkbox_besides_region_names_in_org_hierarchy_selection_by_xpath")
            print("checkbox besides region: ", checkbox_besides_region_names_in_org_hierarchy_selection_by_xpath)
            return checkbox_besides_region_names_in_org_hierarchy_selection_by_xpath
        except Exception as ex:
            print(ex)

    def get_checkbox_in_region_by_xpath_1(self):
        try:
            checkbox_in_region_by_xpath_1 = self.config.get("Notifier", "checkbox_in_region_by_xpath_1")
            print("Individual checkbox for region;first part: ", checkbox_in_region_by_xpath_1)
            return checkbox_in_region_by_xpath_1
        except Exception as ex:
            print(ex)

    def get_checkbox_in_region_by_xpath_2(self):
        try:
            checkbox_in_region_by_xpath_2 = self.config.get("Notifier", "checkbox_in_region_by_xpath_2")
            print("Individual checkbox for region;second part: ", checkbox_in_region_by_xpath_2)
            return checkbox_in_region_by_xpath_2
        except Exception as ex:
            print(ex)

    def get_expected_text_on_org_hierarchy_selection_button(self):
        try:
            expected_text_on_org_hierarchy_selection_button = \
                self.config.get("Notifier", "expected_text_on_org_hierarchy_selection_button")
            print("expected text on Org/Hierarchy Selection button: ", expected_text_on_org_hierarchy_selection_button)
            return expected_text_on_org_hierarchy_selection_button
        except Exception as ex:
            print(ex)

    def get_notifier_setting_button_by_xpath(self):
        try:
            notifier_setting_button_by_xpath = self.config.get("Notifier", "notifier_setting_button_by_xpath")
            print("Notifier Setting button: ", notifier_setting_button_by_xpath)
            return notifier_setting_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_gear_icon_on_notifier_setting_button_by_xpath(self):
        try:
            gear_icon_on_notifier_setting_button_by_xpath = \
                self.config.get("Notifier", "gear_icon_on_notifier_setting_button_by_xpath")
            print("gear icon on Notifier Setting button: ", gear_icon_on_notifier_setting_button_by_xpath)
            return gear_icon_on_notifier_setting_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_text_on_notifier_setting_button_by_xpath(self):
        try:
            text_on_notifier_setting_button_by_xpath = \
                self.config.get("Notifier", "text_on_notifier_setting_button_by_xpath")
            print("text on Notifier Setting button: ", text_on_notifier_setting_button_by_xpath)
            return text_on_notifier_setting_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_notifier_setting_button(self):
        try:
            expected_text_on_notifier_setting_button = \
                self.common_test_data_config.get("Notifier_Data", "expected_text_on_notifier_setting_button")
            print("expected text on Notifier Setting button: ", expected_text_on_notifier_setting_button)
            return expected_text_on_notifier_setting_button
        except Exception as ex:
            print(ex)

    def get_close_notifier_button_on_notifier_panel_by_xpath(self):
        try:
            close_notifier_button_on_notifier_panel_by_xpath = \
                self.config.get("Notifier", "close_notifier_button_on_notifier_panel_by_xpath")
            print("close notifier button on notifier panel: ", close_notifier_button_on_notifier_panel_by_xpath)
            return close_notifier_button_on_notifier_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_close_symbol_on_close_notifier_button_by_xpath(self):
        try:
            close_symbol_on_close_notifier_button_by_xpath = \
                self.config.get("Notifier", "close_symbol_on_close_notifier_button_by_xpath")
            print("close symbol on close notifier button: ", close_symbol_on_close_notifier_button_by_xpath)
            return close_symbol_on_close_notifier_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_select_group_dialog_box_in_enrollment_group_selection_by_xpath(self):
        try:
            select_group_dialog_box_in_enrollment_group_selection_by_xpath = \
                self.config.get("Notifier", "select_group_dialog_box_in_enrollment_group_selection_by_xpath")
            print("'Select a group' dialog box in Enrollment Group Selection: ",
                  select_group_dialog_box_in_enrollment_group_selection_by_xpath)
            return select_group_dialog_box_in_enrollment_group_selection_by_xpath
        except Exception as ex:
            print(ex)

    def get_heading_on_select_a_group_dialog_box_by_xpath(self):
        try:
            heading_on_select_a_group_dialog_box_by_xpath = \
                self.config.get("Notifier", "heading_on_select_a_group_dialog_box_by_xpath")
            print("Heading on 'Select a group' dialog box: ", heading_on_select_a_group_dialog_box_by_xpath)
            return heading_on_select_a_group_dialog_box_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_heading_on_select_a_group_dialog_box(self):
        try:
            expected_heading_on_select_a_group_dialog_box = \
                self.common_test_data_config.get("Notifier_Data", "expected_heading_on_select_a_group_dialog_box")
            print("expected heading on 'Select a group' dialog box: ", expected_heading_on_select_a_group_dialog_box)
            return expected_heading_on_select_a_group_dialog_box
        except Exception as ex:
            print(ex)

    def get_close_button_on_group_selection_panel_by_xpath(self):
        try:
            close_button_on_group_selection_panel_by_xpath = \
                self.config.get("Notifier", "close_button_on_group_selection_panel_by_xpath")
            print("close button on group selection panel: ", close_button_on_group_selection_panel_by_xpath)
            return close_button_on_group_selection_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_filter_group_list_textbox_by_xpath(self):
        try:
            filter_group_list_textbox_by_xpath = self.config.get("Notifier", "filter_group_list_textbox_by_xpath")
            print("'filter group list below..' textbox: ", filter_group_list_textbox_by_xpath)
            return filter_group_list_textbox_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_label_on_filter_group_list_textbox(self):
        try:
            expected_label_on_filter_group_list_textbox = \
                self.common_test_data_config.get("Notifier_Data", "expected_label_on_filter_group_list_textbox")
            print("expected label on 'filter group list' textbox: ", expected_label_on_filter_group_list_textbox)
            return expected_label_on_filter_group_list_textbox
        except Exception as ex:
            print(ex)

    def get_group_items_below_filter_group_list_textbox_by_xpath(self):
        try:
            group_items_below_filter_group_list_textbox_by_xpath = \
                self.config.get("Notifier", "group_items_below_filter_group_list_textbox_by_xpath")
            print("group list below filter group list textbox: ", group_items_below_filter_group_list_textbox_by_xpath)
            return group_items_below_filter_group_list_textbox_by_xpath
        except Exception as ex:
            print(ex)

    def get_group_list_from_enrollment_groups_module_by_xpath(self):
        try:
            group_list_from_enrollment_groups_module_by_xpath = \
                self.config.get("Notifier", "group_list_from_enrollment_groups_module_by_xpath")
            print("group list from Enrollment Groups module: ", group_list_from_enrollment_groups_module_by_xpath)
            return group_list_from_enrollment_groups_module_by_xpath
        except Exception as ex:
            print(ex)

    def get_enrollment_groups_close_panel_button_by_xpath(self):
        try:
            enrollment_groups_close_panel_button_by_xpath = \
                self.config.get("Notifier", "enrollment_groups_close_panel_button_by_xpath")
            print("Close panel button on Enrollment Groups panel: ", enrollment_groups_close_panel_button_by_xpath)
            return enrollment_groups_close_panel_button_by_xpath
        except Exception as ex:
            print(ex)

    def get_radio_buttons_in_select_a_group_panel_by_xpath(self):
        try:
            radio_buttons_in_select_a_group_panel_by_xpath = \
                self.config.get("Notifier", "radio_buttons_in_select_a_group_panel_by_xpath")
            print("radio buttons in 'Select a group' panel: ", radio_buttons_in_select_a_group_panel_by_xpath)
            return radio_buttons_in_select_a_group_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_group_names_in_select_a_group_panel_by_xpath(self):
        try:
            group_names_in_select_a_group_panel_by_xpath = \
                self.config.get("Notifier", "group_names_in_select_a_group_panel_by_xpath")
            print("Group names in 'Select a group' panel: ", group_names_in_select_a_group_panel_by_xpath)
            return group_names_in_select_a_group_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_text_selected_groups_by_xpath(self):
        try:
            text_selected_groups_by_xpath = self.config.get("Notifier", "text_selected_groups_by_xpath")
            print("text : ", text_selected_groups_by_xpath)
            return text_selected_groups_by_xpath
        except Exception as ex:
            print(ex)

    def get_name_of_group_selected_by_xpath(self):
        try:
            name_of_group_selected_by_xpath = self.config.get("Notifier", "name_of_group_selected_by_xpath")
            print("name of group selected: ", name_of_group_selected_by_xpath)
            return name_of_group_selected_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_selected_groups(self):
        try:
            expected_text_selected_groups = self.common_test_data_config.get("Notifier_Data", "expected_text_selected_groups")
            print("expected text: ", expected_text_selected_groups)
            return expected_text_selected_groups
        except Exception as ex:
            print(ex)

    def get_clear_button_on_select_a_group_panel_by_xpath(self):
        try:
            clear_button_on_select_a_group_panel_by_xpath = \
                self.config.get("Notifier", "clear_button_on_select_a_group_panel_by_xpath")
            print("'Clear' button on 'Select a group' panel: ", clear_button_on_select_a_group_panel_by_xpath)
            return clear_button_on_select_a_group_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_clear_button(self):
        try:
            expected_text_on_clear_button = self.common_test_data_config.get("Notifier_Data", "expected_text_on_clear_button")
            print("expected text on 'Clear' button: ", expected_text_on_clear_button)
            return expected_text_on_clear_button
        except Exception as ex:
            print(ex)

    def get_close_button_on_select_a_group_panel_by_xpath(self):
        try:
            close_button_on_select_a_group_panel_by_xpath = \
                self.config.get("Notifier", "close_button_on_select_a_group_panel_by_xpath")
            print("'Close' button on 'Select a group' panel: ", close_button_on_select_a_group_panel_by_xpath)
            return close_button_on_select_a_group_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_close_button(self):
        try:
            expected_text_on_close_button = self.common_test_data_config.get("Notifier_Data", "expected_text_on_close_button")
            print("expected text on 'Clear' button: ", expected_text_on_close_button)
            return expected_text_on_close_button
        except Exception as ex:
            print(ex)

    def get_save_button_on_select_a_group_panel_by_xpath(self):
        try:
            save_button_on_select_a_group_panel_by_xpath = \
                self.config.get("Notifier", "save_button_on_select_a_group_panel_by_xpath")
            print("'Save' button on 'Select a group' panel: ", save_button_on_select_a_group_panel_by_xpath)
            return save_button_on_select_a_group_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_save_button(self):
        try:
            expected_text_on_save_button = self.common_test_data_config.get("Notifier_Data", "expected_text_on_save_button")
            print("expected text on 'Save' button: ", expected_text_on_save_button)
            return expected_text_on_save_button
        except Exception as ex:
            print(ex)

    def get_org_region_panel_by_xpath(self):
        try:
            org_region_panel_by_xpath = self.config.get("Notifier", "org_region_panel_by_xpath")
            print("Region panel in Org/Hierarchy Selection: ", org_region_panel_by_xpath)
            return org_region_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_heading_on_region_selection_panel_by_xpath(self):
        try:
            heading_on_region_selection_panel_by_xpath = self.config.get("Notifier",
                                                                         "heading_on_region_selection_panel_by_xpath")
            print("Heading on region selection panel: ", heading_on_region_selection_panel_by_xpath)
            return heading_on_region_selection_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_heading_on_region_selection_panel(self):
        try:
            expected_heading_on_region_selection_panel = self.common_test_data_config.get("Notifier_Data",
                                                                         "expected_heading_on_region_selection_panel")
            print("expected heading on region selection panel: ", expected_heading_on_region_selection_panel)
            return expected_heading_on_region_selection_panel
        except Exception as ex:
            print(ex)

    def get_collapse_all_button_on_region_selection_panel_by_xpath(self):
        try:
            collapse_all_button_on_region_selection_panel_by_xpath = \
                self.config.get("Notifier", "collapse_all_button_on_region_selection_panel_by_xpath")
            print("'Collapse all' button on region selection panel: ",
                  collapse_all_button_on_region_selection_panel_by_xpath)
            return collapse_all_button_on_region_selection_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_collapse_all_button(self):
        try:
            expected_text_on_collapse_all_button = self.common_test_data_config.get("Notifier_Data", "expected_text_on_collapse_all_button")
            print("expected text on collapse all button: ", expected_text_on_collapse_all_button)
            return expected_text_on_collapse_all_button
        except Exception as ex:
            print(ex)

    def get_expand_all_button_on_region_selection_panel_by_xpath(self):
        try:
            expand_all_button_on_region_selection_panel_by_xpath = \
                self.config.get("Notifier", "expand_all_button_on_region_selection_panel_by_xpath")
            print("'Expand all' button on region selection panel: ",
                  expand_all_button_on_region_selection_panel_by_xpath)
            return expand_all_button_on_region_selection_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_expand_all_button(self):
        try:
            expected_text_on_expand_all_button = self.common_test_data_config.get("Notifier_Data", "expected_text_on_expand_all_button")
            print("expected text on expand all button: ", expected_text_on_expand_all_button)
            return expected_text_on_expand_all_button
        except Exception as ex:
            print(ex)

    def get_select_all_button_on_region_selection_panel_by_xpath(self):
        try:
            select_all_button_on_region_selection_panel_by_xpath = \
                self.config.get("Notifier", "select_all_button_on_region_selection_panel_by_xpath")
            print("'Select all' button on region selection panel: ",
                  select_all_button_on_region_selection_panel_by_xpath)
            return select_all_button_on_region_selection_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_select_all_button(self):
        try:
            expected_text_on_select_all_button = self.common_test_data_config.get("Notifier_Data", "expected_text_on_select_all_button")
            print("expected text on select all button: ", expected_text_on_select_all_button)
            return expected_text_on_select_all_button
        except Exception as ex:
            print(ex)

    def get_unselect_all_button_on_region_selection_panel_by_xpath(self):
        try:
            unselect_all_button_on_region_selection_panel_by_xpath = \
                self.config.get("Notifier", "unselect_all_button_on_region_selection_panel_by_xpath")
            print("'Unselect all' button on region selection panel: ",
                  unselect_all_button_on_region_selection_panel_by_xpath)
            return unselect_all_button_on_region_selection_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_unselect_all_button(self):
        try:
            expected_text_on_unselect_all_button = self.common_test_data_config.get("Notifier_Data", "expected_text_on_unselect_all_button")
            print("expected text on unselect all button: ", expected_text_on_unselect_all_button)
            return expected_text_on_unselect_all_button
        except Exception as ex:
            print(ex)

    def get_search_textbox_on_org_hierarchy_panel_by_xpath(self):
        try:
            search_textbox_on_org_hierarchy_panel_by_xpath = \
                self.config.get("Notifier", "search_textbox_on_org_hierarchy_panel_by_xpath")
            print("'Search' textbox in Org/Hierarchy Selection panel: ", search_textbox_on_org_hierarchy_panel_by_xpath)
            return search_textbox_on_org_hierarchy_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_label_on_search_textbox(self):
        try:
            expected_label_on_search_textbox = self.common_test_data_config.get("Notifier_Data", "expected_label_on_search_textbox")
            print("expected label on 'Search' textbox: ", expected_label_on_search_textbox)
            return expected_label_on_search_textbox
        except Exception as ex:
            print(ex)

    def get_close_button_on_org_hierarchy_panel_by_xpath(self):
        try:
            close_button_on_org_hierarchy_panel_by_xpath = \
                self.config.get("Notifier", "close_button_on_org_hierarchy_panel_by_xpath")
            print("'Close' button on Org/Hierarchy panel: ", close_button_on_org_hierarchy_panel_by_xpath)
            return close_button_on_org_hierarchy_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_save_button_on_org_hierarchy_panel_by_xpath(self):
        try:
            save_button_on_org_hierarchy_panel_by_xpath = \
                self.config.get("Notifier", "save_button_on_org_hierarchy_panel_by_xpath")
            print("'Save' button on Org/Hierarchy panel: ", save_button_on_org_hierarchy_panel_by_xpath)
            return save_button_on_org_hierarchy_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_notifier_setting_panel_by_xpath(self):
        try:
            notifier_setting_panel_by_xpath = self.config.get("Notifier", "notifier_setting_panel_by_xpath")
            print("'Notifier Setting' panel: ", notifier_setting_panel_by_xpath)
            return notifier_setting_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_heading_on_notifier_setting_panel_by_xpath(self):
        try:
            heading_on_notifier_setting_panel_by_xpath = \
                self.config.get("Notifier", "heading_on_notifier_setting_panel_by_xpath")
            print("Heading on Notifier Setting panel: ", heading_on_notifier_setting_panel_by_xpath)
            return heading_on_notifier_setting_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_cancel_button_on_notifier_setting_panel_by_xpath(self):
        try:
            cancel_button_on_notifier_setting_panel_by_xpath = \
                self.config.get("Notifier", "cancel_button_on_notifier_setting_panel_by_xpath")
            print("'Cancel' button on Notifier Setting' panel: ", cancel_button_on_notifier_setting_panel_by_xpath)
            return cancel_button_on_notifier_setting_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_save_button_on_notifier_setting_panel_by_xpath(self):
        try:
            save_button_on_notifier_setting_panel_by_xpath = \
                self.config.get("Notifier", "save_button_on_notifier_setting_panel_by_xpath")
            print("'Save' button on Notifier Setting panel: ", save_button_on_notifier_setting_panel_by_xpath)
            return save_button_on_notifier_setting_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_refresh_rate_text_by_xpath(self):
        try:
            refresh_rate_text_by_xpath = self.config.get("Notifier",
                                                         "refresh_rate_text_on_notifier_setting_panel_by_xpath")
            print("Refresh rate text: ", refresh_rate_text_by_xpath)
            return refresh_rate_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_of_events_display_text_on_notifier_panel_by_xpath(self):
        try:
            of_events_display_text_on_notifier_panel_by_xpath = \
                self.config.get("Notifier", "of_events_display_text_on_notifier_setting_panel_by_xpath")
            print("# Of events display text: ", of_events_display_text_on_notifier_panel_by_xpath)
            return of_events_display_text_on_notifier_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_station_name_for_of_event_generation_by_xpath(self):
        try:
            station_name_for_of_event_generation_by_xpath = \
                self.config.get("Notifier", "station_name_for_of_event_generation_by_xpath")
            print("Station name of event generation: ", station_name_for_of_event_generation_by_xpath)
            return station_name_for_of_event_generation_by_xpath
        except Exception as ex:
            print(ex)

    def get_cameras_in_region_by_xpath_1(self):
        try:
            cameras_in_region_by_xpath_1 = self.config.get("Notifier", "cameras_in_region_by_xpath_1")
            print("Cameras in region: ", cameras_in_region_by_xpath_1)
            return cameras_in_region_by_xpath_1
        except Exception as ex:
            print(ex)

    def get_cameras_in_region_by_xpath_2(self):
        try:
            cameras_in_region_by_xpath_2 = self.config.get("Notifier", "cameras_in_region_by_xpath_2")
            print("Cameras in region: ", cameras_in_region_by_xpath_2)
            return cameras_in_region_by_xpath_2
        except Exception as ex:
            print(ex)

    def get_regions_under_root_region_by_xpath(self):
        try:
            regions_under_root_region_by_xpath = self.config.get("Notifier", "regions_under_root_region_by_xpath")
            print("Regions under root region: ", regions_under_root_region_by_xpath)
            return regions_under_root_region_by_xpath
        except Exception as ex:
            print(ex)

    def get_checkboxes_for_regions_by_xpath(self):
        try:
            checkboxes_for_regions_by_xpath = self.config.get("Notifier", "checkboxes_for_regions_by_xpath")
            print("Check box for region: ", checkboxes_for_regions_by_xpath)
            return checkboxes_for_regions_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_cancel_button(self):
        try:
            expected_text_on_cancel_button = self.common_test_data_config.get("Notifier_Data", "expected_text_on_cancel_button")
            print("expected text on CANCEL button: ", expected_text_on_cancel_button)
            return expected_text_on_cancel_button
        except Exception as ex:
            print(ex)

    def get_expected_text_refresh_rate(self):
        try:
            expected_text_refresh_rate = self.common_test_data_config.get("Notifier_Data", "expected_text_refresh_rate")
            print("expected text: ", expected_text_refresh_rate)
            return expected_text_refresh_rate
        except Exception as ex:
            print(ex)

    def get_refresh_rate_dropdown_by_xpath(self):
        try:
            refresh_rate_dropdown_by_xpath = self.config.get("Notifier", "refresh_rate_dropdown_by_xpath")
            print("Refresh rate dropdown: ", refresh_rate_dropdown_by_xpath)
            return refresh_rate_dropdown_by_xpath
        except Exception as ex:
            print(ex)

    def get_refresh_rate_dropdown_options_by_xpath(self):
        try:
            refresh_rate_dropdown_options_by_xpath = self.config.get("Notifier",
                                                                     "refresh_rate_dropdown_options_by_xpath")
            print("Refresh Rate dropdown options: ", refresh_rate_dropdown_options_by_xpath)
            return refresh_rate_dropdown_options_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_of_events_display(self):
        try:
            expected_text_of_events_display = self.common_test_data_config.get("Notifier_Data", "expected_text_of_events_display")
            print("expected text: ", expected_text_of_events_display)
            return expected_text_of_events_display
        except Exception as ex:
            print(ex)

    def get_events_display_dropdown_by_xpath(self):
        try:
            events_display_dropdown_by_xpath = self.config.get("Notifier", "events_display_dropdown_by_xpath")
            print("events display dropdown: ", events_display_dropdown_by_xpath)
            return events_display_dropdown_by_xpath
        except Exception as ex:
            print(ex)

    def get_events_display_dropdown_options_by_xpath(self):
        try:
            events_display_dropdown_options_by_xpath = self.config.get("Notifier",
                                                                       "events_display_dropdown_options_by_xpath")
            print("events display dropdown options: ", events_display_dropdown_options_by_xpath)
            return events_display_dropdown_options_by_xpath
        except Exception as ex:
            print(ex)

    def get_photo_size_text_on_notifier_setting_panel_by_xpath(self):
        try:
            photo_size_text_on_notifier_setting_panel_by_xpath = \
                self.config.get("Notifier", "photo_size_text_on_notifier_setting_panel_by_xpath")
            print("Photo Size text: ", photo_size_text_on_notifier_setting_panel_by_xpath)
            return photo_size_text_on_notifier_setting_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_photo_size(self):
        try:
            expected_text_photo_size = self.common_test_data_config.get("Notifier_Data", "expected_text_photo_size")
            print("expected text: ", expected_text_photo_size)
            return expected_text_photo_size
        except Exception as ex:
            print(ex)

    def get_photo_size_dropdown_by_xpath(self):
        try:
            photo_size_dropdown_by_xpath = self.config.get("Notifier", "photo_size_dropdown_by_xpath")
            print("Photo Size dropdown: ", photo_size_dropdown_by_xpath)
            return photo_size_dropdown_by_xpath
        except Exception as ex:
            print(ex)

    def get_photo_size_dropdown_options_by_xpath(self):
        try:
            photo_size_dropdown_options_by_xpath = self.config.get("Notifier", "photo_size_dropdown_options_by_xpath")
            print("Photo Size dropdown options: ", photo_size_dropdown_options_by_xpath)
            return photo_size_dropdown_options_by_xpath
        except Exception as ex:
            print(ex)

    def get_sound_option_text_on_notifier_setting_panel_by_xpath(self):
        try:
            sound_option_text_on_notifier_setting_panel_by_xpath = \
                self.config.get("Notifier", "sound_option_text_on_notifier_setting_panel_by_xpath")
            print("Sound Option text: ", sound_option_text_on_notifier_setting_panel_by_xpath)
            return sound_option_text_on_notifier_setting_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_sound_option(self):
        try:
            expected_text_sound_option = self.common_test_data_config.get("Notifier_Data", "expected_text_sound_option")
            print("expected text: ", expected_text_sound_option)
            return expected_text_sound_option
        except Exception as ex:
            print(ex)

    def get_sound_option_dropdown_by_xpath(self):
        try:
            sound_option_dropdown_by_xpath = self.config.get("Notifier", "sound_option_dropdown_by_xpath")
            print("Sound Option dropdown: ", sound_option_dropdown_by_xpath)
            return sound_option_dropdown_by_xpath
        except Exception as ex:
            print(ex)

    def get_sound_option_dropdown_options_by_xpath(self):
        try:
            sound_option_dropdown_options_by_xpath = self.config.get("Notifier",
                                                                     "sound_option_dropdown_options_by_xpath")
            print("Sound Option dropdown options: ", sound_option_dropdown_options_by_xpath)
            return sound_option_dropdown_options_by_xpath
        except Exception as ex:
            print(ex)

    def get_message_to_user_for_region_selection_by_xpath(self):
        try:
            message_to_user_for_region_selection_by_xpath = self.config.get(
                "Notifier", "message_to_user_for_region_selection_by_xpath")
            print("Message to user On Region selection: ", message_to_user_for_region_selection_by_xpath)
            return message_to_user_for_region_selection_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_message_to_user_for_region_selection(self):
        try:
            expected_message_to_user_for_region_selection = self.common_test_data_config.get(
                "Notifier_Data", "expected_message_to_user_for_region_selection")
            print("expected message on Region selection: ", expected_message_to_user_for_region_selection)
            return expected_message_to_user_for_region_selection
        except Exception as ex:
            print(ex)

    def get_message_to_user_for_group_selection_by_xpath(self):
        try:
            message_to_user_for_group_selection_by_xpath = self.config.get(
                "Notifier", "message_to_user_for_group_selection_by_xpath")
            print("Message to user on Group selection: ", message_to_user_for_group_selection_by_xpath)
            return message_to_user_for_group_selection_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_message_to_user_for_group_selection(self):
        try:
            expected_message_to_user_for_group_selection = self.common_test_data_config.get(
                "Notifier_Data", "expected_message_to_user_for_group_selection")
            print("expected message on Group selection: ", expected_message_to_user_for_group_selection)
            return expected_message_to_user_for_group_selection
        except Exception as ex:
            print(ex)

    def get_radio_button_for_group_by_xpath_1(self):
        try:
            radio_button_for_group_by_xpath_1 = self.config.get("Notifier", "radio_button_for_group_by_xpath_1")
            print("radio button for group selected part 1: ", radio_button_for_group_by_xpath_1)
            return radio_button_for_group_by_xpath_1
        except Exception as ex:
            print(ex)

    def get_radio_button_for_group_by_xpath_2(self):
        try:
            radio_button_for_group_by_xpath_2 = self.config.get("Notifier", "radio_button_for_group_by_xpath_2")
            print("radio button for group selected part 2: ", radio_button_for_group_by_xpath_2)
            return radio_button_for_group_by_xpath_2
        except Exception as ex:
            print(ex)

    def get_collapse_button_on_event_info_by_xpath(self):
        try:
            collapse_button_on_event_info_by_xpath = self.config.get("Notifier",
                                                                     "collapse_button_on_event_info_by_xpath")
            print("Collapse button: ", collapse_button_on_event_info_by_xpath)
            return collapse_button_on_event_info_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_COLLAPSE_button(self):
        try:
            expected_text_on_COLLAPSE_button = self.common_test_data_config.get("Notifier_Data", "expected_text_on_COLLAPSE_button")
            print("expected text on COLLAPSE button: ", expected_text_on_COLLAPSE_button)
            return expected_text_on_COLLAPSE_button
        except Exception as ex:
            print(ex)

    def get_close_notifier_button_on_event_info_by_xpath(self):
        try:
            close_notifier_button_on_event_info_by_xpath = self.config.get(
                "Notifier", "close_notifier_button_on_event_info_by_xpath")
            print("'Close Notifier' button on event info: ", close_notifier_button_on_event_info_by_xpath)
            return close_notifier_button_on_event_info_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_close_notifier_button_on_event_info(self):
        try:
            expected_text_on_close_notifier_button_on_event_info = \
                self.common_test_data_config.get("Notifier_Data", "expected_text_on_close_notifier_button_on_event_info")
            print("expected text on 'Close Notifier' button: ", expected_text_on_close_notifier_button_on_event_info)
            return expected_text_on_close_notifier_button_on_event_info
        except Exception as ex:
            print(ex)

    def get_expand_button_on_event_info_by_xpath(self):
        try:
            expand_button_on_event_info_by_xpath = self.config.get("Notifier", "expand_button_on_event_info_by_xpath")
            print("'+EXPAND' button on event info: ", expand_button_on_event_info_by_xpath)
            return expand_button_on_event_info_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_text_on_expand_button(self):
        try:
            expected_text_on_expand_button = self.common_test_data_config.get("Notifier_Data", "expected_text_on_expand_button")
            print("Expected text on EXPAND button: ", expected_text_on_expand_button)
            return expected_text_on_expand_button
        except Exception as ex:
            print(ex)

    def get_close_group_selected_visible_on_notifier_panel_by_xpath(self):
        try:
            close_group_selected_visible_on_notifier_panel_by_xpath = \
                self.config.get("Notifier", "close_group_selected_visible_on_notifier_panel_by_xpath")
            print("Close group selected: ", close_group_selected_visible_on_notifier_panel_by_xpath)
            return close_group_selected_visible_on_notifier_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_enrollment_view_panel_by_xpath(self):
        try:
            enrollment_view_panel_by_xpath = self.config.get("Notifier", "enrollment_view_panel_by_xpath")
            print("Enrollment-View panel: ", enrollment_view_panel_by_xpath)
            return enrollment_view_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_events_panel_by_xpath(self):
        try:
            events_panel_by_xpath = self.config.get("Notifier", "events_panel_by_xpath")
            print("Events panel: ", events_panel_by_xpath)
            return events_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_number_of_events_displayed_by_xpath(self):
        try:
            number_of_events_displayed_by_xpath = self.config.get("Notifier", "number_of_events_displayed_by_xpath")
            print("Number of events displayed: ", number_of_events_displayed_by_xpath)
            return number_of_events_displayed_by_xpath
        except Exception as ex:
            print(ex)

    def get_live_image_text_by_xpath(self):
        try:
            live_image_text_by_xpath = self.config.get("Notifier", "live_image_text_by_xpath")
            print("LIVE IMAGE text: ", live_image_text_by_xpath)
            return live_image_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_possible_match_text_by_xpath(self):
        try:
            possible_match_text_by_xpath = self.config.get("Notifier", "possible_match_text_by_xpath")
            print("Possible Match text: ", possible_match_text_by_xpath)
            return possible_match_text_by_xpath
        except Exception as ex:
            print(ex)

    def get_expected_live_image_text(self):
        try:
            expected_live_image_text = self.common_test_data_config.get("Notifier_Data", "expected_live_image_text")
            print("expected live image text: ", expected_live_image_text)
            return expected_live_image_text
        except Exception as ex:
            print(ex)

    def get_expected_text_possible_match(self):
        try:
            expected_text_possible_match = self.common_test_data_config.get("Notifier_Data", "expected_text_possible_match")
            print("expected possible match text: ", expected_text_possible_match)
            return expected_text_possible_match
        except Exception as ex:
            print(ex)

    def get_alert_completion_time_on_notifier_panel_by_xpath(self):
        try:
            alert_completion_time_on_notifier_panel_by_xpath = \
                self.config.get("Notifier", "alert_completion_time_on_notifier_panel_by_xpath")
            print("Alert completion time: ", alert_completion_time_on_notifier_panel_by_xpath)
            return alert_completion_time_on_notifier_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_notifier_alert_real_time_on_notifier_panel_by_xpath(self):
        try:
            notifier_alert_real_time_on_notifier_panel_by_xpath = \
                self.config.get("Notifier", "notifier_alert_real_time_on_notifier_panel_by_xpath")
            print("Notifier alert real time: ", notifier_alert_real_time_on_notifier_panel_by_xpath)
            return notifier_alert_real_time_on_notifier_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_alert_completion_time_on_events_panel_by_xpath(self):
        try:
            alert_completion_time_on_events_panel_by_xpath = \
                self.config.get("Notifier", "alert_completion_time_on_events_panel_by_xpath")
            print("Alert completion time on events panel: ", alert_completion_time_on_events_panel_by_xpath)
            return alert_completion_time_on_events_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_notifier_alert_real_time_on_events_panel_by_xpath(self):
        try:
            notifier_alert_real_time_on_events_panel_by_xpath = \
                self.config.get("Notifier", "notifier_alert_real_time_on_events_panel_by_xpath")
            print("Notifier alert real time on events panel: ", notifier_alert_real_time_on_events_panel_by_xpath)
            return notifier_alert_real_time_on_events_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_station_name_on_events_panel_by_xpath(self):
        try:
            station_name_on_events_panel_by_xpath = self.config.get("Notifier", "station_name_on_events_panel_by_xpath")
            print("Station name on events panel: ", station_name_on_events_panel_by_xpath)
            return station_name_on_events_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_updating_text_on_notifier_panel_by_xpath(self):
        try:
            updating_text_on_notifier_panel_by_xpath = self.config.get("Notifier",
                                                                       "updating_text_on_notifier_panel_by_xpath")
            print("'UPDATING' text on notifier panel: ", updating_text_on_notifier_panel_by_xpath)
            return updating_text_on_notifier_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_group_name_on_event_panel_by_xpath(self):
        try:
            group_name_on_event_panel_by_xpath = self.config.get("Notifier", "group_name_on_event_panel_by_xpath")
            print("Group name on events panel: ", group_name_on_event_panel_by_xpath)
            return group_name_on_event_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_enrollments_group_button_on_enrollments_view_panel_by_xpath(self):
        try:
            enrollments_group_button_on_enrollments_view_panel_by_xpath = \
                self.config.get("Notifier", "enrollments_group_button_on_enrollments_view_panel_by_xpath")
            print("Enrollments Group button: ", enrollments_group_button_on_enrollments_view_panel_by_xpath)
            return enrollments_group_button_on_enrollments_view_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_enrollment_group_name_on_enrollment_groups_panel_by_xpath(self):
        try:
            enrollment_group_name_on_enrollment_groups_panel_by_xpath = \
                self.config.get("Notifier", "enrollment_group_name_on_enrollment_groups_panel_by_xpath")
            print("Enrollment group name on Enrollment Groups panel: ",
                  enrollment_group_name_on_enrollment_groups_panel_by_xpath)
            return enrollment_group_name_on_enrollment_groups_panel_by_xpath
        except Exception as ex:
            print(ex)

    def get_close_panel_buttons_by_xpath(self):
        try:
            close_panel_buttons_by_xpath = self.config.get("Notifier", "close_panel_buttons_by_xpath")
            print("Close all panels: ", close_panel_buttons_by_xpath)
            return close_panel_buttons_by_xpath
        except Exception as ex:
            print(ex)

    def get_photo_size_on_event_info_by_xpath(self):
        try:
            photo_size_on_event_info_by_xpath = self.config.get("Notifier", "photo_size_on_event_info_by_xpath")
            print("actual photo size on event info: ", photo_size_on_event_info_by_xpath)
            return photo_size_on_event_info_by_xpath
        except Exception as ex:
            print(ex)

    def get_abe_enrollment_group(self):
        try:
            get_abe_enrollment_group = self.common_test_data_config.get("Notifier_Data", "abe_enrollment_group")
            print("get_abe_enrollment_group: ", get_abe_enrollment_group)
            return get_abe_enrollment_group
        except Exception as ex:
            print(ex)

    def get_vipe_enrollment_group(self):
        try:
            get_vipe_enrollment_group = self.common_test_data_config.get("Notifier_Data", "vipe_enrollment_group")
            print("get_vipe_enrollment_group: ", get_vipe_enrollment_group)
            return get_vipe_enrollment_group
        except Exception as ex:
            print(ex)

    def get_soe_enrollment_group(self):
        try:
            get_soe_enrollment_group = self.common_test_data_config.get("Notifier_Data", "soe_enrollment_group")
            print("get_soe_enrollment_group: ", get_soe_enrollment_group)
            return get_soe_enrollment_group
        except Exception as ex:
            print(ex)

    def get_pte_enrollment_group(self):
        try:
            get_pte_enrollment_group = self.common_test_data_config.get("Notifier_Data", "pte_enrollment_group")
            print("get_pte_enrollment_group: ", get_pte_enrollment_group)
            return get_pte_enrollment_group
        except Exception as ex:
            print(ex)

    def get_fraude_enrollment_group(self):
        try:
            get_fraude_enrollment_group = self.common_test_data_config.get("Notifier_Data", "fraude_enrollment_group")
            print("get_fraude_enrollment_group: ", get_fraude_enrollment_group)
            return get_fraude_enrollment_group
        except Exception as ex:
            print(ex)

    def get_camera0(self):
        try:
            get_camera0 = self.common_test_data_config.get("Notifier_Data", "camera0")
            print("get_camera0: ", get_camera0)
            return get_camera0
        except Exception as ex:
            print(ex)

    def get_camera1(self):
        try:
            get_camera1 = self.common_test_data_config.get("Notifier_Data", "camera1")
            print("get_camera1: ", get_camera1)
            return get_camera1
        except Exception as ex:
            print(ex)

    def get_auto_Refresh_Off(self):
        try:
            auto_Refresh_Off = self.common_test_data_config.get("Notifier_Data", "auto_Refresh_Off")
            print("auto_Refresh_Off: ", auto_Refresh_Off)
            return auto_Refresh_Off
        except Exception as ex:
            print(ex)

    def get_refresh_Rate_5_minutes(self):
        try:
            refresh_Rate_5_minutes = self.common_test_data_config.get("Notifier_Data", "refresh_Rate_5_minutes")
            print("refresh_Rate_5_minutes: ", refresh_Rate_5_minutes)
            return refresh_Rate_5_minutes
        except Exception as ex:
            print(ex)

    def get_refresh_Rate_4_minutes(self):
        try:
            refresh_Rate_4_minutes = self.common_test_data_config.get("Notifier_Data", "refresh_Rate_4_minutes")
            print("refresh_Rate_4_minutes: ", refresh_Rate_4_minutes)
            return refresh_Rate_4_minutes
        except Exception as ex:
            print(ex)

    def get_refresh_Rate_3_minutes(self):
        try:
            refresh_Rate_3_minutes = self.common_test_data_config.get("Notifier_Data", "refresh_Rate_3_minutes")
            print("refresh_Rate_3_minutes: ", refresh_Rate_3_minutes)
            return refresh_Rate_3_minutes
        except Exception as ex:
            print(ex)

    def get_refresh_Rate_2_minutes(self):
        try:
            refresh_Rate_2_minutes = self.common_test_data_config.get("Notifier_Data", "refresh_Rate_2_minutes")
            print("refresh_Rate_2_minutes: ", refresh_Rate_2_minutes)
            return refresh_Rate_2_minutes
        except Exception as ex:
            print(ex)

    def get_refresh_Rate_1_minutes(self):
        try:
            refresh_Rate_1_minutes = self.common_test_data_config.get("Notifier_Data", "refresh_Rate_1_minutes")
            print("refresh_Rate_1_minutes: ", refresh_Rate_1_minutes)
            return refresh_Rate_1_minutes
        except Exception as ex:
            print(ex)

    def get_refresh_Rate_30_seconds(self):
        try:
            refresh_Rate_30_seconds = self.common_test_data_config.get("Notifier_Data", "refresh_Rate_30_seconds")
            print("refresh_Rate_30_seconds: ", refresh_Rate_30_seconds)
            return refresh_Rate_30_seconds
        except Exception as ex:
            print(ex)

    def get_refresh_Rate_10_seconds(self):
        try:
            refresh_Rate_10_seconds = self.common_test_data_config.get("Notifier_Data", "refresh_Rate_10_seconds")
            print("refresh_Rate_10_seconds: ", refresh_Rate_10_seconds)
            return refresh_Rate_10_seconds
        except Exception as ex:
            print(ex)

    def get_refresh_Rate_5_seconds(self):
        try:
            refresh_Rate_5_seconds = self.common_test_data_config.get("Notifier_Data", "refresh_Rate_5_seconds")
            print("refresh_Rate_5_seconds: ", refresh_Rate_5_seconds)
            return refresh_Rate_5_seconds
        except Exception as ex:
            print(ex)

    def get_refresh_Rate_1_seconds(self):
        try:
            refresh_Rate_1_seconds = self.common_test_data_config.get("Notifier_Data", "refresh_Rate_1_seconds")
            print("refresh_Rate_1_seconds: ", refresh_Rate_1_seconds)
            return refresh_Rate_1_seconds
        except Exception as ex:
            print(ex)

    def get_events_Displayed_1(self):
        try:
            events_Displayed_1 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_1")
            print("events_Displayed_1: ", events_Displayed_1)
            return events_Displayed_1
        except Exception as ex:
            print(ex)

    def get_events_Displayed_2(self):
        try:
            events_Displayed_2 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_2")
            print("events_Displayed_2: ", events_Displayed_2)
            return events_Displayed_2
        except Exception as ex:
            print(ex)

    def get_events_Displayed_3(self):
        try:
            events_Displayed_3 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_3")
            print("events_Displayed_3: ", events_Displayed_3)
            return events_Displayed_3
        except Exception as ex:
            print(ex)

    def get_events_Displayed_4(self):
        try:
            events_Displayed_4 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_4")
            print("events_Displayed_4: ", events_Displayed_4)
            return events_Displayed_4
        except Exception as ex:
            print(ex)

    def get_events_Displayed_5(self):
        try:
            events_Displayed_5 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_5")
            print("events_Displayed_5: ", events_Displayed_5)
            return events_Displayed_5
        except Exception as ex:
            print(ex)

    def get_events_Displayed_6(self):
        try:
            events_Displayed_6 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_6")
            print("events_Displayed_6: ", events_Displayed_6)
            return events_Displayed_6
        except Exception as ex:
            print(ex)

    def get_events_Displayed_7(self):
        try:
            events_Displayed_7 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_7")
            print("events_Displayed_7: ", events_Displayed_7)
            return events_Displayed_7
        except Exception as ex:
            print(ex)

    def get_events_Displayed_8(self):
        try:
            events_Displayed_8 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_8")
            print("events_Displayed_8: ", events_Displayed_8)
            return events_Displayed_8
        except Exception as ex:
            print(ex)

    def get_events_Displayed_9(self):
        try:
            events_Displayed_9 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_9")
            print("events_Displayed_9: ", events_Displayed_9)
            return events_Displayed_9
        except Exception as ex:
            print(ex)

    def get_events_Displayed_10(self):
        try:
            events_Displayed_10 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_10")
            print("events_Displayed_10: ", events_Displayed_10)
            return events_Displayed_10
        except Exception as ex:
            print(ex)

    def get_events_Displayed_11(self):
        try:
            events_Displayed_11 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_11")
            print("events_Displayed_11: ", events_Displayed_11)
            return events_Displayed_11
        except Exception as ex:
            print(ex)

    def get_events_Displayed_12(self):
        try:
            events_Displayed_12 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_12")
            print("events_Displayed_12: ", events_Displayed_12)
            return events_Displayed_12
        except Exception as ex:
            print(ex)

    def get_events_Displayed_13(self):
        try:
            events_Displayed_13 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_13")
            print("events_Displayed_13: ", events_Displayed_13)
            return events_Displayed_13
        except Exception as ex:
            print(ex)

    def get_events_Displayed_14(self):
        try:
            events_Displayed_14 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_14")
            print("events_Displayed_14: ", events_Displayed_14)
            return events_Displayed_14
        except Exception as ex:
            print(ex)

    def get_events_Displayed_15(self):
        try:
            events_Displayed_15 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_15")
            print("events_Displayed_15: ", events_Displayed_15)
            return events_Displayed_15
        except Exception as ex:
            print(ex)

    def get_events_Displayed_16(self):
        try:
            events_Displayed_16 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_16")
            print("events_Displayed_16: ", events_Displayed_16)
            return events_Displayed_16
        except Exception as ex:
            print(ex)

    def get_events_Displayed_17(self):
        try:
            events_Displayed_17 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_17")
            print("events_Displayed_17: ", events_Displayed_17)
            return events_Displayed_17
        except Exception as ex:
            print(ex)

    def get_events_Displayed_18(self):
        try:
            events_Displayed_18 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_18")
            print("get_camera1: ", events_Displayed_18)
            return events_Displayed_18
        except Exception as ex:
            print(ex)

    def get_events_Displayed_19(self):
        try:
            events_Displayed_19 = self.common_test_data_config.get("Notifier_Data", "events_Displayed_19")
            print("events_Displayed_19: ", events_Displayed_19)
            return events_Displayed_19
        except Exception as ex:
            print(ex)

    def get_events_Displayed_20(self):
        try:
            vents_Displayed_20 = self.common_test_data_config.get("Notifier_Data", "vents_Displayed_20")
            print("vents_Displayed_20: ", vents_Displayed_20)
            return vents_Displayed_20
        except Exception as ex:
            print(ex)

    def get_photo_Size_X_Small(self):
        try:
            photo_Size_X_Small = self.common_test_data_config.get("Notifier_Data", "photo_Size_X_Small")
            print("photo_Size_X_Small: ", photo_Size_X_Small)
            return photo_Size_X_Small
        except Exception as ex:
            print(ex)

    def get_photo_Size_Small(self):
        try:
            photo_Size_Small = self.common_test_data_config.get("Notifier_Data", "photo_Size_Small")
            print("photo_Size_Small: ", photo_Size_Small)
            return photo_Size_Small
        except Exception as ex:
            print(ex)

    def get_photo_Size_Medium(self):
        try:
            photo_Size_Medium = self.common_test_data_config.get("Notifier_Data", "photo_Size_Medium")
            print("photo_Size_Medium: ", photo_Size_Medium)
            return photo_Size_Medium
        except Exception as ex:
            print(ex)

    def get_photo_Size_Large(self):
        try:
            photo_Size_Large = self.common_test_data_config.get("Notifier_Data", "photo_Size_Large")
            print("photo_Size_Large: ", photo_Size_Large)
            return photo_Size_Large
        except Exception as ex:
            print(ex)

    def get_photo_Size_X_Large(self):
        try:
            photo_Size_X_Large = self.common_test_data_config.get("Notifier_Data", "photo_Size_X_Large")
            print("photo_Size_X_Large: ", photo_Size_X_Large)
            return photo_Size_X_Large
        except Exception as ex:
            print(ex)

    def get_photo_Size_XX_Large(self):
        try:
            photo_Size_XX_Large = self.common_test_data_config.get("Notifier_Data", "photo_Size_XX_Large")
            print("photo_Size_XX_Large: ", photo_Size_XX_Large)
            return photo_Size_XX_Large
        except Exception as ex:
            print(ex)

    def get_sound_Option_OFF(self):
        try:
            sound_Option_OFF = self.common_test_data_config.get("Notifier_Data", "sound_Option_OFF")
            print("sound_Option_OFF: ", sound_Option_OFF)
            return sound_Option_OFF
        except Exception as ex:
            print(ex)

    def get_sound_Option_ON(self):
        try:
            sound_Option_ON = self.common_test_data_config.get("Notifier_Data", "sound_Option_ON")
            print("sound_Option_ON: ", sound_Option_ON)
            return sound_Option_ON
        except Exception as ex:
            print(ex)

    def get_region_name(self):
        try:
            region_name = self.common_test_data_config.get("Notifier_Data", "region_name")
            print("region_name: ", region_name)
            return region_name
        except Exception as ex:
            print(ex)

    def get_Location_Name(self):
        try:
            Location_name = self.config.get("data_validation", "Location_name")
            return Location_name
        except Exception as ex:
            print(ex.args)

    def get_location_data(self):
        try:
            location_data = self.config.get("data_validation", "location_data")
            return location_data
        except Exception as ex:
            print(ex.args)

    def get_station_camera_name(self):
        try:
            get_station_camera_name = self.config.get("data_validation", "camera_name")
            return get_station_camera_name
        except Exception as ex:
            print(ex.args)

    def get_station_camera_data(self):
        try:
            get_station_camera_data = self.config.get("data_validation", "camera_data")
            return get_station_camera_data
        except Exception as ex:
            print(ex.args)

    def get_case_subject(self):
        try:
            case_subject = self.config.get("data_validation", "case_subject")
            return case_subject
        except Exception as ex:
            print(ex.args)

    def get_Action(self):
        try:
            Action = self.config.get("data_validation", "Action")
            return Action
        except Exception as ex:
            print(ex.args)

    def get_Action_data(self):
        try:
            Action_data = self.config.get("data_validation", "Action_data")
            return Action_data
        except Exception as ex:
            print(ex.args)

    def get_Index(self):
        try:
            Index = self.config.get("data_validation", "Index")
            return Index
        except Exception as ex:
            print(ex.args)

    def get_Index_data(self):
        try:
            get_Index_data = self.config.get("data_validation", "Index_data")
            return get_Index_data
        except Exception as ex:
            print(ex.args)

    def get_enrollment_number(self):
        try:
            enrollment_number = self.config.get("data_validation", "enrollment_number")
            return enrollment_number
        except Exception as ex:
            print(ex.args)

    def get_enrollment_number_data(self):
        try:
            enrollment_number_data = self.config.get("data_validation", "enrollment_number_data")
            return enrollment_number_data
        except Exception as ex:
            print(ex.args)
