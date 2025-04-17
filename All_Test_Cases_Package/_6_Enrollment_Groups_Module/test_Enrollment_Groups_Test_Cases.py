import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._5_Enrollment_Groups_Module_POM.Enrollment_Groups_Module_POM import Enrollments_Groups_Module_pom


@pytest.mark.run(order=6)
class Test_Enrollment_Groups_Module(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Enrollment_Groups_Module (Order - 5) Begin ********")
    print("******** Enrollment_Groups_Module (Order - 5) Begin ********")

    @pytest.mark.p1
    def test_TC_EG_01(self):
        self.logger.info("Enrollment Groups module = test_TC_EG_01 execution started..")
        if Enrollments_Groups_Module_pom().verify_Enrollment_Groups_submenu_is_visible_and_enabled_in_cloud_menu():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_EG_02(self):
        self.logger.info("Enrollment Groups module = test_TC_EG_02 execution started..")
        if Enrollments_Groups_Module_pom().verify_user_click_on_enrollment_groups_enrollment_groups_panel_is_displayed():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_EG_05(self):
        self.logger.info("Enrollment Groups module = test_TC_EG_05 execution started..")
        if Enrollments_Groups_Module_pom().verify_action_button_is_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_EG_26(self):
        self.logger.info("Enrollment Groups module = test_TC_EG_26 execution started..")
        if Enrollments_Groups_Module_pom().verify_user_fill_the_name_text_box_with_data_click_save_button_then_below_fields_should_be_activated():
            assert True
        else:

            assert False

    @pytest.mark.p1
    def test_TC_EG_27(self):
        self.logger.info("Enrollment Groups module = test_TC_EG_27 execution started..")
        if Enrollments_Groups_Module_pom().verify_user_without_saving_Enrollment_Group_details_panel_below_Enrollments_Notification_Group_Probable_match_Events_should_be_in_disable_mode():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_EG_35(self):
        self.logger.info("Enrollment Groups module = test_TC_EG_35 execution started..")
        if Enrollments_Groups_Module_pom().verify_enrollment_group_details_action_dropdown_has_edit_button_is_visible_and_clickable():
            assert True
        else:
            assert False

    # delete enrollment group is skipped for now
    @pytest.mark.p1
    def test_TC_EG_36(self):
        self.logger.info("Enrollment Groups module = test_TC_EG_36 execution started..")
        if Enrollments_Groups_Module_pom().verify_user_can_delete_any_enrollment_groups_which_has_no_enrollments_linked():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_EG_25(self):
        self.logger.info("Enrollment Groups module = test_TC_EG_25 execution started..")
        if Enrollments_Groups_Module_pom().verify_user_fills_the_Name_text_box_with_any_data_and_click_on_Save_button_then_validation_message_Success_the_group_below_has_been_created_should_display():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_EG_68(self):
        self.logger.info("Enrollment Groups module = test_TC_EG_68 execution started..")
        if Enrollments_Groups_Module_pom().verify_enrollment_groups_functionality_by_filling_name_description_face_threshold_masked_face_threshold_serious_offender_suppress_duplicate_Probable_match_Events_data_it_should_displayed_success_the_group_below_has_been_created_message():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_EG_70(self):
        self.logger.info("Enrollment Groups module = test_TC_EG_70 execution started..")
        if Enrollments_Groups_Module_pom().verify_that_notification_group_should_be_created_from_enrollment_group_module_end_to_end():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_EG_71(self):
        self.logger.info("Enrollment Groups module = test_TC_EG_71 execution started..")
        if Enrollments_Groups_Module_pom().verify_that_Probable_match_Events_should_be_displayed_from_enrollment_group_module_end_to_end():
            assert True
        else:
            assert False

