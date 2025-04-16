import sys
import colorsys
import subprocess
from pathlib import Path
import datetime
import pytest


if __name__ == "__main__":

    # ------------------------------------------ regression and p1 - p5 Report Path ---------------------------------

    '''# ************* Report Path *********************'''
    Regression_suit = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\Regression_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p1_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\p1_re-test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p2_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\p2_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p3_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\p3_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p4_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\p4_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    p5_report_path = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\p5_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    # ------------------------------------------------------------------------------------------------------------

    # ------------------------------------------ Individual Module Report path  ---------------------------------
    # ************* Module Wise Report Path **********
    report_path_pl = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\1_portal_login_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_pm = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\2_portal_menu_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_stl = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\3_system_level_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_ur = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\4_user_roles_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_users = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\5_users_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_ng = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\7_Notification_Groups_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_eg = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\6_Enrollment_Groups_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_events = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\10_Events_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_enrollments = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\9_Enrollments_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_detect_faces = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\13_Detect_Faces_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_tags = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\14_Tags_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_ie = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\8_I&E_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_vs = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\11_Visitor_Search_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_vsj = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\12_Visitor_Search_Jobs_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_notes = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\15_Notes_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_alr = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\17_ALR_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_notifier = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\18_Notifier_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_accounts = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\20_Accounts_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_reporting = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\19_Reporting_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_notes_search_filter = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\16_Notes_search_filter_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    report_path_insight_dashboard = f"{Path(__file__).parent}\\Reports\\HTML_Reports\\21_Insight_Dashboard_Module_test_report_{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.html"
    # -----------------------------------------------------------------------------------------------------------
    # --------------------------------- regression and p1 - p5 Test suite path  ---------------------------------
    # ************* test suite path ******************
    Regression_test_suite_path = f"{Path(__file__).parent}\\All_Test_Cases_Package\\"
    p1_test_suite_path = f"{Path(__file__).parent}\\All_Test_Cases_Package\\"
    p2_test_suite_path = f"{Path(__file__).parent}\\All_Test_Cases_Package\\"
    p3_test_suite_path = f"{Path(__file__).parent}\\All_Test_Cases_Package\\"
    p4_test_suite_path = f"{Path(__file__).parent}\\All_Test_Cases_Package\\"
    p5_test_suite_path = f"{Path(__file__).parent}\\All_Test_Cases_Package\\"
    # -----------------------------------------------------------------------------------------------------------
    # --------------------------------- Individual Module Test suite path  ---------------------------------
    test_suite_path_pl = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_1_Portal_Login_Module\\"
    test_suite_path_pm = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_2_Portal_Menu_Module\\"
    test_suite_path_stl = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_3_System_Level_Test\\"
    test_suite_path_ur = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_4_User_Roles_Module\\"
    test_suite_path_users = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_5_Users_Module\\"
    test_suite_path_eg = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_6_Enrollment_Groups_Module\\"
    test_suite_path_ng = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_7_Notification_Groups_Module\\"
    test_suite_path_IE = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_8_Identify_and_Enroll_Module\\"
    test_suite_path_enrollments = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_9_Enrollment_Module"
    test_suite_path_events = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_10_Events_Module"
    test_suite_path_vs = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_11_Visitor_Search_Module\\"
    test_suite_path_vsj = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_12_Visitor_Search_Jobs_Module\\"
    test_suite_path_detect_faces = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_13_Detect_Faces_Module\\"
    test_suite_path_tags = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_14_tags_Module\\"
    test_suite_path_notes = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_15_Notes_Module"
    test_suite_path_notifier = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_18_Notifier_Module"
    test_suite_path_acc = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_20_Account_Module\\"
    test_suite_path_notes_search_filter = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_16_Notes_search_filter"
    test_suite_path_alr = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_17_Audit_Log_Report_Module"
    test_suite_path_reporting = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_19_Reporting_Module"
    test_suite_path_insight_dashboard = f"{Path(__file__).parent}\\All_Test_Cases_Package\\_21_Insight_Dashboard_Module"

    # -----------------------------------------------------------------------------------------------------------
    # --------------------------------- Regression and p1 - p5  Test suite run commands  ------------------------

    # ************************ Commands to Run Test Suite *****************************
    # ************************** P1 Priority Test Run *********************************
    # pytest.main(['-v', '-m', 'p1', f'{Regression_test_suite_path}', '--html', f'{p1_report_path}'])

    # ************************** P2 Priority Test Run *********************************
    # pytest.main(['-v', '-m', 'p2', f'{Regression_test_suite_path}', '--html', f'{p2_report_path}'])

    # ************************** P3 Priority Test Run *********************************
    # pytest.main(['-v', '-m', 'p3', f'{Regression_test_suite_path}', '--html', f'{p3_report_path}'])

    # ************************** P4 Priority Test Run *********************************
    # pytest.main(['-v', '-m', 'p4', f'{Regression_test_suite_path}', '--html', f'{p4_report_path}'])

    # ************************** P5 Priority Test Run *********************************
    # pytest.main(['-v', '-m', 'p5', f'{Regression_test_suite_path}', '--html', f'{p5_report_path}'])

    # ************************** Regression Suite Test Run *********************************
    #pytest.main(['-v', f'{Regression_test_suite_path}', '--html', f'{Regression_suit}'])

    # -----------------------------------------------------------------------------------------------------------
    # --------------------------------- Module wise  Test suite run commands  ------------------------
    # ************************** Module Wise Test Run *********************************
    pytest.main(['-v', f'{test_suite_path_pl}', '--html', f'{report_path_pl}'])
    pytest.main(['-v', f'{test_suite_path_pm}', '--html', f'{report_path_pm}'])
    pytest.main(['-v', f'{test_suite_path_stl}', '--html', f'{report_path_stl}'])
    pytest.main(['-v', f'{test_suite_path_ur}', '--html', f'{report_path_ur}'])
    pytest.main(['-v', f'{test_suite_path_users}', '--html', f'{report_path_users}'])
    pytest.main(['-v', f'{test_suite_path_eg}', '--html', f'{report_path_eg}'])
    pytest.main(['-v', f'{test_suite_path_ng}', '--html', f'{report_path_ng}'])
    pytest.main(['-v', f'{test_suite_path_IE}', '--html', f'{report_path_ie}'])
    pytest.main(['-v', f'{test_suite_path_enrollments}', '--html', f'{report_path_enrollments}'])
    pytest.main(['-v', f'{test_suite_path_events}', '--html', f'{report_path_events}'])
    pytest.main(['-v', f'{test_suite_path_vs}', '--html', f'{report_path_vs}'])
    pytest.main(['-v', f'{test_suite_path_vsj}', '--html', f'{report_path_vsj}'])
    pytest.main(['-v', f'{test_suite_path_detect_faces}', '--html', f'{report_path_detect_faces}'])
    pytest.main(['-v', f'{test_suite_path_tags}', '--html', f'{report_path_tags}'])
    pytest.main(['-v', f'{test_suite_path_notes}', '--html', f'{report_path_notes}'])
    pytest.main(['-v', f'{test_suite_path_notes_search_filter}', '--html', f'{report_path_notes_search_filter}'])
    pytest.main(['-v', f'{test_suite_path_notifier}', '--html', f'{report_path_notifier}'])
    pytest.main(['-v', f'{test_suite_path_insight_dashboard}', '--html', f'{report_path_insight_dashboard}'])
    pytest.main(['-v', f'{test_suite_path_reporting}', '--html', f'{report_path_reporting}'])
    pytest.main(['-v', f'{test_suite_path_acc}', '--html', f'{report_path_accounts}'])
    pytest.main(['-v', f'{test_suite_path_alr}', '--html', f'{report_path_alr}'])


    # ------------------------------------------------------------------------------------------------------------

    # ************* First Run Command p1 written above then re-verify failed tests by running commands below *****
    # *************************** Commands to run only failed test cases second time *****************************
    # ******************* commands below should only run after first execution is completed **********************

    # ***********Re-run Failed p1 tests across all modules *******************
    # pytest.main(['-v', '--lf', '-m', 'p1', f'{Regression_test_suite_path}', '--html', f'{Regression_suit}'])

    # ***********Re-run Failed p2 tests across all modules *******************
    # pytest.main(['-v', '--lf', '-m', 'p2', f'{Regression_test_suite_path}', '--html', f'{p2_report_path}'])

    # ***********Re-run Failed p3 tests across all modules *******************
    # pytest.main(['-v', '--lf', '-m', 'p3', f'{Regression_test_suite_path}', '--html', f'{p3_report_path}'])

    # ***********Re-run Failed p4 tests across all modules *******************
    # pytest.main(['-s', '-q', '--lf', '-m', 'p4', f'{test_suite_path}', '--html', f'{p1_report_path}'])

    # ***********Re-run Failed p5 tests across all modules *******************
    # pytest.main(['-s', '-q', '--lf', '-m', 'p5', f'{test_suite_path}', '--html', f'{p1_report_path}'])

# ******************************************************************************************************************
