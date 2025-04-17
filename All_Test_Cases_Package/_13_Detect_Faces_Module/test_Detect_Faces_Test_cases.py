import pytest
from All_POM_Packages._8_Detect_Faces_Module_POM.Detect_Faces_pom import detect_faces_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from Base_Package.Login_Logout_Ops import login, logout


@pytest.mark.run(order=9)
class Test_detect_faces_testcases(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** detect_faces (Order - 11) Begin ********")
    print("******** detect_faces (Order - 11) Begin ********")



    @pytest.mark.p3
    def test_TC_DF_01(self):
        if detect_faces_pom().Click_on_Detect_Faces_menu_and_verify_it_is_navigating_to_Detect_Faces_panel_verify_panel_heading_is_visible_as_expected():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_DF_08(self):
        if detect_faces_pom().upload_a_image_having_more_no_of_faces_verify_banner_showing_number_of_faces_on_a_image():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_DF_22(self):
        if detect_faces_pom().on_image_quality_page_In_action_dropdown_click_on_identify_within_enrollments_Identify_and_enroll_page_is_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_DF_23(self):
        if detect_faces_pom().In_identify_and_enroll_page_if_person_is_already_enrolled_identify_results_page_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_Detect_faces_Tc_032(self):
        if detect_faces_pom().on_image_quality_page_click_on_identify_within_visitors_inside_Action_dropdown_and_perform_visitor_search():
            assert True
        else:
            assert False