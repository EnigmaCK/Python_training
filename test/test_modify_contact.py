
from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="New contact"))
    old_contact = app.contact.get_contact_list()
    contact = Contact(name="Tasha")
    contact.id = old_contact[0].id
    app.contact.modify_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# def test_modify_contact_mobile(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(name="New contact"))
#     old_contact = app.contact.get_contact_list()
#     app.contact.modify_contact(Contact(mobile="888888888"))
#     new_contact = app.contact.get_contact_list()
#     assert len(old_contact) == len(new_contact)