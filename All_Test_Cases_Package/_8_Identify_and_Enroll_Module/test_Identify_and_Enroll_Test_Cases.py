
import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._12_Identify_and_Enroll_Module_POM.Identify_and_Enroll_Module_POM import Identify_And_Enroll_POM


@pytest.mark.run(order=8)
class Test_Identify_and_Enroll_Test_Cases(web_driver, web_logger):
    # d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Identify & Enroll (Order - 12) Begin ********")
    print("******** Identify & Enroll (Order - 12) Begin ********")

    @pytest.mark.p1
    def test_TC_IE_01(self):
        if Identify_And_Enroll_POM().Click_on_Identify_Entroll_Option_inside_Cloud_Menu_Local_Menu_and_verify_a_new_panel_is_displayed_with_title_as_Identify_Enroll():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_13(self):
        if Identify_And_Enroll_POM().verify_new_panel_is_displayed_with_title_as_Identify_Results():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_14(self):
        if Identify_And_Enroll_POM().verify_matches_are_found_and_displayed_inside_Identify_Results_panel():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_32(self):
        if Identify_And_Enroll_POM().click_on_download_image_image_verify_visitor_image_is_downloaded_successfully():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_103(self):
        if Identify_And_Enroll_POM().Enter_Data_into_fields_displayed_on_Add_Details_panel_and_verify_enrollment_successfully_created_and_add_details_panel_closed():
            assert True
        else:
            assert False

    def test_TC_IE_104(self):
        if Identify_And_Enroll_POM().verify_Success_message_is_displayed_below_warning_on_Identify_and_enroll_panel():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_106(self):
        if Identify_And_Enroll_POM().click_on_Review_Enrollment_Details_button_and_verify_if_Enrollment_Details_panel_is_displayed():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_107(self):
        if Identify_And_Enroll_POM().verify_Action_button_visible_and_clickable_on_Enrollment_Details_Panel_below_its_title():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_108(self):
        if Identify_And_Enroll_POM().click_and_verify_Edit_Identify_Within_Enrollment_and_Identify_within_visitors_option_are_visible_and_clickable():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_TC_IE_116(self):
        if Identify_And_Enroll_POM().click_on_Review_Added_Groups_Button_and_verify_if_enrollment_groups_panel_is_visible():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_124(self):
        if Identify_And_Enroll_POM().click_on_add_more_faces_button_and_verify_if_Enrollment_Faces_panel_is_displayed():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_126(self):
        if Identify_And_Enroll_POM().verify_Action_button_is_visible_and_clickable_on_Enrollment_Faces_Panel_below_its_title():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_129(self):
        if Identify_And_Enroll_POM().click_on_sample_image_box_and_verify_if_file_open_dialog_box_is_displayed():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_134(self):
        if Identify_And_Enroll_POM().click_on_download_image_button_and_verify_image_is_downloaded_successfully():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_IE_135(self):
        if Identify_And_Enroll_POM().click_on_image_file_info_button_and_verify_a_pop_up_is_displayed_with_image_information():
            assert True
        else:
            assert False