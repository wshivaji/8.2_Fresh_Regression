from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._3_User_Roles_Module_POM.User_Roles_Module_POM import user_roles_module_pom
import pytest


@pytest.mark.run(order=4)
class Test_User_Roles_Test_Cases(web_driver, web_logger):
    # d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** User_Roles (Order - 4) Begin ********")
    print("******** User_Roles (Order - 4) Begin ********")

    @pytest.mark.p1
    def test_TC_UR_20(self):
        self.logger.info("***************** test_TC_UR_20 *****************")
        if user_roles_module_pom().enter_user_role_details_and_click_on_Save_btn_and_verify_user_role_with_given_name_is_created_successfully():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_UR_70(self):
        self.logger.info("***************** test_TC_UR_23 *****************")
        if user_roles_module_pom().Verify_User_role_deletion_functionality_by_deleting_one_user_role():
            assert True
        else:
            assert False
