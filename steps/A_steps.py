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


@step('Click on "{xpath}" button')
def click_element(context, xpath):
    names = {
        'LogIn': '//button[contains(@class, "ant-btn")]',
        'Logout': '//button[@class="left-panel_list_element_link__ycxmi left-panel_logout__3wDO1"]',
        'Checkbox': '//span[@class="ant-checkbox ant-checkbox-checked"]',
        'Contact_us': '//a[@href="/contact-us"]',
        'Select_subject': '//div[@class="ant-select ant-select-borderless contact-us_input_field__A70z3 '
                          'contact-us_select_field__kRV2_ ant-select-single ant-select-show-arrow"]',
        'Suggestion': '//div[text()="Suggestion"]',
        'Send': '//button//span[text()="SEND"]',
        'Language_menu': '//button[@class="left-panel_list_element_link__ycxmi '
                         'left-panel_list_element_dropdown__18nGj"]',
        'Language': '//div[text()="Русский"]',
        'Language_English': '//div[text()="English"]',
        'Settings': '//a[@href="/settings"]',
        'Notifications': '//a[text()="Notifications"]'
    }
    btn = names.get(xpath)
    element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, f"{btn}")))
    assert element, f"Element with xpath {btn} is not found"
    element.click()


@step('Verify element "{xpath}" is present')
def step_impl(context, xpath):
    names = {
        'logo': '//div[contains(@class, "form_header")]',
        'User_name': '//div[text()="Alex"and "Sava"]',
        'Unknown_button': '//div[@class="auth_auth_logo__36DCJ"]',
        'text_there_are_no_posts': '//span[text()="There are no posts here yet"]',
        'Report': '//span[text()="Report sent"]',
        'Language_Check': '//p[text()="Главная"]'
    }
    # element = context.driver.find_element(By.XPATH, f"{xpath}")
    element = WebDriverWait(context.driver, 15).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                           f"{names[xpath]}")))
    assert element, f"Element with xpath {names[xpath]} is not found"


@step('Verify that error message for "{xpath}" is present')
def step_impl(context, xpath):
    names = {
        'email': '//div[text()="Please input your email address"]',
        'password': '//div[text()="Please input your password!"]',
        'email_not_found': '//div[text()="User with such email is not found"]',
    }
    # element = context.driver.find_element(By.XPATH, f"{xpath}")
    element = WebDriverWait(context.driver, 15).until(EC.presence_of_all_elements_located((By.XPATH,
                                                                                           f"{names[xpath]}")))
    assert element, f"Element with xpath {names[xpath]} is not found"


@step('Toggle element "{xpath}" to "{condition}"')
def step_impl(context, xpath, condition):
    switch_button = {
        'Password_change': '//div[./div/p[text()="Password change"]]/button',
        'Connection_accepted': '//div[./div/p[text()="Connection accepted"]]/button',
        'Birthdays': '//div[./div/p[text()="Birthdays"]]/button'
    }
    element = WebDriverWait(context.driver, 15).until(EC.element_to_be_clickable((By.XPATH, f"{switch_button[xpath]}")))
    assert element, f"Element with xpath {switch_button[xpath]} is not found"
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

# @then('Login with "{text}" credentials')
# def step_impl(context, text):
#     options = {
#         'login': '//input[@placeholder="Email Address"]',
#         'password': '//input[@placeholder="Password"]'
#     }
#     for row in context.table:
#         login_value = row['login']
#         password_value = row['password']
#         if text == "valid":
#             type_in(context, login_value, options['login'])
#             type_in(context, password_value, options['password'])
#             click_element(context, "//button[contains(@class, 'ant-btn')]")
#         elif text == "invalid":
#                 type_in(context, login_value, options['login'])
#                 type_in(context, password_value, options['password'])
#                 click_element(context, "//button[contains(@class, 'ant-btn')]")
