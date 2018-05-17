from model.group import Group
from random import randrange


def test_delete_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="TEST"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert app.group.count() == len(old_groups) - 1
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups