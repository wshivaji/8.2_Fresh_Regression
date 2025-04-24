import pytest
from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages.SSPR_Module_POM.Sspr_POM import SSPR_pom


@pytest.mark.run(order=21)
class Test_Reporting_Module_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** SSPR_Module (Order - 21) Begin ********")
    print("******** SSPR_Module (Order - 21) Begin ********")

    @pytest.mark.p1
    def test_TC_SSPR_02(self):
        if SSPR_pom().open_portal_login_page_enter_username_password_and_click_on_login_btn_verify_password_reset_pop_up_displayed():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_SSPR_08(self):
        if SSPR_pom().verify_password_length_should_not_accept_less_than_8():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_SSPR_09(self):
        if SSPR_pom().verify_password_combination_alphabets_capital_small_digits_and_symbol_accepted_successfully():
            assert True
        else:
            assert False
