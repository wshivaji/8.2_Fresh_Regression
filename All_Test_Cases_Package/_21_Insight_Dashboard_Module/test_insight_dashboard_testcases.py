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

    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_03(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_Possible_Match_Events_by_enrollment_action_counts():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_04(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_counts_on_overview_dashboard_organisation_and_individual_groups():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_05(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_loss_prevented_by_enrollment_group_counts_organisation_and_individual_groups():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_06(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_Possible_Match_Events_by_enrollment_action_counts_organisation_and_individual_groups():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_07(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_counts_on_Probable_Match_Events_Dashboard():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_08(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_cumulative_Probable_Match_Events_by_date_todays_date_and_25_count():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_09(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_tagged_vs_untagged_Probable_Match_Events_count_as_tagged_and_untagged():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_10(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_Probable_Match_Events_by_enrollment_groups_counts():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_11(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_tagged_Probable_Match_Events_by_tag_type():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_12(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_counts_on_Probable_Match_Events_dashboard_organisation_and_individual_groups():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_13(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_cumulative_Probable_Match_Events_by_date_organisation_and_individual_group():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_14(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_tagged_vs_untagged_Probable_Match_Events_count_organisation_and_individual_groups():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_15(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_Probable_Match_Events_by_enrollment_groups_counts_organisation_and_individual_groups():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_16(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_tagged_Probable_Match_Events_by_tag_type_organisation_and_individual_groups():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_17(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_on_enrollment_dashboard_as_enrollment_overview_and_cumulative_enrollments_by_date_as_mention_is_link():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_18(self):
    #     if insight_dashboard_pom().Verify_enrollment_by_date_counts_on_enrollment_dashboard():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_19(self):
    #     if insight_dashboard_pom().Verify_enrollments_by_enrollment_group_counts_as_mention_in_link():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_20(self):
    #     if insight_dashboard_pom().Verify_enrollments_by_week_org_counts_as_mention_in_link():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_21(self):
    #     if insight_dashboard_pom().Verify_Enrollments_by_status_count():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_22(self):
    #     if insight_dashboard_pom().Verify_user_is_able_to_see_on_enrollment_dashboard_as_enrollment_overview_and_cumulative_enrollments_by_date():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_23(self):
    #     if insight_dashboard_pom().Verify_enrollment_by_date_counts_as_mention_in_link_organisation_and_individual_group():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_24(self):
    #     if insight_dashboard_pom().Verify_enrollments_by_enrollment_group_counts_as_mention_in_link_organisation_and_individual_group():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_25(self):
    #     if insight_dashboard_pom().Verify_enrollments_by_week_counts_as_mention_in_link_organisation_and_individual_groups():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_Insight_Dashboard_26(self):
    #     if insight_dashboard_pom().Verify_Enrollments_by_Status_counts_organisation_and_individual_groups():
    #         assert True
    #     else:
    #         assert False

    # ********************************************* P1 Completed ****************************************************
