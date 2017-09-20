# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(name="Natasha", mobile="55555555555", email="nataliia.hubenko@gmail.com"))
        app.session.logout()


def test_add_second_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(name="Max", mobile="454545454545", email="max@gmail.com"))
        app.session.logout()

