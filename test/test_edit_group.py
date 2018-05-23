from model.group import Group
import random


def test_edit_group_name_by_id(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="TEST"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group(name="NAME EDITED")
    new_group_data.id = group.id
    app.group.edit_group_by_id(new_group_data.id, new_group_data)
    new_groups = db.get_group_list()
    index = old_groups.index(group)
    old_groups[index] = new_group_data
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        db_list = map(clean, new_groups)
        assert sorted(db_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)