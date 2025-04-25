from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages.System_Level_Test.System_Level_Test_POM import System_Level_Test_pom
import pytest


@pytest.mark.run(order=3)
class Test_System_Level_Test_testcases(web_driver, web_logger):
    d = web_driver.d
    logger = web_logger.logger_obj()
    logger.info(" ******** System_Level_Test_Module (Order - 3) Begin ********")
    print("******** System_Level_Test_Module (Order - 3) Begin ********")

    @pytest.mark.p1
    def test_TC_SLT_1(self):
        if System_Level_Test_pom().creating_five_user_roles():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_SLT_2(self):
        if System_Level_Test_pom().creating_dummy_user_with_firstname_lastname_user_role_password_region_email_timezone_display_success_msg():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_SLT_3(self):
        if System_Level_Test_pom().creating_dummy_Notification_Groups_Functionality_by_filling_Name_and_Description_data_it_should_displayed_Success_the_alert_below_has_been_created_message():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_SLT_4(self):
        if System_Level_Test_pom().creating_dummy_enrollment_group_by_filling_name_description_data_success_message():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_SLT_5(self):
        if System_Level_Test_pom().users_notification_group_enrollment_group_bottom_up_integration():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_SLT_6(self):
        if System_Level_Test_pom().enrollment_group_notification_group_users_top_down_integration():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_SLT_7(self):
        if System_Level_Test_pom().Creating_Notification_Group_from_Users_panel():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_SLT_8(self):
        if System_Level_Test_pom().Creating_User_and_Enrollment_Group_from_Notification_Group_panel():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_SLT_9(self):
        if System_Level_Test_pom().Creating_Notification_Group_and_User_from_Enrollment_Group_panel():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_SLT_10(self):
        if System_Level_Test_pom().Verify_visitor_enrollment_successfully_done_from_Visitor_Search_Results_for_visitor_with_image_for_all_edges_present():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_SLT_11(self):
        if System_Level_Test_pom().Verify_visitor_enrollment_successfully_done_from_Visitor_Search_Results_for_visitor_with_meta_data_for_all_edges_present():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_SLT_12(self):
        if System_Level_Test_pom().Verify_visitor_enrollment_successfully_done_from_Visitor_Search_Results_for_visitor_with_image_and_meta_data_for_all_edges_present():
            assert True
        else:
            assert False
