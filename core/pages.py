import time
from abc import abstractmethod, ABC

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from core.config import CAREERS_URL, GLOBAL_TIMEOUT, MAIN_PAGE_URL, QA_POSITION_URL
from core.locators import MainPageLocators, CareersPageLocators, PositionPageLocators
from test_data.position import TEST_DATA


class BasePage(ABC):
    def __init__(self, driver):
        self._driver = driver

    def find_element(self, locator_type, locator, timeout=GLOBAL_TIMEOUT):
        return WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located((locator_type, locator)))

    @abstractmethod
    def is_title_matches(self):
        raise NotImplementedError("Implement method")

    @abstractmethod
    def is_url_matches(self):
        raise NotImplementedError("Implement method")


class MainPage(BasePage):
    def is_url_matches(self):
        return self._driver.current_url == MAIN_PAGE_URL

    def is_title_matches(self):
        # TODO check on Travis. Main page is not always opening correctly!!!
        # Even in normal user mode. DoS protection?
        i = 0
        while (TEST_DATA["main_page_title"] not in self._driver.title) and i < 10:
            self._driver.refresh()
            i += 1
            time.sleep(i)
        return i < 10

    def navigate_careers_page(self):
        careers_button = self.find_element(*MainPageLocators.CAREERS_BUTTON)

        # actions = ActionChains(self._driver)
        # actions.move_to_element(careers_button).perform()
        # If use scroll to element it still element be covered with cookies dialog box and not clickable,
        # it's simpler to scroll wholo window or click with JS.

        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        careers_button.click()
        return CareersPage(self._driver)


class CareersPage(BasePage):
    def is_url_matches(self):
        return self._driver.current_url == CAREERS_URL

    def is_title_matches(self):
        return TEST_DATA["careers_page_title"] in self._driver.title

    def find_qa_position(self):
        job_opening_menu = self.find_element(*CareersPageLocators.CAREERS_DROPDOWN)
        ActionChains(self._driver).move_to_element(job_opening_menu).perform()
        self.find_element(*CareersPageLocators.JOB_OPENINGS_BUTTON).click()

        select_city_dropdown = Select(self.find_element(*CareersPageLocators.SELECT_CITY_DROPDOWN))
        select_city_dropdown.select_by_value(TEST_DATA["position_city"])

        self.find_element(*CareersPageLocators.VIEW_JOB_BUTTON).click()
        self._driver.switch_to.window(self._driver.window_handles[1])  # switch to new window
        return QAPositionPage(self._driver)


class QAPositionPage(BasePage):
    def is_url_matches(self):
        return self._driver.current_url == QA_POSITION_URL

    def is_title_matches(self):
        return TEST_DATA["position_page_title"] in self._driver.title

    def is_apply_button_present(self):
        return self.find_element(*PositionPageLocators.APPLY_BUTTON).is_displayed()
