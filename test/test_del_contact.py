from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="f_name", middle_name="m_name", last_name="l_name"))
    app.contact.delete_first()