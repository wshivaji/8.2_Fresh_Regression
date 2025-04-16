import pytest
from All_POM_Packages._1_Portal_Login_Module_POM.Portal_Login_Page_POM import Portal_Login_Page_Pom
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger


@pytest.mark.run(order=1)
class Test_Portal_Login_Page_Test_Cases(web_driver, web_logger):
    logger = web_logger.logger_obj()
    logger.info(" ******** Portal_Login_Page (Order - 1) Begin ********")
    print("******** Portal_Login_Page (Order - 1) Begin ********")

    @pytest.mark.p1
    def test_Portal_Login_TC01(self):
        if Portal_Login_Page_Pom().open_portal_url_and_verify_expected_url_is_visible_verify_expected_page_title_is_visible_and_verify_face_first_logo_is_visible():
            assert True
        else:
            assert False

