from Base_Package.Web_Logger import web_logger
from pathlib import Path
import configparser
from selenium.webdriver.common.by import By
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import Portal_Menu_Module_read_ini


class LoginLogout_Read_ini:

    def __init__(self):
        self.file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\0_Login_Logout_Data\\Data_From_INI\\login_logout.ini"
        print(f"INI Data File Path: {self.file_path}")
        self.config = configparser.RawConfigParser()
        self.config.read(self.file_path)
        common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
        self.common_test_data_config = configparser.RawConfigParser()
        self.common_test_data_config.read(common_test_data_ini_file_path)
        # self.local_url = self.config.get("login_urls", "local_login_url")
        # self.cloud_url = self.config.get("login_urls", "cloud_login_url")
        # print(f"local url: {self.local_url}")
        # print(f"cloud url: {self.cloud_url}")

    def get_portal_url(self):
        try:
            portal_url = self.common_test_data_config.get("Login_Logout_Data", "cloud_login_url")
            print("portal page url: ", portal_url)
            return portal_url
        except Exception as ex:
            print(ex)

    def get_portal_title(self):
        try:
            portal_title = self.common_test_data_config.get("Login_Logout_Data", "portal_title")
            print("portal title: ", portal_title)
            return portal_title
        except Exception as ex:
            print(ex)

    def get_password(self):
        password = self.config.get("user_info", "password")
        return password

    def get_username(self):
        username = self.config.get("user_info", "username")
        return username


    def get_advance_btn_by_xpath(self):
        try:
            advance_btn_by_xpath = self.common_test_data_config.get("Login_Logout_Data", "advance_btn_by_xpath")
            print("portal title: ", advance_btn_by_xpath)
            return advance_btn_by_xpath
        except Exception as ex:
            print(ex)

    def get_proceed_link_by_xpath(self):
        try:
            proceed_link_by_xpath = self.common_test_data_config.get("Login_Logout_Data", "proceed_link_by_xpath")
            print("portal title: ", proceed_link_by_xpath)
            return proceed_link_by_xpath
        except Exception as ex:
            print(ex)

    def operator_username(self):
        try:
            operator_username = self.common_test_data_config.get("users_to_login", "operator_username")
            print("operator_username: ", operator_username)
            return operator_username
        except Exception as ex:
            print(ex)

