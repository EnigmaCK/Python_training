
from model.contact import Contact


def test_modify_contact_name(app):
    app.contact.modify_contact(Contact(name="Tasha"))


def test_modify_contact_mobile(app):
    app.contact.modify_contact(Contact(mobile="888888888"))