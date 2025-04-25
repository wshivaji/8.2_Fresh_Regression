import pytest
from All_POM_Packages._6_Notes_Module_POM.Notes_pom import notes_pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=15)
class Test_notes_page_testcases(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** Notes_Module (Order - 14) Begin ********")
    print("******** Notes_Module (Order - 14) Begin ********")

    @pytest.mark.p1
    def test_TC_Notes_03(self):
        if notes_pom().verify_user_able_create_a_note():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Notes_06(self):
        if notes_pom().click_on_Edit_note_on_notes_details_panel_and_verify_notes_is_edited():
            assert True
        else:
            assert False

    @pytest.mark.p2
    def test_TC_Notes_05(self):
        if notes_pom().verify_user_able_to_view_created_notes():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Notes_04(self):
        if notes_pom().verify_user_able_to_delete_a_notes_from_notes_panel():
            assert True
        else:
            assert False
