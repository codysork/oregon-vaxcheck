#!/usr/bin/python3

from datetime import datetime
# from pyautogui import screenshot
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

SLEEP = 3


def check_vaccine_oregon_gov():
    driver.get("https://covidvaccine.oregon.gov/")
    check_wait_switch('chatbot-chat-frame')
    check_wait_click_tag('svg')  # Click chatbot
    check_wait_click_class('button')  # Click "start chat"
    time.sleep(SLEEP)
    check_wait_click_class('quick-reply')  # Language? Click "English"
    time.sleep(SLEEP)
    check_wait_click_class('quick-reply')  # Click "Vaccine Eligibility"
    time.sleep(SLEEP + 2)
    check_wait_click_class('quick-reply')  # Check eligibility? Click "Yes"
    time.sleep(SLEEP)
    # TODO: Remove hard-coding for under 70, and change age through web app
    check_wait_click_xpath("//div[@class='quick-replies-response']/div[2]")  # Over 70? Click "No"
    time.sleep(SLEEP)
    check_wait_click_class('tpl-response-buttons-button-text')
    time.sleep(SLEEP)
    check_wait_click_class('quick-reply')  # In the listed counties? Click "Yes"
    time.sleep(SLEEP)
    check_wait_click_class('quick-reply')  # Get shot at convention center? Click "Yes"
    time.sleep(SLEEP)
    check_wait_click_xpath("//div[@class='quick-replies-response']/div[2]")  # Allergic reaction? Click "No"
    time.sleep(SLEEP)
    check_wait_click_xpath("//div[@class='quick-replies-response']/div[3]")  # Received any doses? Click "No"
    time.sleep(SLEEP)
    check_wait_click_xpath("//div[@class='quick-replies-response']/div[2]")  # Tested positive? Click "No"
    time.sleep(SLEEP)
    check_wait_click_xpath("//div[@class='quick-replies-response']/div[2]")  # Vaccine in last 14 days? Click "No"
    time.sleep(SLEEP)
    check_wait_click_xpath("//div[@class='quick-replies-response']/div[2]")  # Close contact? Click "No"
    time.sleep(SLEEP + 10)
    # Click "schedule appointment"
    check_wait_click_xpath(
        "//div[@style='background: rgb(255, 255, 255) none repeat scroll 0% 0%; border-top-color: rgb(219, 225, 232);']//div[last()]"
    )
    driver.switch_to.window("MyHealth - Login Page")

    # On MyHealth Page
    assert WebDriverWait(driver, 2).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//center"))
    )

    cur = driver.find_element_by_xpath("//center")
    print(cur.text)
    return


def check_vaccine_walgreens():
    driver.get("https://www.walgreens.com/findcare/vaccination/covid-19/location-screening")
    check_wait_click_xpath("//button[@class='btn']")  # Click "Search"
    tstamp = datetime.utcnow()
    print(tstamp)
    # scrot = screenshot()
    # scrot.save()


def check_wait_click_class(name, tries=5):
    try:
        assert WebDriverWait(driver, 2).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, name))
        )
        button = driver.find_element_by_class_name(name)
        button.click()

        if tries == 0:
            return

    except TimeoutError:
        check_wait_click_class(name, tries - 1)

    except exceptions.WebDriverException:
        print("Could not complete chatbot interaction. Check the webpage for updates.")


def check_wait_click_tag(name, wait=2, tries=5):
    try:
        assert WebDriverWait(driver, wait).until(
            expected_conditions.presence_of_element_located((By.TAG_NAME, name))
        )
        button = driver.find_element_by_tag_name(name)
        button.click()

        if tries == 0:
            return

    except TimeoutError:
        check_wait_click_tag(name, wait, tries - 1)

    except exceptions.WebDriverException:
        print("Could not complete chatbot interaction. Check the webpage for updates.")


def check_wait_switch(frame_name, wait=2, tries=5):
    """Checks if a frame exists on the web page, and then switches to it if it does."""
    try:
        assert WebDriverWait(driver, wait).until(
            expected_conditions.presence_of_element_located((By.ID, frame_name))
        )

        driver.switch_to.frame(driver.find_element_by_id(frame_name))

        if tries == 0:
            return

    except TimeoutError:
        check_wait_switch(frame_name, tries - 1)

    except exceptions.WebDriverException:
        print("Could not complete chatbot interaction. Check the webpage for updates.")


def check_wait_click_xpath(xpath, wait=2, tries=5):
    try:
        assert WebDriverWait(driver, wait).until(
            expected_conditions.presence_of_element_located((By.XPATH, xpath))
        )
        button = driver.find_element_by_xpath(xpath)
        button.click()

        if tries == 0:
            return

    except TimeoutError:
        check_wait_click_xpath(xpath, wait, tries - 1)

    except TypeError:
        button = driver.find_element_by_tag_name(xpath)
        button.click()

    except exceptions.WebDriverException:
        print("Could not complete chatbot interaction. Check the webpage for updates.")


# TODO: Add tests for buttons
if __name__ == '__main__':
    driver = webdriver.Firefox()
    check_vaccine_oregon_gov()
    # check_vaccine_walgreens()
