from time import sleep

from behave import step
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@step('Open "{env}" url')
def open_url(context, env):
    urls = {
        'prod': 'https://www.lifetwig.com/',
        'uat': 'https://google.com/',
        'dev': 'https://yahoo.com'
    }

    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get(urls[env])


@step('Type "{text}" in field "{xpath}"')
def type_in(context, text, xpath):
    element = context.driver.find_elements(By.XPATH, f"{xpath}")
    assert element, f"Element with xpath {xpath} is not found"
    element[0].send_keys(text)


@step('Wait for "{seconds}" seconds')
def sleep_for(context, seconds):
    sleep(int(seconds))


@step('Click on element "{xpath}" button')
def click_element(context, xpath):
    names = {
        'LogIn': '//button[contains(@class, "ant-btn")]',
    }
    btn = names.get(xpath)
    element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, f"{btn}")))
    assert element, f"Element with xpath {btn} is not found"
    element.click()

# For review#1
# @step('Verify element "{logo}" is present')
# def step_impl(context, logo):
#     element = "//div[contains(@class, 'form_header')]"
#     # element = context.driver.find_element(By.XPATH, f"{xpath}")
#     element = WebDriverWait(context.driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, f"{element}")))
#     assert element, f"Element with xpath {element} is not found"

@step('Verify element "{xpath}" is present')
def step_impl(context, xpath):
    names = {
        'logo': '//div[contains(@class, "form_header")]',
        'email_field': '//div[text()="Please input your email address"]',
        'password_field': '//div[text()="Please input your password!"]',
        'email is not found': '//div[text()="User with such email is not found"]'
    }
    button = names.get(xpath)
    # element = context.driver.find_element(By.XPATH, f"{xpath}")
    element = WebDriverWait(context.driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, f"{button}")))
    assert element, f"Element with xpath {button} is not found"


@step('Toggle element "{xpath}" to "{condition}"')
def step_impl(context, xpath, condition):
    element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, f"{xpath}")))
    assert element, f"Element with xpath {xpath} is not found"
    element_condition = element.get_attribute("aria-checked")
    if condition.lower() == "on" and element_condition == 'false':
        element.click()
    elif condition.lower() == "off" and element_condition == 'true':
        element.click()


@step('Login as "{role}"')
def login_as(context, role):
    users = {
        'admin': ('pcs.class1223@gmail.com', '!Qwerty&8'),
        'sales': ('sales@gmail.com', '12345'),
    }

    type_in(context, users[role][0], "//input[@placeholder='Email Address']")
    type_in(context, users[role][1], "//input[@placeholder='Password']")
    click_element(context, "//button[contains(@class, 'ant-btn')]")
