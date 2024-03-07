Feature: Test login page
#  These tests are for the login page

  Scenario: Open login page
    Given Open "prod" url
    Then Wait for "2" seconds
#    Then Verify element "//div[contains(@class, 'form_header')]" is present

  Scenario: Login with valid credentials
    Given Open "prod" url
#    Then Wait for "2" seconds
    Then Type "pcs.class1223@gmail.com" in field "//input[@placeholder='Email Address']"
#    Then Wait for "2" seconds
    Then Type "!Qwerty&8" in field "//input[@placeholder='Password']"
#    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
#    Then Wait for "1" seconds
    And Verify element "//div[text()='pcs.class1223@gmail.com']" is present

  Scenario: Login with invalid credentials
    Given Open "prod" url
    Then Type "pcs.class1223@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "wrongpassword" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    And Verify element "//div[text()='Email or password field not correct']" is present

  Scenario: Goto forgot password page and go back
    Given Open "prod" url
    Then Wait for "2" seconds
    Then Click on element "//a[text()='Forgot Password']"
    Then Wait for "2" seconds
    Then Click on element "//a[text()='Go back to the login page']"
    Then Wait for "2" seconds
    Then Verify element "//div[contains(@class, 'form_header')]" is present
    Then Temporary

  Scenario: Toggle notifications
    Given Open "prod" url
    Then Login as "admin"
#    Then Type "pcs.class1223@gmail.com" in field "//input[@placeholder='Email Address']"
#    Then Type "!Qwerty&8" in field "//input[@placeholder='Password']"
#    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Click on element "//button[.//p[text()='Settings']]"
#    Then Click on "Settings"
#    Then Click on "Notifications"
    Then Click on element "//a[text()='Notifications']"
#    Then Click on element "//div[./div/p[text()='Password change']]/button"
    Then Toggle element "//div[./div/p[text()='Password change']]/button" to "Off"
    Then Toggle element "Password change" to "Off"
    Then Wait for "2" seconds
