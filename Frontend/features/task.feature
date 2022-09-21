Feature: Task tests

    Background: User accesses website an login
        Given I navigate to todo app page
        And I insert email as "adrielson.rodrigues@gmail.com" and password as "assessmentqa" and click sign in
        And I am on QA Assessment page

    Scenario: User sees welcome message
        Given I have clicked on My tasks
        Then I see welcome message for "Adrielson" is displayed
        And I sign out the application

    Scenario: User adds a new task by clicking '+' button and remove it
        Given I have clicked on My tasks
        When I create a task named "Testing"
        Then I am able to see the task "Testing" on the list and remove it
        And I sign out the application

    Scenario: User adds a new task by pressing enter and remove it
        Given I have clicked on My tasks
        When I create a task named "Testing" by pressing enter
        Then I am able to see the task "Testing" on the list and remove it
        And I sign out the application

    Scenario: User tries to add a task with more than 250 characters
        Given I have clicked on My tasks
        When I create a task with more than 250 characters by pressing enter
        Then I am able to see until the 250th character of the task on the list and remove it
        And I sign out the application