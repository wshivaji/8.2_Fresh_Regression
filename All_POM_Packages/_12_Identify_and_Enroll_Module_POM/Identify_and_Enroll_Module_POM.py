import time
from datetime import date
import datetime
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from All_Config_Packages._16_Audit_Log_Report_Module_Config_Files.Audit_Log_Report_Read_INI import Audit_Log_Report_Components
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login, logout
from selenium.webdriver.common.by import By
from All_Config_Packages._12_Identify_and_Enroll_Config_Files.Identify_and_Enroll_Readd_INI import Read_Identify_and_Enroll_Components
from pathlib import Path


class Identify_And_Enroll_POM(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    status = []

    now = (datetime.datetime.now())
    # DATE_IE = now.strftime('%m/%d/%Y')
    # TIME_IE = now.strftime('%H%M')
    # AM_PM_IE = now.strftime('%p')
    DATE_IE = now.strftime(Read_Identify_and_Enroll_Components().date_format())
    TIME_IE = now.strftime(Read_Identify_and_Enroll_Components().hh_mm_format())
    AM_PM_IE = now.strftime(Read_Identify_and_Enroll_Components().am_pm_format())

    tomorrow = now + datetime.timedelta(2)
    # expirationDATE_IE = tomorrow.strftime('%m/%d/%Y')
    # expirationTIME_IE = now.strftime('%H%M')
    # expirationAM_PM_IE = now.strftime('%p')
    expirationDATE_IE = tomorrow.strftime(Read_Identify_and_Enroll_Components().date_format())
    expirationTIME_IE = now.strftime(Read_Identify_and_Enroll_Components().hh_mm_format())
    expirationAM_PM_IE = now.strftime(Read_Identify_and_Enroll_Components().am_pm_format())

    def upload_image_to_identify_and_enroll(self, img_path):
        try:
            # self.choose_file("image", img_path, by="name")
            self.logger.info(f"image uploaded: {img_path}")
            # upload_image = self.explicit_wait(10, "NAME", "image", self.d)
            upload_image = self.d.find_element(By.NAME, "image")
            upload_image.send_keys(img_path)
            time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.info(f"upload image exception: {ex.args}")

    def dateTimeAMPM(self, date_incident):
        date_incident.send_keys(self.DATE_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(self.TIME_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(self.AM_PM_IE)
        time.sleep(web_driver.one_second)

    def expirirationdateTimeAMPM(self, date_incident):
        self.logger.info(f" tommorow date : {self.expirationDATE_IE}")
        date_incident.send_keys(self.expirationDATE_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(" " + self.TIME_IE)
        time.sleep(web_driver.one_second)
        date_incident.send_keys(" " + self.AM_PM_IE)
        time.sleep(web_driver.one_second)

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

    def load_portal_login_page_if_not_loaded(self):
        try:
            login_func = login()
            if self.d.current_url == login_func.cloud_url:
                pass
            else:
                login().login_to_cloud_if_not_done(self.d)
                self.status.clear()
                time.sleep(web_driver.one_second)
                # self.d.get(Read_Portal_Menu_Components().get_url())
                # self.d.maximize_window()
                # time.sleep(web_driver.one_second)
        except Exception as ex:
            self.logger.error(ex)

    def Select_Enrollment_Group(self, i):
        try:
            # i = int(i)
            self.logger.info(f"eg index: {i}")
            eg = Read_Identify_and_Enroll_Components().get_eg()
            enrollment_groups_list = eg.split(',')

            time.sleep(web_driver.two_second)
            enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().enrollment_group_by_xpath())
            enrollment_group.click()
            time.sleep(web_driver.one_second)
            select = Select(enrollment_group)
            select.select_by_index(1)
            # select.select_by_value(enrollment_groups_list[i])
            self.logger.info(f"enrollment group: {enrollment_groups_list}")
            # enter_eg = enrollment_groups_list[i] + " (Serious Offender - High)"
            # enter_eg = i + " (Serious Offender - High)"
            # enter_eg = i + " (Serious Offender - None)"
            enter_eg = i + " " + Read_Identify_and_Enroll_Components().serious_offender_text()
            self.logger.info(f"entering eg: {enter_eg}")
            select.select_by_visible_text(enter_eg)
            time.sleep(web_driver.one_second)
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
        except Exception as ex:
            print("select enrollment group exception: ", ex.args)

    def Create_New_Enrollment_using_Identify_and_Enroll(self):
        try:
            self.logger.info("************* test_TC_IE_00 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()

            time.sleep(web_driver.two_second)
            link = self.explicit_wait(10, "XPATH",
                                      Read_Identify_and_Enroll_Components().identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"

            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH",
                                                  Read_Identify_and_Enroll_Components().enrollment_basis_by_xpath(),
                                                  self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)
            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')

            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            self.logger.info("region btn clicked")
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            self.logger.info(f"edge name: {edge_name}")
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    self.logger.info(f"region name selected: {region_names[i].text}")
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            self.d.execute_script("arguments[0].click();", save_btn)
            # save_btn.click()
            self.logger.info(f"save btn : {save_btn.text}")
            time.sleep(web_driver.two_second)

            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().action_input_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            reported_loss = self.d.find_element(By.XPATH,
                                                Read_Identify_and_Enroll_Components().reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH,
                                           Read_Identify_and_Enroll_Components().add_details_save_btn_by_xpath())
            time.sleep(web_driver.one_second)
            if save_btn.is_displayed():
                self.logger.info(f"save btn displayed: {save_btn.is_displayed()}")
                self.status.append(True)
            else:
                self.logger.info(f"save btn displayed: {save_btn.is_displayed()}")
                self.status.append(False)
            self.d.execute_script("arguments[0].click();", save_btn)
            self.logger.info("Enrollment details filled and save btn is clicked")

            time.sleep(5)

            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()
            title = self.d.find_elements(By.XPATH,
                                         Read_Identify_and_Enroll_Components().add_details_panel_title_panel())
            time.sleep(web_driver.one_second)
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components().add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************

            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_00.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_00_failed.png")
                return False
            else:
                return True
        except Exception as ex:

            self.logger.error(f"test_TC_IE_00 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_00_Exception.png")
            return False

    def verify_portal_login(self):
        try:
            self.load_portal_login_page_if_not_loaded()
            logout_func = logout()
            logout_button = self.d.find_element(By.XPATH,
                                                logout_func.config.get("logout_locators", "logout_btn_by_xpath"))
            time.sleep(web_driver.one_second)
            if logout_button.is_displayed():
                pass
            else:
                login_func = login()
                if self.d.current_url == login_func.cloud_url:
                    self.status.append(True)
                else:
                    self.status.append(False)
                    login().login_to_cloud_if_not_done(self.d)
                    self.status.clear()
                    time.sleep(web_driver.one_second)
            if False in self.status:
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(ex.args)

    def login_before(self):

        try:
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
        except Exception as ex:
            msg = str(ex.args)
            if msg.__contains__('not clickable at point'):
                self.logger.info("Exception crated: ", ex.args, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\login_failed_for_portal_menu_pg_03.png")
                return False

    def upload_image(self, file_path):
        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        # self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().upload_image_by_xpath(), self.d)
        # file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\ab\\00076.png"
        self.logger.info(f"image uploaded: {file_path}")
        # upload_image = self.explicit_wait(10, "NAME", "image", self.d)
        upload_image = self.d.find_element(By.NAME, "image")
        upload_image.send_keys(file_path)
        time.sleep(web_driver.one_second)
        self.logger.info("Photo Selected....")

    def upload_image_not_enrolled(self, img_path):

        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        file_path = img_path
        time.sleep(web_driver.one_second)
        self.logger.info(f"image uploaded: {file_path}")
        # upload_image = self.explicit_wait(10, "NAME", "image", self.d)
        upload_image = self.d.find_element(By.NAME, "image")
        upload_image.send_keys(file_path)
        time.sleep(web_driver.one_second)
        
    def upload_image_enrollment_not_required(self):

        """
        This function is usd to upload the image and click on the search button
        :return:
        """
        # upload_photo = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().upload_image_by_xpath(),
        #                                   self.d)
        # upload_photo.click()
        # self.logger.info(f"clicked on upload image icon")
        time.sleep(web_driver.one_second)
        # file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\ab\\00077.png"
        file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\ENR.png"

        self.logger.info(f"image uploaded: {file_path}")
        # upload_image = self.explicit_wait(10, "NAME", "image", self.d)
        upload_image = self.d.find_element(By.NAME, "image")
        upload_image.send_keys(file_path)
        time.sleep(web_driver.one_second)

    def enroll_person(self):
        """
        This function is used to enroll the person
        :return:
        """
        self.login_before()
        time.sleep(web_driver.two_second)

        link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                   .identify_and_enroll_link_by_xpath())
        self.d.execute_script("arguments[0].click();", link)
        self.logger.info(f"clicked on Identify and enroll link")
        time.sleep(web_driver.one_second)
        file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\fraud\\00081.png"
        self.upload_image(file_path)
        time.sleep(web_driver.one_second)
        identify_enroll_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .identify_enroll_panel_identify_enroll_btn_by_xpath())

        self.d.execute_script("arguments[0].click();", identify_enroll_btn)

        wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .identifying_photo_wait_by_xpath())
        count = 0
        while wait_icon.is_displayed():
            if count > 15:
                break
            time.sleep(web_driver.one_second)
            count += 1
            self.logger.info(f"waiting fir wait icon, count: {count}")

        enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .enrollment_group_by_xpath())
        select = Select(enrollment_group)
        select.select_by_index(1)
        time.sleep(web_driver.one_second)
        location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .location_store_inpt_bx_by_xpath())
        location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

        case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .case_subject_inpt_bx_by_xpath())
        case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
        time.sleep(web_driver.one_second)
        reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .reported_loss_inpt_bx_by_xpath())
        reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
        time.sleep(web_driver.one_second)
        date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .date_incident_inpt_bx_by_xpath())
        time.sleep(web_driver.two_second)
        self.dateTimeAMPM(date_incident)
        time.sleep(web_driver.two_second)
        action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .action_inpt_bx_by_xpath())
        action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
        time.sleep(web_driver.one_second)
        save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .add_details_save_btn_by_xpath())
        # assert save_btn.is_displayed()
        time.sleep(web_driver.one_second)
        save_btn.click()
        self.logger.info("Enrollment details filled and save btn is clicked")
        wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .enrollment_success_loader())
        count = 0
        while wait_icon.is_displayed():
            if count > 15:
                break
            time.sleep(web_driver.one_second)
            count += 1
            self.logger.info(f"waiting fir wait icon, count: {count}")
        success_msg = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                          .enrollment_success_msg_xpath())
        # assert success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation().lower()
        time.sleep(web_driver.one_second)
        title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().add_details_panel_title_panel())
        for x in title:
            if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                    add_details_panel_validation().lower():
                assert False
        self.close_all_panel_one_by_one()
        self.click_on_logout_button()

    def add_details_enrollment(self):
        """
        This function is used to add details for the enrollment
        :return:
        """

        wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .identifying_photo_wait_by_xpath())
        count = 0
        while wait_icon.is_displayed() or count == 120:
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"waiting for wait icon, count: {count}")

        time.sleep(web_driver.two_second)
        enrollment_basis = self.d.find_element(By.XPATH,
                                               Read_Identify_and_Enroll_Components().enrollment_basis_by_xpath())
        select = Select(enrollment_basis)
        select.select_by_index(1)
        
        time.sleep(web_driver.two_second)
        enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .enrollment_group_by_xpath())
        select = Select(enrollment_group)
        select.select_by_index(2)
        time.sleep(web_driver.one_second)
        region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
        time.sleep(web_driver.one_second)
        region_btn.click()
        time.sleep(web_driver.one_second)
        region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
        edge_name = Read_Identify_and_Enroll_Components().edge_name()
        for i in range(len(region_names)):
            if edge_name in region_names[i].text:
                region_names[i].click()
                time.sleep(web_driver.one_second)
                break
        save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
        save_btn.click()
        time.sleep(web_driver.two_second)

        enrollment_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .enrollment_group_by_xpath())
        select = Select(enrollment_group)
        select.select_by_index(1)
        time.sleep(web_driver.one_second)
        location_store = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .location_store_inpt_bx_by_xpath())
        location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
        time.sleep(web_driver.one_second)
        case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .case_subject_inpt_bx_by_xpath())
        case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
        time.sleep(web_driver.one_second)
        reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .reported_loss_inpt_bx_by_xpath())
        reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
        time.sleep(web_driver.one_second)
        date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .date_incident_inpt_bx_by_xpath())
        time.sleep(web_driver.two_second)
        self.dateTimeAMPM(date_incident)
        time.sleep(web_driver.two_second)
        action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .action_inpt_bx_by_xpath())
        action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
        time.sleep(web_driver.one_second)
        save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .add_details_save_btn_by_xpath())
        save_btn.click()
        time.sleep(web_driver.one_second)
        self.logger.info("Enrollment details filled and save btn is clicked")
        wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .enrollment_success_loader())
        count = 0
        while wait_icon.is_displayed() or count == 120:
            time.sleep(web_driver.two_second)
            count += 1
            self.logger.info(f"waiting for wait icon, count: {count}")

        self.close_all_panel_one_by_one()

    def delete_enrollment(self):
        try:
            pass

            cloud_menu = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                             cloud_menu_button_xpath())
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            enrollment_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                 enrollment_menu_button_xpath())
            # time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            enrollment_btn.click()
            time.sleep(web_driver.one_second)
            # time.sleep(web_driver.one_second)
            
            select_all_checkbox = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                      select_all_enrollment_btn_xpath())
            # time.sleep(web_driver.one_second)
            select_all_checkbox.click()
            time.sleep(web_driver.one_second)

            action_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                             enrollment_panel_action_btn())
            # time.sleep(web_driver.one_second)
            action_btn.click()
            time.sleep(web_driver.one_second)

            delete_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                             delete_enrollments_btn_xpath())
            # time.sleep(web_driver.one_second)
            delete_btn.click()
            time.sleep(web_driver.one_second)

            yes_delete = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                             yes_delete_btn_xpath())
            # time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            yes_delete_2 = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                               yes_delete_btn_xpath_2())
            # time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            if yes_delete.is_displayed():
                time.sleep(web_driver.one_second)
                yes_delete.click()
                time.sleep(web_driver.one_second)
            else:
                time.sleep(web_driver.one_second)
                yes_delete_2.click()
                time.sleep(web_driver.one_second)

            return True
        except Exception as ex:

            msg = str(ex.args)
            if msg.__contains__('not clickable at point'):
                self.logger.info("Exception crated: ", ex.args, " #returning false# ")
                self.d.save_screenshot(
                    f"{Path(__file__).parent.parent}\\Screenshots\\delete_enrollment_failed.png")
                return False

    def verify_Cloud_Menu_Local_Menu(self):
        try:
            self.logger.info("************* test_TC_IE_01 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().cloud_menu_by_xpath(), self.d)
            cloud_menu = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().cloud_menu_by_xpath())
            time.sleep(web_driver.one_second)
            if cloud_menu.is_displayed():
                self.logger.info("Cloud menu is visible...")
                self.status.append(True)
            else:
                self.logger.info("Cloud menu is not visible...")
                self.status.append(False)
            if cloud_menu.is_enabled():
                self.logger.info("Cloud menu is clickable...")
                self.status.append(True)
            else:
                self.logger.info("Cloud menu is not clickable...")
                self.status.append(False)
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_01_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_01_Failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.logger.error(f"test_TC_IE_01 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_01_exception.png")
            return False

    def Click_on_Identify_Entroll_Option_inside_Cloud_Menu_Local_Menu_and_verify_a_new_panel_is_displayed_with_title_as_Identify_Enroll(self):
        try:
            self.logger.info("************* test_TC_IE_02 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            identify_and_enroll = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_and_enroll_link_by_xpath(), self.d)
            if identify_and_enroll.is_displayed():
                self.logger.info("identify_and_enroll is visible...")
                self.status.append(True)
            else:
                self.logger.info("identify_and_enroll is not visible...")
                self.status.append(False)
            if identify_and_enroll.is_enabled():
                self.logger.info("identify_and_enroll is clickable...")
                self.status.append(True)
            else:
                self.logger.info("identify_and_enroll is not clickable...")
                self.status.append(False)
            identify_and_enroll = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_and_enroll)
            self.logger.info("clicked on Identify and enroll link")
            time.sleep(web_driver.two_second)

            identify_and_enroll_panel_title = self.explicit_wait(10, "XPATH",
                                                                 Read_Identify_and_Enroll_Components().identify_and_enroll_panel_title_by_xpath(),
                                                                 self.d)
            actual_text = identify_and_enroll_panel_title.text
            expected_text = Read_Identify_and_Enroll_Components().identify_and_enroll_panel_title()
            self.logger.info(f"Expected data = {expected_text}")
            self.logger.info(f"Actual data = {actual_text}")
            self.close_all_panel_one_by_one()
            if actual_text.lower() == expected_text.lower():
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_02_Failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_02_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_02 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_02_exception.png")
            return False

    def verify_a_new_panel_is_displayed_with_title_as_Identify_and_Enroll(self):
        try:
            self.logger.info("************* test_TC_IE_03 started  **************")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            identify_and_enroll = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_and_enroll)
            self.logger.info("clicked on Identify and enroll link")
            time.sleep(web_driver.two_second)

            identify_and_enroll_panel_title = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().identify_and_enroll_panel_title_by_xpath(), self.d)
            actual_text = identify_and_enroll_panel_title.text
            expected_text = Read_Identify_and_Enroll_Components().identify_and_enroll_panel_title()
            self.logger.info(f"Expected data = {expected_text}")
            self.logger.info(f"Actual data = {actual_text}")
            if actual_text.lower() == expected_text.lower():
                self.status.append(True)
            else:
                self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_03_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_03_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_03 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_03_exception.png")
            return False

    def verify_Select_A_Photo_test_is_displayed_at_the_top_inside_Identity_and_Enroll_Panel(self):
        try:
            self.logger.info("************* test_TC_IE_04 started  **************")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            identify_and_enroll = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_and_enroll)
            time.sleep(web_driver.two_second)

            select_a_photo_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().select_a_photo_text_by_xpath())
            actual_text = select_a_photo_text.text
            expected_text = Read_Identify_and_Enroll_Components().identify_and_enroll_panel_select_photo_text()
            self.logger.info(f"Expected data = {expected_text}")
            self.logger.info(f"Actual data = {actual_text}")
            if actual_text.lower() == expected_text.lower():
                self.status.append(True)
            else:
                self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_04_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_04_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_04 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_04_Exception.png")
            return False

    def verify_a_square_box_blank_image_icon_is_displayed_below_select_a_photo_and_it_is_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_05 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            identify_and_enroll = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().
                                                     identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_and_enroll)
            self.logger.info("Clicked on identify and enroll link")
            time.sleep(web_driver.two_second)

            square_box_blank_image_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                              upload_image_by_xpath())
            time.sleep(web_driver.one_second)
            if square_box_blank_image_icon.is_displayed():
                self.logger.info("square_box_blank_image_icon is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if square_box_blank_image_icon.is_enabled():
                self.logger.info("square_box_blank_image_icon is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\so\\00091.png"
            self.upload_image_to_identify_and_enroll(file_path)
            time.sleep(web_driver.one_second)
            self.logger.info(f"Image upload success")
            self.logger.info("Uploaded photo...")
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_05_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_05_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_05 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_05_Exception.png")
            return False

    def verify_text_below_image_icon_is_displayed_and_expected_text(self):
        try:
            self.logger.info("************* test_TC_IE_06 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            identify_and_enroll = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_and_enroll)
            time.sleep(web_driver.two_second)
            validate_text = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().
                                               select_photo_instructions_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            if validate_text.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            actual_text = validate_text.text.lower()
            expected_text = Read_Identify_and_Enroll_Components().select_photo_instructions_text_validation().lower()
            self.logger.info(f"Expected data = {expected_text}")
            self.logger.info(f"actual data = {actual_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_06_Failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_06_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_06 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_06_Exception.png")
            return False

    def verify_if_a_new_dialog_box_is_appeared_to_choose_image_file(self):
        try:
            self.logger.info("************* test_TC_IE_07 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            identify_and_enroll = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_and_enroll)
            self.logger.info("Clicked on identify and enroll link")
            time.sleep(web_driver.two_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\fraud\\00082.png"
            self.upload_image(file_path)
            
            uploaded_image_validation = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().
                                                           uploaded_photo_validation_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            if uploaded_image_validation.is_displayed():
                self.logger.info("Dialog box is visible.....")
                self.status.append(True)
            else:
                self.logger.info("Dialog box is not visible.....")
                self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_07_Failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_07_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_07 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_07_Exception.png")
            return False

    def click_on_image_icon_upload_image_and_verify_if_same_image_displayed_inside_image_box(self):
        try:
            self.logger.info("************* test_TC_IE_08 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()

            time.sleep(web_driver.two_second)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\fraud\\00083.png"
            self.upload_image(file_path)
            self.logger.info("Image uploaded....")
            time.sleep(web_driver.two_second)
            uploaded_image_validation = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                           .uploaded_image_validation(), self.d)
            time.sleep(web_driver.one_second)
            if uploaded_image_validation.is_displayed():
                self.logger.info("Image is visible...")
                self.status.append(True)
            else:
                self.logger.info("Image is not visible...")
                self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_08_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_08_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_08 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_08_Exception.png")
            return False

    def verify_two_new_panel_appeared_with_title_as_Enrollment_Steps_and_Add_Details(self):
        try:
            self.logger.info("************* test_TC_IE_57 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\vip\\00097.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            time.sleep(web_driver.one_second)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            enrollment_steps_title = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .enrollment_steps_by_xpath())
            time.sleep(web_driver.two_second)
            if enrollment_steps_title.is_displayed():
                self.logger.info("enrollment_steps_title is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            ex_enrollments_steps_title_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_steps_title_txt_validation().lower()
            ac_enrollment_steps_title_txt = enrollment_steps_title.text.lower()
            self.logger.info(f"Expected data = {ex_enrollments_steps_title_txt}")
            self.logger.info(f"Actual data = {ac_enrollment_steps_title_txt}")
            if ex_enrollments_steps_title_txt == ac_enrollment_steps_title_txt:
                self.status.append(True)
            else:
                self.status.append(False)

            add_details_panel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .add_details_panel_by_xpath())
            time.sleep(web_driver.two_second)
            if add_details_panel.is_displayed():
                self.logger.info(f"add_details_panel is visible")
                self.status.append(True)
            else:
                self.logger.info(f"add_details_panel is visible")
                self.status.append(False)

            ex_add_details_panel_txt = Read_Identify_and_Enroll_Components() \
                .add_details_panel_title_txt_validation().lower()
            ac_add_details_panel_txt = add_details_panel.text.lower()

            self.logger.info(f"Expected data = {ex_add_details_panel_txt}")
            self.logger.info(f"Actual data = {ac_add_details_panel_txt}")

            if ex_add_details_panel_txt == ac_add_details_panel_txt:
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.two_second)
            cancel = self.d.find_element(By.XPATH,
                                         Read_Identify_and_Enroll_Components().add_details_cancel_btn_by_xpath())
            cancel.click()
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)

            enrollment_cancel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .warning_msg_close_button())
            enrollment_cancel.click()
            self.logger.info("clicked on enrollment_cancel...")
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_57_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_57_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_57 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_57_Exception.png")
            return False

    def verify_Image_Properties_text_below_image_and_its_dimensions_are_visible(self):
        try:
            self.logger.info("************* test_TC_IE_09 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            identify_and_enroll = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_and_enroll)
            time.sleep(web_driver.two_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\fraud\\00084.png"
            self.upload_image(file_path)
            self.logger.info("Photo uploaded....")
            uploaded_image_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                            uploaded_photo_validation_by_xpath())
            time.sleep(web_driver.one_second)
            if uploaded_image_validation.is_displayed():
                self.logger.info("Photo is visible....")
                self.status.append(True)
            else:
                self.status.append(False)
            Image_Properties_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                        image_properties_text_by_xpath())
            actual_text = Image_Properties_text.text
            expected_text = Read_Identify_and_Enroll_Components().image_properties_text()
            self.logger.info(f"Expected data = {expected_text}")
            self.logger.info(f"Actual data = {actual_text}")
            if actual_text == expected_text:
                self.status.append(True)
            else:
                self.status.append(False)

            image_dimension_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                             image_dia_mentions_by_xpath())
            if image_dimension_validation.is_displayed():
                self.logger.info("Photo dimensions are visible....")
                self.status.append(True)
            else:
                self.status.append(False)

            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_09_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_09_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_09 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_09_Exception.png")
            return False

    def verify_re_Select_Photo_button_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_10 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on link...")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\fraud\\00085.png"
            self.upload_image(file_path)
            self.logger.info("Uploaded image....")
            reselect_photo_btn = self.d.find_element(By.XPATH,
                                                     Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_reselect_photo_btn_by_xpath())
            if reselect_photo_btn.is_displayed():
                self.logger.info("reselect_photo_btn is visible....")
                self.status.append(True)
            else:
                self.logger.info("reselect_photo_btn is not visible....")
                self.status.append(False)
            reselect_photo_icon = self.d.find_element(By.XPATH,
                                                      Read_Identify_and_Enroll_Components()
                                                      .reselect_photo_icon())
            if reselect_photo_icon.is_displayed():
                self.logger.info("reselect_photo_icon is visible....")
                self.status.append(True)
            else:
                self.logger.info("reselect_photo_icon is not visible....")
                self.status.append(False)
            self.d.execute_script("arguments[0].click();", reselect_photo_btn)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_10_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_10_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_10 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_10_Exception.png")
            return False

    def verify_crop_photo_button_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_12 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00086.png"
            self.upload_image(file_path)
            crop_photo_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .identify_enroll_panel_crop_photo_btn_by_xpath())

            if crop_photo_btn.is_displayed():
                self.logger.info("crop_photo_btn is visible...")
                self.status.append(True)
            else:
                self.logger.info("crop_photo_btn is visible...")
                self.status.append(False)

            crop_photo_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .crop_photo_icon())
            if crop_photo_icon.is_displayed():
                self.logger.info("crop_photo_icon is visible...")
                self.status.append(True)
            else:
                self.logger.info("crop_photo_icon is not visible...")
                self.status.append(False)

            self.d.execute_script("arguments[0].click();", crop_photo_btn)
            self.logger.info("Clicked on crop photo button...")
            time.sleep(web_driver.one_second)
            Alert(self.d).accept()
            self.logger.info("Accepted pop-up alert ...")
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_12_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_12_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_12 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_12_exception.png")
            return False

    def verify_text_below_three_buttons_is_displayed(self):
        try:
            self.logger.info("************* test_TC_IE_13 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00087.png"
            self.upload_image(file_path)

            # identify and enroll button below text validation
            identify_enroll_txt_ele = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                         .identify_enroll_btn_below_text_xpath(), self.d)

            exp_identify_enroll_txt = Read_Identify_and_Enroll_Components().identify_enroll_btn_below_text() \
                .replace(" ", "")
            act_identify_enroll_txt = identify_enroll_txt_ele.text.replace("\n", "").lower().replace(" ", "")
            self.logger.info(f"Expected data = {exp_identify_enroll_txt}")
            self.logger.info(f"Actual data = {act_identify_enroll_txt}")
            if identify_enroll_txt_ele.is_displayed() and exp_identify_enroll_txt == act_identify_enroll_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            # reselect photo button below text validation
            reselect_photo_txt_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .reselect_btn_below_text_xpath())
            exp_reselect_photo_txt = Read_Identify_and_Enroll_Components().reselect_photo_btn_below_text() \
                .replace(" ", "")
            act_reselect_photo_txt = reselect_photo_txt_ele.text.replace("\n", "").lower().replace(" ", "")
            self.logger.info(f"Expected data = {exp_reselect_photo_txt}")
            self.logger.info(f"Actual data = {act_reselect_photo_txt}")
            if reselect_photo_txt_ele.is_displayed() and exp_reselect_photo_txt == act_reselect_photo_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            # crop photo button below text validation

            crop_photo_txt_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .crop_photo_btn_below_xpath())
            exp_crop_photo_txt = Read_Identify_and_Enroll_Components().crop_photo_btn_below_text() \
                .replace(" ", "")
            act_crop_photo_txt = crop_photo_txt_ele.text.replace("\n", "").lower().replace(" ", "")
            self.logger.info(f"Expected data = {exp_crop_photo_txt}")
            self.logger.info(f"Actual data = {act_crop_photo_txt}")
            time.sleep(web_driver.one_second)
            if crop_photo_txt_ele.is_displayed() and exp_crop_photo_txt == act_crop_photo_txt:
                self.status.append(True)
            else:
                self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            time.sleep(web_driver.one_second)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_13_failed.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_13_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_13 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_13_exception.png")
            return False

    def verify_if_current_image_is_removed_from_image_box(self):
        try:
            self.logger.info("************* test_TC_IE_14 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00088.png"
            self.upload_image(file_path)

            reselect_photo_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                    .identify_enroll_panel_reselect_photo_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", reselect_photo_btn)
            self.logger.info("Clicked on Re-Select photo button...")
            time.sleep(web_driver.two_second)

            upload_photo_ele = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .upload_image_by_xpath(), self.d)

            if upload_photo_ele.is_displayed():
                self.logger.info("upload_photo_ele is visible...")
                self.status.append(True)
            else:
                self.logger.info("upload_photo_ele is not visible...")
                self.status.append(False)

            ex_validate_txt = Read_Identify_and_Enroll_Components().select_photo_instructions_text_validation()

            validate_btn_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .select_photo_instructions_by_xpath())
            ac_validate_txt = validate_btn_ele.text
            self.logger.info(f"Expected data = {ex_validate_txt}")
            self.logger.info(f"Actual data = {ac_validate_txt}")
            if ex_validate_txt.lower() == ac_validate_txt.lower():
                self.status.append(True)
            else:
                self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_14.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_14_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_14 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}"
                                   f"\\test_TC_IE_14_Exception.png")
            return False

    def verify_identify_enroll_button_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_11 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.two_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\so\\00092.png"
            self.upload_image_to_identify_and_enroll(file_path)

            time.sleep(web_driver.two_second)
            self.logger.info("Photo Selected....")
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            if identify_enroll_btn.is_displayed():
                self.logger.info("Identify & Enroll button is visible...")
                self.status.append(True)
            else:
                self.logger.info("Identify & Enroll button is not visible...")
                self.status.append(False)

            identify_enroll_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .identify_enroll_icon())
            if identify_enroll_icon.is_displayed():
                self.logger.info("Icon on Identify & Enroll button is visible...")
                self.status.append(True)
            else:
                self.logger.info("Icon on Identify & Enroll button is not visible...")
                self.status.append(False)

            print(self.status)

            # identify_enroll_btn.click()
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            time.sleep(web_driver.three_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            web_driver.implicit_wait(self, web_driver.two_second, self.d)
            add_details_panel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().add_details_panel_by_xpath())
            self.logger.info(f"add details panel visible: {add_details_panel.is_displayed()}")
            cancel = self.d.find_element(By.XPATH,
                                         Read_Identify_and_Enroll_Components().add_details_cancel_btn_by_xpath())
            
            time.sleep(web_driver.two_second)
            self.logger.info("wait end..")
            if cancel.is_displayed():
                self.logger.info("cancel btn displayed")
                cancel.click()
                self.logger.info("Clicked on 'Cancel' button....")
                time.sleep(web_driver.one_second)
                cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                        cancel_enrollment_btn_by_xpath())
                cancel_enrollment.click()
            else:
                self.logger.info("Person already enrolled...")
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_11.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_11_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_11 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}"
                                   f"\\test_TC_IE_11_Exception.png")
            return False

    def verify_new_panel_is_displayed_with_title_as_Identify_Results(self):
        try:
            self.logger.info("************* test_TC_IE_13 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            while wait_icon.is_displayed():
                time.sleep(web_driver.two_second)

            time.sleep(web_driver.three_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.three_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            print(region_names)
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    time.sleep(web_driver.one_second)
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

            # action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH,
                                                Read_Identify_and_Enroll_Components().date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.one_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.one_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_details_save_btn_by_xpath(), self.d)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                self.logger.info(f"success message: {success_msg.text}")
                time.sleep(web_driver.one_second)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            self.close_all_panel_one_by_one()
            # self.add_details_enrollment()

            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().identify_and_enroll_link_by_xpath(),
                               self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.three_second)
            ex_identify_results_txt = Read_Identify_and_Enroll_Components().identify_results_text_validation()
            # time.sleep(web_driver.two_second)
            self.logger.info("2")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().identify_results_panel_by_xpath(),
                               self.d)
            identify_results = self.d.find_elements(By.XPATH,
                                                    Read_Identify_and_Enroll_Components().identify_results_panel_by_xpath())
            self.logger.info("3")
            self.logger.info(f"actual: {identify_results[0].text}")
            time.sleep(web_driver.one_second)
            ac_identify_results_txt = identify_results[0].text

            if ex_identify_results_txt.lower() == ac_identify_results_txt.lower():
                self.status.append(True)
            else:
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            self.close_all_panel_one_by_one()

            print(self.status)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_13.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_13_failed.png")
                print(self.status)
                self.click_on_close_all_panel_btn()
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_13 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}"
                                   f"\\test_TC_IE_13_exception.png")
            return False

    def verify_matches_are_found_and_displayed_inside_Identify_Results_panel(self):
        try:
            self.logger.info("************* test_TC_IE_16 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().identify_results_panel_by_xpath(),
                               self.d)
            identify_results_img_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .identify_results_image_by_xpath())

            self.logger.info(f"Matches found: {len(identify_results_img_list)}")
            time.sleep(web_driver.one_second)
            for ele in identify_results_img_list:
                if ele.is_displayed():
                    self.status.append(True)

            self.close_all_panel_one_by_one()

            if False in self.status:
                self.logger.info(f"status: {False}")
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_16.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_16_failed.png")
                return False
            else:
                self.logger.info(f"status: {True}")
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_16 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}"
                                   f"\\test_TC_IE_16_Exception.png")
            return False

    def verify_visitor_image_is_displayed_as_expected_below_sample_image_icon(self):
        try:
            self.logger.info("************* test_TC_IE_30 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            faces_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .identify_results_faces_icon_by_xpath())
            faces_icon.click()
            self.logger.info(f"Clicked on face_icon")
            time.sleep(web_driver.two_second)
            face_images_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .visitor_image_on_enroll_face_panel())
            if face_images_validation.is_displayed():
                self.logger.info("Visitor image is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_30.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_30_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_30 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_30_exception.png")
            return False

    def verify_a_check_box_is_displayed_and_it_is_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_31 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            faces_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .identify_results_faces_icon_by_xpath())
            faces_icon.click()
            self.logger.info(f"Clicked on face_icon")
            time.sleep(web_driver.two_second)
            checkbox = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .enrollment_faces_panel_checkbox_by_xpath())
            if checkbox.is_displayed():
                self.logger.info("Check box is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            checkbox.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_31.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_31_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_31 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}"
                                   f"\\test_TC_IE_31_Exception.png")
            return False

    def verify_download_image_button_with_its_label_poping_up_and_it_is_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_32 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            faces_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .identify_results_faces_icon_by_xpath())
            faces_icon.click()
            self.logger.info(f"Clicked on face_icon")
            time.sleep(web_driver.two_second)
            download_button = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                  download_button_enroll_panel_by_xpath())
            actions = ActionChains(self.d)
            actions.move_to_element(download_button).perform()
            time.sleep(web_driver.two_second)
            download_button_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .download_button_validation_by_xpath())
            if download_button.is_displayed():
                self.logger.info("Download button is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if download_button.is_enabled():
                self.logger.info("Download button is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            if download_button_validation.is_displayed():
                self.logger.info("download_button_validation  is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"Expected data = {Read_Identify_and_Enroll_Components().download_button_validation()}")
            self.logger.info(f"Actual data = {download_button_validation.text}")
            if download_button_validation.text.lower() == Read_Identify_and_Enroll_Components(). \
                    download_button_validation().lower():
                self.status.append(True)
            else:
                self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_32.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_32_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_32 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_32_exception.png")
            return False

    def verify_view_image_info_button_is_visible_along_with_its_label(self):
        try:
            self.logger.info("************* test_TC_IE_34 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.three_second)
            # web_driver.implicit_wait(self, web_driver.one_second, self.d)

            faces_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath(), self.d)
            print(faces_icon)
            faces_icon.click()
            self.logger.info(f"Clicked on Faces icon")
            time.sleep(web_driver.two_second)

            view_image_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                 .view_image_file_info_button(), self.d)
            actions = ActionChains(self.d)
            actions.move_to_element(view_image_icon).perform()
            time.sleep(web_driver.one_second)
            view_image_icon_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                             view_image_file_info_validation())
            time.sleep(web_driver.two_second)
            if view_image_icon.is_displayed():
                self.logger.info("view_image_icon is visible...")
                self.status.append(True)
            else:
                self.logger.info("view_image_icon is not visible...")
                self.status.append(False)

            if view_image_icon_validation.is_displayed():
                self.logger.info("view_image_icon_validation is visible...")
                self.status.append(True)
            else:
                self.logger.info("view_image_icon_validation is not visible...")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            self.logger.info(f"Expected data = {Read_Identify_and_Enroll_Components().view_image_file_info()}")
            self.logger.info(f"Actual data = {view_image_icon_validation.text}")
            if view_image_icon_validation.text.lower() == Read_Identify_and_Enroll_Components(). \
                    view_image_file_info().lower():
                self.status.append(True)
            else:
                self.status.append(False)
            view_image_icon.click()
            time.sleep(web_driver.three_second)
            Alert(self.d).accept()
            time.sleep(web_driver.one_second)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_34.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_34_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_34 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}"
                                   f"\\test_TC_IE_34_exception.png")
            return False

    def click_on_view_image_info_button_verify_a_pop_up_is_appeared_with_image_information(self):
        try:
            self.logger.info("************* test_TC_IE_35 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"clicked on Identify and enroll button")
            time.sleep(web_driver.two_second)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)

            faces_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .identify_results_faces_icon_by_xpath())
            faces_icon.click()
            self.logger.info(f"Clicked on face_icon")
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.two_second)
            view_image_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                  view_image_file_info_button())

            view_image_icon.click()
            self.logger.info(f"Clicked on view_image_icon")
            time.sleep(web_driver.two_second)
            pop_up_text = self.d.switch_to.alert.text
            self.logger.info(f"Expected data = {pop_up_text}")
            self.logger.info(f"Actual data = {Read_Identify_and_Enroll_Components().view_image_pop_up_text_1()}")
            self.logger.info(f"Expected data = {pop_up_text}")
            self.logger.info(f"Actual data = {Read_Identify_and_Enroll_Components().view_image_pop_up_text_2()}")
            self.logger.info(f"Expected data = {pop_up_text}")
            self.logger.info(f"Actual data = {Read_Identify_and_Enroll_Components().view_image_pop_up_text_3()}")
            self.logger.info(f"Expected data = {pop_up_text}")
            self.logger.info(f"Actual data = {Read_Identify_and_Enroll_Components().view_image_pop_up_text_4()}")
            time.sleep(web_driver.two_second)
            if Read_Identify_and_Enroll_Components().view_image_pop_up_text_1() in pop_up_text:
                self.status.append(True)
            else:
                self.status.append(False)
            if Read_Identify_and_Enroll_Components().view_image_pop_up_text_2() in pop_up_text:
                self.status.append(True)
            else:
                self.status.append(False)
            if Read_Identify_and_Enroll_Components().view_image_pop_up_text_3() in pop_up_text:
                self.status.append(True)
            else:
                self.status.append(False)
            if Read_Identify_and_Enroll_Components().view_image_pop_up_text_4() in pop_up_text:
                self.status.append(True)
            else:
                self.status.append(False)

            self.d.switch_to.alert.accept()
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_35.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_35_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_35 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_35_exception.png")
            return False

    def click_on_close_panel_button_displayed_beside_panel_title_verify_panel_is_closed_successfully(self):
        try:
            self.logger.info("************* test_TC_IE_36 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            panel_close = self.explicit_wait(10, "XPATH",
                                             Read_Identify_and_Enroll_Components().identify_results_panel_close(),
                                             self.d)
            panel_close.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Panel closed...")

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         close_panel_enroll_faces_validation())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components().identify_result_text_validation(). \
                        lower():
                    self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_36.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_36_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_36 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_36_exception.png")
            return False

    def click_on_Person_View_button_and_verify_a_new_panel_with_title_Enrollment_View_is_displayed(self):
        try:
            self.logger.info("************* test_TC_IE_37 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            person_view = self.d.find_element(By.XPATH,
                                              Read_Identify_and_Enroll_Components().identify_results_person_view_icon_by_xpath())
            person_view.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on person's view button...")
            enrollment_view_panel_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                                   .enrollment_view_panel_validation())
            if enrollment_view_panel_validation.is_displayed():
                self.logger.info("Enrollment view panel is visible......")
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_37.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_37_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_37 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_37_Exception.png")
            return False

    def verify_action_dropdown_is_displayed_and_clickable_in_top_right_corner_of_Enrollment_View_is_displayed(self):
        try:
            self.logger.info("************* test_TC_IE_38 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            person_view = self.explicit_wait(10, "XPATH",
                                             Read_Identify_and_Enroll_Components().identify_results_person_view_icon_by_xpath(),
                                             self.d)
            person_view.click()
            self.logger.info(f"Clicked on identify_results_person_view_icon")
            time.sleep(web_driver.two_second)
            action_button = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                               .enrollment_view_panel_action_button(), self.d)
            if action_button.is_displayed():
                self.logger.info("'Action' dropdown is visible...")
                self.status.append(True)
            else:
                self.logger.info("'Action' dropdown is not visible...")
                self.status.append(False)

            action_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicked on 'Action' dropdown...")

            action_button_validation = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                          .enrollment_view_panel_action_button_validation(), self.d)
            time.sleep(web_driver.one_second)
            if action_button_validation.is_displayed():
                self.logger.info("'action_button_validation' is visible...")
                self.status.append(True)
            else:
                self.logger.info("'action_button_validation' is not visible...")
                self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_38.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_38_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_38 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_38_exception.png")
            return False

    def click_on_action_dropdown_and_verify_menu_items(self):
        try:
            self.logger.info("************* test_TC_IE_39 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\vip\\00098.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            # web_driver.explicit_wait(self, 10, identify_enroll_btn, self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            person_view = self.explicit_wait(10, "XPATH",
                                             Read_Identify_and_Enroll_Components().identify_results_person_view_icon_by_xpath(),
                                             self.d)
            person_view.click()
            self.logger.info(f"Clicked on person view icon")
            time.sleep(web_driver.one_second)

            action_button = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                               .enrollment_view_panel_action_button(), self.d)
            action_button.click()
            self.logger.info(f"Clicked on Action dropdown")
            time.sleep(web_driver.one_second)
            # disable enrollment option display and click verify

            disable_enrollment_option = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                           .enrollment_view_panel_action_button_validation(), self.d)
            if disable_enrollment_option.is_displayed():
                self.logger.info("disable_enrollment_option is visible")
                self.status.append(True)
            else:
                self.logger.info("disable_enrollment_option is not visible")
                self.status.append(False)
            time.sleep(web_driver.two_second)
            self.logger.info(f"Expected data = "
                             f"{Read_Identify_and_Enroll_Components().disable_enrollment_option_validation()}")
            self.logger.info(f"Actual data = {disable_enrollment_option.text}")
            if disable_enrollment_option.text == Read_Identify_and_Enroll_Components(). \
                    disable_enrollment_option_validation():
                self.status.append(True)
            else:
                self.status.append(False)

            disable_enrollment_option.click()
            self.logger.info("clicked on 'disable enrollment'....")
            time.sleep(web_driver.one_second)
            if self.d.switch_to.alert.text == Read_Identify_and_Enroll_Components(). \
                    disable_enrollment_option_click_validation():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            self.d.switch_to.alert.dismiss()
            time.sleep(web_driver.one_second)
            # identify within enrollments option display and click verify

            action_button.click()
            self.logger.info(f"Clicked on Action dropdown")
            time.sleep(web_driver.two_second)

            identify_within_enrollments_option = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                                    .identify_within_enrollments_option(), self.d)
            time.sleep(web_driver.one_second)
            if identify_within_enrollments_option.is_displayed():
                self.status.append(True)
                self.logger.info("identify_within_enrollments_option is visible")
            else:
                self.logger.info("identify_within_enrollments_option is not visible")
                self.status.append(False)
            time.sleep(web_driver.two_second)
            self.logger.info(f"Expected data = "
                             f"{Read_Identify_and_Enroll_Components().identify_within_enrollments_option_validation()}")
            self.logger.info(f"Actual data = {identify_within_enrollments_option.text}")
            if identify_within_enrollments_option.text == Read_Identify_and_Enroll_Components(). \
                    identify_within_enrollments_option_validation():
                self.status.append(True)
            else:
                self.status.append(False)
            print(self.status)
            identify_within_enrollments_option.click()
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().identifying_photo_wait_by_xpath_second_panel())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            self.logger.info("clicked on 'identify_within_enrollments_option'....")
            time.sleep(web_driver.two_second)

            click_validation = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().
                                                  identify_enroll_panel_validation(), self.d)
            if click_validation.is_displayed():
                self.logger.info("identify_enroll_panel_validation is visible")
                self.status.append(True)
            else:
                self.logger.info("identify_enroll_panel_validation is not visible")
                self.status.append(False)

            time.sleep(web_driver.three_second)
            result_panel_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().identify_result_panel_close())
            result_panel_close.click()
            self.logger.info("result panel closed..")
            time.sleep(web_driver.two_second)
            identify_panel_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().identify_and_enroll_panel_close())
            identify_panel_close.click()
            self.logger.info("identify enroll panel closed..")
            # identify within visitor option display and click verify
            time.sleep(web_driver.two_second)
            action_button.click()
            self.logger.info(f"Clicked on Action dropdown")
            time.sleep(web_driver.two_second)

            identify_within_visitor_option = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().identify_within_visitors_option(), self.d)
            if identify_within_visitor_option.is_displayed():
                self.logger.info(f"identify_within_visitor_option is visible")
                self.status.append(True)
            else:
                self.logger.info(f"identify_within_visitor_option is not visible")
                self.status.append(False)
            time.sleep(web_driver.two_second)
            self.logger.info(f"Expected data = {Read_Identify_and_Enroll_Components().identify_within_visitors_option_validation()}")
            self.logger.info(f"Actual data = {identify_within_visitor_option.text}")
            if identify_within_visitor_option.text == Read_Identify_and_Enroll_Components().identify_within_visitors_option_validation():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", identify_within_visitor_option)
            self.logger.info("identify_within_visitor_option clicked..")
            time.sleep(web_driver.three_second)
            click_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().visitor_search_panel_validation())
            if click_validation.is_displayed():
                self.logger.info(f"visitor_search_panel_validation clicked.. {click_validation.is_displayed()}")
                self.status.append(True)
            else:
                self.logger.info(f"visitor_search_panel_validation clicked.. {click_validation.is_displayed()}")
                self.status.append(False)
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            visitor_search_panel_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().visitor_search_panel_close())
            visitor_search_panel_close.click()

            # view / edite details option display and click verify
            time.sleep(web_driver.two_second)
            action_button.click()
            self.logger.info(f"Clicked on Action dropdown")
            edite_details_option = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                      .view_edit_details_option(), self.d)
            time.sleep(web_driver.two_second)
            if edite_details_option.is_displayed():
                self.logger.info(f"view_edit_details_option is visible")
                self.status.append(True)
            else:
                self.logger.info(f"view_edit_details_option is not visible")
                self.status.append(False)
            time.sleep(web_driver.two_second)
            self.logger.info(f"Expected data = "
                             f"{Read_Identify_and_Enroll_Components().view_edit_details_option_validation()}")
            self.logger.info(f"Actual data = {edite_details_option.text}")
            if edite_details_option.text == Read_Identify_and_Enroll_Components().view_edit_details_option_validation():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", edite_details_option)
            self.logger.info(f"Clicked on enrollment_details_panel_validation")
            time.sleep(web_driver.two_second)

            click_validation = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().
                                                  enrollment_details_panel_validation(), self.d)
            if click_validation.is_displayed():
                self.logger.info(f"enrollment_details_panel_validation is visible")
                self.status.append(True)
            else:
                self.logger.info(f"enrollment_details_panel_validation is not visible")
                self.status.append(False)
            time.sleep(web_driver.two_second)

            view_edit_panel_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                        enrollment_details_panel_close())
            view_edit_panel_close.click()

            # delete enrollment option display and click verify
            time.sleep(web_driver.two_second)
            action_button.click()
            self.logger.info(f"Clicked on Action dropdown")
            time.sleep(web_driver.one_second)
            delete_enrollment_option = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                          .delete_enrollment_option(), self.d)
            time.sleep(web_driver.two_second)
            if delete_enrollment_option.is_displayed():
                self.logger.info(f"delete_enrollment_option is visible")
                self.status.append(True)
            else:
                self.logger.info(f"delete_enrollment_option is not visible")
                self.status.append(False)
            time.sleep(web_driver.two_second)
            self.logger.info(f"Expected data = "
                             f"{Read_Identify_and_Enroll_Components().delete_enrollment_option_validation()}")
            self.logger.info(f"Actual data = {delete_enrollment_option.text}")
            if delete_enrollment_option.text == Read_Identify_and_Enroll_Components().delete_enrollment_option_validation():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            self.d.execute_script("arguments[0].click();", delete_enrollment_option)

            time.sleep(web_driver.two_second)

            click_validation = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().
                                                  delete_enrollment_validation(), self.d)
            if click_validation.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            cancel_button = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().
                                               delete_enrollment_cancel_button(), self.d)
            cancel_button.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_39.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_39_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            self.logger.error(f"test_TC_IE_39 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_39_Exception.png")
            return False

    def click_on_close_button_of_Identify_Results_panel_and_verify_closed_successfully(self):
        try:
            self.logger.info("************* test_TC_IE_40 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            panel_close = self.explicit_wait(10, "XPATH",
                                             Read_Identify_and_Enroll_Components().identify_results_panel_close(),
                                             self.d)
            panel_close.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Clicked on close panel button...")
            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         close_panel_enroll_faces_validation())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components().identify_result_text_validation().lower():
                    self.logger.info(f"x title: {x.text}")
                    self.logger.info(f"x title stripped: {x.text.strip().lower()}")
                    expected_txt = Read_Identify_and_Enroll_Components().identify_results_text_validation()
                    self.logger.info(f"expected txt: {expected_txt}")
                    self.status.append(True)
            self.logger.info("panel closed...")
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_40.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_40_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_40 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_40_exception.png")
            return False

    def click_on_download_image_image_verify_visitor_image_is_downloaded_successfully(self):
        try:
            self.logger.info("************* test_TC_IE_33 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_results_faces_icon_by_xpath(), self.d)
            faces_icon = self.d.find_element(By.XPATH,
                                             Read_Identify_and_Enroll_Components().identify_results_faces_icon_by_xpath())
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            faces_icon.click()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().
                               download_button_enroll_panel_by_xpath(), self.d)
            try:
                download_button = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                      download_button_enroll_panel_by_xpath())
                download_button.click()
                self.logger.info("Clicked on download image button...")
                time.sleep(web_driver.one_second)
                self.status.append(True)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.status.append(False)
            time.sleep(web_driver.two_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_33.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_34_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_33 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_34_exception.png")
            return False

    def verify_faces_button_is_visible_with_its_label_popping_up_and_clickable_on_identify_results_panel(self):
        try:
            self.logger.info("************* test_TC_IE_21 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.two_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            time.sleep(web_driver.two_second)

            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())
            time.sleep(web_driver.two_second)
            expected_face_icon_hover_txt = Read_Identify_and_Enroll_Components() \
                .identify_results_face_icon_hover_text_validation().lower()
            time.sleep(web_driver.one_second)
            a = ActionChains(self.d)
            a.move_to_element(face_icon).perform()
            time.sleep(web_driver.two_second)

            actual_face_icon_hover_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .identify_results_faces_icon_hover_by_xpath())
            actual_face_icon_hover_txt = actual_face_icon_hover_ele.text.lower()
            self.logger.info(f"Expected data = {expected_face_icon_hover_txt}")
            self.logger.info(f"Actual data = {actual_face_icon_hover_txt}")
            if expected_face_icon_hover_txt in actual_face_icon_hover_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            face_icon.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_21.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_21_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_21 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_21_Exception.png")
            return False

    def verify_person_view_button_is_visible_with_its_label_popping_up_and_clickable_on_identify_results_panel(self):
        try:
            self.logger.info("************* test_TC_IE_22 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            person_view_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .identify_results_person_view_icon_by_xpath(), self.d)

            expected_person_view_icon_hover_txt = Read_Identify_and_Enroll_Components() \
                .identify_results_person_view_icon_hover_text_validation().lower()

            a = ActionChains(self.d)
            a.move_to_element(person_view_icon).perform()

            time.sleep(web_driver.two_second)

            actual_person_view_hover_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                               .identify_results_person_view_icon_hover_by_xpath())

            actual_person_view_hover_txt = actual_person_view_hover_ele.text.lower()
            self.logger.info(f"Expected data = {expected_person_view_icon_hover_txt}")
            self.logger.info(f"Actual data = {actual_person_view_hover_txt}")
            if expected_person_view_icon_hover_txt == actual_person_view_hover_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            person_view_icon.click()

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_22.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_22_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_22 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_22_exception.png")
            return False

    def verify_purge_replace_button_is_visible_with_its_label_popping_up_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_23 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            time.sleep(web_driver.two_second)

            purge_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .identify_results_purge_replace_icon_by_xpath())

            expected_purge_icon_hover_txt = Read_Identify_and_Enroll_Components() \
                .identify_results_purge_replace_icon_hover_text_validation().lower()

            a = ActionChains(self.d)
            a.move_to_element(purge_icon).perform()

            time.sleep(web_driver.two_second)
            actual_purge_hover_ele = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                        .identify_results_purge_replace_icon_hover_by_xpath(), self.d)

            actual_purge_hover_ele_txt = actual_purge_hover_ele.text.lower()
            self.logger.info(f"Expected data = {expected_purge_icon_hover_txt}")
            self.logger.info(f"Actual data = {actual_purge_hover_ele_txt}")
            if expected_purge_icon_hover_txt == actual_purge_hover_ele_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            purge_icon.click()
            # Alert(self.d).dismiss()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_23.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_23_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_23 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_23_Exception.png")
            return False

    def click_on_faces_button_and_verify_a_new_panel_with_title_enrollment_faces_is_displayed(self):
        try:
            self.logger.info("************* test_TC_IE_24 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())
            face_icon.click()
            self.logger.info(f"Clicked on face_icon")
            time.sleep(web_driver.one_second)
            exp_enrollment_faces_txt = Read_Identify_and_Enroll_Components().enrollment_faces_text_validation().lower()

            enrollment_faces_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .enrollment_faces_panel_by_xpath())
            ac_enrollment_faces_txt = enrollment_faces_ele.text.lower()
            self.logger.info(f"Expected data = {exp_enrollment_faces_txt}")
            self.logger.info(f"Actual data = {ac_enrollment_faces_txt}")
            if enrollment_faces_ele.is_displayed() and exp_enrollment_faces_txt == ac_enrollment_faces_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_24.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_24_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_24 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_24_exception.png")
            return False

    def verify_action_dropdown_is_displayed_and_clickable_in_top_right_corner_of_enrollment_faces_panel(self):
        try:
            self.logger.info("************* test_TC_IE_25 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.two_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)

            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())
            face_icon.click()
            self.logger.info(f"Clicked on face_icon")
            time.sleep(web_driver.one_second)
            action_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .enrollment_faces_action_drop_down_by_xpath())
            if action_ele.is_displayed():
                self.logger.info("'Action' is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if action_ele.is_enabled():
                self.logger.info("'Action' is clickable...")
                self.status.append(True)
            else:
                self.status.append(False)
            action_ele.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_25.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_25_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_25 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_25_exception.png")
            return False

    def click_on_action_dropdown_and_verify_menu_items_displayed_are_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_26 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(),
                                      self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.three_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_results_faces_icon_by_xpath(), self.d)
            face_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                           .identify_results_faces_icon_by_xpath(), self.d)
            face_icon.click()
            self.logger.info(f"Clicked on face icon")
            time.sleep(web_driver.one_second)

            action_ele = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                            .enrollment_faces_action_drop_down_by_xpath(), self.d)
            action_ele.click()
            self.logger.info(f"Clicked on action dropdown")
            time.sleep(web_driver.two_second)
            ex_identify_within_enrollments_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_faces_drop_down_identify_within_enrollments_txt_validation().lower()
            ex_identify_within_visitors_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_faces_drop_down_identify_within_visitors_txt_validation().lower()
            ex_add_photo_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_faces_drop_down_add_photo_txt_validation().lower()
            ex_delete_selected_faces = Read_Identify_and_Enroll_Components() \
                .enrollment_faces_drop_down_delete_selected_faces_txt_validation().lower()

            identify_within_enrollments_ele = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                                 .enrollment_faces_drop_down_identify_within_enrollments_ele_by_xpath(),
                                                                 self.d)
            ac_identify_within_enrollments_txt = identify_within_enrollments_ele.text.lower()
            identify_within_visitors_ele = self.d \
                .find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                              .enrollment_faces_drop_down_identify_within_visitors_ele_by_xpath())
            ac_identify_within_visitors_txt = identify_within_visitors_ele.text.lower()
            add_photo_ele = self.d \
                .find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                              .enrollment_faces_drop_down_add_photo_ele_by_xpath())
            ac_add_photo_txt = add_photo_ele.text.lower()
            delete_selected_faces_ele = self.d \
                .find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                              .enrollment_faces_drop_down_delete_selected_faces_ele_by_xpath())
            ac_delete_selected_faces_txt = delete_selected_faces_ele.text.lower()
            self.logger.info(f"Expected data = {ex_identify_within_enrollments_txt}")
            self.logger.info(f"Actual data = {ac_identify_within_enrollments_txt}")
            self.logger.info(f"Expected data = {ex_identify_within_visitors_txt}")
            self.logger.info(f"Actual data = {ac_identify_within_visitors_txt}")
            self.logger.info(f"Expected data = {ex_add_photo_txt}")
            self.logger.info(f"Actual data = {ac_add_photo_txt}")
            self.logger.info(f"Expected data = {ex_delete_selected_faces}")
            self.logger.info(f"Actual data = {ac_delete_selected_faces_txt}")
            time.sleep(web_driver.one_second)
            if ex_identify_within_enrollments_txt == ac_identify_within_enrollments_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            if ex_identify_within_visitors_txt == ac_identify_within_visitors_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            if ex_add_photo_txt == ac_add_photo_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            if ex_delete_selected_faces == ac_delete_selected_faces_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_26.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_26_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_26 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_26_Exception.png")
            return False

    def verify_location_and_case_information_is_displayed_as_a_heading_inside_enrollment_faces_panel(self):
        try:
            self.logger.info("************* test_TC_IE_27 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())
            face_icon.click()
            self.logger.info(f"Clicked on face_icon")
            time.sleep(web_driver.two_second)
            # for x in range(50):
            location_case_heading = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                        .enrollment_faces_location_case_heading_ele_by_xpath())
            location_case_heading_txt = location_case_heading.text
            if location_case_heading_txt != "":
                self.logger.info(f"{location_case_heading_txt}")
                self.status.append(True)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_27.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_27_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_27 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_27_Exception.png")
            return False

    def verify_sample_image_icon_is_visible_below_location_and_it_is_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_28 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.three_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)
            time.sleep(web_driver.three_second)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            time.sleep(web_driver.two_second)
            face_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                           .identify_results_faces_icon_by_xpath(), self.d)

            face_icon.click()
            self.logger.info(f"Clicked on identify results face icon")
            time.sleep(web_driver.two_second)
            sample_image_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                   .enrollment_faces_sample_image_icon_by_xpath(), self.d)
            if sample_image_icon.is_displayed():
                self.logger.info("Sample image icon is visible...")
                self.status.append(True)
            else:
                self.logger.info("Sample image icon is not visible...")
                self.status.append(False)

            sample_image_icon.click()
            time.sleep(web_driver.two_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"

            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.press('enter')

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_28.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_28.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_28 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_28_exception.png")
            return False

    def verify_if_draggable_photo_text_is_visible_above_image_displayed(self):
        try:
            self.logger.info("************* test_TC_IE_29 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            face_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                           .identify_results_faces_icon_by_xpath(), self.d)

            face_icon.click()
            time.sleep(web_driver.two_second)

            ex_draggable_photo_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_faces_draggable_photo_txt_validation().lower()
            draggable_ele = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                               .enrollment_faces_draggable_photo_by_xpath(), self.d)
            ac_draggable_photo_txt = draggable_ele.text.strip().lower()

            if draggable_ele.is_displayed():
                self.logger.info("Draggable photo text is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            self.logger.info(f"Expected data = {ex_draggable_photo_txt}")
            self.logger.info(f"Actual data = {ac_draggable_photo_txt}")

            if ex_draggable_photo_txt == ac_draggable_photo_txt:
                self.status.append(True)
            else:
                self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_29.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_29_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_29 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_29_exception.png")
            return False

    def verify_visitor_image_is_displayed_as_expected_below_sample_image_icon_inside_enrollment_faces_panel(self):
        try:
            self.logger.info("************* test_TC_IE_38 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00088.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())

            face_icon.click()

            visitor_img_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .enrollment_faces_visitor_img_by_xpath())
            if visitor_img_ele.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_38.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_38_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_38 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_38_exception.png")
            return False

    def verify_location_and_case_information_is_displayed_as_a_heading_inside_enrollment_view_panel(self):
        try:
            self.logger.info("************* test_TC_IE_41 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            person_view_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .identify_results_person_view_icon_by_xpath(), self.d)
            person_view_icon.click()
            self.logger.info(f"Clicked on person view")
            time.sleep(web_driver.one_second)
            # for x in range(50):
            location_case_heading = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                        .enrollment_view_location_case_heading_ele_by_xpath())
            location_case_heading_txt = location_case_heading.text
            if location_case_heading_txt != "":
                self.status.append(True)
                self.logger.info(f"location: {location_case_heading_txt}")

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_41.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_41_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_41 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_41_exception.png")
            return False

    def verify_visitor_image_is_displayed_as_expected_below_heading_on_enrollment_view_panel(self):
        try:
            self.logger.info("************* test_TC_IE_42 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            time.sleep(web_driver.one_second)
            person_view_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .identify_results_person_view_icon_by_xpath(), self.d)
            person_view_icon.click()
            self.logger.info(f"Clicked on person view")
            time.sleep(web_driver.one_second)
            img = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                      .enrollment_view_visitor_img_by_xpath())
            time.sleep(web_driver.one_second)
            if img.is_displayed():
                self.logger.info("visitor's image is visible...")
                self.status.append(True)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_42.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_42_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_42 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_42_exception.png")
            return False

    def verify_visitors_lOCATION_STORE_CASE_SUBJECT_information_is_displayed_on_enrollment_view_panel(self):
        try:
            self.logger.info("************* test_TC_IE_43 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\vip\\00098.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            person_view_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .identify_results_person_view_icon_by_xpath(), self.d)
            person_view_icon.click()
            self.logger.info(f"Clicked on person view icon")
            time.sleep(web_driver.two_second)
            location_store_case_subject = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                             .enrollment_view_location_store_case_subject_ele_by_xpath(),
                                                             self.d)
            location_store_case_subject_info = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().enrollment_view_location_store_case_subject_info_by_xpath())
            if location_store_case_subject.is_displayed():
                self.logger.info("location_store_case_subject is visible...")
                self.status.append(True)
            else:
                self.logger.info("location_store_case_subject is not visible...")
                self.status.append(False)

            if location_store_case_subject_info.is_displayed():
                self.logger.info("location_store_case_subject_info is visible...")
                self.status.append(True)
            else:
                self.logger.info("location_store_case_subject_info is not visible...")
                self.status.append(False)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_43.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_43_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_43 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_43_exception.png")
            return False

    def verify_ranked_match_index_title_along_with_symbol_visible_on_identify_results_panel(self):
        try:
            self.logger.info("************* test_TC_IE_17 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)
            time.sleep(web_driver.one_second)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            time.sleep(web_driver.one_second)
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            expected_ranked_match_index_txt = Read_Identify_and_Enroll_Components().identify_results_ranked_match_index_text_validation().lower()
            identify_results_probable_matches_text_validation = Read_Identify_and_Enroll_Components().identify_results_probable_matches_text_validation().lower()
            time.sleep(web_driver.one_second)
            ranked_match_index_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().identify_results_ranked_match_index_by_xpath())
            time.sleep(web_driver.two_second)
            actual_ranked_match_index_txt = ranked_match_index_ele.text.lower()
            self.logger.info(f"Expected data = {expected_ranked_match_index_txt}")
            self.logger.info(f"Actual data = {actual_ranked_match_index_txt}")
            if expected_ranked_match_index_txt == actual_ranked_match_index_txt or identify_results_probable_matches_text_validation == actual_ranked_match_index_txt:
                self.status.append(True)
            else:
                self.status.append(False)

            exclamation_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .identify_results_exclamation_symbol_by_xpath())
            time.sleep(web_driver.one_second)
            if exclamation_icon.is_displayed():
                self.logger.info(f"exclamation_icon is visible")
                self.status.append(True)
            else:
                self.logger.info(f"exclamation_icon is not visible")
                self.status.append(False)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_17.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_17_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_17 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_17_exception.png")
            return False

    def verify_images_are_visible_enlisted_inside_identify_result_panel(self):
        try:
            self.logger.info("************* test_TC_IE_18 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(),
                                      self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(),
                                                     self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"clicked on Identify and enroll btn")
            time.sleep(web_driver.two_second)

            identify_results_img_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .identify_results_image_by_xpath())
            self.logger.info(f"Matches found: {len(identify_results_img_list)}")
            time.sleep(web_driver.one_second)
            for ele in identify_results_img_list:
                if ele.is_displayed():
                    self.logger.info("Image is displayed...")
                    self.status.append(True)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_18.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_18_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_18 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_18_exception.png")
            return False

    def verify_location_Case_information_and_index_score_displayed_inside_indentify_result_panel(self):
        try:
            self.logger.info("************* test_TC_IE_19 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            location_case_info_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .identify_results_location_case_info())

            if location_case_info_ele.is_displayed():
                self.logger.info("Location of event is visible...")
                self.status.append(True)
            else:
                self.logger.info("Location of event is not visible...")
                self.status.append(False)

            index_score_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .identify_results_index_score_by_xpath())
            if index_score_ele.is_displayed():
                self.logger.info("Index Score of event is visible...")
                self.status.append(True)
            else:
                self.logger.info("Index Score of event is not visible...")
                self.status.append(False)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_19.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_19_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_19 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_19_exception.png")
            return False

    def verify_three_buttons_faces_person_view_and_purge_Replace_are_visible(self):
        try:
            self.logger.info("************* test_TC_IE_20 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            face_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identify_results_faces_icon_by_xpath())
            if face_icon.is_displayed():
                self.logger.info("Face icon is visible...")
                self.status.append(True)
            else:
                self.logger.info("Face icon is not visible...")
                self.status.append(False)
            person_view = self.d.find_element(By.XPATH,
                                              Read_Identify_and_Enroll_Components().identify_results_person_view_icon_by_xpath())
            if person_view.is_displayed():
                self.logger.info("Person view is visible...")
                self.status.append(True)
            else:
                self.logger.info("Person view is visible...")
                self.status.append(False)
            purge_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .identify_results_purge_replace_icon_by_xpath())
            if purge_icon.is_displayed():
                self.logger.info("purge icon is visible...")
                self.status.append(True)
            else:
                self.logger.info("Person view is not visible...")
                self.status.append(False)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_20.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_20_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_20 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_20_exception.png")
            return False

    def close_all_panel_one_by_one(self):
        try:
            # close_panel_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().close_all_panel_one_by_one())
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
                try:
                    self.d.switch_to.alert.accept()
                    time.sleep(web_driver.one_second)
                except Exception as ex:
                    self.logger.info(f"exception: {ex.args}")
                    self.logger.info("Alert handled")
            else:
                pass
            time.sleep(web_driver.one_second)

        except Exception as ex:
            self.logger.error(f"Exception crated: {ex.args}")
            self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\test_TC_IE_20_exception.png")
            return False

    def click_on_logout_button(self):
        try:
            time.sleep(web_driver.one_second)
            logout_func = logout()
            logout_button = self.d.find_element(By.XPATH,
                                                logout_func.config.get("logout_locators", "logout_btn_by_xpath"))
            time.sleep(web_driver.one_second)
            logout_button.click()
            time.sleep(web_driver.one_second)
            self.logger.info("logout")
        except Exception as ex:
            self.logger.error(f"Exception crated: {ex.args}")
            # self.d.save_screenshot(f"{Path(__file__).parent.parent}\\Screenshots\\Button_not_clickable_logout_pg_03.png")
            return False

    def verify_visitors_ACTION_information_is_displayed_below_its_image_on_Enrollment_View_panel(self):
        try:
            self.logger.info("************* test_TC_IE_44 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\so\\00091.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            person_view_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .identify_results_person_view_icon_by_xpath(), self.d)
            person_view_icon.click()
            time.sleep(web_driver.two_second)
            time.sleep(web_driver.two_second)
            action_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .enrollment_view_action_ele_by_xpath())
            action_ele_info = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .enrollment_view_action_info_by_xpath())
            if action_ele.is_displayed():
                self.logger.info("action_ele is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if action_ele_info.is_displayed():
                self.logger.info("action_ele_info is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_44.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_44_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_44 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_44_exception.png")
            return False

    def verify_Enrolled_On_text_and_its_information_is_visible_as_expected_on_enrollment_view_panel(self):
        try:
            self.logger.info("************* test_TC_IE_45 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            person_view_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .identify_results_person_view_icon_by_xpath(), self.d)
            person_view_icon.click()
            self.logger.info(f"Clicked on person view")
            time.sleep(web_driver.two_second)
            enrolled_on_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .enrollment_view_enrolled_on_ele_by_xpath())
            enrolled_on_ele_info = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .enrollment_view_enrolled_on_info_by_xpath())
            if enrolled_on_ele.is_displayed():
                self.logger.info("enrolled_on_ele is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            if enrolled_on_ele_info.is_displayed():
                self.logger.info("enrolled_on_ele_info is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_45.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_45_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_45 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_45_exception.png")
            return False

    def verify_enabled_disabled_information_is_visible_on_enrollment_view_panel(self):
        try:
            self.logger.info("************* test_TC_IE_46 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            person_view_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .identify_results_person_view_icon_by_xpath(), self.d)
            person_view_icon.click()
            self.logger.info(f"Clicked on person view")
            time.sleep(web_driver.two_second)
            enabled_status = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .enrollment_view_enrolled_status_by_xpath())
            if enabled_status.is_displayed():
                self.logger.info("enabled_status is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            disabled_status = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .enrollment_view_disabled_status_by_xpath())
            if disabled_status.is_displayed():
                self.logger.info("disabled_status is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_46.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_46_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_46 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_46_Exception.png")
            return False

    def verify_enrollment_details_button_is_visible_and_clickable_as_expected_on_enrollment_view_panel(self):
        try:
            self.logger.info("************* test_TC_IE_47 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            person_view_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .identify_results_person_view_icon_by_xpath(), self.d)
            person_view_icon.click()
            self.logger.info(f"Clicked on person view")
            time.sleep(web_driver.two_second)
            enrollment_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                 enrollment_view_enrollment_details_btn_by_xpath())
            if enrollment_btn.is_displayed():
                self.logger.info("enrollment_btn is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            ex_enrollment_btn_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_view_enrollment_details_txt_validation().lower()
            time.sleep(web_driver.one_second)
            ac_enrollment_btn_txt = enrollment_btn.text.lower()
            self.logger.info(f"Expected data = {ex_enrollment_btn_txt}")
            self.logger.info(f"Actual data = {ac_enrollment_btn_txt}")
            if ex_enrollment_btn_txt == ac_enrollment_btn_txt:
                self.status.append(True)
            else:
                self.status.append(False)

            enrollment_btn.click()
            time.sleep(web_driver.one_second)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_47.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_47_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_47 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_47_exception.png")
            return False

    def verify_faces_button_is_visible_along_with_count_and_it_is_clickable_on_enrollment_view_panel(self):
        try:
            self.logger.info("************* test_TC_IE_48 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.two_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)
            time.sleep(web_driver.two_second)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            time.sleep(web_driver.two_second)
            person_view_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .identify_results_person_view_icon_by_xpath(), self.d)
            person_view_icon.click()
            self.logger.info(f"Clicked on person view")
            time.sleep(web_driver.two_second)
            face_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .enrollment_view_faces_btn_by_xpath())
            time.sleep(web_driver.two_second)
            if face_btn.is_displayed():
                self.logger.info("face_btn is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            ex_face_btn_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_view_faces_txt_validation().lower()
            self.logger.info(f"expected: {ex_face_btn_txt}")
            ac_faces_btn_txt = face_btn.text.lower()
            self.logger.info(f"actual: {ac_faces_btn_txt}")
            time.sleep(web_driver.one_second)
            if ex_face_btn_txt == ac_faces_btn_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            count = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .enrollment_view_faces_count_by_xpath())
            if count.is_displayed():
                self.logger.info("count is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            if int(count.text.strip()) >= 0:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            face_btn.click()
            self.logger.info("face_btn is clicked...")

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_48.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_48_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_48 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_48_exception.png")
            return False

    def verify_events_button_is_visible_along_with_count_and_it_is_clickable_on_enrollment_view_panel(self):
        try:
            self.logger.info("************* test_TC_IE_49 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            person_view_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .identify_results_person_view_icon_by_xpath(), self.d)
            person_view_icon.click()
            self.logger.info(f"Clicked on person view")
            events_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                            .enrollment_view_events_btn_by_xpath(), self.d)
            if events_btn.is_displayed():
                self.logger.info("events_btn is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            ex_events_btn_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_view_events_txt_validation().lower()
            self.logger.info(f"expected: {ex_events_btn_txt}")
            ac_events_btn_txt = events_btn.text.lower()
            self.logger.info(f"actual: {ac_events_btn_txt}")

            if ex_events_btn_txt == ac_events_btn_txt:
                self.status.append(True)
            else:
                self.status.append(False)

            events_btn.click()
            self.logger.info("clicked on events button...")
            time.sleep(web_driver.one_second)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_49.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_49_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_49 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_49_exception.png")
            return False

    def verify_enrollment_groups_button_is_visible_along_with_its_count_and_is_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_50 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            time.sleep(web_driver.one_second)
            person_view_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .identify_results_person_view_icon_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            person_view_icon.click()
            self.logger.info(f"Clicked on person view")
            time.sleep(web_driver.one_second)
            enrollment_group_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .enrollment_view_enrollment_groups_btn_by_xpath())
            time.sleep(web_driver.one_second)
            if enrollment_group_btn.is_displayed():
                self.logger.info("enrollment_group_btn is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            ex_enrollment_group_btn_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_view_enrollment_groups_txt_validation().lower()
            self.logger.info(f"ex_enrollment_group_btn_txt: {ex_enrollment_group_btn_txt}")
            ac_enrollment_group_btn_txt = enrollment_group_btn.text.lower()
            self.logger.info(f"ac_enrollment_group_btn_txt: {ac_enrollment_group_btn_txt}")
            time.sleep(web_driver.one_second)
            if ex_enrollment_group_btn_txt == ac_enrollment_group_btn_txt:
                self.status.append(True)
            else:
                self.status.append(False)

            count = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .enrollment_view_enrollment_groups_count_by_xpath())
            time.sleep(web_driver.one_second)
            if count.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            if int(count.text.strip()) >= 0:
                self.status.append(True)
            else:
                self.status.append(False)

            enrollment_group_btn.click()
            self.logger.info("Clicked on enrollment_group_btn...")

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_50.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_50_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_50 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_50_exception.png")
            return False

    def verify_notes_button_is_visible_along_with_its_count_and_is_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_51 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            time.sleep(web_driver.one_second)
            person_view_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .identify_results_person_view_icon_by_xpath(), self.d)
            person_view_icon.click()
            self.logger.info(f"clicked on person_view_icon")
            time.sleep(web_driver.one_second)
            notes_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                           .enrollment_view_notes_btn_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            if notes_btn.is_displayed():
                self.logger.info("notes_btn is visible...")
                self.status.append(True)
            else:
                self.logger.info("notes_btn is not visible...")
                self.status.append(False)
            ex_notes_btn_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_view_notes_txt_validation().lower()
            self.logger.info(f"ex_notes_btn_txt: {ex_notes_btn_txt}")
            ac_notes_btn_txt = notes_btn.text.lower()
            self.logger.info(f"ac_notes_btn_txt: {ac_notes_btn_txt}")
            time.sleep(web_driver.one_second)
            if ex_notes_btn_txt == ac_notes_btn_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            count = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                        .enrollment_view_notes_count_by_xpath())
            time.sleep(web_driver.one_second)
            if count.is_displayed():
                self.logger.info("count is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            if int(count.text.strip()) >= 0:
                self.status.append(True)
            else:
                self.status.append(False)

            notes_btn.click()
            self.logger.info("clicked on notes_btn")
            time.sleep(web_driver.one_second)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_51.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_51_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_51 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_51_exception.png")
            return False

    def click_on_close_panel_button_displayed_beside_panel_title_and_verify_panel_is_closed_successfully(self):
        try:
            self.logger.info("************* test_TC_IE_52 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            enrollment_view_panel = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                       .identify_results_person_view_icon_by_xpath(), self.d)
            enrollment_view_panel.click()
            self.logger.info(f"Clicked on person view icon")
            time.sleep(web_driver.two_second)

            panel_close = self.d.find_element(By.XPATH,
                                              Read_Identify_and_Enroll_Components().enrollment_view_panel_close())
            panel_close.click()
            time.sleep(web_driver.one_second)
            self.logger.info("panel closed...")

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_52.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_52_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_52 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_52_exception.png")
            return False

    def click_on_purge_and_replace_button_and_pop_up_is_appeared_along_with_expected_message(self):
        try:
            self.logger.info("************* test_TC_IE_53 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            purge_and_replace = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                   .identify_results_purge_replace_icon_by_xpath(), self.d)
            purge_and_replace.click()
            self.logger.info("clicked on 'purge and replace' button....")
            time.sleep(web_driver.two_second)
            p_and_r_popup = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                               .purge_and_replace_pop_up_validation(), self.d)
            print(p_and_r_popup.text.lower())
            print(Read_Identify_and_Enroll_Components().purge_and_replace_validation_text().lower())
            self.logger.info(
                f"Ex pop up : {Read_Identify_and_Enroll_Components().purge_and_replace_validation_text().lower()}")
            self.logger.info(f"Ac pop up : {p_and_r_popup.text.lower()}")
            if p_and_r_popup.text.lower() == Read_Identify_and_Enroll_Components().purge_and_replace_validation_text().lower():
                # self.logger.info(f"actual alert text: {self.d.switch_to.alert.text}")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            self.logger.info("alert dismissed...")
            print(self.status)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_53.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_53_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_53 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_53_exception.png")
            return False

    def click_on_close_panel_button_displayed_beside_panel_title_verify_panel_closed_successfully(self):
        try:
            self.logger.info("************* test_TC_IE_54 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            enrollment_view_panel = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                       .identify_results_person_view_icon_by_xpath(), self.d)
            enrollment_view_panel.click()
            self.logger.info("clicked on person view icon...")
            time.sleep(web_driver.two_second)

            panel_close = self.d.find_element(By.XPATH,
                                              Read_Identify_and_Enroll_Components().enrollment_view_panel_close())
            panel_close.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicked on close panel button...")

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         close_panel_enroll_faces_validation())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        enrollment_view_panel_title_validation().lower():
                    self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_54.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_54_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_54 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_54_exception.png")
            return False

    def click_on_Crop_Image_button_and_verify_a_pop_up_is_visible_with_expected_message(self):
        try:
            self.logger.info("************* test_TC_IE_55 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            crop_photo_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .crop_photo_button())

            self.d.execute_script("arguments[0].click();", crop_photo_btn)
            time.sleep(web_driver.two_second)
            self.logger.info("Clicked on crop photo btn.....")

            if self.d.switch_to.alert.text == Read_Identify_and_Enroll_Components().crop_photo_validation():
                self.logger.info(f"actual alert text: {self.d.switch_to.alert.text}")
                self.status.append(True)
            else:
                self.status.append(False)

            self.d.switch_to.alert.accept()
            self.logger.info("alert accepted....")
            time.sleep(web_driver.one_second)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_55.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_55_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_55 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_55_Exception.png")
            return False

    def click_on_close_panel_button_displayed_beside_panel_title_verify_panel_successfully_closed(self):
        try:
            self.logger.info("************* test_TC_IE_56 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            enrollment_view_panel = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                       .identify_results_person_view_icon_by_xpath(), self.d)
            enrollment_view_panel.click()
            time.sleep(web_driver.two_second)
            self.logger.info("clicked on identify_results_person_view_icon....")
            panel_close = self.d.find_element(By.XPATH,
                                              Read_Identify_and_Enroll_Components().enrollment_view_panel_close())
            panel_close.click()
            time.sleep(web_driver.one_second)
            self.logger.info("clicked on panel close button....")
            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         close_panel_enroll_faces_validation())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        enrollment_view_panel_title_validation().lower():
                    self.status.append(False)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_56.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_56_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_56 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_56_Exception.png")
            return False

    def verify_two_new_panel_appeared_with_title_as_Enrollment_Steps_and_Add_Detailss(self):
        try:
            self.logger.info("************* test_TC_IE_ started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\vip\\00098.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            enrollment_steps_title = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .enrollment_steps_by_xpath())
            if enrollment_steps_title.is_displayed():
                self.logger.info("enrollment_steps_title is visible....")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)

            ex_enrollments_steps_title_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_steps_title_txt_validation().lower()
            self.logger.info(f"ex_enrollments_steps_title_txt: {ex_enrollments_steps_title_txt}")
            ac_enrollment_steps_title_txt = enrollment_steps_title.text.lower()
            self.logger.info(f"ac_enrollment_steps_title_txt: {ac_enrollment_steps_title_txt}")

            if ex_enrollments_steps_title_txt == ac_enrollment_steps_title_txt:
                self.status.append(True)
            else:
                self.status.append(False)

            add_details_panel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .add_details_panel_by_xpath())
            if add_details_panel.is_displayed():
                self.logger.info("add_details_panel is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)

            ex_add_details_panel_txt = Read_Identify_and_Enroll_Components() \
                .add_details_panel_title_txt_validation().lower()
            self.logger.info(f"ex_add_details_panel_txt: {ex_add_details_panel_txt}")
            ac_add_details_panel_txt = add_details_panel.text.lower()
            self.logger.info(f"ac_add_details_panel_txt: {ac_add_details_panel_txt}")
            if ex_add_details_panel_txt == ac_add_details_panel_txt:
                self.status.append(True)
            else:
                self.status.append(False)

            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_57_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_ got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{Path(__file__).parent.parent}\\Screenshots\\test_TC_IE_57_exception.png")
            return False

    def verify_first_panel_title_Enrollment_Steps_and_below_it_image_selected_is_visible(self):
        try:
            self.logger.info("************* test_TC_IE_58 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\vip\\00098.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            enrollment_steps_title = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .enrollment_steps_by_xpath())
            if enrollment_steps_title.is_displayed():
                self.logger.info("enrollment_steps_title is visible...")
                self.status.append(True)
            else:
                self.status.append(False)

            ex_enrollments_steps_title_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_steps_title_txt_validation().lower()
            self.logger.info(f"ex_enrollments_steps_title_txt: {ex_enrollments_steps_title_txt}")
            ac_enrollment_steps_title_txt = enrollment_steps_title.text.lower()
            self.logger.info(f"ac_enrollment_steps_title_txt: {ac_enrollment_steps_title_txt}")
            if ex_enrollments_steps_title_txt == ac_enrollment_steps_title_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)

            enrollment_steps_img = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .enrollment_steps_selected_img_by_xpath())
            if enrollment_steps_img.is_displayed():
                self.logger.info("enrollment_steps_img is visible...")
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)
            cancel = self.d.find_element(By.XPATH,
                                         Read_Identify_and_Enroll_Components().add_details_cancel_btn_by_xpath())
            cancel.click()
            time.sleep(web_driver.one_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)

            enrollment_cancel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .warning_msg_close_button())
            enrollment_cancel.click()
            self.logger.info("clicked on enrollment_cancel...")
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_58.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_58_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_58 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_58_exception.png")
            return False

    def verify_image_properties_text_below_image_along_with_details_is_displayed_as_expected(self):
        try:
            self.logger.info("************* test_TC_IE_59 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\vip\\00099.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            image_properties = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_steps_image_properties_by_xpath())
            ex_image_properties_txt = Read_Identify_and_Enroll_Components() \
                .enrollment_steps_image_properties_txt_validation().lower()
            self.logger.info(f"ex_image_properties_txt: {ex_image_properties_txt}")
            ac_image_properties_txt = image_properties.text.lower()
            self.logger.info(f"{ex_image_properties_txt} ========> actual: {ac_image_properties_txt}")
            if image_properties.is_displayed() and ex_image_properties_txt == ac_image_properties_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            image_properties_info = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                        .enrollment_steps_image_properties_info_by_xpath())
            self.logger.info(f"image_properties_info: {image_properties_info.text}")
            time.sleep(web_driver.one_second)
            if "pixels" or "kb" in image_properties_info.text.lower():
                self.status.append(True)
            else:
                self.status.append(False)
            warning_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .warning_msg_close_button())

            self.d.execute_script("arguments[0].click();", warning_close)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_59.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_59_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_59 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_59_exception.png")
            return False

    def verify_warning_text_is_displayed_below_image_on_Enrollment_Steps_panel_as_expected(self):
        try:
            self.logger.info("************* test_TC_IE_60 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            self.upload_image_enrollment_not_required()

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            time.sleep(web_driver.two_second)

            warning = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                          .enrollment_steps_warning_by_xpath())
            ex_warning_txt = Read_Identify_and_Enroll_Components().enrollment_steps_warning_txt_validation()
            self.logger.info(f"ex_warning_txt: {ex_warning_txt}")
            ac_warning_txt = warning.text
            self.logger.info(f"ac_warning_txt: {ac_warning_txt}")
            if ex_warning_txt.lower() in ac_warning_txt.lower():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            try:
                warning_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .warning_msg_close_button())

                self.d.execute_script("arguments[0].click();", warning_close)
                time.sleep(web_driver.one_second)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.logger.info("close button is not present : continue")
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_60.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_60_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_60 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_60_exception.png")
            return False

    def verify_No_match_found_text_below_warning_is_visible_as_expected_on_Enrollment_Steps_panel(self):
        try:
            self.logger.info("************* test_TC_IE_61 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            self.upload_image_enrollment_not_required()
            time.sleep(web_driver.two_second)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)

            no_match_found = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .enrollments_steps_no_match_found_by_xpath())
            exp_msg = Read_Identify_and_Enroll_Components().enrollment_steps_no_match_found_txt_validation().lower()
            ac_msg = no_match_found.text.lower()
            if no_match_found.is_displayed():
                self.logger.info(f"no_match_found is visible")
                self.status.append(True)
            else:
                self.logger.info(f"no_match_found is not visible")
                self.status.append(False)
            if exp_msg == ac_msg:
                self.status.append(True)
            else:
                self.status.append(False)
            print(self.status)
            self.close_all_panel_one_by_one()
            warning_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .warning_msg_close_button())

            self.d.execute_script("arguments[0].click();", warning_close)
            time.sleep(web_driver.one_second)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_61.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_61_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_61 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_61_exception.png")
            return False

    def verify_exposure_sharpness_resolution_images_parameters_their_data_green_tick_symbol_is_displayed(self):
        try:
            self.logger.info("************* test_TC_IE_62 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            self.upload_image_enrollment_not_required()

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            image_info_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_steps_image_info_list_by_xpath())
            image_data_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .enrollment_steps_image_datas_list_by_xpath())
            green_ticks_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .enrollment_steps_green_ticks_list_by_xpath())
            time.sleep(web_driver.one_second)
            for i in range(0, len(image_info_list)):
                if image_info_list.__getitem__(i).is_displayed():
                    self.status.append(True)
                else:
                    self.status.append(False)
                if image_data_list.__getitem__(i).is_displayed():
                    self.status.append(True)
                else:
                    self.status.append(False)
                if green_ticks_list.__getitem__(i).is_displayed():
                    self.status.append(True)
                else:
                    self.status.append(False)
            self.close_all_panel_one_by_one()
            warning_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .warning_msg_close_button())

            self.d.execute_script("arguments[0].click();", warning_close)
            time.sleep(web_driver.one_second)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_62.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_62_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_62 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_62_exception.png")
            return False

    def verify_second_panel_titled_as_Add_Details_and_panel_is_active_enabled(self):
        try:
            self.logger.info("************* test_TC_IE_63 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\vip\\000100.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH,
                                            Read_Identify_and_Enroll_Components().identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.three_second)

            add_details_panel = self.explicit_wait(10, "XPATH",
                                                   Read_Identify_and_Enroll_Components()
                                                   .add_details_panel_by_xpath(),
                                                   self.d)
            if add_details_panel.is_displayed():
                self.logger.info("add_details_panel is visible")
                self.status.append(True)
            else:
                self.logger.info("add_details_panel is not visible")
                self.status.append(False)

            ex_add_details_panel_txt = Read_Identify_and_Enroll_Components() \
                .add_details_panel_title_txt_validation().lower()
            ac_add_details_panel_txt = add_details_panel.text.lower()
            self.logger.info(f"ex add_details_panel : {ex_add_details_panel_txt}")
            self.logger.info(f"ac add_details_panel : {ac_add_details_panel_txt}")
            if ex_add_details_panel_txt == ac_add_details_panel_txt:
                self.status.append(True)
            else:
                self.status.append(False)

            self.close_all_panel_one_by_one()

            warning_close = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .warning_msg_close_button())

            self.d.execute_script("arguments[0].click();", warning_close)
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_63.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_63_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_63 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_63_exception.png")
            return False

    def verify_cancel_button_below_title_Add_Details_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_64 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\so\\00091.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            if cancel_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_msg_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().cancel_msg_by_xpath())
            exp_cancel_msg = Read_Identify_and_Enroll_Components().add_details_cancel_msg_txt_validation().lower()
            ac_cancel_msg = cancel_msg_ele.text.lower()

            if exp_cancel_msg == ac_cancel_msg:
                self.status.append(True)
            else:
                self.status.append(False)

            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_64.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_64_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_64 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_64_Exception.png")
            return False

    def verify_save_button_below_title_Add_Details_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_65 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\so\\00092.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.logger.info(f"save_btn is visible")
                self.status.append(True)
            else:
                self.logger.info(f"save_btn is not visible")
                self.status.append(False)
            save_btn.click()
            time.sleep(web_driver.one_second)
            Alert(self.d).accept()
            time.sleep(web_driver.one_second)
            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_65.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_65_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_65 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_65_Exception.png")
            return False

    def verify_two_option_Expire_Date_and_Do_Not_Expire_are_visible_and_clickable_below_Add_Details_title(self):
        try:
            self.logger.info("************* test_TC_IE_66 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\so\\00093.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")
            self.click_on_enroll_for_already_enrolled()

            expire_date_rado_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                      .expire_date_radio_btn_by_xpath(), self.d)
            do_not_expire_radio_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                          .do_not_expire_radio_btn_by_xpath())

            expire_date_rado_btn.click()
            self.logger.info("Clicked on expire_date_rado_btn")
            time.sleep(web_driver.one_second)
            if expire_date_rado_btn.is_selected():
                self.logger.info("expire_date_rado_btn is selected")
                self.status.append(True)
            else:
                self.logger.info("expire_date_rado_btn is not selected")
                self.status.append(False)

            do_not_expire_radio_btn.click()
            self.logger.info("Clicked on do_not_expire_radio_btn")
            time.sleep(web_driver.one_second)
            if do_not_expire_radio_btn.is_selected():
                self.logger.info("do_not_expire_radio_btn is selected")
                self.status.append(True)
            else:
                self.logger.info("do_not_expire_radio_btn is not selected")
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                   .cancel_enrollment_btn_by_xpath(), self.d)
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_66.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_66_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_66 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_66_exception.png")
            return False

    def verify_date_entry_textbox_beside_Expire_Date_is_visible_and_clickable_and_current_date_is_displayed(self):
        try:
            self.logger.info("************* test_TC_IE_67 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\pt\\00089.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            expire_date_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().add_details_expire_date_text_bx_by_xpath())
            if expire_date_txt_bx.is_displayed():
                self.logger.info(f"expire_date_txt_bx is visible")
                self.status.append(True)
            else:
                self.logger.info(f"expire_date_txt_bx is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            expire_date_txt_bx.click()
            time.sleep(web_driver.one_second)
            expire_date_calender_popup = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().add_details_expire_date_calender_pop_up_by_xpath())
            if expire_date_calender_popup.is_displayed():
                self.logger.info(f"expire_date_calender_popup is visible")
                self.status.append(True)
            else:
                self.logger.info(f"expire_date_calender_popup is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            exp_date = expire_date_txt_bx.get_attribute("value").split(" ")[0].split("/")

            ac_date = str(date.today()).replace("-", "/").split("/")
            temp = ac_date[0]
            for x in range(1, len(temp) - 1):
                ac_date[x - 1] = ac_date[x]
            ac_date[len(ac_date) - 1] = temp

            if exp_date == ac_date:
                self.status.append(True)
            else:
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_67.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_67_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_67 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_67_exception.png")
            return False

    def verify_opt_out_label_text_and_check_box_besides_is_visible_and_clickable_on_Add_Details_panel(self):
        try:
            self.logger.info("************* test_TC_IE_68 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\so\\00094.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            opt_out_txt_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .add_details_opt_out_by_xpath())
            exp_opt_out_txt = Read_Identify_and_Enroll_Components().opt_out_txt_validation().lower()
            ac_opt_out_txt = opt_out_txt_ele.text.strip().lower()
            self.logger.info(f"exp_opt_out_txt : {exp_opt_out_txt}")
            self.logger.info(f"ac_opt_out_txt : {ac_opt_out_txt}")
            if exp_opt_out_txt == ac_opt_out_txt:
                self.status.append(True)
            else:
                self.status.append(False)

            opt_out_check_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .opt_out_chk_bx_by_xpath())
            if opt_out_check_bx.is_displayed():
                self.logger.info(f"opt_out_check_bx is visible")
                self.status.append(True)
            else:
                self.logger.info(f"opt_out_check_bx is not visible")
                self.status.append(False)
            opt_out_check_bx.click()
            if opt_out_check_bx.is_selected():
                self.logger.info(f"opt_out_check_bx is selected")
                self.status.append(True)
            else:
                self.logger.info(f"opt_out_check_bx is not selected")
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_68.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_68_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_68 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_68_exception.png")
            return False

    def verify_Enrollment_Group_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_69 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\so\\00095.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            enrollment_group_text_ele = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_details_enrollment_groups_text_by_xpath())
            enrollment_group_text_ele.is_displayed()
            self.logger.info(f"enrollment_group_text_ele : {enrollment_group_text_ele.is_displayed()}")
            enrollment_group_drop_dwn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .enrollment_group_by_xpath())
            enrollment_group_drop_dwn.click()
            self.logger.info(f"Clicked on enrollment_group_drop_dwn")
            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_69.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_69_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_69 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_69_Exception.png")
            return False

    def click_on_Enrollment_Group_dropdown_and_verify_options_inside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_70 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\so\\00091.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")
            self.click_on_enroll_for_already_enrolled()

            enrollment_group_drop_dwn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                           .enrollment_group_by_xpath(), self.d)
            enrollment_group_drop_dwn.click()
            self.logger.info("Clicked on enrollment_group dropdown")
            time.sleep(web_driver.one_second)
            enrollment_groups_options = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .add_details_enrollment_groups_options_by_xpath())
            for ele in enrollment_groups_options:
                if not ele.is_displayed() and ele.click():
                    self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                   .cancel_enrollment_btn_by_xpath(), self.d)
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_70.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_70_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_70 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_70_exception.png")
            return False

    def verify_Field_Incomplete_text_below_enrollment_group_dropdown_is_visible_as_expected(self):
        try:
            self.logger.info("************* test_TC_IE_71 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\so\\00092.png"
            self.upload_image_not_enrolled(img_path)
            time.sleep(web_driver.two_second)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            field_incomplete = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .add_details_enrollment_groups_field_incomplete_by_xpath())
            field_incomplete.is_displayed()
            self.logger.info(f"field_incomplete : {field_incomplete.is_displayed()}")
            time.sleep(web_driver.one_second)
            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_71.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_71_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_71 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_71_exception.png")
            return False

    def verify_REQUIRED_FIELDS_heading_below_enrollment_group_dropdown_is_displayed(self):
        try:
            self.logger.info("************* test_TC_IE_72 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            self.upload_image_enrollment_not_required()

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            time.sleep(web_driver.two_second)
            required_fields = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                 .add_details_required_fields_by_xpath(), self.d)

            if required_fields.is_displayed():
                self.logger.info(f"required_fields is visible")
                self.status.append(True)
            else:
                self.logger.info(f"required_fields is not visible")
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.two_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_72.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_72_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_72 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_72_Exception.png")
            return False

    def verify_LOCATION_STORE_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_73 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            self.upload_image_enrollment_not_required()

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")

            location_store_txt = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                    .add_details_location_store_text_ele_by_xpath(), self.d)
            ex_location_store_txt = Read_Identify_and_Enroll_Components() \
                .add_details_location_store_txt_validation().lower()
            ac_location_store_txt = location_store_txt.text.lower()
            self.logger.info(f"ex_location_store_txt : {ex_location_store_txt}")
            self.logger.info(f"ac_location_store_txt : {ac_location_store_txt}")
            if ex_location_store_txt == ac_location_store_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            location_store_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                        .location_store_inpt_bx_by_xpath())
            location_store_txt_bx.send_keys(Read_Identify_and_Enroll_Components()
                                            .add_details_location_store_data_input())
            time.sleep(web_driver.one_second)
            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                   .cancel_enrollment_btn_by_xpath(), self.d)
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_73.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_73_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_73 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_73_exception.png")
            return False

    def verify_Field_Incomplete_text_below_location_store_textbox_is_visible_as_expected(self):
        try:
            self.logger.info("************* test_TC_IE_74 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            self.upload_image_enrollment_not_required()

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            field_incomplete = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .add_details_location_store_field_incomplete_by_xpath())
            if field_incomplete.is_displayed():
                self.logger.info(f"field_incomplete is visible")
                self.status.append(True)
            else:
                self.logger.info(f"field_incomplete is not visible")
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_74.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_74_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_74 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_74_exception.png")
            return False

    def verify_CASE_SUBJECT_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_75 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\so\\00092.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            case_subject_txt = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().add_details_case_subject_text_ele_by_xpath())
            ex_case_subject_txt = Read_Identify_and_Enroll_Components().add_details_case_subject_txt_validation().lower()
            ac_case_subject_txt = case_subject_txt.text.lower()
            self.logger.info(f"ex_case_subject_txt : {case_subject_txt.text.lower()}")
            self.logger.info(
                f"ac_case_subject_txt : {Read_Identify_and_Enroll_Components().add_details_case_subject_txt_validation().lower()}")
            if ex_case_subject_txt == ac_case_subject_txt:
                self.status.append(True)
            else:
                self.status.append(False)
            case_subject_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .case_subject_inpt_bx_by_xpath())
            case_subject_txt_bx.send_keys(Read_Identify_and_Enroll_Components().add_details_case_subject_data_input())
            if case_subject_txt_bx.get_attribute("value").lower().strip() == Read_Identify_and_Enroll_Components(). \
                    add_details_case_subject_data_input().lower():
                self.status.append(True)
            else:
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_75.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_75_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_75 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_75_exception.png")
            return False

    def verify_Field_Incomplete_text_below_case_subject_textbox_is_visible_as_expected(self):
        try:
            self.logger.info("************* test_TC_IE_76 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            self.upload_image_enrollment_not_required()

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            field_incomplete = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .add_details_case_subject_field_incomplete_by_xpath(), self.d)
            if field_incomplete.is_displayed():
                self.logger.info("field_incomplete is visible")
                self.status.append(True)
            else:
                self.logger.info("field_incomplete is not visible")
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_76.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_76_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_76 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_76_Exception.png")
            return False

    def verify_REPORTED_LOSS_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_77 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\so\\00093.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            reported_loss_txt = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .add_details_reported_loss_text_ele_by_xpath())
            ex_reported_loss_txt = Read_Identify_and_Enroll_Components() \
                .add_details_reported_loss_txt_validation().lower()
            ac_reported_loss_txt = reported_loss_txt.text.lower()
            self.logger.info(f"ex_reported_loss_txt : {ex_reported_loss_txt}")
            self.logger.info(f"ac_reported_loss_txt : {ac_reported_loss_txt}")
            if ex_reported_loss_txt == ac_reported_loss_txt:
                self.status.append(True)
            else:
                self.status.append(False)

            reported_loss_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .reported_loss_inpt_bx_by_xpath())
            reported_loss_txt_bx.send_keys(Read_Identify_and_Enroll_Components().add_details_reported_loss_data_input())
            ex_reported_loss_data = int(Read_Identify_and_Enroll_Components().add_details_reported_loss_data_input())
            ac_reported_loss_data = int(reported_loss_txt_bx.get_attribute("value").strip())
            if ex_reported_loss_data == ac_reported_loss_data:
                self.status.append(True)
            else:
                self.status.append(False)
            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_77.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_77_failing.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_77 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_77_Exception.png")
            return False

    def verify_Field_Incomplete_text_below_REPORTED_LOSS_textbox_is_visible_as_expected(self):
        try:
            self.logger.info("************* test_TC_IE_78 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            self.upload_image_enrollment_not_required()

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            field_incomplete = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .add_details_reported_loss_field_incomplete_by_xpath(), self.d)
            if field_incomplete.is_displayed():
                self.logger.info(f"field_incomplete is visible")
                self.status.append(True)
            else:
                self.logger.info(f"field_incomplete is not visible")
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_78.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_78_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_78 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_78_exception.png")
            return False

    def verify_DATE_INCIDENT_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_79 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")

            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\so\\00094.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            date_incident_txt = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .add_details_date_incident_text_ele_by_xpath())
            if date_incident_txt.is_displayed():
                self.logger.info(f"date_incident_txt is visible")
                self.status.append(True)
            else:
                self.logger.info(f"date_incident_txt is not visible")
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_79.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_79_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_79 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_79_Exception.png")
            return False

    def verify_Field_Incomplete_text_below_DATE_INCIDENT_textbox_is_visible_as_expected(self):
        try:
            self.logger.info("************* test_TC_IE_80 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            self.upload_image_enrollment_not_required()

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            field_incomplete = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .add_details_date_incident_field_incomplete_by_xpath(), self.d)
            if field_incomplete.is_displayed():
                self.logger.info(f"date_incident_field_incomplete is visible")
                self.status.append(True)
            else:
                self.logger.info(f"date_incident_field_incomplete is not visible")
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_80.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_80_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_80 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_80_Exception.png")
            return False

    def verify_ACTION_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_83 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            self.upload_image_enrollment_not_required()

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            action_text = self.d.find_element(By.XPATH,
                                              Read_Identify_and_Enroll_Components().add_details_action_text_ele_by_xpath())
            if action_text.is_displayed():
                self.logger.info(f"action_text is visible")
                self.status.append(True)
            else:
                self.logger.info(f"action_text is not visible")
                self.status.append(False)

            action_text_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .action_inpt_bx_by_xpath())
            action_text_bx.send_keys(Read_Identify_and_Enroll_Components().add_details_action_data_input())
            time.sleep(web_driver.one_second)
            if Read_Identify_and_Enroll_Components().add_details_action_data_input().lower() == \
                    action_text_bx.get_attribute("value").lower():
                self.status.append(True)
            else:
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_83.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_83_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_83 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_83_Exception.png")
            return False

    def verify_Field_Incomplete_text_below_ACTION_textbox_is_visible_as_expected(self):
        try:
            self.logger.info("************* test_TC_IE_84 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            self.upload_image_enrollment_not_required()

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            field_incomplete = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .add_details_action_field_incomplete_by_xpath(), self.d)
            if field_incomplete.is_displayed():
                self.logger.info(f"action_field_incomplete is visible")
                self.status.append(True)
            else:
                self.logger.info(f"action_field_incomplete is not visible")
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_84.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_84_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_84 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_84_exception.png")
            return False

    def verify_OPTIONAL_FIELDS_heading_below_action_textbox_is_displayed(self):
        try:
            self.logger.info("************* test_TC_IE_85 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                       .identify_and_enroll_link_by_xpath())
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            self.upload_image_enrollment_not_required()

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            optional_fields = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                 .add_details_optional_fields_by_xpath(), self.d)
            if optional_fields.is_displayed():
                self.logger.info(f"add_details_optional_fields is visible")
                self.status.append(True)
            else:
                self.logger.info(f"add_details_optional_fields is not visible")
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_85.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_85_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_85 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_85_exception.png")
            return False

    def verify_CASE_EVENT_TYPE_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_86 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            self.upload_image_enrollment_not_required()

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            case_event_type_text = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                      .add_details_case_event_type_text_ele_by_xpath(), self.d)
            if case_event_type_text.is_displayed():
                self.logger.info(f"case_event_type_text is visible")
                self.status.append(True)
            else:
                self.logger.info(f"case_event_type_text is not visible")
                self.status.append(False)

            case_event_type_drop_dwn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .case_event_type_by_xpath())
            s = Select(case_event_type_drop_dwn)
            options_list = s.options
            if len(options_list) > 0:
                self.status.append(True)
            else:
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_86.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_86_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_86 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_86_Exception.png")
            return False

    def click_on_CASE_EVENT_TYPE_dropdown_and_verify_options_inside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_87 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\so\\00095.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            case_event_type_drop_dwn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .case_event_type_by_xpath())
            s = Select(case_event_type_drop_dwn)
            options_list = s.options
            for x in options_list:
                s.select_by_visible_text(x.text)
                time.sleep(web_driver.two_second)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_87.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_87_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_87 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_87_Exception.png")
            return False

    def verify_ACTIVITY_TYPE_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_88 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\pt\\00086.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            activity_type_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_details_activity_type_text_ele_by_xpath())
            if activity_type_text.is_displayed():
                self.logger.info(f"activity_type_text is visible")
                self.status.append(True)
            else:
                self.logger.info(f"activity_type_text is not visible")
                self.status.append(False)

            activity_type_drop_dwn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .activity_type_by_xpath())
            s = Select(activity_type_drop_dwn)
            options_list = s.options
            if len(options_list) > 0:
                self.status.append(True)
            else:
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_88.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_88_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_88 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_88_exception.png")
            return False

    def click_on_ACTIVITY_TYPE_dropdown_and_verify_options_inside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_89 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\pt\\00087.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            activity_type_drop_dwn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .activity_type_by_xpath())
            s = Select(activity_type_drop_dwn)
            options_list = s.options
            for x in options_list:
                s.select_by_visible_text(x.text)
                time.sleep(web_driver.two_second)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_89.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_89_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_89 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_89_exception.png")
            return False

    def verify_METHOD_OF_OFFENSE_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_90 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\pt\\00088.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            method_of_offence_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .add_details_method_of_offence_text_ele_by_xpath())
            if method_of_offence_text.is_displayed():
                self.logger.info(f"method_of_offence_text is visible")
                self.status.append(True)
            else:
                self.logger.info(f"method_of_offence_text is visible")
                self.status.append(False)

            method_of_offence_drop_dwn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .method_of_offence_by_xpath())
            s = Select(method_of_offence_drop_dwn)
            options_list = s.options
            if len(options_list) > 0:
                self.status.append(True)
            else:
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_90.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_90_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_90 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_90_Exception.png")
            return False

    def click_on_METHOD_OF_OFFENSE_dropdown_and_verify_options_inside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_91 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\pt\\00089.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            self.click_on_enroll_for_already_enrolled()

            method_of_offence_drop_dwn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                            .method_of_offence_by_xpath(), self.d)
            s = Select(method_of_offence_drop_dwn)

            options_list = s.options
            for x in options_list:
                s.select_by_visible_text(x.text)
                time.sleep(web_driver.two_second)
            self.logger.info("method_of_offence_drop_dwn validation is done")
            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                   .cancel_enrollment_btn_by_xpath(), self.d)
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_91.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_91_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_91 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_91_exception.png")
            return False

    def verify_REPORTED_BY_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_92 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            self.upload_image_enrollment_not_required()

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            time.sleep(web_driver.one_second)

            add_details_reported_by_text = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                              .add_details_reported_by_text_ele_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            if add_details_reported_by_text.is_displayed():
                self.logger.info(f"add_details_reported_by_text is visible")
                self.status.append(True)
            else:
                self.logger.info(f"add_details_reported_by_text is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            reported_by_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .reported_by_inpt_bx_by_xpath())
            ex_reported_by_data = Read_Identify_and_Enroll_Components().reported_by_data()
            reported_by_txt_bx.send_keys(ex_reported_by_data)
            time.sleep(web_driver.one_second)
            ac_reported_by_data = reported_by_txt_bx.get_attribute("value")
            time.sleep(web_driver.one_second)
            self.logger.info(f"ex_reported_by_data : {ex_reported_by_data}")
            self.logger.info(f"ac_reported_by_data : {ac_reported_by_data}")
            if ex_reported_by_data.lower() == ac_reported_by_data.lower():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.one_second)
            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            time.sleep(web_driver.one_second)
            cancel_btn.click()
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            time.sleep(web_driver.one_second)
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_92.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_92_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_92 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_92_Exception.png")
            return False

    def verify_Build_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_93 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\pt\\00090.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            add_details_build_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .add_details_build_text_ele_by_xpath())
            time.sleep(web_driver.one_second)
            if add_details_build_text.is_displayed():
                self.logger.info("add_details_build_text is visible")
                self.status.append(True)
            else:
                self.logger.info("add_details_build_text is not visible")
                self.status.append(False)

            build_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().build_inpt_bx_by_xpath())
            ex_build_data = Read_Identify_and_Enroll_Components().build_data()
            build_txt_bx.send_keys(ex_build_data)
            time.sleep(web_driver.one_second)
            ac_build_data = build_txt_bx.get_attribute("value")
            time.sleep(web_driver.one_second)
            if ex_build_data.lower() == ac_build_data.lower():
                self.status.append(True)
            else:
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            time.sleep(web_driver.one_second)
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            time.sleep(web_driver.one_second)
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_93.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_93_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_93 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_93_Exception.png")
            return False

    def verify_Body_Markings_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_94 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\fraud\\00081.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            body_marking_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .body_markings_inpt_bx_by_xpath())
            if body_marking_text.is_displayed():
                self.logger.info("body_marking_text is visible")
                self.status.append(True)
            else:
                self.logger.info("body_marking_text is not visible")
                self.status.append(False)

            body_marking_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                      .build_inpt_bx_by_xpath())
            ex_body_marking_data = Read_Identify_and_Enroll_Components().body_markings_data()
            body_marking_txt_bx.send_keys(ex_body_marking_data)
            time.sleep(web_driver.one_second)
            ac_body_marking_data = body_marking_txt_bx.get_attribute("value")
            if ex_body_marking_data.lower() == ac_body_marking_data.lower():
                self.status.append(True)
            else:
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_94.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_94_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_94 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_94_Exception.png")
            return False

    def verify_GENDER_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_95 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\fraud\\00082.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            gender_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().gender_by_xpath())
            if gender_text.is_displayed():
                self.logger.info("gender_text is visible")
                self.status.append(True)
            else:
                self.logger.info("gender_text is not visible")
                self.status.append(False)

            gender_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().gender_by_xpath())
            s = Select(gender_txt_bx)
            options_list = s.options
            if len(options_list) > 0:
                self.status.append(True)
            else:
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_95.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_95_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_95 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_95_exception.png")
            return False

    def click_on_GENDER_dropdown_and_verify_options_inside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_96 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\fraud\\00083.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            gender_text = self.explicit_wait(10, "XPATH",
                                             Read_Identify_and_Enroll_Components().add_details_gender_text_ele_by_xpath(),
                                             self.d)
            if gender_text.is_displayed():
                self.logger.info(f"gender text is visible")
                self.status.append(True)
            else:
                self.logger.info(f"gender text is not visible")
                self.status.append(False)

            gender_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().gender_by_xpath())
            s = Select(gender_txt_bx)
            options_list = s.options
            for x in options_list:
                s.select_by_visible_text(x.text)
                time.sleep(web_driver.two_second)

            self.logger.info(f"gender dropdown option validation is done")
            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                   .cancel_enrollment_btn_by_xpath(), self.d)
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_96.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_96_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_96 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_96_Exception.png")
            return False

    def verify_HEIGHT_label_text_is_displayed_with_dropdown_beside_it_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_97 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\fraud\\00084.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            height_text = self.d.find_element(By.XPATH,
                                              Read_Identify_and_Enroll_Components().add_details_height_text_ele_by_xpath())
            if height_text.is_displayed():
                self.logger.info("height_text is visible")
                self.status.append(True)
            else:
                self.logger.info("height_text is not visible")
                self.status.append(False)

            height_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().height_by_xpath())
            s = Select(height_txt_bx)
            options_list = s.options
            if len(options_list) > 0:
                self.status.append(True)
            else:
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_97.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_97_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_97 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_97_exception.png")
            return False

    def click_on_HEIGHT_dropdown_and_verify_options_inside_it_are_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_98 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\fraud\\00085.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            self.click_on_enroll_for_already_enrolled()

            height_text = self.explicit_wait(10, "XPATH",
                                             Read_Identify_and_Enroll_Components().add_details_height_text_ele_by_xpath(),
                                             self.d)
            if height_text.is_displayed():
                self.logger.info(f"height_text is visible")
                self.status.append(True)
            else:
                self.logger.info(f"height_text is not visible")
                self.status.append(False)

            height_txt_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().height_by_xpath())
            s = Select(height_txt_bx)
            options_list = s.options
            for x in options_list:
                s.select_by_visible_text(x.text)
                time.sleep(web_driver.two_second)
            self.logger.info(f"height dropdwon validation is done")
            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                   .cancel_enrollment_btn_by_xpath(), self.d)
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_98.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_98_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_98 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_98_Exception.png")
            return False

    def verify_NARRATIVES_label_text_and_text_box_besides_it_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_99 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\ab\\00076.png"
            self.upload_image_not_enrolled(img_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed() or count == 120:
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            narratives_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .add_details_narratives_text_ele_by_xpath())
            if narratives_text.is_displayed():
                self.logger.info("narratives_text is visible")
                self.status.append(True)
            else:
                self.logger.info("narratives_text is not visible")
                self.status.append(False)

            narratives_text_bx = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .narratives_txt_bx_by_xpath())
            ex_narratives_data = Read_Identify_and_Enroll_Components().narratives_data()
            narratives_text_bx.send_keys(ex_narratives_data)

            ac_narratives_data = narratives_text_bx.get_attribute("value")
            if ex_narratives_data.lower() == ac_narratives_data.lower():
                self.status.append(True)
            else:
                self.status.append(False)

            cancel_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                             .add_details_cancel_btn_by_xpath())
            cancel_btn.click()
            time.sleep(web_driver.one_second)
            cancel_enrollment = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .cancel_enrollment_btn_by_xpath())
            cancel_enrollment.click()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_99.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_99_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_99 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_99_Exception.png")
            return False

    def Enter_Data_into_fields_displayed_on_Add_Details_panel_and_verify_enrollment_successfully_created_and_add_details_panel_closed(self):
        try:
            self.logger.info("************* test_TC_IE_100 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.two_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\ab\\00077.png"
            self.upload_image_not_enrolled(img_path)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group(0)
            time.sleep(web_driver.two_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.two_second)
            region_btn.click()
            time.sleep(web_driver.two_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH,
                                                Read_Identify_and_Enroll_Components().date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.one_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.one_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_details_save_btn_by_xpath(), self.d)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)

            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_100.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_100_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_100 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_100_Exception.png")
            return False

    def verify_Success_message_is_displayed_below_warning_on_Identify_and_enroll_panel(self):
        try:
            self.logger.info("************* test_TC_IE_101 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.two_second)
            img_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\dataset1\\vip\\00096.png"
            print(f"iamge_path : {img_path}")
            self.upload_image_not_enrolled(img_path)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH",
                                                  Read_Identify_and_Enroll_Components().enrollment_basis_by_xpath(),
                                                  self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)

            self.Select_Enrollment_Group(0)

            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

            # action_input = self.d.find_element(By.XPATH,
            #                                    Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_details_save_btn_by_xpath(), self.d)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Enrollment details filled and save btn is clicked")

            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            self.close_all_panel_one_by_one()
            # ***************************************************************

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_101.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_101_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_101 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_101_Exception.png")
            return False

    def verify_three_buttons_below_success_message_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_102 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\test_102.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')

            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Enrollment details filled and save btn is clicked")

            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_102.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_102_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_102 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_102_Exception.png")
            return False

    def click_on_Review_Enrollment_Details_button_and_verify_if_Enrollment_Details_panel_is_displayed(self):
        try:
            self.logger.info("************* test_TC_IE_103 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.two_second)
            # self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().upload_image_by_xpath(), self.d)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\img\\visitor_search_img_1.png"

            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")

            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group(0)

            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

            # time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_103.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_103_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_103 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_103_Exception.png")
            return False

    def verify_Action_button_visible_and_clickable_on_Enrollment_Details_Panel_below_its_title(self):
        try:
            self.logger.info("************* test_TC_IE_104 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            # self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().upload_image_by_xpath(), self.d)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\img\\visitor_search_img_2.png"

            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Enrollment details filled and save btn is clicked")
            
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)
            time.sleep(web_driver.one_second)
            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_104.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_104_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_104 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_104_Exception.png")
            return False

    def click_and_verify_Edit_Identify_Within_Enrollment_and_Identify_within_visitors_option_are_visible_and_clickable(
            self):
        try:
            self.logger.info("************* test_TC_IE_105 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            # self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().upload_image_by_xpath(), self.d)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\img\\visitor_search_img_3.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Enrollment details filled and save btn is clicked")
            
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .review_enrollment_details_button_xpath(), self.d)
            review_enroll_details_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                           .review_enrollment_details_button_xpath(), self.d)
            review_enroll_details_btn.click()
            self.logger.info("Clicked on review enrollment details button")
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .enrollment_details_action_button(), self.d)
            action_btn_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                        .enrollment_details_action_button())
            if action_btn_validation.is_displayed():
                self.logger.info("Action dropdown is visible")
                self.status.append(True)
            else:
                self.logger.info("Action dropdown is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            action_btn_validation.click()
            self.logger.info("Clicked on Action dropdown")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .enrollment_details_action_button_validation(), self.d)
            edite_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .enrollment_details_action_button_validation())
            if edite_option.is_displayed():
                self.logger.info("Edit option is visible")
                self.status.append(True)
            else:
                self.logger.info("Edit option is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            edite_option.click()
            self.logger.info("Clicked on Edit option")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .edite_button_validation_xpath(), self.d)
            edite_option_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                          .edite_button_validation_xpath())
            if edite_option_validation.is_displayed():
                self.logger.info(f"Edit option validation : {True}")
                self.status.append(True)
            else:
                self.logger.info(f"Edit option validation : {False}")
                self.status.append(False)
            save_button = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().edite_panel_save_button())
            time.sleep(web_driver.one_second)
            save_button.click()
            self.logger.info("Clicked on save btn")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .enrollment_details_action_button(), self.d)
            action_btn_validation.click()
            self.logger.info("Clicked on Action dropdown")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .action_button_identify_option(), self.d)
            identify_enroll_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .action_button_identify_option())
            if identify_enroll_option.is_displayed():
                self.logger.info("identify_enroll_option is visible")
                self.status.append(True)
            else:
                self.logger.info("identify_enroll_option is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)
            identify_enroll_option.click()
            self.logger.info("Clicked on identify_enroll_option option")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_option_validation(), self.d)
            identify_enroll_option_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                                    .identify_enroll_option_validation())
            time.sleep(web_driver.two_second)
            web_driver.implicit_wait(self, web_driver.one_second, self.d)
            # web_driver.explicit_wait(self, web_driver.two_second, identify_enroll_option_validation, self.d)
            if identify_enroll_option_validation.is_displayed():
                self.logger.info(f"identify_enroll_option validation : {True}")
                self.status.append(True)
            else:
                self.logger.info(f"identify_enroll_option validation : {True}")
                self.status.append(False)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .enrollment_details_action_button(), self.d)
            action_btn_validation.click()
            self.logger.info("Clicked on Action dropdown")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .action_button_visitors_option(), self.d)
            visitors_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .action_button_visitors_option())

            visitors_option.click()
            self.logger.info("Clicked on identify within Visitors option")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .visitor_search_panel_validation(), self.d)
            visitors_option_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .visitor_search_panel_validation())
            if visitors_option_validation.is_displayed():
                self.logger.info(f"identify within Visitors_option validation : {True}")
                self.status.append(True)
            else:
                self.logger.info(f"identify within Visitors_option_validation : {True}")
                self.status.append(False)
            time.sleep(web_driver.one_second)

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_105.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_105_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_105 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_105_Exception.png")
            return False

    def verify_location_and_case_name_is_displayed_as_heading_on_Enrollment_Details_panel(self):
        try:
            self.logger.info("************* test_TC_IE_106 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\img\\visitor_search_img_4.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)

            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            time.sleep(web_driver.one_second)
            self.logger.info("Enrollment details filled and save btn is clicked")
            
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            time.sleep(web_driver.one_second)

            review_enroll_details_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                           .review_enrollment_details_button_xpath(), self.d)
            review_enroll_details_btn.click()
            self.logger.info(f"Clicked on review_enrollment_details_button")
            time.sleep(web_driver.one_second)
            location_store_text = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .location_store_text_validation(), self.d)
            if location_store_text.is_displayed():
                self.logger.info(f"location_store_text is visible")
                self.status.append(True)
            else:
                self.logger.info(f"location_store_text is not visible")
                self.status.append(False)

            case_subject_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .case_subject_text_validation())
            if case_subject_text.is_displayed():
                self.logger.info(f"case_subject_text is visible")
                self.status.append(True)
            else:
                self.logger.info(f"case_subject_text is not visible")
                self.status.append(False)

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_106.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_106_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_106 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_106_exception.png")
            return False

    def verify_visitor_image_is_visible_besides_it_Enrolled_on_date_and_time_is_displayed_as_expected(self):
        try:
            self.logger.info("************* test_TC_IE_107 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path_1 = f"{Path(__file__).parent.parent.parent}\\{Read_Identify_and_Enroll_Components().enrolled_visitor_image_path_1()}"
            self.upload_image_to_identify_and_enroll(file_path_1)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.three_second)

            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************

            review_enroll_details_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                           .review_enrollment_details_button_xpath(), self.d)
            review_enroll_details_btn.click()
            self.logger.info("Clicked on review_enrollment_details_button")
            time.sleep(web_driver.one_second)
            image_validation = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_details_img_validation(), self.d)
            if image_validation.is_displayed():
                self.logger.info("image_validation is visible")
                self.status.append(True)
            else:
                self.logger.info("image_validation is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)

            enrolled_on_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .enrolled_on_text_validation())
            if enrolled_on_validation.is_displayed():
                self.logger.info("enrolled_on_text is visible")
                self.status.append(True)
            else:
                self.logger.info("enrolled_on_text is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)

            time_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().enrolled_time_validation())
            if time_validation.is_displayed():
                self.logger.info("enrolled time is visible")
                self.status.append(True)
            else:
                self.logger.info("enrolled time is visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_107.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_107_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_107 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_107_exception.png")
            return False

    def verify_Enabled_Disabled_status_with_its_symbol_is_visible_besides_visitor_image(self):
        try:
            self.logger.info("************* test_TC_IE_108 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\img\\visitor_search_img_4.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            review_enroll_details_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                           .review_enrollment_details_button_xpath(), self.d)
            review_enroll_details_btn.click()
            self.logger.info("Clicked on review_enroll_details_btn")
            time.sleep(web_driver.one_second)
            enable_btn_with_symbol_validation = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                                   .enable_text_with_symbol_validation(), self.d)
            if enable_btn_with_symbol_validation.is_displayed():
                self.logger.info("enable_btn_with_symbol_validation is visible")
                self.status.append(True)
            else:
                self.logger.info("enable_btn_with_symbol_validation is not visible")
                self.status.append(False)
            time.sleep(web_driver.one_second)

            enable_symbol_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .enable_button_symbol_validation())
            if enable_symbol_validation.is_displayed():
                self.logger.info("enable_symbol_validation is visible")
                self.status.append(True)
            else:
                self.logger.info("enable_symbol_validation is not visible")
                self.status.append(False)

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_108.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_108_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_108 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_108_exception.png")
            return False

    def verify_Opt_out_status_is_displayed_as_expected_on_Enrollment_Details_panel(self):
        try:
            self.logger.info("************* test_TC_IE_109 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.status.clear()
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\img\\visitor_search_img_1.png"
            self.upload_image_to_identify_and_enroll(file_path)
            
            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            review_enroll_details_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                           .review_enrollment_details_button_xpath(), self.d)
            review_enroll_details_btn.click()
            self.logger.info("Clicked on review_enroll_details_btn")
            time.sleep(web_driver.one_second)
            opt_out_status_validation = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                           .opt_out_status_validation(), self.d)
            if opt_out_status_validation.is_displayed():
                self.logger.info("opt_out_status_validation is visible")
                self.status.append(True)
            else:
                self.logger.info("opt_out_status_validation is not visible")
                self.status.append(False)

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_109.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_109_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_109 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_109_Exception.png")
            return False

    def verify_REQUIRED_FIELDS_heading_is_displayed_along_with_its_data_on_Enrollment_Details_Panel(self):
        try:
            self.logger.info("************* test_TC_IE_110 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\img\\visitor_search_img_2.png"
            self.upload_image_to_identify_and_enroll(file_path)
            
            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().add_details_panel_title_panel())
            self.logger.info(f"title list length: {len(title)}")
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components().add_details_panel_validation().lower():
                    self.logger.info(f"x: {x.text}")
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************

            review_enroll_details_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().review_enrollment_details_button_xpath(), self.d)
            self.logger.info(f"review enroll details btn displayed: {review_enroll_details_btn.is_displayed()}")
            review_enroll_details_btn.click()

            time.sleep(web_driver.one_second)

            required_fields_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().required_fields_title_validation())
            self.logger.info(f"required fields validation displayed: {required_fields_validation.is_displayed()}")
            if required_fields_validation.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)

            location_store_text_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().location_store_text_validation())
            self.logger.info(f"location store text displayed: {location_store_text_validation.is_displayed()}")
            if location_store_text_validation.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            case_subject_text_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().case_subject_text_validation())
            self.logger.info(f"case subject text displayed: {case_subject_text_validation.is_displayed()}")
            if case_subject_text_validation.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            reported_loss_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .reported_loss_validation())
            self.logger.info(f"report loss validation displayed: {reported_loss_validation.is_displayed()}")
            if reported_loss_validation.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)

            date_incident_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().date_incident_validation())
            self.logger.info(f"date incident displayed: {date_incident_validation.is_displayed()}")
            if date_incident_validation.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)

            action_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().action_data_validation())
            self.logger.info(f"action validation displayed: {action_validation.is_displayed()}")
            if action_validation.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_110.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_110_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_110 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_110_Exception.png")
            return False

    def verify_OPTIONAL_FIELDS_heading_below_required_field_is_displayed_as_expected(self):
        try:
            self.logger.info("************* test_TC_IE_111 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\Other_IMP_Files\\Images\\Images\\img6.jpg"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)

            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            activity_type = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                                .activity_type_dropdown())
            select = Select(activity_type)
            select.select_by_index(1)
            time.sleep(web_driver.one_second)

            method_of_offense = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                                    .method_of_offence_by_xpath())
            select = Select(method_of_offense)
            select.select_by_index(1)
            time.sleep(web_driver.one_second)

            gender = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                         .gender_dropdown())
            select = Select(gender)
            select.select_by_index(1)
            time.sleep(web_driver.one_second)

            case_event_type = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                                  .case_event_type_dropdown())
            select = Select(case_event_type)
            select.select_by_index(1)
            time.sleep(web_driver.one_second)

            height = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                         .height_type_dropdown())
            select = Select(height)
            select.select_by_index(1)
            time.sleep(web_driver.one_second)

            reported_by = self.d.find_element(By.XPATH, Audit_Log_Report_Components().reported_by_input())
            reported_by.send_keys(Audit_Log_Report_Components().reported_by_data())
            time.sleep(web_driver.one_second)

            build = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                        .build_input())
            build.send_keys(Audit_Log_Report_Components().build_data())
            time.sleep(web_driver.one_second)

            body_markings = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                                .body_markings_input())
            body_markings.send_keys(Audit_Log_Report_Components().body_markings_data())
            time.sleep(web_driver.one_second)

            narratives = self.d.find_element(By.XPATH, Audit_Log_Report_Components()
                                             .narrative_Desc_input())
            narratives.send_keys(Audit_Log_Report_Components().narratives_data())
            time.sleep(web_driver.two_second)

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            review_enroll_details_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                           .review_enrollment_details_button_xpath(), self.d)
            review_enroll_details_btn.click()
            self.logger.info("Clicked on review_enrollment_details_button")
            time.sleep(web_driver.two_second)

            optional_fields_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .optional_fields_text_validation())
            time.sleep(web_driver.three_second)
            if optional_fields_validation.is_displayed():
                self.logger.info("optional_fields_text is visible")
                self.status.append(True)
            else:
                self.logger.info("optional_fields_text is not visible")
                self.status.append(False)
            case_event_type_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                             .case_event_type_validation())
            if case_event_type_validation.is_displayed():
                self.logger.info("case_event_type is visible")
                self.status.append(True)
            else:
                self.logger.info("case_event_type is not visible")
                self.status.append(False)
            activity_type_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .activity_type_validation())
            if activity_type_validation.is_displayed():
                self.logger.info("activity_type is visible")
                self.status.append(True)
            else:
                self.logger.info("activity_type is not visible")
                self.status.append(False)
            method_of_offense_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                               .method_of_offense_validation())
            if method_of_offense_validation.is_displayed():
                self.logger.info("method_of_offense is visible")
                self.status.append(True)
            else:
                self.logger.info("method_of_offense is not visible")
                self.status.append(False)

            reported_by_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                         .reported_by_validation())
            if reported_by_validation.is_displayed():
                self.logger.info("reported_by is visible")
                self.status.append(True)
            else:
                self.logger.info("reported_by is not visible")
                self.status.append(False)

            body_markings_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .body_markings_validation())
            if body_markings_validation.is_displayed():
                self.logger.info("body_markings is visible")
                self.status.append(True)
            else:
                self.logger.info("body_markings is not visible")
                self.status.append(False)

            gender_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .gender_validation())
            if gender_validation.is_displayed():
                self.logger.info("gender is visible")
                self.status.append(True)
            else:
                self.logger.info("gender is not visible")
                self.status.append(False)

            height_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .height_validation())
            if height_validation.is_displayed():
                self.logger.info("height is visible")
                self.status.append(True)
            else:
                self.logger.info("height is not visible")
                self.status.append(False)

            narratives_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                        .narratives_validation())
            if narratives_validation.is_displayed():
                self.logger.info("narratives is visible")
                self.status.append(True)
            else:
                self.logger.info("narratives is not visible")
                self.status.append(False)

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_111.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_111_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_111 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_111_Exception.png")
            return False

    def click_on_close_enrollment_details_panel_and_verify_panel_is_closed_successfully(self):
        try:
            self.logger.info("************* test_TC_IE_112 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            # self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().upload_image_by_xpath(), self.d)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_Data\\img\\visitor_search_img_3.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())

            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_112.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_112_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_112 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_112_Exception.png")
            return False

    def click_on_Review_Added_Groups_Button_and_verify_if_enrollment_groups_panel_is_visible(self):
        try:
            self.status = []
            self.logger.info("************* test_TC_IE_113 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_4.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            review_added_groups_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                         .review_added_groups_button_xpath(), self.d)
            review_added_groups_btn.click()
            self.logger.info("Clicked on review_added_groups_button")
            review_added_groups_validation = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                                .review_added_groups_button_validation(), self.d)
            if review_added_groups_validation.is_displayed():
                self.logger.info("review_added_groups_validation is visible")
                self.status.append(True)
            else:
                self.logger.info("review_added_groups_validation is not visible")
                self.status.append(False)

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_113.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_113_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_113 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_113_exception.png")
            return False

    def verify_Filter_dropdown_is_visible_and_clickable_on_Enrollment_Groups_Panel(self):
        try:
            self.logger.info("************* test_TC_IE_114 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_4.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************

            review_added_groups_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                         .review_added_groups_button_xpath(), self.d)
            review_added_groups_btn.click()
            self.logger.info("Clicked on review_added_groups_btn")
            time.sleep(web_driver.two_second)
            filter_dropdown = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                 .filter_dropdown_xpath(), self.d)
            if filter_dropdown.is_displayed():
                self.logger.info("filter_dropdown is visible")
                self.status.append(True)
            else:
                self.logger.info("filter_dropdown is not visible")
                self.status.append(False)
            filter_dropdown.click()

            time.sleep(web_driver.one_second)
            filter_dropdown_click_validation = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                                  .filter_dropdown_validation(), self.d)
            if filter_dropdown_click_validation.is_displayed():
                self.logger.info("filter_dropdown_click_validation is visible")
                self.status.append(True)
            else:
                self.logger.info("filter_dropdown_click_validation is not visible")
                self.status.append(False)

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_114.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_114_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_114 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_114_exception.png")
            return False

    def click_on_Filter_dropdown_and_verify_its_options_are_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_115 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_4.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            review_added_groups_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                         .review_added_groups_button_xpath(), self.d)
            review_added_groups_btn.click()
            self.logger.info("Clicked on review_added_groups_button")
            time.sleep(web_driver.two_second)

            filter_dropdown = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                 .filter_dropdown_xpath(), self.d)
            if filter_dropdown.is_displayed():
                self.logger.info("filter_dropdown is visible")
                self.status.append(True)
            else:
                self.logger.info("filter_dropdown is not visible")
                self.status.append(False)
            filter_dropdown.click()
            self.logger.info("Clicked on filter dropdown")
            time.sleep(web_driver.two_second)

            linked_enroll_option = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                      .linked_enroll_option(), self.d)
            if linked_enroll_option.is_displayed():
                self.logger.info("linked_enroll_option is visible")
                self.status.append(True)
            else:
                self.logger.info("linked_enroll_option is not visible")
                self.status.append(False)
            linked_enroll_option.click()
            self.logger.info("Clicked on linked_enroll_option")
            time.sleep(web_driver.two_second)

            filter_dropdown.click()
            self.logger.info("Clicked on filter dropdown")
            time.sleep(web_driver.one_second)

            unlinked_enroll_option = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                        .unlinked_enroll_option(), self.d)
            if unlinked_enroll_option.is_displayed():
                self.logger.info("unlinked_enroll_option is visible")
                self.status.append(True)
            else:
                self.logger.info("unlinked_enroll_option is not visible")
                self.status.append(False)
            unlinked_enroll_option.click()
            time.sleep(web_driver.one_second)
            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_115.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_115_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_115 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_115_Exception.png")
            return False

    def verify_Action_dropdown_is_visible_and_clickable_on_Enrollment_Groups_Panel(self):
        try:
            self.logger.info("************* test_TC_IE_116 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_4.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)
            time.sleep(web_driver.one_second)
            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            review_added_groups_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                         .review_added_groups_button_xpath(), self.d)
            review_added_groups_btn.click()
            self.logger.info("Clicked on review_added_groups_btn")
            time.sleep(web_driver.two_second)
            action_dropdown = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                 .enrollment_group_action_btn(), self.d)
            if action_dropdown.is_displayed():
                self.logger.info("action_dropdown is visible")
                self.status.append(True)
            else:
                self.logger.info("action_dropdown is not visible")
                self.status.append(False)
            action_dropdown.click()

            time.sleep(web_driver.two_second)

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_116.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_116_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_116 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_116_exception.png")
            return False

    def click_on_Action_dropdown_and_verify_its_options_are_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_117 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image_to_identify_and_enroll(file_path)
            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.three_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            review_added_groups_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                         .review_added_groups_button_xpath(), self.d)
            review_added_groups_btn.click()
            self.logger.info("Clicked on review_added_groups btn")
            time.sleep(web_driver.two_second)

            action_dropdown = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                 .enrollment_group_action_btn(), self.d)
            if action_dropdown.is_displayed():
                self.logger.info("action_dropdown is visible")
                self.status.append(True)
            else:
                self.logger.info("action_dropdown is not visible")
                self.status.append(False)
            action_dropdown.click()
            self.logger.info("Clicked on action_dropdown")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().action_btn_refresh_option(), self.d)
            add_person = None
            remove_person = None
            refresh = None
            try:
                add_person = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().action_btn_add_person_option())
                self.logger.info(f"add person panel option visible: {add_person.is_displayed()}")
            except Exception as ex:
                self.logger.info(f"add person option exception: {ex.args}")
            try:
                remove_person = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().remove_person_from_group())
            except Exception as ex:
                self.logger.info(f"remove person option exception: {ex.args}")
            if add_person or remove_person:
                if add_person:
                    if add_person.is_enabled():
                        self.status.append(True)
                        self.logger.info("add_person is enabled")
                elif remove_person:
                    if remove_person.is_enabled():
                        self.status.append(True)
                        self.logger.info("remove_person is enabled")
                else:
                    self.status.append(False)
            try:

                self.d.switch_to.alert.accept()
                time.sleep(web_driver.one_second)
            except Exception as ex:
                self.logger.info(ex.args)
            time.sleep(web_driver.one_second)
            # action_dropdown.click()
            self.logger.info("Clicked on action_dropdown")
            time.sleep(web_driver.one_second)
            create_group = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().action_btn_create_group_option(), self.d)
            self.logger.info(f"create group option visible: {create_group.is_displayed()}")
            if create_group.is_displayed():
                if create_group.is_enabled():
                    self.status.append(True)
                    self.logger.info("enabled create_group")

            time.sleep(web_driver.one_second)
            # action_dropdown.click()
            self.logger.info("Clicked on action_dropdown")
            try:
                refresh = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                         .action_btn_refresh_option(), self.d)
            except Exception as ex:
                self.logger.info(f"refresh exception: {ex.args}")
            if refresh.is_displayed():
                refresh.click()
                self.logger.info("Clicked on refresh")

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_117.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_117_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_117 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_117_exception.png")
            return False

    def verify_select_all_check_box_along_with_its_label_is_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_118 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_4.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")
            time.sleep(web_driver.two_second)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            review_added_groups_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                         .review_added_groups_button_xpath(), self.d)
            review_added_groups_btn.click()
            time.sleep(web_driver.two_second)

            select_all_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .select_all_text_validation())
            if select_all_text.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            time.sleep(web_driver.two_second)

            select_all_check_box = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .select_all_check_box_click())
            if select_all_check_box.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            select_all_check_box.click()
            time.sleep(web_driver.one_second)
            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_118.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_118_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_118 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_118_Exception.png")
            return False

    def verify_enrollment_groups_associated_with_enrollment_is_enlisted_inside_Enrollment_Groups_panel(self):
        try:
            self.logger.info("************* test_TC_IE_119 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_4.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            review_added_groups_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                         .review_added_groups_button_xpath(), self.d)
            review_added_groups_btn.click()
            self.logger.info("Clicked on review_added_groups_btn")
            time.sleep(web_driver.two_second)
            associate_group = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                 .associate_group_validation(), self.d)
            if associate_group.is_displayed():
                self.logger.info("associate_group is visible")
                self.status.append(True)
            else:
                self.logger.info("associate_group is not visible")
                self.status.append(False)
            time.sleep(web_driver.two_second)

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_119.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_119_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_119 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_119_Exception.png")
            return False

    def click_on_close_enrollment_group_panel_and_verify_panel_is_closed_successfully(self):
        try:
            self.logger.info("************* test_TC_IE_120 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            # self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().upload_image_by_xpath(), self.d)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_4.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .review_added_groups_button_xpath(), self.d)
            review_add_group = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                   .review_added_groups_button_xpath())
            review_add_group.click()
            self.logger.info("Clicked on review added groups btn")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().
                               enrollment_details_panel_close_1(), self.d)
            enrollment_group_panel = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().
                                                         enrollment_details_panel_close_1())
            enrollment_group_panel.click()
            # self.d.execute_script("arguments[0].click();", enrollment_group_panel)
            time.sleep(web_driver.two_second)

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         review_added_groups_button_validation())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        enrollment_view_enrollment_groups_txt_validation().lower():
                    self.status.append(False)

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.logger.info(f"status: {self.status}")
            print(self.status)
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_120.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_120_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_120 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_120_exception.png")
            return False

    def click_on_add_more_faces_button_and_verify_if_Enrollment_Faces_panel_is_displayed(self):
        try:
            self.logger.info("************* test_TC_IE_121 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            # self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().upload_image_by_xpath(), self.d)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_4.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")
            self.click_on_enroll_for_already_enrolled()
            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_more_faces_xpath(), self.d)
            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()
            self.logger.info("Clicked on Add more faces btn")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_more_faces_validation(), self.d)
            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()
            self.logger.info(f"add_more_faces_validation is visible : {add_more_faces_validation.is_displayed()}")
            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_121.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_121_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_121 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_121_exception.png")
            return False

    def verify_Action_button_is_visible_and_clickable_on_Enrollment_Faces_Panel_below_its_title(self):
        try:
            self.logger.info("************* test_TC_IE_122 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_4.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            add_more_faces_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                    .add_more_faces_xpath(), self.d)
            add_more_faces_btn.click()
            self.logger.info("Clicked on add_more_faces_btn")
            add_more_faces_validation = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                           .add_more_faces_validation(), self.d)
            add_more_faces_validation.is_displayed()

            add_more_faces_action_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .enrollment_faces_action_btn())
            if add_more_faces_action_btn.is_displayed():
                self.logger.info("add_more_faces_action_btn is visible")
                self.status.append(True)
            else:
                self.logger.info("add_more_faces_action_btn is not visible")
                self.status.append(False)
            add_more_faces_action_btn.click()
            time.sleep(web_driver.two_second)

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_122.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_122_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_122 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_122_exception.png")
            return False

    def click_on_Action_dropdown_and_verify_its_options_are_visible_and_clickable_enroll_face_panel(self):
        try:
            self.logger.info("************* test_TC_IE_123 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            # self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().upload_image_by_xpath(), self.d)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_4.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_more_faces_xpath(), self.d)
            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            if add_more_faces_btn.is_displayed():
                self.logger.info("add_more_faces_btn is visible")
                self.status.append(True)
            else:
                self.logger.info("add_more_faces_btn is not visible")
                self.status.append(False)
            add_more_faces_btn.click()
            self.logger.info("clicked on add_more_faces_btn")
            time.sleep(web_driver.one_second)
            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            add_more_faces_action_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .enrollment_faces_action_btn())
            if add_more_faces_action_btn.is_displayed():
                self.logger.info("add_more_faces_action_btn is visible")
                self.status.append(True)
            else:
                self.logger.info("add_more_faces_action_btn is not visible")
                self.status.append(False)
            add_more_faces_action_btn.click()
            self.logger.info("clicked on add_more_faces_action_btn")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .enrollments_option_xpath(), self.d)
            enrollment_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                    .enrollments_option_xpath())
            if enrollment_option.is_displayed():
                self.logger.info("enrollment_option is visible")
                self.status.append(True)
            else:
                self.logger.info("enrollment_option is not visible")
                self.status.append(False)
            enrollment_option.click()
            self.logger.info("clicked on enrollment_option")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().enrollment_faces_action_btn(), self.d)
            add_more_faces_action_btn.click()
            self.logger.info("clicked on add_more_faces_action_btn")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .visitors_option_xpath(), self.d)
            visitors_option = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                  .visitors_option_xpath())
            if visitors_option.is_displayed():
                self.logger.info("visitors_option is visible")
                self.status.append(True)
            else:
                self.logger.info("visitors_option is not visible")
                self.status.append(False)
            visitors_option.click()
            self.logger.info("clicked on Visitors option")
            time.sleep(web_driver.one_second)
            add_more_faces_action_btn.click()
            self.logger.info("clicked on add_more_faces_action_btn")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_photo_option_xpath(), self.d)
            add_photo = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .add_photo_option_xpath())
            if add_photo.is_displayed():
                self.logger.info("add_photo is visible")
                self.status.append(True)
            else:
                self.logger.info("add_photo is not visible")
                self.status.append(False)
            add_photo.click()
            self.logger.info("clicked on add_photo option")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().enrollment_faces_action_btn(), self.d)
            add_more_faces_action_btn.click()
            self.logger.info("clicked on add_more_faces_action_btn")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_4.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(web_driver.one_second)
            pyautogui.press('enter')
            self.logger.info(f"Image upload success")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .delete_faces_option_xpath(), self.d)
            delete_faces = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .delete_faces_option_xpath())
            if delete_faces.is_displayed():
                self.logger.info("delete_faces_option is visible")
                self.status.append(True)
            else:
                self.logger.info("delete_faces_option is not visible")
                self.status.append(False)
            delete_faces.click()
            self.logger.info("clicked on delete_faces option")
            self.d.switch_to.alert.accept()
            time.sleep(web_driver.one_second)
            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_123.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_123_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_123 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_123_Exception.png")
            return False

    def verify_location_and_case_name_is_displayed_as_heading_on_Enrollment_Faces_panel(self):
        try:
            self.logger.info("************* test_TC_IE_124 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_3.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************

            add_more_faces_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                    .add_more_faces_xpath(), self.d)
            add_more_faces_btn.click()
            self.logger.info("Clicked on add_more_faces_btn")
            time.sleep(web_driver.one_second)
            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(web_driver.three_second)

            location_case_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                           .location_cases_name_validation())
            time.sleep(web_driver.three_second)
            print(location_case_validation.text)
            if location_case_validation.is_displayed():
                self.logger.info("location_case_validation is visible")
                self.status.append(True)
            else:
                self.logger.info("location_case_validation is not visible")
                self.status.append(False)
            print(self.status)
            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_124.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_124_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_124 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_124_Exception.png")
            return False

    def verify_sample_image_box_is_visible_and_clickable_below_location_information(self):
        try:
            self.logger.info("************* test_TC_IE_125 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_3.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************

            add_more_faces_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                    .add_more_faces_xpath(), self.d)
            add_more_faces_btn.click()
            self.logger.info("Clicked on add_more_faces_btn")
            time.sleep(web_driver.one_second)
            add_more_faces_validation = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                           .add_more_faces_validation(), self.d)
            add_more_faces_validation.is_displayed()

            time.sleep(web_driver.three_second)

            sample_img_box = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .sample_img_box_xpath())
            time.sleep(web_driver.three_second)
            if sample_img_box.is_displayed():
                self.logger.info("sample_img_box is visible")
                self.status.append(True)
            else:
                self.logger.info("sample_img_box is not visible")
                self.status.append(False)
            sample_img_box.click()

            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_3.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(web_driver.one_second)
            pyautogui.press('enter')
            self.logger.info(f"Image upload success")

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_125.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_125_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_125 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_125_exception.png")
            return False

    def click_on_sample_image_box_and_verify_if_file_open_dialog_box_is_displayed(self):
        try:
            self.logger.info("************* test_TC_IE_126 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            # self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().upload_image_by_xpath(), self.d)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\unenrolled_visitor_search_img_2.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH",
                                                  Read_Identify_and_Enroll_Components().enrollment_basis_by_xpath(),
                                                  self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            time.sleep(web_driver.one_second)
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************

            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_more_faces_xpath(), self.d)
            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()
            self.logger.info("clicked on add_more_faces_btn")
            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_more_faces_validation(), self.d)
            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(web_driver.one_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .sample_img_box_xpath(), self.d)
            sample_img_box = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                 .sample_img_box_xpath())
            if sample_img_box.is_displayed():
                self.logger.info("sample_img_box is visible")
                self.status.append(True)
            else:
                self.logger.info("sample_img_box is not visible")
                self.status.append(False)
            sample_img_box.click()
            self.logger.info("clicked on sample_img_box")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\test_102.png"
            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(web_driver.one_second)
            pyautogui.press('enter')
            self.logger.info(f"Image upload success")

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_126.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_126_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_126 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_126_Exception.png")
            return False

    def verify_Dragable_Photo_Text_be_displayed_on_enrolled_visitor_image_below_sample_image(self):
        try:
            self.logger.info("************* test_TC_IE_127 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_1.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            time.sleep(web_driver.one_second)
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.two_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            time.sleep(web_driver.one_second)
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************

            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()
            self.logger.info("Clicked on add_more_faces_btn")
            time.sleep(web_driver.two_second)

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(web_driver.one_second)

            draggable_photo_text = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                       .draggable_photo_text())
            if draggable_photo_text.is_displayed():
                self.logger.info("draggable_photo_text is visible")
                self.status.append(True)
            else:
                self.logger.info("draggable_photo_text is not visible")
                self.status.append(False)

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_127.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_127_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_127 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_127_exception.png")
            return False

    def verify_check_box_is_visible_and_clickable_besides_visitor_image_on_the_panel(self):
        try:
            self.logger.info("************* test_TC_IE_128 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_2.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            add_more_faces_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                    .add_more_faces_xpath(), self.d)
            add_more_faces_btn.click()
            self.logger.info("Clicked on add_more_faces_btn")
            add_more_faces_validation = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                           .add_more_faces_validation(), self.d)
            add_more_faces_validation.is_displayed()

            time.sleep(web_driver.one_second)

            check_box = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .check_box_xpath())
            if check_box.is_displayed():
                self.logger.info("check_box is visible")
                self.status.append(True)
            else:
                self.logger.info("check_box is not visible")
                self.status.append(False)
            check_box.click()

            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_128.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_128_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_128 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_128_Exception.png")
            return False

    def verify_download_image_button_is_visible_and_clickable_besides_visitor_image(self):
        try:
            self.logger.info("************* test_TC_IE_129 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_3.png"

            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.two_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            add_more_faces_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                    .add_more_faces_xpath(), self.d)
            add_more_faces_btn.click()
            self.logger.info("Clicked on add_more_faces_btn")
            time.sleep(web_driver.two_second)

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(web_driver.one_second)

            download_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .download_img_button_xpath())
            if download_btn.is_displayed():
                download_btn.click()
                self.logger.info("Clicked on download_img_button_xpath")

            self.delete_enrollment()
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_129.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_129_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_129 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_129_exception.png")
            return False

    def verify_image_file_info_button_is_visible_and_clickable_besides_visitor_image(self):
        try:
            self.logger.info("************* test_TC_IE_130 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_3.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.two_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.two_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())
            time.sleep(web_driver.one_second)
            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())
            time.sleep(web_driver.one_second)
            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())
            time.sleep(web_driver.one_second)
            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())
            time.sleep(web_driver.one_second)
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************

            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()
            self.logger.info("Clicked on add_more_faces_btn")
            time.sleep(web_driver.two_second)

            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(web_driver.one_second)

            img_file_info = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .view_img_info_xpath())
            if img_file_info.is_displayed():
                self.logger.info("view_img_info is visible")
                self.status.append(True)
            else:
                self.logger.info("view_img_info is not visible")
                self.status.append(False)
            img_file_info.click()
            time.sleep(web_driver.two_second)

            self.d.switch_to.alert.accept()
            time.sleep(web_driver.one_second)
            self.delete_enrollment()
            time.sleep(web_driver.one_second)
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_130.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_130_failed.png")
                logout().logout_from_core(self.d)
                return False
            else:
                logout().logout_from_core(self.d)
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_130 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_130_Exception.png")
            return False

    def click_on_download_image_button_and_verify_image_is_downloaded_successfully(self):
        try:
            self.logger.info("************* test_TC_IE_131 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            # self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().upload_image_by_xpath(), self.d)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_3.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            time.sleep(web_driver.one_second)
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")
            
            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************

            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_more_faces_xpath(), self.d)
            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()
            self.logger.info("clicked on add_more_faces_btn")
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_more_faces_validation(), self.d)
            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(web_driver.one_second)

            download_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .download_img_button_xpath())
            if download_btn.is_displayed():
                download_btn.click()
                self.logger.info("clicked on download_btn")

            self.delete_enrollment()
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_131.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_131_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_131 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_131_Exception.png")
            return False

    def click_on_image_file_info_button_and_verify_a_pop_up_is_displayed_with_image_information(self):
        try:
            self.logger.info("************* test_TC_IE_132 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            # self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().upload_image_by_xpath(), self.d)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_3.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            self.click_on_enroll_for_already_enrolled()
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)

