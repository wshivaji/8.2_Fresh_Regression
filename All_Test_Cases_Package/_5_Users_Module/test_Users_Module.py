import pytest
from All_POM_Packages._4_Users_Module_POM.Users_Module_POM import Users_Module_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=5)
class Test_Users_Module(web_driver, web_logger):
    logger = web_logger.logger_obj()
    d = web_driver.d()
    logger.info(" ******** Users_Module (Order - 5) Begin ********")
    print("******** Users_Module (Order - 5) Begin ********")

    # @pytest.mark.p2
    # def test_TC_US_001(self):
    #     self.logger.info("Users module = test_TC_US_001 execution started..")
    #     if Users_Module_pom().verify_user_able_to_view_the_user_on_cloud_menu():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_002(self):
    #     self.logger.info("Users module = test_TC_US_002 execution started..")
    #     if Users_Module_pom().verify_user_opens_user_then_users_panel_should_display():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_003(self):
    #     self.logger.info("Users module = test_TC_US_003 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_and_open_action_dropdown():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_US_004(self):
    #     self.logger.info("Users module = test_TC_US_004 execution started..")
    #     if Users_Module_pom().verify_users_able_to_see_refresh():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_005(self):
    #     self.logger.info("Users module = test_TC_US_005 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_create_user():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_006(self):
    #     self.logger.info("Users module = test_TC_US_006 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_delete_selected_user():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_007(self):
    #     self.logger.info("Users module = test_TC_US_007 execution started..")
    #     if Users_Module_pom().verify_user_clicks_refresh_then_it_should_refresh_the_users_list():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_008(self):
    #     self.logger.info("Users module = test_TC_US_008 execution started..")
    #     if Users_Module_pom().verify_user_clicks_create_user_user_panel_should_be_displayed():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_US_009(self):
    #     self.logger.info("Users module = test_TC_US_009 execution started..")
    #     if Users_Module_pom().verify_title_new_user_details_face_first_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_010(self):
    #     self.logger.info("Users module = test_TC_US_010 execution started..")
    #     if Users_Module_pom().verify_cancel_and_save_button_is_present():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_011(self):
    #     self.logger.info("Users module = test_TC_US_011 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_username_required_text_for_username():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_012(self):
    #     self.logger.info("Users module = test_TC_US_012 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_user_role_required_text_for_user_role():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_013(self):
    #     self.logger.info("Users module = test_TC_US_013 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_able_to_see_password_required_and_confirm_password_required_text_for_password():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_014(self):
    #     self.logger.info("Users module = test_TC_US_014 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_region_required_text_for_region():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_015(self):
    #     self.logger.info("Users module = test_TC_US_015 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_email_required_text_for_email():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_016(self):
    #     self.logger.info("Users module = test_TC_US_016 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_timezone_required_text_for_timezone():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_017(self):
    #     self.logger.info("Users module = test_TC_US_017 execution started..")
    #     if Users_Module_pom().verify_enabled_checkbox_is_selected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_018(self):
    #     self.logger.info("Users module = test_TC_US_018 execution started..")
    #     if Users_Module_pom().verify_user_able_to_select_disabled_checkbox():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_019(self):
    #     self.logger.info("Users module = test_TC_US_019 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_username_textbox_and_fill_username():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_020(self):
    #     self.logger.info("Users module = test_TC_US_020 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_first_name_textbox_and_fill_first_name():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_021(self):
    #     self.logger.info("Users module = test_TC_US_021 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_last_name_textbox_and_fill_last_name():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_022(self):
    #     self.logger.info("Users module = test_TC_US_022 execution started..")
    #     if Users_Module_pom()\
    #             .verify_user_able_to_see_user_role_dropdown_is_present_and_choose_the_user_roles():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_023(self):
    #     self.logger.info("Users module = test_TC_US_023 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_password_textbox_and_fill_password():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_024(self):
    #     self.logger.info("Users module = test_TC_US_024 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_company_textbox_and_enter_their_company_name():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_025(self):
    #     self.logger.info("Users module = test_TC_US_025 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_title_textbox_and_enter_title():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_026(self):
    #     self.logger.info("Users module = test_TC_US_026 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_region_popup_and_choose_a_region():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_027(self):
    #     self.logger.info("Users module = test_TC_US_027 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_department_textbox_and_enter_their_department_name():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_028(self):
    #     self.logger.info("Users module = test_TC_US_028 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_email_textbox_and_enter_a_valid_email():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_029(self):
    #     self.logger.info("Users module = test_TC_US_029 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_alert_email_and_enter_a_valid_alert_email():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_030(self):
    #     self.logger.info("Users module = test_TC_US_030 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_alert_phone_number_and_enter_a_valid_phone_number():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_031(self):
    #     self.logger.info("Users module = test_TC_US_031 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_timezone_dropdown_and_select_a_timezone():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_032(self):
    #     self.logger.info("Users module = test_TC_US_032 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_address_textbox_and_enter_their_address():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_033(self):
    #     self.logger.info("Users module = test_TC_US_033 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_address_2_textbox_and_enter_their_address():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_034(self):
    #     self.logger.info("Users module = test_TC_US_034 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_city_textbox_and_fill_it():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_035(self):
    #     self.logger.info("Users module = test_TC_US_035 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_state_textbox_and_fill_it():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_036(self):
    #     self.logger.info("Users module = test_TC_US_036 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_postal_code_textbox_and_fill_it():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_037(self):
    #     self.logger.info("Users module = test_TC_US_037 execution started..")
    #     if Users_Module_pom()\
    #             .verify_user_able_to_see_house_phone_number_textbox_and_enter_a_valid_phone_number():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_038(self):
    #     self.logger.info("Users module = test_TC_US_038 execution started..")
    #     if Users_Module_pom()\
    #             .verify_users_able_to_see_work_phone_number_textbox_and_enter_a_valid_work_phone_number():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_039(self):
    #     self.logger.info("Users module = test_TC_US_039 execution started..")
    #     if Users_Module_pom().verify_users_able_to_see_fax_phone_number_textbox_and_fill_it():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_040(self):
    #     self.logger.info("Users module = test_TC_US_040 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_phone_type_textbox_and_fill_it():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_041(self):
    #     self.logger.info("Users module = test_TC_US_041 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_phone_provider_dropdown_and_select_the_required_phone_provider():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_042(self):
    #     self.logger.info("Users module = test_TC_US_042 execution started..")
    #     if Users_Module_pom().verify_alert_schedule_is_disabled():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_043(self):
    #     self.logger.info("Users module = test_TC_US_043 execution started..")
    #     if Users_Module_pom().verify_notification_groups_is_disabled():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_044(self):
    #     self.logger.info("Users module = test_TC_US_044 execution started..")
    #     if Users_Module_pom().verify_users_able_to_close_user_panel_on_clicking_cancel_button():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_045(self):
    #     self.logger.info("Users module = test_TC_US_045 execution started..")
    #     if Users_Module_pom().verify_users_able_to_close_users_pane():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_046(self):
    #     self.logger.info("Users module = test_TC_US_046 execution started..")
    #     if Users_Module_pom()\
    #             .verify_user_fills_first_name_and_last_name_then_save_should_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_047(self):
    #     self.logger.info("Users module = test_TC_US_047 execution started..")
    #     if Users_Module_pom()\
    #             .verify_user_fills_first_name_last_name_and_time_zone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_048(self):
    #     self.logger.info("Users module = test_TC_US_048 execution started..")
    #     if Users_Module_pom().verify_user_fills_first_name_last_name_and_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_049(self):
    #     self.logger.info("Users module = test_TC_US_049 execution started..")
    #     if Users_Module_pom()\
    #             .verify_user_fills_first_name_last_name_email_and_time_zone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_050(self):
    #     self.logger.info("Users module = test_TC_US_050 execution started..")
    #     if Users_Module_pom().verify_user_fills_first_name_last_name_and_region_save_display_error_message():
    #         assert True
    #     else:
    #         assert False

    @pytest.mark.p1
    def test_TC_US_051(self):
        self.logger.info("Users module = test_TC_US_051 execution started..")
        if Users_Module_pom()\
                .verify_user_fills_first_name_last_name_region_and_time_zone_save_display_error_message():
            assert True
        else:
            assert False

    # @pytest.mark.p2
    # def test_TC_US_052(self):
    #     self.logger.info("Users module = test_TC_US_052 execution started..")
    #     if Users_Module_pom()\
    #             .verify_user_fills_first_name_last_name_region_and_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_053(self):
    #     self.logger.info("Users module = test_TC_US_053 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_first_name_last_name_region_email_and_time_zone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_054(self):
    #     self.logger.info("Users module = test_TC_US_054 execution started..")
    #     if Users_Module_pom()\
    #             .verify_user_fills_first_name_last_name_and_password_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_055(self):
    #     self.logger.info("Users module = test_TC_US_055 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_first_mame_last_name_password_and_time_zone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_056(self):
    #     self.logger.info("Users module = test_TC_US_056 execution started..")
    #     if Users_Module_pom().verify_user_fills_first_name_last_name_password_and_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_057(self):
    #     self.logger.info("Users module = test_TC_US_057 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_first_name_last_name_password_email_and_time_zone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_058(self):
    #     self.logger.info("Users module = test_TC_US_058 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_first_name_last_name_password_and_region_save_display_error_message():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p2
    # def test_TC_US_059(self):
    #     self.logger.info("Users module = test_TC_US_059 execution started..")
    #     if Users_Module_pom().verify_user_fills_first_name_last_name_password_region_and_time_zone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p2
    # def test_TC_US_060(self):
    #     self.logger.info("Users module = test_TC_US_060 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_first_name_last_name_password_region_and_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_061(self):
    #     self.logger.info("Users module = test_TC_US_061 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_first_last_name_password_region_email_and_time_zone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p2
    # def test_TC_US_062(self):
    #     self.logger.info("Users module = test_TC_US_062 execution started..")
    #     if Users_Module_pom().verify_user_fills_first_name_last_name_and_user_role_save_display_error_message():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p2
    # def test_TC_US_063(self):
    #     self.logger.info("Users module = test_TC_US_063 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_first_name_last_name_user_role_and_time_zone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_064(self):
    #     self.logger.info("Users module = test_TC_US_064 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_first_name_last_name_user_role_and_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p2
    # def test_TC_US_065(self):
    #     self.logger.info("Users module = test_TC_US_065 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_first_name_last_name_user_role_email_and_time_zone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_066(self):
    #     self.logger.info("Users module = test_TC_US_066 execution started..")
    #     if Users_Module_pom().verify_user_fills_first_name_last_name_user_role_and_region_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_067(self):
    #     self.logger.info("Users module = test_TC_US_067 execution started..")
    #     if Users_Module_pom().verify_user_fills_first_name_last_name_user_role_region_and_time_zone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p2
    # def test_TC_US_068(self):
    #     self.logger.info("Users module = test_TC_US_068 execution started..")
    #     if Users_Module_pom().verify_user_fills_first_name_last_name_user_role_region_and_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p2
    # def test_TC_US_069(self):
    #     self.logger.info("Users module = test_TC_US_069 execution started..")
    #     if Users_Module_pom().verify_user_fills_first_name_last_name_user_role_region_email_time_zone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_070(self):
    #     self.logger.info("Users module = test_TC_US_070 execution started..")
    #     if Users_Module_pom().verify_user_fills_first_name_last_name_user_role_and_password_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_071(self):
    #     self.logger.info("Users module = test_TC_US_071 execution started..")
    #     if Users_Module_pom().verify_user_fills_first_name_last_name_user_role_password_and_time_zone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_072(self):
    #     self.logger.info("Users module = test_TC_US_072 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_first_name_last_name_user_role_password_and_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_073(self):
    #     self.logger.info("Users module = test_TC_US_073 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_first_name_last_name_user_role_password_email_time_zone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_074(self):
    #     self.logger.info("Users module = test_TC_US_074 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_first_name_last_name_user_role_password_and_region_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_075(self):
    #     self.logger.info("Users module = test_TC_US_075 execution started..")
    #     if Users_Module_pom() \
    #             .user_fills_first_name_last_name_user_role_password_region_time_zone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_076(self):
    #     self.logger.info("Users module = test_TC_US_076 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_first_name_last_name_user_role_password_region_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_077(self):
    #     self.logger.info("Users module = test_TC_US_077 execution started..")
    #     if Users_Module_pom() \
    #             .user_fills_first_name_last_name_user_role_password_region_email_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_078(self):
    #     self.logger.info("Users module = test_TC_US_078 execution started..")
    #     if Users_Module_pom()\
    #             .verify_user_fills_username_first_name_and_last_name_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_079(self):
    #     self.logger.info("Users module = test_TC_US_079 execution started..")
    #     if Users_Module_pom()\
    #             .verify_user_fills_username_first_name_last_name_and_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_080(self):
    #     self.logger.info("Users module = test_TC_US_080 execution started..")
    #     if Users_Module_pom()\
    #             .verify_user_fills_username_first_name_last_name_and_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_081(self):
    #     self.logger.info("Users module = test_TC_US_081 execution started..")
    #     if Users_Module_pom()\
    #             .user_fills_username_first_name_last_name_email_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_082(self):
    #     self.logger.info("Users module = test_TC_US_082 execution started..")
    #     if Users_Module_pom()\
    #             .verify_user_fills_username_first_name_last_name_and_region_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_083(self):
    #     self.logger.info("Users module = test_TC_US_083 execution started..")
    #     if Users_Module_pom()\
    #             .user_fills_username_first_name_last_name_region_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_084(self):
    #     self.logger.info("Users module = test_TC_US_084 execution started..")
    #     if Users_Module_pom()\
    #             .user_fills_username_first_name_last_name_region_and_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_085(self):
    #     self.logger.info("Users module = test_TC_US_085 execution started..")
    #     if Users_Module_pom().user_fills_username_first_name_last_name_region_email_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_086(self):
    #     self.logger.info("Users module = test_TC_US_086 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_username_first_name_last_name_and_password_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_087(self):
    #     self.logger.info("Users module = test_TC_US_087 execution started..")
    #     if Users_Module_pom() .user_fills_username_first_name_last_name_password_and_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_088(self):
    #     self.logger.info("Users module = test_TC_US_088 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_username_first_name_last_name_password_and_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_089(self):
    #     self.logger.info("Users module = test_TC_US_089 execution started..")
    #     if Users_Module_pom().user_fills_username_first_name_last_name_password_email_and_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_090(self):
    #     self.logger.info("Users module = test_TC_US_090 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_username_first_name_last_name_password_and_region_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_091(self):
    #     self.logger.info("Users module = test_TC_US_091 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_username_first_name_last_name_password_region_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_092(self):
    #     self.logger.info("Users module = test_TC_US_092 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_username_first_name_last_name_password_region_and_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_093(self):
    #     self.logger.info("Users module = test_TC_US_093 execution started..")
    #     if Users_Module_pom() \
    #             .user_fills_username_first_name_last_name_password_region_email_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_094(self):
    #     self.logger.info("Users module = test_TC_US_094 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_username_first_name_last_name_and_user_role_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_095(self):
    #     self.logger.info("Users module = test_TC_US_095 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_username_first_name_last_name_user_role_and_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_096(self):
    #     self.logger.info("Users module = test_TC_US_096 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_username_first_name_last_name_user_role_and_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_097(self):
    #     self.logger.info("Users module = test_TC_US_097 execution started..")
    #     if Users_Module_pom() \
    #             .user_fills_username_first_name_last_name_user_role_email_and_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_098(self):
    #     self.logger.info("Users module = test_TC_US_098 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_username_first_name_last_name_user_role_and_region_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_099(self):
    #     self.logger.info("Users module = test_TC_US_099 execution started..")
    #     if Users_Module_pom() \
    #             .user_fills_username_first_name_last_name_user_role_region_and_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_100(self):
    #     self.logger.info("Users module = test_TC_US_100 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_username_first_name_last_name_user_role_region_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_101(self):
    #     self.logger.info("Users module = test_TC_US_101 execution started..")
    #     if Users_Module_pom() \
    #             .user_fills_username_first_name_last_name_user_role_region_email_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_102(self):
    #     self.logger.info("Users module = test_TC_US_102 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_username_first_name_last_name_user_role_and_password_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_103(self):
    #     self.logger.info("Users module = test_TC_US_103 execution started..")
    #     if Users_Module_pom() \
    #             .user_fills_username_first_name_last_name_user_role_password_and_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_104(self):
    #     self.logger.info("Users module = test_TC_US_104 execution started..")
    #     if Users_Module_pom() \
    #             .verify_user_fills_username_first_name_last_name_user_role_password_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_105(self):
    #     self.logger.info("Users module = test_TC_US_105 execution started..")
    #     if Users_Module_pom() \
    #             .user_fills_username_first_name_lastname_user_role_password_email_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_106(self):
    #     self.logger.info("Users module = test_TC_US_106 execution started..")
    #     if Users_Module_pom() \
    #             .user_fills_username_first_name_last_name_user_role_password_region_save_display_error_message():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_107(self):
    #     self.logger.info("Users module = test_TC_US_107 execution started..")
    #     if Users_Module_pom() \
    #             .user_fills_username_firstname_lastname_user_role_password_region_timezone_save_display_error_message():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p2
    # def test_TC_US_108(self):
    #     self.logger.info("Users module = test_TC_US_108 execution started..")
    #     if Users_Module_pom().user_fills_username_first_name_lastname_user_role_password_region_email_save_display_error_message():
    #         assert True
    #     else:
    #         assert False

    @pytest.mark.p1
    def test_TC_US_118(self):
        self.logger.info("Users module = test_TC_US_118 execution started..")
        if Users_Module_pom().user_fills_username_firstname_lastname_user_role_password_region_email_timezone_display_success_msg():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_119(self):
        self.logger.info("Users module = test_TC_US_119 execution started..")
        if Users_Module_pom().verify_user_able_to_create_a_new_user_by_filling_only_mandatory_fields():
            assert True
        else:
            assert False

    # @pytest.mark.p2
    # def test_TC_US_111(self):
    #     self.logger.info("Users module = test_TC_US_111 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_the_mandatory_details_filled_for_the_newly_created_user():
    #         assert True
    #     else:
    #         assert False

    # @pytest.mark.p2
    # def test_TC_US_120(self):
    #     self.logger.info("Users module = test_TC_US_120 execution started..")
    #     if Users_Module_pom().verify_user_able_to_create_a_new_users_by_filling_all_the_fields():
    #         assert True
    #     else:
    #         assert False

    @pytest.mark.p1
    def test_TC_US_120(self):
        self.logger.info("Users module = test_TC_US_120 execution started..")
        if Users_Module_pom().verify_user_able_to_see_all_the_details_filled_for_the_newly_created_user():
            assert True
        else:
            assert False

    # @pytest.mark.p2
    # def test_TC_US_114(self):
    #     self.logger.info("Users module = test_TC_US_114 execution started..")
    #     if Users_Module_pom().verify_if_user_creates_a_new_users_marked_as_enabled_it_should_reflect_as_enabled():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_115(self):
    #     self.logger.info("Users module = test_TC_US_115 execution started..")
    #     if Users_Module_pom().verify_if_user_creates_a_new_users_marked_as_disabled_it_should_reflect_as_disabled():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_116(self):
    #     self.logger.info("Users module = test_TC_US_116 execution started..")
    #     if Users_Module_pom().verify_the_alert_schedule_is_enabled_after_creating_a_new_user():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_117(self):
    #     self.logger.info("Users module = test_TC_US_117 execution started..")
    #     if Users_Module_pom().verify_user_able_to_open_the_alert_schedule_after_creating_a_new_user():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_118(self):
    #     self.logger.info("Users module = test_TC_US_118 execution started..")
    #     if Users_Module_pom().verify_the_notification_groups_is_enabled_after_creating_a_new_user():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_119(self):
    #     self.logger.info("Users module = test_TC_US_119 execution started..")
    #     if Users_Module_pom().verify_user_able_to_open_the_notification_groups_after_creating_a_new_user():
    #         assert True
    #     else:
    #         assert False

    @pytest.mark.p1
    def test_TC_US_121(self):
        self.logger.info("Users module = test_TC_US_121 execution started..")
        if Users_Module_pom().user_able_to_see_the_newly_created_users_details_username_firstname_lastname_email_under_users_panel():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_121(self):
        self.logger.info("Users module = test_TC_US_121 execution started..")
        if Users_Module_pom().verify_user_able_to_see_if_the_enabled_is_displayed_for_users_marked_as_enabled_under_users_panel():
            assert True
        else:
            assert False

    # @pytest.mark.p2
    # def test_TC_US_122(self):
    #     self.logger.info("Users module = test_TC_US_122 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_if_the_disabled_is_displayed_for_users_marked_as_disabled_under_users_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_123(self):
    #     self.logger.info("Users module = test_TC_US_123 execution started..")
    #     if Users_Module_pom().verify_users_able_to_see_the_notification_groups_icon_for_the_newly_created_user_under_users_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_124(self):
    #     self.logger.info("Users module = test_TC_US_124 execution started..")
    #     if Users_Module_pom().verify_for_newly_created_user_the_hover_text_is_visible_for_notification_groups_under_users_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_125(self):
    #     self.logger.info("Users module = test_TC_US_125 execution started..")
    #     if Users_Module_pom().verify_user_able_to_open_the_notification_groups_for_the_newly_created_user_under_users_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_126(self):
    #     self.logger.info("Users module = test_TC_US_126 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_the_details_icon_for_the_newly_created_user_under_users_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_127(self):
    #     self.logger.info("Users module = test_TC_US_127 execution started..")
    #     if Users_Module_pom().verify_that_for_the_newly_created_user_the_hover_text_is_visible_for_details_icon_under_users_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_128(self):
    #     self.logger.info("Users module = test_TC_US_128 execution started..")
    #     if Users_Module_pom().verify_user_able_to_open_the_details_for_the_newly_created_user_under_users_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_129(self):
    #     self.logger.info("Users module = test_TC_US_129 execution started..")
    #     if Users_Module_pom().verify_user_able_to_see_the_alert_schedule_icon_for_the_newly_created_user_under_users_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_130(self):
    #     self.logger.info("Users module = test_TC_US_130 execution started..")
    #     if Users_Module_pom().verify_for_the_newly_created_user_the_hover_text_is_visible_for_alert_schedule_under_users_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_131(self):
    #     self.logger.info("Users module = test_TC_US_131 execution started..")
    #     if Users_Module_pom().verify_user_able_to_open_the_alert_schedule_for_the_newly_created_user_under_users_panel():
    #         assert True
    #     else:
    #         assert False

    @pytest.mark.p1
    def test_TC_US_132(self):
        self.logger.info("Users module = test_TC_US_132 execution started..")
        if Users_Module_pom().verify_user_able_to_edit_the_details_for_the_newly_created_user_details():
            assert True
        else:
            assert False

    # @pytest.mark.p2
    # def test_TC_US_133(self):
    #     self.logger.info("Users module = test_TC_US_133 execution started..")
    #     if Users_Module_pom().verify_user_able_to_delete_the_newly_created_user():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_134(self):
    #     self.logger.info("Users module = test_TC_US_134 execution started..")
    #     if Users_Module_pom().verify_user_should_not_be_able_to_create_user_which_already_exist():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_135(self):
    #     self.logger.info("Users module = test_TC_US_135 execution started..")
    #     if Users_Module_pom().verify_user_should_not_be_able_to_create_user_if_password_and_confirm_password_does_not_match():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_136(self):
    #     self.logger.info("Users module = test_TC_US_136 execution started..")
    #     if Users_Module_pom().verify_user_able_to_cancel_the_user_creation_after_filling_all_the_details():
    #         assert True
    #     else:
    #         assert False

    @pytest.mark.p1
    def test_TC_US_137(self):
        self.logger.info("Users module = test_TC_US_137 execution started..")
        if Users_Module_pom().verify_when_user_close_user_panel_it_should_display_a_warning_popup():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_138(self):
        self.logger.info("Users module = test_TC_US_138 execution started..")
        if Users_Module_pom().verify_users_sees_go_back_and_close_panel_and_discard_changes_in_warning_popup():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_139(self):
        self.logger.info("Users module = test_TC_US_139 execution started..")
        if Users_Module_pom().verify_user_lands_on_the_same_panel_on_clicking_go_back():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_US_140(self):
        self.logger.info("Users module = test_TC_US_140 execution started..")
        if Users_Module_pom().verify_on_clicking_close_panel_and_discard_changes_user_panel_should_be_closed():
            assert True
        else:
            assert False

    # @pytest.mark.p3
    # def test_TC_US_141(self):
    #     self.logger.info("Users module = test_TC_US_141 execution started..")
    #     if Users_Module_pom().verify_user_is_able_to_open_filter_drop_down_in_notification_group_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_142(self):
    #     self.logger.info("Users module = test_TC_US_142 execution started..")
    #     if Users_Module_pom().verify_the_user_is_able_to_open_action_drop_down_in_notification_group_panel():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_143(self):
    #     self.logger.info("Users module = test_TC_US_143 execution started..")
    #     if Users_Module_pom().verify_user_able_to_assign_the_newly_created_user_to_a_notification_group():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_US_144(self):
    #     self.logger.info("Users module = test_TC_US_144 execution started..")
    #     if Users_Module_pom().verify_company_input_fields_should_not_accept_special_characters():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_145(self):
    #     self.logger.info("Users module = test_TC_US_145 execution started..")
    #     if Users_Module_pom().verify_user_should_not_be_able_to_create_a_user_if_password_value_is_username_firstname_or_lastname():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_146(self):
    #     self.logger.info("Users module = test_TC_US_146 execution started..")
    #     if Users_Module_pom().verify_user_should_not_be_able_to_create_a_user_if_password_value_is_less_than_8_characters():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_147(self):
    #     self.logger.info("Users module = test_TC_US_147 execution started..")
    #     if Users_Module_pom().verify_user_should_not_be_able_to_create_a_user_if_password_value_is_greater_than_20_characters():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_148(self):
    #     self.logger.info("Users module = test_TC_US_148 execution started..")
    #     if Users_Module_pom().verify_user_should_not_be_able_to_create_a_user_if_password_value_is_only_alphabets():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_149(self):
    #     self.logger.info("Users module = test_TC_US_149 execution started..")
    #     if Users_Module_pom().verify_user_should_not_be_able_to_create_a_user_if_password_value_is_only_numbers():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_150(self):
    #     self.logger.info("Users module = test_TC_US_150 execution started..")
    #     if Users_Module_pom().verify_user_should_not_be_able_to_create_a_user_if_password_value_is_only_special_characters():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_151(self):
    #     self.logger.info("Users module = test_TC_US_151 execution started..")
    #     if Users_Module_pom().Verify_if_password_value_is_only_combination_of_alphabet_in_lower_case_and_number():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_152(self):
    #     self.logger.info("Users module = test_TC_US_152 execution started..")
    #     if Users_Module_pom().verify_if_password_value_is_only_combination_of_alphabet_in_lower_case_and_special_characters():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_153(self):
    #     self.logger.info("Users module = test_TC_US_152 execution started..")
    #     if Users_Module_pom().verify_if_password_value_is_only_combination_of_number_and_special_characters():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_154(self):
    #     self.logger.info("Users module = test_TC_US_154 execution started..")
    #     if Users_Module_pom().verify_user_on_clicking_alert_schedule_alert_schedule_panel_pops_up_and_the_title_is_visible():
    #         assert True
    #     else:
    #         assert False

    @pytest.mark.p1
    def test_TC_US_155(self):
        self.logger.info("Users module = test_TC_US_155 execution started..")
        if Users_Module_pom().verify_on_alert_schedule_user_is_able_to_see_the_sub_title_user_alert_schedule():
            assert True
        else:
            assert False

    # @pytest.mark.p3
    # def test_TC_US_156(self):
    #     self.logger.info("Users module = test_TC_US_156 execution started..")
    #     if Users_Module_pom().verify_on_alert_schedule_user_is_able_to_see_schedule_sub_title():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_157(self):
    #     self.logger.info("Users module = test_TC_US_157 execution started..")
    #     if Users_Module_pom().verify_on_alert_schedule_settings_text_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p4
    # def test_TC_US_158(self):
    #     self.logger.info("Users module = test_TC_US_158 execution started..")
    #     if Users_Module_pom().verify_on_alert_schedule_settings_details_and_its_values_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_159(self):
    #     self.logger.info("Users module = test_TC_US_159 execution started..")
    #     if Users_Module_pom().verify_on_alert_schedule_under_schedule_day_and_time_range_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_160(self):
    #     self.logger.info("Users module = test_TC_US_160 execution started..")
    #     if Users_Module_pom().verify_on_alert_schedule_action_drop_down_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_161(self):
    #     self.logger.info("Users module = test_TC_US_161 execution started..")
    #     if Users_Module_pom().on_alert_schedule_click_on_action_dropdown_verify_option_inside_drop_down_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_162(self):
    #     self.logger.info("Users module = test_TC_US_162 execution started..")
    #     if Users_Module_pom().on_alert_schedule_click_on_edit_user_alert_schedule_and_verify_the_panel_should_be_editable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_163(self):
    #     self.logger.info("Users module = test_TC_US_163 execution started..")
    #     if Users_Module_pom().on_alert_schedule_verify_save_and_cancel_button_is_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_164(self):
    #     self.logger.info("Users module = test_TC_US_164 execution started..")
    #     if Users_Module_pom().on_alert_schedule_verify_the_username_is_correct():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p2
    # def test_TC_US_165(self):
    #     self.logger.info("Users module = test_TC_US_165 execution started..")
    #     if Users_Module_pom() .on_alert_schedule_verify_the_time_zone_ID_is_correct():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_166(self):
    #     self.logger.info("Users module = test_TC_US_166 execution started..")
    #     if Users_Module_pom().verify_send_sms_send_mms_send_email_send_in_app_notifications_enable_alerts_Yes_No_button():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_167(self):
    #     self.logger.info("Users module = test_TC_US_167 execution started..")
    #     if Users_Module_pom().on_alert_schedule_under_schedule_verify_the_day_and_checkbox_are_visible_and_clickable():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_168(self):
    #     self.logger.info("Users module = test_TC_US_168 execution started..")
    #     if Users_Module_pom().on_alert_schedule_under_schedule_verify_the_time_range_slider_is_visible():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_169(self):
    #     self.logger.info("Users module = test_TC_US_169 execution started..")
    #     if Users_Module_pom().verify_on_marking_the_days_checkbox_the_time_range_slider_is_enabled():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_170(self):
    #     self.logger.info("Users module = test_TC_US_170 execution started..")
    #     if Users_Module_pom().un_mark_the_days_checkbox_and_verify_the_time_range_slider_is_disabled():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_171(self):
    #     self.logger.info("Users module = test_TC_US_171 execution started..")
    #     if Users_Module_pom().edit_the_settings_send_sms_toggle_it_either_yes_or_no_save_and_verify_the_changes_are_reflected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_172(self):
    #     self.logger.info("Users module = test_TC_US_172 execution started..")
    #     if Users_Module_pom().edit_the_settings_send_mms_toggle_it_either_yes_or_no_save_and_verify_the_changes_are_reflected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_173(self):
    #     self.logger.info("Users module = test_TC_US_173 execution started..")
    #     if Users_Module_pom().edit_the_settings_send_email_toggle_it_either_yes_or_no_save_and_verify_the_changes_are_reflected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_174(self):
    #     self.logger.info("Users module = test_TC_US_174 execution started..")
    #     if Users_Module_pom().edit_the_settings_send_in_app_notifications_toggle_yes_no_save_and_verify_the_changes_are_reflected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_175(self):
    #     self.logger.info("Users module = test_TC_US_175 execution started..")
    #     if Users_Module_pom().edit_the_settings_enable_alerts_toggle_it_either_yes_or_no_save_and_verify_the_changes_are_reflected():
    #         assert True
    #     else:
    #         assert False
    #
    # @pytest.mark.p3
    # def test_TC_US_176(self):
    #     self.logger.info("Users module = test_TC_US_176 execution started..")
    #     if Users_Module_pom().on_alert_schedule_panel_verify_close_panel_button_is_visible_and_clickable_hover_text_is_visible():
    #         assert True
    #     else:
    #         assert False

    @pytest.mark.p1
    def test_TC_US_177(self):
        self.logger.info("Users module = test_TC_US_177 execution started..")
        if Users_Module_pom().on_alert_schedule_panel_click_on_close_panel_button_and_verify_alert_schedule_panel_is_closing():
            assert True
        else:
            assert False
