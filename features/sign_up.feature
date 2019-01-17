Feature: signup

  Scenario: Successfully create an account

    Given I am a new user
    When I fill signup form
    Then User account should be created