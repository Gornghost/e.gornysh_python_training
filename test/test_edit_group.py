from model.group import Group


def test_edit_first_group_name(app):
    app.group.edit_first(Group(name=" NAME EDITED"))


def test_edit_first_group_header(app):
    app.group.edit_first(Group(header=" HEADER EDITED"))


def test_edit_first_group_footer(app):
    app.group.edit_first(Group(footer=" FOOTER EDITED"))