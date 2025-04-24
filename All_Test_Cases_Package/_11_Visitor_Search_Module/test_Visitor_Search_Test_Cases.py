import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._7_Visitor_Search_Module_POM.Visitor_Search_Module_POM import Visitor_Search_Module_pom


@pytest.mark.run(order=10)
class Test_Visitor_Search_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Visitor_Search (Order - 10) Begin ********")
    print("******** Visitor_Search (Order - 10) Begin ********")

    @pytest.mark.p1
    def test_TC_Visitor_Search_059(self):
        if Visitor_Search_Module_pom().Verify_Visitor_search_with_no_criteria_selection_should_display_error_message_above_search_menu_as_Error_Meta_data_only_search_should_target_a_single_store():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Visitor_Search_069(self):
        if Visitor_Search_Module_pom().Verify_visitor_search_with_Date_range_and_Org_Hierarch_Selection_should_list_the_visitors_in_selected_date_range_and_belongs_to_selected_Org_Hierarchy_Selection_sorted_by_date_time_in_ascending_order_():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Visitor_Search_080(self):
        if Visitor_Search_Module_pom().Verify_visitor_search_with_image_only_should_list_the_matching_visitors_with_image_sorted_by_Index_Score_in_descending_order_best_to_worst():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Visitor_Search_086(self):
        if Visitor_Search_Module_pom().Verify_visitor_search_with_Image_Date_and_Org_Hierarchy_Selection_should_list_the_matched_visitors_with_search_image_from_selected_Org_Hierarchy_Selection_within_date_range_sorted_by_Index_Score_best_to_worst_order():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Visitor_Search_089(self):
        if Visitor_Search_Module_pom().Verify_visitor_search_with_image_Threshold_and_Max_number_of_Matches_should_list_the_matching_visitors_with_image_having_threshold_more_than_or_equal_to_search_threshold_Search_result_should_contain_selected_count_of_matching_visitors_and_sorted_by_Index_Score_in_descending_order_best_to_worst():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Visitor_Search_093(self):
        if Visitor_Search_Module_pom().Verify_visitor_search_with_Image_Date_range_and_Max_number_of_Matches_search_criteria_should_list_the_result_with_visitors_matched_with_image_in_searched_date_range_Search_result_should_contain_selected_count_of_matching_visitors_sorted_by_Index_Score_in_descending_order_best_to_worst():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Visitor_Search_094(self):
        if Visitor_Search_Module_pom().Verify_visitor_search_with_Image_Date_range_and_Threshold_search_criteria_should_list_the_result_with_visitors_matched_with_image_in_searched_date_range_having_threshold_greater_than_or_equal_to_searched_threshold_and_sorted_by_Index_Score_in_descending_order_best_to_worst():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Visitor_Search_095(self):
        if Visitor_Search_Module_pom().Verify_visitor_search_with_Image_Date_range_Threshold_and_max_number_of_Matches_search_criteria_should_list_the_result_with_visitors_matched_with_image_in_searched_date_range_having_threshold_greater_than_or_equal_to_searched_threshold_Search_result_should_contain_selected_count_of_matching_visitors_and_sorted_by_Index_Score_in_descending_order_best_to_worst():
            assert True
        else:
            assert False
