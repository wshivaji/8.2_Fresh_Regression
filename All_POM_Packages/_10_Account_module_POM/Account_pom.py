import time
from selenium.webdriver.common.by import By
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login, logout
from All_Config_Packages._10_Account_config_Files.Accounts_Read_INI import account_Read_Ini


class account_pom(web_driver, web_logger):

    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    '''
    def Launching_login_page(self):
        try:
            self.logger.info("*********TC_001******** started")
            self.d.get(account_Read_Ini().get_Launching_url())
            expected_url = account_Read_Ini().get_Launching_url()
            time.sleep(web_driver.one_second)
            self.d.maximize_window()
            actual_url = self.d.current_url
            print(f"actual: {actual_url},\nexpected: {expected_url}")
            if expected_url == actual_url:
               self.status.append(True)
            else:
                self.status.append(False)

            actual_title = self.d.title
            print("actual is", actual_title)
            expected_title = account_Read_Ini().get_expecting_title_webportal_login()
            print("expected title is", expected_title)
            if actual_title == expected_title:
               self.status.append(True)
            else:
               self.status.append(False)
            print(self.status)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
               self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_account_001.png")
               self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_001.png")
               return False
            else:
               return True
        except Exception as ex:
               self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_account_001.png")
               self.d.save_screenshot(f"{self.screenshots_path}\\Tc_account_001.png")
               self.logger.error(f"Tc_account_001 got exception as: {ex}")
               print(ex)

    def logo_username_texbox_password_textbox_is_visible(self):
        try:
            self.logger.info("*****TC_002***** started")
            self.d.get(account_Read_Ini().get_Launching_url())
            self.status.clear()
            time.sleep(web_driver.three_second)
            logo = self.d.find_element(By.XPATH, account_Read_Ini().get_logo_is_visible_on_login_page())
            username = self.d.find_element(By.XPATH, account_Read_Ini().get_username_textbox())
            username.is_displayed()
            password = self.d.find_element(By.XPATH, account_Read_Ini().get_password_textbox())
            password.is_displayed()
            if logo.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            print(self.status)
            self.logger.info(f"status:{self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_account_002.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_002.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_002.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\Tc_account_002.png")
            self.logger.error(f"TC_account_002 got exception as: {ex} ")
            print(ex)

    def load_login_page_if_not_loaded(self):
        try:
            self.d.get(account_Read_Ini().get_Launching_url())
            expected_url = account_Read_Ini().get_Launching_url()
            time.sleep(web_driver.two_second)
            self.d.maximize_window()
            actual_url = self.d.current_url
            print(f"actual: {actual_url}, expected: {expected_url}")
            if expected_url == actual_url:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            username = self.d.find_element(By.XPATH, account_Read_Ini().get_username_textbox())
            username.clear()
            username.send_keys(account_Read_Ini().get_valid_username())
            time.sleep(web_driver.two_second)
            password = self.d.find_element(By.XPATH, account_Read_Ini().get_password_textbox())
            password.clear()
            password.send_keys(account_Read_Ini().get_valid_password())
            time.sleep(web_driver.two_second)
            cloud_login = self.d.find_element(By.XPATH, account_Read_Ini().get_cloudlogin_button())
            cloud_login.click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            print(ex)

    def verify_on_cloud_menu_after_login(self):
        try:
            self.logger.info("*****TC_003_*****started")
            self.load_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.two_second)
            cloud_menu = self.d.find_element(By.XPATH, account_Read_Ini().get_afterlogin_cloud_menu_is_visible())
            if cloud_menu.is_displayed():
                self.logger.info(f"cloud menu is displayed after login,{cloud_menu}")
                self.status.append(True)
            else:
                self.logger.info(f"cloud menu is not displayed after login,{cloud_menu}")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_003.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_003.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_003.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_003.png")
            self.logger.error(f"TC_account_003 got exception as: {ex} ")

    def verify_account_is_visible_in_dashboard_items(self):
        try:
            self.logger.info("********TC_004****** started")
            self.load_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.one_second)
            account_in_dashboarditems=self.d.find_element(By.XPATH,account_Read_Ini().account_in_dashboarditems())
            if account_in_dashboarditems.is_displayed():
                self.logger.info("account is visible in dashboard items")
                self.status.append(True)
            else:
                self.logger.info("account is not visible in dashboard items")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
               self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_004.png")
               self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_004.png")
               return False
            else:
               return True
        except Exception as ex:
               self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_004.png")
               self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_004.png")
               self.logger.error(f"TC_account_004 got exception as: {ex} ")
    '''

    def wait_for_element_to_appear(self, element_list, xpath):
        count = 0
        if len(element_list) == 0:
            while len(element_list) == 0 or count == 10:
                element_list = self.d.find_elements(By.XPATH, xpath)
                time.sleep(web_driver.one_second)
                if len(element_list) > 0:
                    self.logger.info("element is visible...")
                    return element_list[0]
                else:
                    self.logger.info("waiting for element...")
                count += 1
                self.logger.info(f"wait count: {count}")
        else:
            self.logger.info(f"element length: {len(element_list)}")
            return element_list[0]

    def verify_panel_heading_of_Account(self):
        try:
            self.logger.info("********TC_005******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            account_panel_heading = self.d.find_element(By.XPATH, account_Read_Ini().Account_panel_heading())
            self.logger.info(f"account_panel_heading_displayed: {account_panel_heading.is_displayed()}")
            if account_panel_heading.is_displayed():
                self.logger.info("Account panel heading is displayed")
                self.status.append(True)
            else:
                self.logger.info("Account panel heading is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:

                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_005_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_005_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_005_Exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_005.png")
            self.logger.error(f"TC_account_005 got exception as: {ex} ")

    def verify_Account_Details_banner_is_visible(self):
        try:
            self.logger.info("*********TC_006******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            account_details_banner = self.d.find_element(By.XPATH, account_Read_Ini().Account_details_banner())
            self.logger.info(f"account_details_banner_displayed: {account_details_banner.is_displayed()}")
            if account_details_banner.is_displayed():
                self.logger.info("account details banner is visible")
                self.status.append(True)
            else:
                self.logger.info("account details banner is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:

                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_006_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_006_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_006_Exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_006_Exception.png")
            self.logger.error(f"TC_account_006 got exception as: {ex} ")

    def verify_Enabled_true_is_displayed(self):
        try:
            self.logger.info("*******TC_007******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            enabled_text = self.d.find_element(By.XPATH, account_Read_Ini().get_enabled_text())
            true_text = self.d.find_element(By.XPATH, account_Read_Ini().get_true_text())
            actual_text = f"{enabled_text} {true_text}"
            self.logger.info(f"actual text: {actual_text}")
            enabled = account_Read_Ini().read_enabled()
            true = account_Read_Ini().read_true()
            expected_text = f"{enabled} {true}"
            self.logger.info(f"expected text: {expected_text}")
            self.logger.info(f"enabled_text displayed: {enabled_text.is_displayed()}")
            if enabled_text.is_displayed():
                self.logger.info("enabled = true")
                self.status.append(True)
            else:
                self.logger.info("enabled = false")
                self.status.append(False)
            if true_text.is_displayed():
                self.logger.info("true is visible")
                self.status.append(True)
            else:
                self.logger.info("true is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_007_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_007_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_007_Exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_007_exception.png")
            self.logger.error(f"TC_account_007 got exception as: {ex} ")

    def verify_Enrollments_and_its_number_is_displayed(self):
        try:
            self.logger.info("******TC_008 ******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            enrollment = self.d.find_element(By.XPATH, account_Read_Ini().get_Enrollments_text())
            enrollment_number = self.d.find_element(By.XPATH, account_Read_Ini().get_number_of_enrollment_text())
            actual_text = f"{enrollment.text} {enrollment_number.text}"
            print(actual_text)
            self.logger.info(f"actual text is :{actual_text}")
            self.logger.info(f"enrollment displayed: {enrollment.is_displayed()}")
            if enrollment.is_displayed():
                self.logger.info("enrollments = 27/1000000")
                self.status.append(True)
            else:
                self.logger.info("enrollment number is not equal")
                self.status.append(False)
            self.logger.info(f"enrollment_number displayed: {enrollment_number.is_displayed()}")
            if enrollment_number.is_displayed():
                self.logger.info("enrollment number is visible")
                self.status.append(True)
            else:
                self.logger.info("enrollment number is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:

                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_008_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_008_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_008_Exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_008_Exception.png")
            self.logger.error(f"TC_account_008 got exception as: {ex} ")

    def verify_Users_Created_and_its_number_is_displayed(self):
        try:
            self.logger.info("*******TC_009 started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            users_created = self.d.find_element(By.XPATH, account_Read_Ini().get_usercreated_text())
            users_created_number = self.d.find_element(By.XPATH, account_Read_Ini().get_number_of_usercreated())
            actual_text = f"{users_created.text} {users_created_number.text}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            self.logger.info(f"users_created displayed: {users_created.is_displayed()}")
            if users_created.is_displayed():
                self.logger.info("users created = 33/100")
                self.status.append(True)
            else:
                self.logger.info("users created number is not equal")
                self.status.append(False)
            if users_created_number.is_displayed():
                self.logger.info("users created number is visible")
                self.status.append(True)
            else:
                self.logger.info("user created number is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_009_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_009_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_009_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_009_exception.png")
            self.logger.error(f"TC_account_009 got exception as: {ex} ")

    def verify_Max_Investigation_Length_along_withits_number_is_displayed(self):
        try:
            self.logger.info("********TC_10******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            maximum_investigation_text = self.d.find_element(By.XPATH, account_Read_Ini().get_maximum_investigation_length())
            maximum_investigation_number = self.d.find_element(By.XPATH, account_Read_Ini().get_number_of_maximum_investigation())
            actual_text = f"{maximum_investigation_text.text} {maximum_investigation_number.text}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            self.logger.info(f"maximum_investigation_text displayed: {maximum_investigation_text.is_displayed()}")
            if maximum_investigation_text.is_displayed():
                self.logger.info("maximum_investigation_length = 1800")
                self.status.append(True)
            else:
                self.logger.info("maximum investigation length is not equal")
                self.status.append(False)
            self.logger.info(f"maximum_investigation_number displayed: {maximum_investigation_number.is_displayed()}")
            if maximum_investigation_number.is_displayed():
                self.logger.info("maximum investigation number is visible")
                self.status.append(True)
            else:
                self.logger.info("maximum investigation number is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_010_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_010_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_010_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_010_exception.png")
            self.logger.error(f"TC_account_010 got exception as: {ex} ")

    def verify_Enrollment_Groups_along_with_its_number_is_displayed(self):
        try:
            self.logger.info("*******TC_011******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            enrollment_groups = self.d.find_element(By.XPATH, account_Read_Ini().enrollment_groups())
            enrollment_groups_number = self.d.find_element(By.XPATH, account_Read_Ini().number_enrollment_groups())
            actual_text = f"{enrollment_groups} {enrollment_groups_number}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            if enrollment_groups:
                self.logger.info("Enrollments groups = 450")
                self.status.append(True)
            else:
                self.logger.info("Enrollment groups is not equal")
                self.status.append(False)
            self.logger.info(f"enrollment_groups_number displayed: {enrollment_groups_number.is_displayed()}")
            if enrollment_groups_number.is_displayed():
                self.logger.info("enrollment number is visible")
                self.status.append(True)
            else:
                self.logger.info("enrollment group number is visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_011_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_011_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_011_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_011_exception.png")
            self.logger.error(f"TC_account_011 got exception as: {ex} ")

    def verify_Notification_Groups_along_its_number_is_displayed(self):
        try:
            self.logger.info("*******TC_012******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.append(True)
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            notification_groups = self.d.find_element(By.XPATH, account_Read_Ini().notification_group())
            number_of_notification_groups = self.d.find_element(By.XPATH, account_Read_Ini().number_of_notification_groups())
            actual_text = f"{notification_groups.text} {number_of_notification_groups.text}"
            self.logger.info(f"actual text {actual_text}")
            print(actual_text)
            self.logger.info(f"notification_groups displayed: {notification_groups.is_displayed()}")
            if notification_groups.is_displayed():
                self.logger.info("notification group = 5")
                self.status.append(True)
            else:
                self.logger.info("notification group number number is not equal")
                self.status.append(False)
            self.logger.info(f"number_of_notification_groups displayed: {number_of_notification_groups.is_displayed()}")
            if number_of_notification_groups.is_displayed():
                self.logger.info("number of notifications groups created is visible")
                self.status.append(True)
            else:
                self.logger.info("number of notification groups created is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_012_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_012_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_012_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_012_exception.png")
            self.logger.error(f"TC_account_012 got exception as: {ex} ")

    def verify_Stations_along_its_number_is_displayed(self):
        try:
            self.logger.info("*******TC_013******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            stations = self.d.find_element(By.XPATH, account_Read_Ini().get_stations())
            number_of_stations = self.d.find_element(By.XPATH, account_Read_Ini().number_of_stations())
            actual_text = f"{stations} {number_of_stations}"
            self.logger.info(f"actual text is {actual_text} ")
            print(actual_text)
            self.logger.info(f"stations are displayed: {stations.is_displayed()}")
            if stations.is_displayed():
                self.logger.info("stations = 6")
                self.status.append(True)
            else:
                self.logger.info("stations not equal ")
                self.status.append(False)
            self.logger.info(f"number_of_stations displayed: {number_of_stations.is_displayed()}")
            if number_of_stations.is_displayed():
                self.logger.info("number of stations is visible")
                self.status.append(True)
            else:
                self.logger.info("number of stations is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_013_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_013_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_013_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_013_exception.png")
            self.logger.error(f"TC_account_013 got exception as: {ex} ")

    def verify_First_Name_is_displayed(self):
        try:
            self.logger.info("*******TC_014******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            firstname = self.d.find_element(By.XPATH, account_Read_Ini().get_firstname())
            comapany_is_firstname = self.d.find_element(By.XPATH, account_Read_Ini().get_comapny_text())
            actual_text = f"{firstname.text} {comapany_is_firstname.text}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            self.logger.info(f"firstname displayed: {firstname.is_displayed()}")
            if firstname.is_displayed():
                self.logger.info("firstname = company")
                self.status.append(True)
            else:
                self.logger.info("firstname is not a company")
                self.status.append(False)
            self.logger.info(f"comapany_is_firstname displayed: {comapany_is_firstname.is_displayed()}")
            if comapany_is_firstname.is_displayed():
                self.logger.info("comapny is visible")
                self.status.append(True)
            else:
                self.logger.info("company is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_014_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_014_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_014_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_014_exception.png")
            self.logger.error(f"TC_account_014 got exception as: {ex} ")

    def verify_Middle_Name_is_displayed(self):
        try:
            self.logger.info("*******TC_015******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            middlename = self.d.find_element(By.XPATH, account_Read_Ini().get_middle_name())
            name_of_middilename = self.d.find_element(By.XPATH, account_Read_Ini().name_of_middle_name())
            actual_text = f"{middlename.text} {name_of_middilename.text}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            self.logger.info(f"middle name is displayed: {middlename.is_displayed()}")
            if middlename.is_displayed():
                self.logger.info("middlename = ")
                self.status.append(True)
            else:
                self.logger.info("middle name is not same")
                self.status.append(False)
            self.logger.info(f"name_of_middilename displayed: {name_of_middilename.is_displayed()}")
            if name_of_middilename.is_displayed():
                self.logger.info("name of middle name is visible")
                self.status.append(True)
            else:
                self.logger.info("name of middle name is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_015_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_015_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_015_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_015_exception.png")
            self.logger.error(f"TC_account_015 got exception as: {ex} ")

    def verify_Last_Name_is_displayed(self):
        try:
            self.logger.info("********TC_016******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            lastname = self.d.find_element(By.XPATH, account_Read_Ini().get_last_name())
            time.sleep(web_driver.one_second)
            name_of_lastname = self.d.find_element(By.XPATH, account_Read_Ini().name_of_lastname())
            actual_text = f"{lastname.text} { name_of_lastname.text}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            time.sleep(web_driver.one_second)
            self.logger.info(f"last name displayed: {lastname.is_displayed()}")
            if lastname.is_displayed():
                self.status.append("lastname is visible")
                self.status.append(True)
            else:
                self.logger.info("lastname is not visible")
                self.status.append(False)
            self.logger.info(f"name_of_lastname displayed: {name_of_lastname.is_displayed()}")
            if name_of_lastname.is_displayed():
                self.logger.info("name of lastname is visible")
                self.status.append(True)
            else:
                self.logger.info("name of lastname is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_016_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_016_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_016_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_016_exception.png")
            self.logger.error(f"TC_account_016 got exception as: {ex} ")

    def verify_Company_and_its_name_is_displayed(self):
        try:
            self.logger.info("*******TC_017********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            company = self.d.find_element(By.XPATH, account_Read_Ini().get_company())
            time.sleep(web_driver.one_second)
            name_of_company = self.d.find_element(By.XPATH, account_Read_Ini().get_company())
            time.sleep(web_driver.one_second)
            actual_text = f"{company.text} {name_of_company.text}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            time.sleep(web_driver.one_second)
            self.logger.info(f"company displayed: {company.is_displayed()}")
            if company.is_displayed():
                self.logger.info("comapany is visible")
                self.status.append(True)
            else:
                self.logger.info("company name is not visible")
                self.status.append(False)
            self.logger.info(f"name_of_company displayed: {name_of_company.is_displayed()}")
            if name_of_company.is_displayed():
                self.logger.info("name of company is visible")
                self.status.append(True)
            else:
                self.logger.info("name of company is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_017_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_017_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_017_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_017_exception.png")
            self.logger.error(f"TC_account_017 got exception as: {ex} ")

    def verify_Department_and_its_name_is_displayed(self):
        try:
            self.logger.info("*********TC_018******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            department = self.d.find_element(By.XPATH, account_Read_Ini().get_department())
            time.sleep(web_driver.one_second)
            name_of_department = self.d.find_element(By.XPATH, account_Read_Ini().name_of_department())
            time.sleep(web_driver.one_second)
            actual_text = f"{department.text} {name_of_department.text}"
            self.logger.info(f"actual text is {actual_text} ")
            print(actual_text)
            time.sleep(web_driver.one_second)
            self.logger.info(f"department displayed: {department.is_displayed()}")
            if department.is_displayed():
                self.logger.info("department is displayed")
                self.status.append(True)
            else:
                self.logger.info("department is not displayed")
                self.status.append(False)
            self.logger.info(f"name_of_department displayed: {name_of_department.is_displayed()}")
            if name_of_department.is_displayed():
                self.logger.info("name of department is visible")
                self.status.append(True)
            else:
                self.logger.info("name of department is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_018_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_018_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_018_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_018_exception.png")
            self.logger.error(f"TC_account_018 got exception as: {ex} ")

    def verify_Title_and_its_name_is_displayed(self):
        try:
            self.logger.info("**********TC_019*********** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            title = self.d.find_element(By.XPATH, account_Read_Ini().get_title())
            time.sleep(web_driver.one_second)
            name_of_title = self.d.find_element(By.XPATH, account_Read_Ini().name_of_title())
            time.sleep(web_driver.one_second)
            actual_text = f"{title.text} {name_of_title.text}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            time.sleep(web_driver.one_second)
            self.logger.info(f"title displayed: {title.is_displayed()}")
            if title.is_displayed():
                self.logger.info("titile is visible")
                self.status.append(True)
            else:
                self.logger.info("title is not visible")
                self.status.append(False)
            self.logger.info(f"name_of_title displayed: {name_of_title.is_displayed()}")
            if name_of_title.is_displayed():
                self.logger.info("title name is visible")
                self.status.append(True)
            else:
                self.logger.info("title name is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_019_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_019_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_019_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_019_exception.png")
            self.logger.error(f"TC_account_019 got exception as: {ex} ")

    def verify_Email_and_its_emailid_is_displayed(self):
        try:
            self.logger.info("******* TC_020 ******* started ")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            email = self.d.find_element(By.XPATH, account_Read_Ini().get_Email())
            time.sleep(web_driver.one_second)
            email_id = self.d.find_element(By.XPATH, account_Read_Ini().email_id())
            time.sleep(web_driver.one_second)
            actual_text = f"{email.text} {email_id.text}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            self.logger.info(f"email displayed: {email.is_displayed()}")
            if email.is_displayed():
                self.logger.info("email is visible")
                self.status.append(True)
            else:
                self.logger.info("email is not visible")
                self.status.append(False)
            self.logger.info(f"email_id displayed: {email_id.is_displayed()}")
            if email_id.is_displayed():
                self.logger.info("email id is visible")
                self.status.append(True)
            else:
                self.logger.info("email id is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_020_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_020_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_020_Exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_020_Exception.png")
            self.logger.error(f"TC_account_020 got exception as: {ex} ")

    def verify_Home_Phone_and_its_number_is_displayed(self):
        try:
            self.logger.info("********TC_021******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            home_phone = self.d.find_element(By.XPATH, account_Read_Ini().Home_phone())
            time.sleep(web_driver.one_second)
            number_of_home_phone = self.d.find_element(By.XPATH, account_Read_Ini().number_of_home_phone())
            time.sleep(web_driver.one_second)
            actual_text = f"{home_phone.text} {number_of_home_phone.text}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            self.logger.info(f"home_phone displayed: {home_phone.is_displayed()}")
            if home_phone.is_displayed():
                self.logger.info("home phone is visible")
                self.status.append(True)
            else:
                self.logger.info("home phone is not visible")
                self.status.append(False)
            self.logger.info(f"number_of_home_phone displayed: {number_of_home_phone.is_displayed()}")
            if number_of_home_phone.is_displayed():
                self.logger.info("number of home phone is visible")
                self.status.append(True)
            else:
                self.logger.info("number of home phone is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_021_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_021_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_021_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_021_exception.png")
            self.logger.error(f"TC_account_021 got exception as: {ex} ")

    def verify_Work_Phone_and_its_number_displayed(self):
        try:
            self.logger.info("********TC_022******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            work_phone = self.d.find_element(By.XPATH, account_Read_Ini().work_phone_number())
            time.sleep(web_driver.one_second)
            work_phone_number = self.d.find_element(By.XPATH, account_Read_Ini().work_phone_number())
            time.sleep(web_driver.one_second)
            actual_text = f"{work_phone.text} {work_phone_number.text}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            self.logger.info(f"work_phone displayed: {work_phone.is_displayed()}")
            if work_phone.is_displayed():
                self.logger.info("work phone is visible")
                self.status.append(True)
            else:
                self.logger.info("work phone is not visible")
                self.status.append(False)
            self.logger.info(f"work_phone_number displayed: {work_phone_number.is_displayed()}")
            if work_phone_number.is_displayed():
                self.logger.info("work phone number is visible")
                self.status.append(True)
            else:
                self.logger.info("work phone number is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_022_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_022_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_022_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_022_exception.png")
            self.logger.error(f"TC_account_022 got exception as: {ex} ")

    def verify_Fax_Number_and_its_number_is_displayed(self):
        try:
            self.logger.info("***********TC_023******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            fax = self.d.find_element(By.XPATH, account_Read_Ini().get_fax())
            time.sleep(web_driver.one_second)
            fax_number = self.d.find_element(By.XPATH, account_Read_Ini().fax_number())
            time.sleep(web_driver.one_second)
            actual_text = f"{fax.text} {fax_number.text}"
            self.logger.info(f"actual text is {actual_text}")
            time.sleep(web_driver.one_second)
            self.logger.info(f"fax displayed: {fax.is_displayed()}")
            if fax.is_displayed():
                self.logger.info("fax is visible")
                self.status.append(True)
            else:
                self.logger.info("fax is not visible")
                self.status.append(False)
            self.logger.info(f"fax_number displayed: {fax_number.is_displayed()}")
            if fax_number.is_displayed():
                self.logger.info("fax number is visible")
                self.status.append(True)
            else:
                self.logger.info("fax number is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_023_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_023_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_023_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_023_exception.png")
            self.logger.error(f"TC_account_023 got exception as: {ex} ")

    def verify_Address_and_its_address_displayed(self):
        try:
            self.logger.info("**********TC_024****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            address = self.d.find_element(By.XPATH, account_Read_Ini().get_Address())
            time.sleep(web_driver.one_second)
            address_details = self.d.find_element(By.XPATH, account_Read_Ini().Address_name())
            time.sleep(web_driver.one_second)
            actual_text = f"{address.text} {address_details.text}"
            self.logger.info(f"actual text is {actual_text}")
            time.sleep(web_driver.one_second)
            self.logger.info(f"address displayed: {address.is_displayed()}")
            if address.is_displayed():
                self.logger.info("adress is visible")
                self.status.append(True)
            else:
                self.logger.info("address is not visible")
                self.status.append(False)
            self.logger.info(f"address_details displayed: {address_details.is_displayed()}")
            if address_details.is_displayed():
                self.logger.info("address details are visible")
                self.status.append(True)
            else:
                self.logger.info("address details are not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_024_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_024_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_024_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_024_exception.png")
            self.logger.error(f"TC_account_024 got exception as: {ex} ")

    def verify_Address2_and_its_details_is_displayed(self):
        try:
            self.logger.info("*********TC_025******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            address2 = self.d.find_element(By.XPATH, account_Read_Ini().get_address2())
            time.sleep(web_driver.one_second)
            address2_details = self.d.find_element(By.XPATH, account_Read_Ini().address2_details())
            time.sleep(web_driver.one_second)
            actual_text = f"{address2.text} {address2_details.text}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            self.logger.info(f"address2 displayed: {address2.is_displayed()}")
            if address2.is_displayed():
                self.logger.info("address2 is displayed")
                self.status.append(True)
            else:
                self.logger.info("address2 is not visible")
                self.status.append(False)
            self.logger.info(f"address2_details displayed: {address2_details.is_displayed()}")
            if address2_details.is_displayed():
                self.logger.info("address2 details are visible")
                self.status.append(True)
            else:
                self.logger.info("address 2 details are not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_025_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_025_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_025_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_025_exception.png")
            self.logger.error(f"TC_account_025 got exception as: {ex} ")

    def verify_city_name_of_cityis_displayed(self):
        try:
            self.logger.info("********TC_026****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            city = self.d.find_element(By.XPATH, account_Read_Ini().get_city())
            time.sleep(web_driver.one_second)
            city_name = self.d.find_element(By.XPATH, account_Read_Ini().city_name())
            time.sleep(web_driver.one_second)
            actual_text = f"{city.text} {city_name.text}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            time.sleep(web_driver.one_second)
            self.logger.info(f"address2_details displayed: {city.is_displayed()}")
            if city.is_displayed():
                self.logger.info("city is visible")
                self.status.append(True)
            else:
                self.logger.info("city is not visible")
                self.status.append(False)
            self.logger.info(f"address2_details displayed: {city_name.is_displayed()}")
            if city_name.is_displayed():
                self.logger.info("city name is visible")
                self.status.append(True)
            else:
                self.logger.info("city name is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_026_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_025_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_026_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_025_exception.png")
            self.logger.error(f"TC_account_026 got exception as: {ex} ")

    def verify_State_and_its_nameis_displayed(self):
        try:
            self.logger.info("********TC_027******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            state = self.d.find_element(By.XPATH, account_Read_Ini().get_state())
            time.sleep(web_driver.one_second)
            name_of_state = self.d.find_element(By.XPATH, account_Read_Ini().state_name())
            time.sleep(web_driver.one_second)
            actual_text = f"{state.text} {name_of_state.text}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            time.sleep(web_driver.one_second)
            self.logger.info(f"state displayed: {state.is_displayed()}")
            if state.is_displayed():
                self.logger.info("state is visible")
                self.status.append(True)
            else:
                self.logger.info("state is not visible")
                self.status.append(False)
            self.logger.info(f"name_of_state displayed: {name_of_state.is_displayed()}")
            if name_of_state.is_displayed():
                self.logger.info("state name is visible")
                self.status.append(True)
            else:
                self.logger.info("state name is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_027_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_027_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_027_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_027_exception.png")
            self.logger.error(f"TC_account_027 got exception as: {ex} ")

    def verify_Zip_Code_and_its_number_is_displayed(self):
        try:
            self.logger.info("*******TC_028******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            zipcode = self.d.find_element(By.XPATH, account_Read_Ini().get_zipcode())
            time.sleep(web_driver.one_second)
            zipcode_number = self.d.find_element(By.XPATH, account_Read_Ini().zipcode_number())
            time.sleep(web_driver.one_second)
            actual_text = f"{zipcode} {zipcode_number}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            time.sleep(web_driver.one_second)
            self.logger.info(f"zipcode displayed: {zipcode.is_displayed()}")
            if zipcode.is_displayed():
                self.logger.info("zipcode is visible")
                self.status.append(True)
            else:
                self.logger.info("zipcode is not visible")
                self.status.append(False)
            self.logger.info(f"zipcode_number displayed: {zipcode_number.is_displayed()}")
            if zipcode_number.is_displayed():
                self.logger.info("zipcode number is visible")
                self.status.append(True)
            else:
                self.logger.info("zipcode number is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_028_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_028_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_028_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_028_exception.png")
            self.logger.error(f"TC_account_028 got exception as: {ex} ")

    def verify_Timezone_Asia_Kolkata_is_displayed(self):
        try:
            self.logger.info("******TC_029****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            timezone = self.d.find_element(By.XPATH, account_Read_Ini().get_timezone())
            time.sleep(web_driver.one_second)
            asia_timezone = self.d.find_element(By.XPATH, account_Read_Ini().timezone_by_xpath())
            time.sleep(web_driver.one_second)
            actual_text = f"{timezone.text} {asia_timezone.text}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            self.logger.info(f"timezone displayed: {timezone.is_displayed()}")
            if timezone.is_displayed():
                self.logger.info("timezone is visible")
                self.status.append(True)
            else:
                self.logger.info("timezone is not visible")
                self.status.append(False)
            self.logger.info(f"asia_timezone displayed: {asia_timezone.is_displayed()}")
            if asia_timezone.is_displayed():
                self.logger.info("asia timezone is visible")
                self.status.append(True)
            else:
                self.logger.info("asia timezone is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_029-failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_029_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_029_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_029_exception.png")
            self.logger.error(f"TC_account_029 got exception as: {ex} ")

    def verify_Case_TTL_and_its_seconds_is_displayed(self):
        try:
            self.logger.info("********TC_030******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.one_second)
            casettl = self.d.find_element(By.XPATH, account_Read_Ini().get_case_TTL())
            time.sleep(web_driver.one_second)
            casettl_seconds = self.d.find_element(By.XPATH, account_Read_Ini().case_ttl_seconds())
            time.sleep(web_driver.one_second)
            actual_text = f"{casettl.text} {casettl_seconds.text}"
            self.logger.info(f"actual text is {actual_text}")
            print(actual_text)
            self.logger.info(f"casettl displayed: {casettl.is_displayed()}")
            if casettl.is_displayed():
                self.logger.info("casettl is visible")
                self.status.append(True)
            else:
                self.logger.info("casettl is not visible")
                self.status.append(False)
            self.logger.info(f"casettl_seconds displayed: {casettl_seconds.is_displayed()}")
            if casettl_seconds.is_displayed():
                self.logger.info("casettl seconds is visible")
                self.status.append(True)
            else:
                self.logger.info("casettl seconds is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_30_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_30_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_30_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_030_exception.png")
            self.logger.error(f"TC_account_030 got exception as: {ex} ")

    def verify_subscription_button_is_visible(self):
        try:
            self.logger.info("*******TC_031******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            subscription = self.d.find_element(By.XPATH, account_Read_Ini().get_subscription())
            time.sleep(web_driver.two_second)
            self.logger.info(f"subscription displayed: {subscription.is_displayed()}")
            if subscription.is_displayed():
                self.logger.info("subscription button is visible")
                self.status.append(True)
            else:
                self.logger.info("subscription is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_31_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_31_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_31_Exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_031_exception.png")
            self.logger.error(f"TC_account_031 got exception as: {ex} ")

    def click_on_subscription_button_verify_account_subscription_banner_is_visible(self):
        try:
            self.logger.info("*******TC_032***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            subscription = self.d.find_element(By.XPATH, account_Read_Ini().get_subscription())
            time.sleep(web_driver.two_second)
            subscription.click()
            time.sleep(web_driver.two_second)
            account_subscription = self.d.find_element(By.XPATH, account_Read_Ini().account_subscription())
            time.sleep(web_driver.one_second)
            self.logger.info(f"account_subscription displayed: {account_subscription.is_displayed()}")
            if account_subscription.is_displayed():
                self.logger.info("account subscription is visible")
                self.status.append(True)
            else:
                self.logger.info("account subscription is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_32_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_32_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_32_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_032_Exception.png")
            self.logger.error(f"TC_account_032 got exception as: {ex} ")

    def verify_Image_sources_button_is_visible(self):
        try:
            self.logger.info("*******TC_033***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.two_second)
            self.logger.info(f"image_source displayed: {image_source.is_displayed()}")
            if image_source.is_displayed():
                self.logger.info("image source button is visible")
                self.status.append(True)
            else:
                self.logger.info("image source button is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_33_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_33_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_33_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_033_exception.png")
            self.logger.error(f"TC_account_033 got exception as: {ex} ")

    def click_on_image_sources_and_check_theplanel_heading_of_Account_Image_sources_is_displayed(self):
        try:
            self.logger.info("**********TC_034******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.two_second)
            image_source.click()
            self.logger.info("click on image_source")
            time.sleep(web_driver.two_second)
            image_source_panel_heading = self.d.find_element(By.XPATH, account_Read_Ini().account_image_sources_panel_heading())
            self.logger.info(f"image_source_panel_heading displayed: {image_source_panel_heading.is_displayed()}")
            if image_source_panel_heading.is_displayed():
                self.logger.info("image source panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("image source panel heading is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_34_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_34_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_34_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_034_Exception.png")
            self.logger.error(f"TC_account_034 got exception as: {ex} ")

    def verify_view_dropdown_is_visible(self):
        try:
            self.logger.info("******TC_035******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.two_second)
            image_source.click()
            self.logger.info("click on image_source")
            time.sleep(web_driver.two_second)
            view_dropdown = self.d.find_element(By.XPATH, account_Read_Ini().view_dropdown())
            if view_dropdown.is_displayed():
                self.logger.info("view dropdown is display")
                self.status.append(True)
            else:
                self.logger.info("view dropdown is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_35_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_34_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_35_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_035_exception.png")
            self.logger.error(f"TC_account_035 got exception as: {ex} ")

    def click_on_location_on_View_dropdown_map_is_visible(self):
        try:
            self.logger.info("*******TC_036****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.two_second)
            image_source.click()
            self.logger.info("click on image_source")
            time.sleep(web_driver.two_second)
            view_dropdown = self.d.find_element(By.XPATH, account_Read_Ini().view_dropdown())
            view_dropdown.click()
            self.logger.info("click on view_dropdown")
            time.sleep(web_driver.two_second)
            location = self.d.find_element(By.XPATH, account_Read_Ini().location_in_viewdropdown())
            location.click()
            self.logger.info("click on location")
            time.sleep(web_driver.two_second)
            a = self.d.switch_to.alert
            a.accept()
            time.sleep(web_driver.one_second)
            checkbox = self.d.find_element(By.XPATH, account_Read_Ini().select_checkbox())
            checkbox.click()
            self.logger.info("click on checkbox")
            time.sleep(web_driver.one_second)
            view_dropdown = self.d.find_element(By.XPATH, account_Read_Ini().view_dropdown())
            view_dropdown.click()
            self.logger.info("click on view_dropdown")
            time.sleep(web_driver.two_second)
            location = self.d.find_element(By.XPATH, account_Read_Ini().location_in_viewdropdown())
            location.click()
            self.logger.info("click on location")
            time.sleep(web_driver.two_second)
            map_1 = self.d.find_element(By.XPATH, account_Read_Ini().get_map())
            if map_1.is_displayed():
                self.logger.info("map is display")
                self.status.append(True)
            else:
                self.logger.info("map is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_36_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_36_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_36_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_036_exception.png")
            self.logger.error(f"TC_account_036 got exception as: {ex} ")

    def verify_regions_button_is_visible(self):
        try:
            self.logger.info("*****TC_037*****strted")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.two_second)
            image_source.click()
            self.logger.info("click on image_source")
            time.sleep(web_driver.two_second)
            regions = self.d.find_element(By.XPATH, account_Read_Ini().regions_button())
            if regions.is_displayed():
                self.logger.info("regions is displayed")
                self.status.append(True)
            else:
                self.logger.info("regions is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_37_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_37_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_37_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_037_exception.png")
            self.logger.error(f"TC_account_037 got exception as: {ex} ")

    def click_on_regions_button_verify_panel_heading(self):
        try:
            self.logger.info("******TC_038****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.one_second)
            image_source.click()
            self.logger.info("click on image_source")
            time.sleep(web_driver.three_second)
            regions = self.d.find_element(By.XPATH, account_Read_Ini().regions_button())
            regions.click()
            self.logger.info("click on regions")
            time.sleep(web_driver.two_second)
            zones_panel_heading = self.d.find_element(By.XPATH, account_Read_Ini().zones_panel_heading())
            if zones_panel_heading.is_displayed():
                self.logger.info("zones panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("zones panel heading is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_38_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_38_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_38_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_038_exception.png")
            self.logger.error(f"TC_account_038 got exception as: {ex} ")

    def verify_details_button_is_visible(self):
        try:
            self.logger.info("********TC_039******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.two_second)
            image_source.click()
            self.logger.info("click on image_source")
            time.sleep(web_driver.two_second)
            details_button = self.d.find_element(By.XPATH, account_Read_Ini().details_button())
            if details_button.is_displayed():
                self.logger.info("details button is visible")
                self.status.append(True)
            else:
                self.logger.info("details button is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_39_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_39_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_39_Exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_039_Exception.png")
            self.logger.error(f"TC_account_039 got exception as: {ex} ")

    def click_on_detailsbutton_verify_imagesource_panel_heading_is_visible(self):
        try:
            self.logger.info("*******TC_040******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.two_second)
            image_source.click()
            self.logger.info("click on image_source")
            time.sleep(web_driver.two_second)
            details_button = self.d.find_element(By.XPATH, account_Read_Ini().details_button())
            details_button.click()
            self.logger.info("click on details_button")
            time.sleep(web_driver.two_second)
            image_source_panel_heading = self.d.find_element(By.XPATH, account_Read_Ini().image_source_panel_heading())
            if image_source_panel_heading.is_displayed():
                self.logger.info("image source panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("image source panel heading is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_40_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_40_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_40_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_040_exception.png")
            self.logger.error(f"TC_account_040 got exception as: {ex} ")

    def on_image_source_panel_verify_view_location_button_is_visible(self):
        try:
            self.logger.info("********TC_041******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.two_second)
            image_source.click()
            self.logger.info("click on image_source")
            time.sleep(web_driver.three_second)
            details_button = self.d.find_element(By.XPATH, account_Read_Ini().details_button())
            details_button.click()
            self.logger.info("click on details_button")
            time.sleep(web_driver.two_second)
            view_location = self.d.find_element(By.XPATH, account_Read_Ini().view_location_button())
            if view_location.is_displayed():
                self.logger.info("view location is visible")
                self.status.append(True)
            else:
                self.logger.info("view location button is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_41_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_41_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_41_Exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_041_Exception.png")
            self.logger.error(f"TC_account_041 got exception as: {ex} ")

    def click_on_viewlocation_button_on_imagesource_verify_location(self):
        try:
            self.logger.info("********TC_042****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            account = self.d.find_element(By.XPATH, account_Read_Ini().account_in_dashboarditems())
            account.click()
            self.logger.info("click on account dashboard items")
            time.sleep(web_driver.two_second)
            image_source = self.d.find_element(By.XPATH, account_Read_Ini().view_Image_source_button())
            time.sleep(web_driver.two_second)
            image_source.click()
            self.logger.info("click on image_source")
            time.sleep(web_driver.two_second)
            details_button = self.d.find_element(By.XPATH, account_Read_Ini().details_button())
            details_button.click()
            self.logger.info("click on details_button")
            time.sleep(web_driver.two_second)
            view_location = self.d.find_element(By.XPATH, account_Read_Ini().view_location_button())
            view_location.click()
            self.logger.info("click on view_location")
            time.sleep(web_driver.two_second)
            events_location = self.d.find_element(By.XPATH, account_Read_Ini().events_location_panel_heading())
            facefirst_logo = self.d.find_element(By.XPATH, account_Read_Ini().get_facefirst_logo_in_map())
            if events_location.is_displayed():
                self.logger.info("events location panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("events location panel heading is not visible")
                self.status.append(False)
            if facefirst_logo.is_displayed():
                self.logger.info("facefirst logo is visible")
                self.status.append(True)
            else:
                self.logger.info("facefirst logo is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_42_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_42-failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\Tc_account_42_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_account_042_exception.png")
            self.logger.error(f"TC_account_042 got exception as: {ex} ")
