Feature: Test the search functionality in the homepage of ebay

  Background:
    Given Home page: I am on ebay homepage

    @T1 @regressionTesting
  Scenario Outline: Check that the user can make a simple search in the ebay homepage
    When Home page: I search for "<product_name>" from category "<category_name>"
    Then Home page: I received as a results also iPhone8 64GB
      @electronics
      Examples:
      |product_name   |category_name|
      |iphone         |Cell Phones & Accessories|
      |TV             |Consumer Electronics     |

      @T2 @sanityTesting
  Scenario Outline: Check that the user can make an advanced search for product
    When Home page: I click on the advanced link
    When Advanced search page: I type "Pampers" in the text box
    When Advanced search page: I select "Exact words, exact order" from dropdown list
    When Advanced search page: I select "Baby" from the category list
    When Advanced search page: I click search button
    Then Advanced search page : I have at least 800 results returned