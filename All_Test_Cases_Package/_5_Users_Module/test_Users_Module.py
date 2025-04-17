import pytest
from All_POM_Packages._4_Users_Module_POM.Users_Module_POM import Users_Module_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=5)
class Test_Users_Module(web_driver, web_logger):
    logger = web_logger.logger_obj()
    d = web_driver.d()
    logger.info(" ******** Users_Module (Order - 5) Begin ********")
    print("******** Users_Module (Order - 5) Begin ********")

    @pytest.mark.p1
    def test_TC_US_118(self):
        self.logger.info("Users module = test_TC_US_118 execution started")
        if Users_Module_pom().user_fills_username_firstname_lastname_user_role_password_region_email_timezone_display_success_msg():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_119(self):
        self.logger.info("Users module = test_TC_US_119 execution started")
        if Users_Module_pom().verify_user_able_to_create_a_new_user_by_filling_only_mandatory_fields():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_120(self):
        self.logger.info("Users module = test_TC_US_120 execution started")
        if Users_Module_pom().verify_user_able_to_see_all_the_details_filled_for_the_newly_created_user():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_121(self):
        self.logger.info("Users module = test_TC_US_121 execution started")
        if Users_Module_pom().Verify_user_able_to_see_all_the_details_filled_for_the_newly_created_user():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_127(self):
        self.logger.info("Users module = test_TC_US_127 execution started")
        if Users_Module_pom().user_able_to_see_the_newly_created_users_details_username_firstname_lastname_email_under_users_panel():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_139(self):
        self.logger.info("Users module = test_TC_US_139 execution started")
        if Users_Module_pom().verify_user_able_to_edit_the_details_for_the_newly_created_user_details():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_140(self):
        self.logger.info("Users module = test_TC_US_140 execution started")
        if Users_Module_pom().verify_user_able_to_delete_the_newly_created_user():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_183(self):
        self.logger.info("Users module = test_TC_US_183 execution started")
        if Users_Module_pom().click_on_edit_alert_schedule_make_some_changes_and_save_new_changes_and_verify_alert_schedule_changes_are_saved_successfully():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_197(self):
        self.logger.info("Users module = test_TC_US_197 execution started")
        if Users_Module_pom().Verify_new_user_can_be_created_without_selecting_store_group():
            assert True
        else:
            assert False
