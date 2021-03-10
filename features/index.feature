Feature: Index to list page
"""
Confirmation that we can navigate correctly through the starting pages on this site and navigate to other pages from it.
"""

Scenario: Successfully accessed the index page and the navigation link on the index page are working correctly.
    Given I navigate to the index page and I can see the navigation link
    When I click on the navigation link
    Then I should be navigated to the anime list page