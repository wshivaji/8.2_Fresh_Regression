import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from  All_POM_Packages._11_Enrollment_module_POM.Enrollments_Filter_combination_POM import Enrollments_Filter_combination_pom


@pytest.mark.run(order=12)
class Test_enrollments_search_filter_combination(web_driver):
    user_list = None
    d = web_driver.d()
    results = list()
    logger = web_logger.logger_obj()
    logger.info(" ******** enrollments_search_filter_combination (Order - 12) Begin ********")

    # @pytest.mark.p2
    # def test_TC_EFC_001(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_no_filter_criteria():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_002(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_003(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_004(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_Sort_by_Enrolled_On_criteria():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_005(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_expiration_Date_Range_criteria():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_006(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_expiration_Date_Range_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_007(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_expiration_date_range_and_sort_by_Location_store_criteria():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_008(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_expiration_date_range_and_sort_by_enrolled_On_criteria():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_009(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_enrollment_Date_Range_criteria():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_010(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_enrollment_Date_Range_and_Sort_by_Case_Subject_criteria():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_011(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_enrollment_Date_Range_and_Sort_by_Location_Store_criteria():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_012(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_Enrollment_Date_Range_and_Sort_by_enrolledOn_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_012.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_013(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_Enrollment_Date_Range_and_Expiration_Date_Range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_013.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_014(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_Enrollment_Date_Range_Expiration_Date_Range_and_Sort_by_Case_Subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_014.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_015(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_Enrollment_Date_Range_Expiration_Date_Range_and_Sort_by_Location_Store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_015.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_016(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_Enrollment_Date_Range_Expiration_Date_Range_and_Sort_by_EnrolledOn_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_016.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_017(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_Exact_Text_Search_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_017.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_018(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_Exact_Text_Search_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_018.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_019(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_Exact_Text_Search_and_Sort_by_Location_Store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_019.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_020(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_exact_text_search_and_sort_by_enrolledOn_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_020.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_021(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_exact_text_search_and_expiration_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_021.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_022(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_exact_text_search_expiration_date_range_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_022.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_023(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_exact_text_search_expiration_date_range_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_023.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_024(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_exact_text_search_expiration_date_range_and_Sort_by_EnrolledOn_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_024.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_025(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_exact_text_search_and_enrollment_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_025.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_026(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_exact_text_search_enrollment_date_range_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_026.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_027(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_exact_text_enrollment_date_range_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_027.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_028(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_exact_text_enrollment_date_range_and_sort_by_enrolled_on_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_028.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_029(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_exact_text_enrollment_date_and_expiration_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_029.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_030(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_exact_text_enrollment_expiration_date_range_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_030.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_031(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_exact_text_enrollment_expiration_date_range_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_031.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_032(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_exact_text_enrollment_expiration_date_range_and_sort_by_enrolled_on_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_032.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_033(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_033.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_034(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_034.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_035(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_035.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_036(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_and_sort_by_enrolled_on_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_036.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_037(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_and_expiration_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_037.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_038(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_expiration_date_range_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_038.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_039(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_expiration_date_range_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_039.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_040(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_expiration_date_range_and_sort_by_enrolled_on_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_040.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_041(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_and_enrollment_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_041.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_042(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_enrollment_date_range_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_042.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_043(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_enrollment_date_range_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_043.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_044(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_enrollment_date_range_and_sort_by_enrolled_on_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_044.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_045(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_enrollment_date_and_expiration_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_045.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_046(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_enrollment_expiration_date_range_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_046.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_047(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_enrollment_expiration_date_range_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_047.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_048(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_enrollment_expiration_date_range_sort_by_enrolled_on_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_048.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_049(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_and_exact_text_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_049.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_050(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_exact_text_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_050.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_051(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_exact_text_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_051.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_052(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_exact_text_and_sort_by_enrolled_on_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_052.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_053(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_exact_text_and_expiration_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_053.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_054(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_exact_text_expiration_date_range_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_054.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_055(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_exact_text_expiration_date_range_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_055.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_056(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_exact_text_expiration_date_range_sort_by_enrolled_on_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_056.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_057(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_exact_text_and_enrollment_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_057.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_058(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_exact_text_enrollment_date_range_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_058.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_059(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_exact_text_enrollment_date_range_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_059.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_060(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_exact_text_enrollment_date_range_sort_by_enrolled_on_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_060.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_061(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_exact_text_enrollment_expiration_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_061.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_062(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_case_subject_exact_text_enrollment_expiration_date_range_sort_case_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_062.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_063(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_exact_text_enrollment_expiration_date_range_sort_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_063.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_064(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_case_subject_exact_text_enrollment_expiration_date_range_sort_enrolled_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_064.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_065(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_065.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_066(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_066.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_067(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_067.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_068(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_and_sort_by_enrolled_on_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_068.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_069(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_and_expiration_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_069png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_070(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_expiration_date_range_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_070.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_071(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_expiration_date_range_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_071.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_072(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_expiration_date_range_and_sort_by_enrolled_on_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_072.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_073(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_and_enrollment_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_073.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_074(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_location_store_enrollment_date_range_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_074.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_075(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_location_store_enrollment_date_range_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_075.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_076(self):
    #     if Enrollments_Filter_combination_pom().enrollment_search_with_location_store_enrollment_date_range_and_sort_by_enrolled_on_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_076.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_077(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_enrollment_date_range_and_expiration_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_078.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_078(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_enrollment_date_range_and_expiration_date_range_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_078.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_079(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_enrollment_date_range_and_expiration_date_range_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_079.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_080(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_enrollment_date_range_and_expiration_date_range_and_sort_by_enrolledOn_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_080.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_081(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_and_exact_text_search_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_081.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_082(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_and_exact_text_search_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_082.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_083(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_and_exact_text_search_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_083.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_084(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_and_exact_text_search_and_sort_by_enrolledOn_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_084.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_085(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_exact_text_search_and_expiration_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_085.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_086(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_exact_text_search_expiration_date_range_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_086.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_087(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_exact_text_search_expiration_date_range_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_087.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_088(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_exact_text_search_expiration_date_range_and_sort_by_enrolledOn_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_088.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_089(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_exact_text_search_and_enrollment_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_089.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_090(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_exact_text_search_enrollment_date_range_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_090.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_091(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_exact_text_search_enrollment_date_range_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_091.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_092(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_exact_text_search_enrollment_date_range_and_sort_by_enrolledOn_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_092.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_093(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_location_store_exact_text_search_enrollment_date_range_and_expiration_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_093.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_094(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_exact_text_search_enrollment_date_range_expiration_date_range_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_094.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_095(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_exact_text_search_enrollment_date_range_expiration_date_range_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_095.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_096(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_exact_text_search_enrollment_date_range_expiration_date_range_and_sort_by_enrolledOn_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_096.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_097(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_and_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_097.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_098(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_case_subject_and_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_098.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_099(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_case_subject_and_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_099.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_100(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_case_subject_and_sort_by_enrolledOn_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_100.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_101(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_case_subject_and_expiration_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_101.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_102(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_location_store_case_subject_expiration_date_range_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_102.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_103(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_case_subject_expiration_date_range_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_103.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_104(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_case_subject_expiration_date_range_sort_by_enrolledOn_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_104.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_105(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_location_store_case_subject_Enrollment_date_range_criteria_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_105.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_106(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_location_store_case_subject_Enrollment_date_range_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_106.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_107(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_location_store_case_subject_Enrollment_date_range_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_107.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_108(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_location_store_case_subject_Enrollment_date_range_sort_by_enrolledOn_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_108.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_109(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_location_store_case_subject_EnrollmentDateRange_expiration_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_109.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_110(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_location_store_case_subject_EnrollmentDateRange_expiration_date_range_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_110.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_111(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_location_store_case_subject_EnrollmentDateRange_expiration_date_range_sort_by_location_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_111.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_112(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_location_store_case_subject_EnrollmentDateRange_expiration_date_range_sort_by_enrolledOn_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_112.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_113(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_location_store_case_subject_exact_text_search_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_113.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_114(self):
    #     if Enrollments_Filter_combination_pom().enrollments_search_with_location_store_case_subject_exact_text_search_sort_by_case_subject_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_114.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_115(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_case_subject_exact_text_search_sort_by_location_store_criteria(
    #     ):
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_115.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_116(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_case_subject_exact_text_search_sort_by_enrolledOn_criteria(
    #     ):
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_116.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_117(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_case_subject_exact_text_search_expiration_date_range_criteria(
    #     ):
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_117.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_118(self):
    #     if Enrollments_Filter_combination_pom(). \
    #         enrollments_search_with_location_store_case_subject_exact_text_search_expiration_date_range_sort_by_case_subject_criteria(
    #     ):
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_118.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_119(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_case_subject_exact_text_search_expiration_date_range_sort_by_enrolledOn_criteria(
    #     ):
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_119.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_120(self):
    #     if Enrollments_Filter_combination_pom(). \
    #             enrollments_search_with_location_store_case_subject_exact_text_search_expiration_date_range_sort_by_location_store_criteria(
    #     ):
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_120.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_121(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_case_subject_exact_text_enrollment_date_range_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_121.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_122(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_case_subject_exact_text_enrollment_date_range_sort_case_criteria(
    #
    #     ):
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_122.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_123(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_case_subject_exact_text_enrollment_date_sort_by_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_123.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_124(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_case_subject_exact_text_enrollment_date_sort_enrolled_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_124.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_125(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_case_subject_exact_text_enrollment_expiration_date_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_125.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_126(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_case_subject_exact_text_enrollment_expiration_date_sort_by_case_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_126.png")
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_EFC_127(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_case_subject_exact_text_enrollment_expiration_date_sort_by_store_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_127.png")
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_EFC_128(self):
    #     if Enrollments_Filter_combination_pom() \
    #             .enrollment_search_with_location_store_case_subject_exact_text_enrollment_expiration_date_sort_by_enrolled_on_criteria():
    #         assert True
    #     else:
    #         # self.d.save_screenshot(f"{self.screenshots_path}\\test_TC_EFC_128.png")
    #         assert False

