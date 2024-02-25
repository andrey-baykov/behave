Feature: Home Screen
#  This is the feature for Home screen

  Scenario: Open Home screen page
    Given Open url "https://www.lifetwig.com/"
    Then Wait for "5" seconds
    Then Verify element "//div[contains(@class, 'form_header')]" is present

  Scenario: Error message for Log In
    Given Open url "https://www.lifetwig.com/"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    And Verify element "//div[text()='Please input your email address']" is present
    Then Wait for "1" seconds
    And Verify element "//div[text()='Please input your password!']" is present

  Scenario: Login with invalid credentials
    Given Open url "https://www.lifetwig.com/"
    Then Wait for "2" seconds
    Then Type "Alex@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "SDET" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    And Verify element "//div[text()='User with such email is not found']" is present

  Scenario: Login with valid credentials
    Given Open url "https://www.lifetwig.com/"
    Then Wait for "2" seconds
    Then Type "Savuchert@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "Savuchert12zm!" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    And Verify element "//div[text()='Alex'and 'Sava']" is present
    Then Wait for "2" seconds
    And Click on element "//button[@class='left-panel_list_element_link__ycxmi left-panel_logout__3wDO1']"
    Then Wait for "2" seconds
    And Verify element "//div[@class='auth_auth_logo__36DCJ']" is present

  Scenario: Login and click and ucheck box Remember Me
    Given Open url "https://www.lifetwig.com/"
    Then Wait for "2" seconds
    Then Type "Savuchert@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "1" seconds
    Then Type "Savuchert12zm!" in field "//input[@placeholder='Password']"
    Then Wait for "1" seconds
    Then Click on element "//input[@id='login_remember']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    Then Verify element "//span[text()='There are no posts here yet']" is present
    Then Wait for "1" seconds
    And Click on element "//button[@class='left-panel_list_element_link__ycxmi left-panel_logout__3wDO1']"
    Then Wait for "2" seconds
    And Verify element "//div[@class='auth_auth_logo__36DCJ']" is present

  Scenario: Verify 'Report Sent' message for Tab 'Contact us'
    Given Open url "https://www.lifetwig.com/"
    Then Wait for "2" seconds
    Then Type "Savuchert@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "1" seconds
    Then Type "Savuchert12zm!" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    Then Click on element "//a[@href='/contact-us']"
    Then Wait for "2" seconds
    Then Click on element "//div[@class='ant-select ant-select-borderless contact-us_input_field__A70z3 contact-us_select_field__kRV2_ ant-select-single ant-select-show-arrow']"
    Then Wait for "3" seconds
    Then Click on element "//div[text()='Suggestion']"
    Then Wait for "2" seconds
    Then Type "WrongAddress@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "GoodJob!" in field "//div//textarea[@id='contact-us_description']"
    Then Wait for "2" seconds
    Then Click on element "//button//span[text()='SEND']"
    Then Wait for "2" seconds
    And Verify element "//span[text()='Report sent']" is present

  Scenario: Change Language successfully
    Given Open url "https://www.lifetwig.com/"
    Then Wait for "2" seconds
    Then Type "Savuchert@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "1" seconds
    Then Type "Savuchert12zm!" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    Then Click on element "//button[@class='left-panel_list_element_link__ycxmi left-panel_list_element_dropdown__18nGj']"
    Then Wait for "2" seconds
    Then Click on element "//div[text()='Русский']"
    Then Wait for "2" seconds
    And  Verify element "//p[text()='Главная']" is present
    Then Wait for "2" seconds
    And  Click on element "//button[@class='left-panel_list_element_link__ycxmi left-panel_logout__3wDO1']"
    Then Wait for "2" seconds
    And  Verify element "//div[@class='auth_auth_logo__36DCJ']" is present