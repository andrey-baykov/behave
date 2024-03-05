Feature: Test login page
#  These tests are for the login page

  Scenario: Open login page
    Given Open url "https://www.lifetwig.com/"
    Then Wait for "5" seconds
    Then Verify element "//div[contains(@class, 'form_header')]" is present

  Scenario: Login with valid credentials
    Given Open url "https://www.lifetwig.com/"
    Then Wait for "2" seconds
    Then Type "pcs.class1223@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "!Qwerty&8" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "5" seconds
    And Verify element "//div[text()='pcs.class1223@gmail.com']" is present

  Scenario: Login with invalid credentials
    Given Open url "https://www.lifetwig.com/"
    Then Type "pcs.class1223@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "wrongpassword" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    And Verify element "//div[text()='Email or password field not correct']" is present

  Scenario: Goto forgot password page and go back
    Given Open url "https://www.lifetwig.com/"
    Then Wait for "2" seconds
    Then Click on element "//a[text()='Forgot Password']"
    Then Wait for "2" seconds
    Then Click on element "//a[text()='Go back to the login page']"
    Then Wait for "2" seconds
    Then Verify element "//div[contains(@class, 'form_header')]" is present
    Then Temporary
