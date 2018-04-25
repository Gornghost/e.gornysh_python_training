from model.contact import Contact


def test_edit_first_contact_general_info(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(first_name=" EDITED", middle_name=" EDITED", last_name=" EDITED", nickname=" EDITED",
                        title=" EDITED", company=" EDITED", address=" EDITED", home_phone=" EDITED",
                        mobile_phone=" EDITED", work_phone=" EDITED", fax=" EDITED", email1=" EDITED",
                        email2=" EDITED", email3=" EDITED", homepage_link=" EDITED",
                        birthday_day="//div[@id='content']/form/select[1]//option[3]",
                        birthday_month="//div[@id='content']/form/select[2]//option[3]", birthday_year=" EDITED",
                        anniversary_day="//div[@id='content']/form/select[3]//option[3]",
                        anniversary_month="//div[@id='content']/form/select[4]//option[3]", anniversary_year=" EDITED",
                        secondary_address=" EDITED", home_phone2=" EDITED", notes=" EDITED"))
    app.session.logout()


def test_edit_first_contact_emails(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(first_name=" EDITED", middle_name=" EDITED", last_name=" EDITED", nickname=" EDITED",
                        title=" EDITED", company=" EDITED", address=" EDITED", home_phone=" EDITED",
                        mobile_phone=" EDITED", work_phone=" EDITED", fax=" EDITED", email1=" EDITED",
                        email2=" EDITED", email3=" EDITED", homepage_link=" EDITED",
                        birthday_day="//div[@id='content']/form/select[1]//option[3]",
                        birthday_month="//div[@id='content']/form/select[2]//option[3]", birthday_year=" EDITED",
                        anniversary_day="//div[@id='content']/form/select[3]//option[3]",
                        anniversary_month="//div[@id='content']/form/select[4]//option[3]", anniversary_year=" EDITED",
                        secondary_address=" EDITED", home_phone2=" EDITED", notes=" EDITED"))
    app.session.logout()