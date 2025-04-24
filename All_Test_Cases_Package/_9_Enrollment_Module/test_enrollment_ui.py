import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from  All_POM_Packages._11_Enrollment_module_POM.Enrollments_Filter_combination_POM import Enrollments_Filter_combination_pom


@pytest.mark.run(order=12)
class Test_enrollment_ui(web_driver):
    user_list = None
    d = web_driver.d()
    results = list()
    logger = web_logger.logger_obj()
    logger.info(" ******** enrollment_ui (Order - 12) Begin ********")

    # @pytest.mark.p2
    # def test_TC_EFC_001(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_no_filter_criteria():
    #         assert True
    #     else:
    #         assert False
