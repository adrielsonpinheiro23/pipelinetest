Feature: Login tests

    Background: User accesses website
        Given I navigate to sauce demo page

    Scenario: User is able to login with standard user
        Given I insert username as "standard_user" and password as "secret_sauce" and click login
        Then I am successfully logged in
        And I click to Logout

    Scenario: User is not able to login with locked out user
        Given I insert username as "locked_out_user" and password as "secret_sauce" and click login
        Then I am not logged in due locked user error message

    Scenario: User is able to login with problem user
        Given I insert username as "problem_user" and password as "secret_sauce" and click login
        Then I am successfully logged in
        And I click to Logout

    Scenario: User is able to login with performance glitch user
        Given I insert username as "performance_glitch_user" and password as "secret_sauce" and click login
        Then I am successfully logged in
        And I click to Logout

    Scenario: User is able to login with error user
        Given I insert username as "error_user" and password as "secret_sauce" and click login
        Then I am successfully logged in
        And I click to Logout

    Scenario: User is able to login with visual user
        Given I insert username as "visual_user" and password as "secret_sauce" and click login
        Then I am successfully logged in
        And I click to Logout

    Scenario: User is not able to login with invalid user
        Given I insert username as "invalid" and password as "secret_sauce" and click login
        Then I am not logged in due invalid user or password error message

    Scenario: User is not able to login with invalid password
        Given I insert username as "standard_user" and password as "wrongpass" and click login
        Then I am not logged in due invalid user or password error message
