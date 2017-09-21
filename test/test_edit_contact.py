
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(name="Tasha", mobile="888888888", email="tasha@gmail.com"))
    app.session.logout()