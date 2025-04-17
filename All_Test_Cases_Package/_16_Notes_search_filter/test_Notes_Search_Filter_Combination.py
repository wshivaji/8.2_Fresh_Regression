from pathlib import Path
import pytest
from All_POM_Packages._6_Notes_search_filter_POM.Notes_Search_Filter_Combination_POM import Notes_search_filter_combination_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=16)
class Test_Notes_Search_Filter_Combination(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Notes_Search_Module (Order - 15) Begin ********")
    print("******** Notes_Search_Module (Order - 15) Begin ********")

    @pytest.mark.p2
    def test_TC_NSFC_15(self):
        self.logger.info("test_TC_NSFC_013 execution started..")
        if Notes_search_filter_combination_pom(). \
                Notes_with_Location_Store_CASE_NUMBER_Sortby_Location_Store_and_Sortby_A_to_Zor_Z_to_A_filter_combination_result_should_be_Location_Store_CASENUMBER_Sortby_Location_Store_and_Sorby_A_to_Z_or_Z_to_A():
            assert True
        else:
            # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_NSFC_013.png")
            assert False
