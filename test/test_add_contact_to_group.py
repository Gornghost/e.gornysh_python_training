from model.contact import Contact
from model.group import Group
import random


def test_add_random_contact_to_random_group(app, db, orm_db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(first_name="f_name", middle_name="m_name", last_name="l_name"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="TEST"))
    group = random.choice(db.get_group_list())
    if len(orm_db.get_contacts_not_in_group(Group(id=group.id))) == 0:
        contacts_in_group = orm_db.get_contacts_in_group(Group(id=group.id))
        contact = random.choice(contacts_in_group)
        app.contact.delete_contact_by_id_from_group(contact.id, group.id)
    contacts_not_in_group = orm_db.get_contacts_not_in_group(Group(id=group.id))
    contact = random.choice(contacts_not_in_group)
    app.contact.add_contact_by_id_to_group(contact.id, group.id)
    assert contact in orm_db.get_contacts_in_group(Group(id=group.id))