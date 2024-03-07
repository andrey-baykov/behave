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
    # if env == 'prod':
    #     url = 'https://www.lifetwig.com/'
    # elif env == 'uat':
    #     url = 'https://google.com/'
    # elif env == 'dev':
    #     url = 'https://yahoo.com'

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


@step('Click on element "{xpath}"')
def click_element(context, xpath):
    element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, f"{xpath}")))
    assert element, f"Element with xpath {xpath} is not found"
    element.click()


@step('Verify element "{xpath}" is present')
def step_impl(context, xpath):
    # element = context.driver.find_element(By.XPATH, f"{xpath}")
    element = WebDriverWait(context.driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, f"{xpath}")))
    assert element, f"Element with xpath {xpath} is not found"


@step("Temporary")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Temporary')


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
