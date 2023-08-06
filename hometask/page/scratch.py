from swi_browser.browser_interface import BrowserInterface
from tests.shared.pages.base_page import BasePage

class ScratchPage(BasePage):
    """Represents the Scratch page and its operations."""

    def __init__(self, browser: BrowserInterface) -> None:
        """
        Initialize the Scratch page with the specified browser and URL.

        :param browser: BrowserInterface object for interaction.
        """
        super().__init__(
            browser,
            url="https://scratch.mit.edu/projects/editor/?tutorial=getStarted",
        )

    def load_main_page(self, browser: BrowserInterface):
        """
        Load the main Scratch page in the specified browser.

        :param browser: BrowserInterface object for interaction.
        """
        scratch_page = ScratchPage(browser)
        return scratch_page.load()
