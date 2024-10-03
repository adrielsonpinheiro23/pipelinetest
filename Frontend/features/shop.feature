Feature: Shopping tests

    Background: User accesses website
        Given I navigate to sauce demo page

    Scenario: Standard User performs the shopping process
        Given I insert username as "standard_user" and password as "secret_sauce" and click login
        And I am successfully logged in
        When I insert all the products in the cart
        And Finish the checkout to payment with names "Adrielson" and "Pinheiro" with zip code "2720-164"
        And I check the amount of "140.34" and click Finish
        Then I receive a notification of success
        And I click on Back Home to return to "Products" Page

    Scenario: Problem user performs the shopping process
        Given I insert username as "problem_user" and password as "secret_sauce" and click login
        And I am successfully logged in
       # TO-DO - This step is going to fail the test due BUG ID RIN1748
        When I insert all the products in the cart
        # TO-DO - This step is going to fail the test due BUG ID RIN1749
        And Finish the checkout to payment with names "Adrielson" and "Pinheiro" with zip code "2720-164"
        And I check the amount of "140.34" and click Finish
        Then I receive a notification of success
        And I click on Back Home to return to "Products" Page

    Scenario: Performance problem user performs the shopping process
        Given I insert username as "performance_glitch_user" and password as "secret_sauce" and click login
        And I am successfully logged in
        When I insert all the products in the cart
        And Finish the checkout to payment with names "Adrielson" and "Pinheiro" with zip code "2720-164"
        And I check the amount of "140.34" and click Finish
        Then I receive a notification of success
        And I click on Back Home to return to "Products" Page

    Scenario: Error user user performs the shopping process
        Given I insert username as "error_user" and password as "secret_sauce" and click login
        And I am successfully logged in
        When I insert all the products in the cart
        # TO-DO - This step is going to fail the test due BUG ID RIN1748
        And Finish the checkout to payment with names "Adrielson" and "Pinheiro" with zip code "2720-164"
        # TO-DO - This step is going to pass, but it should fail the test due BUG ID RIN1750
        And I check the amount of "140.34" and click Finish
        # TO-DO - This step is going to fail the test due BUG ID RIN1748
        Then I receive a notification of success
        And I click on Back Home to return to "Products" Page

    Scenario: Standard user removes the products on shopping cart
        Given I insert username as "standard_user" and password as "secret_sauce" and click login
        And I am successfully logged in
        When I insert all the products in the cart
        And I remove the "t-shirt" products
        And Finish the checkout to payment with names "Adrielson" and "Pinheiro" with zip code "2720-164"
        And I check the amount of "105.80" and click Finish
        Then I receive a notification of success
        And I click on Back Home to return to "Products" Page

    Scenario: Standard user removes the products before going to cart
        Given I insert username as "standard_user" and password as "secret_sauce" and click login
        And I am successfully logged in
        When I insert all the products in the cart
        And I remove the "t-shirt" products
        And I return to "Products" Page and remove the "backpack" product
        And Finish the checkout to payment with names "Adrielson" and "Pinheiro" with zip code "2720-164"
        And I check the amount of "73.41" and click Finish
        Then I receive a notification of success
        And I click on Back Home to return to "Products" Page

#     """BUG ID RIN1748: It's not possible to add some products on the cart for error user and problem user """
#     """BUG ID RIN1749: The last name field is returning to first name field """
#     """BUG ID RIN1750: It's being possible to Continue to Payment without inserting Last name for error_user """