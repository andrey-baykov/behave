from time import sleep

from behave import step
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@step('Open url "{url}"')
def open_url(context, url):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get(url)


@step('Type "{text}" in field "{xpath}"')
def type_in(context, text, xpath):
    element = context.driver.find_element(By.XPATH, f"{xpath}")
    assert element, f"Element with xpath {xpath} is not found"
    element.send_keys(text)


@step('Wait for "{seconds}" seconds')
def sleep_for(context, seconds):
    sleep(int(seconds))


@step('Click on element "{xpath}"')
def click_element(context, xpath):
    element = context.driver.find_element(By.XPATH, f"{xpath}")
    assert element, f"Element with xpath {xpath} is not found"
    element.click()


@step('Verify element "{xpath}" is present')
def step_impl(context, xpath):
    element = context.driver.find_element(By.XPATH, f"{xpath}")
    assert element, f"Element with xpath {xpath} is not found"
