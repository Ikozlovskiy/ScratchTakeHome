from selenium.webdriver.common.by import By
from swi_browser.browser_interface import BrowserInterface

from tests.shared.pages.base_page import BasePage


class MenuBar(BasePage):

    file = (By.XPATH,
            "//span[@class='menu-bar_collapsible-label_o2tym']"
            "/span[text()='File']")
    file_option = (lambda option: (
        By.XPATH, f"//li[@class='menu_menu-item_3EwYA "
                  f"menu_hoverable_3u9dt menu_menu-section_2U-v6']"
                  f"/span[text()='{option}']"))

    def __init__(self, browser: BrowserInterface) -> None:
        super().__init__(browser)

    def click_file_option(self, option: str):
        """
        Clicks on the specified option within the 'File' menu.

        :param option: The option to click (e.g., 'New' or 'Load').
        """
        self.browser.wait_for_element(self.file).click()
        option_locator = self.file_option(option)
        self.browser.get_element_in_stable_state(option_locator).click()

    def upload_basketball_file(self):
        """
        Uploads the 'Basketball.sb3' file.
        """
        self.browser.send_keys("../Basketball.sb3")
