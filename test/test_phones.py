import re


def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.home_phone == clear(contact_from_editpage.home_phone)
    assert contact_from_homepage.mobile_phone == clear(contact_from_editpage.mobile_phone)
    assert contact_from_homepage.work_phone == clear(contact_from_editpage.work_phone)
    assert contact_from_homepage.home_phone2 == clear(contact_from_editpage.home_phone2)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_editpage.home_phone
    assert contact_from_view_page.mobile_phone == contact_from_editpage.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_editpage.work_phone
    assert contact_from_view_page.home_phone2 == contact_from_editpage.home_phone2


def clear(s):
    return re.sub("[() -]", "", s)