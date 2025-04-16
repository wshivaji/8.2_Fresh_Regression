import configparser
import time
from pathlib import Path

from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from selenium.webdriver.common.by import By
# from All_Config_Packages._17_Notifier_Module_Config_Files.Notifier_Read_INI import Notifier_Read_ini
# from All_Config_Packages._18_Reporting_Module_Config_Files.Reporting_Read_INI import Reporting_read_ini
# from All_Config_Packages._0_login_logout_config_file.login_logout_read_ini import LoginLogout_Read_ini
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import \
    Portal_Menu_Module_read_ini
# from All_Config_Packages._6_Notification_Groups_Module_Config_Files.Notification_Groups_Read_INI import \
#     Read_Notification_Groups_Components
from All_Config_Packages._20_Insight_Dashboard_Config_File.Insight_Dashboard_Read_INI import insight_dashboard_read_ini
from Base_Package.Login_Logout_Ops import login, logout
# from All_Other_Utility_Packages._4_User_Roles_Module.Read_Excel import Read_excel


class insight_dashboard_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []


    def Verify_user_is_able_to_see_counts_on_overview_dashboard_as_total_loss_prevented_5500_active_enrollment_25_total_match_events_25_visito_searches_0_investgation_saving_time_0_repeat_people_of_interest_0(
            self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_01 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            self.get_insight_dashboard_data()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            if self.verify_overview_dashboard_label_on_insight_dashboard():
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status1: {self.status}")
            self.status.append(self.verify_total_loss_prevented())
            self.logger.info(f"status2: {self.status}")
            self.status.append(self.verify_total_new_enrollments())
            self.logger.info(f"status3: {self.status}")
            self.status.append(self.verify_total_facefirst_enrollments())
            self.logger.info(f"status4: {self.status}")
            self.status.append(self.verify_total_match_events())
            self.logger.info(f"status5: {self.status}")
            self.status.append(self.verify_visitor_searches())
            self.logger.info(f"status6: {self.status}")
            self.status.append(self.verify_investigation_time())
            self.logger.info(f"status7: {self.status}")
            self.status.append(self.verify_repeat_people_of_interest())
            self.logger.info(f"status8: {self.status}")

            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_01 end  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_01_failed.png")
                self.logger.info(f"overview dashboard is not visible")
                return False
            else:
                self.logger.info(f"overview dashboard is visible.")
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_01_exception.png")
            self.logger.info(f"verify count on overview dashboard: {ex.args}")
            return False

    def Verify_user_is_able_to_see_loss_prevented_by_enrollment_group_counts(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_02 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.d.refresh()
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.loss_prevented_by_enrollment_group())
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info("************* test_TC_Insight_Dashboard_02 end  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_02_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_02_exception.png")
            self.logger.info(f"user_is_able_to_see_loss_prevented_by_enrollment_group ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_Possible_Match_Events_by_enrollment_action_counts(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_03 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.verify_possible_match_event_by_enrollment_action_count())
            self.logger.info(f"status: {self.status}")
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info("************* test_TC_Insight_Dashboard_03 end  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_03_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_03_exception.png")
            self.logger.info(f"user_is_able_to_see_Possible_Match_Events_by_enrollment_action_counts ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_counts_on_overview_dashboard_organisation_and_individual_groups(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_04 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            enrollment_group_dropdown = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().enrollment_group_dropdown_by_xpath(), self.d)
            if enrollment_group_dropdown:
                enrollment_group_dropdown.click()
                time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            enrollment_groups_list = self.d.find_elements(By.XPATH, insight_dashboard_read_ini().enrollment_group_list_by_xpath())
            enrollment_group_dropdown.click()
            time.sleep(web_driver.one_second)
            if enrollment_groups_list:
                enrollment_group_dropdown.click()
                for eg in enrollment_groups_list:
                    self.logger.info(f"eg enlisted: {eg.text}")
                    if eg.text.isalnum():
                        eg.click()
                        self.status.append(self.verify_total_loss_prevented())
                        time.sleep(web_driver.one_second)
                        self.status.append(self.verify_total_new_enrollments())
                        time.sleep(web_driver.one_second)
                        self.status.append(self.verify_total_facefirst_enrollments())
                        time.sleep(web_driver.one_second)
                        self.status.append(self.verify_total_match_events())
                        time.sleep(web_driver.one_second)
                        self.status.append(self.verify_visitor_searches())
                        time.sleep(web_driver.one_second)
                        self.status.append(self.verify_investigation_time())
                        time.sleep(web_driver.one_second)
                        self.status.append(self.verify_repeat_people_of_interest())
                        time.sleep(web_driver.one_second)
                        eg.click()
                        time.sleep(web_driver.one_second)

            self.logger.info(f"status: {self.status}")
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info("************* test_TC_Insight_Dashboard_04 end  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_04_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_04_exception.png")
            self.logger.info(f"user_is_able_to_see_counts_on_overview_dashboard_organisation_and_individual_groups ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_loss_prevented_by_enrollment_group_counts_organisation_and_individual_groups(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_05 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            enrollment_group_dropdown = self.explicit_wait(5, "XPATH",
                                                           insight_dashboard_read_ini().enrollment_group_dropdown_by_xpath(),
                                                           self.d)
            if enrollment_group_dropdown:
                enrollment_group_dropdown.click()
                time.sleep(web_driver.one_second)

            enrollment_groups_list = self.d.find_elements(By.XPATH, insight_dashboard_read_ini().enrollment_group_list_by_xpath())
            enrollment_group_dropdown.click()
            time.sleep(web_driver.one_second)
            if enrollment_groups_list:
                enrollment_group_dropdown.click()
                time.sleep(web_driver.one_second)
                for eg in enrollment_groups_list:
                    self.logger.info(f"eg enlisted: {eg.text}")
                    if eg.text.isalnum():
                        eg.click()
                        time.sleep(web_driver.one_second)
                        self.status.append(self.loss_prevented_by_enrollment_group())
                        eg.click()
                        time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info("************* test_TC_Insight_Dashboard_05 end  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_05_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_05_exception.png")
            self.logger.info(f"user_is_able_to_see_loss_prevented_by_enrollment_group_counts_organisation_and_individual_groups ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_Possible_Match_Events_by_enrollment_action_counts_organisation_and_individual_groups(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_06 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            enrollment_group_dropdown = self.explicit_wait(5, "XPATH",
                                                           insight_dashboard_read_ini().enrollment_group_dropdown_by_xpath(),
                                                           self.d)
            if enrollment_group_dropdown:
                enrollment_group_dropdown.click()
                time.sleep(web_driver.one_second)

            enrollment_groups_list = self.d.find_elements(By.XPATH,
                                                          insight_dashboard_read_ini().enrollment_group_list_by_xpath())
            enrollment_group_dropdown.click()
            time.sleep(web_driver.one_second)
            if enrollment_groups_list:
                enrollment_group_dropdown.click()
                time.sleep(web_driver.one_second)
                for eg in enrollment_groups_list:
                    self.logger.info(f"eg enlisted: {eg.text}")
                    if eg.text.isalnum():
                        eg.click()
                        time.sleep(web_driver.one_second)
                        self.status.append(self.verify_possible_match_event_by_enrollment_action_count())
                        eg.click()
                        time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info("************* test_TC_Insight_Dashboard_05 end  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_06_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_06_exception.png")
            self.logger.info(f"user_is_able_to_see_Possible_Match_Events_by_enrollment_action_counts_organisation_and_individual_groups ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_07 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.select_all_options_dashboard_option())
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info("************* test_TC_Insight_Dashboard_07 end  **************")
            if False in self.status:
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_07_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_cumulative_Probable_Match_Events_by_date_todays_date_and_25_count(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_08 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.select_probable_match_events_dashboard_option_and_verify_cumulative_match_events())
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info("************* test_TC_Insight_Dashboard_08 end  **************")
            if False in self.status:
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_08_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_tagged_vs_untagged_Probable_Match_Events_count_as_tagged_and_untagged(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_09 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.select_probable_match_events_and_Verify_tagged_untagged_probable_match_events())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_09 end  **************")
            if False in self.status:
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_09_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_Probable_Match_Events_by_enrollment_groups_counts(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_10 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.Probable_Match_Events_by_enrollment_groups_counts())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_10 end  **************")
            if False in self.status:
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_10_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_tagged_Probable_Match_Events_by_tag_type(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_11 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.tagged_probable_match_events_by_tag_type())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_11 end  **************")
            if False in self.status:
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_11_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_counts_on_Probable_Match_Events_dashboard_organisation_and_individual_groups(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_12 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.able_to_see_counts_on_Probable_Match_Events_dashboard_organisation_and_individual_groups())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_12 end  **************")
            if False in self.status:
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_12_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_cumulative_Probable_Match_Events_by_date_organisation_and_individual_group(self):
        try:
            # test case 8 adn 13 are similar
            self.logger.info("************* test_TC_Insight_Dashboard_13 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.select_probable_match_events_dashboard_option_and_verify_cumulative_match_events())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info("************* test_TC_Insight_Dashboard_13 end  **************")
            if False in self.status:
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_13_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_tagged_vs_untagged_Probable_Match_Events_count_organisation_and_individual_groups(self):
        try:
            # test case 11 and 14
            self.logger.info("************* test_TC_Insight_Dashboard_14 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.tagged_probable_match_events_by_tag_type())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_14 end  **************")
            if False in self.status:
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_14_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_Probable_Match_Events_by_enrollment_groups_counts_organisation_and_individual_groups(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_15 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.Probable_Match_Events_by_enrollment_groups_counts())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_10 end  **************")
            if False in self.status:
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_15_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_tagged_Probable_Match_Events_by_tag_type_organisation_and_individual_groups(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_16 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.tagged_probable_match_events_by_tag_type())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_16 end  **************")
            if False in self.status:
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_16_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_on_enrollment_dashboard_as_enrollment_overview_and_cumulative_enrollments_by_date_as_mention_is_link(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_17 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.select_enrollment_dashboard_option_and_verify_cumulative_enrollments_by_date())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_17 end  **************")
            if False in self.status:
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_17_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_enrollment_by_date_counts_on_enrollment_dashboard(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_18 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.enrollments_by_date_counts_on_enrollment_dashboard())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_17 end  **************")
            if self.status:
                if False in self.status:
                    return False
                else:
                    return True
            else:
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_18_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_enrollments_by_enrollment_group_counts_as_mention_in_link(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_19 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.enrollments_by_enrollment_group_counts())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_19 end  **************")
            if len(self.status) > 0:
                if None in self.status:
                    return False
                else:
                    if False in self.status:
                        return False
                    else:
                        return True
            else:
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_19_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_enrollments_by_week_org_counts_as_mention_in_link(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_20 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.enrollments_by_week_org_counts())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_20 end  **************")
            if len(self.status) > 0:
                if False in self.status:
                    return False
                else:
                    return True
            else:
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_20_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_Enrollments_by_status_count(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_21 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.Enrollments_by_status_count())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_21 end  **************")
            if self.status:
                if False in self.status:
                    return False
                else:
                    return True
            else:
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_21_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_user_is_able_to_see_on_enrollment_dashboard_as_enrollment_overview_and_cumulative_enrollments_by_date(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_22 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)

            self.status.append(self.user_is_able_to_see_on_enrollment_dashboard_as_enrollment_overview_and_cumulative_enrollments_by_date())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_22 end  **************")
            if len(self.status) > 0:
                if None in self.status:
                    return False
                else:
                    if False in self.status:
                        return False
                    else:
                        return True
            else:
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_22_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_enrollment_by_date_counts_as_mention_in_link_organisation_and_individual_group(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_23 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.enrollment_by_date_counts_as_mention_in_link_organisation_and_individual_group())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_23 end  **************")
            if len(self.status) > 0:
                if None in self.status:
                    return False
                else:
                    if False in self.status:
                        return False
                    else:
                        return True
            else:
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_23_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_enrollments_by_enrollment_group_counts_as_mention_in_link_organisation_and_individual_group(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_24 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.enrollments_by_enrollment_group_counts_as_mention_in_link_organisation_and_individual_group())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_24 end  **************")
            if len(self.status) > 0:
                if None in self.status:
                    return False
                else:
                    if False in self.status:
                        return False
                    else:
                        return True
            else:
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_24_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_enrollments_by_week_counts_as_mention_in_link_organisation_and_individual_groups(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_25 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.enrollments_by_week_counts_as_mention_in_link_organisation_and_individual_groups())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_25 end  **************")
            if len(self.status) > 0:
                if None in self.status:
                    return False
                else:
                    if False in self.status:
                        return False
                    else:
                        return True
            else:
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_25_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    def Verify_Enrollments_by_Status_counts_organisation_and_individual_groups(self):
        try:
            self.logger.info("************* test_TC_Insight_Dashboard_26 started  **************")
            login().login_to_facecirst_portal_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_insights_dashboard()
            time.sleep(web_driver.one_second)
            self.switch_to_insight_dashboard_tab()
            time.sleep(web_driver.one_second)
            self.status.append(self.Enrollments_by_Status_counts_organisation_and_individual_groups())
            time.sleep(web_driver.one_second)
            self.close_current_tab()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_Insight_Dashboard_26 end  **************")
            if len(self.status) > 0:
                if None in self.status:
                    return False
                else:
                    if False in self.status:
                        return False
                    else:
                        return True
            else:
                return False
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_26_exception.png")
            self.logger.info(f"Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard ex: {ex.args}")
            return False

    # ****************************** user Methods *******************************************

    def get_insight_dashboard_data(self):
        try:
            common_test_data_ini_file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\common_test_data.ini"
            file = Path(common_test_data_ini_file_path)
            config = configparser.ConfigParser()
            config.read(file)
            total_enrollments = self.get_total_enrollments()
            time.sleep(web_driver.one_second)
            total_events = self.get_total_events()
            time.sleep(web_driver.one_second)
            total_visitor_search = self.get_total_visitor_search_count()
            time.sleep(web_driver.one_second)
            self.logger.info(f"got total enrollments: {total_enrollments}")
            self.logger.info(f"got total events: {total_events}")
            self.logger.info(f"got total visitor searches: {total_visitor_search}")

            config.set("Insights_Dashboard_Data", "total_enrollments_count", total_enrollments)
            config.set("Insights_Dashboard_Data", "total_events_count", total_events)
            config.set("Insights_Dashboard_Data", "total_visitor_search_count", total_visitor_search)
            config.write(file.open('w'))

        except Exception as ex:
            self.logger.info(f"get_insight_dashboard_data ex: {ex.args}")

    def get_total_enrollments(self):
        try:
            enrollments_menu = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().enrollments_menu_item_by_xpath(), self.d)
            self.logger.info(f"enrollments menu: {enrollments_menu.is_displayed()}")
            enrollments_menu.click()
            time.sleep(web_driver.one_second)
            filter_option = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().get_filter_option_by_xpath(), self.d)
            self.logger.info(f"filter option visible: {filter_option.is_displayed()}")
            filter_option.click()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            enabled_option = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().get_enabled_option_by_xpath(), self.d)
            self.logger.info(f"enabled option visible: {enabled_option.is_displayed()}")
            enabled_option.click()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            enrollments_count_text = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().total_enrollments_text_on_enrollments_panel_by_xpath(), self.d)
            self.logger.info(f"text: {enrollments_count_text.text}")
            text_list = enrollments_count_text.text.split(" ")
            self.logger.info(text_list)
            return text_list[3]
        except Exception as ex:
            self.logger.info(f"get_total_enrollments ex: {ex.args}")

    def get_total_events(self):
        try:
            self.d.find_element(By.XPATH, insight_dashboard_read_ini().cloud_menu_by_xpath()).click()
            events_menu = self.explicit_wait(5, "XPATH", Portal_Menu_Module_read_ini().get_events_menu_by_xpath(), self.d)
            events_menu.click()
            total_events_text = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().probable_match_events_text_on_events_panel_by_xpath(), self.d)
            self.logger.info(f"total events text: {total_events_text.text}")
            total_events_text_list = total_events_text.text.split(' ')
            self.logger.info(f"text list: {total_events_text_list}")
            return total_events_text_list[3]
        except Exception as ex:
            self.logger.info(f"get_total_events ex : {ex.args}")

    def get_total_visitor_search_count(self):
        try:
            self.d.find_element(By.XPATH, insight_dashboard_read_ini().cloud_menu_by_xpath()).click()
            vsj_menu_item = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().visitor_search_jobs_menu_item_by_xpath(), self.d)
            vsj_menu_item.click()
            total_vs_text = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().visitor_search_count_text_on_vsj_panel(), self.d)
            if total_vs_text:

                self.logger.info(f"vs text: {total_vs_text.text}")
                total_vs_text_list = total_vs_text.text.split(' ')
                self.logger.info(f"vs text list: {total_vs_text_list}")
                return total_vs_text_list[3]
            else:
                self.logger.info(f"total visitor search data not available")

        except Exception as ex:
            self.logger.info(f"get_total_visitor_search_count ex: {ex.args}")

    def open_insights_dashboard(self):
        try:
            self.d.find_element(By.XPATH, insight_dashboard_read_ini().cloud_menu_by_xpath()).click()
            time.sleep(web_driver.one_second)
            insight_dashboard_menu = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().Insight_Dashboard_menu_by_xpath(), self.d)
            if insight_dashboard_menu:
                insight_dashboard_menu.click()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.info(f"open insight dashboard: {ex.args}")

    def switch_to_insight_dashboard_tab(self):
        try:
            tabs = self.d.window_handles
            self.d.switch_to.window(tabs[1])
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.info(f"switch to insight dashboard tab exception: {ex.args}")

    def switch_to_portal_page_tab(self):
        try:
            tabs = self.d.window_handles
            self.d.switch_to.window(tabs[0])
            # self.d.switch_to.default_content()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.info(f"switch to portal page: {ex.args}")

    def close_current_tab(self):
        try:
            open_tabs = self.d.window_handles
            parent = self.d.window_handles[0]
            child = self.d.window_handles[1]
            # i = 1
            # for i in range(open_tabs):
            #     child = self.d.window_handles[i]
            self.d.switch_to.window(child)
            self.d.close()
            self.d.switch_to.window(parent)
        except Exception as ex:
            self.logger.info(f"close current tab: {ex.args}")

    def verify_overview_dashboard_label_on_insight_dashboard(self):
        try:

            time.sleep(web_driver.two_second)
            overview_dashboard = self.explicit_wait(10, "XPATH", insight_dashboard_read_ini().overview_dashboard_label_by_xpath(), self.d)
            self.logger.info(f"overview dashboard visible: {overview_dashboard.is_displayed()}")
            if overview_dashboard:
                self.logger.info(f"overview dashboard visible: {overview_dashboard.is_displayed()}")
                if overview_dashboard.is_displayed():
                    return True
                else:
                    return False

        except Exception as ex:
            self.logger.info(f"overview dashboard label exception: {ex.args}")

    def verify_total_loss_prevented(self):
        try:
            total_loss_prevented_text = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().total_loss_prevented_label_by_xpath(), self.d)
            self.logger.info(f"total loss prevented text visible: {total_loss_prevented_text.is_displayed()}")
            self.logger.info(f"total loss text: {total_loss_prevented_text.text}")
            total_loss_prevented_count = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().total_loss_prevented_amount_by_xpath(), self.d)
            self.logger.info(f"total loss prevented amount visible: {total_loss_prevented_count.is_displayed()}")
            self.logger.info(f"total loss: {total_loss_prevented_count.text}")
            loss_count = total_loss_prevented_count.text[1:]
            self.logger.info(f"loss count int: {loss_count}")
            x = []
            if total_loss_prevented_text:
                if total_loss_prevented_text.is_displayed():
                    x.append(True)
                else:
                    x.append(False)

            if total_loss_prevented_count:
                if total_loss_prevented_text.is_displayed():
                    x.append(True)
                else:
                    x.append(False)
            if False in x:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"verify total loss prevented exception: {ex.args}")

    def verify_total_new_enrollments(self):
        try:
            total_new_enrollments_text = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().total_new_enrollments_label_by_xpath(), self.d)
            self.logger.info(f"total_new_enrollments text visible: {total_new_enrollments_text.is_displayed()}")
            self.logger.info(f"text: {total_new_enrollments_text.text}")
            total_new_enrollments_count = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().total_new_enrollments_count_by_xpath(), self.d)
            self.logger.info(f"total_new_enrollments count visible: {total_new_enrollments_count.is_displayed()}")
            self.logger.info(f"total new enrollments count: {total_new_enrollments_count.text}")
            total_enrollments = total_new_enrollments_count.text
            x = []
            if total_new_enrollments_text:
                if total_new_enrollments_text.is_displayed():
                    x.append(True)
                else:
                    x.append(False)
            if total_new_enrollments_count:
                if total_new_enrollments_count.is_displayed():
                    x.append(True)
                else:
                    x.append(False)
            if total_enrollments == insight_dashboard_read_ini().total_enrollments_count():
                x.append(True)
            else:
                x.append(False)
            if False in x:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"verify total new enrollments exception: {ex.args}")

    def verify_total_facefirst_enrollments(self):
        try:
            total_facefirst_enrollments_text = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().total_facefirst_enrollments_label_by_xpath(), self.d)
            self.logger.info(f"total_facefirst_enrollments text visible: {total_facefirst_enrollments_text.is_displayed()}")
            self.logger.info(f"text: {total_facefirst_enrollments_text.text}")
            total_facefirst_enrollments_count = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().total_facefirst_enrollments_count_by_xpath(), self.d)
            self.logger.info(f"total_facefirst_enrollments count visible: {total_facefirst_enrollments_count.is_displayed()}")
            self.logger.info(f"count: {total_facefirst_enrollments_count.text}")
            total_facefirst_count = total_facefirst_enrollments_count.text
            x = []
            if total_facefirst_enrollments_text:
                if total_facefirst_enrollments_text.is_displayed():
                    x.append(True)
                else:
                    x.append(False)
            if total_facefirst_enrollments_count:
                if total_facefirst_enrollments_count.is_displayed():
                    x.append(True)
                else:
                    x.append(False)
            if total_facefirst_count == insight_dashboard_read_ini().total_enrollments_count():
                x.append(True)
            else:
                x.append(False)
            if False in x:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"verify total facefirst enrollments exception: {ex.args}")

    def verify_total_match_events(self):
        try:
            total_match_events_text = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().total_probable_match_events_label_by_xpath(), self.d)
            self.logger.info(f"total_match_events text visible: {total_match_events_text.is_displayed()}")
            total_match_event_count_displayed = (total_match_events_text.text).replace(",", "")
            self.logger.info(f"text: {total_match_event_count_displayed}.")
            total_match_events_count = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().total_probable_match_events_count_by_xpath(), self.d)
            self.logger.info(f"total_match_events count visible: {total_match_events_count.is_displayed()}")
            self.logger.info(f"actual total match events count: {total_match_event_count_displayed}")
            self.logger.info(f"expected total match events count: {insight_dashboard_read_ini().total_events_count()}")
            # y = total_match_events_count.text[0]
            # z = total_match_events_count.text[2:]
            # m = y+z
            # total_match_events_count_actual = m

            # if total_match_events_text:
            #     if total_match_events_text.is_displayed():
            #         x.append(True)
            #     else:
            #         x.append(False)
            # if total_match_events_count:
            #     if total_match_events_count.is_displayed():
            #         x.append(True)
            #     else:
            #         x.append(False)

            self.logger.info(f"final total_match_events_count_actual: {total_match_event_count_displayed}")
            if total_match_event_count_displayed == insight_dashboard_read_ini().total_events_count():
                return True
            else:
                return False

        except Exception as ex:
            self.logger.info(f"verify total_match_events exception: {ex.args}")

    def verify_visitor_searches(self):
        try:
            visitor_searches_text = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().visitor_searches_label_by_xpath(), self.d)
            self.logger.info(f"visitor_searches text visible: {visitor_searches_text.is_displayed()}")
            self.logger.info(f"text: {visitor_searches_text.text}")

            visitor_searches_count = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().visitor_searches_count_by_xpath(), self.d)
            self.logger.info(f"visitor_searches count visible: {visitor_searches_count.is_displayed()}")
            self.logger.info(f"count: {visitor_searches_count.text}")
            visitor_search_count_actual = visitor_searches_count.text
            x = []
            if visitor_searches_text:
                if visitor_searches_text.is_displayed():
                    x.append(True)
                else:
                    x.append(False)
            if visitor_searches_count:
                if visitor_searches_count.is_displayed():
                    x.append(True)
                else:
                    x.append(False)
            if visitor_search_count_actual == insight_dashboard_read_ini().total_visitor_search_count():
                x.append(True)
            else:
                x.append(False)
            if False in x:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"verify visitor_searches exception: {ex.args}")

    def verify_investigation_time(self):
        try:
            investigation_time_text = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().investigation_saving_time_label_by_xpath(), self.d)
            self.logger.info(f"investigation_time text visible: {investigation_time_text.is_displayed()}")
            self.logger.info(f"text: {investigation_time_text.text}")
            investigation_time_count = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().investigation_saving_time_count_by_xpath(), self.d)
            self.logger.info(f"investigation_time count visible: {investigation_time_count.is_displayed()}")
            self.logger.info(f"count: {investigation_time_count.text}")
            investigation_time_count_actual = investigation_time_count.text
            x = []
            if investigation_time_text:
                if investigation_time_text.is_displayed():
                    x.append(True)
                else:
                    x.append(False)
            if investigation_time_count:
                if investigation_time_count.is_displayed():
                    x.append(True)
                else:
                    x.append(False)
            if False in x:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"verify investigation_time exception: {ex.args}")

    def verify_repeat_people_of_interest(self):
        try:
            repeat_people_of_interest_text = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().repeat_people_label_by_xpath(), self.d)
            self.logger.info(f"repeat_people_of_interest text visible: {repeat_people_of_interest_text.is_displayed()}")
            self.logger.info(f"text: {repeat_people_of_interest_text.text}")
            repeat_people_of_interest_count = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().repeat_people_count_by_xpath(), self.d)
            self.logger.info(f"repeat_people_of_interest count visible: {repeat_people_of_interest_count.is_displayed()}")
            self.logger.info(f"count: {repeat_people_of_interest_count.text}")
            repeat_people_of_count = repeat_people_of_interest_count.text
            x = []
            if repeat_people_of_interest_text:
                if repeat_people_of_interest_text.is_displayed():
                    x.append(True)
                else:
                    x.append(False)
            if repeat_people_of_interest_count:
                if repeat_people_of_interest_count.is_displayed():
                    x.append(True)
                else:
                    x.append(False)
            if False in x:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"verify repeat_people_of_interest exception: {ex.args}")

    def loss_prevented_by_enrollment_group(self):
        try:
            loss_prevented_by_enrollment_group_label = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().loss_prevented_by_enrollment_group_label_by_xpath(), self.d)
            self.logger.info(f"loss prevented by enrollment groups label visible: {loss_prevented_by_enrollment_group_label.is_displayed()}")
            self.logger.info(f"text: {loss_prevented_by_enrollment_group_label.text}")
            loss_prevented_by_enrollment_group_chart = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            self.logger.info(f"loss prevented chart visible: {loss_prevented_by_enrollment_group_chart.is_displayed()}")

            x = []
            if loss_prevented_by_enrollment_group_label:
                if loss_prevented_by_enrollment_group_label.is_displayed():
                    x.append(True)
                else:
                    x.append(False)
            if loss_prevented_by_enrollment_group_chart:
                if loss_prevented_by_enrollment_group_chart.is_displayed():
                    x.append(True)
                else:
                    x.append(False)
            if False in x:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"loss_prevented_by_enrollment_group ex: {ex.args}")

    def verify_possible_match_event_by_enrollment_action_count(self):
        try:
            # possible_match_event_by_enrollment_action_label = self.explicit_wait()
            possible_match_event_by_enrollment_action_label = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().possible_match_event_by_enrollment_action_label_by_xpath(), self.d)
            self.logger.info(f"loss prevented by enrollment groups label visible: {possible_match_event_by_enrollment_action_label.is_displayed()}")
            self.logger.info(f"text: {possible_match_event_by_enrollment_action_label.text}")
            possible_match_event_by_enrollment_action_chart = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().possible_match_event_by_enrollment_action_chart_by_xpath(), self.d)
            self.logger.info(f"loss prevented chart visible: {possible_match_event_by_enrollment_action_chart.is_displayed()}")
            x = []
            if possible_match_event_by_enrollment_action_label:
                if possible_match_event_by_enrollment_action_label.is_displayed():
                    x.append(True)
                else:
                    x.append(False)
            if possible_match_event_by_enrollment_action_chart:
                if possible_match_event_by_enrollment_action_chart.is_displayed():
                    x.append(True)
                else:
                    x.append(False)
            if False in x:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"verify_possible_mathc_event_by_enrollment_action_count ex: {ex.args}")

    def select_all_options_dashboard_option(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(), self.d)
            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(), self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH, insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                # dashboard_select_dropdown.click()
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option visible: {option.text}")

                        time.sleep(web_driver.one_second)
                        if insight_dashboard_read_ini().overview_dashboard_option_text() == option.text:
                            option.click()
                            self.logger.info(f"{option.text} is displaying.")
                            self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
                            time.sleep(web_driver.one_second)
                            x.append(True)
                        elif insight_dashboard_read_ini().probable_match_events_dashboard_option_text() == option.text:
                            option.click()
                            self.logger.info(f"{option.text} is displaying.")
                            self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().Probable_Match_Events_by_Enrollment_Group_label_by_xpath(), self.d)
                            time.sleep(web_driver.one_second)
                            x.append(True)
                        elif insight_dashboard_read_ini().enrollments_dashboard_text() == option.text:
                            option.click()
                            self.logger.info(f"{option.text} is displaying.")
                            self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().Cumulative_Enrollments_by_Date_label_by_xpath(), self.d)
                            time.sleep(web_driver.one_second)
                            x.append(True)
                        else:
                            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_07_Failed.png")
                            x.append(False)
                        self.logger.info(f"x: {x}")

                        dashboard_select_dropdown.click()

            if False in x:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"select_probable_match_events_dashboard_option: {ex.args}")

    def select_probable_match_events_dashboard_option_and_verify_cumulative_match_events(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH",
                               insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(), self.d)
            self.logger.info(f"dashboard dropdown visible: {dashboard_select_dropdown.is_displayed()}")

            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH",
                                   insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(),
                                   self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH, insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                # dashboard_select_dropdown.click()
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option visible: {option.text}")

                        time.sleep(web_driver.one_second)
                        if insight_dashboard_read_ini().overview_dashboard_option_text() == option.text:
                            option.click()
                            self.logger.info(f"{option.text} is displaying.")
                            self.explicit_wait(5, "XPATH",
                                               insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(),
                                               self.d)
                            time.sleep(web_driver.one_second)
                            # x.append(True)
                        elif insight_dashboard_read_ini().probable_match_events_dashboard_option_text() == option.text:
                            option.click()
                            self.logger.info(f"{option.text} is displaying.")
                            self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().Probable_Match_Events_by_Enrollment_Group_label_by_xpath(), self.d)
                            cumulative_probable_match_events_by_date_label = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().Cumulative_probable_match_events_by_date_label_by_xpath(), self.d)
                            if cumulative_probable_match_events_by_date_label:
                                if cumulative_probable_match_events_by_date_label.is_displayed():
                                    self.logger.info(f"cumulative probable match events visible: {cumulative_probable_match_events_by_date_label.is_displayed()}")
                                    x.append(True)
                                else:
                                    x.append(False)
                            cumulative_probable_match_events_by_date_chart = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().Cumulative_probable_match_events_by_date_chart_by_xpath(), self.d)
                            if cumulative_probable_match_events_by_date_chart:
                                if cumulative_probable_match_events_by_date_chart.is_displayed():
                                    self.logger.info(f"cumulative probable match events chart visible: {cumulative_probable_match_events_by_date_chart.is_displayed()}")
                                    x.append(True)
                                else:
                                    x.append(False)

                            time.sleep(web_driver.one_second)
                            x.append(True)
                        elif insight_dashboard_read_ini().enrollments_dashboard_text() == option.text:
                            option.click()
                            self.logger.info(f"{option.text} is displaying.")
                            self.explicit_wait(5, "XPATH",
                                               insight_dashboard_read_ini().Cumulative_Enrollments_by_Date_label_by_xpath(),
                                               self.d)
                            time.sleep(web_driver.one_second)
                            # x.append(True)
                        else:
                            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_08_Failed.png")
                            x.append(False)
                        self.logger.info(f"x: {x}")

                        dashboard_select_dropdown.click()

            if False in x:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"select_probable_match_events_dashboard_option ex:{ex.args}")

    def select_probable_match_events_and_Verify_tagged_untagged_probable_match_events(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH",
                                                           insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(),
                                                           self.d)
            self.logger.info(f"dashboard dropdown visible: {dashboard_select_dropdown.is_displayed()}")
            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(), self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH, insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                self.logger.info(f"dashboard option list count: {len(dashboard_options_list)}")
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option: {option.text}")
                        if option.text == insight_dashboard_read_ini().probable_match_events_dashboard_option_text():
                            self.logger.info(f"{option.text} option selected")
                            option.click()
                            tagged_untagged_probable_match_events_label = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().Tagged_vs_Untagged_Probable_Match_Events_label_bt_xpath(), self.d)
                            self.logger.info(f"tagged_untagged_probable_match_events visible: {tagged_untagged_probable_match_events_label.is_displayed()}")
                            if tagged_untagged_probable_match_events_label:
                                if tagged_untagged_probable_match_events_label.is_displayed():
                                    x.append(True)
                                else:
                                    x.append(False)
                            else:
                                x.append(False)
                            tagged_untagged_probable_match_events_chart = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().Tagged_vs_Untagged_Probable_Match_Events_chart_bt_xpath(), self.d)
                            self.logger.info(f"tagged_untagged_probable_match_events_chart visible: {tagged_untagged_probable_match_events_chart.is_displayed()}")
                            if tagged_untagged_probable_match_events_chart:
                                if tagged_untagged_probable_match_events_chart.is_displayed():
                                    x.append(True)
                                else:
                                    x.append(False)
                            else:
                                x.append(False)
            self.logger.info(f"x: {x}")
            if False in x:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"select_probable_match_events_and_Verify_tagged_untagged_probable_match_events ex: {ex.args}")

    def Probable_Match_Events_by_enrollment_groups_counts(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(), self.d)
            self.logger.info(f"dashboard dropdown visible: {dashboard_select_dropdown.is_displayed()}")
            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(), self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH, insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                self.logger.info(f"dashboard option list count: {len(dashboard_options_list)}")
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option: {option.text}")
                        if option.text == insight_dashboard_read_ini().probable_match_events_dashboard_option_text():
                            self.logger.info(f"{option.text} option selected")
                            option.click()
                            probable_match_events_by_enrollment_groups_label = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().Probable_Match_Events_by_Enrollment_Group_label_by_xpath(), self.d)
                            self.logger.info(f"probable_match_events_by_enrollment_groups_label visible: {probable_match_events_by_enrollment_groups_label.is_displayed()}")
                            if probable_match_events_by_enrollment_groups_label.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
                            probable_match_events_by_enrollment_groups_chart = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().Probable_Match_Events_by_Enrollment_Group_chart_by_xpath(), self.d)
                            self.logger.info(f"probable_match_events_by_enrollment_groups_chart visible: {probable_match_events_by_enrollment_groups_chart.is_displayed()}")
                            if probable_match_events_by_enrollment_groups_chart.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
            self.logger.info(f"x: {x}")
            if False in x:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_10_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"Probable_Match_Events_by_enrollment_groups_counts ex: {ex.args}")

    def tagged_probable_match_events_by_tag_type(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH",
                               insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH",
                                                           insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(),
                                                           self.d)
            self.logger.info(f"dashboard dropdown visible: {dashboard_select_dropdown.is_displayed()}")
            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH",
                                   insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(),
                                   self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH,
                                                              insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                self.logger.info(f"dashboard option list count: {len(dashboard_options_list)}")
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option: {option.text}")
                        if option.text == insight_dashboard_read_ini().probable_match_events_dashboard_option_text():
                            self.logger.info(f"{option.text} option selected")
                            option.click()
                            Tagged_Probable_Match_Events_by_Tag_Type_label = self.explicit_wait(5, "XPATH",
                                                                                                  insight_dashboard_read_ini().Tagged_Probable_Match_Events_by_Tag_Type_label_by_xpath(),
                                                                                                  self.d)
                            self.logger.info(
                                f"Tagged_Probable_Match_Events_by_Tag_Type_label visible: {Tagged_Probable_Match_Events_by_Tag_Type_label.is_displayed()}")
                            if Tagged_Probable_Match_Events_by_Tag_Type_label.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
                            Tagged_Probable_Match_Events_by_Tag_Type_chart = self.explicit_wait(5, "XPATH",
                                                                                                  insight_dashboard_read_ini().Tagged_Probable_Match_Events_by_Tag_Type_chart_by_xpath(),
                                                                                                  self.d)
                            self.logger.info(
                                f"Tagged_Probable_Match_Events_by_Tag_Type_chart visible: {Tagged_Probable_Match_Events_by_Tag_Type_chart.is_displayed()}")
                            if Tagged_Probable_Match_Events_by_Tag_Type_chart.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
            self.logger.info(f"x: {x}")
            if False in x:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_11_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"tagged_probable_match_events_by_tag_type ex: {ex.args}")

    def able_to_see_counts_on_Probable_Match_Events_dashboard_organisation_and_individual_groups(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH",
                               insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH",
                                                           insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(),
                                                           self.d)
            self.logger.info(f"dashboard dropdown visible: {dashboard_select_dropdown.is_displayed()}")
            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH",
                                   insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(),
                                   self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH,
                                                              insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                self.logger.info(f"dashboard option list count: {len(dashboard_options_list)}")
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option: {option.text}")
                        if option.text == insight_dashboard_read_ini().probable_match_events_dashboard_option_text():
                            self.logger.info(f"{option.text} option selected")
                            option.click()
                            enrollment_group_dropdown = self.explicit_wait(5, "XPATH",
                                                                           insight_dashboard_read_ini().enrollment_group_dropdown_by_xpath(),
                                                                           self.d)
                            if enrollment_group_dropdown:
                                enrollment_group_dropdown.click()
                                time.sleep(web_driver.one_second)
                            enrollment_groups_list = self.d.find_elements(By.XPATH,
                                                                          insight_dashboard_read_ini().enrollment_group_list_by_xpath())
                            enrollment_group_dropdown.click()
                            if enrollment_groups_list:
                                enrollment_group_dropdown.click()
                                for eg in enrollment_groups_list:
                                    self.logger.info(f"eg enlisted: {eg.text}")
                                    if eg.text.isalnum():
                                        eg.click()

                                        Deterred_Probable_Match_Events_label = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().Deterred_Probable_Match_Events_label_by_xpath(), self.d)
                                        self.logger.info(f"Deterred_Probable_Match_Events_label visible: {Deterred_Probable_Match_Events_label.is_displayed()}")
                                        self.logger.info(f"Deterred_Probable_Match_Events_label text: {Deterred_Probable_Match_Events_label.text}")
                                        if Deterred_Probable_Match_Events_label:
                                            if Deterred_Probable_Match_Events_label.is_displayed():
                                                x.append(True)
                                            else:
                                                x.append(False)
                                        else:
                                            x.append(False)
                                        Deterred_Probable_Match_Events_count = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().Deterred_Probable_Match_Events_count_by_xpath(), self.d)
                                        self.logger.info(f"Deterred_Probable_Match_Events_count visible: {Deterred_Probable_Match_Events_count.is_displayed()}")
                                        self.logger.info(f"Deterred_Probable_Match_Events_count count: {Deterred_Probable_Match_Events_count.text}")
                                        if Deterred_Probable_Match_Events_count:
                                            if Deterred_Probable_Match_Events_count.is_displayed():
                                                x.append(True)
                                            else:
                                                x.append(False)
                                        else:
                                            x.append(False)
                                        Total_Tagged_Probable_Match_Events_label_by_xpath = self.explicit_wait(5, "XPATH",
                                                                                                  insight_dashboard_read_ini().Total_Tagged_Probable_Match_Events_label_by_xpath(),
                                                                                                  self.d)
                                        self.logger.info(
                                            f"Total_Tagged_Probable_Match_Events_label_by_xpath visible: {Total_Tagged_Probable_Match_Events_label_by_xpath.is_displayed()}")
                                        self.logger.info(
                                            f"Total_Tagged_Probable_Match_Events_label_by_xpath count: {Total_Tagged_Probable_Match_Events_label_by_xpath.text}")
                                        if Total_Tagged_Probable_Match_Events_label_by_xpath:
                                            if Total_Tagged_Probable_Match_Events_label_by_xpath.is_displayed():
                                                x.append(True)
                                            else:
                                                x.append(False)
                                        else:
                                            x.append(False)
                                        Total_Tagged_Probable_Match_Events_count_by_xpath = self.explicit_wait(5, "XPATH",
                                                                                                               insight_dashboard_read_ini().Total_Tagged_Probable_Match_Events_count_by_xpath(),
                                                                                                               self.d)
                                        self.logger.info(
                                            f"Total_Tagged_Probable_Match_Events_count_by_xpath visible: {Total_Tagged_Probable_Match_Events_count_by_xpath.is_displayed()}")
                                        self.logger.info(
                                            f"Total_Tagged_Probable_Match_Events_count_by_xpath count: {Total_Tagged_Probable_Match_Events_count_by_xpath.text}")
                                        if Total_Tagged_Probable_Match_Events_count_by_xpath:
                                            if Total_Tagged_Probable_Match_Events_count_by_xpath.is_displayed():
                                                x.append(True)
                                            else:
                                                x.append(False)
                                        else:
                                            x.append(False)
                                        Serious_Offender_Tagged_Probable_Match_Events_label_by_xpath = self.explicit_wait(5, "XPATH",
                                                                                                               insight_dashboard_read_ini().Serious_Offender_Tagged_Probable_Match_Events_label_by_xpath(),
                                                                                                               self.d)
                                        self.logger.info(
                                            f"Serious_Offender_Tagged_Probable_Match_Events_label_by_xpath visible: {Serious_Offender_Tagged_Probable_Match_Events_label_by_xpath.is_displayed()}")
                                        self.logger.info(
                                            f"Serious_Offender_Tagged_Probable_Match_Events_label_by_xpath count: {Serious_Offender_Tagged_Probable_Match_Events_label_by_xpath.text}")
                                        if Serious_Offender_Tagged_Probable_Match_Events_label_by_xpath:
                                            if Serious_Offender_Tagged_Probable_Match_Events_label_by_xpath.is_displayed():
                                                x.append(True)
                                            else:
                                                x.append(False)
                                        else:
                                            x.append(False)
                                        Serious_Offender_Tagged_Probable_Match_Events_count_by_xpath = self.explicit_wait(5,
                                                                                                                          "XPATH",
                                                                                                                          insight_dashboard_read_ini().Serious_Offender_Tagged_Probable_Match_Events_count_by_xpath(),
                                                                                                                          self.d)
                                        self.logger.info(
                                            f"Serious_Offender_Tagged_Probable_Match_Events_count_by_xpath visible: {Serious_Offender_Tagged_Probable_Match_Events_count_by_xpath.is_displayed()}")
                                        self.logger.info(
                                            f"Serious_Offender_Tagged_Probable_Match_Events_count_by_xpath count: {Serious_Offender_Tagged_Probable_Match_Events_count_by_xpath.text}")
                                        if Serious_Offender_Tagged_Probable_Match_Events_count_by_xpath:
                                            if Serious_Offender_Tagged_Probable_Match_Events_count_by_xpath.is_displayed():
                                                x.append(True)
                                            else:
                                                x.append(False)
                                        else:
                                            x.append(False)
                                        Total_Probable_Match_Events_label_by_xpath_1 = self.explicit_wait(5,
                                                                                                                          "XPATH",
                                                                                                                          insight_dashboard_read_ini().Total_Probable_Match_Events_label_by_xpath_1(),
                                                                                                                          self.d)
                                        self.logger.info(
                                            f"Total_Probable_Match_Events_label_by_xpath_1 visible: {Total_Probable_Match_Events_label_by_xpath_1.is_displayed()}")
                                        self.logger.info(
                                            f"Total_Probable_Match_Events_label_by_xpath_1 count: {Total_Probable_Match_Events_label_by_xpath_1.text}")
                                        if Total_Probable_Match_Events_label_by_xpath_1:
                                            if Total_Probable_Match_Events_label_by_xpath_1.is_displayed():
                                                x.append(True)
                                            else:
                                                x.append(False)
                                        else:
                                            x.append(False)
                                        Total_Probable_Match_Events_count_by_xpath_1 = self.explicit_wait(5,
                                                                                                          "XPATH",
                                                                                                          insight_dashboard_read_ini().Total_Probable_Match_Events_count_by_xpath_1(),
                                                                                                          self.d)
                                        self.logger.info(
                                            f"Total_Probable_Match_Events_count_by_xpath_1 visible: {Total_Probable_Match_Events_count_by_xpath_1.is_displayed()}")
                                        self.logger.info(
                                            f"Total_Probable_Match_Events_count_by_xpath_1 count: {Total_Probable_Match_Events_count_by_xpath_1.text}")
                                        if Total_Probable_Match_Events_count_by_xpath_1:
                                            if Total_Probable_Match_Events_count_by_xpath_1.is_displayed():
                                                x.append(True)
                                            else:
                                                x.append(False)
                                        else:
                                            x.append(False)

            self.logger.info(f"x: {x}")
            if False in x:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_12_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"able_to_see_counts_on_Probable_Match_Events_dashboard_organisation_and_individual_groups ex:{ex.args}")

    def select_enrollment_dashboard_option_and_verify_cumulative_enrollments_by_date(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH",
                               insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH",
                                                           insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(),
                                                           self.d)
            self.logger.info(f"dashboard dropdown visible: {dashboard_select_dropdown.is_displayed()}")
            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH",
                                   insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(),
                                   self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH,
                                                              insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                self.logger.info(f"dashboard option list count: {len(dashboard_options_list)}")
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option: {option.text}")
                        if option.text == insight_dashboard_read_ini().enrollments_dashboard_text():
                            self.logger.info(f"{option.text} option selected")
                            option.click()
                            time.sleep(web_driver.two_second)
                            Cumulative_Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath = self.explicit_wait(5, "XPATH",
                                                                                                  insight_dashboard_read_ini().Cumulative_Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath(),
                                                                                                  self.d)
                            self.logger.info(
                                f"Cumulative_Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath visible: {Cumulative_Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if Cumulative_Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
                            Cumulative_Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath = self.explicit_wait(5, "XPATH",
                                                                                                  insight_dashboard_read_ini().Cumulative_Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath(),
                                                                                                  self.d)
                            self.logger.info(
                                f"Cumulative_Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath visible: {Cumulative_Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if Cumulative_Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
            self.logger.info(f"x: {x}")
            if False in x:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_17_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"select_enrollment_dashboard_option_and_verify_cumulative_enrollments_by_date: {ex.args}")

    def enrollments_by_date_counts_on_enrollment_dashboard(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH",
                                                           insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(),
                                                           self.d)
            self.logger.info(f"dashboard dropdown visible: {dashboard_select_dropdown.is_displayed()}")
            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH",
                                   insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(),
                                   self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH,
                                                              insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                self.logger.info(f"dashboard option list count: {len(dashboard_options_list)}")
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option: {option.text}")
                        if option.text == insight_dashboard_read_ini().enrollments_dashboard_text():
                            self.logger.info(f"{option.text} option selected")
                            option.click()
                            time.sleep(web_driver.two_second)
                            Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath(),
                                self.d)
                            self.logger.info(
                                f"Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath visible: {Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if Enrollments_by_Date_label_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
                            Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath(),
                                self.d)
                            self.logger.info(
                                f"Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath visible: {Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if Enrollments_by_Date_chart_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
            self.logger.info(f"x: {x}")
            if False in x:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_18_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"enrollments_by_date_counts_on_enrollment_dashboard ex: {ex.args}")

    def enrollments_by_enrollment_group_counts(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH",
                               insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH",
                                                           insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(),
                                                           self.d)
            self.logger.info(f"dashboard dropdown visible: {dashboard_select_dropdown.is_displayed()}")
            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH",
                                   insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(),
                                   self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH,
                                                              insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                self.logger.info(f"dashboard option list count: {len(dashboard_options_list)}")
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option: {option.text}")
                        if option.text == insight_dashboard_read_ini().enrollments_dashboard_text():
                            self.logger.info(f"{option.text} option selected")
                            option.click()
                            time.sleep(web_driver.two_second)
                            enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath(),
                                self.d)
                            self.logger.info(f"enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath visible: {enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
                            enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath(),
                                self.d)
                            self.logger.info(f"enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath visible: {enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
            self.logger.info(f"x: {x}")
            if False in x:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_19_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"enrollments_by_enrollment_group_counts ex: {ex.args}")

    def enrollments_by_week_org_counts(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH",
                               insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH",
                                                           insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(),
                                                           self.d)
            self.logger.info(f"dashboard dropdown visible: {dashboard_select_dropdown.is_displayed()}")
            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH",
                                   insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(),
                                   self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH,
                                                              insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                self.logger.info(f"dashboard option list count: {len(dashboard_options_list)}")
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option: {option.text}")
                        if option.text == insight_dashboard_read_ini().enrollments_dashboard_text():
                            self.logger.info(f"{option.text} option selected")
                            option.click()
                            time.sleep(web_driver.two_second)
                            enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath(), self.d)
                            self.logger.info(f"enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath visible: {enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
                            enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath = self.explicit_wait(5, "XPATH", insight_dashboard_read_ini().enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath(), self.d)
                            self.logger.info(f"enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath visible: {enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
            self.logger.info(f"x: {x}")
            if False in x:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_20_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"enrollments_by_week_org_counts ex: {ex.args}")

    def Enrollments_by_status_count(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH",
                               insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH",
                                                           insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(),
                                                           self.d)
            self.logger.info(f"dashboard dropdown visible: {dashboard_select_dropdown.is_displayed()}")
            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH",
                                   insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(),
                                   self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH,
                                                              insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                self.logger.info(f"dashboard option list count: {len(dashboard_options_list)}")
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option: {option.text}")
                        if option.text == insight_dashboard_read_ini().enrollments_dashboard_text():
                            self.logger.info(f"{option.text} option selected")
                            option.click()
                            time.sleep(web_driver.two_second)
                            Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath(),
                                self.d)
                            self.logger.info(
                                f"Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath visible: {Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
                            Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath(),
                                self.d)
                            self.logger.info(
                                f"Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath visible: {Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
            self.logger.info(f"x: {x}")
            if False in x:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_21_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"Enrollments_by_status_count ex: {ex.args}")

    def user_is_able_to_see_on_enrollment_dashboard_as_enrollment_overview_and_cumulative_enrollments_by_date(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH",
                               insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH",
                                                           insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(),
                                                           self.d)
            self.logger.info(f"dashboard dropdown visible: {dashboard_select_dropdown.is_displayed()}")
            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH",
                                   insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(),
                                   self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH,
                                                              insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                self.logger.info(f"dashboard option list count: {len(dashboard_options_list)}")
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option: {option.text}")
                        if option.text == insight_dashboard_read_ini().enrollments_dashboard_text():
                            self.logger.info(f"{option.text} option selected")
                            option.click()
                            time.sleep(web_driver.two_second)
                            cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath_1(),
                                self.d)
                            self.logger.info(
                                f"cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath visible: {cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
                            cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath_1(),
                                self.d)
                            self.logger.info(
                                f"cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath visible: {cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
            self.logger.info(f"x: {x}")
            if False in x:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_21_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"user_is_able_to_see_on_enrollment_dashboard_as_enrollment_overview_and_cumulative_enrollments_by_date ex: {ex.args}")

    def enrollment_by_date_counts_as_mention_in_link_organisation_and_individual_group(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH",
                               insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH",
                                                           insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(),
                                                           self.d)
            self.logger.info(f"dashboard dropdown visible: {dashboard_select_dropdown.is_displayed()}")
            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH",
                                   insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(),
                                   self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH,
                                                              insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                self.logger.info(f"dashboard option list count: {len(dashboard_options_list)}")
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option: {option.text}")
                        if option.text == insight_dashboard_read_ini().enrollments_dashboard_text():
                            self.logger.info(f"{option.text} option selected")
                            option.click()
                            time.sleep(web_driver.two_second)
                            cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath_1(),
                                self.d)
                            self.logger.info(
                                f"cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath visible: {cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if cumulative_enrollments_by_date_label_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
                            cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath_1(),
                                self.d)
                            self.logger.info(
                                f"cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath visible: {cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if cumulative_enrollments_by_date_chart_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
            self.logger.info(f"x: {x}")
            if False in x:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_21_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"enrollment_by_date_counts_as_mention_in_link_organisation_and_individual_group ex:{ex.args}")

    def enrollments_by_enrollment_group_counts_as_mention_in_link_organisation_and_individual_group(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH",
                               insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH",
                                                           insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(),
                                                           self.d)
            self.logger.info(f"dashboard dropdown visible: {dashboard_select_dropdown.is_displayed()}")
            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH",
                                   insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(),
                                   self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH,
                                                              insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                self.logger.info(f"dashboard option list count: {len(dashboard_options_list)}")
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option: {option.text}")
                        if option.text == insight_dashboard_read_ini().enrollments_dashboard_text():
                            self.logger.info(f"{option.text} option selected")
                            option.click()
                            time.sleep(web_driver.two_second)
                            enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath(),
                                self.d)
                            self.logger.info(
                                f"enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath visible: {enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if enrollments_by_enrollment_group_label_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
                            enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath(),
                                self.d)
                            self.logger.info(
                                f"enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath visible: {enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if enrollments_by_enrollment_group_chart_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
            self.logger.info(f"x: {x}")
            if False in x:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_19_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"enrollments_by_enrollment_group_counts_as_mention_in_link_organisation_and_individual_group ex: {ex.args}")

    def enrollments_by_week_counts_as_mention_in_link_organisation_and_individual_groups(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH",
                               insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH",
                                                           insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(),
                                                           self.d)
            self.logger.info(f"dashboard dropdown visible: {dashboard_select_dropdown.is_displayed()}")
            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH",
                                   insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(),
                                   self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH,
                                                              insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                self.logger.info(f"dashboard option list count: {len(dashboard_options_list)}")
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option: {option.text}")
                        if option.text == insight_dashboard_read_ini().enrollments_dashboard_text():
                            self.logger.info(f"{option.text} option selected")
                            option.click()
                            time.sleep(web_driver.two_second)
                            Enrollments_by_Week_label_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().Enrollments_by_Week_label_on_enrollment_dashboard_by_xpath(),
                                self.d)
                            self.logger.info(
                                f"Enrollments_by_Week_label_on_enrollment_dashboard_by_xpath visible: {Enrollments_by_Week_label_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if Enrollments_by_Week_label_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
                            Enrollments_by_Week_chart_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().Enrollments_by_Week_chart_on_enrollment_dashboard_by_xpath(),
                                self.d)
                            self.logger.info(
                                f"Enrollments_by_Week_chart_on_enrollment_dashboard_by_xpath visible: {Enrollments_by_Week_chart_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if Enrollments_by_Week_chart_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
            self.logger.info(f"x: {x}")
            if False in x:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_20_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(f"enrollments_by_week_counts_as_mention_in_link_organisation_and_individual_groups ex: {ex.args}")

    def Enrollments_by_Status_counts_organisation_and_individual_groups(self):
        try:
            x = []
            time.sleep(web_driver.one_second)
            self.explicit_wait(5, "XPATH",
                               insight_dashboard_read_ini().loss_prevented_by_enrollment_group_chart_by_xpath(), self.d)
            dashboard_select_dropdown = self.explicit_wait(5, "XPATH",
                                                           insight_dashboard_read_ini().dashboard_select_dropdown_by_xpath(),
                                                           self.d)
            self.logger.info(f"dashboard dropdown visible: {dashboard_select_dropdown.is_displayed()}")
            if dashboard_select_dropdown.is_displayed():
                dashboard_select_dropdown.click()
                self.explicit_wait(5, "XPATH",
                                   insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath(),
                                   self.d)
                dashboard_options_list = self.d.find_elements(By.XPATH,
                                                              insight_dashboard_read_ini().options_inside_dashboard_select_dropdown_by_xpath())
                self.logger.info(f"dashboard option list count: {len(dashboard_options_list)}")
                if len(dashboard_options_list) > 0:
                    for option in dashboard_options_list:
                        self.logger.info(f"option: {option.text}")
                        if option.text == insight_dashboard_read_ini().enrollments_dashboard_text():
                            self.logger.info(f"{option.text} option selected")
                            option.click()
                            time.sleep(web_driver.two_second)
                            Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath(),
                                self.d)
                            self.logger.info(
                                f"Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath visible: {Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if Enrollments_by_Status_label_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
                            Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath = self.explicit_wait(
                                5, "XPATH",
                                insight_dashboard_read_ini().Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath(),
                                self.d)
                            self.logger.info(
                                f"Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath visible: {Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath.is_displayed()}")
                            if Enrollments_by_Status_chart_on_enrollment_dashboard_by_xpath.is_displayed():
                                x.append(True)
                            else:
                                x.append(False)
            self.logger.info(f"x: {x}")
            if False in x:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_Insight_Dashboard_21_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"Enrollments_by_Status_counts_organisation_and_individual_groups ex:{ex.args}")
