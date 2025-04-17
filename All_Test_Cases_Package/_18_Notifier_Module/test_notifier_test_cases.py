from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._17_Notifier_Module_POM.Notifier_POM import Notifier_pom
import pytest


@pytest.mark.run(order=18)
class Test_Notifier_Module_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Notifier (Order - 17) Begin ********")
    print("******** Notifier (Order - 17) Begin ********")

    @pytest.mark.p1
    def test_TC_Notifier_001(self):
        if Notifier_pom().Verify_Notifier_is_visible_and_clickable_in_dashboard_menu_items_click_on_Notifier_and_verify_it_is_navigating_to_notifier_panel():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Notifier_087(self):
        if Notifier_pom().Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_ABE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Notifier_088(self):
        if Notifier_pom().Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_PTE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Notifier_089(self):
        if Notifier_pom().Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_FRAUDE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Notifier_090(self):
        if Notifier_pom().Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_VIPE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Notifier_091(self):
        if Notifier_pom().Verify_Notifier_result_for_first_camera_of_first_region_selected_with_group_selected_as_SOE_with_Auto_Refresh_Of_events_displayed_as_2_photo_size_as_Medium_and_Sound_Option_as_OFF():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Notifier_092(self):
        if Notifier_pom().Verify_Notifier_result_for_root_region_selected_with_refresh_rate_10_sec_probable_match_events_displayed_as_2_photo_size_as_Medium_Sound_Option_as_ON():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Notifier_095(self):
        if Notifier_pom().Verify_notifier_panel_should_display_LOCATION_with_valid_name():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Notifier_096(self):
        if Notifier_pom().Verify_notifier_panel_should_display_CAMERA_with_valid_data():
            assert True
        else:
            assert False

    def test_TC_Notifier_097(self):
        if Notifier_pom().Verify_notifier_panel_should_display_ENROLLMENT_NUMBER_with_valid_data():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Notifier_098(self):
        if Notifier_pom().Verify_notifier_panel_should_display_ACTION_with_valid_data():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Notifier_100(self):
        if Notifier_pom().Verify_notifier_panel_should_display_INDEX_SCORE_with_valid_data():
            assert True
        else:
            assert False
