import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._20_Insight_Dashboard_Module_POM.Insight_Dashboard_POM import insight_dashboard_pom


@pytest.mark.run(order=21)
class Test_insight_dashboard_test_cases(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** Insight Dashboard (Order - 21) Begin ********")
    print("******** Insight Dashboard (Order - 21) Begin ********")

    @pytest.mark.p1
    def test_TC_InDB_36(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_loss_prevented_by_enrollment_group_counts():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_InDB_33(self):
        if insight_dashboard_pom().Verify_user_is_able_to_see_counts_on_overview_dashboard_as_total_loss_prevented_5500_active_enrollment_25_total_match_events_25_visito_searches_0_investgation_saving_time_0_repeat_people_of_interest_0():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_InDB_154(self):
        if insight_dashboard_pom().Verify_user_able_to_select_the_Probable_Match_Events_Dashbaord_from_the_Dashbaord_dropdown_list_and_switched_to_Probabel_Match_Events_Dashboard():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_InDB_358(self):
        if insight_dashboard_pom().Verify_clicking_on_Enrollment_Dashbaord_Should_launch_the_Enrollment_Dashbaord():
            assert True
        else:
            assert False

    # ********************************************* P1 Completed ****************************************************
