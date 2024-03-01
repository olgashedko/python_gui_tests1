def test_add_group(app):
    old_groups = app.groupHelp.get_group_list()
    app.groupHelp.add_new_group("group1")
    new_groups = app.groupHelp.get_group_list()
    old_groups.append("group1")
    assert sorted(old_groups) == sorted(new_groups)