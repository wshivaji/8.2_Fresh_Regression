import time
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Base_Package.Web_Logger import web_logger
from Base_Package.Web_Driver import web_driver
from Base_Package.Login_Logout_Ops import login, logout
from All_Config_Packages._11_Enrollment_config_Files.Enrollments_Read_INI import Read_Enrollments_Components


class Enrollments_Filter_combination_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    # def login_before(self):
    # 
    #     try:
    # 
    #         print("Before launching URL")
    #         self.d.get(Read_Portal_Menu_Components().get_url())
    #         time.sleep(web_driver.one_second)
    #         print("After launching URL")
    #         print("Before launching time sleep")
    #         self.d.maximize_window()
    #         # time.sleep(web_driver.two_second)
    #         print("after launching time sleep")
    #         print("Before launching username")
    #         username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
    #         print("After launching username")
    #         print(username)
    #         time.sleep(web_driver.one_second)
    #         self.logger.info(f"username text box : {username.is_displayed()}")
    #         counter = 0
    #         while not username.is_displayed():
    #             time.sleep(web_driver.two_second)
    #             counter = counter + 1
    #             if counter > 3:
    #                 time.sleep(web_driver.one_second)
    #                 self.d.refresh()
    #         print("After while loop time sleep")
    #         time.sleep(web_driver.two_second)
    #         self.logger.info(f"username: {Read_Portal_Menu_Components().get_username()}")
    #         username.send_keys(Read_Portal_Menu_Components().get_username())
    #         time.sleep(web_driver.one_second)
    #         password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
    #         self.logger.info(f"password: {Read_Portal_Menu_Components().get_password()}")
    #         password.send_keys(Read_Portal_Menu_Components().get_password())
    #         time.sleep(web_driver.one_second)
    #         login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
    #         self.d.execute_script("arguments[0].click();", login_btn)
    #         time.sleep(web_driver.two_second)
    #         self.click_on_enrollments_link()
    #         time.sleep(web_driver.two_second)
    # 
    #     except Exception as ex:
    #         time.sleep(web_driver.one_second)
    #         msg = str(ex)
    #         if msg.__contains__('not clickable at point'):
    #             time.sleep(web_driver.one_second)
    #             print("Exception crated: ", ex, " #returning false# ")
    #             self.d.save_screenshot(
    #                 f"{Path(__file__).parent.parent}\\Screenshots\\login_failed_for_portal_menu_pg_03.png")

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

    def enrollments_search_with_no_filter_criteria(self):
        try:
            self.logger.info("*********TC_001********* started")
            # login().login_to_localhost_if_not_done()
            login().login_to_cloud_if_not_done(self.d)
            # self.load_login_page_if_not_loaded()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.two_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                time.sleep(web_driver.one_second)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_001_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_001_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_001_exception.png")

        # finally:
        # self.close_all_panel_one_by_one()
        # self.click_on_logout_button()

    def enrollments_search_with_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("********TC_002***** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            time.sleep(web_driver.one_second)
            self.status.clear()
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.select_sort_by_case_or_subject()
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                time.sleep(web_driver.one_second)
                self.status.append(var)
            else:
                self.status.append(False)
            var = self.verify_sort_key_case_subject()
            time.sleep(web_driver.one_second)
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                time.sleep(web_driver.one_second)
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_002_failed.png")
                time.sleep(web_driver.one_second)
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_002_failed.png")
                return False
            else:
                time.sleep(web_driver.one_second)
                return True
        except Exception as ex:
            time.sleep(web_driver.one_second)
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                time.sleep(web_driver.one_second)
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_002_exception.png")
        #     time.sleep(web_driver.one_second)
        # finally:
        #     time.sleep(web_driver.one_second)
        #     self.close_all_panel_one_by_one()

    def enrollments_search_with_sort_by_location_store_criteria(self):
        try:
            self.logger.info("******TC_003***** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.select_sort_by_location_or_store()
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            var = self.verify_sort_key_location_store()
            self.status.append(var)

            self.logger.info(f"status is {self.status}")
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_003_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_003_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_003_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_Sort_by_Enrolled_On_criteria(self):
        try:
            self.logger.info("******TC_004****** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.select_sort_by_enrolled_on()
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_004_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_004_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_004_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_expiration_Date_Range_criteria(self):
        try:
            self.logger.info("******TC_005****** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                time.sleep(web_driver.one_second)
                var = self.validate_match_list_output(4)
                time.sleep(web_driver.one_second)
                self.validate_expiration_start_or_end_date_search_result()
                time.sleep(web_driver.one_second)
                self.status.append(var)
                # self.status.append(var1)
            else:
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_005_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_005_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_005_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_expiration_Date_Range_and_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*******TC_006***** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            time.sleep(web_driver.one_second)
            self.select_sort_by_case_or_subject()
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                time.sleep(web_driver.one_second)
                var = self.validate_match_list_output(4)
                time.sleep(web_driver.one_second)
                self.status.append(var)
            else:
                self.status.append(False)
            self.validate_expiration_start_or_end_date_search_result()
            time.sleep(web_driver.one_second)
            # self.status.append(var)
            var = self.verify_sort_key_case_subject()
            time.sleep(web_driver.one_second)
            self.status.append(var)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_006***** end")
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_006_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_006_failed.png")
                return False
            else:
                return True
        except Exception as ex:

            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_006_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_expiration_date_range_and_sort_by_Location_store_criteria(self):
        try:
            self.logger.info("******TC_007****** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.handle_expiration_start_or_end_date_calender("from")
            time.sleep(web_driver.one_second)
            self.handle_expiration_start_or_end_date_calender("to")
            time.sleep(web_driver.one_second)
            self.select_sort_by_location_or_store()
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                time.sleep(web_driver.one_second)
                var = self.validate_match_list_output(4)
                time.sleep(web_driver.one_second)
                self.status.append(var)
            else:
                self.status.append(False)
            self.validate_expiration_start_or_end_date_search_result()
            time.sleep(web_driver.one_second)
            # self.status.append(var)
            var = self.verify_sort_key_location_store()
            time.sleep(web_driver.one_second)
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_007***** end")
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_007_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_007_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_007_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_expiration_date_range_and_sort_by_enrolled_On_criteria(self):
        try:
            self.logger.info("*******TC_008******* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            time.sleep(web_driver.one_second)
            self.select_sort_by_enrolled_on()
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                time.sleep(web_driver.one_second)
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.validate_expiration_start_or_end_date_search_result()
            time.sleep(web_driver.one_second)
            # self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_008***** end")
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_008_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_008_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_003_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_enrollment_Date_Range_criteria(self):
        try:
            self.logger.info("*********TC_009***** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.two_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.two_second)
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            time.sleep(web_driver.two_second)
            self.click_on_search_button()
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                var1 = self.validate_enrolled_start_or_end_date_search_result()
                self.status.append(var)
                self.status.append(var1)
            else:
                self.status.append(False)

            # var= self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_009***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_009_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_009_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_009_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_enrollment_Date_Range_and_Sort_by_Case_Subject_criteria(self):
        try:
            self.logger.info("******TC_010***** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            time.sleep(web_driver.one_second)
            self.select_sort_by_case_or_subject()
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                time.sleep(web_driver.one_second)
                var = self.validate_match_list_output(4)
                self.status.append(var)
                time.sleep(web_driver.one_second)
                var1 = self.validate_enrolled_start_or_end_date_search_result()
                self.status.append(var1)
                time.sleep(web_driver.one_second)
                var2 = self.verify_sort_key_case_subject()
                self.status.append(var2)
            else:
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_010***** end")
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_010_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_010_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_010_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_enrollment_Date_Range_and_Sort_by_Location_Store_criteria(self):
        try:
            self.logger.info("********TC_011***** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                time.sleep(web_driver.one_second)
                var = self.validate_match_list_output(4)
                time.sleep(web_driver.one_second)
                self.status.append(var)
                time.sleep(web_driver.one_second)
                var1 = self.validate_enrolled_start_or_end_date_search_result()
                self.status.append(var1)
                time.sleep(web_driver.one_second)
                var2 = self.verify_sort_key_location_store()
                self.status.append(var2)
            else:
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_011***** end")
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_011_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_011_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_011_exception.png")
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_Enrollment_Date_Range_and_Sort_by_enrolledOn_criteria(self):
        try:
            self.logger.info("*******TC_012******* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.two_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.two_second)
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()
            time.sleep(web_driver.two_second)
            self.click_on_search_button()
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                time.sleep(web_driver.one_second)
                var = self.validate_match_list_output(4)
                self.status.append(var)
                time.sleep(web_driver.one_second)
                var1 = self.validate_enrolled_start_or_end_date_search_result()
                self.status.append(var1)
            else:
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_012***** end")
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_012_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_012_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_012_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_Enrollment_Date_Range_and_Expiration_Date_Range_criteria(self):
        try:
            self.logger.info("*******TC_013******* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                time.sleep(web_driver.one_second)
                var = self.validate_match_list_output(4)
                self.status.append(var)
                time.sleep(web_driver.one_second)
                var1 = self.validate_enrolled_start_or_end_date_search_result()
                self.status.append(var1)
                time.sleep(web_driver.one_second)
                self.validate_expiration_start_or_end_date_search_result()
                # self.status.append(var2)
            else:
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_013***** end")
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_013_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_013_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_013_failed.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_Enrollment_Date_Range_Expiration_Date_Range_and_Sort_by_Case_Subject_criteria(self):
        try:
            self.logger.info("********TC_014****** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                time.sleep(web_driver.one_second)
                var = self.validate_match_list_output(4)
                self.status.append(var)
                time.sleep(web_driver.one_second)
                var1 = self.validate_enrolled_start_or_end_date_search_result()
                self.status.append(var1)
                time.sleep(web_driver.one_second)
                self.validate_expiration_start_or_end_date_search_result()
                # self.status.append(var2)
                time.sleep(web_driver.one_second)
                var3 = self.verify_sort_key_case_subject()
                self.status.append(var3)
            else:
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_014***** end")
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_014_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_014_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_014_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_Enrollment_Date_Range_Expiration_Date_Range_and_Sort_by_Location_Store_criteria(self):
        try:
            self.logger.info("*******TC_015****** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()

            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                time.sleep(web_driver.one_second)
                var = self.validate_match_list_output(4)
                self.status.append(var)
                time.sleep(web_driver.one_second)
                var1 = self.validate_enrolled_start_or_end_date_search_result()
                self.status.append(var1)
                time.sleep(web_driver.one_second)
                var2 = self.validate_expiration_start_or_end_date_search_result()
                self.status.append(var2)
                time.sleep(web_driver.one_second)
                self.verify_sort_key_location_store()
                # self.status.append(var3)
            else:
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_015***** end")
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_015_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_015_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_015_exception.png")

    def enrollments_search_with_Enrollment_Date_Range_Expiration_Date_Range_and_Sort_by_EnrolledOn_criteria(self):
        try:
            self.logger.info("*******TC_016****** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                time.sleep(web_driver.one_second)
                var = self.validate_match_list_output(4)
                self.status.append(var)
                time.sleep(web_driver.one_second)
                var1 = self.validate_enrolled_start_or_end_date_search_result()
                self.status.append(var1)
                time.sleep(web_driver.one_second)
                self.validate_expiration_start_or_end_date_search_result()
                # self.status.append(var2)
            else:
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_016***** end")
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_016_Failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_016_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_016_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_Exact_Text_Search_criteria(self):
        try:
            self.logger.info("********TC_017***** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.click_on_exact_text_search_checkBox()
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                time.sleep(web_driver.one_second)
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_017***** end")
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_017_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_017_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_017_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_Exact_Text_Search_and_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*******TC_018**** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_case_or_subject()
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                time.sleep(web_driver.one_second)
                var = self.validate_match_list_output(4)
                self.status.append(var)
                time.sleep(web_driver.one_second)
                var1 = self.verify_sort_key_case_subject()
                self.status.append(var1)
            else:
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_018***** end")
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_018_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_018_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_018_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_Exact_Text_Search_and_Sort_by_Location_Store_criteria(self):
        try:
            self.logger.info("******TC_019******* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_location_or_store()
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                time.sleep(web_driver.one_second)
                var = self.validate_match_list_output(4)
                self.status.append(var)
                time.sleep(web_driver.one_second)
                var1 = self.verify_sort_key_location_store()
                self.status.append(var1)
            else:
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_019***** end")
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_019_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_019_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_019_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_exact_text_search_and_sort_by_enrolledOn_criteria(self):
        try:
            self.logger.info("******TC_020****** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()

            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.click_on_exact_text_search_checkBox()
            time.sleep(web_driver.one_second)
            self.select_sort_by_enrolled_on()
            time.sleep(web_driver.one_second)

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                time.sleep(web_driver.one_second)
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_020***** end")
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_020_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_020_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_020_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_exact_text_search_and_expiration_date_range_criteria(self):
        try:
            self.logger.info("*****TC_021****** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.two_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_021***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_021_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_021_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_021_Exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_exact_text_search_expiration_date_range_and_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("******TC_022*** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
                self.validate_expiration_start_or_end_date_search_result()
                # self.status.append(var1)
                var2 = self.verify_sort_key_case_subject()
                self.status.append(var2)
            else:
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_022***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_022_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_022_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_022_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_exact_text_search_expiration_date_range_and_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*******TC_023*** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.two_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.two_second)
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
                self.validate_expiration_start_or_end_date_search_result()
                # self.status.append(var1)
                var2 = self.verify_sort_key_location_store()
                self.status.append(var2)
            else:
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_023***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_023_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_023_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_023_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_exact_text_search_expiration_date_range_and_Sort_by_EnrolledOn_criteria(self):
        try:
            self.logger.info("*******TC_024**** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.two_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.two_second)
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(web_driver.two_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
                self.validate_expiration_start_or_end_date_search_result()
                # self.status.append(var1)
            else:
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_024***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_024_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_024_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_024_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_exact_text_search_and_enrollment_date_range_criteria(self):
        try:
            self.logger.info("******TC_025******* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()

            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.two_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.two_second)
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            time.sleep(web_driver.one_second)
            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
                var1 = self.validate_enrolled_start_or_end_date_search_result()
                self.status.append(var1)
            else:
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_025***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_025_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_025_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_025_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_exact_text_search_enrollment_date_range_and_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("********TC_026 ****** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.two_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.two_second)
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()
            time.sleep(web_driver.two_second)
            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
                var1 = self.validate_enrolled_start_or_end_date_search_result()
                self.status.append(var1)
                var2 = self.verify_sort_key_case_subject()
                self.status.append(var2)
            else:
                self.status.append(False)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_026***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_026_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_026_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_026_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_enrollment_date_range_and_expiration_date_range_criteria(self):
        try:
            self.logger.info("*******TC_077**** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)
            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_077***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_077_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_077_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_076_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_enrollment_date_range_and_expiration_date_range_and_sort_by_case_subject_criteria(
            self):
        try:
            self.logger.info("******TC_078******** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.logger.info("executed click_on_enrollments_link")
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            print(self.status)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)
            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.verify_sort_key_case_subject()
            self.status.append(var)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_078***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_078_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_078_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_078_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_enrollment_date_range_and_expiration_date_range_and_sort_by_location_store_criteria(
            self):
        try:
            self.logger.info("********TC_079******** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)
            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_079***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_079_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_079_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_079_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_enrollment_date_range_and_expiration_date_range_and_sort_by_enrolledOn_criteria(
            self):
        try:
            self.logger.info("******TC_080***** started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)
            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_080***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_080_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_080_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_030_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_and_exact_text_search_criteria(self):
        try:
            self.logger.info("*********TC_081********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_081***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_081_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_081_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_081_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_and_exact_text_search_and_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_082********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_082***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_082_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_082_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_082_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_and_exact_text_search_and_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_083********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_083***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_083_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_083_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_033_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_and_exact_text_search_and_sort_by_enrolledOn_criteria(self):
        try:
            self.logger.info("*********TC_084********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_084***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_084_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_084_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_084_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_exact_text_search_and_expiration_date_range_criteria(self):
        try:
            self.logger.info("*********TC_085********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_085***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_085_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_085_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_085_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_exact_text_search_expiration_date_range_and_sort_by_case_subject_criteria(
            self):
        try:
            self.logger.info("*********TC_086********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)
            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_086***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_086_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_086_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_086_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_exact_text_search_expiration_date_range_and_sort_by_location_store_criteria(
            self):
        try:
            self.logger.info("*********TC_087********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_087***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_087_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_087_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_087_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_exact_text_search_expiration_date_range_and_sort_by_enrolledOn_criteria(
            self):
        try:
            self.logger.info("*********TC_088********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_088***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_088_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_088_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_088_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_exact_text_search_and_enrollment_date_range_criteria(self):
        try:
            self.logger.info("*********TC_089********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_039***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_089_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_089_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_089_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_exact_text_search_enrollment_date_range_and_sort_by_case_subject_criteria(
            self):
        try:
            self.logger.info("*********TC_090********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            var = self.verify_sort_key_case_subject()
            self.status.append(var)

            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_090***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_090_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_090_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_090_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_exact_text_search_enrollment_date_range_and_sort_by_location_store_criteria(
            self):
        try:
            self.logger.info("*********TC_091********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_091***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_091_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_091_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_091_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_exact_text_search_enrollment_date_range_and_sort_by_enrolledOn_criteria(
            self):
        try:
            self.logger.info("*********TC_092********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(web_driver.three_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_092***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_092_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_092_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_092_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_exact_text_search_enrollment_date_range_and_expiration_date_range_criteria(
            self):
        try:
            self.logger.info("*********TC_093********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.status.append(True)
            elif self.validate_match_list_output(4):
                # var=self.validate_match_list_output(4)
                self.status.append(True)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_093***** end")

            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_093_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_093_failed.png")
                self.close_all_panel_one_by_one()
                return False
            else:
                self.close_all_panel_one_by_one()
                return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_093_exception.png")

        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_exact_text_search_enrollment_date_range_expiration_date_range_and_sort_by_case_subject_criteria(
            self):
        try:
            self.logger.info("*********TC_094********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_094***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_094_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_094_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_094_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_exact_text_search_enrollment_date_range_expiration_date_range_and_sort_by_location_store_criteria(
            self):
        try:
            self.logger.info("*********TC_095********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_095***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_095_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_095_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_095_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_exact_text_search_enrollment_date_range_expiration_date_range_and_sort_by_enrolledOn_criteria(
            self):
        try:
            self.logger.info("*********TC_096********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_096***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_096_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_096_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_096_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_and_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_097********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()

            self.click_on_search_button()

            time.sleep(web_driver.three_second)

            if self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_097***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_097_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_097_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_097_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_and_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_098********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_098***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_098_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_098_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_098_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_and_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_099********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_099***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_099_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_099_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_099_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_and_sort_by_enrolledOn_criteria(self):
        try:
            self.logger.info("*********TC_100********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_100***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_100_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_100_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_100_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_and_expiration_date_range_criteria(self):
        try:
            self.logger.info("*********TC_101********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_101***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_101_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_101_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_101_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_expiration_date_range_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_102********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            self.verify_sort_key_case_subject()
            # self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_102******* end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_102_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_102_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_102_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_expiration_date_range_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_103********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_103***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_103_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_103_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_103_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_expiration_date_range_sort_by_enrolledOn_criteria(self):
        try:
            self.logger.info("*********TC_104********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("there are no matching enrollments for current search")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_104***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_104_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_104_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_104_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_Enrollment_date_range_criteria_criteria(self):
        try:
            self.logger.info("*********TC_105********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("There are no matching enrollments for current search")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_105***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_105_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_105_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_105_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_Enrollment_date_range_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_106********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("There are no matching enrollments for current search")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_106***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_106_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_106_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_106_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_Enrollment_date_range_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_107********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("There are no matching enrollments for current search")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_107***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_107_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_107_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_107_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_Enrollment_date_range_sort_by_enrolledOn_criteria(self):
        try:
            self.logger.info("*********TC_108********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("There are no matching enrollments for current search")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_108***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_108_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_108_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_108_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_EnrollmentDateRange_expiration_date_range_criteria(self):
        try:
            self.logger.info("*********TC_109********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("There are no matching enrollments for current search")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_109***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_109_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_109_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_109_Exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_EnrollmentDateRange_expiration_date_range_sort_by_case_subject_criteria(
            self):
        try:
            self.logger.info("*********TC_110********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("There are no matching enrollments for current search")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_110***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_110_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_110_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_110_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_EnrollmentDateRange_expiration_date_range_sort_by_location_store_criteria(
            self):
        try:
            self.logger.info("*********TC_111********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("There are no matching enrollments for current search")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_061***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_111_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_111_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_111_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_EnrollmentDateRange_expiration_date_range_sort_by_enrolledOn_criteria(
            self):
        try:
            self.logger.info("*********TC_112********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("There are no matching enrollments for current search")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_112***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_112_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_112_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_112_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_exact_text_search_criteria(self):
        try:
            self.logger.info("*********TC_113********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("There are no matching enrollments for current search")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_113***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_113_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_113_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_113_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_exact_text_search_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_114********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(web_driver.two_second)

            if not self.verify_if_match_found():
                self.logger.info("'there are no matching enrollments for current search' message is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_114***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_114_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_114_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_114_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_exact_text_search_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_115********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_115***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_115_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_115_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_115_Exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_exact_text_search_sort_by_enrolledOn_criteria(self):
        try:
            self.logger.info("*********TC_116********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_116***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_116_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_116_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_116_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_exact_text_search_expiration_date_range_criteria(self):
        try:
            self.logger.info("*********TC_117********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_117***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_117_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_117_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_117_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_exact_text_search_expiration_date_range_sort_by_case_subject_criteria(
            self):
        try:
            self.logger.info("*********TC_118********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_118***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_118_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_118_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_118_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_exact_text_search_expiration_date_range_sort_by_location_store_criteria(
            self):
        try:
            self.logger.info("*********TC_120********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search'")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_120***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_120_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_120_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_120_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollments_search_with_location_store_case_subject_exact_text_search_expiration_date_range_sort_by_enrolledOn_criteria(
            self):
        try:
            self.logger.info("*********TC_119********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_119***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_119_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_119_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_119_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_exact_text_enrollment_date_range_and_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_027********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.two_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.two_second)
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.select_sort_by_location_or_store()
            time.sleep(web_driver.two_second)
            self.click_on_search_button()

            time.sleep(web_driver.one_second)
            var1 = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var1)
            var2 = self.verify_sort_key_location_store()
            self.status.append(var2)
            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_027***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_027_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_027_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_027_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_exact_text_enrollment_date_range_and_sort_by_enrolled_on_criteria(self):
        try:
            self.logger.info("*********TC_028********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.two_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.two_second)
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.select_sort_by_enrolled_on()
            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var1 = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var1)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_028***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_028_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_028_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_028_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_exact_text_enrollment_date_and_expiration_date_range_criteria(self):
        try:
            self.logger.info("*********TC_029********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.select_sort_by_enrolled_on()

            self.click_on_search_button()

            time.sleep(web_driver.one_second)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_029***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_029_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_029_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_029_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_exact_text_enrollment_expiration_date_range_and_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_030********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()

            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.two_second)
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            time.sleep(web_driver.one_second)
            self.handle_enrollment_start_or_end_date_calender("to")
            time.sleep(web_driver.one_second)
            self.handle_expiration_start_or_end_date_calender("from")
            time.sleep(web_driver.one_second)
            self.handle_expiration_start_or_end_date_calender("to")
            time.sleep(web_driver.one_second)
            self.select_sort_by_case_or_subject()
            time.sleep(web_driver.two_second)
            self.click_on_search_button()

            time.sleep(web_driver.three_second)
            var1 = self.verify_sort_key_case_subject()
            self.status.append(var1)
            var2 = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var2)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var3)

            time.sleep(web_driver.three_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_030***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_030_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_030_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_030_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_exact_text_enrollment_expiration_date_range_and_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_031********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.verify_sort_key_location_store()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)
            self.logger.info(f"status1: {self.status}")
            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                self.logger.info("match list found")
                var = self.validate_match_list_output(4)
                self.status.append(var)
                self.logger.info(f"match list: {var}")
            else:

                self.status.append(False)
            self.logger.info(f"status2 is {self.status}")
            self.logger.info("*******TC_031***** end")
            self.close_all_panel_one_by_one()

            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_031_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_031_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_031_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_exact_text_enrollment_expiration_date_range_and_sort_by_enrolled_on_criteria(self):
        try:
            self.logger.info("*********TC_032********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_032***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_032_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_032_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_032_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_033********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_case_subject()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_033***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_033_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_033_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_033_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_and_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_034********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.select_sort_by_case_or_subject()
            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.verify_sort_key_case_subject()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_034***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_034_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_034_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_034_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_and_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_035********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.enter_case_subject()
            self.select_sort_by_location_or_store()
            self.click_on_search_button()
            time.sleep(web_driver.two_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_035***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_035_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_035_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_035_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_and_sort_by_enrolled_on_criteria(self):
        try:
            self.logger.info("*********TC_036********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.enter_case_subject()
            self.select_sort_by_enrolled_on()
            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_036***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_036_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_036_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_036_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_and_expiration_date_range_criteria(self):
        try:
            self.logger.info("*********TC_037********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()

            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()
            time.sleep(web_driver.one_second)
            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_037***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_037_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_037_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_037_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_expiration_date_range_and_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_038********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()

            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()
            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            print(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            print(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)
            print(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
                print(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_038***** end")
            print(self.status)
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_038_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_038_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_038_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_expiration_date_range_and_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_039********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()
            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.verify_sort_key_location_store()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_039***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_039_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_039_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_039_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_expiration_date_range_and_sort_by_enrolled_on_criteria(self):
        try:
            self.logger.info("*********TC_040********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)

            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()
            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_040***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_040_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_040_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_040_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_and_enrollment_date_range_criteria(self):
        try:
            self.logger.info("*********TC_041********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            print(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            print(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
                print(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_041***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_041_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_041_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_041_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_enrollment_date_range_and_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_042********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.two_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_042***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_042_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_042_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_042_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_enrollment_date_range_and_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_043********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.verify_sort_key_location_store()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_043***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_043_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_043_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_043_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_enrollment_date_range_and_sort_by_enrolled_on_criteria(self):
        try:
            self.logger.info("*********TC_044********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_044***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_044_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_044_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_044_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_enrollment_date_and_expiration_date_range_criteria(self):
        try:
            self.logger.info("*********TC_045********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_089***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_045_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_045_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_045_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_enrollment_expiration_date_range_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_046********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_046***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_046_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_046_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_046_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_enrollment_expiration_date_range_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_047********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.verify_sort_key_location_store()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_047***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_047_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_047_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_047_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_enrollment_expiration_date_range_sort_by_enrolled_on_criteria(self):
        try:
            self.logger.info("*********TC_048********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_048***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_048_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_048_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_048_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_and_exact_text_criteria(self):
        try:
            self.logger.info("*********TC_049********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_049***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_049_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_049_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_049_Exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_exact_text_and_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_050********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_050***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_050_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_050_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_050_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_exact_text_and_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_051********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.verify_sort_key_location_store()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_051***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_051_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_051_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_051_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_exact_text_and_sort_by_enrolled_on_criteria(self):
        try:
            self.logger.info("*********TC_052********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_052***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_052_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_052_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_052_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_exact_text_and_expiration_date_range_criteria(self):
        try:
            self.logger.info("*********TC_053********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_053***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_053_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_053_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_053_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_exact_text_expiration_date_range_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_054********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_054***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_054_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_054_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_054_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_exact_text_expiration_date_range_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_055********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.verify_sort_key_location_store()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_055***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_055_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_055_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_055_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_exact_text_expiration_date_range_sort_by_enrolled_on_criteria(self):
        try:
            self.logger.info("*********TC_056********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_056***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_056_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_056_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_056_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_exact_text_and_enrollment_date_range_criteria(self):
        try:
            self.logger.info("*********TC_057********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_057***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_057_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_057_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_057_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_exact_text_enrollment_date_range_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_058********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_058***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_058_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_058_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_058_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_exact_text_enrollment_date_range_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_059********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.verify_sort_key_location_store()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_059***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_059_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_059_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_059_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_exact_text_enrollment_date_range_sort_by_enrolled_on_criteria(self):
        try:
            self.logger.info("*********TC_060********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_060***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_060_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_060_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_060_Exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_exact_text_enrollment_expiration_date_range_criteria(self):
        try:
            self.logger.info("*********TC_061********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_061***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_061_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_061_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_061_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_exact_text_enrollment_expiration_date_range_sort_case_criteria(self):
        try:
            self.logger.info("*********TC_106********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_106***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_106_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_106_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_106_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_exact_text_enrollment_expiration_date_range_sort_store_criteria(self):
        try:
            self.logger.info("*********TC_107********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.verify_sort_key_location_store()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_107***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_107_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_107_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_107_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_case_subject_exact_text_enrollment_expiration_date_range_sort_enrolled_criteria(self):
        try:
            self.logger.info("*********TC_064********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_064***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_064_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_064_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_064_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_criteria(self):
        try:
            self.logger.info("*********TC_065********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_065***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_065_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_065_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_065_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_and_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_066********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.verify_sort_key_case_subject()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_066***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_066_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_066_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_066_Exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_and_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_067********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_067***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_067_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_067_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_067_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_and_sort_by_enrolled_on_criteria(self):
        try:
            self.logger.info("*********TC_068********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(web_driver.two_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)

            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_068***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_068_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_068_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_068_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_and_expiration_date_range_criteria(self):
        try:
            self.logger.info("*********TC_069********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_069***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_069_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_069_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_069_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_expiration_date_range_and_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_070********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)
            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_070***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_070_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_070_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_070_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_expiration_date_range_and_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_071********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)
            if self.verify_sort_key_location_store():
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_071***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_071_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_071_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_071_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_expiration_date_range_and_sort_by_enrolled_on_criteria(self):
        try:
            self.logger.info("*********TC_072********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_072***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_072_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_072_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_072_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_and_enrollment_date_range_criteria(self):
        try:
            self.logger.info("*********TC_073********* started")
            login().login_to_cloud_if_not_done(self.d)
            # ogin().login_to_localhost_if_not_done()
            time.sleep(web_driver.one_second)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_073***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_073_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_073_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_073_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_enrollment_date_range_and_sort_by_case_subject_criteria(self):
        try:
            self.logger.info("*********TC_074********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_074***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_074_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_074_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_074_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_enrollment_date_range_and_sort_by_location_store_criteria(self):
        try:
            self.logger.info("*********TC_075********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_075***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_075_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_075_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_075_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_enrollment_date_range_and_sort_by_enrolled_on_criteria(self):
        try:
            self.logger.info("*********TC_076********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search; is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_076***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_076_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_076_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_076_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_date_range_criteria(self):
        try:
            self.logger.info("*********TC_121********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_121***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_121_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_121_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_121_exception.png")
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_date_range_sort_case_criteria(self):
        try:
            self.logger.info("*********TC_122********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            if self.verify_sort_key_case_subject():
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search filter' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_122***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_122_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_122_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_122_exception.png")
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_date_sort_by_store_criteria(self):
        try:
            self.logger.info("*********TC_123********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)
            time.sleep(web_driver.one_second)

            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_123***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_123_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_123_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_123_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_date_sort_enrolled_criteria(self):
        try:
            self.logger.info("*********TC_124********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(web_driver.two_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)

            time.sleep(web_driver.two_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_124***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_124_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_124_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_124_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_expiration_date_criteria(self):
        try:
            self.logger.info("*********TC_125********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_125***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_125_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_125_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_125_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_expiration_date_sort_by_case_criteria(
            self):
        try:
            self.logger.info("*********TC_126********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_case_or_subject()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            var = self.verify_sort_key_case_subject()
            self.status.append(var)
            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_126***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_126_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_126_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_126_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_expiration_date_sort_by_store_criteria(
            self):
        try:
            self.logger.info("*********TC_127********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_location_or_store()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)
            var = self.verify_sort_key_location_store()
            self.status.append(var)
            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_127***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_127_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_127_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_127_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    def enrollment_search_with_location_store_case_subject_exact_text_enrollment_expiration_date_sort_by_enrolled_on_criteria(
            self):
        try:
            self.logger.info("*********TC_128********* started")
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done()
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.click_on_enrollments_link()
            time.sleep(web_driver.one_second)
            self.click_on_search_dropdown()

            self.enter_location_or_store()
            self.enter_case_subject()
            self.click_on_exact_text_search_checkBox()
            self.handle_enrollment_start_or_end_date_calender("from")
            self.handle_enrollment_start_or_end_date_calender("to")
            self.handle_expiration_start_or_end_date_calender("from")
            self.handle_expiration_start_or_end_date_calender("to")
            self.select_sort_by_enrolled_on()

            self.click_on_search_button()
            time.sleep(web_driver.one_second)

            var = self.validate_location_store_search_criteria_result()
            self.status.append(var)
            var = self.validate_case_subject_search_criteria_result()
            self.status.append(var)
            var = self.validate_enrolled_start_or_end_date_search_result()
            self.status.append(var)
            self.validate_expiration_start_or_end_date_search_result()
            # self.status.append(var)

            time.sleep(web_driver.one_second)
            if not self.verify_if_match_found():
                self.logger.info("'There are no matching enrollments for current search' is visible")
                self.status.append(True)
            elif self.verify_if_match_found():
                var = self.validate_match_list_output(4)
                self.status.append(var)
            else:
                self.status.append(False)
            self.logger.info(f"status is {self.status}")
            self.logger.info("*******TC_128***** end")
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_enrollments_128_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_enrollments_128_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\TC_enrollments_128_exception.png")
                return False
        # finally:
        #     self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()

    ####################################### REUSABLE METHODS ###############################################

    def click_on_enrollments_link(self):
        self.logger.info("started click_on_enrollments_link")
        ele = self.d.find_elements(By.XPATH, Read_Enrollments_Components().enrollments_link_by_xpath())
        self.logger.info("clicked on enrollments link")
        enrollments_link = Read_Enrollments_Components().search_drop_down_by_xpath()
        ele = self.wait_for_element_to_appear(ele, enrollments_link)
        self.logger.info("clicking on search dropdown")
        ele.click()
        time.sleep(web_driver.one_second)

    def click_on_search_dropdown(self):
        ele = self.d.find_elements(By.XPATH, Read_Enrollments_Components().search_drop_down_by_xpath())
        search_dd_xpath = Read_Enrollments_Components().search_drop_down_by_xpath()
        ele = self.wait_for_element_to_appear(ele, search_dd_xpath)
        self.logger.info("clicking on search dropdown")
        ele.click()
        time.sleep(web_driver.one_second)

    def enter_location_or_store(self):
        location_store_data = Read_Enrollments_Components().location_store_data_input()
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().location_store_txt_bx_by_xpath())
        ele.send_keys(location_store_data)
        time.sleep(web_driver.one_second)

    def enter_case_subject(self):
        case_subject_data = Read_Enrollments_Components().case_subject_data_input()
        self.logger.info(f"case subject data: {case_subject_data}")
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().case_subject_txt_bx_by_xpath())
        self.logger.info(f"ele is visible: {ele.is_displayed()}")
        ele.send_keys(case_subject_data)
        time.sleep(web_driver.one_second)

    def click_on_exact_text_search_checkBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().exact_text_search_check_bx_by_xpath())
        ele.click()

    def click_on_enrollment_start_date_checkBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().enrollment_start_date_check_bx_by_xpath())
        ele.click()

    def click_on_enrollment_end_date_checkBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().enrollment_end_date_check_bx_by_xpath())
        ele.click()

    def click_on_expiration_start_date_checkBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().expiration_start_date_check_bx_by_xpath())
        ele.click()

    def click_on_expiration_end_date_checkBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().expiration_end_date_check_bx_by_xpath())
        ele.click()

    def click_on_enrollment_start_date_inputBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().enrollment_start_date_input_bx_by_xpath())
        ele.click()

    def click_on_enrollment_end_date_inputBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().enrollment_end_date_input_bx_by_xpath())
        ele.click()

    def click_on_expiration_start_date_inputBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().expiration_start_date_input_bx_by_xpath())
        ele.click()

    def click_on_expiration_end_date_inputBox(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().expiration_end_date_input_bx_by_xpath())
        ele.click()

    def select_sort_by_enrolled_on(self):

        visible_text_data = Read_Enrollments_Components().sort_by_data_input_Enrolled_On()
        ele = self.explicit_wait(10, "XPATH", Read_Enrollments_Components().sort_by_by_xpath(), self.d)
        s = Select(ele)
        s.select_by_visible_text(visible_text_data)
        time.sleep(web_driver.one_second)

    def select_sort_by_case_or_subject(self):
        visible_text_data = Read_Enrollments_Components().sort_by_data_input_CASE_SUBJECT()
        self.logger.info(f"visible text data is {visible_text_data}")
        ele = self.explicit_wait(10, "XPATH", Read_Enrollments_Components().sort_by_by_xpath(), self.d)
        self.logger.info(f"ele visible: {ele.is_displayed()}")
        s = Select(ele)
        print(s)
        s.select_by_visible_text(visible_text_data)

    def select_sort_by_location_or_store(self):
        visible_text_data = Read_Enrollments_Components().sort_by_data_input_LOCATION_STORE()
        self.logger.info(f"visible text data is {visible_text_data}")

        ele = self.explicit_wait(10, "XPATH", Read_Enrollments_Components().sort_by_by_xpath(), self.d)
        s = Select(ele)
        s.select_by_visible_text(visible_text_data)

    def click_on_clear_btn(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().clear_btn_by_xpath())
        ele.click()

    def click_on_search_button(self):
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().search_btn_by_xpath())
        self.logger.info("clicking on search button")
        ele.click()
        time.sleep(web_driver.one_second)

    def validate_location_store_search_criteria_result(self):
        location_store_data = Read_Enrollments_Components().location_store_data_input()
        self.logger.info((f"location store data is {location_store_data}"))
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().location_store_filter_result_by_xpath())
        self.logger.info(ele.text)
        print("Expected data = " + location_store_data)
        print("Actual data = " + ele.text)
        if location_store_data.lower() in ele.text.lower():
            return True
        else:
            return False

    def validate_case_subject_search_criteria_result(self):

        case_subject_data = Read_Enrollments_Components().case_subject_data_input()
        self.logger.info(f"expected case_subject data is {case_subject_data}")
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().case_subject_filter_result_by_xpath())
        self.logger.info(f"actual text is {ele.text}")
        print("Expected data = ", case_subject_data)
        print("Actual data = ", ele.text)
        if case_subject_data.lower() in ele.text.lower():
            return True
        else:
            return False

    def validate_enrolled_start_or_end_date_search_result(self):
        month_to_num = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }

        date = int(Read_Enrollments_Components().enroll_get_start_date())
        print("enroll satart date is ", date)
        month = str(Read_Enrollments_Components().enroll_get_start_month())
        print("enroll start month is ", month)
        year = int(Read_Enrollments_Components().enroll_get_start_year())
        print("enroll start year is ", year)
        hour = str(Read_Enrollments_Components().enroll_get_start_hour())
        print("enroll start hour is ", hour)
        minute = int(Read_Enrollments_Components().enroll_get_start_minuet())
        print("enroll start minute is ", minute)
        req_period = str(Read_Enrollments_Components().enroll_get_start_am_pm_period())
        print("enroll pm or am is", req_period)
        mon = month_to_num.get(month)

        if 1 <= date <= 9:
            date = "0" + str(date)
        if 1 <= mon <= 9:
            mon = "0" + str(mon)
        if minute == 0:
            minute = "00"

        exp_asser1 = "{mon}/{date}/{year} {hour}:{min} {pe}"
        print(exp_asser1)
        exp_asser1 = exp_asser1.format(mon=mon, date=date, year=year, hour=int(hour), min=minute, pe=req_period)
        print(exp_asser1)

        date = int(Read_Enrollments_Components().enroll_get_end_date())
        print("enroll end date is ", date)
        month = str(Read_Enrollments_Components().enroll_get_end_month())
        print("enroll end month is", month)
        year = int(Read_Enrollments_Components().enroll_get_end_year())
        print("enroll end year is", year)
        hour = str(Read_Enrollments_Components().enroll_get_end_hour())
        print("enroll end hour is ", hour)
        minute = int(Read_Enrollments_Components().enroll_get_end_minuet())
        print("enroll end minute", minute)
        req_period = str(Read_Enrollments_Components().enroll_get_end_am_pm_period())
        print("enroll req period is ", req_period)
        mon = month_to_num.get(month)

        if 1 <= date <= 9:
            date = "0" + str(date)
        if 1 <= mon <= 9:
            mon = "0" + str(mon)
        if minute == 0:
            minute = "00"
        exp_asser2 = "{mon}/{date}/{year} {hour}:{min} {pe}"
        exp_asser2 = exp_asser2.format(mon=mon, date=date, year=year, hour=int(hour), min=minute, pe=req_period)
        print("date format: ", exp_asser2)

        time.sleep(1)
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().enrolled_filter_result_by_xpath())
        if exp_asser1 in ele.text and exp_asser2 in ele.text:
            return True
        else:
            return False

    def validate_expiration_start_or_end_date_search_result(self):
        month_to_num = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }

        date = int(Read_Enrollments_Components().expiration_get_start_date())
        print(date)
        month = str(Read_Enrollments_Components().expiration_get_start_month())
        print(month)
        year = int(Read_Enrollments_Components().expiration_get_start_year())
        print(year)
        hour = str(Read_Enrollments_Components().expiration_get_start_hour())
        print(hour)
        minute = int(Read_Enrollments_Components().expiration_get_start_minuet())
        print(minute)
        req_period = str(Read_Enrollments_Components().expiration_get_start_am_pm_period())
        print(req_period)
        mon = month_to_num.get(month)

        if 1 <= date <= 9:
            date = "0" + str(date)
        if 1 <= mon <= 9:
            mon = "0" + str(mon)
        if minute == 0:
            minute = "00"

        exp_asser1 = "{mon}/{date}/{year} {hour}:{minu} {pe}"
        exp_asser1 = exp_asser1.format(mon=mon, date=date, year=year, hour=int(hour), minu=minute, pe=req_period)
        print("date format: ", exp_asser1)

        date = int(Read_Enrollments_Components().expiration_get_end_date())
        print("input date is ", date)
        month = str(Read_Enrollments_Components().expiration_get_end_month())
        print("input month is ", month)
        year = int(Read_Enrollments_Components().expiration_get_end_year())
        print("input year is ", year)
        hour = str(Read_Enrollments_Components().expiration_get_end_hour())
        print("input hour is ", hour)
        minute = int(Read_Enrollments_Components().expiration_get_end_minuet())
        print("input hour is ", minute)
        req_period = str(Read_Enrollments_Components().expiration_get_end_am_pm_period())
        print("input req-period is", req_period)
        mon = month_to_num.get(month)

        if 1 <= date <= 9:
            date = "0" + str(date)
        if 1 <= mon <= 9:
            mon = "0" + str(mon)
        if minute == 0:
            minute = "00"
        exp_asser2 = "{mon}/{date}/{year} {hour}:{minu} {pe}"
        exp_asser2 = exp_asser2.format(mon=mon, date=date, year=year, hour=int(hour), minu=minute, pe=req_period)
        print("date format: ", exp_asser2)

        time.sleep(1)
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().expiration_filter_result_by_xpath())
        self.logger.info(f"ele text is {ele.text}")
        print(ele.text)
        self.logger.info(f"Expected data = {exp_asser1}")
        self.logger.info(f"Actual data = {ele.text}")
        self.logger.info(f"Expected data = {exp_asser2}")
        self.logger.info(f"Actual data = {ele.text}")
        if exp_asser1 in ele.text and exp_asser2 in ele.text:
            return True
        else:
            return False

    def handle_enrollment_start_or_end_date_calender(self, strategy):
        # click on the form calendar popup
        if strategy == "from":
            date = int(Read_Enrollments_Components().enroll_get_start_date())
            print(date)
            month = str(Read_Enrollments_Components().enroll_get_start_month())
            print(month)
            year = int(Read_Enrollments_Components().enroll_get_start_year())
            print(year)
            hour = str(Read_Enrollments_Components().enroll_get_start_hour())
            print(hour)
            minute = int(Read_Enrollments_Components().enroll_get_start_minuet())
            print(minute)
            req_period = str(Read_Enrollments_Components().enroll_get_start_am_pm_period())
            print(req_period)
            self.click_on_enrollment_start_date_checkBox()
            self.click_on_enrollment_start_date_inputBox()
        else:
            date = int(Read_Enrollments_Components().enroll_get_end_date())
            print(date)
            month = str(Read_Enrollments_Components().enroll_get_end_month())
            print(month)
            year = int(Read_Enrollments_Components().enroll_get_end_year())
            print(year)
            hour = str(Read_Enrollments_Components().enroll_get_end_hour())
            print(hour)
            minute = int(Read_Enrollments_Components().enroll_get_end_minuet())
            print(minute)
            req_period = str(Read_Enrollments_Components().enroll_get_end_am_pm_period())
            print(req_period)
            # click on calendar pop up
            self.click_on_enrollment_end_date_checkBox()
            self.click_on_enrollment_end_date_inputBox()

        # click on the clock icon
        calender_clock = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_timer_icon_by_xpath())
        self.logger.info("clicking on calender clock")
        calender_clock.click()

        time.sleep(web_driver.two_second)

        # handle the hour and minute based on the strategy
        if strategy == "from":
            self.calender_handle_hour_minute_from(hour, minute)
        else:
            self.calender_handle_hour_minute_to(hour, minute)

        # select the period am or pm
        period = self.d.find_element(By.XPATH, Read_Enrollments_Components().period_by_xpath())
        if period.text == req_period:
            print("")
        else:
            period.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_tick_icon_by_xpath())
        self.logger.info("clicking on tick icon")
        tick_icon.click()

        if strategy == "from":
            self.click_on_enrollment_start_date_inputBox()
        else:
            # click on calendar pop up
            self.click_on_enrollment_end_date_inputBox()

        req_month = month
        req_year = year
        month_to_num = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        month_year = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_month_year_by_xpath())
        ac_month = month_year.text.split(" ")[0]
        ac_year = int(month_year.text.split(" ")[1])

        # click on the back button
        while month_to_num.get(req_month) < month_to_num.get(ac_month) or req_year < ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  Read_Enrollments_Components().calender_back_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()
            time.sleep(web_driver.two_second)
            month_year = self.d.find_element(By.XPATH,
                                             Read_Enrollments_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the forward button
        while month_to_num.get(req_month) > month_to_num.get(ac_month) or req_year > ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  Read_Enrollments_Components().calender_forward_button_by_xpath())
            if cal_back_button.is_enabled():
                cal_back_button.click()
            time.sleep(web_driver.two_second)
            month_year = self.d.find_element(By.XPATH,
                                             Read_Enrollments_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the required date
        # date = self.d.find_element(By.XPATH,"(//td[@class='day' or @class='day weekend' or @class='day active' "
        #                            "or @class='day active today'])[" + str(date) + "]")

        date = self.d.find_element(By.XPATH, f"//td[contains(@class, 'day') and text()='{date}']")

        date.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_tick_icon_by_xpath())
        tick_icon.click()

    def handle_expiration_start_or_end_date_calender(self, strategy):
        # click on the form calendar popup
        if strategy == "from":
            date = int(Read_Enrollments_Components().expiration_get_start_date())
            month = str(Read_Enrollments_Components().expiration_get_start_month())
            year = int(Read_Enrollments_Components().expiration_get_start_year())
            hour = str(Read_Enrollments_Components().expiration_get_start_hour())
            minute = int(Read_Enrollments_Components().expiration_get_start_minuet())
            req_period = str(Read_Enrollments_Components().expiration_get_start_am_pm_period())
            self.click_on_expiration_start_date_checkBox()
            self.click_on_expiration_start_date_inputBox()
        else:
            date = int(Read_Enrollments_Components().expiration_get_end_date())
            month = str(Read_Enrollments_Components().expiration_get_end_month())
            year = int(Read_Enrollments_Components().expiration_get_end_year())
            hour = str(Read_Enrollments_Components().expiration_get_end_hour())
            minute = int(Read_Enrollments_Components().expiration_get_end_minuet())
            req_period = str(Read_Enrollments_Components().expiration_get_end_am_pm_period())
            # click on calendar pop up
            self.click_on_expiration_end_date_checkBox()
            self.click_on_expiration_end_date_inputBox()

        # click on the clock icon
        calender_clock = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_timer_icon_by_xpath())
        calender_clock.click()

        time.sleep(web_driver.two_second)

        # handle the hour and minute based on the strategy
        if strategy == "from":
            self.calender_handle_hour_minute_from(hour, minute)
        else:
            self.calender_handle_hour_minute_to(hour, minute)

        # select the period am or pm
        period = self.d.find_element(By.XPATH, Read_Enrollments_Components().period_by_xpath())
        if period.text == req_period:
            print("")
        else:
            period.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_tick_icon_by_xpath())
        tick_icon.click()

        if strategy == "from":
            self.click_on_expiration_start_date_inputBox()
        else:
            # click on calendar pop up
            self.click_on_expiration_end_date_inputBox()

        req_month = month
        req_year = year
        month_to_num = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        month_year = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_month_year_by_xpath())
        ac_month = month_year.text.split(" ")[0]
        ac_year = int(month_year.text.split(" ")[1])

        # click on the back button
        while month_to_num.get(req_month) < month_to_num.get(ac_month) or req_year < ac_year:
            cal_back_button = self.d.find_element(By.XPATH,
                                                  Read_Enrollments_Components().calender_back_button_by_xpath())
            # if cal_back_button.is_enabled():
            #     cal_back_button.click()

            self.d.execute_script("arguments[0].click();", cal_back_button)
            time.sleep(web_driver.one_second)
            month_year = self.d.find_element(By.XPATH,
                                             Read_Enrollments_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the forward button
        while month_to_num.get(req_month) > month_to_num.get(ac_month) or req_year > ac_year:
            next_button = self.d.find_element(By.XPATH,
                                              Read_Enrollments_Components().calender_forward_button_by_xpath())
            # if next_button.is_enabled():
            #     next_button.click()

            self.d.execute_script("arguments[0].click();", next_button)
            time.sleep(web_driver.one_second)

            month_year = self.d.find_element(By.XPATH,
                                             Read_Enrollments_Components().calender_month_year_by_xpath())
            ac_month = month_year.text.split(" ")[0]
            ac_year = int(month_year.text.split(" ")[1])

        # click on the required date
        date = self.d.find_element(By.XPATH,
                                   "(//td[@class='day' or @class='day weekend' or @class='day active' "
                                   "or @class='day active today'])[" + str(date) + "]")
        date.click()

        # click on the tick icon
        tick_icon = self.d.find_element(By.XPATH, Read_Enrollments_Components().calender_tick_icon_by_xpath())
        # tick_icon.click()
        self.d.execute_script("arguments[0].click();", tick_icon)

    def calender_handle_hour_minute_to(self, hour, minute):
        # set the minute
        current_min_ele = self.d.find_element(By.XPATH,
                                              Read_Enrollments_Components().current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)
        if int(minute) > int(cur_min):
            while int(cur_min) != int(minute):
                clock_up_button = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                      .clock_min_up_button_by_xpath())
                clock_up_button.click()
                current_min_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                      .current_minute_element_by_xpath())
                cur_min = int(current_min_ele.text)
        else:
            while int(cur_min) != int(minute):
                clock_down_button = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                        .clock_min_down_button_by_xpath())
                clock_down_button.click()
                current_min_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                      .current_minute_element_by_xpath())
                cur_min = int(current_min_ele.text)

        time.sleep(web_driver.two_second)

        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, Read_Enrollments_Components().hour_down_by_xpath())
            hour_down.click()
            current_hour_ele = self.d.find_element(By.XPATH,
                                                   Read_Enrollments_Components().current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

    def calender_handle_hour_minute_from(self, hour, minute):

        # set the minute
        current_min_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                              .current_minute_element_by_xpath())
        cur_min = int(current_min_ele.text)

        if int(minute) > int(cur_min):
            while int(cur_min) != int(minute):
                clock_up_button = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                      .clock_min_up_button_by_xpath())
                clock_up_button.click()
                current_min_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                      .current_minute_element_by_xpath())
                cur_min = int(current_min_ele.text)
        else:
            while int(cur_min) != int(minute):
                clock_down_button = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                        .clock_min_down_button_by_xpath())
                clock_down_button.click()
                current_min_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                      .current_minute_element_by_xpath())
                cur_min = int(current_min_ele.text)

        time.sleep(web_driver.two_second)
        # set the hour
        current_hour_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().current_hour_ele_by_xpath())
        cur_hour = int(current_hour_ele.text)

        # decrementHours
        while int(cur_hour) != int(hour):
            hour_down = self.d.find_element(By.XPATH, Read_Enrollments_Components().hour_down_by_xpath())
            hour_down.click()
            current_hour_ele = self.d.find_element(By.XPATH, Read_Enrollments_Components()
                                                   .current_hour_ele_by_xpath())
            cur_hour = int(current_hour_ele.text)

    def verify_if_match_found(self):
        self.logger.info(f"function: verify_if_match_found")
        self.explicit_wait(10, "XPATH", Read_Enrollments_Components().no_match_search_filter_message(), self.d)
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().no_match_search_filter_message())
        if ele.is_displayed():
            self.logger.info(f"match list displayed: {ele.is_displayed()}, Returning False")
            return False
        else:
            self.logger.info(f"match list displayed: {ele.is_displayed()}, Returning True")
            return True

    def validate_enrolled_on_is_displayed_from_the_match_list(self):
        result = False
        self.logger.info(f"function: validate_enrolled_on_is_displayed_from_the_match_list()")
        self.logger.info("matches are found...")
        match_found_list_enrolled = self.d.find_elements(By.XPATH, Read_Enrollments_Components()
                                                         .match_list_enrolled_output())
        for ele in match_found_list_enrolled:
            self.logger.info("no matches are found...")
            if ele.is_displayed():
                result = True
            else:
                result = False
        self.logger.info(f"returning {result} from validate_enrolled_on_is_displayed_from_the_match_list")
        return result

    def validate_location_store_case_subject_from_match_list(self):
        result = True
        location_store_data = Read_Enrollments_Components().location_store_data_input()
        case_subject_data = Read_Enrollments_Components().case_subject_data_input()

        print(location_store_data, case_subject_data)
        match_found_list_location_store_case_subject = self.d \
            .find_elements(By.XPATH,
                           Read_Enrollments_Components().match_list_location_store_case_subject_output())
        for ele in match_found_list_location_store_case_subject:
            if not location_store_data and case_subject_data in ele.text:
                self.logger.info("location/store and case/subject")
                result = False
            else:
                result = True
        return result

    def validate_action_is_displayed_from_the_match_list(self):
        result = True
        time.sleep(web_driver.two_second)
        match_found_list_action = self.d.find_elements(By.XPATH, Read_Enrollments_Components().match_list_action_output())
        for ele in match_found_list_action:
            if not ele.is_displayed():
                self.logger.info("no matches are found...")
                result = False
            else:
                result = True
        return result

    def validate_match_list_output(self, choice):
        """
        This function is used to validate the search filters criteria applied, from the list of enrollments matches
        \n choice 1 : validate enrolled on is displayed from match list
        \n choice 2 : validate location/store ,case/subject from match list
        \n choice 3 : validate action is displayed from the match list
        \n choice 4 : validate all search criteria from the match list

        :param choice:
        :return:
        """
        self.logger.info(f"function : validate_match_list_output")
        result = result1 = result2 = None
        status = []
        photo = self.d.find_element(By.XPATH, Read_Enrollments_Components().match_list_image_by_xpath())

        while not photo.is_displayed():
            time.sleep(web_driver.one_second)

        if self.validate_enrolled_on_is_displayed_from_the_match_list():
            self.logger.info(f"function: validate_enrolled_on_is_displayed_from_the_match_list(): True")
            status.append(True)
        else:
            self.logger.info(f"function: validate_enrolled_on_is_displayed_from_the_match_list(): Fale")
            status.append(False)
        if self.validate_location_store_case_subject_from_match_list():
            status.append(True)
        else:
            status.append(False)
        if self.validate_action_is_displayed_from_the_match_list():
            status.append(True)
        else:
            status.append(False)

        self.logger.info(f"staus: {status}")
        print(f"status inside method : {status}")
        # match int(choice):
        #     case 1:
        #         result = self.validate_enrolled_on_is_displayed_from_the_match_list()
        #
        #     case 2:
        #         result = self.validate_location_store_case_subject_from_match_list()
        #
        #     case 3:
        #         result = self.validate_action_is_displayed_from_the_match_list()
        #
        #     case 4:
        #         result = self.validate_enrolled_on_is_displayed_from_the_match_list()
        #
        #         result1 = self.validate_location_store_case_subject_from_match_list()
        #
        #         result2 = self.validate_action_is_displayed_from_the_match_list()
        #     case _:
        #         print("invalid input provided")
        #         result =  False

        if status == [True, True, True]:
            return True
        else:
            return False

    def verify_sort_key_location_store(self):
        data = Read_Enrollments_Components().sort_by_data_input_LOCATION_STORE()
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().sort_key_by_xpath())
        print("Expected data = " + data)
        print("Actual data = " + ele.text)
        if data in ele.text:
            return True
        else:
            return False

    def verify_sort_key_case_subject(self):
        data = Read_Enrollments_Components().sort_by_data_input_CASE_SUBJECT()
        ele = self.d.find_element(By.XPATH, Read_Enrollments_Components().sort_key_by_xpath())
        print("Expected data = ", data)
        print("Actual data = ", ele.text)
        if data.lower() in ele.text.lower():
            return True
        else:
            return False

    def close_all_panel_one_by_one(self):
        self.logger.info("function: close_all_panel_one_by_one")
        time.sleep(web_driver.one_second)
        try:
            close_panel_list = self.d.find_elements(By.XPATH,
                                                    Read_Enrollments_Components().close_panel_one_by_one_list())
            for i in close_panel_list:
                time.sleep(web_driver.two_second)
                i.click()
                time.sleep(web_driver.two_second)
                self.logger.info("function close_all_panel_one_by_one returning true")
            return True

        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\close_all_panel_failed_pg_03.png")
                return False

    '''
    def click_on_logout_button(self):
        try:
            time.sleep(web_driver.one_second)
            logout_button = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().logout_btn_by_xpath())
            while not logout_button.is_displayed():
                time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            try:
                self.d.execute_script("arguments[0].click();", logout_button)
            except Exception as ex:
                logout_button.click()
            time.sleep(web_driver.one_second)
            self.d.delete_cookie()
        except Exception as ex:
            msg = str(ex)
            if msg.__contains__('not clickable at point'):
                print("Exception crated: ", ex, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_logout_pg_03.png")
                return False
    '''

    def load_login_page_if_not_loaded(self):
        try:
            self.d.get(Read_Enrollments_Components().get_Launching_url())
            expected_url = Read_Enrollments_Components().get_Launching_url()
            time.sleep(web_driver.one_second)
            self.d.maximize_window()
            actual_url = self.d.current_url
            print(f"actual: {actual_url},\nexpected: {expected_url}")
            if expected_url == actual_url:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.three_second)
            username = self.d.find_element(By.XPATH, Read_Enrollments_Components().get_username_textbox())
            username.clear()
            username.send_keys(Read_Enrollments_Components().get_valid_username())
            time.sleep(web_driver.two_second)
            password = self.d.find_element(By.XPATH, Read_Enrollments_Components().get_password_textbox())
            password.clear()
            password.send_keys(Read_Enrollments_Components().get_valid_password())
            time.sleep(web_driver.two_second)
            cloud_login = self.d.find_element(By.XPATH, Read_Enrollments_Components().get_cloudlogin_button())
            cloud_login.click()
            time.sleep(web_driver.two_second)
        except Exception as ex:
            print(ex)
