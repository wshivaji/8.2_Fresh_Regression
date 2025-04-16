import configparser
from pathlib import Path


class detect_Faces_Read_Ini:
    def __init__(self):
        try:
            self.file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\8_Detect_Faces_Module\\Data_From_INI\\Detect_Faces_module.ini"
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            self.config = configparser.RawConfigParser()
            self.common_test_data_config = configparser.RawConfigParser()
            self.common_test_data_config.read(common_test_data_ini_file_path)
            print("ini file path: ", self.file_path)
            self.config.read(self.file_path)
        except Exception as ex:
            print(ex)

    def get_Launching_url(self):
        url = self.common_test_data_config.get("Login_Logout_Data", "cloud_login_url")
        print("launching web portal login page", url)
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
        cloud_menu = self.config.get("login_locators", "cloud_menu")
        print("cloud menu is displayed", cloud_menu)
        return cloud_menu

    def get_afterlogin_cloud_menu_is_visible(self):
        cloud_menu_after_login = self.config.get("Detect_faces_locators", "After_login_cloud_menu")
        print("after login cloud menu is visible", cloud_menu_after_login)
        return cloud_menu_after_login

    def detect_faces_in_dashboard(self):
        detect_faces = self.config.get("Detect_faces_locators", "detect_faces_in_dashboard")
        print("Detect Faces is visible in dashboard", detect_faces)
        return detect_faces

    def heading_of_detect_faces(self):
        heading_of_detect_faces = self.config.get("Detect_faces_locators", "detect_faces_panel_heading")
        print("heading of detect faces", heading_of_detect_faces)
        return heading_of_detect_faces

    def image_box(self):
        image_box = self.config.get("Detect_faces_locators", "image_box")
        print("image is selection ", image_box)
        return image_box

    def number_of_faces_detected_banner(self):
        banner_gives_no_of_faces = self.config.get("Detect_faces_locators", "number_of_faces_detected")
        print("banner gives number of faces detected", banner_gives_no_of_faces)
        return banner_gives_no_of_faces

    def number_of_faces_detected_text(self):
        number_of_faces_detected=self.common_test_data_config.get("Detect_Faces_module_Data", "number_of_faces_detected_text")
        print("number of faces detected gives text", number_of_faces_detected)
        return number_of_faces_detected

    def number_of_faces_deteced_in_a_imagebox(self):
        number_of_faces_detected=self.config.get("Detect_faces_locators", "number_of_faces_detected_in_image")
        print("number of faces in a imagebox", number_of_faces_detected)
        return number_of_faces_detected

    def reselect_button_in_detectfaces(self):
        reselect=self.config.get("Detect_faces_locators", "reselect_button")
        print("reselect button is visible in detectfaces", reselect)
        return reselect

    def question_mark_symbol(self):
        question_mark=self.config.get("Detect_faces_locators", "question_mark_symbol")
        print("question mark symbol is visile", question_mark)
        return question_mark

    def cross_symbol(self):
        cross_symbol=self.config.get("Detect_faces_locators", "cross_symbol_after_uploading_a_image")
        print("cross symbol is visible after uploading a image", cross_symbol)
        return cross_symbol

    def image_quality_page_panel(self):
        image_quality_panel = self.config.get("Detect_faces_locators", "Image_quqlity_page")
        print("image quality page after clicking questionmark symbol", image_quality_panel)
        return image_quality_panel

    def download_image_button(self):
        download_image=self.config.get("Detect_faces_locators", "download_button")
        print("download image button is visible in image quality page", download_image)
        return download_image

    def view_info_button_in_imagequality(self):
        view_info=self.config.get("Detect_faces_locators", "view_info")
        print("view detect faces button is visible", view_info)
        return view_info

    def Action_dropdown_in_image_quality(self):
        action=self.config.get("Detect_faces_locators", "action_dropdown")
        print("action dropdown in image quality ", action)
        return action

    def identify_within_enrollments(self):
        identify_within_enrollments=self.config.get("Detect_faces_locators", "Identify_with_in_enrollments")
        print("identify with in enrollments in action dropdown", identify_within_enrollments)
        return identify_within_enrollments

    def identify_enroll_heading_panel(self):
        identify_enroll=self.config.get("Detect_faces_locators", "Identify_enroll_heading_panel")
        print("identify and enroll details", identify_enroll)
        return identify_enroll

    def identify_with_in_visitors(self):
        identify_within_visitors=self.config.get("Detect_faces_locators", "Identify_within_visitors")
        print("identify with in visitors", identify_within_visitors)
        return identify_within_visitors

    def identification_results_panel_heading(self):
        identification_results_panel=self.config.get("Detect_faces_locators", "Identification_results_panel_heading")
        print("identification results panel heading", identification_results_panel)
        return identification_results_panel

    def faces_button_in_identification_results_page(self):
        faces_button=self.config.get("Detect_faces_locators", "Faces_button_in_identification_results")
        print("faces_button in identification page", faces_button)
        return faces_button

    def enroll_faces_panel_heading(self):
        enroll_faces=self.config.get("Detect_faces_locators", "Faces_button_in_identification_results")
        print("enroll faces page is opened", enroll_faces)
        return enroll_faces

    def person_view_button_in_identification_results(self):
        person_view=self.config.get("Detect_faces_locators", "person_view_button_in_identification_results")
        print("persons view button identify results", person_view)
        return person_view

    def enrollment_view_panel_heading(self):
        enrollment_view_panel_heading=self.config.get("Detect_faces_locators", "Enrollment_view")
        print("enrollment view page is opened", enrollment_view_panel_heading)
        return enrollment_view_panel_heading

    def purge_replace_button_in_identification_results(self):
        purge_replace=self.config.get("Detect_faces_locators", "purge_replace")
        print("purge and replace button in identify results", purge_replace)
        return purge_replace

    def enrollment_faces_panel_heading(self):
        enrollment_faces_panel_heading=self.config.get("Detect_faces_locators", "Enrollment_faces")
        print("enrollment faces panel heading", enrollment_faces_panel_heading)
        return enrollment_faces_panel_heading

    def visitor_serach_panel_heading(self):
        visitor_search_panel_heading=self.config.get("Detect_faces_locators", "visitor_search_panel")
        print("visitor search panel heading", visitor_search_panel_heading)
        return visitor_search_panel_heading

    def download_image_option_action_dropdown(self):
        download_image=self.config.get("Detect_faces_locators", "download_image")
        print("download image option is visible", download_image)
        return download_image

    def detect_faces_quality_check(self):
        try:
            quality_check=self.config.get("Detect_faces_locators", "detect_faces_quality_table")
            print("quality check in detect faces", quality_check)
            return quality_check
        except Exception as ex:
            print(ex)

    def image_quality_scan_result_heading_txt_by_xpath(self):
        try:
            image_quality_scan_result_heading_txt_by_xpath=self.config.get("Detect_faces_locators", "image_quality_scan_result_heading_txt_by_xpath")
            print("image_quality_scan_result_heading_txt_by_xpath", image_quality_scan_result_heading_txt_by_xpath)
            return image_quality_scan_result_heading_txt_by_xpath
        except Exception as ex:
            print(ex)

    def cross_symbol_on_identify_and_enroll_panel(self):
        try:
            cross_symbol=self.config.get("Detect_faces_locators", "cross_symbol_on_identify_and_enroll_panel")
            print("cross symbol on indentify and enroll page", cross_symbol)
            return cross_symbol
        except Exception as ex:
            print(ex)

    def close_panel_and_cancel_enrollment(self):
        try:

            close_panel = self.config.get("Detect_faces_locators", "close_panel_and_cancel_enrollment")
            print("close panel and cancel enrollment button", close_panel)
            return close_panel
        except Exception as ex:
            print(ex)






#detect_Faces_Read_Ini().get_afterlogin_cloud_menu_is_visible()