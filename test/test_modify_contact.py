from model.contact import Contact
import random


def test_modify_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="New contact"))
    old_contact = db.get_contact_list()
    select_contact = random.choice(old_contact)
    contact = Contact(firstname="Natasha")
    app.contact.modify_contact_by_id(select_contact.id, contact)
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[old_contact.index(select_contact)].firstname = contact.firstname
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


# def test_modify_contact_mobile(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(name="New contact"))
#     old_contact = app.contact.get_contact_list()
#     app.contact.modify_contact(Contact(mobile="888888888"))
#     new_contact = app.contact.get_contact_list()
#     assert len(old_contact) == len(new_contact)