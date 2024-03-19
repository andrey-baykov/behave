from time import sleep

from behave import step
from selenium import webdriver
from selenium.common import TimeoutException
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
    try:
        element = WebDriverWait(context.driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, f"{xpath}")))
    except TimeoutException:
        element = []
    assert element, f"Element with xpath {xpath} is not found"


@step("Temporary")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Temporary')


@step('Toggle element "{xpath}" to "{condition}"')
def step_impl(context, xpath, condition):
    elements = {
        'password_change': "//div[./div/p[text()='Password change']]/button",
        'connection': "//div[./div/p[text()='Connection accepted']]/button",
        'birthdays': "//div[./div/p[text()='Birthdays']]/button",
        'likes': "//div[./div/p[text()='Likes, comments & shares']]/button"
    }

    element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"{elements[xpath]}")))

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
        'user1': ('grishina.ermashkevich@gmail.com', 'Ven12345@')
    }

    type_in(context, users[role][0], "//input[@placeholder='Email Address']")
    type_in(context, users[role][1], "//input[@placeholder='Password']")

    click_element(context, "//button[contains(@class, 'ant-btn')]")
    click_element(context, "//button[.//p[text()='Settings']]")
    click_element(context, "//a[text()='Notifications']")


@step("Login with following credentials")
def step_impl(context):
    xpaths = {
        'login': "//input[@placeholder='Email Address']",
        'password': "//input[@placeholder='Password']"
    }

    for row in context.table:
        type_in(context, row['value'], xpaths[row['element']])
        # type_in(context, "pcs.class1223@gmail.com", "//input[@placeholder='Email Address']")
        # type_in(context, "!Qwerty&8", "//input[@placeholder='Password']")



    # context.table = [{'element': 'login', 'value': 'pcs.class1223@gmail.com'},
    #                  {'element': 'password','value': '!Qwerty&8 '}]


@step("Verify google play is open")
def verify_google_play(context):
    current_window = context.driver.current_window_handle
    context.driver.switch_to.window(context.driver.window_handles[1])
    element = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Google Play']")),
                                                      message="Google play not found")
    assert element, "Google play not found"
    sleep(2)
    context.driver.close()
    context.driver.switch_to.window(current_window)
    # context.driver.switch_to.window(context.driver.window_handles[0])
