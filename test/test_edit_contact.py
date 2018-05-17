from model.contact import Contact
from random import randrange


def test_edit_first_contact_general_info(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(first_name="TEST"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    contact = Contact(first_name="EDITED", middle_name="EDITED", last_name="EDITED", nickname="EDITED",
                      title="EDITED", company="EDITED", address="EDITED")
    contact.id = old_contact_list[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contact_list) == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)