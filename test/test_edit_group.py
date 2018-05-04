from model.group import Group


def test_edit_first_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="TEST"))
    group = Group(name="NAME EDITED")
    group.id = old_groups[0].id
    app.group.edit_first(group)
    assert app.group.count() == len(old_groups)
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


"""def test_edit_first_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="TEST"))
    app.group.edit_first(Group(header=" HEADER EDITED"))
    app.group.edit_first(Group(name=" NAME EDITED"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)


def test_edit_first_group_footer(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="TEST"))
    app.group.edit_first(Group(footer=" FOOTER EDITED"))
    app.group.edit_first(Group(name=" NAME EDITED"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)"""