from model.contact import Contact


def test_delete_first_contact(app):
    old_contact_list = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="f_name", middle_name="m_name", last_name="l_name"))
    app.contact.delete_first()
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact_list)
    old_contact_list[0:1] = []
    assert old_contact_list == new_contact_list