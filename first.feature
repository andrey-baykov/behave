Feature: Test login page
#  These tests are for the login page

  Scenario: Open login page
    Given Open url "https://www.lifetwig.com/"
    Then Verify element "//div[contains(@class, 'form_header')]" is present

  Scenario: Login with valid credentials
    Given Open url "https://www.lifetwig.com/"
    Then Type "pcs.class1223@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Type "!Qwerty&8" in field "//input[@placeholder='Password']"
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    And Verify element "//div[text()='pcs.class1223@gmail.com']" is present

  Scenario: Login with invalid credentials
    Given Open url "https://www.lifetwig.com/"
    Then Type "pcs.class1223@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Type "wrongpassword" in field "//input[@placeholder='Password']"
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    And Verify element "//div[text()='Email or password field not correct']" is present
