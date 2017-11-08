from model.group import Group
from model.contact import Contact
import random


def test_del_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test group"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="New contact"))
    all_groups = db.get_group_list()
    select_random_group = random.choice(all_groups)
    if len(db.get_contacts_in_group(select_random_group)) == 0:
        all_contacts = db.get_contact_list()
        select_random_contact = random.choice(all_contacts)
        app.contact.add_contact_to_group(select_random_contact.id, select_random_group.id)
    contacts_in_group = db.get_contacts_in_group(select_random_group)
    contact_in_group = random.choice(contacts_in_group)
    app.contact.del_contact_from_group(contact_in_group.id, select_random_group.id)
    new_contacts_in_group = db.get_contacts_in_group(select_random_group)
    contacts_in_group.remove(contact_in_group)
    assert sorted(contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)