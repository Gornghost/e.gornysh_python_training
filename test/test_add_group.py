# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="New group 1", header="Group header 1", footer="Group footer"))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups) + 1


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups) + 1