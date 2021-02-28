
from checkclickdriver import CheckClickDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

SLEEP = 3


class SiteCheckDriver(CheckClickDriver):

    def check_vaccine_oregon_gov(self):
        self.get("https://covidvaccine.oregon.gov/")
        self.check_wait_switch('chatbot-chat-frame')
        self.check_wait_click_class('bubble')  # Click chatbot
        self.check_wait_click_class('button')  # Click "start chat"
        sleep(SLEEP)
        self.check_wait_click_class('quick-reply')  # Language? Click "English"
        sleep(SLEEP)
        self.check_wait_click_class('quick-reply')  # Click "Vaccine Eligibility"
        sleep(SLEEP + 2)
        self. check_wait_click_class('quick-reply')  # Check eligibility? Click "Yes"
        sleep(SLEEP)
        # TODO: Remove hard-coding for under 70, and change age through web app
        self. check_wait_click_xpath("//div[@class='quick-replies-response']/div[2]")  # Over 70? Click "No"
        sleep(SLEEP)
        self. check_wait_click_class('tpl-response-buttons-button-text')
        sleep(SLEEP)
        self.check_wait_click_class('quick-reply')  # In the listed counties? Click "Yes"
        sleep(SLEEP)
        self.check_wait_click_class('quick-reply')  # Get shot at convention center? Click "Yes"
        sleep(SLEEP)
        self.check_wait_click_xpath("//div[@class='quick-replies-response']/div[2]")  # Allergic reaction? Click "No"
        sleep(SLEEP)
        self.check_wait_click_xpath("//div[@class='quick-replies-response']/div[3]")  # Received any doses? Click "No"
        sleep(SLEEP)
        self.check_wait_click_xpath("//div[@class='quick-replies-response']/div[2]")  # Tested positive? Click "No"
        sleep(SLEEP)
        # Vaccine in last 14 days? Click "No"
        self.check_wait_click_xpath("//div[@class='quick-replies-response']/div[2]")
        sleep(SLEEP)
        self.check_wait_click_xpath("//div[@class='quick-replies-response']/div[2]")  # Close contact? Click "No"
        sleep(SLEEP + 10)
        # Click "schedule appointment"
        self.check_wait_click_xpath(
            "//div[@style='background: rgb(255, 255, 255) none repeat scroll 0% 0%; border-top-color: rgb(219, 225, 232);']//div[last()]"
        )
        self.switch_to.window("MyHealth - Login Page")

        # On MyHealth Page
        assert WebDriverWait(self, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//center"))
        )

        cur = self.find_element_by_xpath("//center")
        print(cur.text)
        return

    def check_vaccine_walgreens(self):
        self.get("https://www.walgreens.com/findcare/vaccination/covid-19/location-screening")
        self.check_wait_click_xpath("//button[@class='btn']")  # Click "Search"
        # tstamp = datetime.utcnow()
        # print(tstamp)
        # scrot = screenshot()
        # scrot.save()
