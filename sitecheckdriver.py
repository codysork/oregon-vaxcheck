
from checkclickdriver import CheckClickDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

SLEEP = 2


class SiteCheckDriver(CheckClickDriver):

    def check_vaccine_oregon_gov(self):
        self.get("https://covidvaccine.oregon.gov/")
        self.check_wait_switch('chatbot-chat-frame')
        self.check_wait_click_element(By.CLASS_NAME, 'bubble')  # Click chatbot
        sleep(SLEEP)
        self.check_wait_click_element(By.CLASS_NAME, 'button')  # Click "start chat"
        self.check_wait_click_element(By.CLASS_NAME, 'quick-reply')  # Language? Click "English"
        self.check_wait_click_element(By.CLASS_NAME, 'quick-reply')  # Click "Vaccine Eligibility"
        self. check_wait_click_element(By.CLASS_NAME, 'quick-reply')  # Check eligibility? Click "Yes"
        # TODO: Remove hard-coding for under 70, and change age through web app
        self. check_wait_click_element(By.XPATH, "//div[@class='quick-replies-response']/div[2]")  # Over 70? Click "No"
        self. check_wait_click_element(By.CLASS_NAME, 'tpl-response-buttons-button-text')
        self.check_wait_click_element(By.CLASS_NAME, 'quick-reply')  # In the listed counties? Click "Yes"
        self.check_wait_click_element(By.CLASS_NAME, 'quick-reply')  # Get shot at convention center? Click "Yes"
        self.check_wait_click_element(By.XPATH, "//div[@class='quick-replies-response']/div[2]")  # Allergic reaction? Click "No"
        self.check_wait_click_element(By.XPATH, "//div[@class='quick-replies-response']/div[3]")  # Received any doses? Click "No"
        self.check_wait_click_element(By.XPATH, "//div[@class='quick-replies-response']/div[2]")  # Tested positive? Click "No"
        # Vaccine in last 14 days? Click "No"
        self.check_wait_click_element(By.XPATH, "//div[@class='quick-replies-response']/div[2]")
        self.check_wait_click_element(By.XPATH, "//div[@class='quick-replies-response']/div[2]")  # Close contact? Click "No"
        # Click "schedule appointment"
        self.check_wait_click_element(By.CSS_SELECTOR, "div.card-response-wrapper > div > div.tpl-response-buttons")
        # self.switch_to.window("MyHealth - Login Page")

        # On MyHealth Page
        # assert WebDriverWait(self, 10).until(
        #    expected_conditions.presence_of_element_located((By.XPATH, "//center"))
        #)

        #cur = self.find_element_by_xpath("//center")
        #print(cur.text)
        return

    def check_vaccine_walgreens(self):
        self.get("https://www.walgreens.com/findcare/vaccination/covid-19/location-screening")
        self.check_wait_click_element("//button[@class='btn']")  # Click "Search"
        # tstamp = datetime.utcnow()
        # print(tstamp)
        # scrot = screenshot()
        # scrot.save()
