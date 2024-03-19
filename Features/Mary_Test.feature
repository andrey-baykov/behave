Feature: Test login page
#  These tests are for the login page


    Scenario Verify 'Send' button is displayed for Logged In user next to 'What's in your mind' field
        Given Open url "https://www.lifetwig.com/"
        Then Type "marysavchuk23@gmail.com" in field "//input[@placeholder='Email Address']"
        Then Wait for "2" seconds
        Then Type "Qwerty12345!" in field "//input[@placeholder='Password']"
        Then Wait for "2" seconds
        Then Click on element "//button[contains(@class, 'ant-btn')]"
        Then Wait for "5" seconds
        And Verify element "//button[@class='ant-btn feed-input-form_confirm_button__1efmF']" is present

    Scenario Verify 'Logout' button is displayed
        Given Open url "https://www.lifetwig.com/"
        Then Type "marysavchuk23@gmail.com" in field "//input[@placeholder='Email Address']"
        Then Wait for "2" seconds
        Then Type "Qwerty12345!" in field "//input[@placeholder='Password']"
        Then Wait for "2" seconds
        Then Click on element "//button[contains(@class, 'ant-btn')]"
        Then Wait for "5" seconds
        And Verify element "//button[@class='left-panel_list_element_link__ycxmi left-panel_logout__3wDO1']" is present

    Scenario Verify 'Logout' button is functional
        Given Open url "https://www.lifetwig.com/"
        Then Type "marysavchuk23@gmail.com" in field "//input[@placeholder='Email Address']"
        Then Wait for "2" seconds
        Then Type "Qwerty12345!" in field "//input[@placeholder='Password']"
        Then Wait for "2" seconds
        Then Click on element "//button[contains(@class, 'ant-btn')]"
        Then Wait for "5" seconds
        Then Click on element "//button[@class='left-panel_list_element_link__ycxmi left-panel_logout__3wDO1']"
        Then Wait for "2" seconds
        And Verify element "//div[@class='auth_login_form_header__Zxwk6']" is present

    Scenario Navigate to My Albums
        Given Open url "https://www.lifetwig.com/"
        Then Type "marysavchuk23@gmail.com" in field "//input[@placeholder='Email Address']"
        Then Wait for "2" seconds
        Then Type "Qwerty12345!" in field "//input[@placeholder='Password']"
        Then Wait for "2" seconds
        Then Click on element "//button[contains(@class, 'ant-btn')]"
        Then Wait for "5" seconds
        Then Click on element "//p[text()='Photos']"
        Then Wait for "2" seconds
        And Verify element "//span[text()='My albums']" is present

    Scenario Create Album input field to be displayed
        Given Open url "https://www.lifetwig.com/"
        Then Type "marysavchuk23@gmail.com" in field "//input[@placeholder='Email Address']"
        Then Wait for "2" seconds
        Then Type "Qwerty12345!" in field "//input[@placeholder='Password']"
        Then Wait for "2" seconds
        Then Click on element "//button[contains(@class, 'ant-btn')]"
        Then Wait for "5" seconds
        Then Click on element "//p[text()='Photos']"
        Then Wait for "2" seconds
        Then Click on element "//span[text()='Create album']"
        Then Wait for "2" seconds
        And Verify element "//input[@class='ant-input']" is present

    Scenario Navigate to Videos
        Given Open url "https://www.lifetwig.com/"
        Then Type "marysavchuk23@gmail.com" in field "//input[@placeholder='Email Address']"
        Then Wait for "2" seconds
        Then Type "Qwerty12345!" in field "//input[@placeholder='Password']"
        Then Wait for "2" seconds
        Then Click on element "//button[contains(@class, 'ant-btn')]"
        Then Wait for "5" seconds
        Then Click on element "//p[text()='Videos']"
        Then Wait for "2" seconds
        And Verify element "//span[text()='Create video album']" is present

    Scenario: Navigate to Calendar
        Given Open url "https://www.lifetwig.com/"
        Then Type "marysavchuk23@gmail.com" in field "//input[@placeholder='Email Address']"
        Then Wait for "2" seconds
        Then Type "Qwerty12345!" in field "//input[@placeholder='Password']"
        Then Wait for "2" seconds
        Then Click on element "//button[contains(@class, 'ant-btn')]"
        Then Wait for "5" seconds
        Then Click on element "//p[text()='Calendar']"
        Then Wait for "2" seconds
        And Verify element "//div[@class='react-calendar calendar_calendar__oX1rf']" is present

    Scenario: Navigate to Personal info
        Given Open url "https://www.lifetwig.com/"
        Then Type "marysavchuk23@gmail.com" in field "//input[@placeholder='Email Address']"
        Then Wait for "2" seconds
        Then Type "Qwerty12345!" in field "//input[@placeholder='Password']"
        Then Wait for "2" seconds
        Then Click on element "//button[contains(@class, 'ant-btn')]"
        Then Wait for "5" seconds
        Then Click on element "//p[text()='Personal Info']"
        Then Wait for "2" seconds
        And Verify element "//div[@class='personal-info_header__15Eu5']" is present

    Scenario: Navigate to Messages
        Given Open url "https://www.lifetwig.com/"
        Then Type "marysavchuk23@gmail.com" in field "//input[@placeholder='Email Address']"
        Then Wait for "2" seconds
        Then Type "Qwerty12345!" in field "//input[@placeholder='Password']"
        Then Wait for "2" seconds
        Then Click on element "//button[contains(@class, 'ant-btn')]"
        Then Wait for "5" seconds
        Then Click on element "//p[text()='Messages']"
        Then Wait for "2" seconds
        And Verify element "//b[text()='SEND MESSAGES']" is present

    Scenario: 'Start new group chat' button is functional
        Given Open url "https://www.lifetwig.com/"
        Then Type "marysavchuk23@gmail.com" in field "//input[@placeholder='Email Address']"
        Then Wait for "2" seconds
        Then Type "Qwerty12345!" in field "//input[@placeholder='Password']"
        Then Wait for "2" seconds
        Then Click on element "//button[contains(@class, 'ant-btn')]"
        Then Wait for "5" seconds
        Then Click on element "//p[text()='Messages']"
        Then Wait for "2" seconds
        Then Click on element "//button[text()='start new group chat']"
        Then Wait for "2" seconds
        And Verify element "//div[text()='Name your group chat and add people']" is present

