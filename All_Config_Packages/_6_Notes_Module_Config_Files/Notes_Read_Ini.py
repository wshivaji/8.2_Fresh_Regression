import configparser
from pathlib import Path


class notes_Read_Ini:
    def __init__(self):
        try:
            self.file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\6_Notes_Module\\Data_From_ini\\Notes_module.ini"
            self.config=configparser.RawConfigParser()
            print("ini file path: ", self.file_path)
            self.config.read(self.file_path)
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
        except Exception as ex:
           print(ex)

    def get_Launching_url(self):
        url = self.common_test_data_config.get("Login_Logout_Data", "cloud_login_url")
        print("launching webportal login page", url)
        return url

    def get_expecting_title_webportal_login(self):
        expected_title = self.common_test_data_config.get("Login_Logout_Data", "portal_title")
        print("expected title of webportal login page", expected_title)
        return expected_title

    def get_logo_is_visible_on_login_page(self):
        logo = self.config.get("login_locators", "logo_image_by_xpath")
        print("logo of webportal login page", logo)
        return logo

    def get_username_textbox(self):
        username = self.config.get("login_locators", "username_textbox_by_xpath")
        print("username texbox", username)
        return username

    def get_password_textbox(self):
        password = self.config.get("login_locators", "password_textbox_by_xpath")
        print("password textbox", password)
        return password

    def get_cloudlogin_button(self):
        cloud_menu = self.config.get("login_locators", "cloudlogin_button_by_xpath")
        print("cloud menu button", cloud_menu)
        return cloud_menu

    def get_valid_username(self):
        valid_username = self.common_test_data_config.get("Login_Logout_Data", "username")
        print("valid username is", valid_username)
        return valid_username

    def get_valid_password(self):
        valid_password = self.common_test_data_config.get("Login_Logout_Data", "password")
        print("valid password is", valid_password)
        return valid_password

    def get_username_after_successfull_login(self):
        afterlogin_username = self.config.get("login_locators", "after_successful_login_username_is_visible")
        print("after successfull login username is displayed on footer section", afterlogin_username)
        return afterlogin_username

    def get_cloud_menu(self):
        cloud_menu=self.config.get("login_locators", "cloud_menu")
        print("cloud menu is displayed", cloud_menu)
        return cloud_menu

    def get_logout(self):
        logout=self.config.get("login_locators", "logout")
        print("logout is",logout)
        return logout

    def get_afterlogin_cloud_menu_is_visible(self):
        cloud_menu_after_login = self.config.get("notes_locators", "After_login_cloud_menu")
        print("after login cloud menu is visible", cloud_menu_after_login)
        return cloud_menu_after_login

    def get_notes_is_displayed(self):
        notes = self.config.get("notes_locators", "notes_by_xpath")
        print("notes is visible", notes)
        return notes

    def get_heading_of_notes_page(self):

        heading_notes = self.config.get("notes_locators", "Heading_of_notes_by_xpath")
        print("heading of notes page", heading_notes)
        return heading_notes

    def get_search_dropdown_on_notes_page(self):
        search_dropdown = self.config.get("notes_locators", "search-dropdown_on_notes_module")
        print("dropdown of search", search_dropdown)
        return search_dropdown

    def get_description_in_search_dropdown(self):
        description_in_searchdropdown = self.config.get("notes_locators", "Description_in_searchdropdown")
        print("description in search dropdown", description_in_searchdropdown)
        return description_in_searchdropdown

    def get_Location_store_in_Description(self):
        store_location_textbox = self.config.get("notes_locators", "Location/store_textbox_in_Description")
        print("location/store textbox in description", store_location_textbox)
        return store_location_textbox

    def enter_a_text_in_location_store(self):
        enter_a_text = self.common_test_data_config.get("common_data", "enter_a_text_in_location/store")
        print("enter a text in location/store", enter_a_text)
        return enter_a_text

    def get_case_subject_in_Description(self):
        case_subject_textbox = self.config.get("notes_locators", "case/subject_textbox_in_Description")
        print("case/subject textbox in description", case_subject_textbox)
        return case_subject_textbox

    def enter_a_text_in_Case_subject(self):
        enter_a_text = self.common_test_data_config.get("common_data", "enter_a_text_in_case/subject")
        print("enter a text in case/subject", enter_a_text)
        return enter_a_text

    def get_search_button_on_Description(self):
        search_button = self.config.get("notes_locators", "search_button_Description")
        print("search button on description", search_button)
        return search_button

    def get_clear_button_on_Description(self):
        clear_button = self.config.get("notes_locators", "clear_button_Description")
        print("clear button on description", clear_button)
        return  clear_button

    def get_sort_by_AtoZ_radiobutton_in_Description(self):
        sort_by_AtoZ_radiobutton = self.config.get("notes_locators", "sort_by_A-Z_radio_button")
        print("sortby atoz radiobutton", sort_by_AtoZ_radiobutton)
        return sort_by_AtoZ_radiobutton

    def get_sort_by_ZtoA_radiobutton_in_Description(self):
        sort_by_ZtoA_radiobutton = self.config.get("notes_locators", "sort_by_Z-A_radio_button")
        print("sortby ztoa radiobutton", sort_by_ZtoA_radiobutton)
        return sort_by_ZtoA_radiobutton

    def get_case_subject_in_sort_by_dropdown(self):
        case_subject_in_sortby=self.config.get("notes_locators", "case_subject_in_sort_by_dropdown")
        print("case subject in sortby dropdown", case_subject_in_sortby)
        return case_subject_in_sortby

    def get_search_criteria(self):
        search_criteria = self.config.get("notes_locators", "search_criteria")
        print("search criteria is displayed", search_criteria)
        return search_criteria

    def get_sort_by_dropdown(self):
        sort_by_dropdown = self.config.get("notes_locators", "sort_by_dropdown")
        print("sort by dropdown is", sort_by_dropdown)
        return sort_by_dropdown

    def get_sort_key_on_notes(self):
        sort_key = self.config.get("notes_locators", "sort_key_on_notes")
        print("sort key on notes", sort_key)
        return sort_key

    def get_location_store_in_search_criteria(self):
        location_store_name = self.config.get("notes_locators", "location_store_in_searchcriteria")
        print("location or store name in search criteria", location_store_name)
        return location_store_name

    def get_cross_symbol_on_searchcriteria(self):
        cross_symbol = self.config.get("notes_locators", "cross_symbol_on_searchcriteria")
        print("clicking on cross symbol", cross_symbol)
        return cross_symbol

    def get_location_in_searchdropdown(self):
        location = self.config.get("notes_locators", "Location_in_serachdropdown")
        print("location on search dropdown", location)
        return location

    def get_map_is_visible(self):
        map = self.config.get("notes_locators", "map")
        print("map is visible ", map)
        return map

    def get_heading_of_notes_location(self):
        heading_of_notes_location = self.config.get("notes_locators", "Heading_of_notes_location")
        print("heading of notes location is", heading_of_notes_location)
        return heading_of_notes_location

    def get_find_location_textbox_in_notes_location(self):
        find_location_textbox = self.config.get("notes_locators", "find_location_text_box_in_notes_Location")
        print("find location textbox in location page", find_location_textbox)
        return find_location_textbox

    def enter_text_on_find_location(self):
        find_location_text = self.common_test_data_config.get("common_data", "text_on_findlocation")
        print("text enter on find location", find_location_text)
        return find_location_text

    def get_search_area_button_on_notes_location(self):
        search_area_button = self.config.get("notes_locators", "search_area_button_on_notes_location")
        print("searching location on map", search_area_button)
        return search_area_button

    def get_marker_pointer(self):
        marker = self.config.get("notes_locators", "marker")
        print("image of marker is", marker)
        return marker

    def get_drawcircle_button(self):
        drawcircle = self.config.get("notes_locators", "Drawcircle_button")
        print("drawcircle button is ", drawcircle)
        return drawcircle

    def get_circledrawn_on_map(self):
        circle_drawn = self.config.get("notes_locators", "element_moved")
        print("for moving cursor on map", circle_drawn)
        return  circle_drawn

    def moving_paricular_location_on_map(self):
        location_on_map = self.config.get("notes_locators", "moving_paricular_location_on_map")
        print("on map going to location", location_on_map)
        return location_on_map

    def get_toggle_full_screen_view(self):
        toggle_symbol = self.config.get("notes_locators", "toggle_fullscreen_view")
        print("sqaure symbol is visible", toggle_symbol)
        return toggle_symbol

    def get_after_clicking_fullscreen_view(self):
        after_full_screen_view = self.config.get("notes_locators", "after_clicking_toggle_fullscreen_view")
        print("after clicking full screen view", after_full_screen_view)
        return after_full_screen_view

    def get_zoom_in_on_map(self):
        zoom_in = self.config.get("notes_locators", "zoom_in_on_map")
        print("performing zoom in on map", zoom_in)
        return zoom_in

    def get_plus_symbol(self):
        plus_symbol = self.config.get("notes_locators", "plus_symbol_on_map")
        print("clicking on plus symbol", plus_symbol)
        return plus_symbol

    def get_zoom_out_(self):
        zoom_out = self.config.get("notes_locators", "zoom_out_on_map")
        print("performing zoom out", zoom_out)
        return zoom_out

    def drag_pegman_by_xpath(self):
        pegman = self.config.get("notes_locators", "pegman_by_xpath")
        print("pegman is",pegman)
        return pegman

    def get_tribar_on_map(self):
        tribar = self.config.get("notes_locators", "tribar")
        print("tribar on right side of map", tribar)
        return tribar

    def get_linktext_searchtarget_on_map(self):
        search_target = self.config.get("notes_locators", "search_target")
        print("search target window is opened", search_target)
        return search_target

    def get_search_target_dropdown(self):
        search_target = self.config.get("notes_locators", "search_target_dropdown")
        print("dropdown of search target", search_target)
        return search_target

    def get_location_panel_headings(self):
        events_location = self.config.get("notes_locators", "panel_headings")
        print("events  notes heading ", events_location)
        return events_location

    def get_cancel_button(self):
         cancel_button = self.config.get("notes_locators", "cancel_button_on_search_target")
         print("cancel button on selec search target", cancel_button)
         return cancel_button

    def get_close_button(self):
        close_button = self.config.get("notes_locators", "close_button")
        print("close button ", close_button)
        return close_button

    def get_Events_location_whole_xpath(self):
        Events_location = self.config.get("notes_locators", "event-location_wholepage_xpath")
        print("Events_location page whole xpath", Events_location)
        return Events_location

    def get_Action_dropdown_on_notes_page(self):
        Action_dropdown = self.config.get("notes_locators", "Action_dropdown_on_notes")
        print("Action dropdoen is visible", Action_dropdown)
        return Action_dropdown

    def get_create_note_on_action_dropdown(self):
        create_note = self.config.get("notes_locators", "create_note")
        print("create note is visible on action dropdown", create_note)
        return create_note

    def create_note_panel_heading(self):
        create_note_heading = self.config.get("notes_locators", "create_note_panelheading")
        print("create_note panel heading is", create_note_heading)
        return create_note_heading

    def browse_a_image(self):
        browse_a_image = self.config.get("notes_locators", "select_a_image")
        print("selecting a image or browsing a image", browse_a_image)
        return browse_a_image

    def add_note_image_panel_heading(self):
        add_note_image = self.config.get("notes_locators", "note_add_image")
        print("add notes panel heading", add_note_image)
        return add_note_image

    def frame_in_createnote(self):
        frame_in_createnote = self.config.get("notes_locators", "frame_in_createnote")
        print("in create note frame", frame_in_createnote)
        return frame_in_createnote

    def Location_store_textbox_on_create_note(self):
        Location_store_textbox_on_createnote = self.config.get("notes_locators", "Location_textbox_in_createnote")
        print("textbox of location_store in create note", Location_store_textbox_on_createnote)
        return Location_store_textbox_on_createnote

    def Enter_text_in_Location_store_in_create_note(self):
        Enter_a_text_in_create_note = self.config.get("notes_locators", "Enter_Location_store_textbox_in_create_note")
        print("entering a text in location store", Enter_a_text_in_create_note)
        return Enter_a_text_in_create_note

    def case_subject_textbox_in_create_note(self):
        case_subject_in_createnote = self.config.get("notes_locators", "case_textbox_in_createnote")
        print("case subject texbox", case_subject_in_createnote)
        return case_subject_in_createnote

    def Enter_text_in_case_subject_in_create_note(self):
        Enter_text_in_case_subject = self.config.get("notes_locators", "Enter_case_subject_in_createnote")
        print("enter a text in case subject", Enter_text_in_case_subject)
        return Enter_text_in_case_subject

    def reported_loss_in_create_note(self):
        reported_loss = self.config.get("notes_locators", "reported_loss_in_createnote")
        print("reported loss in create note", reported_loss)
        return reported_loss

    def Enter_reported_loss(self):
        reported_loss = self.common_test_data_config.get("common_data", "Enter_reported_loss")
        print("reported loss is", reported_loss)
        return reported_loss

    def Date_of_incident(self):
        date_of_incident = self.config.get("notes_locators", "Date_of_incident")
        print("date of incident textbox", date_of_incident)
        return date_of_incident

    def date_time_of_incident(self):
        date_time = self.common_test_data_config.get("common_data", "date_and_time_of_incident")
        print("date and time of incident", date_time)
        return date_time

    def case_event_type(self):
        case_event_type = self.config.get("notes_locators", "case_Event_type")
        print("case event dropdown", case_event_type)
        return case_event_type

    def Employee_threatened_assaulted_option_in_dropdown(self):
        Employee_threat = self.config.get("notes_locators", "employee_threat_option_in_dropdown")
        print("store threat option in dropdown", Employee_threat)
        return Employee_threat

    def employee_threat_by_xpath(self):
        employee_threat_by_xpath = self.config.get("notes_locators", "employee_threat_in_case_Event")
        print("store threat option in dropdown,", employee_threat_by_xpath)
        return employee_threat_by_xpath

    def activity_type_dropdown(self):
        activity_type = self.config.get("notes_locators", "activity_type")
        print("activity type dropdown", activity_type)
        return activity_type

    def gift_card_option_in_activity_type(self):
        giftcard_in_dropdown = self.config.get("notes_locators", "Gift_card_fraud_option_in_activity_dropdown")
        print("option in activity dropdown", giftcard_in_dropdown)
        return giftcard_in_dropdown

    def gift_card_by_xpath(self):
        gift_card = self.config.get("notes_locators", "Gift_card_fraud_activity_type")
        print("gift card option by xpath", gift_card)
        return gift_card

    def method_of_offence(self):
        method_of_offence = self.config.get("notes_locators", "method_of_offence")
        print("method of offence dropdown",method_of_offence)
        return method_of_offence

    def concealment_option_in_dropdown(self):
        concealment_option = self.config.get("notes_locators", "concealment_option_in_dropdown")
        print("concealment in method of offence", concealment_option)
        return concealment_option

    def concealment_by_xpath(self):
        concealment_option_xpath = self.config.get("notes_locators", "concealment_by_xpath")
        print("concealment option xpath", concealment_option_xpath)
        return concealment_option_xpath

    def reported_by_textbox(self):
        reported_by = self.config.get("notes_locators", "reported_by_textbox")
        print("reported by textbox", reported_by)
        return reported_by

    def build_on_createnote(self):
        build = self.config.get("notes_locators", "build")
        print("build on create notes ", build)
        return build

    def Enter_a_test_in_build(self):
        entering_text = self.common_test_data_config.get("common_data", "Enter_text_on_build")
        print("entering a build text", entering_text)
        return entering_text

    def body_markings_textbox(self):
        body_markings = self.config.get("notes_locators", "bodymarkings")
        print("bodymarkings textbox", body_markings)
        return body_markings

    def Enter_a_text_on_bodymarkings(self):
        entering_text = self.config.get("notes_locators", "Enter_text_on_bodymarkings")
        print("entering a bodymarkings", entering_text)
        return entering_text

    def gender_dropdown(self):
        gender = self.config.get("notes_locators", "gender_dropdown")
        print("gender dropdown", gender)
        return gender

    def female_in_genderdropdown(self):
        female_option = self.config.get("notes_locators", "female_in_genderdropdown")
        print("female option in gender dropdown", female_option)
        return female_option

    def female_text_in_gender_dropdown(self):
        female_text = self.config.get("notes_locators", "female_option_in_genderdropdown")
        print("getting female text", female_text)
        return female_text

    def Height_dropdown(self):
        Height_dropdown = self.config.get("notes_locators", "Height_dropdown")
        print("height dropdown in create note", Height_dropdown)
        return Height_dropdown

    def Height_dropdown_text(self):
        Height_dropdown_text = self.common_test_data_config.get("common_data", "Height_dropdown_text")
        print("getting text of height dropdown", Height_dropdown_text)
        return Height_dropdown_text

    def Height_dropdown_options(self):
        Height_dropdown_option = self.config.get("notes_locators", "Height_dropdown_options")
        print("height dropdown options", Height_dropdown_option)
        return Height_dropdown_option

    def Narratives_textbox(self):
        Narratives_textbox = self.config.get("notes_locators", "Narratives_textbox")
        print("narratives on create note", Narratives_textbox)
        return Narratives_textbox

    def enter_text_in_narratives_textbox(self):
        enter_text = self.config.get("notes_locators", "Enter_text_on_narratives")
        print("entering text in narratives textbox", enter_text)
        return enter_text

    def action_textbox(self):
        action_textbox_in_createnote = self.config.get("notes_locators", "action_textbox")
        print("action textbox in createnote", action_textbox_in_createnote)
        return action_textbox_in_createnote

    def moving_mouse_into_map(self):
        move_to = self.config.get("notes_locators", "moving_to_element_to_map")
        print("moving to map", move_to)
        return move_to

    def facefirst_logo_on_map(self):
        facefirst_logo=self.config.get("notes_locators", "face_first_logo_visible_on_location")
        print("facefirstlogo is visible", facefirst_logo)
        return facefirst_logo

    def entering_text_in_action_textbox(self):
        Enter_text = self.common_test_data_config.get("common_data", "Enter_action")
        print("entering text in action textbox", Enter_text)
        return Enter_text

    def cancel_button_in_add_image(self):
        cancel_button = self.config.get("notes_locators", "cancel_button")
        print("cancel button is in add image page", cancel_button)
        return cancel_button

    def skip_cropping_button_in_add_image(self):
        skip_cropping = self.config.get("notes_locators", "skip_cropping")
        print("skip cropping button is in add image page", skip_cropping)
        return skip_cropping

    def crop_photo_button_in_add_image(self):
        crop_photo = self.config.get("notes_locators", "crop_photo")
        print("crop image button in add image page", crop_photo)
        return crop_photo

    def recrop_photo_button(self):
        recrop_photo = self.config.get("notes_locators", "re_crop_photo")
        print("recrop photo button ", recrop_photo)
        return recrop_photo

    def select_image_button(self):
        select_image = self.config.get("notes_locators", "select_image")
        print("selecting a image", select_image)
        return select_image

    def add_location_button(self):
        add_location = self.config.get("notes_locators", "add_location_button")
        print("add location button is visible", add_location)
        return add_location

    def save_button_in_createnote(self):
        save_button = self.config.get("notes_locators", "save_button")
        print("save button present on createnote", save_button)
        return save_button

    def cancel_button_in_createnote(self):
        cancel_button = self.config.get("notes_locators", "cancel_button_in_createnote")
        print("cancel button in create note", cancel_button)
        return cancel_button

    def delete_selected_notes(self):
        delete_selected_notes = self.config.get("notes_locators", "delete_selected_notes")
        print("delete selected notes", delete_selected_notes)
        return delete_selected_notes

    def refresh_in_action_dropdown(self):
        refresh = self.config.get("notes_locators", "refresh_in_action_dropdown")
        print("click on refresh", refresh)
        return refresh

    def change_panel_refresh(self):
        change_panel_refresh = self.config.get("notes_locators", "change_panel_refresh")
        print("change panel refresh rate", change_panel_refresh)
        return change_panel_refresh

    def change_refresh_panel_text(self):
        change_refresh_panel_text = self.config.get("notes_locators","change_refresh_panel_text")
        print("change refresh rate text",change_refresh_panel_text)
        return change_refresh_panel_text

    def auto_refresh_dropdown(self):
        auto_refresh_dropdown = self.config.get("notes_locators","auto_refresh_dropdown")
        print("auto refresh dropdown",auto_refresh_dropdown)
        return auto_refresh_dropdown

    def auto_refresh_option(self):
        auto_refresh_option = self.config.get("notes_locators","auto_refresh_option")
        print("auto refresh option",auto_refresh_option)
        return auto_refresh_option

    def auto_refresh_text(self):
        auto_refresh_text = self.common_test_data_config.get("common_data", "auto_refresh_text")
        print("getting auto refresh text", auto_refresh_text)
        return auto_refresh_text

    def cancel_button_in_change_refresh_dropdown(self):
        cancel_button_in_dropdown = self.config.get("notes_locators", "cancel_button_change_refresh_dropdown")
        print("cancel button in auto refresh dropdown", cancel_button_in_dropdown)
        return cancel_button_in_dropdown

    def delete_notes_checkbox(self):
        delete_notes_checkbox = self.config.get("notes_locators", "delete_notes_checkbox")
        print("delete note checkbox", delete_notes_checkbox)
        return delete_notes_checkbox

    def select_all_checkboxes_for_deleting_notes(self):
        select_all_checkboxes = self.config.get("notes_locators","select_all_checkboxes_for_deleting_notes")
        print("select all checkboxes",select_all_checkboxes)
        return select_all_checkboxes

    def gives_no_for_deleting_notes_text(self):
        selected_no = self.config.get("notes_locators","no_of_selected_for_deletion_text")
        print("gives number for deleting notes",selected_no)
        return selected_no

    def text_present_in_deleted_notes(self):
        text = self.common_test_data_config.get("common_data", "no_of_selected_notes_text")
        print("no gives delete seleted notes text", text)
        return text

    def yes_delete_selected_notes_button(self):
        button = self.config.get("notes_locators", "yes_delete_selected_button")
        print("yes delete selected notes button", button)
        return button

    def no_cancel_button_in_deleting_notes(self):
        no_cancel = self.config.get("notes_locators", "no,cancel_button")
        print("cancel button is displayed in deleting notes", no_cancel)
        return no_cancel

    def view_dropdown(self):
        view_dropdown=self.config.get("notes_locators","view_dropdown")
        print("view drop is visible",)
        return view_dropdown

    def location_in_view_dropdown(self):
        location_in_view_dropdown = self.config.get("notes_locators","location_in_view_dropdown")
        print("location_in_view_dropdown is",location_in_view_dropdown)
        return location_in_view_dropdown

    def location_symbol(self):
        location_symbol = self.config.get("notes_locators","location_symbol")
        print("location symbol is visible",location_symbol)
        return location_symbol

    def view_details_button(self):
        view_details=self.config.get("notes_locators","view_details_button")
        print("view details button",view_details)
        return view_details

    def notes_details_heading(self):
        notes_details_heading=self.config.get("notes_locators","notes_details_heading")
        print("heading of notes details",notes_details_heading)
        return notes_details_heading

    def tribar_in_notes(self):
        tribar_in_notes=self.config.get("notes_locators","three_horizantal_lines")
        print("three horizantal lines",tribar_in_notes)
        return tribar_in_notes

    def images_button(self):
        image_button=self.config.get("notes_locators","images_button")
        print("image button is visible",image_button)
        return image_button

    def enrollment_button(self):
        enrollment_button=self.config.get("notes_locators","enrollments_button")
        print("enrollment button is visible",enrollment_button)
        return enrollment_button

    def image_heading(self):
        image_heading=self.config.get("notes_locators","notes_image_heading")
        print("heading of notes images",image_heading)
        return image_heading

    def close_notes_panel(self):
        try:
            close_notes_panel=self.config.get("notes_locators","close_panel")
            print("closing notes page",close_notes_panel)
            return close_notes_panel
        except Exception as ex:
            print(ex)

    def select_search_dropdown_options(self):
        try:
            options=self.config.get("notes_locators","select_search_target_dropdown_options")
            print("select search target dropdown options",options)
            return options
        except Exception as ex:
            print(ex)

    def close_panels_one_by_one(self):
        try:
            close = self.config.get("notes_locators","close_panel_one_by_one")
            return close
        except Exception as ex:
            print(ex)

    def action_dropdown_in_notes_details_panel(self):
        try:
            action = self.config.get("notes_locators","action_dropdown_in_notes_details")
            return action
        except Exception as ex:
            print(ex)

    def Edit_note_option(self):
        try:
            edit = self.config.get("notes_locators","Edit_note_option")
            return edit
        except Exception as ex:
            print(ex)

    def save_button_on_notes_details(self):
        try:
            save = self.config.get("notes_locators","save_button_in_notes_details")
            return save
        except Exception as ex:
            print(ex)

    def create_notes_cancel_btn(self):
        try:
            save = self.config.get("notes_locators","create_notes_cancel_btn")
            return save
        except Exception as ex:
            print(ex)











#notes_Read_Ini().get_Launching_url()
#notes_Read_Ini().get_logo_is_visible_on_login_page()
#notes_Read_Ini().get_cloudmenu_textbox()
