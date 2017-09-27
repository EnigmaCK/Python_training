
from model.contact import Contact


def test_modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(name="Tasha"))
    app.session.logout()


def test_modify_contact_mobile(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(mobile="888888888"))
    app.session.logout()