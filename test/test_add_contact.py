import pytest
from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(name="", lastname="", email="", address="", mobile="", homephone="")] + [
    Contact(name=random_string("name", 10), lastname=random_string("lastname", 10), address=random_string("address", 15),
            mobile=random_string("159", 10), homephone=random_string("3578", 5))
    for i in range(1)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
        old_contact = app.contact.get_contact_list()
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
