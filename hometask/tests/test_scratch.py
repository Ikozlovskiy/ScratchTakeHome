import allure

from tests.e2e.hometask.page.scratch import ScratchPage
from tests.e2e.hometask.page_components.canvas import Canvas
from tests.e2e.hometask.page_components.top_menu import MenuBar


class TestScratch:

    def setup(self, browser):
        page = ScratchPage(browser)
        page.load_main_page(browser)
        return page

    @allure.testcase("Test Drag and Drop Functionality")
    @allure.feature("Drag and Drop Feature")
    @allure.story("Dragging and Dropping Elements")
    def test_drag_and_drop(self, setup):
        canvas = Canvas(setup.browser)

        with allure.step("Perform drag and drop"):
            canvas.drag_and_drop()

    @allure.testcase("Test Creating a New Project")
    @allure.feature("Project Creation Feature")
    @allure.story("Creating a New Project")
    def test_create_new_project(self, setup):
        canvas = Canvas(setup.browser)
        menu = MenuBar(setup.browser)

        with allure.step("Click 'New' option"):
            menu.click_file_option("New")

        with allure.step("Verify new project creation"):
            canvas.verify_new_project()

    @allure.testcase("Test Adding a Saved Project")
    @allure.feature("Project Loading Feature")
    @allure.story("Adding a Saved Project")
    def test_add_saved_project(self, setup):
        canvas = Canvas(setup.browser)
        menu = MenuBar(setup.browser)

        with allure.step("Click 'Load' option"):
            menu.click_file_option("Load")

        with allure.step("Upload saved project and start"):
            menu.upload_basketball_file()
            canvas.start_project_flag()

        with allure.step("Verify saved project state"):
            canvas.verify_basketball_state()






