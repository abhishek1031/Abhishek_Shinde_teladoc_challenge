Feature: Add user to the table
  Scenario: User addition successful
    Given Launch the Chrome Browser
    When open given url
    Then  click on add user button
    Then add user details
    Then  click on save button
    And assert user added
    And close browser


