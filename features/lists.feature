Feature: List page
  """
  Confirmation that we can navigate the Anime list page correctly on this site, and from there to the Anime details page.
  """

  Scenario: From list page navigate to Anime details
    Given The Anime list page is successfully accessed and the list on the Anime list page are being used correctly
    When I click on the link to the Anime details
    Then I should be navigated to the Anime details page

  Scenario: Pagination feature availability - Next page
    Given I navigate to the Anime list page
    When I click on the link to the Next page
    Then I should be navigated to the next Anime list page

  Scenario: Pagination feature availability - Specifying a page number
    Given I navigate to the Anime list page
    When I click on the link to a page number
    Then I should be navigated to the page number of Anime list page