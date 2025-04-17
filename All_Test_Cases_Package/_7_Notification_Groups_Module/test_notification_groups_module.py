from pathlib import Path
import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._6_Notification_Groups_Module.notification_groups_module_POM import Notification_Groups_Module_pom


@pytest.mark.run(order=7)
class Test_Notification_Groups_Module(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** Notification_Groups_Module (Order - 6) Begin ********")
    print("******** Notification_Groups_Module (Order - 6) Begin ********")
    
    @pytest.mark.p1
    def test_TC_NG_001(self):
        self.logger.info("Notification Groups module = test_TC_NG_001 execution started..")
        if Notification_Groups_Module_pom().Verify_Notification_Groups_submenu_is_visible_and_enabled_in_cloud_menu():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_NG_002(self):
        self.logger.info("Notification Groups module = test_TC_NG_002 execution started..")
        if Notification_Groups_Module_pom().Verify_user_click_on_Notification_Groups_menu_Notification_Groups_panel_is_displayed():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_NG_003(self):
        self.logger.info("Notification Groups module = test_TC_NG_003 execution started..")
        if Notification_Groups_Module_pom().Verify_Notification_Groups_title_is_visible_on_Notification_Groups_panel():
            assert True
        else:
            assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_004(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_004 execution started..")
    #     if Notification_Groups_Module_pom().Verify_Action_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_005(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_005 execution started..")
    #     if Notification_Groups_Module_pom().Verify_Action_button_has_dropdown_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_006(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_006 execution started..")
    #     if Notification_Groups_Module_pom() \
    #             .Verify_Action_dropdown_consist_Create_Notification_Group_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_007(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_007 execution started..")
    #     if Notification_Groups_Module_pom().Verify_Action_dropdown_consist_Delete_Selected_Notification_Groups_From_System_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_008(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_008 execution started..")
    #     if Notification_Groups_Module_pom().Verify_Action_dropdown_consist_Refresh_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_009(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_009 execution started..")
    #     if Notification_Groups_Module_pom().Verify_user_click_on_Create_Notification_Group_Notification_Group_Details_panel_should_be_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_010(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_010 execution started..")
    #     if Notification_Groups_Module_pom().Verify_user_click_on_Create_Notification_Group_pop_up_panel_title_is_Notification_Group_Details():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_011(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_011 execution started..")
    #     if Notification_Groups_Module_pom().Verify_Notification_Group_Cancel_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_012(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_012 execution started..")
    #     if Notification_Groups_Module_pom().Verify_Notification_Group_Save_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_NG_013(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_013 execution started..")
    #     if Notification_Groups_Module_pom().Verify_Notification_Group_NOTIFICATION_GROUP_DETAILS_sub_title_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_NG_014(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_014 execution started..")
    #     if Notification_Groups_Module_pom().Verify_Name_text_and_Name_textbox_field_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_NG_015(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_015 execution started..")
    #     if Notification_Groups_Module_pom().Verify_Description_text_and_Description_text_box_field_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_NG_016(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_016 execution started..")
    #     if Notification_Groups_Module_pom().Verify_validation_message_Missing_required_parameter_is_populated_when_user_click_on_save_button_with_the_blank():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_NG_017(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_017 execution started..")
    #     if Notification_Groups_Module_pom().Verify_user_fills_the_Name_text_box_with_data_and_click_on_Save_button_then_validation_message_Success_the_alert_below_has_been_created_should_populate():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_018(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_018 execution started..")
    #     if Notification_Groups_Module_pom().Verify_user_fill_the_name_text_box_with_data_and_click_Save_button_then_below_fields_Users_Enrollment_Groups_Events_should_be_activated():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_019(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_019 execution started..")
    #     if Notification_Groups_Module_pom().Verify_Notification_Group_Details_panel_while_creating_Notification_Group_below_Users_Enrollment_Groups_Events_should_be_in_disable_mode():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_020(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_020 execution started..")
    #     if Notification_Groups_Module_pom() .Verify_user_click_on_Delete_Groups_From_System_option_without_selecting_the_check_box_it_should_display_a_popup_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_021(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_021 execution started..")
    #     if Notification_Groups_Module_pom().Verify_user_click_on_Refresh_button_Notification_Group_page_should_get_refreshed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_022(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_022 execution started..")
    #     if Notification_Groups_Module_pom().Verify_SELECT_ALL_check_box_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_NG_023(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_023 execution started..")
    #     if Notification_Groups_Module_pom() \
    #             .Verify_user_clicks_on_SELECT_ALL_check_box_all_the_below_check_boxes_should_get_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_NG_024(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_024 execution started..")
    #     if Notification_Groups_Module_pom() \
    #             .Verify_user_clicks_on_SELECT_ALL_uncheck_box_all_the_below_check_boxes_should_get_unselected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_NG_025(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_025 execution started..")
    #     if Notification_Groups_Module_pom() \
    #             .Verify_user_fills_the_Name_text_box_with_any_data_and_click_on_Save_button_then_validation_message_Success_the_alert_below_has_been_created_should_populate():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_NG_026(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_026 execution started..")
    #     if Notification_Groups_Module_pom().Verify_Users_button_is_activated_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_NG_027(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_027 execution started..")
    #     if Notification_Groups_Module_pom().Verify_Enrollment_Groups_button_is_activated_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_NG_028(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_028 execution started..")
    #     if Notification_Groups_Module_pom().Verify_Events_button_is_activated_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_NG_029(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_029 execution started..")
    #     if Notification_Groups_Module_pom().Verify_user_click_on_Users_then_Users_panel_should_open():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_NG_030(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_030 execution started..")
    #     if Notification_Groups_Module_pom()\
    #             .Verify_user_click_on_Enrollment_Groups_then_Enrollment_Groups_panel_should_open():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_NG_031(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_031 execution started..")
    #     if Notification_Groups_Module_pom().Verify_user_click_on_Events_then_Events_panel_should_open():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_NG_032(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_032 execution started..")
    #     if Notification_Groups_Module_pom() \
    #             .Verify_Notification_Group_Details_Action_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_033(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_033 execution started..")
    #     if Notification_Groups_Module_pom() \
    #             .Verify_Notification_Group_Details_Action_dropdown_has_Edit_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_034(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_034 execution started..")
    #     if Notification_Groups_Module_pom().Verify_Notification_Groups_Functionality_without_filling_any_data_it_should_displayed_Missing_required_parameter_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_035(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_035 execution started..")
    #     if Notification_Groups_Module_pom() \
    #             .Verify_Notification_Groups_Functionality_by_filling_Description_data_it_should_displayed_Missing_required_parameter_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_NG_036(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_036 execution started..")
    #     if Notification_Groups_Module_pom().Verify_Notification_Groups_Functionality_by_filling_Name_data_it_should_displayed_Success_the_alert_below_has_been_created_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_037(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_037 execution started..")
    #     if Notification_Groups_Module_pom() \
    #             .Verify_Notification_Groups_Functionality_by_filling_Name_and_Description_data_it_should_displayed_Success_the_alert_below_has_been_created_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_038(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_038 execution started..")
    #     if Notification_Groups_Module_pom() \
    #             .Verify_that_when_user_click_on_action_button_dropdown_and_click_on_edit_button_then_Name_and_Description_field_should_appear():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p1
    # def test_TC_NG_039(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_039 execution started..")
    #     if Notification_Groups_Module_pom().Verify_that_user_can_edit_update_Name_field_and_Description_field():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_NG_040(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_040 execution started..")
    #     if Notification_Groups_Module_pom() \
    #             .Verify_that_user_click_on_Cancel_button_then_Name_field_and_Description_field_should_disappear():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_041(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_041 execution started..")
    #     if Notification_Groups_Module_pom().verify_that_users_should_be_created_from_Notification_Group_module():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_042(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_042 execution started..")
    #     if Notification_Groups_Module_pom() \
    #             .verify_that_enrollment_groups_should_be_created_from_notification_group_module():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_NG_043(self):
    #     self.logger.info("Notification Groups module = test_TC_NG_043 execution started..")
    #     if Notification_Groups_Module_pom() \
    #             .verify_that_events_should_be_created_from_notification_group_module():
    #         assert True
    #     else:
    #         assert False
    #
