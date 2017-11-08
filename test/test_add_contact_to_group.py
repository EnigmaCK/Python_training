from model.group import Group
from model.contact import Contact
import random
from fixture.orm import ORMFixture

db = ORMFixture(host='127.0.0.1', name="addressbook", user="root", password="")

def test_add_contact_to_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test group"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="New contact"))
    all_groups = db.get_group_list()
    select_random_group = random.choice(all_groups)
    old_contacts_in_group = db.get_contacts_in_group(select_random_group)
    all_contacts = db.get_contact_list()
    select_random_contact = random.choice(all_contacts)
    app.contact.add_contact_to_group(select_random_contact.id, select_random_group.id)
    new_contacts_in_group = db.get_contacts_in_group(select_random_group)
    if select_random_contact not in old_contacts_in_group:
        old_contacts_in_group.append(select_random_contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)