from selenium.webdriver.common.by import By


class MainPageLocators:
    CAREERS_BUTTON = (By.XPATH, '//li/a[@href="/en/web/about_global/careers"]')


class CareersPageLocators:
    CAREERS_DROPDOWN = (By.XPATH, '//a[contains(@href, "/about_global/careers") and  @class ="dropdown-toggle"]')
    JOB_OPENINGS_BUTTON = (By.XPATH, '//a[contains(@href, "/careers/job-openings")]')
    SELECT_CITY_DROPDOWN = (By.ID, 'job-city')
    VIEW_JOB_BUTTON = (By.XPATH, '//a[contains(@data-track-name , "Frontend Software Engineer") and text()="View job"]')


class PositionPageLocators:
    APPLY_BUTTON = (By.XPATH, '//a[contains(span/text(), "interested")]')
