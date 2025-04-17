import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._7_Visitor_Search_Module_POM.Visitor_Search_Module_POM import Visitor_Search_Module_pom


@pytest.mark.run(order=10)
class Test_Visitor_Search_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Visitor_Search (Order - 7) Begin ********")
    print("******** Visitor_Search (Order - 7) Begin ********")

    @pytest.mark.p1
    def test_TC_VS_059(self):
        if Visitor_Search_Module_pom().Verify_Visitor_search_with_no_criteria_selection_should_display_error_message_above_search_menu_as_Error_Meta_data_only_search_should_target_a_single_store():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_VS_069(self):
        if Visitor_Search_Module_pom().Verify_visitor_search_with_Date_range_and_Org_Hierarch_Selection_should_list_the_visitors_in_selected_date_range_and_belongs_to_selected_Org_Hierarchy_Selection_sorted_by_date_time_in_ascending_order_():
            assert True
        else:
            assert False

