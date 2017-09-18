# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_contact import ApplicationContact


@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        app.login(username="admin", password="secret")
        app.create_new_contact(Contact(name="Natasha", mobile="55555555555", email="nataliia.hubenko@gmail.com"))
        app.logout()


def test_add_second_contact(app):
        app.login(username="admin", password="secret")
        app.create_new_contact(Contact(name="Max", mobile="454545454545", email="max@gmail.com"))
        app.logout()

