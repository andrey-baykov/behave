Feature: Homework
  # Enter feature description here
  Background:
    Given Open "prod" url
    Then Wait for "2" seconds

  Scenario Outline:
    Then Type "<email>" in field "//input[@placeholder='Email Address']"
    Then Type "<password>" in field "//input[@placeholder='Password']"
    Then Click on element "//button[contains(@class, 'ant-btn')]"

    Examples:
      | email                           | password  |
      | pcs.class1223@gmail.com         | !Qwerty&8 |
      | grishina.ermashkevich@gmail.com | Ven12345@ |
