
from model.contact import Contact
import re


def test_contact_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="New contact"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_contact_data_like_on_home_page(contact_from_edit_page, "phone")
    assert contact_from_home_page.all_emails_from_home_page == merge_contact_data_like_on_home_page(contact_from_edit_page, "email")
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.name == contact_from_edit_page.name
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname


# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#     assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#     assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_contact_data_like_on_home_page(contact, param):
    if param == "phone":
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.homephone, contact.mobile, contact.workphone,
                                            contact.secondaryphone]))))
    elif param == "email":
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.email, contact.secondemail, contact.thirdemail]))))
    else:
        print("Wrong parameter")