
from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="New contact"))
    app.contact.modify_contact(Contact(name="Tasha"))


def test_modify_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="New contact"))
    app.contact.modify_contact(Contact(mobile="888888888"))