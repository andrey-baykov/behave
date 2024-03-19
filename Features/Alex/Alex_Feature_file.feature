Feature: Home Screen
#  This is the feature for Home screen
  Background:
    Given Open "prod" url

  Scenario: Open Home screen pag
    Then Verify element "logo" is present

  Scenario: Error message for Log In
    Then Click on "LogIn" button
    And Verify that error message for "email" is present
    And Verify that error message for "password" is present

  Scenario: Login with invalid credentials
    Then Type "Savucht@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Type "SDET" in field "//input[@placeholder='Password']"
    Then Click on "LogIn" button
    And Verify that error message for "email_not_found" is present

  Scenario: Login with valid credentials
    Then Type "Savuchert@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Type "Savuchert12zm!" in field "//input[@placeholder='Password']"
    Then Click on "LogIn" button
    And Verify element "User_name" is present
    And Click on "Logout" button
    And Verify element "logo" is present

  Scenario: Login and click and ucheck box Remember Me
    Then Type "Savuchert@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Type "Savuchert12zm!" in field "//input[@placeholder='Password']"
    Then Click on "Checkbox" button
    Then Click on "LogIn" button
    Then Verify element "text_there_are_no_posts" is present
    And Click on "Logout" button
    And Verify element "logo" is present

  Scenario: Verify 'Report Sent' message for Tab 'Contact us'
    Then Type "Savuchert@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Type "Savuchert12zm!" in field "//input[@placeholder='Password']"
    Then Click on "LogIn" button
    Then Click on "Contact_us" button
    Then Click on "Select_subject" button
    Then Click on "Suggestion" button
    Then Type "WrongAddress@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Type "GoodJob!" in field "//div/textarea[@class='ant-input contact-us_input_field__A70z3']"
    Then Click on "Send" button
    And Verify element "Report" is present

  Scenario: Change Language successfully
    Then Type "Savuchert@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Type "Savuchert12zm!" in field "//input[@placeholder='Password']"
    Then Click on "LogIn" button
    Then Click on "Language_menu" button
    Then Click on "Language" button
    And  Verify element "Language_Check" is present
    And  Click on "Logout" button
    And  Verify element "logo" is present

  Scenario: Toggle elements
    Then Type "Savuchert@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Type "Savuchert12zm!" in field "//input[@placeholder='Password']"
    Then Click on "LogIn" button
    Then Click on "Language_menu" button
    Then Click on "Language_English" button
    Then Click on "Settings" button
    Then Click on "Notifications" button
    Then Toggle element "Password_change" to "on"
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
