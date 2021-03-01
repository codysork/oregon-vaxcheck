from exception import InvalidStrategy
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class CheckClickDriver(webdriver.Chrome):
    """A custom version of Selenium's webdriver that includes functions that both check for
    and click elements. """

    def __init__(self):

        super().__init__()
        self.cur_element = None

    def check_wait_click_element(self, by, name, tries=5):
        """Checks if an HTML on the current page has the class specified by "name",
         and clicks the element if it does.
         "strategy" specifies the method the web driver will use to select the element.
         This method currently supports selecting an element by class, css selector, tag,
         or xpath.
         """

        if tries == 0:
            raise exceptions.WebDriverException

        self.implicitly_wait(10)

        try:
            assert WebDriverWait(self, 10).until(
                expected_conditions.presence_of_element_located((by, name))
            )

            if by == 'class name':
                self.cur_element = self.find_element_by_class_name(name)
            elif by == 'css selector':
                self.cur_element = self.find_element_by_css_selector(name)
            elif by == 'tag':
                self.cur_element = self.find_element_by_tag_name(name)
            elif by == 'xpath':
                self.cur_element = self.find_element_by_xpath(name)
            else:
                raise InvalidStrategy()
            self.cur_element.click()

        except TimeoutError:
            self.check_wait_click_element(name, by, tries - 1)

        except exceptions.WebDriverException:
            print("Could not complete chatbot interaction. Check the webpage for updates.")
            raise SystemExit

    def check_wait_switch(self, frame_name, tries=5):
        """Checks if a frame exists on the web page, and then switches to it if it does."""

        if tries == 0:
            raise exceptions.WebDriverException

        self.implicitly_wait(10)

        try:
            assert WebDriverWait(self, 10).until(
                expected_conditions.presence_of_element_located((By.ID, frame_name))
            )

            # Make sure the expected frame was selected
            self.switch_to.frame(self.find_element_by_id(frame_name))

        except TimeoutError:
            self.check_wait_switch(frame_name, tries - 1)

        except exceptions.WebDriverException:
            print("Could not complete chatbot interaction. Check the webpage for updates.")
            raise SystemExit
