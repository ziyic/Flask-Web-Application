Feature: List page
    """
    Confirmation that we can navigate the Anime list page correctly on this site, and from there to the Anime details page.
    """

  Scenario: Back feature availability
    Given I navigate to the Anime details page
    When I click on the Back link
    Then I should be navigated to Anime list page

  Scenario: Home feature availability
    Given I navigate to the Anime details page
    When I click on the Home link
    Then I should be navigated to the index page