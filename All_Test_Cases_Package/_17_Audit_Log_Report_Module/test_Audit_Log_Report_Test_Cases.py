
import pytest
# from All_POM_Package.Audit_Log_Reports.Audit_Log_Reports_POM import Audit_log_report_pom
from All_POM_Packages._16_Audit_Log_Report_Module_POM.Audit_Log_Report_Module_POM import Audit_log_report_pom
# from All_Test_Cases_Package.conftest import Base_Class
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=17)
class Test_Audit_Log_Report_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Audit_Log_Report (Order - 17) Begin ********")

    @pytest.mark.p1
    def test_TC_ALR_002(self):
        self.logger.info("Audit Log Report = test_TC_ALR_002 execution started..")
        if Audit_log_report_pom().Verify_user_clicks_on_AuditLogReport_should_open_new_tab_AuditLogReport_page_contains_Select_report_criteria_followed_by_Report_type_filter_by_select_users_and_submit_report_right_to_header():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_ALR_004(self):
        self.logger.info("Audit Log Report = test_TC_ALR_004 execution started..")
        if Audit_log_report_pom().Verify_user1_with_permissions_able_to_view_Audit_log_reports_on_Cloud_menu():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_ALR_009(self):
        self.logger.info("Audit Log Report = test_TC_ALR_009 execution started..")
        if Audit_log_report_pom().Generate_audit_log_report_with_Select_report_criteria_dropdown_buttons():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_ALR_005(self):
        self.logger.info("Audit Log Report = test_TC_ALR_005 execution started..")
        if Audit_log_report_pom().Verify_Report_type_drop_down_appears_with_Aged_Enrollments_wo_Events_Approver_Enrollments_User_Enrollments_Login_Logout_Threshold_changes_and_System_User_Logs():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_ALR_006(self):
        self.logger.info("Audit Log Report = test_TC_ALR_006 execution started..")
        if Audit_log_report_pom().Verify_Filter_date_drop_down_appears_with_Add_date_selection_Custom_Date_Range_Last_7_days_Last_14_days_Last_30_Days_Month_to_date_Last_90_days_Quarter_to_date_Year_to_date():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_ALR_010(self):
        self.logger.info("Audit Log Report = test_TC_ALR_010 execution started..")
        if Audit_log_report_pom().Validate_generated_report_by_providing_all_valid_inputs_to_select_report_criteria():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_ALR_011(self):
        self.logger.info("Audit Log Report = test_TC_ALR_011 execution started..")
        if Audit_log_report_pom().Verify_download_csv_report_by_checking_data_and_text_format_as_shown_in_the_UI_Audit_log_reports_page():
            assert True
        else:
            # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_016_failed.png")
            assert False

    @pytest.mark.p1
    def test_TC_ALR_027(self):
        self.logger.info("Audit Log Report = test_TC_ALR_027 execution started..")
        if Audit_log_report_pom().Verify_generated_report_with_Approver_Enrollments_should_contain_Approver_name_Approver_Date_Time_Enrollment_status_Reported_by_Enrollment_Group_Enrolled_Date_Time_Location_store_Reported_Loss_Enrollment_Event_type_Enrollment_Number():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_ALR_066(self):
        self.logger.info("Audit Log Report = test_TC_ALR_066 execution started..")
        if Audit_log_report_pom().Verify_user_with_all_permissions_enrolled_mask_subject_should_be_in_disable_status_for_user_Enrollment_status():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_ALR_067(self):
        self.logger.info("Audit Log Report = test_TC_ALR_067 execution started..")
        if Audit_log_report_pom().Verify_user_with_all_permissions_enrolled_mask_subject_that_should_be_in_enable_for_Enrollment_status():
            assert True
        else:
            # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_061_failed.png")
            assert False

    @pytest.mark.p1
    def test_TC_ALR_070(self):
        self.logger.info("Audit Log Report = test_TC_ALR_070 execution started")
        if Audit_log_report_pom().Verify_user_with_2FA_enrolled_mask_subject_should_be_in_pending_for_Enrollment_status():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_ALR_071(self):
        self.logger.info("Audit Log Report = test_TC_ALR_071 execution started")
        if Audit_log_report_pom().Verify_user_with_2FA_enrolled_mask_subject_and_approved_by_admin_should_be_in_approved_for_Enrollment_status():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_ALR_156(self):
        self.logger.info("Audit Log Report = test_TC_ALR_156 execution started..")
        if Audit_log_report_pom().Verify_Threshold_changes_report_with_user_modified_threshold_type_for_enrolment_group():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_ALR_157(self):
        self.logger.info("Audit Log Report = test_TC_ALR_157 execution started..")
        if Audit_log_report_pom().Verify_Threshold_changes_report_with_user_modified_threshold_change_result_for_enrolment_group_match():
            assert True
        else:
            # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_135_failed.png")
            assert False

    @pytest.mark.p1
    def test_TC_ALR_158(self):
        self.logger.info("Audit Log Report = test_TC_ALR_158 execution started..")
        if Audit_log_report_pom().Verify_Threshold_changes_report_with_user_modified_serious_offender_change_for_enrolment_group_match():
            assert True
        else:
            # # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_ALR_136_failed.png")
            assert False

