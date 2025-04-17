import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages.Store_Groups_Module_POM.Store_Groups_Module_POM import Store_Groups_Module_pom


class Test_Portal_Smoke_Test_Cases(web_driver, web_logger):
    logger = web_logger.logger_obj()

    @pytest.mark.p1
    def test_TC_SG_01(self):
        if Store_Groups_Module_pom().Verify_Store_Groups_appears_in_portal_web_menu_only_if_logged_in_user_holds_Store_Group_and_Configuration_Permisisons_in_userroles():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_SG_15(self):
        if Store_Groups_Module_pom().Verify_admin_user_able_to_create_store_group_successfully_by_entering_required_fields_such_as_Name_and_Location_Verify_user_able_to_see_success_message_as_Success_A_store_group_has_been_created():
            assert True
        else:
            assert False
