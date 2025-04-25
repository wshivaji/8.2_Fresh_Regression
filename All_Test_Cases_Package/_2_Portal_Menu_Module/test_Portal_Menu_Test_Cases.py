import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._2_Portal_Menu_Module_POM.Portal_Menu_Module_POM import Portal_Menu_Module_pom


@pytest.mark.run(order=2)
class Test_Portal_Menu_Test_Cases(web_driver, web_logger):
    d = web_driver.d
    logger = web_logger.logger_obj()
    logger.info(" ******** Portal_Menu (Order - 2) Begin ********")
    print("******** Portal_Menu (Order - 2) Begin ********")

    @pytest.mark.p1
    def test_TC_PM_1(self):
        if Portal_Menu_Module_pom().Verify_events_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_2(self):
        if Portal_Menu_Module_pom().Verify_tags_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_3(self):
        if Portal_Menu_Module_pom().Verify_Identify_and_Enroll_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_4(self):
        if Portal_Menu_Module_pom().Verify_Detect_Faces_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_5(self):
        if Portal_Menu_Module_pom().Verify_Enrollments_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_6(self):
        if Portal_Menu_Module_pom().Verify_Enrollment_Groups_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_7(self):
        if Portal_Menu_Module_pom().Verify_Notification_Groups_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_8(self):
        if Portal_Menu_Module_pom().Verify_Visitor_Search_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_9(self):
        if Portal_Menu_Module_pom().Verify_Visitor_Search_Jobs_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_10(self):
        if Portal_Menu_Module_pom().Verify_Notes_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_11(self):
        if Portal_Menu_Module_pom().Verify_Locations_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_12(self):
        if Portal_Menu_Module_pom().Verify_Users_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_13(self):
        if Portal_Menu_Module_pom().Verify_User_Roles_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_14(self):
        if Portal_Menu_Module_pom().Verify_Zones_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_15(self):
        if Portal_Menu_Module_pom().Verify_Account_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_16(self):
        if Portal_Menu_Module_pom().Verify_Reporting_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_18(self):
        if Portal_Menu_Module_pom().Verify_Notifier_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_19(self):
        if Portal_Menu_Module_pom().Verify_Audit_Log_Report_menu_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_20(self):
        if Portal_Menu_Module_pom().click_on_events_menu_tags_menu_and_Identify_and_Enroll_menu_and_verify_Close_All_Panels_menu_is_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_25(self):
        if Portal_Menu_Module_pom().verify_user_able_to_change_password_from_user_panel_by_clicking_edit_user_option_inside_action_dropdown_on_user_panel():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_28(self):
        if Portal_Menu_Module_pom().click_and_verify_logout_btn_is_working_as_expected():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_PM_29(self):
        if Portal_Menu_Module_pom().Verify_Dashboard_menu_visible_and_clickable():
            assert True
        else:
            assert False
