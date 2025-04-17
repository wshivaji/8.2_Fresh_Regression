from Base_Package.Web_Driver import web_driver
from Base_Package.Web_Logger import web_logger
from All_POM_Packages._18_Reporting_Module.Reporting_POM import Reporting_pom
from All_POM_Packages._18_Reporting_Module.Reporting_Events_POM import Reporting_Events_pom
import pytest


@pytest.mark.run(order=19)
class Test_Reporting_Module_Test_Cases(web_driver, web_logger):
    d = web_driver.d()
    logger = web_logger.logger_obj()
    logger.info(" ******** Reporting_Module (Order - 19) Begin ********")
    print("******** Reporting_Module (Order - 19) Begin ********")

    @pytest.mark.p1
    def test_TC_Reporting_EN_ZN_033(self):
        if Reporting_pom().Verify_individual_report_for_number_of_enrollments_by_zone_with_date_range_with_group_selected_as_SOE_ABE_PTE_FRAUDE_and_VIPE():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Reporting_ZN_EN_079(self):
        if Reporting_pom().Verify_individual_report_for_number_of_zones_by_enrollment_with_date_range_and_with_groups_as_SOE_ABE_PTE_FRAUDE_VIPE_and_zone_selected_as_All_devices():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Reporting_PME_EN_112(self):
        if Reporting_Events_pom().Verify_individual_report_for_number_of_probable_match_events_by_enrollment_with_date_range_and_with_group_selected_as_SOE_ABE_PTE_FRAUDE_and_VIPE():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Reporting_PME_HD_158(self):
        if Reporting_Events_pom().Verify_individual_report_for_number_of_probable_match_events_by_hour_of_day_with_date_range_and_with_groups_as_SOE_ABE_PTE_FRAUDE_VIPE_and_zone_selected_as_All_devices():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Reporting_PME_DW_204(self):
        if Reporting_Events_pom().Verify_individual_report_for_number_of_probable_match_events_by_day_of_week_with_date_range_and_with_groups_as_SOE_ABE_PTE_FRAUDE_VIPE_and_zone_selected_as_All_devices():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Reporting_PME_HW_250(self):
        if Reporting_Events_pom().Verify_individual_report_for_number_of_probable_match_events_by_hour_of_week_with_date_range_and_with_groups_as_SOE_ABE_PTE_FRAUDE_VIPE_and_zone_selected_as_All_devices():
            assert True
        else:
            assert False

    @pytest.mark.p1
    def test_TC_Reporting_PME_ZN_283(self):
        if Reporting_Events_pom().Verify_individual_report_for_number_of_probable_match_events_by_zone_with_date_range_and_with_group_selected_as_SOE_ABE_PTE_FRAUDE_and_VIPE():
            assert True
        else:
            assert False
