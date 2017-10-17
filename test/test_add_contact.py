# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
        old_contact = app.contact.get_contact_list()
        contact = Contact(name="Natasha", lastname="H", homephone="648",
                          mobile="55555555555", workphone="+0000", secondaryphone="125895",
                          email="nataliia.hubenko@gmail.com")
        app.contact.create(contact)
        assert len(old_contact) +1 == app.contact.count()
        new_contact = app.contact.get_contact_list()
        old_contact.append(contact)
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


# def test_add_second_contact(app):
#         old_contact = app.contact.get_contact_list()
#         contact = Contact(name="Max", mobile="454545454545", email="max@gmail.com")
#         app.contact.create(contact)
#         new_contact = app.contact.get_contact_list()
#         assert len(old_contact) + 1 == len(new_contact)
#         old_contact.append(contact)
#         assert sorted(old_contact, key=Contact.id_or_max) == sorted(old_contact, key=Contact.id_or_max)
