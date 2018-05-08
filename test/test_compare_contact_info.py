import re
from random import randrange


def test_contact_data_on_homepage(app):
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_from_homepage = contact_list[index]
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.last_name == contact_from_editpage.last_name
    assert contact_from_homepage.first_name == contact_from_editpage.first_name
    assert contact_from_homepage.address == contact_from_editpage.address
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_editpage)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_editpage)


# def test_phones_on_contact_view_page(app):
#    contact_from_view_page = app.contact.get_contact_from_view_page(0)
#    contact_from_editpage = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_view_page.home_phone == contact_from_editpage.home_phone
#    assert contact_from_view_page.mobile_phone == contact_from_editpage.mobile_phone
#    assert contact_from_view_page.work_phone == contact_from_editpage.work_phone
#    assert contact_from_view_page.home_phone2 == contact_from_editpage.home_phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.home_phone2]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join([contact.email1, contact.email2, contact.email3])