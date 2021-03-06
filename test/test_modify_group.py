
from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test group"))
    old_groups = db.get_group_list()
    select_group = random.choice(old_groups)
    group = Group(name="test2")
    app.group.modify_group_by_id(select_group.id, group)
    new_groups = db.get_group_list()
    old_groups[old_groups.index(select_group)].name = group.name
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test group"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="test2"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
