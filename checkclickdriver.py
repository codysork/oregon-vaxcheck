import re
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class CheckClickDriver(webdriver.Chrome):
    """A custom version of Selenium's webdriver that includes functions that both check for
    and click elements. """

    def check_wait_click_class(self, name, tries=5):
        """Checks if an HTML on the current page has the class specified by "name",
         and clicks the element if it does."""

        if tries == 0:
            raise exceptions.WebDriverException

        self.implicitly_wait(10)

        try:
            assert WebDriverWait(self, 10).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, name))
            )

            button = self.find_element_by_class_name(name)
            button.click()

        except TimeoutError:
            self.check_wait_click_class(name, tries - 1)

        except exceptions.WebDriverException:
            print("Could not complete chatbot interaction. Check the webpage for updates.")
            raise SystemExit

    def check_wait_click_css(self, selector, tries=5):

        if tries == 0:
            raise exceptions.WebDriverException

        self.implicitly_wait(10)

        try:
            assert WebDriverWait(self, 10).until(
                expected_conditions.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            button = self.find_element_by_css_selector(selector)
            button.click()

            if tries == 0:
                return

        except TimeoutError:
            self.check_wait_click_css(selector, tries - 1)

        except exceptions.WebDriverException:
            print("Could not complete chatbot interaction. Check the webpage for updates.")
            raise SystemExit

    def check_wait_click_tag(self, name, tries=5):
        """Checks if an HTML on the current page has the tag specified by "name",
         and clicks the element if it does."""

        if tries == 0:
            raise exceptions.WebDriverException

        try:
            assert WebDriverWait(self, 10).until(
                expected_conditions.presence_of_element_located((By.TAG_NAME, name))
            )

            button = self.find_element_by_tag_name(name)
            button.click()

        except TimeoutError:
            self.check_wait_click_class(name, tries - 1)

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

    def check_wait_click_xpath(self, xpath, tries=5):
        try:
            assert WebDriverWait(self, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath))
            )
            button = self.find_element_by_xpath(xpath)
            button.click()

            if tries == 0:
                return

        except TimeoutError:
            self.check_wait_click_xpath(xpath, tries - 1)

        except exceptions.WebDriverException:
            print("Could not complete chatbot interaction. Check the webpage for updates.")
            raise SystemExit
