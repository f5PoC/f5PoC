import core.pages as pages
from tests.base_test import BaseTest


class TestCareersPage(BaseTest):
    def test_qa_position(self):
        main_page = pages.MainPage(self.driver)
        assert main_page.is_url_matches()
        assert main_page.is_title_matches()

        careers_page = main_page.navigate_careers_page()
        assert careers_page.is_url_matches()
        assert careers_page.is_title_matches()

        qa_position_page = careers_page.find_qa_position()
        assert qa_position_page.is_url_matches()
        assert qa_position_page.is_title_matches()
        assert qa_position_page.is_apply_button_present()
