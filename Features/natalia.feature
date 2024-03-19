Feature: Test login page
#  These tests are for the login page

  Scenario: Reset password
    Given Open "prod" url
    Then Wait for "2" seconds
    Then Click on element "//a[text()='Forgot Password']"
    Then Wait for "2" seconds
    Then Type "grishina.ermashkevich@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Click on element "//span[text() = 'SEND']"
    Then Wait for "2" seconds
    Then Verify element "//div[text() = 'Enter security code']" is present

  Scenario: Sign up flow
    Given Open "prod" url
    Then Wait for "2" seconds
    Then Click on element "//a[text() = 'Sign up']"
    Then Wait for "2" seconds
    Then Type "Natalia" in field "//input[@placeholder='First Name']"
    Then Wait for "2" seconds
    Then Type "Grishina" in field "//input[@placeholder='Last Name']"
    Then Wait for "2" seconds
    Then Type "grishina.enmashkevich+10@gmail.com" in field "//input[@placeholder='Email address']"
    Then Wait for "2" seconds
    Then Type "Ven12345@" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//span[./input[@class= 'ant-checkbox-input']]"
    Then Wait for "2" seconds
    Then Click on element "//Span[text() = 'Sign up']"
    Then Wait for "2" seconds
    Then Verify element "//div[text() = 'Enter security code']" is present
    Then Wait for "2" seconds

  Scenario: Sign in from Sign up screen
    Given Open "prod" url
    Then Wait for "2" seconds
    Then Click on element "//a[text() = 'Sign up']"
    Then Wait for "2" seconds
    Then Click on element "//a[text() = 'Sign in']"
    Then Wait for "2" seconds
    Then Type "grishina.ermashkevich@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "Ven12345@" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "5" seconds
    And Verify element "//div[text()='grishina.ermashkevich@gmail.com']" is present

  Scenario: Log out from the main page
    Given Open "prod" url
    Then Wait for "2" seconds
    Then Type "grishina.ermashkevich@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "Ven12345@" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "5" seconds
    And Verify element "//div[text()='grishina.ermashkevich@gmail.com']" is present
    Then Wait for "2" seconds
    Then Click on element "//button[@class = 'left-panel_list_element_link__ycxmi left-panel_logout__3wDO1']"
    Then Wait for "2" seconds
    And Verify element "//span[text()='Login']" is present

  Scenario: Go to the Photos section from the main page
    Given Open "prod" url
    Then Wait for "2" seconds
    Then Type "grishina.ermashkevich@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "Ven12345@" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    Then Click on element "//p[text() = 'Photos']"
    Then Wait for "2" seconds
    And Verify element "//span[text()='Create album']" is present

  Scenario: Go to the Videos section from the main page
    Given Open "prod" url
    Then Wait for "2" seconds
    Then Type "grishina.ermashkevich@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "Ven12345@" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    Then Click on element "//p[text() = 'Videos']"
    Then Wait for "2" seconds
    And Verify element "//span[text()='Create video album']" is present

  Scenario: Go to the Calendar section from the main page
    Given Open "prod" url
    Then Wait for "2" seconds
    Then Type "grishina.ermashkevich@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "Ven12345@" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    Then Click on element "//p[text() = 'Calendar']"
    Then Wait for "2" seconds
    And Verify element "//button[@class='react-calendar__navigation__arrow react-calendar__navigation__prev2-button']" is present

  Scenario: Go to the Personal info section from the main page
    Given Open "prod" url
    Then Wait for "2" seconds
    Then Type "grishina.ermashkevich@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "Ven12345@" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    Then Click on element "//p[text() = 'Personal Info']"
    Then Wait for "2" seconds
    And Verify element "//div[text()='Personal Info']" is present

  Scenario: Go to the Messages section from the main page
    Given Open "prod" url
    Then Wait for "2" seconds
    Then Type "grishina.ermashkevich@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "Ven12345@" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    Then Click on element "//p[text() = 'Messages']"
    Then Wait for "2" seconds
    And Verify element "//b[text()='SEND MESSAGES']" is present

  Scenario: Go to the Settings section from the main page
    Given Open "prod" url
    Then Wait for "2" seconds
    Then Type "grishina.ermashkevich@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "Ven12345@" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    Then Click on element "//p[text() = 'Settings']"
    Then Wait for "2" seconds
    And Verify element "//a[text()='Privacy']" is present

  Scenario: Go to the Settings section from the main page
    Given Open "prod" url
    Then Wait for "2" seconds
    Then Type "grishina.ermashkevich@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "Ven12345@" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    Then Click on element "//p[text() = 'Contact us']"
    Then Wait for "2" seconds
    And Verify element "//div[text()='Contact us']" is present

  Scenario: Go to Change language section from the main page
    Given Open "prod" url
    Then Wait for "2" seconds
    Then Type "grishina.ermashkevich@gmail.com" in field "//input[@placeholder='Email Address']"
    Then Wait for "2" seconds
    Then Type "Ven12345@" in field "//input[@placeholder='Password']"
    Then Wait for "2" seconds
    Then Click on element "//button[contains(@class, 'ant-btn')]"
    Then Wait for "2" seconds
    Then Click on element "//span[@class='ant-select-selection-item']"
    Then Wait for "2" seconds

  Scenario: Toggle notifications
    Given Open "prod" url
    Then Login as "user1"
    Then Click on element "Settings"
    Then Click on element "Notifications"
    Then Click on element "password_change"
    Then Click on element "connections"
    Then Click on element "birthdays"
    Then Click on element "likes"
    Then Wait for "2" seconds

  Scenario: Select Privacy settings
    Given Open "prod" url
    Then Login as "user1"
    Then Click on element "Settings"
    Then Click on element "//a[text()='Privacy']"
    Then Click on element "//input[@id = 'rc_select_1']"
    Then Click on element "//input[@id = 'rc_select_1'][./span[text() = 'Public']"











