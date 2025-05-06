import time
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from selenium.webdriver.common.by import By
from All_Config_Packages._2_Portal_Menu_Module_Config_Files.Portal_Menu_Module_Read_INI import \
    Portal_Menu_Module_read_ini
from All_Config_Packages._0_login_logout_config_file.login_logout_read_ini import LoginLogout_Read_ini
from Base_Package.Login_Logout_Ops import login
from Base_Package.Login_Logout_Ops import logout


class Portal_Menu_Module_pom(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    def load_portal_login_page_if_not_loaded(self):
        try:
            if self.d.title != None and self.d.title == LoginLogout_Read_ini().get_portal_title():
                self.logger.info("title is none or matching")
                pass
            else:
                self.logger.info(" no url ")
                self.d.get(LoginLogout_Read_ini().get_portal_url())

                self.d.maximize_window()
                time.sleep(web_driver.two_second)
                # self.d.find_element(By.XPATH, LoginLogout_Read_ini().get_advance_btn_by_xpath()).click()
                # self.logger.info("clicked on advance")
                # time.sleep(web_driver.one_second)
                # self.logger.info(f"proceed link xpath: {LoginLogout_Read_ini().get_proceed_link_by_xpath()}")
                # self.d.find_element(By.XPATH, LoginLogout_Read_ini().get_proceed_link_by_xpath()).click()
                # self.logger.info("clicked on proceed link")
                # time.sleep(web_driver.one_second)
            return self.d
        except Exception as ex:
            self.logger.error(ex)

    # def wait_for_element_to_appear(self, element_list, xpath):
    #     count = 0
    #     if len(element_list) == 0:
    #         while len(element_list) == 0 or count == 10:
    #             element_list = self.d.find_elements(By.XPATH, xpath)
    #             time.sleep(web_driver.one_second)
    #             if len(element_list) > 0:
    #                 self.logger.info("element is visible...")
    #                 return element_list[0]
    #             else:
    #                 self.logger.info("waiting for element...")
    #             count += 1
    #             self.logger.info(f"wait count: {count}")
    #     else:
    #         self.logger.info(f"element length: {len(element_list)}")
    #         return element_list[0]

    def Verify_events_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_1 started ********")
            self.status.clear()
            # # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            # login().login_to_localhost_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10,"XPATH",Portal_Menu_Module_read_ini().get_events_menu_by_xpath(), self.d)
            events_menu_list = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_events_menu_by_xpath())
            time.sleep(web_driver.two_second)
            events_menu = self.explicit_wait(5, "XPATH", Portal_Menu_Module_read_ini().get_events_menu_by_xpath(), self.d)
            expected_title = Portal_Menu_Module_read_ini().get_expected_events_text()
            if events_menu.is_displayed():
                if events_menu.text == expected_title:
                    self.logger.info(f"Events menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            time.sleep(web_driver.two_second)
            exclamatory_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_events_menu_by_xpath() + icon)
            if exclamatory_icon.is_displayed():
                self.logger.info("exclamatory icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            events_menu.click()
            time.sleep(web_driver.two_second)
            actual_title_list = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_title_on_Events_panel_by_xpath())

            actual_title = self.explicit_wait(5, "XPATH", Portal_Menu_Module_read_ini().get_title_on_Events_panel_by_xpath(), self.d)
            self.logger.info(f"actual title: {actual_title.text}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title.text == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn_list = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())

            close_panel_btn = self.explicit_wait(5, "XPATH", Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath(), self.d)
            close_panel_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"status: {self.status}")

            if False in self.status:
                self.logger.error(f"screenshot file path: {web_driver.screenshots_path}\\TC_PM_1.png")
                self.d.save_screenshot(f"{web_driver.screenshots_path}\\TC_PM_1.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {web_driver.screenshots_path}\\TC_PM_1_exception.png")
            self.d.save_screenshot(f"{web_driver.screenshots_path}\\TC_PM_1_exception.png")
            self.logger.error(f"TC_PM_1 got exception as: {ex}")

    def Verify_tags_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_2 started ********")
            self.status.clear()
            time.sleep(web_driver.two_second)
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Tags_menu_by_xpath(), self.d)
            tags_menu_list = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_Tags_menu_by_xpath())

            tags_menu = self.explicit_wait(5, "XPATH", Portal_Menu_Module_read_ini().get_Tags_menu_by_xpath(), self.d)
            expected_title = Portal_Menu_Module_read_ini().get_expected_tags_text()
            time.sleep(web_driver.one_second)
            if tags_menu.is_displayed():
                if tags_menu.text == expected_title:
                    self.logger.info(f"Tags menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            tag_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Tags_menu_by_xpath() + icon)
            if tag_icon.is_displayed():
                self.logger.info("tag icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            tags_menu.click()
            time.sleep(web_driver.two_second)
            actual_title_list = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_title_on_Tags_panel_by_xpath())

            actual_title = self.explicit_wait(5, "XPATH", Portal_Menu_Module_read_ini().get_title_on_Tags_panel_by_xpath(), self.d)
            self.logger.info(f"actual title: {actual_title.text}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title.text == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn_list = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())

            close_panel_btn = self.explicit_wait(5, "XPATH", Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath(), self.d)
            close_panel_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_2.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_2.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_2_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_2_exception.png")
            self.logger.error(f"TC_PM_2 got exception as: {ex}")

    def Verify_Identify_and_Enroll_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_3 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Identify_and_Enroll_menu_by_xpath(), self.d)
            identify_enroll_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                       get_Identify_and_Enroll_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_identify_enroll_text()

            if identify_enroll_menu.is_displayed():
                if identify_enroll_menu.text == expected_title:
                    self.logger.info(f"Identify & Enroll menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            camera_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                              get_Identify_and_Enroll_menu_by_xpath() + icon)
            time.sleep(web_driver.two_second)
            if camera_icon.is_displayed():
                self.logger.info("camera icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            identify_enroll_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Identify_Enroll_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_close_panel_button_by_xpath())
            close_panel_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_3.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_3.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_3_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_3_exception.png")
            self.logger.error(f"TC_PM_3 got exception as: {ex}")

    def Verify_Detect_Faces_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_4 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                                                    get_Detect_Faces_menu_by_xpath(), self.d)
            detect_faces_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                    get_Detect_Faces_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_detect_faces_text()

            if detect_faces_menu.is_displayed():
                if detect_faces_menu.text == expected_title:
                    self.logger.info(f"Detect Faces menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            camera_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                              get_Detect_Faces_menu_by_xpath() + icon)
            if camera_icon.is_displayed():
                self.logger.info("camera icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            detect_faces_menu.click()
            time.sleep(web_driver.three_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Detect_Faces_panel_by_xpath()).text

            self.logger.info(f"actual title: {actual_title}")
            expected_title = Portal_Menu_Module_read_ini().get_expected_detect_faces_text()
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_close_panel_button_by_xpath())
            close_panel_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_4.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_4.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_4_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_4_exception.png")
            self.logger.error(f"TC_PM_4 got exception as: {ex}")

    def Verify_Enrollments_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_5 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                                                   get_Enrollments_menu_by_xpath(), self.d)
            enrollments_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                   get_Enrollments_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_enrollments_text()

            if enrollments_menu.is_displayed():
                if enrollments_menu.text == expected_title:
                    self.logger.info(f"Enrollments menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            person_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Enrollments_menu_by_xpath() +
                                              icon)
            if person_icon.is_displayed():
                self.logger.info("person icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            enrollments_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Enrollments_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_close_panel_button_by_xpath())
            close_panel_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_5.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_5.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_5_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_5_exception.png")
            self.logger.error(f"TC_PM_5 got exception as: {ex}")

    def Verify_Enrollment_Groups_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_6 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Enrollment_Groups_menu_by_xpath(), self.d)
            enrollment_groups_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Enrollment_Groups_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_enrollment_groups_text()

            if enrollment_groups_menu.is_displayed():
                if enrollment_groups_menu.text == expected_title:
                    self.logger.info(f"Enrollment Groups menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            group_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                             get_Enrollment_Groups_menu_by_xpath() + icon)
            if group_icon.is_displayed():
                self.logger.info("group icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            enrollment_groups_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Enrollment_Groups_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_close_panel_button_by_xpath())
            close_panel_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_6.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_6.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_6_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_6_exception.png")
            self.logger.error(f"TC_PM_6 got exception as: {ex}")

    def Verify_Notification_Groups_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_7 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Notification_Groups_menu_by_xpath(), self.d)
            notification_groups_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Notification_Groups_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_notification_groups_text()

            if notification_groups_menu.is_displayed():
                if notification_groups_menu.text == expected_title:
                    self.logger.info(f"Notification Groups menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            alert_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                             get_Notification_Groups_menu_by_xpath() + icon)
            if alert_icon.is_displayed():
                self.logger.info("alert icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            notification_groups_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Notification_Groups_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_close_panel_button_by_xpath())
            close_panel_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_7.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_7.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_7_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_7_exception.png")
            self.logger.error(f"TC_PM_5 got exception as: {ex}")

    def Verify_Visitor_Search_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_8 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                                                      get_Visitor_Search_menu_by_xpath(), self.d)
            visitor_search_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                      get_Visitor_Search_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_visitor_search_text()

            if visitor_search_menu.is_displayed():
                if visitor_search_menu.text == expected_title:
                    self.logger.info(f"Visitor Search menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            search_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                              get_Visitor_Search_menu_by_xpath() + icon)
            if search_icon.is_displayed():
                self.logger.info("search icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            visitor_search_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Visitor_Search_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_close_panel_button_by_xpath())
            close_panel_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_8.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_8.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_8_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_8_exception.png")
            self.logger.error(f"TC_PM_8 got exception as: {ex}")

    def Verify_Visitor_Search_Jobs_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_9 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                                                           get_Visitor_Search_Jobs_menu_by_xpath(), self.d)
            visitor_search_jobs_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                           get_Visitor_Search_Jobs_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_visitor_search_jobs_text()

            if visitor_search_jobs_menu.is_displayed():
                if visitor_search_jobs_menu.text == visitor_search_jobs_menu:
                    self.logger.info(f"Visitor Search Jobs menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            list_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                            get_Visitor_Search_Jobs_menu_by_xpath() + icon)
            if list_icon.is_displayed():
                self.logger.info("list icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            visitor_search_jobs_menu.click()
            time.sleep(web_driver.three_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Visitor_Search_Jobs_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_close_panel_button_by_xpath())
            close_panel_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_9.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_9.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_9_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_9_exception.png")
            self.logger.error(f"TC_PM_9 got exception as: {ex}")

    def Verify_Notes_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_10 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Notes_menu_by_xpath(), self.d)
            notes_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Notes_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_notes_text()

            if notes_menu.is_displayed():
                if notes_menu.text == expected_title:
                    self.logger.info(f"Notes menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            notes_icon = self.d.find_element(By.XPATH,
                                           Portal_Menu_Module_read_ini().get_Notes_menu_by_xpath() + icon)
            if notes_icon.is_displayed():
                self.logger.info("notes icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            notes_menu.click()
            time.sleep(web_driver.three_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Notes_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_close_panel_button_by_xpath())
            close_panel_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_10.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_10.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_10_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_10_exception.png")
            self.logger.error(f"TC_PM_10 got exception as: {ex}")

    def Verify_Locations_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_11 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Locations_menu_by_xpath(), self.d)
            locations_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Locations_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_locations_text()
            if locations_menu.is_displayed():
                if locations_menu.text == expected_title:
                    self.logger.info(f"Locations menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            location_icon = self.d.find_element(By.XPATH,
                                           Portal_Menu_Module_read_ini().get_Locations_menu_by_xpath() + icon)
            if location_icon.is_displayed():
                self.logger.info("location icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            locations_menu.click()
            time.sleep(web_driver.two_second)
            cancel_button = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                get_cancel_button_on_location_panel_by_xpath())
            if cancel_button.is_displayed():
                cancel_button.click()
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_close_panel_button_by_xpath())
            close_panel_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_11.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_11.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_11_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_11_exception.png")
            self.logger.error(f"TC_PM_11 got exception as: {ex}")

    def Verify_Users_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_12 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Users_menu_by_xpath(), self.d)
            users_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Users_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_users_text()

            if users_menu.is_displayed():
                if users_menu.text == expected_title:
                    self.logger.info(f"Users menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            user_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Users_menu_by_xpath() + icon)
            if user_icon.is_displayed():
                self.logger.info("user icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            users_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Users_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_close_panel_button_by_xpath())
            close_panel_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_12.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_12.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_12_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_12_exception.png")
            self.logger.error(f"TC_PM_12 got exception as: {ex}")

    def Verify_User_Roles_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_13 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                                                  get_User_Roles_menu_by_xpath(), self.d)
            user_roles_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_User_Roles_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_user_roles_text()

            if user_roles_menu.is_displayed():
                if user_roles_menu.text == expected_title:
                    self.logger.info(f"User Roles menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            user_roles_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_User_Roles_menu_by_xpath()
                                                  + icon)
            if user_roles_icon.is_displayed():
                self.logger.info("user roles icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            user_roles_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_User_Roles_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_close_panel_button_by_xpath())
            close_panel_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_13.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_13.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_13_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_13_exception.png")
            self.logger.error(f"TC_PM_13 got exception as: {ex}")

    def Verify_Zones_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_14 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Zones_menu_by_xpath(), self.d)
            zones_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Zones_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_zones_text()

            if zones_menu.is_displayed():
                if zones_menu.text == expected_title:
                    self.logger.info(f"Zones menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            dot_circle_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Zones_menu_by_xpath() +
                                                  icon)
            if dot_circle_icon.is_displayed():
                self.logger.info("dot circle icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            zones_menu.click()
            time.sleep(web_driver.three_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Zones_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            expected_title = Portal_Menu_Module_read_ini().get_expected_zones_text()
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_close_panel_button_by_xpath())
            close_panel_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_14.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_14.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_14_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_14_exception.png")
            self.logger.error(f"TC_PM_14 got exception as: {ex}")

    def Verify_Account_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_15 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Account_menu_by_xpath(), self.d)
            account_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Account_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_account_text()
            if account_menu.is_displayed():
                if account_menu.text == expected_title:
                    self.logger.info(f"Account menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            lock_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Account_menu_by_xpath() + icon)
            if lock_icon.is_displayed():
                self.logger.info("lock icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            account_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Account_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_close_panel_button_by_xpath())
            close_panel_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_15.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_15.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_15_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_15_exception.png")
            self.logger.error(f"TC_PM_15 got exception as: {ex}")

    def Verify_Reporting_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_16 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Reporting_menu_by_xpath(), self.d)
            reporting_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Reporting_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_reporting_text()

            if reporting_menu.is_displayed():
                if reporting_menu.text == expected_title:
                    self.logger.info(f"Reporting menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            chart_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Reporting_menu_by_xpath() +
                                             icon)
            time.sleep(web_driver.two_second)
            if chart_icon.is_displayed():
                self.logger.info("chart icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            reporting_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Reporting_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_close_panel_button_by_xpath())
            close_panel_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_16.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_16.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_16_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_16_exception.png")
            self.logger.error(f"TC_PM_16 got exception as: {ex}")

    def Verify_Dashboard_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_17 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            dashboard_menu = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Dashboard_menu_by_xpath(), self.d)
            # dashboard_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Dashboard_menu_by_xpath())
            expected_text = Portal_Menu_Module_read_ini().get_expected_dashboard_text()
            if dashboard_menu.is_displayed():
                if dashboard_menu.text == expected_text:
                    self.logger.info(f"Dashboard menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            dollar_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                              get_dollar_icon_on_dashboard_menu_by_xpath())
            if dollar_icon.is_displayed():
                self.logger.info("dollar icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            dashboard_menu.click()
            time.sleep(web_driver.two_second)
            self.d.switch_to.window(self.d.window_handles[1])
            time.sleep(web_driver.three_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Dashboard_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            expected_title = Portal_Menu_Module_read_ini().get_expected_fidusvision_text()
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_17.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_17.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_17_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_17_exception.png")
            self.logger.error(f"TC_PM_17 got exception as: {ex}")
        finally:
            self.d.close()
            self.d.switch_to.window(self.d.window_handles[0])


    def Verify_Notifier_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_18 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Notifier_menu_by_xpath(), self.d)
            notifier_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Notifier_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_notifier_text()

            if notifier_menu.is_displayed():
                if notifier_menu.text == expected_title:
                    self.logger.info(f"Notifier menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = Portal_Menu_Module_read_ini().get_icon_by_xpath()
            horn_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Notifier_menu_by_xpath() + icon)
            time.sleep(web_driver.two_second)
            if horn_icon.is_displayed():
                self.logger.info("horn icon is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            notifier_menu.click()
            time.sleep(web_driver.two_second)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                               get_title_on_Notifier_panel_by_xpath()).text
            self.logger.info(f"actual title: {actual_title}")
            self.logger.info(f"expected title: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            close_notifier_panel_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                           get_close_notifier_button_by_xpath())
            close_notifier_panel_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_18.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_18.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_18_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_18_exception.png")
            self.logger.error(f"TC_PM_18 got exception as: {ex}")

    def Verify_Audit_Log_Report_menu_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_19 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_Audit_Log_Report_menu_by_xpath(), self.d)
            alr_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Audit_Log_Report_menu_by_xpath())
            expected_title = Portal_Menu_Module_read_ini().get_expected_audit_log_report_text()
            expected_select_report_criteria_text = Portal_Menu_Module_read_ini().get_select_report_criteria_heading()
            if alr_menu.is_displayed():
                if alr_menu.text == expected_title:
                    self.logger.info(f"Audit Log Report menu is visible in menu items...")
                    self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            alr_icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_shield_icon_on_alr_menu_by_xpath())
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)

            if alr_icon.is_displayed():
                self.logger.info("audit log report icon is visible..")
                self.status.append(True)
            else:
                self.logger.info("audit log report icon is not visible..")
                self.status.append(False)
            alr_menu.click()
            time.sleep(web_driver.two_second)
            # self.d.find_element(By.XPATH, "//main[@class='MuiBox-root css-1ruo4ps']").click()
            # self.d.find_element(By.XPATH, "//div[@id='root']").click()
            self.d.switch_to.window(self.d.window_handles[1])
            time.sleep(web_driver.three_second)
            alr = self.explicit_wait(20, "XPATH", Portal_Menu_Module_read_ini().get_select_report_criteria_heading_by_xpath(), self.d)
            # alr = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_title_on_Audit_Log_Report_panel_by_xpath(), self.d)
            self.logger.info(f'alr title visible: {alr.text}')
            if alr.is_displayed():
                self.logger.info("alr is visible")
                pass
            else:
                self.logger.info("alr is not visible")
                # self.d.switch_to.window(self.d.window_handles[1])
            time.sleep(web_driver.three_second)
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_select_report_criteria_heading_by_xpath(), self.d)
            actual_title = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_select_report_criteria_heading_by_xpath()).text
            self.logger.info(f"expected title: {expected_title}")
            self.logger.info(f"actual select report criteria text: {actual_title}")
            self.logger.info(f"expected select report criteria text: {expected_select_report_criteria_text}")
            time.sleep(web_driver.one_second)
            if actual_title == expected_select_report_criteria_text:
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_19.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_19.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_19_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_19_exception.png")
            self.logger.error(f"TC_PM_19 got exception as: {ex}")
        finally:
            # self.d.close()
            self.d.switch_to.window(self.d.window_handles[0])

    def click_on_events_menu_tags_menu_and_Identify_and_Enroll_menu_and_verify_Close_All_Panels_menu_is_visible_and_clickable(self):
        try:
            self.logger.info("********** TC_PM_20 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            web_driver.implicit_wait(self, 10, self.d)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_events_menu_by_xpath(), self.d)
            events = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_events_menu_by_xpath())
            tags = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Tags_menu_by_xpath())
            identify_enroll = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                  get_Identify_and_Enroll_menu_by_xpath())
            cloud_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath())
            events.click()
            time.sleep(web_driver.one_second)
            cloud_menu.click()
            tags.click()
            time.sleep(web_driver.one_second)
            cloud_menu.click()
            time.sleep(web_driver.two_second)
            identify_enroll.click()
            time.sleep(web_driver.one_second)
            cloud_menu.click()
            close_all_panels_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_close_all_panels_menu_by_xpath())
            time.sleep(web_driver.two_second)
            if close_all_panels_menu.is_displayed():
                self.logger.info("Close All Panels menu is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_text = close_all_panels_menu.text
            self.logger.info(f"actual text on menu: {actual_text}")
            expected_text = Portal_Menu_Module_read_ini().get_expected_close_all_panels_text()
            self.logger.info(f"expected text on menu: {expected_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            icon = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                       get_icon_on_close_all_panels_menu_by_xpath())
            if icon.is_displayed():
                self.logger.info("Icon on Close All Panels menu is visible..")
                self.status.append(True)
            else:
                self.status.append(False)

            if close_all_panels_menu.is_enabled():
                self.logger.info("'Close All Panels' menu is clickable...")
                self.status.append(True)
                close_all_panels_menu.click()
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_20.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_20.png")
                return False
            else:
                return True
            # logout().logout_from_core()

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_20_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_20_exception.png")
            self.logger.error(f"TC_PM_20 got exception as: {ex}")

    def click_on_Close_All_Panels_menu_and_verify_all_panels_are_closed_successfully(self):
        try:
            self.logger.info("********** TC_PM_21 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            time.sleep(web_driver.two_second)
            login().login_to_cloud_if_not_done(self.d)
            web_driver.implicit_wait(self, 10, self.d)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_events_menu_by_xpath(), self.d)
            events = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_events_menu_by_xpath())
            tags = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Tags_menu_by_xpath())
            identify_enroll = self.d.find_element(By.XPATH,
                                                  Portal_Menu_Module_read_ini().get_Identify_and_Enroll_menu_by_xpath())
            cloud_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_CLOUD_MENU_button_by_xpath())

            events.click()
            time.sleep(web_driver.one_second)
            cloud_menu.click()
            time.sleep(web_driver.two_second)
            tags.click()
            time.sleep(web_driver.one_second)
            cloud_menu.click()
            time.sleep(web_driver.two_second)
            identify_enroll.click()
            time.sleep(web_driver.one_second)
            cloud_menu.click()
            time.sleep(web_driver.two_second)
            close_all_panels_menu = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                        get_close_all_panels_menu_by_xpath())
            close_all_panels_menu.click()
            time.sleep(web_driver.two_second)
            close_panel_button = self.d.find_elements(By.XPATH,
                                                      Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            if len(close_panel_button) == 0:
                self.logger.info("All Panels closed...")
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_21.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_21.png")
                return False
            else:
                return True
            # logout().logout_from_core()

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_21_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_21_exception.png")
            self.logger.error(f"TC_PM_21 got exception as: {ex}")

    def Verify_version_information_is_visible_on_task_bar(self):
        try:
            self.logger.info("********** TC_PM_22 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            face_first_copyright = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_copyright_text_by_xpath(), self.d)
            if face_first_copyright.is_displayed():
                self.logger.info("FaceFirst copyright text is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            if face_first_copyright.is_enabled():
                self.logger.info(" FaceFirst copyright is clickable..")
                self.status.append(True)
            else:
                self.status.append(False)

            actual_copyright_text = face_first_copyright.text
            self.logger.info(f"Actual copyright text: {actual_copyright_text}")
            expected_text = Portal_Menu_Module_read_ini().get_expected_face_first_copyright()
            self.logger.info(f"expected text: {expected_text}")

            if expected_text in actual_copyright_text:
                self.status.append(True)
            else:
                self.status.append(False)

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_22.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_22.png")
                return False
            else:
                return True
            # logout().logout_from_core()

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_22_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_22_exception.png")
            self.logger.error(f"TC_PM_22 got exception as: {ex}")

    def click_on_version_information_on_task_bar_and_verify_information_panel_is_displayed_validate_information_visible_on_panel(self):
        try:
            self.logger.info("********** TC_PM_23 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                               get_copyright_text_by_xpath(), self.d)
            face_first_copyright = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                       get_copyright_text_by_xpath())
            face_first_copyright.click()
            time.sleep(web_driver.two_second)

            actual_title = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                                               get_title_on_version_information_panel_by_xpath(), self.d)
            self.logger.info(f"actual title: {actual_title.text}")
            expected_title = Portal_Menu_Module_read_ini().get_expected_version_information_text()
            self.logger.info(f"expected title: {expected_title}")
            if actual_title.text.lower() == expected_title.lower():
                self.logger.info("Version Information panel visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            face_first_logo = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_face_first_logo_on_version_info_panel_by_xpath())
            if face_first_logo.is_displayed():
                self.logger.info("FaceFirst logo is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            copyright_on_panel = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_face_first_copyright_on_version_info_panel_by_xpath())
            if copyright_on_panel.is_displayed():
                if Portal_Menu_Module_read_ini().get_expected_face_first_copyright() in copyright_on_panel.text:
                    self.logger.info("FaceFirst copyright is visible.... ")
                    self.status.append(True)
                else:
                    self.status.append(False)
            time.sleep(web_driver.two_second)
            actual_webapi_text_on_version_info = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().
                                                                     get_WebAPI_text_on_version_info_by_xpath()).text
            expected_webapi_text_on_version_info = Portal_Menu_Module_read_ini().get_expected_webapi_text_on_version_info()
            self.logger.info(f"actual: {actual_webapi_text_on_version_info}")
            self.logger.info(f"expected: {expected_webapi_text_on_version_info}")
            if actual_webapi_text_on_version_info == expected_webapi_text_on_version_info:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            actual_webapi_version_number = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_webapi_version_info_by_xpath()).text
            self.logger.info(f"actual webapi version: {actual_webapi_text_on_version_info} v{actual_webapi_version_number}")
            expected_webapi_version_number = Portal_Menu_Module_read_ini().get_expected_webapi_version_number()
            self.logger.info(f"expected version: {expected_webapi_version_number}")
            self.logger.info(f"expected webapi version: {expected_webapi_text_on_version_info} v{expected_webapi_version_number}")
            if actual_webapi_version_number == expected_webapi_version_number:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            actual_server_text_on_version_info = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_Server_text_on_version_info_by_xpath()).text
            expected_server_text_on_version_info = Portal_Menu_Module_read_ini().get_expected_server_text_on_version_info()
            if actual_server_text_on_version_info == expected_server_text_on_version_info:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            actual_portal_version_number = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_portal_version_number_by_xpath()).text
            self.logger.info(f"actual portal version: {actual_server_text_on_version_info} v{actual_portal_version_number}")
            expected_portal_version_number = Portal_Menu_Module_read_ini().get_expected_portal_version_number()
            self.logger.info(f"expected portal number: {expected_server_text_on_version_info} v{expected_portal_version_number}")
            if actual_portal_version_number == expected_portal_version_number:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_23.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_23.png")
                return False
            else:
                return True
            # logout().logout_from_core()

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_23_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_23_exception.png")
            self.logger.error(f"TC_PM_23 got exception as: {ex}")

    def verify_user_logo_is_visible_on_task_bar_at_right_corner_besides_logout_btn(self):
        try:
            self.logger.info("********** TC_PM_24 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            user = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_user_name_on_taskbar_by_xpath(), self.d)
            if user.is_displayed():
                self.logger.info(f"Username is displayed as: {user.text}")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            user_logo = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_user_logo_by_xpath())
            if user_logo.is_displayed():
                self.logger.info("User logo is visible beside user's name")
                self.status.append(True)
            else:
                self.status.append(False)

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_24.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_24.png")
                return False
            else:
                return True
            # logout().logout_from_core()

        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_24_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_24_exception.png")
            self.logger.error(f"TC_PM_24 got exception as: {ex}")

    def click_on_user_logo_on_task_bar_at_right_corner_and_verify_user_panel_is_displayed(self):
        try:
            self.logger.info("********** TC_PM_25 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            user = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_user_name_on_taskbar_by_xpath(), self.d)

            user.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on user logo...")
            time.sleep(web_driver.one_second)
            user_panel = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_user_panel_by_xpath())
            if user_panel.is_displayed():
                if user_panel.text in Portal_Menu_Module_read_ini().get_expected_users_text():
                    self.logger.info("User panel is visible....")
                    self.status.append(True)
                else:
                    self.status.append(False)
            time.sleep(web_driver.two_second)
            actual_heading_on_panel = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_heading_on_user_panel_by_xpath()).text
            self.logger.info(f"actual heading: {actual_heading_on_panel}")
            expected_heading = Portal_Menu_Module_read_ini().get_expected_heading_on_user_panel()
            self.logger.info(f"expected heading: {expected_heading}")
            if actual_heading_on_panel == expected_heading.upper():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_25.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_25.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_25_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_25_exception.png")
            self.logger.error(f"TC_PM_25 got exception as: {ex}")

    def verify_user_able_to_change_password_from_user_panel_by_clicking_edit_user_option_inside_action_dropdown_on_user_panel(self):
        try:
            self.logger.info("********** TC_PM_26 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_user_name_on_taskbar_by_xpath(), self.d)
            user = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_user_name_on_taskbar_by_xpath())

            user.click()
            time.sleep(web_driver.one_second)

            action_dropdown = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().
                                                  get_action_dropdown_by_xpath(), self.d )
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            option_inside_action = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().
                                                        get_options_inside_action_dropdown_on_user_panel_by_xpath())
            option_inside_action[0].click()
            time.sleep(web_driver.one_second)
            login_data = LoginLogout_Read_ini()
            password = login_data.get_password()
            # ************************************************************************************************* #
            # ******************************* Changing password to new password ******************************* #
            first_name_textbox = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_first_name_textbox_by_xpath(), self.d)
            first_name_textbox.clear()
            time.sleep(web_driver.two_second)
            first_name_textbox.send_keys(Portal_Menu_Module_read_ini().get_first_name())
            time.sleep(web_driver.one_second)
            last_name_textbox = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_last_name_textbox_by_xpath())
            last_name_textbox.clear()
            time.sleep(web_driver.two_second)
            last_name_textbox.send_keys(Portal_Menu_Module_read_ini().get_last_name())
            time.sleep(web_driver.one_second)
            current_password_textbox = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_current_password_textbox_by_xpath())
            current_password_textbox.send_keys(password)
            new_password_textbox = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_new_password_textbox_by_xpath())
            new_password_textbox.send_keys(Portal_Menu_Module_read_ini().get_new_password())
            time.sleep(web_driver.two_second)
            confirm_password_textbox = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_confirm_password_textbox_by_xpath())
            confirm_password_textbox.send_keys(Portal_Menu_Module_read_ini().get_new_password())
            time.sleep(web_driver.one_second)
            save_button = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_save_button_on_user_panel_by_xpath())
            save_button.click()
            time.sleep(web_driver.two_second)

            actual_message = self.explicit_wait(10, "XPATH",  Portal_Menu_Module_read_ini().get_success_message_to_user_by_xpath(), self.d).text
            self.logger.info(f"actual message: {actual_message}")
            expected_message = Portal_Menu_Module_read_ini().get_expected_success_message_to_user()
            print(actual_message,"==",expected_message)
            self.logger.info(f"expected message: {expected_message}")
            if actual_message == expected_message:
                self.logger.info("Password successfully changed to new ..")
                self.status.append(True)
            else:
                self.status.append(False)
            # ************************************************************************************************* #
            # ******************************* Changing password to previous password ************************** #
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            option_inside_action = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_options_inside_action_dropdown_on_user_panel_by_xpath())
            option_inside_action[0].click()
            time.sleep(web_driver.two_second)

            current_password_textbox = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_current_password_textbox_by_xpath(), self.d)
            current_password_textbox.send_keys(Portal_Menu_Module_read_ini().get_new_password())
            new_password_textbox = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_new_password_textbox_by_xpath())
            new_password_textbox.send_keys(password)
            time.sleep(web_driver.one_second)
            confirm_password_textbox = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_confirm_password_textbox_by_xpath())
            confirm_password_textbox.send_keys(password)
            time.sleep(web_driver.two_second)
            save_button = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_save_button_on_user_panel_by_xpath())
            save_button.click()
            time.sleep(web_driver.two_second)
            actual_message = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_success_message_to_user_by_xpath(), self.d).text
            expected_message = Portal_Menu_Module_read_ini().get_expected_success_message_to_user()
            if actual_message == expected_message:
                self.logger.info("Password successfully changed to previous ..")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath()).click()
            print(self.status)
            self.logger.info(f"Status : {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_26.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_26.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_26_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_26_exception.png")
            self.logger.error(f"TC_PM_26 got exception as: {ex}")

    def click_on_alert_schedule_btn_on_user_panel_and_verify_user_alert_schedule_panel_is_displayed(self):
        try:
            self.logger.info("********** TC_PM_27 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            user = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_user_name_on_taskbar_by_xpath(), self.d)
            user.click()
            time.sleep(web_driver.one_second)
            alert_schedule_button = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_alert_schedule_button_on_user_panel_by_xpath(), self.d)
            alert_schedule_button.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on alert schedule button...")
            time.sleep(web_driver.one_second)
            actual_heading = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_heading_on_alert_schedule_panel_by_xpath(), self.d)
            self.logger.info(f"actual heading: {actual_heading.text}")
            expected_heading = Portal_Menu_Module_read_ini().get_expected_heading_on_alert_schedule_panel()
            self.logger.info(f"expected heading: {expected_heading.upper()}")
            if actual_heading.text == expected_heading.upper():
                self.logger.info("Alert Schedule panel is visible..")
                self.status.append(True)
            else:
                self.status.append(False)
            close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            time.sleep(web_driver.two_second)
            if len(close_panel) > 1:
                for i in range(len(close_panel)):
                    close_panel[i].click()

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_27.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_27.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_27_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_27_exception.png")
            self.logger.error(f"TC_PM_27 got exception as: {ex}")

    def click_on_notification_groups_btn_on_user_panel_and_verify_notification_groups_panel_is_displayed(self):
        try:
            self.logger.info("********** TC_PM_28 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            user = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_user_name_on_taskbar_by_xpath(), self.d)
            user.click()
            time.sleep(web_driver.one_second)
            notification_groups_btn = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_notification_groups_button_on_user_panel_by_xpath(), self.d)
            notification_groups_btn.click()
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on Notification Groups button..")
            time.sleep(web_driver.one_second)
            notification_groups_panel = self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_notification_groups_panel_by_xpath(), self.d)
            time.sleep(web_driver.two_second)
            if notification_groups_panel.is_displayed():
                self.logger.info("Notification Groups panel is displayed..")
                self.status.append(True)
            else:
                self.status.append(False)
            close_panel = self.d.find_elements(By.XPATH, Portal_Menu_Module_read_ini().get_close_panel_button_by_xpath())
            time.sleep(web_driver.two_second)
            if len(close_panel) > 1:
                for i in range(len(close_panel)):
                    close_panel[i].click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_28.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_28.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_28_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_28_exception.png")
            self.logger.error(f"TC_PM_28 got exception as: {ex}")

    def click_and_verify_logout_btn_is_working_as_expected(self):
        try:
            self.logger.info("********** TC_PM_29 started ********")
            self.status.clear()
            # self.d = self.load_portal_login_page_if_not_loaded()
            login().login_to_cloud_if_not_done(self.d)
            time.sleep(web_driver.two_second)
            self.d.refresh()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Portal_Menu_Module_read_ini().get_logout_btn_by_xpath(), self.d)
            logout_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_logout_btn_by_xpath())
            if logout_btn.is_displayed():
                self.logger.info("Logout button is displayed...")
                logout_btn.click()
                time.sleep(web_driver.one_second)
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            login_btn = self.d.find_element(By.XPATH, Portal_Menu_Module_read_ini().get_login_btn_by_xpath())
            if login_btn.is_displayed():
                self.logger.info("User logged out successfully..")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"Status : {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_29.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_29.png")
                return False
            else:
                return True
            # logout().logout_from_core()
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_PM_29_exception.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_PM_29_exception.png")
            self.logger.error(f"TC_PM_29 got exception as: {ex}")

