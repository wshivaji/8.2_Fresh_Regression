import time
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from All_Config_Packages._6_Notes_search_filter_Config_Files.Notes_Search_Filter_Combination_Read_INI import \
    Read_notes_search_filter_combination
from Base_Package.Web_Logger import web_logger
from Base_Package.Web_Driver import web_driver
from Base_Package.Login_Logout_Ops import login, logout


class Notes_search_filter_combination_pom(web_driver, web_logger):
    d = web_driver.d()
    log = web_logger.logger_obj()
    screenshots_path = f"{Path(__file__).parent.parent.parent}\\Reports\\Screenshots"
    '''
    def login_before(self):

        try:
            self.d.get(Read_Portal_Menu_Components().get_url())
            username = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_usernameField())
            username.send_keys(Read_Portal_Menu_Components().get_username())
            password = self.d.find_element(By.XPATH, Read_Portal_Menu_Components().get_passwordField())
            password.send_keys(Read_Portal_Menu_Components().get_password())
            time.sleep(web_driver.one_second)
            login_btn = self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton())
            self.d.execute_script("arguments[0].click();", login_btn)
            time.sleep(web_driver.three_second)
        except Exception as ex:
            self.d.save_screenshot(
                f"{self.screenshots_path}\\login_failed_for_Notes_search_filter_combination_pom.png")
            self.log.info(f"login_before:  {ex}")
            return False
    

    def login(self):
        if self.d.title == "" or self.d.find_element(By.ID, Read_Portal_Menu_Components().get_loginButton()). \
                is_displayed():
            self.login_before()
    '''

    def wait_for_element_to_appear(self, element_list, xpath):
        count = 0
        if len(element_list) == 0:
            while len(element_list) == 0 or count == 10:
                element_list = self.d.find_elements(By.XPATH, xpath)
                time.sleep(web_driver.one_second)
                if len(element_list) > 0:
                    self.log.info("element is visible...")
                    return element_list[0]
                else:
                    self.log.info("waiting for element...")
                count += 1
                self.log.info(f"wait count: {count}")
        else:
            self.log.info(f"element length: {len(element_list)}")
            return element_list[0]

    def click_on_notes_menu(self):
        notes = self.explicit_wait(10, "XPATH", Read_notes_search_filter_combination().notes_menu_button_by_xpath(),
                                   self.d)
        notes.click()

    def click_on_notes_search_button(self):
        time.sleep(web_driver.one_second)
        search_button = self.explicit_wait(10, "XPATH",
                                           Read_notes_search_filter_combination().notes_search_button_by_xpath(),
                                           self.d)
        search_button.click()

    def click_on_description_dropdown_option(self):
        time.sleep(web_driver.one_second)
        description_option = self.explicit_wait(10, "XPATH", Read_notes_search_filter_combination().
                                                search_dropdown_description_option_by_xpath(), self.d)
        description_option.click()

    def enter_location_or_store(self):
        location_or_store = self.explicit_wait(10, "XPATH", Read_notes_search_filter_combination().
                                               location_or_store_input_field_by_xpath(), self.d)

        location_or_store.send_keys(Read_notes_search_filter_combination().get_location_or_store())

    def enter_case_or_subject(self):
        case_or_subject = self.explicit_wait(10, "XPATH", Read_notes_search_filter_combination().
                                             case_or_subject_input_field_by_xpath(), self.d)
        case_or_subject.send_keys(Read_notes_search_filter_combination().get_case_or_subject())

    def click_on_filter_search_button(self):
        time.sleep(web_driver.one_second)
        filter_search_button = self.explicit_wait(10, "XPATH",
                                                  Read_notes_search_filter_combination().
                                                  notes_filter_search_button_by_xpath(), self.d)
        filter_search_button.click()
        # return filter_search_button.is_enabled()

    def sort_by_case_or_subject(self):
        time.sleep(web_driver.one_second)

        ele = self.explicit_wait(10, "XPATH", Read_notes_search_filter_combination().sort_by_dropdown_by_xpath(), self.d)
        time.sleep(web_driver.one_second)
        select = Select(ele)
        sort_by = Read_notes_search_filter_combination().get_sort_by_case_or_subject()
        time.sleep(web_driver.one_second)
        select.select_by_visible_text(sort_by)

    def sort_by_location_or_store(self):
        time.sleep(web_driver.one_second)

        ele = self.explicit_wait(10, "XPATH", Read_notes_search_filter_combination().
                                 sort_by_dropdown_by_xpath(), self.d)
        select = Select(ele)
        sort_by = Read_notes_search_filter_combination().get_sort_by_location_or_store()
        select.select_by_visible_text(sort_by)

    def location_or_store_search_result_validation(self):
        time.sleep(web_driver.one_second)

        result_validation = self.explicit_wait(10, "XPATH", Read_notes_search_filter_combination().
                                               location_or_store_search_result_validation_by_xpath(), self.d)
        actual_text = result_validation.text.lower()
        expected_text = Read_notes_search_filter_combination().get_location_or_store().lower()
        return expected_text in actual_text

    def case_or_subject_search_result_validation(self):
        time.sleep(web_driver.one_second)

        result_validation = self.explicit_wait(10, "XPATH", Read_notes_search_filter_combination().
                                               case_or_subject_search_result_validation_by_xpath(), self.d)
        actual_text = result_validation.text.lower()
        expected_text = Read_notes_search_filter_combination().get_case_or_subject().lower()
        return expected_text in actual_text

    def sort_by_location_or_store_validation(self):
        time.sleep(web_driver.one_second)
        self.explicit_wait(10, "XPATH", Read_notes_search_filter_combination().
                           sort_by_result_validation_by_xpath(), self.d)
        result_validation = self.explicit_wait(10, "XPATH", Read_notes_search_filter_combination().
                                               sort_by_result_validation_by_xpath(), self.d)
        actual_text = result_validation.text.lower()
        self.log.info(f"actual text: {actual_text}")
        expected_text = Read_notes_search_filter_combination().get_sort_by_location_or_store().lower()
        self.log.info(f"expected text: {expected_text}")
        if expected_text in actual_text:
            return True
        else:
            return False

    def sort_by_case_or_subject_validation(self):
        time.sleep(web_driver.one_second)

        result_validation = self.explicit_wait(10, "XPATH", Read_notes_search_filter_combination().
                           sort_by_result_validation_by_xpath(), self.d)
        actual_text = result_validation.text.lower()
        print(actual_text)
        self.log.info(f"actual: {actual_text}")
        expected_text = Read_notes_search_filter_combination().get_sort_by_case_or_subject().lower()
        print(expected_text)
        self.log.info(f"expected: {expected_text}")
        if expected_text in actual_text:
            return True
        else:
            return False

        # close tab and logout method

    def close_all_panel_one_by_one(self):
        try:
            close_panel_list = self.d.find_elements(By.XPATH, Read_notes_search_filter_combination()
                                                    .close_panel_one_by_one_list())
            for i in close_panel_list:
                i.click()
                time.sleep(web_driver.one_second)
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\close_panel_failed_event_search_filter_combination.png")
            self.log.info(f"close all panel one by one:  {ex}")
            return False

    def click_on_logout_button(self):
        try:
            time.sleep(web_driver.one_second)
            logout_button = self.d.find_element(By.XPATH, Read_notes_search_filter_combination().logout_btn_by_xpath())
            logout_button.click()
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\Button_not_clickable_logout_pg_03.png")
            self.log.info(f"logout:  {ex}")
            return False

    ######################################### Business Methods #################################################

    def notes_with_no_filter_combination(self):
        try:
            self.log.info("*********** test_TC_NSFC_01 *************")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)
            if self.click_on_filter_search_button():
                time.sleep(web_driver.one_second)
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_01_failed.png")
                status.append(False)
            return status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_01_exception.png")
            self.log.info(f"notes_with_no_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            # logout().logout_from_core(self.d)

    def notes_with_sort_by_Case_Subject_filter_combination(self):
        try:
            self.log.info("************ test_TC_NSFC_02 **************")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_notes_menu()
            self.log.info("clicking on Notes menu")
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            self.log.info("click on description option on notes search dropdown")
            time.sleep(web_driver.one_second)
            self.sort_by_case_or_subject()
            time.sleep(web_driver.one_second)
            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)
            if self.sort_by_case_or_subject_validation():
                time.sleep(web_driver.one_second)
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_02_failed.png")
                status.append(False)
            return status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_02_exception.png")
            self.log.info(f"notes_with_sort_by_Case_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            # logout().logout_from_core(self.d)

    def notes_with_sort_by_location_store_filter_combination(self):
        try:
            self.log.info("******** test_TC_NSFC_03 ***********")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)

            self.sort_by_location_or_store()
            time.sleep(web_driver.one_second)
            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)

            if self.sort_by_location_or_store_validation():
                time.sleep(web_driver.one_second)
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_03_failed.png")
                status.append(False)
            return status[0]
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_03_exception.png")
            self.log.info(f"notes_with_sort_by_location_store_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            # logout().logout_from_core(self.d)

    def notes_with_Sort_by_Location_Store_and_Sort_by_Case_Subject_filter_combination(self):
        try:
            status = self.validate_notes_with_Sort_by_Location_Store_and_Sort_by_Case_Subject_filter_combination()
            time.sleep(web_driver.one_second)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_"
                                   f"Sort_by_Location_Store_and_Sort_by_Case_Subject_filter_combination_failed.png")
            self.log.info(f"notes_with_Sort_by_Location_Store_and_Sort_by_Case_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_Case_Subject_filter_combination(self):
        try:
            self.log.info("************ test_TC_NSFC_05 ****************")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)

            self.enter_case_or_subject()
            time.sleep(web_driver.one_second)

            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)

            if self.case_or_subject_search_result_validation():
                time.sleep(web_driver.one_second)
                status.append(True)
            else:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_05_failed.png")
                status.append(False)
            return status[0]
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_05_Exception.png")
            self.log.info(f"notes_with_Case_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            # logout().logout_from_core(self.d)

    def notes_with_Case_Subject_and_Sort_by_Case_Subject_filter_combination(self):
        try:
            self.log.info("***************** test_TC_NSFC_06 ********************")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)

            self.enter_case_or_subject()
            time.sleep(web_driver.one_second)
            self.sort_by_case_or_subject()
            time.sleep(web_driver.one_second)

            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)

            status.append(self.case_or_subject_search_result_validation())
            time.sleep(web_driver.one_second)
            status.append(self.sort_by_case_or_subject_validation())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_06_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_06_exception.png")
            self.log.info(f"notes_with_Case_Subject_and_Sort_by_Case_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            # logout().logout_from_core(self.d)

    def notes_with_filter_Case_Subject_and_Sort_by_Location_Store_combination(self):
        try:
            self.log.info("************* test_TC_NSFC_07 ****************")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)

            self.enter_case_or_subject()
            time.sleep(web_driver.one_second)
            self.sort_by_location_or_store()
            time.sleep(web_driver.one_second)

            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)

            status.append(self.case_or_subject_search_result_validation())
            time.sleep(web_driver.one_second)
            status.append(self.sort_by_location_or_store_validation())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_07_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_07_exception.png")
            self.log.info(f"notes_with_filter_Case_Subject_and_Sort_by_Location_Store_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            logout().logout_from_core(self.d)

    def notes_with_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination(self):
        try:
            status = self.validate_notes_with_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination()
            time.sleep(web_driver.one_second)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Case_Subject_Sort_by_"
                                   f"Location_Store_and_Sort_by_Core_Subject_filter_combination_failed.png")
            self.log.info(f"notes_with_Case_Subject_Sort_"
                          f"by_Location_Store_and_Sort_by_Core_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def notes_with_Location_Store_filter_combination(self):
        try:
            self.log.info("************* test_TC_NSFC_09 *******************")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)

            self.enter_location_or_store()
            time.sleep(web_driver.one_second)

            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)

            if self.location_or_store_search_result_validation():
                time.sleep(web_driver.one_second)
                status.append(True)
            else:
                status.append(False)
            return status[0]
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_09_exception.png")
            self.log.info(f"notes_with_Location_Store_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            # logout().logout_from_core(self.d)

    def notes_with_Location_Store_and_Sort_by_Case_Subject_filter_combination(self):
        try:
            self.log.info("************* test_TC_NSFC_010 ***************")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)

            self.enter_location_or_store()
            time.sleep(web_driver.one_second)
            self.sort_by_case_or_subject()
            time.sleep(web_driver.one_second)

            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)

            status.append(self.location_or_store_search_result_validation())
            time.sleep(web_driver.one_second)
            status.append(self.sort_by_case_or_subject_validation())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_010_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_010_exception.png")
            self.log.info(f"notes_with_Location_Store_and_Sort_by_Case_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            # logout().logout_from_core(self.d)

    def notes_with_Location_Store_and_Sort_by_Location_Store_filter_combination(self):
        try:
            self.log.info("************** test_TC_NSFC_011 ******************")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)

            self.enter_location_or_store()
            time.sleep(web_driver.one_second)
            self.sort_by_location_or_store()
            time.sleep(web_driver.one_second)

            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)

            status.append(self.location_or_store_search_result_validation())
            time.sleep(web_driver.one_second)
            status.append(self.sort_by_location_or_store_validation())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_011_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_011_exception.png")
            self.log.info(f"notes_with_Location_Store_and_Sort_by_Location_Store_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            # logout().logout_from_core(self.d)

    def notes_with_Location_Store_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination(self):
        try:
            status = self.validate_notes_with_Location_Store_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination()
            time.sleep(web_driver.one_second)
            return status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_012_exception.png")
            self.log.info(f"notes_with_Location_Store_Sort_by_Location_Store_and"
                          f"_Sort_by_Core_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()

    def Notes_with_Location_Store_CASE_NUMBER_Sortby_Location_Store_and_Sortby_A_to_Zor_Z_to_A_filter_combination_result_should_be_Location_Store_CASENUMBER_Sortby_Location_Store_and_Sorby_A_to_Z_or_Z_to_A(self):
        try:
            self.log.info("*********** test_TC_NSFC_013 ************")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)

            self.enter_location_or_store()
            time.sleep(web_driver.one_second)
            self.enter_case_or_subject()
            time.sleep(web_driver.one_second)

            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)

            status.append(self.location_or_store_search_result_validation())
            time.sleep(web_driver.one_second)
            status.append(self.case_or_subject_search_result_validation())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_013_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_013_Exception.png")
            self.log.info(f"notes_with_Location_Store_and_Case_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            # logout().logout_from_core(self.d)

    def notes_with_Location_Store_Case_Subject_and_Sort_by_Case_Subject_filter_combination(self):
        try:
            self.log.info("*********** test_TC_NSFC_014 ****************")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)

            self.enter_location_or_store()
            time.sleep(web_driver.one_second)
            self.enter_case_or_subject()
            time.sleep(web_driver.one_second)
            self.sort_by_case_or_subject()
            time.sleep(web_driver.one_second)

            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)

            status.append(self.location_or_store_search_result_validation())
            time.sleep(web_driver.one_second)
            status.append(self.case_or_subject_search_result_validation())
            time.sleep(web_driver.one_second)
            status.append(self.sort_by_case_or_subject_validation())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_014_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_014_exception.png")
            self.log.info(f"notes_with_Location_Store_Case_Subject_and_Sort_by_Case_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            # logout().logout_from_core(self.d)

    def notes_with_Location_Store_Case_Subject_and_Sort_by_Location_Store_filter_combination(self):
        try:
            self.log.info("************* test_TC_NSFC_015 ****************")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)

            self.enter_location_or_store()
            time.sleep(web_driver.one_second)
            self.enter_case_or_subject()
            time.sleep(web_driver.one_second)
            self.sort_by_location_or_store()
            time.sleep(web_driver.one_second)

            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)

            status.append(self.location_or_store_search_result_validation())
            time.sleep(web_driver.one_second)
            status.append(self.case_or_subject_search_result_validation())
            time.sleep(web_driver.one_second)
            status.append(self.sort_by_location_or_store_validation())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_015_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_015_Exception.png")
            self.log.info(f"notes_with_Location_Store_Case_Subject"
                          f"_and_Sort_by_Location_Store_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            # logout().logout_from_core(self.d)

    def notes_with_Location_Store_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination(self):
        try:
            status = self.validate_notes_with_Location_Store_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination()
            time.sleep(web_driver.one_second)
            return False not in status
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\notes_with_Location_Store_Case_Subject_"
                                   f"Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination_failed.png")
            self.log.info(f"notes_with_Location_Store_Case_Subject_Sort_by_Location_Store_and"
                          f"_Sort_by_Core_Subject_filter_combination:  {ex}")
            return False
        finally:
            # self.close_all_panel_one_by_one()
            self.click_on_logout_button()

    def validate_notes_with_Sort_by_Location_Store_and_Sort_by_Case_Subject_filter_combination(self):
        try:
            self.log.info("************ test_TC_NSFC_04 *************")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)
            self.sort_by_case_or_subject()
            time.sleep(web_driver.one_second)
            self.log.info("entered case/subject")
            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)
            status.append(self.sort_by_case_or_subject_validation())
            time.sleep(web_driver.two_second)

            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)
            self.sort_by_location_or_store()
            time.sleep(web_driver.one_second)
            self.log.info("entered on location/store")
            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)
            status.append(self.sort_by_location_or_store_validation())
            time.sleep(web_driver.one_second)
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_04_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_04_exception.png")
            self.log.info(f"notes_with_Sort_by_Location_Store_and_Sort_by_Case_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            # logout().logout_from_core(self.d)

    def validate_notes_with_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination(self):
        try:
            self.log.info("********** test_TC_NSFC_08 **************")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)
            self.enter_case_or_subject()
            time.sleep(web_driver.one_second)
            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)
            status.append(self.case_or_subject_search_result_validation())
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)

            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)
            self.sort_by_case_or_subject()
            time.sleep(web_driver.one_second)
            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)
            status.append(self.sort_by_case_or_subject_validation())
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)
            self.sort_by_location_or_store()
            time.sleep(web_driver.one_second)
            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)
            status.append(self.sort_by_location_or_store_validation())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_08_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_08_exception.png")
            self.log.info(
                f"validate_notes_with_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination:  {ex}")
            return False
        finally:
            self.close_all_panel_one_by_one()
            # logout().logout_from_core(self.d)

    def validate_notes_with_Location_Store_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination(self):
        status = []
        login().login_to_cloud_if_not_done(self.d)
        time.sleep(web_driver.one_second)

        self.click_on_notes_menu()
        time.sleep(web_driver.one_second)
        self.click_on_notes_search_button()
        time.sleep(web_driver.one_second)
        self.click_on_description_dropdown_option()
        time.sleep(web_driver.one_second)
        self.enter_location_or_store()
        time.sleep(web_driver.one_second)
        self.click_on_filter_search_button()
        time.sleep(web_driver.one_second)
        status.append(self.location_or_store_search_result_validation())
        time.sleep(web_driver.one_second)
        self.close_all_panel_one_by_one()

        self.click_on_notes_menu()
        time.sleep(web_driver.one_second)
        self.click_on_notes_search_button()
        time.sleep(web_driver.one_second)
        self.click_on_description_dropdown_option()
        time.sleep(web_driver.one_second)
        self.sort_by_location_or_store()
        time.sleep(web_driver.one_second)
        self.click_on_filter_search_button()
        time.sleep(web_driver.one_second)
        status.append(self.sort_by_location_or_store_validation())
        time.sleep(web_driver.one_second)
        self.close_all_panel_one_by_one()

        self.click_on_notes_menu()
        time.sleep(web_driver.one_second)
        self.click_on_notes_search_button()
        time.sleep(web_driver.one_second)
        self.click_on_description_dropdown_option()
        time.sleep(web_driver.one_second)
        self.sort_by_case_or_subject()
        time.sleep(web_driver.one_second)
        self.click_on_filter_search_button()
        time.sleep(web_driver.one_second)
        status.append(self.sort_by_case_or_subject_validation())
        time.sleep(web_driver.one_second)
        self.logger.info(f"status: {status}")
        if False in status:
            return False
        else:
            return True

    def validate_notes_with_Location_Store_Case_Subject_Sort_by_Location_Store_and_Sort_by_Core_Subject_filter_combination(
            self):
        try:
            self.log.info("************ test_TC_NSFC_016 **************")
            status = []
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.click_on_notes_menu()
            time.sleep(web_driver.one_second)
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)
            self.sort_by_case_or_subject()
            time.sleep(web_driver.one_second)
            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)
            status.append(self.sort_by_case_or_subject_validation())
            time.sleep(web_driver.one_second)
            # self.close_all_panel_one_by_one()

            # self.click_on_notes_menu()
            self.click_on_notes_search_button()
            time.sleep(web_driver.one_second)
            self.click_on_description_dropdown_option()
            time.sleep(web_driver.one_second)
            self.sort_by_location_or_store()
            time.sleep(web_driver.one_second)
            self.click_on_filter_search_button()
            time.sleep(web_driver.one_second)
            status.append(self.sort_by_location_or_store_validation())
            time.sleep(web_driver.one_second)
            # self.close_all_panel_one_by_one()

            # self.click_on_notes_menu()
            # self.click_on_notes_search_button()
            # self.click_on_description_dropdown_option()
            # self.sort_by_case_or_subject()
            # self.click_on_filter_search_button()
            # status.append(self.sort_by_case_or_subject_validation())
            # self.close_all_panel_one_by_one()
            #
            # self.click_on_notes_menu()
            # self.click_on_notes_search_button()
            # self.click_on_description_dropdown_option()
            # self.sort_by_location_or_store()
            # self.click_on_filter_search_button()
            # status.append(self.sort_by_location_or_store_validation())
            self.logger.info(f"status: {status}")
            if False in status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_016_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_016_exception.png")
            self.log.info(f"validate_notes_with_Location_Store_Case_Subject_Sort_by_Location_Store_and"
                          f"_Sort_by_Core_Subject_filter_combination:  {ex}")
            return False
        # finally:
        #     # self.close_all_panel_one_by_one()
        #     self.click_on_logout_button()
