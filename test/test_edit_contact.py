from model.contact import Contact


def test_edit_first_contact_general_info(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="TEST"))
    app.contact.edit_first(Contact(first_name=" EDITED", middle_name=" EDITED", last_name=" EDITED", nickname=" EDITED",
                                   title=" EDITED", company=" EDITED", address=" EDITED"))


def test_edit_first_contact_phone_info(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="TEST"))
    app.contact.edit_first(Contact(home_phone=" EDITED", mobile_phone=" EDITED", work_phone=" EDITED", fax=" EDITED"))


def test_edit_first_contact_email_info(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="TEST"))
    app.contact.edit_first(Contact(email1=" EDITED", email2=" EDITED", email3=" EDITED"))


def test_edit_first_contact_other_info(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="TEST"))
    app.contact.edit_first(Contact(homepage_link=" EDITED", birthday_day="//div[@id='content']/form/select[1]//option[3]",
                                   birthday_month="//div[@id='content']/form/select[2]//option[3]",
                                   birthday_year=" EDITED", anniversary_day="//div[@id='content']/form/select[3]//option[3]",
                                   anniversary_month="//div[@id='content']/form/select[4]//option[3]",
                                   anniversary_year=" EDITED", secondary_address=" EDITED", home_phone2=" EDITED",
                                   notes=" EDITED"))