
from model.contact import Contact
from pytest_bdd import given, when, then
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <lastname> and <mobile>')
def new_contact(firstname, lastname, mobile):
    return Contact(firstname=firstname, lastname=lastname, mobile=mobile)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then("the new contact list is equal to the old list with the added contact")
def verify_group_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='Some name'))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_random_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then("the new contact list is equal to the old list without the deleted contact")
def verify_deleted_contact(app, db, non_empty_contact_list, random_contact, check_ui):
    old_contacts = non_empty_contact_list
    new_contact = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contact)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contact
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                    key=Contact.id_or_max)

@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='Some name'))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@given('parameters to modify')
def contact_parameters():
    return Contact(firstname='Anny')


@when('I modify the contact in the list')
def delete_random_contact(app, random_contact, contact_parameters):
    app.contact.modify_contact_by_id(random_contact.id, contact_parameters)


@then("the new contact list is equal to the old list with the modified contact")
def verify_deleted_contact(app, db, non_empty_contact_list, random_contact, contact_parameters, check_ui):
    old_contacts = non_empty_contact_list
    new_contact = db.get_contact_list()
    assert len(old_contacts) == len(new_contact)
    old_contacts[old_contacts.index(random_contact)].firstname = contact_parameters.firstname
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                    key=Contact.id_or_max)
