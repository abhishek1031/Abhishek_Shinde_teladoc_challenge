Feature: delete user to the table
  Scenario: User deletion successful
    Given Launch the Chrome Browser
    When open given url
    Then delete selected user
    Then confirm deletion
    Then assert user deleted
    And close browser