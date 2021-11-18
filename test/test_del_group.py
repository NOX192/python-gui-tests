def test_del_group(app):
    if "New group" not in app.groups.get_group_list():
        app.groups.add_new_group("New group")
    old_list = app.groups.get_group_list()
    app.groups.del_new_group()
    new_list = app.groups.get_group_list()
    old_list.remove('New group')
    assert old_list == new_list




