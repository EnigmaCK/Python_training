# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
        old_contact = app.contact.get_contact_list()
        app.contact.create(Contact(name="Natasha", mobile="55555555555", email="nataliia.hubenko@gmail.com"))
        new_contact = app.contact.get_contact_list()
        assert len(old_contact) +1 == len(new_contact)


def test_add_second_contact(app):
        old_contact = app.contact.get_contact_list()
        app.contact.create(Contact(name="Max", mobile="454545454545", email="max@gmail.com"))
        new_contact = app.contact.get_contact_list()
        assert len(old_contact) + 1 == len(new_contact)
