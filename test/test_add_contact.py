# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(first_name="Eugene", middle_name="Mykolayovich", last_name="Gornysh", nickname="Gorn",
                      title="Title test", company="Company test", address="Address test", home_phone="+123456789",
                      mobile_phone="+123456789", work_phone="+987654321", fax="+654321987", email1="test@test.te",
                      email2="mail@test.te", email3="mail2@test.te", homepage_link="Homepage test",
                      birthday_day="//div[@id='content']/form/select[1]//option[3]",
                      birthday_month="//div[@id='content']/form/select[2]//option[2]", birthday_year="1981",
                      anniversary_day="//div[@id='content']/form/select[3]//option[4]",
                      anniversary_month="//div[@id='content']/form/select[4]//option[3]", anniversary_year="1992",
                      secondary_address="Secondary address", home_phone2="Home test", notes="Notes test")
    app.contact.create_contact(contact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) + 1 == len(new_contact_list)
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#    old_contact_list = app.contact.get_contact_list()
#    app.contact.create_contact(Contact(first_name="", middle_name="", last_name="", nickname="", title="",
#                                       company="", address="", home_phone="", mobile_phone="", work_phone="",
#                                       fax="", email1="", email2="", email3="", homepage_link="", birthday_year="",
#                                       anniversary_year="", secondary_address="", home_phone2="", notes=""))
#    new_contact_list = app.contact.get_contact_list()
#    assert len(old_contact_list) + 1 == len(new_contact_list)