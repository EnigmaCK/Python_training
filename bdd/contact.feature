Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname> and <mobile>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname | lastname | mobile |
  | Natasha   | Hubenko  | 555555 |
  | Alina     | Smith    | 333333 |

Scenario Outline: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact

Scenario Outline: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given parameters to modify
  When I modify the contact in the list
  Then the new contact list is equal to the old list with the modified contact

