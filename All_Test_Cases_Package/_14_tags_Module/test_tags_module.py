
import pytest
# from All_POM_Packages._9_tags_module_POM.Tags_Module_POM import Tags_Module_pom
from All_POM_Packages._9_tags_module_POM.Tags_Module_POM import Tags_Module_pom
from Base_Package.Web_Logger import web_logger
from Base_Package.Web_Driver import web_driver


@pytest.mark.run(order=13)
class Test_Tags_Module(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Tags_Module (Order - 13) Begin ********")
    print("******** Tags_Module (Order - 13) Begin ********")

    @pytest.mark.p1
    def test_TC_TAG_01(self):

        if Tags_Module_pom().create_tags_for_serious_event():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_TAG_02(self):
        if Tags_Module_pom().create_tags_for_non_serious_event():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_TAG_05(self):
        if Tags_Module_pom().duplicate_tags_not_create_validation():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_TAG_06(self):
        if Tags_Module_pom().Verify_tags_name_edit_functionality():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_TAG_07(self):
        if Tags_Module_pom().delete_all_tags():
            assert True
        else:
            assert False