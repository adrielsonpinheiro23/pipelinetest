Feature: Subtask tests

    Background: User accesses website an login
        Given I navigate to todo app page
        And I insert email as "adrielson.rodrigues@gmail.com" and password as "assessmentqa" and click sign in
        And I am on QA Assessment page
        And I have clicked on My tasks

    Scenario: User is able to see Manage task button
        Given I create a task named "Testing" by pressing enter
        Then I am able to see the in the task the button "Manage Subtasks"
        And I sign out the application

    Scenario: User counts the number of created subtasks
        Given I create a task named "Testing" by pressing enter
        And I click the button Manage Subtasks
        And I create a subtask with description as "subtask test"
        And I create a subtask with description as "subtask test 2"
        And I create a subtask with description as "subtask test 3"
        When I close the modal
        Then I can see there are "3" subtasks created
        And I sign out the application

    Scenario: User tries to edit task name on subtask modal
        Given I create a task named "Testing" by pressing enter
        When I click the button Manage Subtasks
        Then I check if task name on modal is editable
        And I sign out the application
