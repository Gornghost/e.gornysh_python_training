from model.contact import Contact
import random


def test_edit_contact_general_info(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(first_name="TEST"))
    old_contact_list = db.get_contact_list()
    contact = random.choice(old_contact_list)
    new_contact_data = Contact(first_name="EDITED", middle_name="EDITED", last_name="EDITED", nickname="EDITED",
                      title="EDITED", company="EDITED", address="EDITED")
    new_contact_data.id = contact.id
    app.contact.edit_contact_by_id(new_contact_data.id, new_contact_data)
    new_contact_list = db.get_contact_list()
    index = old_contact_list.index(contact)
    old_contact_list[index] = new_contact_data
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)