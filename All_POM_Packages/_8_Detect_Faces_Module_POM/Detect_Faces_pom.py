import time
from pathlib import Path
from selenium.webdriver.common.by import By

from All_Config_Packages._12_Identify_and_Enroll_Config_Files.Identify_and_Enroll_Readd_INI import \
    Read_Identify_and_Enroll_Components
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_Config_Packages._8_detect_faces_config_Files.Detect_Faces_Read_Ini import detect_Faces_Read_Ini
from Base_Package.Login_Logout_Ops import login, logout


class detect_faces_pom(web_driver, web_logger):

    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

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

    def Launching_login_page(self):
        try:
            self.logger.info(f"*****TC_001***** started")
            self.d.get(detect_Faces_Read_Ini().get_Launching_url())
            expected_url = detect_Faces_Read_Ini().get_Launching_url()
            time.sleep(web_driver.one_second)
            self.d.maximize_window()
            actual_url = self.d.current_url
            self.logger.info(f"actual: {actual_url},\nexpected: {expected_url}")
            if expected_url == actual_url:
                self.status.append(True)
            else:
                self.status.append(False)

            actual_title = self.d.title
            self.logger.info(f"actual is: {actual_title}")
            expected_title = detect_Faces_Read_Ini().get_expecting_title_webportal_login()
            self.logger.info(f"expected title is: {expected_title}")
            if actual_title == expected_title:
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_001.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_001.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_001.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_001.png")
            self.logger.error(f"TC_detect_faces_001 got exception as: {ex}")
            self.logger.info(ex)

    def logo_username_texbox_password_textbox_is_visible(self):
        try:
            self.logger.info("*****TC_002***** started")
            self.d.get(detect_Faces_Read_Ini().get_Launching_url())
            self.status.clear()
            time.sleep(web_driver.three_second)
            logo = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().get_logo_is_visible_on_login_page())
            username = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().get_username_textbox())
            username.is_displayed()
            self.logger.info(f"username is displayed: {username.is_displayed()}")
            password = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().get_password_textbox())
            password.is_displayed()
            self.logger.info(f"password is displayed: {password.is_displayed()}")
            if logo.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_002.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_002.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_002.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_002.png")
            self.logger.error(f"TC_detect_faces_002 got exception as: {ex} ")
            self.logger.info(ex)

    def load_login_page_if_not_loaded(self):
        try:
            self.d.get(detect_Faces_Read_Ini().get_Launching_url())
            expected_url = detect_Faces_Read_Ini().get_Launching_url()
            time.sleep(web_driver.one_second)
            self.d.maximize_window()
            actual_url = self.d.current_url
            self.logger.info(f"actual: {actual_url},\nexpected: {expected_url}")
            if expected_url == actual_url:
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.three_second)
            username = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().get_username_textbox())
            username.clear()
            username.send_keys(detect_Faces_Read_Ini().get_valid_username())
            time.sleep(web_driver.two_second)
            password = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().get_password_textbox())
            password.clear()
            password.send_keys(detect_Faces_Read_Ini().get_valid_password())
            time.sleep(web_driver.two_second)
            cloud_login = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().get_cloudlogin_button())
            cloud_login.click()
            time.sleep(web_driver.two_second)
            self.logger.info(f"status :{self.status}")
        except Exception as ex:
            self.logger.info(ex)

    def verify_after_login_on_cloud_menu_DETECT_FACES_is_visible_in_cloudmenu_items(self):
        try:
            self.logger.info("*****TC_003_*****started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            cloud_menu = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().get_afterlogin_cloud_menu_is_visible())
            if cloud_menu.is_displayed():
                self.logger.info(f"cloud menu is displayed after login, {cloud_menu}")
                self.status.append(True)
            else:
                self.logger.info(f"cloud menu is not displayed after login, {cloud_menu}")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_003.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_005.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_003.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_003.png")
            self.logger.error(f"TC_detect_faces_003 got exception as: {ex} ")

    def Click_on_Detect_Faces_menu_and_verify_it_is_navigating_to_Detect_Faces_panel_verify_panel_heading_is_visible_as_expected(self):
        try:
            self.logger.info("******TC_004******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            if detect_faces.is_displayed():
                self.logger.info(f"detect faces is visible in dashboard items:")
                self.status.append(True)
            else:
                self.logger.info(f"detect faces is not visible in dashboard items:")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            self.close_all_panels()

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_004.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_004.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_004.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_004.png")
            self.logger.error(f"TC_detect_faces_004 got exception as: {ex} ")

    def click_on_DETECT_FACES_on_clould_menu_items_and_verify_detect_faces_panel_is_visible(self):
        try:
            self.logger.info("**********TC_005******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.three_second)
            heading_of_detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().heading_of_detect_faces())
            if heading_of_detect_faces.is_displayed():
                self.logger.info(f"after clicking detect faces  panel heading of detect faces is visible")
                self.status.append(True)
            else:
                self.logger.info(f"after clicking detect faces panel heading of detect faces is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.two_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_005.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_005.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_005.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_005.png")
            self.logger.error(f"TC_detect_faces_005 got exception as: {ex} ")

    def on_Detect_faces_page_check_a_banner_containing_no_faces_detected_before_uploading_a_image_is_visible(self):
        try:
            self.logger.info("*******TC_006****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            banner = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().number_of_faces_detected_banner())
            if banner.is_displayed():
                self.logger.info(f"banner will gives number of faces detected")
                self.status.append(True)
            else:
                self.logger.info(f"banner is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.two_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_006.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_006.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_006.png")
            self.logger.error(f"TC_detect_faces_006 got exception as: {ex} ")

    def on_Detect_faces_page_verify_a_image_box_is_visible(self):
        try:
            self.logger.info("*******TC_007****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.one_second)
            image_box = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().image_box())
            if image_box.is_displayed():
                self.logger.info(f"image box is visible")
                self.status.append(True)
            else:
                self.logger.info(f"image box is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_007.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_007.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_007.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_007.png")
            self.logger.error(f"TC_detect_faces_007 got exception as: {ex} ")

    def on_Detect_faces_page_upload_a_image_into_image_box(self):
        try:
            self.logger.info("********TC_008******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().detect_faces_in_dashboard(),self.d)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            # file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img2.jpg"
            # file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img3.png"
            # file_image_path = "D:/My Code/07-08-2023 code/ff-automation/Other_IMP_Files/Images/Images/img1.png"
            # file_image_path = "C:\Users\Divya\Downloads\images\gdv.png"
            # self.d.find_element(By.XPATH, "//img[@id='uploadPreviewImg']").send_keys(file_image_path)
            time.sleep(web_driver.one_second)
            # self.d.find_element(By.ID, "copyOfOriginalPhoto']").send_keys(file_image_path)
            # self.d.find_element(By.ID, "uploadPreviewImg").send_keys(file_image_path)image0
            # self.d.find_element(By.ID, "image").clear()
            time.sleep(web_driver.one_second)
            # self.explicit_wait(10, "ID", "image", self.d)
            # self.explicit_wait(10, "ID", "image", self.d)
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(6)
            self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().number_of_faces_deteced_in_a_imagebox(), self.d)
            banner = self.d.find_elements(By.XPATH, detect_Faces_Read_Ini().number_of_faces_deteced_in_a_imagebox())

            expected_banner_text = f"{len(banner)} {detect_Faces_Read_Ini().number_of_faces_detected_text()}"
            self.logger.info(f"expected: {expected_banner_text}")
            actual_banner_text = self.d.find_element(By.XPATH,
                                                     detect_Faces_Read_Ini().number_of_faces_detected_banner()).text
            self.logger.info(f"actual: {actual_banner_text}")
            if actual_banner_text == expected_banner_text:
                self.logger.info("number of faces detected is displayed in banner")
                self.status.append(True)
            else:
                self.logger.info("if image not selected gives a select image")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_008.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_008.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_008.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_008.png")
            self.logger.error(f"TC_detect_faces_008 got exception as: {ex} ")

    def upload_a_image_having_more_no_of_faces_verify_banner_showing_number_of_faces_on_a_image(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.logger.info("********TC_009******* started")
            time.sleep(web_driver.two_second)
            # detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces = web_driver.explicit_wait(self, 10, "XPATH", detect_Faces_Read_Ini().detect_faces_in_dashboard(), self.d)
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img2.jpg"
            time.sleep(web_driver.two_second)
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(15)
            banner = self.d.find_elements(By.XPATH, detect_Faces_Read_Ini().number_of_faces_deteced_in_a_imagebox())

            expected_banner_text = f"{len(banner)} {detect_Faces_Read_Ini().number_of_faces_detected_text()}"
            self.logger.info(f"expected: {expected_banner_text}")
            actual_banner_text = self.d.find_element(By.XPATH,
                                                     detect_Faces_Read_Ini().number_of_faces_detected_banner()).text
            self.logger.info(f"actual: {actual_banner_text}")
            if actual_banner_text == expected_banner_text:
                self.logger.info("number of faces detected is displayed in banner")
                self.status.append(True)
            else:
                self.logger.info("if image not selected gives a select image")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.three_second)
            # logout().logout_from_core(self.d)
            self.close_all_panels()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_009.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_009.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_009.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_009.png")
            self.logger.error(f"TC_detect_faces_009 got exception as: {ex} ")

    def On_Detect_faces_page_upload_a_image_having_face_with_mask(self):
        try:
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            self.logger.info("********TC_010******* started")
            time.sleep(web_driver.two_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img3.png"
            time.sleep(web_driver.two_second)
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(15)
            banner = self.d.find_elements(By.XPATH, detect_Faces_Read_Ini().number_of_faces_deteced_in_a_imagebox())

            expected_banner_text = f"{len(banner)} {detect_Faces_Read_Ini().number_of_faces_detected_text()}"
            self.logger.info(f"expected: {expected_banner_text}")
            actual_banner_text = self.d.find_element(By.XPATH,
                                                     detect_Faces_Read_Ini().number_of_faces_detected_banner()).text
            self.logger.info(f"actual: {actual_banner_text}")

            if actual_banner_text == expected_banner_text:
                self.logger.info("number of faces detected is displayed in banner")
                self.status.append(True)
            else:
                self.logger.info("if image not selected gives a select image")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_010.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_010.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_010.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_010.png")
            self.logger.error(f"TC_detect_faces_010 got exception as: {ex} ")

    def verify_reselect_button_is_visible_in_detect_faces(self):
        try:
            self.logger.info("*******TC_011******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.append(True)
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            time.sleep(web_driver.two_second)
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(10)
            reselect_button = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().reselect_button_in_detectfaces())
            if reselect_button.is_displayed():
                self.logger.info("after uploading a image into imagebox reselect button is visible")
                self.status.append(True)
            else:
                self.logger.info("if image is not uploaded image button is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.two_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_011.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_011.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_011.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_011.png")
            self.logger.error(f"TC_detect_faces_011 got exception as: {ex} ")

    def on_Detect_faces_click_on_reselect_button_again_upload_a_image_verify_if_image_is_uploaded(self):
        try:
            self.logger.info("*******TC_012*******started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            time.sleep(web_driver.two_second)
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(6)
            reselect_button = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().reselect_button_in_detectfaces())
            reselect_button.click()
            time.sleep(web_driver.one_second)
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img4.png"
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(6)
            question_mark_symbol = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().question_mark_symbol())
            if question_mark_symbol.is_displayed():
                self.logger.info("question mark symbol is visible after selecting a image")
                self.status.append(True)
            else:
                self.logger.info("question mark symbol is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_012.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_012.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_012.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_012.png")
            self.logger.error(f"TC_detect_faces_012 got exception as: {ex} ")

    def on_Detect_faces_verify_cross_symbol_is_visible_after_uploding_a_image(self):
        try:
            self.logger.info("*********TC_013********* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            time.sleep(web_driver.two_second)
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(6)
            cross_symbol = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().cross_symbol())
            if cross_symbol.is_displayed():
                self.logger.info("cross symbol is visible after uploading a image")
                self.status.append(True)
            else:
                self.logger.info("cross symbol is not visible if we donot upload a image")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_013.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_013.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_013.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_013.png")
            self.logger.error(f"TC_detect_faces_013 got exception as: {ex} ")

    def on_Detect_faces_click_on_cross_symbol_verify_cross_symbol_is_visible(self):
        try:
            self.logger.info("*******TC_014 ******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.one_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"

            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(web_driver.two_second)

            cross_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().cross_symbol(),self.d)
            cross_symbol.click()
            time.sleep(web_driver.three_second)
            cross_symbol_list = self.d.find_elements(By.XPATH, detect_Faces_Read_Ini().cross_symbol())
            if len(cross_symbol_list) > 0:
                self.logger.info("cross symbol is visible ")
                self.status.append(True)
            else:
                self.logger.info("cross symbol is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_014.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_014.png")
                return True
            else:
                return False
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_014.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_014.png")
            self.logger.error(f"TC_detect_faces_014 got exception as: {ex} ")

    def on_Detect_faces_After_a_selecting_a_image_question_mark_symbol_is_visible(self):
        try:
            self.logger.info("********TC_015******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            time.sleep(web_driver.two_second)
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(6)
            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            if question_mark_symbol.is_displayed():
                self.logger.info("question mark symbol is visible after selecting a image")
                self.status.append(True)
            else:
                self.logger.info("question mark symbol is not visible if image not selected")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_015.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_015.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_015.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_015.png")
            self.logger.error(f"TC_detect_faces_015 got exception as: {ex} ")

    def After_uploading_a_image_into_imagebox_on_detect_faces_click_on_question_mark_IMAGE_QUALITY_page_is_visible(self):
        try:
            self.logger.info("*******TC_016******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.one_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(5)
            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.two_second)
            image_quality_panel_heading = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().image_quality_page_panel(), self.d)
            if image_quality_panel_heading.is_displayed():
                self.logger.info("image quality panel heading is visible")
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_015.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_015.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_016.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_016.png")
            self.logger.error(f"TC_detect_faces_016 got exception as: {ex} ")

    def on_image_quality_page_verify_download_image_button_is_visible(self):
        try:
            self.logger.info("*******Tc_017 ******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(5)
            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.two_second)
            download_image = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().download_image_button(), self.d)
            if download_image.is_displayed():
                self.logger.info("download image button is visible")
                self.status.append(True)
            else:
                self.logger.info("download image button is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_017.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_017.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_017.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_017.png")
            self.logger.error(f"TC_detect_faces_017 got exception as: {ex} ")

    def on_image_quality_page_verify_view_file_info_button_is_visible(self):
        try:
            self.logger.info("******TC_018******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(7)
            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.three_second)
            view_info_button_in_image_quality = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().view_info_button_in_imagequality(), self.d)
            if view_info_button_in_image_quality.is_displayed():
                self.logger.info("view info button is visible in image quality page")
                self.status.append(True)
            else:
                self.logger.info("view info button is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_018.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_018.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_018.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_018.png")
            self.logger.error(f"TC_detect_faces_018 got exception as: {ex} ")

    def click_on_view_file_info_button_on_image_quality_page_verify_information_of_image_click_on_ok_on_alert(self):
        try:
            self.logger.info("*******TC_019******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(5)
            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.three_second)
            view_info_button_in_image_quality = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().view_info_button_in_imagequality(), self.d)
            view_info_button_in_image_quality.click()
            time.sleep(web_driver.two_second)
            a = self.d.switch_to.alert
            if a:
                self.logger.info("file info alert is opened")
                self.status.append(True)
            else:
                self.logger.info("file info alert is not opened")
                self.status.append(False)
            a.accept()
            # a = self.d.switch_to.alert
            # if a:
            #     self.status.append(True)
            # else:
            #     self.status.append(False)
            # print(self.status)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_019.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_019.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_019.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_019.png")
            self.logger.error(f"TC_detect_faces_019 got exception as: {ex} ")

    def on_image_quality_page_verify_and_scroll_image_information_is_visible(self):
        try:
            self.logger.info("******TC_20****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(5)
            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.three_second)
            self.d.execute_script("window.scrollTo(0, 150)")
            image_quality_scan_text = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().image_quality_scan_result_heading_txt_by_xpath(), self.d)
            if image_quality_scan_text.is_displayed():
                self.logger.info("image quality scan heading visible")
                self.status.append(True)
            else:
                self.logger.info("is no masked face is not visible")
                self.status.append(False)

            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_020.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_020.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_020.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_020.png")
            self.logger.error(f"TC_detect_faces_020 got exception as: {ex} ")
        finally:
            logout().logout_from_core(self.d)


    def verify_action_dropdown_is_visible_on_image_quality_page(self):
        try:
            self.logger.info("******TC_21****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(5)
            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.three_second)
            action_dropdown = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().Action_dropdown_in_image_quality(), self.d)
            if action_dropdown.is_displayed():
                self.logger.info("action dropdown is visible in image quality page")
                self.status.append(True)
            else:
                self.logger.info("action dropdown is not visible in image quality page")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.two_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_21.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_21.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_21.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_21.png")
            self.logger.error(f"TC_detect_faces_21 got exception as: {ex} ")

    def on_image_quality_page_In_action_dropdown_click_on_identify_within_enrollments_Identify_and_enroll_page_is_visible_and_clickable(self):
        try:
            self.logger.info("*******TC_022******** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(10)
            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.three_second)
            action_dropdown = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().Action_dropdown_in_image_quality(), self.d)
            action_dropdown.click()
            time.sleep(web_driver.three_second)
            identify_within_enrollments = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().identify_within_enrollments(), self.d)
            if identify_within_enrollments.is_displayed():
                self.logger.info("identify within enrollments is option in action dropdown")
                self.status.append(True)
            else:
                self.logger.info("identify within enrollments is not in action dropdown")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.two_second)
            # logout().logout_from_core(self.d)
            self.close_all_panels()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_22.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_22.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_22.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_22.png")
            self.logger.error(f"TC_detect_faces_22 got exception as: {ex} ")

    def on_image_qualty_page_in_action_dropdown_click_on_identify_within_enrollments_Identify_and_enroll_page_is_visible(self):
        try:
            self.logger.info("*******TC_023****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(5)
            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.three_second)
            action_dropdown = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().Action_dropdown_in_image_quality(), self.d)
            action_dropdown.click()
            time.sleep(web_driver.three_second)
            identify_within_enrollments = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().identify_within_enrollments(), self.d)
            self.logger.info("identify within enrollments is option in action dropdown")
            identify_within_enrollments.click()
            time.sleep(web_driver.three_second)
            identify_enroll = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().identify_enroll_heading_panel(), self.d)
            if identify_enroll.is_displayed():
                self.logger.info("identify and enroll page is opened ")
                self.status.append(True)
            else:
                self.logger.info("identify within enrollments is not in action dropdown")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_23.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_23.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_23.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_23.png")
            self.logger.error(f"TC_detect_faces_23 got exception as: {ex} ")

    def In_identify_and_enroll_page_if_person_is_already_enrolled_identify_results_page_is_visible(self):
        try:
            self.logger.info("******TC_024***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img6.jpg"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(10)
            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.three_second)
            action_dropdown = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().Action_dropdown_in_image_quality(), self.d)
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            identify_within_enrollments = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().identify_within_enrollments(), self.d)
            self.logger.info("identify within enrollments is option in action dropdown")
            identify_within_enrollments.click()
            time.sleep(web_driver.three_second)
            identification_results = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().identification_results_panel_heading(), self.d)
            if identification_results.is_displayed():
                self.logger.info("identification results  page is opened ")
                self.status.append(True)
            else:
                self.logger.info("identification results page is not opened")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            logout().logout_from_core(self.d)
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_24.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_24.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_24.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_24.png")
            self.logger.error(f"TC_detect_faces_24 got exception as: {ex} ")

    def In_identify_results_page_verify_faces_button_is_visible(self):
        try:
            self.logger.info("********TC_025******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)

            detect_faces = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini()
                                              .detect_faces_in_dashboard(), self.d)
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().heading_of_detect_faces(), self.d)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\img\\visitor_search_img_1.png"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(7)
            self.explicit_wait(10, "XPATH",detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().question_mark_symbol())
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")

            action_dropdown = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().Action_dropdown_in_image_quality(), self.d)
            action_dropdown.click()
            time.sleep(web_driver.three_second)

            identify_within_enrollments = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().identify_within_enrollments(), self.d)
            self.logger.info("identify within enrollments is option in action dropdown")
            identify_within_enrollments.click()
            time.sleep(web_driver.three_second)
            self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini()
                               .identification_results_panel_heading(),self.d)
            identification_results = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().identification_results_panel_heading())
            self.logger.info("identification results panel is visible")
            time.sleep(web_driver.three_second)
            faces_button_in_identification_results = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().faces_button_in_identification_results_page())
            if faces_button_in_identification_results.is_displayed():
                self.logger.info("faces button is visible in identification results page")
                self.status.append(True)
            else:
                self.logger.info("faces button is not visible in identification results page")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            # logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_25.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_25.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_25.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_25.png")
            self.logger.error(f"TC_detect_faces_25 got exception as: {ex} ")

    def On_identify_results_page_click_faces_button_enrollment_faces_page_is_visible(self):
        try:
            self.logger.info("********TC_026******* started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().detect_faces_in_dashboard(), self.d)
            detect_faces = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().detect_faces_in_dashboard(), self.d)
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().heading_of_detect_faces(), self.d)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\img\\visitor_search_img_1.png"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(10)

            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.three_second)

            action_dropdown = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().Action_dropdown_in_image_quality(), self.d)
            action_dropdown.click()
            time.sleep(web_driver.two_second)

            identify_within_enrollments = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().identify_within_enrollments(), self.d)
            self.logger.info("identify within enrollments is option in action dropdown")
            identify_within_enrollments.click()
            time.sleep(web_driver.three_second)
            self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().identification_results_panel_heading(), self.d)
            identification_results = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().identification_results_panel_heading())
            time.sleep(web_driver.three_second)

            faces_button_in_identification_results = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().faces_button_in_identification_results_page(), self.d)
            self.logger.info("faces button is visible in identification results page")
            faces_button_in_identification_results.click()
            time.sleep(web_driver.three_second)

            enroll_faces = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().enroll_faces_panel_heading(),
                               self.d)
            if enroll_faces.is_displayed():
                self.logger.info("enroll faces page is opened")
                self.status.append(True)
            else:
                self.logger.info("enroll faces page is not opened")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_26.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_26.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_26.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_26.png")
            self.logger.error(f"TC_detect_faces_26 got exception as: {ex} ")

    def verify_person_view_button_is_visible_in_identify_results_page(self):
        try:
            self.logger.info("*******TC_027****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img6.jpg"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(5)
            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.three_second)
            action_dropdown = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().Action_dropdown_in_image_quality(), self.d)
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            identify_within_enrollments = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().identify_within_enrollments(), self.d)
            self.logger.info("identify within enrollments is option in action dropdown")
            identify_within_enrollments.click()
            time.sleep(web_driver.three_second)
            # identification_results = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().identification_results_panel_heading())
            time.sleep(web_driver.three_second)
            person_view_button = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().person_view_button_in_identification_results(), self.d)
            if person_view_button.is_displayed():
                self.logger.info("person view button is visible")
                self.status.append(True)
            else:
                self.logger.info("person view button is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_27.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_27.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_27.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_27.png")
            self.logger.error(f"TC_detect_faces_27 got exception as: {ex} ")

    def on_identify_results_page_click_on_person_view_button_enrollment_view_page_is_visible(self):
        try:
            self.logger.info("*******TC_028****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            time.sleep(web_driver.three_second)
            file_image_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\vip\\00099.png"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(7)
            question_mark_symbol = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().question_mark_symbol())
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.three_second)
            action_dropdown = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().Action_dropdown_in_image_quality())
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            identify_within_enrollments = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().identify_within_enrollments(), self.d)
            self.logger.info("identify within enrollments option in action dropdown")
            identify_within_enrollments.click()
            time.sleep(web_driver.three_second)
            identification_results = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().identification_results_panel_heading(), self.d)
            time.sleep(web_driver.three_second)
            person_view_button = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().person_view_button_in_identification_results())
            person_view_button.click()
            self.logger.info(f"person view button is clicked: {person_view_button.click()}")
            time.sleep(web_driver.three_second)
            enrollment_view = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().enrollment_view_panel_heading())
            if enrollment_view.is_displayed():
                self.logger.info("enrollment view page is opened")
                self.status.append(True)
            else:
                self.logger.info("enrollment view page is not opened")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_28.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_28.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_28.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_28.png")
            self.logger.error(f"TC_detect_faces_28 got exception as: {ex} ")

    def verify_purge_and_replace_button_is_visible_on_identify_results(self):
        try:
            self.logger.info("*******TC_029****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img6.jpg"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(5)
            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.three_second)
            action_dropdown = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().Action_dropdown_in_image_quality(), self.d)
            action_dropdown.click()
            time.sleep(web_driver.one_second)
            identify_within_enrollments = self.explicit_wait(10, "XPATH",
                                                              detect_Faces_Read_Ini().identify_within_enrollments(), self.d)
            self.logger.info("identify within enrollments option in action dropdown")
            identify_within_enrollments.click()
            time.sleep(web_driver.three_second)
            # identification_results = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().identification_results_panel_heading())
            time.sleep(web_driver.three_second)
            purge_replace_button = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().purge_replace_button_in_identification_results(), self.d)
            if purge_replace_button.is_displayed():
                self.logger.info("purge and replace button is visible in identify results")
                self.status.append(True)
            else:
                self.logger.info("purge and relace button is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_29.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_29.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_29.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_29.png")
            self.logger.error(f"TC_detect_faces_29 got exception as: {ex} ")

    def on_identify_results_page_click_on_purge_and_replace_an_alert_is_visible_click_ok_button_on_alert_enrollment_faces_page_is_displayed(self):
        try:
            self.logger.info("*******TC_030****** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().detect_faces_in_dashboard(), self.d)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\vip\\00099.png"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().question_mark_symbol())
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.three_second)
            action_dropdown = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().Action_dropdown_in_image_quality())
            action_dropdown.click()
            time.sleep(web_driver.three_second)
            identify_within_enrollments = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().identify_within_enrollments(), self.d)
            self.logger.info("identify within enrollments is option in action dropdown")
            identify_within_enrollments.click()
            # time.sleep(web_driver.three_second)
            # identification_results = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().identification_results_panel_heading())
            time.sleep(web_driver.three_second)
            # purge_replace_button = self.explicit_wait(10, "XPATH",detect_Faces_Read_Ini().purge_replace_button_in_identification_results(), self.d)
            # purge_replace_button.click()
            # time.sleep(web_driver.three_second)
            # a = self.d.switch_to.alert
            # self.logger.info("first alert is opened")
            # a.accept()
            # print(a, "step1")
            # time.sleep(web_driver.three_second)
            # a1 = self.d.switch_to.alert
            # self.logger.info("second alert is displayed")
            # a1.accept()
            # print(a1, "step1")
            # time.sleep(web_driver.three_second)

            faces_button_in_identification_results = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().faces_button_in_identification_results_page(), self.d)
            self.logger.info("faces button is visible in identification results page")
            faces_button_in_identification_results.click()
            enrollment_faces = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().enrollment_faces_panel_heading(), self.d)
            if enrollment_faces.is_displayed():
                self.logger.info("enrollment view page is opened")
                self.status.append(True)
            else:
                self.logger.info("enrollment view page is not opened")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.two_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_30.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_30.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_30.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_30.png")
            self.logger.error(f"TC_detect_faces_30 got exception as: {ex} ")

    def on_identify_and_enroll_page_if_person_is_not_enrolled_add_details_are_page_is_visible(self):
        try:
            self.logger.info("******TC_031***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(6)
            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(),self.d)
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.three_second)
            action_dropdown = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().Action_dropdown_in_image_quality(), self.d)
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            identify_within_enrollments = self.explicit_wait(10, "XPATH",
                                                              detect_Faces_Read_Ini().identify_within_enrollments(), self.d)
            self.logger.info("identify within enrollments is option in action dropdown")
            identify_within_enrollments.click()
            time.sleep(web_driver.three_second)
            identify_enroll = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().identify_enroll_heading_panel(), self.d)
            if identify_enroll.is_displayed():
                self.logger.info("if person is not enrolled add details page will be opened")
                self.status.append(True)
            else:
                self.logger.info("if page is not opened")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.two_second)
            # self.d.find_element(By.XPATH, Web_portal_login_Read_INI().get_facefirst_logout_button()).click()
            self.d.find_element(By.XPATH, detect_Faces_Read_Ini().cross_symbol_on_identify_and_enroll_panel()).click()
            time.sleep(web_driver.two_second)
            self.d.find_element(By.XPATH, detect_Faces_Read_Ini().close_panel_and_cancel_enrollment()).click()
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_31.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_31.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_31.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_31.png")
            self.logger.error(f"TC_detect_faces_31 got exception as: {ex} ")

    def on_image_quality_page_click_on_identify_within_visitors_inside_Action_dropdown_and_perform_visitor_search(self):
        try:
            self.logger.info("******TC_032***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(5)
            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.three_second)
            action_dropdown = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().Action_dropdown_in_image_quality(), self.d)
            action_dropdown.click()
            time.sleep(web_driver.two_second)
            identify_with_in_visitors = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().identify_with_in_visitors(), self.d)
            identify_with_in_visitors.click()
            time.sleep(web_driver.two_second)
            visitor_search_panel = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().visitor_serach_panel_heading(), self.d)
            if visitor_search_panel.is_displayed():
                self.logger.info("visitor search panel heading is visible")
                self.status.append(True)
            else:
                self.logger.info("visitor search panel heading is not visible")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_32.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_32.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_32.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_32.png")
            self.logger.error(f"TC_detect_faces_32 got exception as: {ex} ")

    def on_image_quality_page_In_action_dropdown_verify_download_image_option_is_visible(self):
        try:
            self.logger.info("******TC_033***** started")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            detect_faces = self.d.find_element(By.XPATH, detect_Faces_Read_Ini().detect_faces_in_dashboard())
            detect_faces.click()
            self.logger.info("detect faces clicked")
            time.sleep(web_driver.two_second)
            self.logger.info("reached to image")
            file_image_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img1.png"
            self.d.find_element(By.ID, "image").send_keys(file_image_path)
            time.sleep(10)
            question_mark_symbol = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().question_mark_symbol(), self.d)
            question_mark_symbol.click()
            self.logger.info("question mark symbol is clicked")
            time.sleep(web_driver.three_second)
            action_dropdown = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().Action_dropdown_in_image_quality(), self.d)
            action_dropdown.click()
            self.logger.info(f"action dropdwon clicked: {action_dropdown.click()}")
            time.sleep(web_driver.three_second)
            download_image = self.explicit_wait(10, "XPATH", detect_Faces_Read_Ini().download_image_option_action_dropdown(), self.d)
            if download_image.is_displayed():
                self.logger.info("download option is visible in action dropdown")
                self.status.append(True)
            else:
                self.logger.info("download option is not visible in action dropdown")
                self.status.append(False)
            self.logger.info(f"status :{self.status}")
            time.sleep(web_driver.one_second)
            logout().logout_from_core(self.d)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_33.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_33.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"screenshot file path: {self.screenshots_path}\\TC_detect_faces_33.png")
            self.d.save_screenshot(f"{self.screenshots_path}\\TC_detect_faces_33.png")
            self.logger.error(f"TC_detect_faces_33 got exception as: {ex} ")

    def close_all_panels(self):
        try:
            time.sleep(web_driver.one_second)
            cloud_menu = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().cloud_menu_by_xpath())
            cloud_menu.click()
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            close_all_panels_menu = self.d.find_elements(By.XPATH,
                                                         Read_Identify_and_Enroll_Components().close_all_panels_btn_by_xpath())
            time.sleep(web_driver.one_second)
            if len(close_all_panels_menu) > 0:
                close_all_panels_menu[0].click()
                time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(f"Exception crated: {ex.args}")
            self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\test_TC_DFexception.png")
            return False