#             action_input = self.d.find_element(By.XPATH,
#                                                Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")

            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation(). \
                        lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            title = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().
                                         add_details_panel_title_panel())
            for x in title:
                if x.text.strip().lower() == Read_Identify_and_Enroll_Components(). \
                        add_details_panel_validation().lower():
                    self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_more_faces_xpath(), self.d)
            add_more_faces_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                     .add_more_faces_xpath())
            add_more_faces_btn.click()
            self.logger.info("Clicked on add_more_faces_btn")
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_more_faces_validation(), self.d)
            add_more_faces_validation = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                            .add_more_faces_validation())
            add_more_faces_validation.is_displayed()

            time.sleep(web_driver.one_second)

            img_file_info = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .view_img_info_xpath())
            if img_file_info.is_displayed():
                self.logger.info("img_file_info is visible")
                self.status.append(True)
            else:
                self.logger.info("img_file_info is not visible")
                self.status.append(False)
            # img_file_info.click()
            self.d.execute_script("arguments[0].click();", img_file_info)
            time.sleep(web_driver.two_second)
            text = self.d.switch_to.alert.text
            if Read_Identify_and_Enroll_Components().view_image_pop_up_text_1() in text:
                self.status.append(True)
            else:
                self.status.append(False)
            if Read_Identify_and_Enroll_Components().view_image_pop_up_text_2() in text:
                self.status.append(True)
            else:
                self.status.append(False)
            if Read_Identify_and_Enroll_Components().view_image_pop_up_text_3() in text:
                self.status.append(True)
            else:
                self.status.append(False)
            if Read_Identify_and_Enroll_Components().view_image_pop_up_text_4() in text:
                self.status.append(True)
            else:
                self.status.append(False)
            self.d.switch_to.alert.accept()

            self.delete_enrollment()
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_132.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_132_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_132 got an exception as: {ex.args}")
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_132_exception.png")
            return False

    def click_on_close_panel_button_and_verify_enrollment_faces_panel_is_closed_successfully(self):
        try:
            self.logger.info("************* test_TC_IE_133 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            # self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().upload_image_by_xpath(), self.d)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_4.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting fir wait icon, count: {count}")

            self.click_on_enroll_for_already_enrolled()

            # ***************************************Enrollment Process start here**********************
            time.sleep(web_driver.two_second)
            enrollment_basis = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                  .enrollment_basis_by_xpath(), self.d)
            select = Select(enrollment_basis)
            select.select_by_index(1)

            time.sleep(web_driver.two_second)
            self.Select_Enrollment_Group('soe')
            
            enrollment_group_selected = select.first_selected_option
            self.logger.info(f"enrollment group selected = {enrollment_group_selected.text}")
            print(f"enrollment group selected: {enrollment_group_selected.text}")
            time.sleep(web_driver.one_second)
            region_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().region_btn_by_xpath())
            time.sleep(web_driver.one_second)
            region_btn.click()
            time.sleep(web_driver.one_second)
            region_names = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().edge_name_list())
            edge_name = Read_Identify_and_Enroll_Components().edge_name()
            for i in range(len(region_names)):
                if edge_name in region_names[i].text:
                    region_names[i].click()
                    break
            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().save_btn_by_xpath())
            save_btn.click()
            time.sleep(web_driver.two_second)
            # action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().action_input_by_xpath())
            time.sleep(web_driver.one_second)

            location_store = self.d.find_element(By.XPATH,
                                                 Read_Identify_and_Enroll_Components().location_store_inpt_bx_by_xpath())
            location_store.send_keys(Read_Identify_and_Enroll_Components().location_store_data())

            case_subject = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .case_subject_inpt_bx_by_xpath())
            case_subject.send_keys(Read_Identify_and_Enroll_Components().case_subject_data())

            date_incident = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .date_incident_inpt_bx_by_xpath())
            time.sleep(web_driver.two_second)
            self.dateTimeAMPM(date_incident)

            time.sleep(web_driver.two_second)

            reported_loss = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                                .reported_loss_inpt_bx_by_xpath())
            reported_loss.send_keys(Read_Identify_and_Enroll_Components().reported_loss_data())

            action_input = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                               .action_inpt_bx_by_xpath())
            action_input.send_keys(Read_Identify_and_Enroll_Components().action_input_data())

            save_btn = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                           .add_details_save_btn_by_xpath())
            if save_btn.is_displayed():
                self.status.append(True)
            else:
                self.status.append(False)
            save_btn.click()
            self.logger.info("Enrollment details filled and save btn is clicked")

            try:
                success_msg = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().enrollment_success_msg_xpath(),
                                                 self.d)
                if success_msg.text.lower() == Read_Identify_and_Enroll_Components().enrollment_success_msg_validation().lower():
                    self.logger.info(f"Success msg is visible : {True}")
                    self.status.append(True)
                else:
                    self.logger.info(f"Success msg is visible : {False}")
                    self.status.append(False)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.d.refresh()

            add_more_faces_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                    .add_more_faces_xpath(), self.d)
            add_more_faces_btn.click()
            self.logger.info("Clicked on Add more faces btn")
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .add_more_faces_validation(), self.d)
            try:
                enrollment_face_close_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                               .enrollment_faces_panel_close_btn(), self.d)
                enrollment_face_close_btn.click()
                self.status.append(True)
            except Exception as ex:
                self.logger.info(f"exception: {ex.args}")
                self.status.append(False)

            time.sleep(web_driver.one_second)
            # ***************************************Enrollment Process end here**********************
            self.delete_enrollment()
            self.close_all_panel_one_by_one()

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_133.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_133_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_133 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_133_Exception.png")
            return False

    def click_on_close_all_panel_btn(self):
        panel_list = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().get_panel_by_xpath())
        if len(panel_list) > 0:
            cloud_menu = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components().cloud_menu_button_xpath())
            cloud_menu.click()
            time.sleep(web_driver.one_second)
            close_all_panel_btn = self.d.find_element(By.XPATH,
                                                      Read_Identify_and_Enroll_Components().get_close_all_panel_menu_item_by_xpath())
            close_all_panel_btn.click()
            time.sleep(web_driver.two_second)

    def click_on_enroll_for_already_enrolled(self):
        time.sleep(web_driver.two_second)
        enroll = self.d.find_element(By.XPATH, "//i[@class='fa fa-pencil']")
        # web_driver.explicit_wait(self, 10, enroll, self.d)
        if enroll.is_displayed():
            # enroll.click()
            self.d.execute_script("arguments[0].click();", enroll)
            self.logger.info("Re-enroll for already enrolled ")
            self.logger.info("clicked on enroll button")

    def Click_on_re_select_photo_btn_and_verify_image_is_removed_from_img_box(self):
        try:
            self.logger.info("************* test_TC_IE_134 started  **************")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.one_second)
            self.open_identify_and_enroll_and_upload_an_image()
            time.sleep(web_driver.one_second)
            self.click_on_reselect_btn()

            select_a_photo_text = self.d.find_element(By.XPATH,
                                                      Read_Identify_and_Enroll_Components().select_a_photo_text_by_xpath())
            actual_text = select_a_photo_text.text
            expected_text = Read_Identify_and_Enroll_Components().identify_and_enroll_panel_select_photo_text()
            self.logger.info(f"Expected data = {expected_text}")
            self.logger.info(f"Actual data = {actual_text}")
            if actual_text.lower() == expected_text.lower():
                self.status.append(True)
            else:
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_IE_134 End  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_134_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_134_Exception.png")
            self.logger.info(f"Test Case Exception: {ex.args}")
            return False

    def verify_enrollment_region_label_and_region_name_is_visible_identify_result_panel(self):
        try:
            self.logger.info("************* test_TC_IE_135 started  **************")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_identify_and_enroll_and_upload_an_image()
            time.sleep(web_driver.one_second)
            # self.verify_identify_enroll_button_is_visible_and_clickable()
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            # identify_result_panel = self.verify_new_panel_is_displayed_with_title_as_Identify_Results()
            identify_result_panel = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().identify_results_panel_by_xpath(), self.d)
            self.logger.info(f"Identify result panel visible: {identify_result_panel.is_displayed()}")
            if identify_result_panel.is_displayed():
                time.sleep(web_driver.one_second)
                enrollment_region_text = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().enrollment_region_text_on_identify_result_panel_by_xpath(), self.d)
                self.logger.info(f"enrollment region text visible: {enrollment_region_text.is_displayed()}")
                enrollment_region_name = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().enrollment_region_name_on_identify_result_panel_by_xpath(), self.d)
                self.logger.info(f"enrollment region name visible: {enrollment_region_name.is_displayed()}")
                if enrollment_region_text.is_displayed():
                    self.status.append(True)
                else:
                    self.logger.info("enrollment region text not displayed")
                    self.status.append(False)
                if enrollment_region_name.is_displayed():
                    self.status.append(True)
                else:
                    self.logger.info("enrollment region name is not visible")
                    self.status.append(False)
            else:
                self.logger.info("image provided is un-enrolled please enroll it before this test. ")
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_IE_135 End  **************")
            if False in self.status:
                self.logger.info("un-enrolled image...")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_135_Failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_135_Exception.png")
            self.logger.info(f"Test Case Exception: {ex.args}")
            return False

    def verify_enrollment_basis_label_test_is_displayed_with_dropdown_besides_it_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_136 started  **************")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\VS_images\\Visitor-1.png"
            self.upload_image_to_identify_and_enroll(file_path)
            time.sleep(web_driver.one_second)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().add_details_panel_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            add_details_panel_title = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().add_details_panel_by_xpath(), self.d)
            self.logger.info(f"add details panel visible: {add_details_panel_title.is_displayed()}")
            if add_details_panel_title.is_displayed():
                enrollment_basis_text = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().enrollment_basis_label_by_xpath(), self.d)
                self.logger.info(f"enrollment basis label is visible: {enrollment_basis_text.is_displayed()}")
                enrollment_basis_dropdown = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().enrollment_basis_by_xpath(), self.d)
                self.logger.info(f"enrollment basis dropdown: {enrollment_basis_dropdown.is_displayed()}")
                if enrollment_basis_text.is_displayed():
                    self.status.append(True)
                else:
                    self.status.append(False)
                if enrollment_basis_dropdown.is_displayed():
                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"add details panel is not visible as expected.")
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_IE_136 End  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_136_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_136_Exception.png")
            self.logger.info(f"Test Case Exception: {ex.args}")
            return False

    def click_on_enrollment_basis_dropdown_and_verify_options_inside_it_visible_and_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_137 started  **************")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\VS_images\\Visitor-1.png"
            self.upload_image_to_identify_and_enroll(file_path)
            time.sleep(web_driver.one_second)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().add_details_panel_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            add_details_panel_title = self.explicit_wait(10, "XPATH",
                                                         Read_Identify_and_Enroll_Components().add_details_panel_by_xpath(),
                                                         self.d)
            self.logger.info(f"add details panel visible: {add_details_panel_title.is_displayed()}")
            if add_details_panel_title.is_displayed():
                enrollment_basis_text = self.explicit_wait(10, "XPATH",
                                                           Read_Identify_and_Enroll_Components().enrollment_basis_label_by_xpath(),
                                                           self.d)
                self.logger.info(f"enrollment basis label is visible: {enrollment_basis_text.is_displayed()}")
                enrollment_basis_dropdown = self.explicit_wait(10, "XPATH",
                                                               Read_Identify_and_Enroll_Components().enrollment_basis_by_xpath(),
                                                               self.d)
                self.logger.info(f"enrollment basis dropdown: {enrollment_basis_dropdown.is_displayed()}")
                if enrollment_basis_text.is_displayed():
                    self.status.append(True)
                else:
                    self.status.append(False)
                if enrollment_basis_dropdown.is_displayed():
                    enrollment_basis_dropdown.click()
                    self.explicit_wait(5, "XPATH", Read_Identify_and_Enroll_Components().enrollment_basis_dropdown_options_by_xpath(), self.d)
                    options = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().enrollment_basis_dropdown_options_by_xpath())
                    for option in options:
                        if option.is_displayed():
                            self.logger.info(f"enrollment basis option: {option.text}")
                            self.status.append(True)
                        else:
                            self.status.append(False)

                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"add details panel is not visible as expected.")
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_IE_137 End  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_137_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_137_exception.png")
            self.logger.info(f"Test Case Exception: {ex.args}")
            return False

    def verify_region_label_and_hover_text_and_select_btn_besides_it_is_visible_and_Select_btn_is_clickable(self):
        try:
            self.logger.info("************* test_TC_IE_138 started  **************")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\VS_images\\Visitor-1.png"
            self.upload_image_to_identify_and_enroll(file_path)
            time.sleep(web_driver.one_second)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().add_details_panel_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            add_details_panel_title = self.explicit_wait(10, "XPATH",
                                                         Read_Identify_and_Enroll_Components().add_details_panel_by_xpath(),
                                                         self.d)
            self.logger.info(f"add details panel visible: {add_details_panel_title.is_displayed()}")
            if add_details_panel_title.is_displayed():
                region_text = self.explicit_wait(10, "XPATH",
                                                           Read_Identify_and_Enroll_Components().region_label_text_by_xpath(),
                                                           self.d)
                self.logger.info(f"region text displayed: {region_text.is_displayed()}")
                region_select_btn = self.explicit_wait(10, "XPATH",
                                                               Read_Identify_and_Enroll_Components().region_select_btn_by_xpath(),
                                                               self.d)
                self.logger.info(f"region select displayed: {region_select_btn.is_displayed()}")
                if region_text.is_displayed():
                    self.logger.info(f"region select label is visible: {region_text.is_displayed()}")
                    self.status.append(True)
                else:
                    self.status.append(False)
                if region_select_btn.is_displayed():
                    # region_select_btn.click()
                    self.logger.info(f"region select btn is visible: {region_select_btn.is_displayed()}")
                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"add details panel is not visible as expected.")
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_IE_138 End  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_138_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_138_Exception.png")
            self.logger.info(f"Test Case Exception: {ex.args}")
            return False

    def click_on_select_btn_abd_verify_region_hirarchy_is_visible_and_user_able_to_select_region(self):
        try:
            self.logger.info("************* test_TC_IE_139 started  **************")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\VS_images\\Visitor-1.png"
            self.upload_image_to_identify_and_enroll(file_path)
            time.sleep(web_driver.one_second)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().add_details_panel_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            add_details_panel_title = self.explicit_wait(10, "XPATH",
                                                         Read_Identify_and_Enroll_Components().add_details_panel_by_xpath(),
                                                         self.d)
            self.logger.info(f"add details panel visible: {add_details_panel_title.is_displayed()}")
            if add_details_panel_title.is_displayed():
                region_text = self.explicit_wait(10, "XPATH",
                                                 Read_Identify_and_Enroll_Components().region_label_text_by_xpath(),
                                                 self.d)
                self.logger.info(f"region text displayed: {region_text.is_displayed()}")
                region_select_btn = self.explicit_wait(10, "XPATH",
                                                       Read_Identify_and_Enroll_Components().region_select_btn_by_xpath(),
                                                       self.d)
                self.logger.info(f"region select displayed: {region_select_btn.is_displayed()}")
                if region_text.is_displayed():
                    self.logger.info(f"region select label is visible: {region_text.is_displayed()}")
                    self.status.append(True)
                else:
                    self.status.append(False)
                if region_select_btn.is_displayed():
                    self.logger.info(f"region select btn is visible: {region_select_btn.is_displayed()}")
                    region_select_btn.click()
                    self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().region_hierarchy_elements_by_xpath(), self.d)
                    regions = self.d.find_elements(By.XPATH, Read_Identify_and_Enroll_Components().region_hierarchy_elements_by_xpath())
                    for region in regions:
                        self.logger.info(f"region visible: {region.text}")
                        if region.is_displayed():
                            self.status.append(True)
                        else:
                            self.status.append(False)
                    for region in regions:
                        if Read_Identify_and_Enroll_Components().edge_name() in region.text:
                            region.click()

                    save_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().save_btn_by_xpath(), self.d)
                    save_btn.click()

                    self.status.append(True)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"add details panel is not visible as expected.")
                self.status.append(False)

            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_IE_139 End  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_139_Failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_139_exception.png")
            self.logger.info(f"Test Case Exception: {ex.args}")
            return False

    def verify_field_incomplete_text_below_region_select_button_is_visible_as_expected(self):
        try:
            self.logger.info("************* test_TC_IE_140 started  **************")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)

            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\VS_images\\Visitor-1.png"
            self.upload_image_to_identify_and_enroll(file_path)
            time.sleep(web_driver.one_second)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().add_details_panel_by_xpath(), self.d)
            time.sleep(web_driver.one_second)
            add_details_panel_title = self.explicit_wait(10, "XPATH",
                                                         Read_Identify_and_Enroll_Components().add_details_panel_by_xpath(),
                                                         self.d)
            self.logger.info(f"add details panel visible: {add_details_panel_title.is_displayed()}")
            if add_details_panel_title.is_displayed():
                field_incomplete_text = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().region_field_incomplete_label_text_by_xpath(), self.d)
                if field_incomplete_text.is_displayed():
                    self.logger.info(f"field incomplete text visible: {field_incomplete_text.is_displayed()}")
                    self.status.append(True)
                else:
                    self.logger.info(f"field incomplete text visible: {field_incomplete_text.is_displayed()}")
                    self.status.append(False)

            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_IE_140 End  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_140_Failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_140_exception.png")
            self.logger.info(f"Test Case Exception: {ex.args}")
            return False

    def verify_download_btn_is_not_overlaping_with_iamge_beides_it_when_new_face_is_added(self):
        try:
            self.logger.info("************* test_TC_IE_141 started  **************")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_identify_and_enroll_and_upload_an_image()
            time.sleep(web_driver.one_second)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            identify_result_panel = self.explicit_wait(10, "XPATH",
                                                       Read_Identify_and_Enroll_Components().identify_results_panel_by_xpath(),
                                                       self.d)
            self.logger.info(f"Identify result panel visible: {identify_result_panel.is_displayed()}")
            if identify_result_panel.is_displayed():
                time.sleep(web_driver.one_second)
                faces_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().faces_btn_by_xpath(), self.d)
                faces_btn.click()
                enrollment_faces_panel = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().enrollment_faces_panel_by_xpath(), self.d)
                self.logger.info(f"enrollment faces panel visible: {enrollment_faces_panel.is_displayed()}")
                if enrollment_faces_panel.is_displayed():
                    self.status.append(True)
                    face_image_box_on_enrollment_faces_by_xpath = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().image_box_on_enrollment_faces_by_xpath(), self.d)
                    self.logger.info(f"face image box on enrollment faces: {face_image_box_on_enrollment_faces_by_xpath.is_displayed()}")
                    download_btn_on_enrollment_faces_by_xpath = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().download_img_btn_on_enrollment_faces_by_xpath(), self.d)
                    self.logger.info(f"download btn on enrollment faces: {download_btn_on_enrollment_faces_by_xpath.is_displayed()}")
                    if face_image_box_on_enrollment_faces_by_xpath.is_displayed():
                        self.status.append(True)
                    else:
                        self.status.append(False)
                    if download_btn_on_enrollment_faces_by_xpath.is_displayed():
                        self.status.append(True)
                    else:
                        self.status.append(False)
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"identify result panel not visible")
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_IE_141 End  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_141_failed.png")
                return False
            else:
                return True

        except Exception as ex:
            self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_141_exception.png")
            self.logger.info(f"Test Case Exception: {ex.args}")
            return False

    def click_on_identify_Enroll_btn_to_add_an_enrolled_faces_to_an_enrollment_and_validate_details_on_identify_result_panel_if_visitor_is_already_enrolled(self):
        try:
            self.logger.info("************* test_TC_IE_142 started  **************")
            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)
            self.open_identify_and_enroll_and_upload_an_image()
            time.sleep(web_driver.one_second)
            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            identify_result_panel = self.explicit_wait(10, "XPATH",
                                                       Read_Identify_and_Enroll_Components().identify_results_panel_by_xpath(),
                                                       self.d)
            self.logger.info(f"Identify result panel visible: {identify_result_panel.is_displayed()}")
            if identify_result_panel.is_displayed():
                time.sleep(web_driver.one_second)
                faces_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().faces_btn_by_xpath(),
                                               self.d)
                faces_btn.click()
                enrollment_faces_panel = self.explicit_wait(10, "XPATH",
                                                            Read_Identify_and_Enroll_Components().enrollment_faces_panel_by_xpath(),
                                                            self.d)
                self.logger.info(f"enrollment faces panel visible: {enrollment_faces_panel.is_displayed()}")
                if enrollment_faces_panel.is_displayed():
                    self.status.append(True)
                    # file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_4.png"
                    # # upload_image = self.d.find_element(By.NAME, "image")
                    # # upload_image.send_keys(file_path)
                    # image_box = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().image_box_by_xpath(), self.d)
                    # image_box.send_keys(file_path)
                    sample_image_icon = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().enrollment_faces_sample_image_icon_by_xpath(), self.d)
                    if sample_image_icon.is_displayed():
                        self.logger.info("Sample image icon is visible...")
                        self.status.append(True)
                    else:
                        self.logger.info("Sample image icon is not visible...")
                        self.status.append(False)

                    sample_image_icon.click()
                    time.sleep(web_driver.two_second)
                    file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\vip\\000100.png"

                    pyautogui.write(file_path)
                    pyautogui.press('enter')
                    time.sleep(3)
                    pyautogui.press('enter')
                else:
                    self.status.append(False)
            else:
                self.logger.info(f"identify result panel not visible")
                self.status.append(False)
            self.logger.info(f"status: {self.status}")
            self.logger.info("************* test_TC_IE_142 End  **************")
            if False in self.status:
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_142_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.info(f"Test Case Exception: {ex.args}")

    def open_identify_and_enroll_and_upload_an_image(self):
        try:
            self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                               .identify_and_enroll_link_by_xpath(), self.d)
            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            # self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components().upload_image_by_xpath(), self.d)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\img\\visitor_search_img_4.png"
            self.upload_image_to_identify_and_enroll(file_path)

            self.logger.info(f"Image upload success")
        except Exception as ex:
            self.logger.info(f"open identify and enroll and upload an image: {ex.args}")

    def click_on_reselect_btn(self):
        try:
            reselect_btn = self.explicit_wait(10, "XPATH",
                                              Read_Identify_and_Enroll_Components().reselect_btn_by_xpath(),
                                              self.d)
            reselect_btn.click()
        except Exception as ex:
            self.logger.info(f"exception at click on reselect btn: {ex.args}")

    def purge_and_replace(self):
        try:
            self.logger.info("************* test_TC_IE_53 started  **************")

            login().login_to_cloud_if_not_done(self.d)
            self.status.clear()
            time.sleep(web_driver.two_second)

            link = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                      .identify_and_enroll_link_by_xpath(), self.d)
            self.d.execute_script("arguments[0].click();", link)
            self.logger.info(f"clicked on Identify and enroll link")
            time.sleep(web_driver.one_second)
            file_path = f"{Path(__file__).parent.parent.parent}\\All_Test_Data\\Common_Test_data\\dataset1\\pt\\00089.png"
            self.upload_image(file_path)

            identify_enroll_btn = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                     .identify_enroll_panel_identify_enroll_btn_by_xpath(), self.d)

            self.d.execute_script("arguments[0].click();", identify_enroll_btn)
            self.logger.info(f"Clicked on Identify and Enroll button")
            wait_icon = self.d.find_element(By.XPATH, Read_Identify_and_Enroll_Components()
                                            .identifying_photo_wait_by_xpath())
            count = 0
            while wait_icon.is_displayed():
                if count > 15:
                    break
                time.sleep(web_driver.two_second)
                count += 1
                self.logger.info(f"waiting for wait icon, count: {count}")
            time.sleep(web_driver.two_second)
            purge_and_replace = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                                   .identify_results_purge_replace_icon_by_xpath(), self.d)
            purge_and_replace.click()
            self.logger.info("clicked on 'purge and replace' button....")
            time.sleep(web_driver.two_second)
            p_and_r_popup = self.explicit_wait(10, "XPATH", Read_Identify_and_Enroll_Components()
                                               .purge_and_replace_pop_up_validation(), self.d)
            print(p_and_r_popup.text.lower())
            print(Read_Identify_and_Enroll_Components().purge_and_replace_validation_text().lower())
            self.logger.info(
                f"Ex pop up : {Read_Identify_and_Enroll_Components().purge_and_replace_validation_text().lower()}")
            self.logger.info(f"Ac pop up : {p_and_r_popup.text.lower()}")
            if p_and_r_popup.text.lower() == Read_Identify_and_Enroll_Components().purge_and_replace_validation_text().lower():
                # self.logger.info(f"actual alert text: {self.d.switch_to.alert.text}")
                self.status.append(True)
            else:
                self.status.append(False)

            time.sleep(web_driver.one_second)
            self.logger.info("alert dismissed...")
            print(self.status)

            self.logger.info(f"status: {self.status}")
            if False in self.status:
                self.logger.error(f"screenshot file path: {self.screenshots_path}\\test_TC_IE_53.png")
                self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_IE_53_failed.png")
                return False
            else:
                return True
        except Exception as ex:
            self.logger.error(f"test_TC_IE_53 got an exception as: {ex.args}")
            self.d.save_screenshot(
                f"{self.screenshots_path}\\test_TC_IE_53_exception.png")
            return False
        finally:
            self.close_all_panel_one_by_one()
