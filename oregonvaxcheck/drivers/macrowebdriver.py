from oregonvaxcheck.common.exceptions import InvalidStrategy
import re
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MacroWebDriver(webdriver.Chrome):
    """A custom version of Selenium's webdriver that includes functions that both check for
    and click elements. """

    def __init__(self):

        super().__init__()
        self.cur_element = None

    def bot_stuck_message(self):
        print("Could not complete chatbot interaction.")
        print("Bot got stuck at: " + self.cur_element.text)
        print("Check the webpage for updates.")

    def match_str_in_element(self, by, elem_str, str_to_find) -> bool:

        self.select_element(by, elem_str)  # self.cur_element is changed
        found = False
        if re.match(r'^.*' + str_to_find + '.*$', elem_str):
            found = True
        return found

    def check_wait_click_element(self, by, _str, csv_file=None, tries=5):
        """
        Checks for an html element on a webpage specified by location strategy,
        and then clicks it.

        by: Takes a By object from the selenium API. Make sure to specify the
            location strategy for selecting an element by passing By.CLASS_NAME,
            By.CSS_SELECTOR, By.TAG, or By.XPATH
        _str: The string that the selection strategy will use for matching the
              element.
        """

        if tries == 0:
            raise exceptions.WebDriverException

        self.implicitly_wait(10)

        try:
            assert WebDriverWait(self, 10).until(
                expected_conditions.presence_of_element_located((by, _str))
            )

            self.select_element(by, _str)

            if csv_file:
                csv_file

            self.cur_element.click()

        except TimeoutError:
            self.check_wait_click_element(_str, by, tries - 1)

        except exceptions.NoSuchElementException:
            print("The expected element is not available on the web page. Check for updates.")

        except exceptions.StaleElementReferenceException:
            self.bot_stuck_message()
            raise SystemExit()

        except exceptions.WebDriverException:
            self.bot_stuck_message()
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

    def select_element(self, by, _str):

        try:
            if by == 'class name':
                self.cur_element = self.find_element_by_class_name(_str)
            elif by == 'css selector':
                self.cur_element = self.find_element_by_css_selector(_str)
            elif by == 'tag':
                self.cur_element = self.find_element_by_tag_name(_str)
            elif by == 'xpath':
                self.cur_element = self.find_element_by_xpath(_str)
            else:
                raise InvalidStrategy()

        except InvalidStrategy:
            print("You did not use a proper strategy for selecting an HTML element.")
