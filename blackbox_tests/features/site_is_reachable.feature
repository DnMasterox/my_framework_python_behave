# Created by mshuma at 9/25/19
Feature: Site is reachable
  Before any testing there is need to be sure the site is UP

  Scenario: Request should have response 200
    Given user send request to URL
    When response is given back
    Then status code should be 200