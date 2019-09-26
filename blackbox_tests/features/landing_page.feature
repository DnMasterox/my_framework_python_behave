# Created by mshuma at 9/26/19
Feature:  Landing Page
  # Enter feature description here

  Scenario Outline: Should see navigation bar
    When user open landing page
    Then user should be able to see landing page
    And the navigation bar should include the following "<column>"
    Examples:
      | column  |
      | HOTELS  |
#      | FLIGHTS |
#      | TOURS   |
#      | CARS    |


#  Scenario Outline: Should find appropriate car
#    When user open landing page
#    And I choose "<option>" tab
#    And I select "<pick_up>" and "<drop_off>" location
#    And I search query
#    Then I should be able to see notification "<message>"
#    Examples:
#      | option | pick_up    | drop_off | message          |
#      | cars   | Manchester | Malaysia | No Results Found |