import configparser
from pathlib import Path


class events_Read_Ini:
    def __init__(self):
        try:
            self.file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\10_Events_Module\\Data_From_INI\\Events_module.ini"
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.config = configparser.RawConfigParser()
            print("ini file path: ",  self.file_path)
            self.config.read(self.file_path)
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
            print(ex)

    def get_Launching_url(self):
        url = self.common_test_data_config.get("Login_Logout_Data", "cloud_login_url")
        print("launching web portal login page",  url)
        return url

    def get_expecting_title_webportal_login(self):
        expected_title = self.common_test_data_config.get("Login_Logout_Data", "portal_title")
        print("expected title of web portal login page",  expected_title)
        return expected_title
    
    def get_logo_is_visible_on_login_page(self):
        logo = self.config.get("login_locators", "logo_image_by_xpath")
        print("logo of web portal login page",  logo)
        return logo
    
    def get_username_textbox(self):
        username = self.config.get("login_locators", "username_textbox_by_xpath")
        print("username texbox",  username)
        return username

    def get_password_textbox(self):
        password = self.config.get("login_locators", "password_textbox_by_xpath")
        print("password textbox",  password)
        return password

    def get_cloudlogin_button(self):
        cloud_menu = self.config.get("login_locators", "cloudlogin_button_by_xpath")
        print("cloud menu button",  cloud_menu)
        return cloud_menu

    def get_valid_username(self):
        valid_username = self.common_test_data_config.get("Login_Logout_Data", "username")
        print("valid username is",  valid_username)
        return valid_username
    
    def get_valid_password(self):
        valid_password = self.common_test_data_config.get("Login_Logout_Data", "password")
        print("valid password is",  valid_password)
        return valid_password
    
    def get_username_after_successfull_login(self):
        afterlogin_username = self.config.get("login_locators", "after_successful_login_username_is_visible")
        print("after successfully login username is displayed on footer section", afterlogin_username)
        return afterlogin_username

    def get_cloud_menu(self):
        cloud_menu = self.config.get("login_locators", "cloud_menu")
        print("cloud menu is displayed",  cloud_menu)
        return cloud_menu

    def get_logout(self):
        logout = self.config.get("login_locators", "logout")
        print("logout is", logout)
        return logout
    
    def get_Events_in_dashboard(self):
        events = self.config.get("events_locators", "events_in_dashboard")
        print("events is ", events)
        return events
    
    def get_events_panel_heading(self):
        events_panel = self.config.get("events_locators", "events_panel_heading")
        print("events panel heading is ", events_panel)
        return events_panel

    def view_dropdown(self):
        try:
            view_dropdown = self.config.get("events_locators", "view_dropdown")
            print("view dropdown is ", view_dropdown)
            return view_dropdown
        except Exception as ex:
            print(ex)
            
    def view_dropdown_options(self):
        try:
            dropdown_options = self.config.get("events_locators", "view_dropdown_options")
            print("view dropdown options are", dropdown_options)
            return dropdown_options
        except Exception as ex:
            print(ex)
            
    def location_in_view_dropdown(self):
        try:
            location = self.config.get("events_locators", "location_in_viewdropdown")
            print("location in view dropdown ", location)
            return location
        except Exception as ex:
            print(ex)

    def select_checkbox_by_xpath(self):
        try:
            checkbox = self.config.get("events_locators", "check_box_by_xpath")
            print("selecting checkbox", checkbox)
            return checkbox
        except Exception as ex:
            print(ex)

    def events_location_panel(self):
        try:
            events_location = self.config.get("events_locators", "Events_location_panel")
            print("events location panel", events_location)
            return events_location
        except Exception as ex:
            print(ex)
            
    def event_page_cross_symbol(self):
        try:
            cross_symbol = self.config.get("events_locators", "cross_symbol_by_xpath")
            print("cross symbol visible on events page", cross_symbol)
            return cross_symbol
        except Exception as ex:
            print(ex)

    def search_filter_by_action_textbox(self):
        try:
            textbox = self.config.get("events_locators", "filter_search_by_action_textbox")
            print("search filter textbox is ", textbox)
            return textbox
        except Exception as ex:
            print(ex)

    def Enter_a_action_text(self):
        try:
            text = self.common_test_data_config.get("Events_Data",  "action_text")
            print("enter a action text ",  text)
            return text
        except Exception as ex:
            print(ex)

    def total_number_of_events_happened_out_of_total_number_of_events(self):
        try:
            text = self.config.get("events_locators", "displaying_text")
            print("number of events happened out of total events", text)
            return text
        except Exception as ex:
            print(ex)

    def get_number_of_text(self):
        try:
            twenty_text = self.config.get("events_locators", "number_of_events_displaying_text")
            print("getting 20 text is ", twenty_text)
            return twenty_text
        except Exception as ex:
            print(ex)
            
    def read_of_text(self):
        try:
            of_text = self.common_test_data_config.get("Events_Data",  "of_text")
            print("of text is ",  of_text)
            return of_text
        except Exception as ex:
            print(ex)

    def get_total_number_of_events(self):
        try:
            total_events = self.config.get("events_locators",  "total_number_of_events_displayed")
            print("total number of events ",  total_events)
            return total_events
        except Exception as ex:
            print(ex)
            
    def read_events_text(self):
        try:
            events = self.common_test_data_config.get("Events_Data",  "events_text")
            print("events text is ",  events)
            return events
        except Exception as ex:
            print(ex)

    def remove_filter_button(self):
        try:
            remove_filter = self.config.get("events_locators", "remove_filter_button")
            print("remove filter button", remove_filter)
            return remove_filter
        except Exception as ex:
            print(ex)
            
    def search_dropdown_in_events(self):
        try:
            search = self.config.get("events_locators",  "search_dropdown_in_events")
            print("search dropdown is ",  search)
            return search
        except Exception as ex:
            print(ex)
            
    def action_dropdown_in_events(self):
        try:

            action = self.config.get("events_locators", "Action_dropdown_in_events")
            print("action dropdown is ", action)
            return action
        except Exception as ex:
            print(ex)

    def select_all_checkbox(self):
        try:
            select_all = self.config.get("events_locators", "select_all_checkbox")
            print("select all checkbox in events", select_all)
            return select_all
        except Exception as ex:
            print(ex)

    def select_all_text(self):
        try:
            select_all_text = self.config.get("events_locators", "select_all_text")
            print("select all text is ", select_all_text)
            return select_all_text
        except Exception as ex:
            print(ex)

    def real_time_event_happened(self):
        try:
            event_happened_time = self.config.get("events_locators", "real_time_event_happened")
            print("real time of event happened", event_happened_time)
            return event_happened_time
        except Exception as ex:
            print(ex)
            
    def location_casesubject_of_an_event(self):
        try:
            location_subject = self.config.get("events_locators", "location_case_subject_text_in_eventspage")
            print("location subject of an event ", location_subject)
            return location_subject
        except Exception as ex:
            print(ex)
            
    def indexscore_of_event(self):
        try:
            indexscore = self.config.get("events_locators",  "indexscore_ofan_event_in_eventspage")
            print("indexscore of an event ",  indexscore)
            return indexscore
        except Exception as ex:
            print(ex)
            
    def actiontaken_by_an_event(self):
        try:
            action = self.config.get("events_locators",  "action_takenby_anevent_in_eventspage")
            print("action taken by an event",  action)
            return action
        except Exception as ex:
            print(ex)

    def region_ofan_event(self):
        try:
            region = self.config.get("events_locators",  "region_ofan_event_in_eventspage")
            print("region of an event",  region)
            return region
        except Exception as ex:
            print(ex)
            
    def live_image_text(self):
        try:
            live_image = self.config.get("events_locators", "Live_image_text")
            print("live image text is ", live_image)
            return live_image
        except Exception as ex:
            print(ex)
            
    def live_image(self):
        try:
            live_image = self.config.get("events_locators", "Live_image")
            print("live image is ", live_image)
            return live_image
        except Exception as ex:
            print(ex)
            
    def file_image_text(self):
        try:
            file_image = self.config.get("events_locators", "file_image_text")
            print("file image is ", file_image)
            return file_image
        except Exception as ex:
            print(ex)
            
    def file_image(self):
        try:
            file_image = self.config.get("events_locators", "file_image")
            print("file image text is ", file_image)
            return file_image
        except Exception as ex:
            print(ex)

    def events_button(self):
        try:
            events = self.config.get("events_locators", "event_button_in_eventspage")
            print("events button is ", events)
            return events
        except Exception as ex:
            print(ex)
            
    def events_button_symbol(self):
        try:
            events_symbol = self.config.get("events_locators", "event_button_symbol_in_eventspage")
            print("events_symbol is ", events_symbol)
            return events_symbol
        except Exception as ex:
            print(ex)

    def tags_button_in_eventspage(self):
        try:

            tags_button = self.config.get("events_locators", "tags_button_in_events_page")
            print("tags button in events page", tags_button)
            return tags_button
        except Exception as ex:
            print(ex)
            
    def tags_button_symbol(self):
        try:
            tags_symbol = self.config.get("events_locators", "tags_symbol_in_events_page")
            print("tags button symbol is ", tags_symbol)
            return tags_symbol
        except Exception as ex:
            print(ex)
            
    def extent_menu(self):
        try:
            extent_menu = self.config.get("events_locators", "extent_menu_in_eventspage")
            print("extent menu in events page", extent_menu)
            return extent_menu
        except Exception as ex:
            print(ex)
            
    def extent_menu_symbol(self):
        try:
            extent_menu_symbol = self.config.get("events_locators", "extent_menu_symbol")
            print("extent_menu symbol is ", extent_menu_symbol)
            return extent_menu_symbol
        except Exception as ex:
            print(ex)

    def loadmore_button(self):
        try:
            loadmore = self.config.get("events_locators", "loadmore_button")
            print("load more button is", loadmore)
            return loadmore
        except Exception as ex:
            print(ex)
            
    def Enter_a_text_findlocation(self):
        try:
            findlocation_text = self.common_test_data_config.get("events_locators",  "Enter_a_text_in_findlocation")
            print(" entering a text in findloaction textbox ",  findlocation_text)
            return findlocation_text
        except Exception as ex:
            print(ex)
            
    def facefirst_logo_on_map(self):
        try:
            facefirstlogo = self.config.get("events_locators", "facefirst_logo_on_map")
            print("facfirst logo is visible in map", facefirstlogo)
            return facefirstlogo
        except Exception as ex:
            print(ex)
            
    def live_image_on_map(self):
        try:
            live_image = self.config.get("events_locators", "live_image_on_map")
            print("live image on map", live_image)
            return live_image
        except Exception as ex:
            print(ex)
            
    def file_image_on_map(self):
        try:
            file_image = self.config.get("events_locators", "file_image_on_map")
            print("file image on map is", file_image)
            return file_image
        except Exception as ex:
            print(ex)
            
    def after_clicking_togglesymbol_map_xpath(self):
        try:
            map_1 = self.config.get("events_locators", "after_clicking_togglesymbol_map_xpath")
            print("after clicking map is visible", map_1)
            return map_1
        except Exception as ex:
            print(ex)
            
    def display_tags_in_eventspage(self):
        try:
            display_tags = self.config.get("events_locators", "Displaytags_in_eventspage")
            print("display tags are visible in view dropdown", display_tags)
            return display_tags
        except Exception as ex:
            print(ex)

    def on_map_number_of_events_visible(self):
        try:
            number_of_events = self.config.get("events_locators", "on_map_number_of_events_visible")
            print("number of events visible on map for a perticular location", number_of_events)
            return number_of_events
        except Exception as ex:
            print(ex)
            
    def tags_display_below_the_events(self):
        try:
            tags_below_events = self.config.get("events_locators", "tags_visible_below_the_event")
            print("tags displayed below the events", tags_below_events)
            return tags_below_events
        except Exception as ex:
            print(ex)
            
    def date_and_time_range_in_searchdropdown(self):
        try:
            date_and_time = self.config.get("events_locators", "Date_time_range")
            print("date and time range box in search dropdown", date_and_time)
            return date_and_time
        except Exception as ex:
            print(ex)
            
    def date_and_time_range_to_in_searchdropdown(self):
        try:
            date_and_time_to = self.config.get("events_locators", "Date_time_range_to")
            print("date and time range to textbox", date_and_time_to)
            return date_and_time_to
        except Exception as ex:
            print(ex)
            
    def enrollment_group_selection(self):
        try:
            enrollment_group_selection = self.config.get("events_locators", "Enrollment_Group_selection")
            print("enrollment group selection", enrollment_group_selection)
            return enrollment_group_selection
        except Exception as ex:
            print(ex)
            
    def org_hierarchy_selection(self):
        try:
            org_hierarchy = self.config.get("events_locators", "org_hierarchy_selection")
            print("org/hierarchy selection button in search dropdown", org_hierarchy)
            return org_hierarchy
        except Exception as ex:
            print(ex)
            
    def tag_selection(self):
        try:
            tag_selection = self.config.get("events_locators", "tag_selection")
            print("tag selection button in search dropdown ", tag_selection)
            return tag_selection
        except Exception as ex:
            print(ex)

    def sort_by_dropdown_in_searchdropdown(self):
        try:
            sort_by_dropdown = self.config.get("events_locators", "sort_by_dropdown_in_searchdropdown")
            print("sort by dropdown in search dropdown is", sort_by_dropdown)
            return sort_by_dropdown
        except Exception as ex:
            print(ex)
            
    def sort_by_atoz_radiobutton(self):
        try:
            sort_by_atoz = self.config.get("events_locators", "sort_by_ato_z_radiobutton")
            print("sort by atoz radio button is", sort_by_atoz)
            return sort_by_atoz
        except Exception as ex:
            print(ex)
            
    def sort_by_ztoa_radiobutton(self):
        try:
            sort_by_ztoa = self.config.get("events_locators", "sort_by_ztoa_radiobutton")
            print("sort by ztoa radio button", sort_by_ztoa)
            return sort_by_ztoa
        except Exception as ex:
            print(ex)
            
    def clear_button_in_searchdropdown(self):
        try:
            clear = self.config.get("events_locators", "clear_button_in_searchdropdown")
            print("clear button is visible", clear)
            return clear
        except Exception as ex:
            print(ex)
            
    def location_search_button_in_searchdropdown(self):
        try:
            location_search = self.config.get("events_locators", "location_serach_button")
            print("location search button in searchdropdown", location_search)
            return location_search
        except Exception as ex:
            print(ex)
            
    def search_button_in_searchdropdown(self):
        try:
            search = self.config.get("events_locators", "search_button_searchdropdown")
            print("search button in search dropdown", search)
            return search
        except Exception as ex:
            print(ex)
            
    def action_dropdown_options(self):
        try:
            actions_dropdown_options = self.config.get("events_locators", "action_dropdown_options")
            print("action dropdown options", actions_dropdown_options)
            return actions_dropdown_options
        except Exception as ex:
            print(ex)
            
    def edit_tags_in_actiondropdown(self):
        try:
            edit_tags = self.config.get("events_locators", "Edit/tags_option_in_actiondropdown")
            print("edit tags option in action dropdown", edit_tags)
            return edit_tags
        except Exception as ex:
            print(ex)
            
    def events_tags_panel_heading(self):
        try:
            events_tags_panel_heading = self.config.get("events_locators", "events_tags_panel_heading")
            print("events tags panel heading is visible", events_tags_panel_heading)
            return events_tags_panel_heading
        except Exception as ex:
            print(ex)
            
    def filter_dropdown_in_events_tag(self):
        try:
            filter_dropdown = self.config.get("events_locators", "filter_dropdown_in_events_tags")
            print("filter dropdown in events tags panel", filter_dropdown)
            return filter_dropdown
        except Exception as ex:
            print(ex)
            
    def filter_dropdown_options(self):
        try:
            filter_dropdown = self.config.get("events_locators", "filter_dropdown_options")
            print("filter dropdown options are", filter_dropdown)
            return filter_dropdown
        except Exception as ex:
            print(ex)
            
    def linked_tags_by_xpath(self):
        try:
            linked_tags = self.config.get("events_locators", "linked_tags_by_xpath")
            print("linked tags in filter dropdown", linked_tags)
            return linked_tags
        except Exception as ex:
            print(ex)
            
    def tags_banner(self):
        try:
            linked_tags_banner = self.config.get("events_locators", "linked_tags_banner")
            print("linked tags banner is visible", linked_tags_banner)
            return linked_tags_banner
        except Exception as ex:
            print(ex)
            
    def tags_names(self):
        try:
            linked_tags = self.config.get("events_locators", "tags_names")
            print("linked tags options are", linked_tags)
            return linked_tags
        except Exception as ex:
            print(ex)
            
    def unlinked_tags_by_xpath(self):
        try:
            unlinked_tags = self.config.get("events_locators", "unlinked_tags_by_xpath")
            print("unlinked tags are", unlinked_tags)
            return unlinked_tags
        except Exception as ex:
            print(ex)
            
    def filter_tags_name_textbox(self):
        try:
            filter_tags_name = self.config.get("events_locators", "filter_tags_by_name_textbox")
            print("events_tags by name ", filter_tags_name)
            return filter_tags_name
        except Exception as ex:
            print(ex)

    def cancle_btn_on_add_details_panel_by_xpath(self):
        cancle_btn_on_add_details_panel_by_xpath = self.config.get("events_locators", "cancle_btn_on_add_details_panel_by_xpath")
        return cancle_btn_on_add_details_panel_by_xpath

    def cancel_button_in_warning_add_details(self):
        cancel_button_in_warning_add_details = self.config.get("events_locators", "cancel_button_in_warning_add_details")
        return cancel_button_in_warning_add_details

    def enter_a_text_in_filter_tagname_texbox(self):
        try:
            text = self.common_test_data_config.get("Events_Data",  "text1")
            print("enter a text in filter texbox",  text)
            return text
        except Exception as ex:
            print(ex)
            
    def tag_details_button(self):
        try:
            tag_details_button = self.config.get("events_locators", "tag_details_button")
            print("tag details button is visible for each tag", tag_details_button)
            return tag_details_button
        except Exception as ex:
            print(ex)
            
    def tag_details_panel_heading(self):
        try:
            tagdetails_panel = self.config.get("events_locators", "tag-details_button_panel")
            print("tag details panel heading is", tagdetails_panel)
            return tagdetails_panel
        except Exception as ex:
            print(ex)
            
    def action_dropdown_in_events_tag(self):
        try:
            action_dropdown = self.config.get("events_locators", "Action_dropdown_in_eventstag")
            print("action dropdown in events tag panel", action_dropdown)
            return action_dropdown
        except Exception as ex:
            print(ex)
            
    def add_tags_to_event_option_in_event_tags(self):
        try:
            add_tags = self.config.get("events_locators", "add_tags_to_event_option")
            print("add tags to an event", add_tags)
            return add_tags
        except Exception as ex:
            print(ex)
            
    def checkbox_number_twentyfour(self):
        try:
            checkbox = self.config.get("events_locators", "checkbox_number_twentyfour")
            print("checkbox number is ", checkbox)
            return checkbox
        except Exception as ex:
            print(ex)
            
    def remove_tags_to_event_in_eventstag(self):
        try:
            remove = self.config.get("events_locators", "remove_tags_o_event")
            print("remove tags to an event", remove)
            return remove
        except Exception as ex:
            print(ex)
            
    def first_checkbox_in_events(self):
        try:
            checkbox = self.config.get("events_locators", "checkbox_one")
            print("check box one in events page is ", checkbox)
            return checkbox
        except Exception as ex:
            print(ex)
            
    def threat_tagname_visible_in_firstevent(self):
        try:
            tagname = self.config.get("events_locators", "threat_tags_name_in_eventspage")
            print("threat tagname in events page", tagname)
            return tagname
        except Exception as ex:
            print(ex)
            
    def tagnames_below_to_an_event(self):
        try:
            tag_names = self.config.get("events_locators", "tagnames_below_the_event")
            print("tag_names are", tag_names)
            return tag_names
        except Exception as ex:
            print(ex)
            
    def refresh_option_in_eventtags(self):
        try:
            refresh_option = self.config.get("events_locators", "refresh_option")
            print("refresh option in action dropdown", refresh_option)
            return refresh_option
        except Exception as ex:
            print(ex)
            
    def updating_text(self):
        try:
            updating_text = self.config.get("events_locators", "updating_text_in_events_tag")
            print("updating text is ", updating_text)
            return updating_text
        except Exception as ex:
            print(ex)

    def refresh_option_in_action_dropdown_on_events_page(self):
        try:
            refresh = self.config.get("events_locators", "refresh_option_in_action_dropdown_on_EV")
            print("refresh option in events page", refresh)
            return refresh
        except Exception as ex:
            print(ex)
            
    def updating_text_in_event(self):
        try:
            updating = self.config.get("events_locators", "updating_text_in_event")
            print("updating text in events page after clicking refresh", updating)
            return updating
        except Exception as ex:
            print(ex)
            
    def change_panel_refresh_in_action_dropdown(self):
        try:
            change_panel = self.config.get("events_locators", "changepanel_refreshrate_option_in_actiondropdown")
            print("change panel refresh rate", change_panel)
            return change_panel
        except Exception as ex:
            print(ex)
            
    def change_panel_refresh_dialouge_box(self):
        try:
            change_panel = self.config.get("events_locators", "change_panel_refreshrate_text_by_xpath")
            print("change panel refresh rate", change_panel)
            return change_panel
        except Exception as ex:
            print(ex)
            
    def change_panel_refresh_rate_text(self):
        try:
            change_panel_refresh_text = self.config.get("events_locators", "change_panel_refreshrate_text")
            print("change panel refresh rate panel", change_panel_refresh_text)
            return change_panel_refresh_text
        except Exception as ex:
            print(ex)
            
    def change_panel_refresh_dropdown(self):
        try:
            dropdown = self.config.get("events_locators", "change_panel_refresh_dropdown")
            print("change panel refresh dropdown is", dropdown)
            return dropdown
        except Exception as ex:
            print(ex)
            
    def minutes_selected_change_panelrate_refresh(self):
        try:
            change_panel = self.config.get("events_locators", "minutes_selected_text_changepanel")
            print("no of minutes selected in change refresh panel", change_panel)
            return change_panel
        except Exception as ex:
            print(ex)
            
    def cancel_button_in_change_panel_rate(self):
        try:
            cancel = self.config.get("events_locators", "cancel_button_in_change_panel_refresh_rate")
            print("cancel button in change panel refresh dialougebox", cancel)
            return cancel
        except Exception as ex:
            print(ex)
            
    def print_option_in_actiondropdown(self):
        try:
            print_option = self.config.get("events_locators", "print_option_in_action_dropdown")
            print("print option in action dropdown", print_option)
            return print_option
        except Exception as ex:
            print(ex)
            
    def print_button_after_clicking_print(self):
        try:
            print_button = self.config.get("events_locators", "print_button_after_clicking_print")
            print("print button is visible", print_button)
            return print_button
        except Exception as ex:
            print(ex)
            
    def cancel_button_after_clicking_print(self):
        try:
            cancel_button = self.config.get("events_locators", "cancel_button_after_clicking_print")
            print("cancel button is visible", cancel_button)
            return cancel_button
        except Exception as ex:
            print(ex)
            
    def event_view_panel_heading(self):
        try:
            event_view = self.config.get("events_locators", "Event_view_panel_heading")
            print("event view panel is visible", event_view)
            return event_view
        except Exception as ex:
            print(ex)
            
    def enrollment_view_panel_heading(self):
        try:
            enrollment_view = self.config.get("events_locators", "Enrollment_view_panel_heading")
            print("enrollment view panel is visible", enrollment_view)
            return enrollment_view
        except Exception as ex:
            print(ex)
            
    def action_dropdown_in_event_view(self):
        try:
            action_dropdown = self.config.get("events_locators", "action_dropdown_in_event_view")
            print("action dropdown in event view", action_dropdown)
            return action_dropdown
        except Exception as ex:
            print(ex)
            
    def identify_within_enrollments(self):
        try:
            identify_within_enrollments = self.config.get("events_locators", "Identify_within_enrollments_in_eventview")
            print("identify with in enrollments", identify_within_enrollments)
            return identify_within_enrollments
        except Exception as ex:
            print(ex)
            
    def identify_and_enroll_panel(self):
        try:
            identify_enroll = self.config.get("events_locators", "identify_enroll_panel")
            print("identify and enroll panel is ", identify_enroll)
            return identify_enroll
        except Exception as ex:
            print(ex)

    def identify_results_panel(self):
        try:
            identify_results = self.config.get("events_locators", "identify_results_panel")
            print("identify results panel is ", identify_results)
            return identify_results
        except Exception as ex:
            print(ex)
            
    def identify_within_visitors_option_in_eventview(self):
        try:
            identify_within_visitors = self.config.get("events_locators", "identify_within_visitors")
            print("identify with in visitors", identify_within_visitors)
            return identify_within_visitors
        except Exception as ex:
            print(ex)

    def visitor_search_panel(self):
        try:
            visitor_search = self.config.get("events_locators", "visitor_search_panel")
            print("visitor search panel is", visitor_search)
            return visitor_search
        except Exception as ex:
            print(ex)
            
    def print_option_in_eventview_actiondropdon(self):
        try:
            print_option = self.config.get("events_locators", "print_option_eventview_actiondropdown")
            print("print option in event view dropdown", print_option)
            return print_option
        except Exception as ex:
            print(ex)

    def videobutton_in_eventview(self):
        try:
            video = self.config.get("events_locators", "videobutton_in_eventview")
            print("video button in event view", video)
            return video
        except Exception as ex:
            print(ex)
            
    def video_details_panel(self):
        try:
            video = self.config.get("events_locators", "videodetails_panel")
            print("video details panel is ", video)
            return video
        except Exception as ex:
            print(ex)
            
    def tagbutton_in_event_view(self):
        try:
            tag = self.config.get("events_locators", "tag_button")
            print("tag button in event view panel", tag)
            return tag
        except Exception as ex:
            print(ex)
            
    def action_dropdown_in_enrollmentview(self):
        try:
            enrollment = self.config.get("events_locators", "action__dropdown_in_enrollmentview")
            print("in enrollment view panel action dropdown", enrollment)
            return enrollment
        except Exception as ex:
            print(ex)
            
    def identify_within_enrollments_in_enrollmentview(self):
        try:
            identify_enrollment = self.config.get("events_locators", "identify_within_enrollments_enrollmentview")
            print("identify with in enrollment in enrollment view", identify_enrollment)
            return identify_enrollment
        except Exception as ex:
            print(ex)
            
    def identify_within_visitors_in_enrollmentview(self):
        try:
            identify_within_in_visitors = self.config.get("events_locators", "identity_within_visitors_in_enrollmentview")
            print("identify within visitors option in enrollment view", identify_within_in_visitors)
            return identify_within_in_visitors
        except Exception as ex:
            print(ex)
            
    def edit_view_enrollment_option_in_actiondropdown(self):
        try:
            edit_view = self.config.get("events_locators", "view_and_editdetails_option_in_enrollmentview")
            print("edit/view details option in action dropdown", edit_view)
            return edit_view
        except Exception as ex:
            print(ex)

    def enrollment_details_panel(self):
        try:
            enrollemnt_details = self.config.get("events_locators", "Enrollment_details_panel")
            print("enrollment details panel is", enrollemnt_details)
            return enrollemnt_details
        except Exception as ex:
            print(ex)
            
    def disabled_enrollment_in_enrollmentview(self):
        try:
            disabled_enrollment = self.config.get("events_locators", "Disable_enrollment_in_enrollmentview")
            print("disabled enrollment enrollment", disabled_enrollment)
            return disabled_enrollment
        except Exception as ex:
            print(ex)

    def disabled_text_in_enrollmentview_page(self):
        try:
            disabled_text = self.config.get("events_locators", "Diabled_text_is_visible_in_enrollmentview")
            print("disabled text in enrollemnt view page", disabled_text)
            return disabled_text
        except Exception as ex:
            print(ex)

    def permenantly_delete_enrollment_option_in_enrollment(self):
        try:
            permenantly_delete_enrollment = self.config.get("events_locators", "permenantly_delete_an_enrollment_option")
            print("permenantly delete enrollment option", permenantly_delete_enrollment)
            return permenantly_delete_enrollment
        except Exception as ex:
            print(ex)
            
    def warning_dialouge_box(self):
        try:
            warning = self.config.get("events_locators", "warning_dialouge_box")
            print("warning dialouge box is visible", warning)
            return warning
        except Exception as ex:
            print(ex)
            
    def cancel_button_in_warning_dialouge_box(self):
        try:
            cancel_button = self.config.get("events_locators", "cancel_button_in_warning")
            print("cancel button is ", cancel_button)
            return cancel_button
        except Exception as ex:
            print(ex)

    def yes_delecte_selected_event_and_their_events_button_on_warning_dialougebox(self):
        try:
            yes_delete_button = self.config.get("events_locators", "yes_delete_selected_enrollment_and_their_events_button")
            print("yes delete selected enrollment and and their button ", yes_delete_button)
            return yes_delete_button
        except Exception as ex:
            print(ex)

    def enrollment_details_button_in_enrollment_view_panel(self):
        try:
            enrollment_details = self.config.get("events_locators", "Enrollment_details_button_in_enrollmentview_panel")
            print("enrollments details button in enrollment view panel is", enrollment_details)
            return enrollment_details
        except Exception as ex:
            print(ex)
            
    def faces_button_in_enrollmentview(self):
        try:
            faces = self.config.get("events_locators", "faces_button_enrollmentview")
            print("faces button in enrollment view", faces)
            return faces
        except Exception as ex:
            print(ex)
            
    def Enrollment_Faces_panel(self):
        try:
            enrollment_faces = self.config.get("events_locators", "Enrollment_Faces_panel")
            print("enrollment faces panel heading", enrollment_faces)
            return enrollment_faces
        except Exception as ex:
            print(ex)
            
    def events_button_enrollment_view(self):
        try:
            events_button = self.config.get("events_locators", "Events_button_in_enrollment_view")
            print("events button in enrollment view", events_button)
            return events_button
        except Exception as ex:
            print(ex)

    def events_panel_heading_after_clicking_events_button_in_enrollmentview(self):
        try:
            events_panel = self.config.get("events_locators", "Events_panel_heading_after_clicking_eventsbutton")
            print("events view panel is visible after clicking event button in enrollment view", events_panel)
            return events_panel
        except Exception as ex:
            print(ex)
            
    def enrollment_groups_button_in_enrollmentview(self):
        try:
            enrollment_group = self.config.get("events_locators", "Enrollments_groups")
            print("enrollment group is visible ", enrollment_group)
            return enrollment_group
        except Exception as ex:
            print(ex)

    def enrollment_group_panel(self):
        try:
            enrollment_group = self.config.get("events_locators", "Enrollment_group_panel")
            print("enrollment group panel is visible", enrollment_group)
            return enrollment_group
        except Exception as ex:
            print(ex)

    def notes_button_in_enrollmentview(self):
        try:
            notes_button = self.config.get("events_locators", "notes_button")
            print("notes button is visible in enrollment view", notes_button)
            return notes_button
        except Exception as ex:
            print(ex)

    def notes_panel(self):
        try:
            notes_panel = self.config.get("events_locators", "notes_panel")
            print("notes panel is", notes_panel)
            return notes_panel
        except Exception as ex:
            print(ex)
            
    def location_button_in_events_page(self):
        try:
            location = self.config.get("events_locators", "location_button_in_extentmenu_on_eventpage")
            print("location button in extent menu on eventspage", location)
            return location
        except Exception as ex:
            print(ex)
            
    def video_button_in_events_page(self):
        try:
            video = self.config.get("events_locators", "video_button_in_extentmenu_on_eventpage")
            print("video button in extent menu on eventspage", video)
            return video
        except Exception as ex:
            print(ex)
            
    def video_in_event_video_panel(self):
        try:
            video = self.config.get("events_locators", "video_in_event_view")
            print("video in event view panel", video)
            return video
        except Exception as ex:
            print(ex)

    def get_find_location_textbox_in_notes_location(self):
        find_location_textbox = self.config.get("events_locators", "find_location_text_box_in_notes_Location")
        print("find location textbox in location page", find_location_textbox)
        return find_location_textbox

    def get_drawcircle_button(self):
        drawcircle = self.config.get("events_locators", "Drawcircle_button")
        print("drawcircle button is ", drawcircle)
        return drawcircle

    def get_search_area_button_on_notes_location(self):
        search_area_button = self.config.get("events_locators", "search_area_button_on_notes_location")
        print("searching location on map", search_area_button)
        return search_area_button

    def get_tribar_on_map(self):
        tribar = self.config.get("events_locators", "tribar")
        print("tribar on right side of map", tribar)
        return tribar

    def get_linktext_searchtarget_on_map(self):
        search_target = self.config.get("events_locators", "search_target")
        print("search target window is opened", search_target)
        return search_target

    def get_search_target_dropdown(self):
        search_target = self.config.get("events_locators", "search_target_dropdown")
        print("dropdown of search target", search_target)
        return search_target

    def get_location_panel_headings(self):
        events_location = self.config.get("events_locators", "panel_headings")
        print("events  notes heading ", events_location)
        return events_location

    def get_cancel_button(self):
         cancel_button = self.config.get("events_locators", "cancel_button_on_search_target")
         print("cancel button on selec search target", cancel_button)
         return cancel_button

    def get_toggle_full_screen_view(self):
        toggle_symbol = self.config.get("events_locators", "toggle_fullscreen_view")
        print("sqaure symbol is visible", toggle_symbol)
        return toggle_symbol

    def get_after_clicking_fullscreen_view(self):
        after_full_screen_view = self.config.get("events_locators", "after_clicking_toggle_fullscreen_view")
        print("after clicking full screen view", after_full_screen_view)
        return after_full_screen_view

    def get_zoom_in_on_map(self):
        zoom_in = self.config.get("events_locators", "zoom_in_on_map")
        print("performing zoom in on map", zoom_in)
        return zoom_in

    def get_zoom_out_(self):
        zoom_out = self.config.get("events_locators", "zoom_out_on_map")
        print("performing zoom out", zoom_out)
        return zoom_out

    def get_facefirst_logout_button(self):
        logout_button_webportal = self.config.get("events_locators", "facefirst_webportal_logout_by_xpath")
        print("logout button on webportal", logout_button_webportal)
        return logout_button_webportal

    def get_match_event_tags_filter_dropdown(self):
        match_event_tags_filter_dropdown = self.config.get("events_locators", "match_event_tags_filter_dropdown")
        print("match_event_tags_filter_dropdown", match_event_tags_filter_dropdown)
        return match_event_tags_filter_dropdown

    def get_match_event_tags_filter_unlink_tag(self):
        match_event_tags_filter_unlink_tag = self.config.get("events_locators", "match_event_tags_filter_unlink_tag")
        print("match_event_tags_filter_dropdown", match_event_tags_filter_unlink_tag)
        return match_event_tags_filter_unlink_tag

    def get_add_tags_to_alert(self):
        add_tags_to_alert = self.config.get("events_locators", "add_tags_to_alert")
        print("add_tags_to_alert", add_tags_to_alert)
        return add_tags_to_alert

    def regions_xpath(self):
        try:
            region_xpath = self.config.get("LOCATOR",  "region_xpath")
            print("region of an event",  region_xpath)
            return region_xpath
        except Exception as ex:
            print(ex)

    def region_checkbox_xpath(self):
        try:
            region_checkbox_xpath = self.config.get("LOCATOR", "region_checkbox_xpath")
            print("region of an event", region_checkbox_xpath)
            return region_checkbox_xpath
        except Exception as ex:
            print(ex)

    def edge_name(self):
        try:
            edge_name = self.common_test_data_config.get("common_data",  "zone_data_input")
            print("edge_name: ",  edge_name)
            return edge_name
        except Exception as ex:
            print(ex)

    def save_zone_button_by_xpath(self):
        save_zone_button_by_xpath = self.config.get("LOCATOR", "save_zone_button_by_xpath")
        return save_zone_button_by_xpath
