
from model.group import Group
from pytest_bdd import given, when, then
import random


@given('a group list')
def group_list(db):
    return db.get_group_list()


@given('a group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)


@then("the new group list is equal to the old list with the added group")
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@given('a non-empty group list')
def non_empty_group_list(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='some group'))
    return db.get_group_list()


@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)

@then("the new group list is equal to the old list without the deleted group")
def verufy_group_deleted(db, non_empty_group_list, random_group, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


@given('a non-empty group list')
def non_empty_group_list(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='some group'))
    return db.get_group_list()


@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@given('parameters to modify')
def group_parameters():
    return Group(name='modified name', header='new header')


@when('I modify the group in the list')
def modify_group(app, random_group, group_parameters):
    app.group.modify_group_by_id(random_group.id, group_parameters)


@then('the new  list is equal to the old list with the modified group')
def verufy_modified_group(db, non_empty_group_list, random_group, group_parameters, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    old_groups[old_groups.index(random_group)].name = group_parameters.name
    old_groups[old_groups.index(random_group)].header = group_parameters.header
    print(old_groups)
    print(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
