from pathlib import Path
import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._6_Notification_Groups_Module.notification_groups_module_POM import Notification_Groups_Module_pom


@pytest.mark.run(order=7)
class Test_Notification_Groups_Module(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** Notification_Groups_Module (Order - 6) Begin ********")
    print("******** Notification_Groups_Module (Order - 6) Begin ********")

    @pytest.mark.p1
    def test_TC_NG_002(self):
        self.logger.info("Notification Groups module = test_TC_NG_002 execution started..")
        if Notification_Groups_Module_pom().Verify_user_click_on_Notification_Groups_menu_Notification_Groups_panel_is_displayed():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_NG_017(self):
        self.logger.info("Notification Groups module = test_TC_NG_017 execution started..")
        if Notification_Groups_Module_pom().Verify_user_fills_the_Name_text_box_with_data_and_click_on_Save_button_then_validation_message_Success_the_alert_below_has_been_created_should_populate():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_NG_025(self):
        self.logger.info("Notification Groups module = test_TC_NG_025 execution started..")
        if Notification_Groups_Module_pom().Verify_user_fills_the_Name_text_box_with_any_data_and_click_on_Save_button_then_validation_message_Success_the_alert_below_has_been_created_should_populate():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_NG_029(self):
        self.logger.info("Notification Groups module = test_TC_NG_029 execution started.")
        if Notification_Groups_Module_pom().Verify_user_click_on_Users_then_Users_panel_should_open():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_NG_030(self):
        self.logger.info("Notification Groups module = test_TC_NG_030 execution started..")
        if Notification_Groups_Module_pom().Verify_user_click_on_Enrollment_Groups_then_Enrollment_Groups_panel_should_open():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_NG_031(self):
        self.logger.info("Notification Groups module = test_TC_NG_031 execution started..")
        if Notification_Groups_Module_pom().Verify_user_click_on_Events_then_Events_panel_should_open():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_NG_036(self):
        self.logger.info("Notification Groups module = test_TC_NG_036 execution started..")
        if Notification_Groups_Module_pom().Verify_Notification_Groups_Functionality_by_filling_Name_data_it_should_displayed_Success_the_alert_below_has_been_created_message():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_NG_037(self):
        self.logger.info("Notification Groups module = test_TC_NG_037 execution started..")
        if Notification_Groups_Module_pom().Verify_Notification_Groups_Functionality_by_filling_Name_and_Description_data_it_should_displayed_Success_the_alert_below_has_been_created_message():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_NG_042(self):
        self.logger.info("Notification Groups module = test_TC_NG_042 execution started..")
        if Notification_Groups_Module_pom().verify_that_enrollment_groups_should_be_created_from_notification_group_module():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_NG_043(self):
        self.logger.info("Notification Groups module = test_TC_NG_043 execution started..")
        if Notification_Groups_Module_pom().verify_that_events_should_be_created_from_notification_group_module():
            assert True
        else:
            assert False

