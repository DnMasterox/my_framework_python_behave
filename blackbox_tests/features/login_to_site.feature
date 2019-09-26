# Created by Mykola Shumakov
@php_travel
Feature: Login to site
  User should always be able to post.
  It is important that the login always works.

  Scenario: Should see navigation bar
    Given user navigates to the URL
    When user logs in
    Then user should be able to see profile page
#    And the navigation bar should include the following "<columns>":
#
#    Examples:
#      | Column  |
#      | HOTELS  |
#      | FLIGHTS |
#      | TOURS   |
#      | CARS    |
#
#
#  Scenario Outline: User logs in to site
#    Given user navigates to the URL
#    When "<user>" logs in
#    Then the twitter timeline appears
#
#    Examples: users
#      | user        |
#      | GlobalEntry |