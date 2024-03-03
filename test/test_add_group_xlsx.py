def test_add_group_xlsx(app, xlsx_groups):
    group = xlsx_groups[0]
    old_groups = app.groupHelp.get_group_list()
    app.groupHelp.add_new_group(group)
    new_groups = app.groupHelp.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups) == sorted(new_groups)

