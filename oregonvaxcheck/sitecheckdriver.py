import re
from oregonvaxcheck.counties import counties_data
from oregonvaxcheck.macrowebdriver import MacroWebDriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

COUNTY = "Washington"
SLEEP = 2


class SiteCheckDriver(MacroWebDriver):

    def match_counties_element(self, counties_to_search, by, _str) -> bool:

        found = False
        for county in counties_to_search:
            found = self.match_str_in_element(by, _str, county['County'])
        return found

    def check_vaccine_oregon_gov(self, tries=5):

        if tries == 0:
            print("Bot could not check for vaccines at https://covidvaccine.oregon.gov")
            print("Check for bugs in your code, and check the site for updates or errors.")

        self.get("https://covidvaccine.oregon.gov/")
        self.check_wait_switch('chatbot-chat-frame')
        self.check_wait_click_element(By.CLASS_NAME, 'bubble')  # Click chatbot
        sleep(SLEEP)
        self.check_wait_click_element(By.CLASS_NAME, 'button')  # Click "start chat"
        self.check_wait_click_element(By.CLASS_NAME, 'quick-reply')  # Language? Click "English"
        self.check_wait_click_element(By.CLASS_NAME, 'quick-reply')  # Click "Vaccine Eligibility"
        self. check_wait_click_element(By.CLASS_NAME, 'quick-reply')  # Check eligibility? Click "Yes"
        # TODO: Remove hard-coding for under 70, and change age through web app
        # Over 70? Click "No"
        self. check_wait_click_element(By.XPATH, '//div[@class=\'quick-replies-response\']/div[2]')
        self. check_wait_click_element(By.CLASS_NAME, 'tpl-response-buttons-button-text')

        # Check County
        correct_county = self.match_counties_element(
            counties_data, By.CSS_SELECTOR, 'div.conversation > div:nth-of-type(23)')
        if correct_county:
            self. check_wait_click_element(By.XPATH, '//div[@class=\'quick-replies-response\']/div[1]')
        else:
            self. check_wait_click_element(By.XPATH, '//div[@class=\'quick-replies-response\']/div[2]')

        # TODO: Handle "get vaccinated Oregon"

        self.check_wait_click_element(By.CLASS_NAME, 'quick-reply')  # Make sure we are in correct county
        self.check_wait_click_element(By.CLASS_NAME, 'quick-reply')  # Get shot at convention center? Click "Yes"
        # Allergic reaction? Click "No"
        self.check_wait_click_element(By.XPATH, '//div[@class=\'quick-replies-response\']/div[2]')
        # Received any doses? Click "No"
        self.check_wait_click_element(By.XPATH, '//div[@class=\'quick-replies-response\']/div[3]')
        # Tested positive? Click "No"
        self.check_wait_click_element(By.XPATH, '//div[@class=\'quick-replies-response\']/div[2]')
        # Vaccine in last 14 days? Click "No"
        self.check_wait_click_element(By.XPATH, '//div[@class=\'quick-replies-response\']/div[2]')
        # Close contact? Click "No"
        self.check_wait_click_element(By.XPATH, '//div[@class=\'quick-replies-response\']/div[2]')

        # Check for an error message
        try:
            check_element = self.find_element_by_css_selector(
                'div.conversation > div:nth-of-type(51) > div > div > div:nth-of-type(4)'
            )

            if re.match('^.*errror.*$', check_element.text):
                self.bot_stuck_message()

        except exceptions.NoSuchElementException:
            print("The expected element is not available on the web page. Check for updates.")

        # Click "schedule appointment"
        self.check_wait_click_element(By.CSS_SELECTOR, "div.card-response-wrapper > div > div.tpl-response-buttons")

        tries = 0
        while tries < 5:
            try:
                self.implicitly_wait(10)
                self.switch_to.window(self.window_handles[1])
            except IndexError:
                tries += 1
            finally:
                break

        # On MyHealth Page
        # TODO: Make sure a center tag actually exists
        # TODO: Confirm the location where vaccines are available
        # TODO: Screenshot or capture text of availability
        assert WebDriverWait(self, 10).until(
           expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "center"))
        )
        cur = self.find_element_by_css_selector("center")

        message = re.sub(r'^All4Oregon.*\n/gi', '', cur.text)
        print(message)

        # TODO: Close page

    def check_vaccine_walgreens(self):
        self.get("https://www.walgreens.com/findcare/vaccination/covid-19/location-screening")
        self.check_wait_click_element(By.XPATH, "//button[@class='btn']")  # Click "Search"
        # tstamp = datetime.utcnow()
        # print(tstamp)
        # scrot = screenshot()
        # scrot.save()
