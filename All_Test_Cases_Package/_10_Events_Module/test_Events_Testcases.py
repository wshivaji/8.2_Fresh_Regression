import pytest
from All_POM_Packages._10_Events_Module_POM.Events_Pom import events_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
# from All_POM_Package.Events_Module.Events_Pom import events_pom
# from All_Test_Cases_Package.conftest import Base_Class


@pytest.mark.run(order=14)
class Test_eVents_testcases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Events (Order - 10) Begin ********")
    print("******** Events (Order - 10) Begin ********")

    @pytest.mark.p1
    def test_TC_EV_84(self):
        if events_pom().on_Events_tags_panel_click_on_Action_dropdrown_followed_by_Addtags_to_events_selecting_a_checkbox_verify_tagname_is_visible_to_an_event():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_EV_75(self):
        if events_pom().on_Events_tags_panel_click_on_linked_tags_in_filter_dropdown_and_verify_only_linked_tags_are_disiplayed():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_EV_86(self):
        if events_pom().on_Events_tags_panel_click_on_Action_dropdrown_followed_by_Remove_tags_to_events_selecting_a_checkbox_an_alert_is_visible_verify_ok_and_text_on_an_alert():
            assert True
        else:
            assert False
    @pytest.mark.p1
    def test_TC_EV_132(self):
        if events_pom().verify_user_able_to_delete_selected_Probable_Match_Events():
            assert True
        else:
            assert False


