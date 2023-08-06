from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from swi_browser.browser_interface import BrowserInterface

from tests.shared.pages.base_page import BasePage


class Canvas(BasePage):

    target_element = (By.XPATH, "//g[@class='blocklyBlockCanvas']")
    source_element_locator = (By.XPATH, "//g[@data-test-id='motion_movesteps']")
    sprite_x_input = (By.XPATH, "//input[@placeholder='x']")
    sprite_y_input = (By.XPATH, "//input[@placeholder='y']")
    start_project_flag = (By.XPATH,
                          "//img[contains(@class, 'green-flag_green-flag_1kiAo')]")

    def __init__(self, browser: BrowserInterface) -> None:
        super().__init__(browser)

    def drag_and_drop(self):
        """
        Performs a drag-and-drop action from source_element to target_element.
        """
        actions = ActionChains(self.browser)
        source_element = self.browser.wait_for_element(
            self.source_element_locator)
        target_element = self.browser.find_element(
            self.target_element)
        actions.drag_and_drop(source_element, target_element).perform()

    def verify_new_project(self):
        """
        Verifies that the new project has been created successfully.
        """
        self.browser.wait_for_element(self.sprite_x_input)

        input_element = self.browser.find_element(*self.sprite_x_input)
        input_value = input_element.get_attribute("value")

        assert input_value == "0", f"Expected input value to be '0', " \
                                   f"but found '{input_value}'"

    def click_on_start_project(self):
        """
        Clicks on the 'Start Project' flag to begin the project.
        """
        self.browser.wait_for_element(self.start_project_flag).click()

    def verify_basketball_state(self):
        """
        Verifies the state of the basketball sprite.
        """
        self.browser.wait_for_element(self.sprite_y_input)

        input_element = self.browser.find_element(*self.sprite_y_input)
        input_value = input_element.get_attribute("value")

        assert input_value == "0", f"Expected input value to be '0', " \
                                   f"but found '{input_value}'"
