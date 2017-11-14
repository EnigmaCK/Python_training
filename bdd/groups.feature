Scenario Outline: Add new group
  Given a group list
  Given a group with <name>, <header> and <footer>
  When I add the group to the list
  Then the new group list is equal to the old list with the added group

  Examples:
  | name | header| footer |
  | test | test_h | test_f |
  | test1 | test_h1 | test_f1 |


Scenario Outline: Delete a group
  Given a non-empty group list
  Given a random group from the list
  When I delete the group from the list
  Then the new group list is equal to the old list without the deleted group


Scenario Outline: Modify a group
  Given a non-empty group list
  Given a random group from the list
  Given parameters to modify
  When I modify the group in the list
  Then the new  list is equal to the old list with the modified group


