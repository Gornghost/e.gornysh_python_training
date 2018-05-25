import re
from model.contact import Contact


def test_contact_data_on_homepage(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(first_name="TEST"))
    contact_list_ui = app.contact.get_contact_list()
    contact_list_db = db.get_contact_list()
    emails_list_from_homepage = app.contact.get_emails_list_from_homepage(contact_list_ui)
    emails_list_from_db = get_emails_list_from_db(contact_list_db)
    phones_list_from_homepage = app.contact.get_phones_list_from_homepage(contact_list_ui)
    phones_list_from_db = get_phones_list_from_db(contact_list_db)
    assert sorted(contact_list_db, key=Contact.id_or_max) == sorted(contact_list_ui, key=Contact.id_or_max)
    assert sorted(emails_list_from_homepage) == sorted(emails_list_from_db)
    assert sorted(phones_list_from_homepage) == sorted(phones_list_from_db)

def get_phones_list_from_db(contact_list_db):
    phones_list_db = []
    for contact in contact_list_db:
        phones_list_db.append(merge_phones_like_on_homepage(contact))
    return phones_list_db


def get_emails_list_from_db(contact_list_db):
    emails_list_db = []
    for contact in contact_list_db:
        emails_list_db.append(merge_emails_like_on_homepage(contact))
    return emails_list_db

def clear(s):
    return re.sub("[(). -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.home_phone2]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email1, contact.email2, contact.email3])))