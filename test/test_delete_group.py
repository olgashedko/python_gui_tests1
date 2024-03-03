import random
import time


def test_delete_group(app):
    if len(app.groupHelp.get_group_list()) == 1:
        app.groupHelp.add_new_group("group1")
    old_groups = app.groupHelp.get_group_list()
    index = random.randrange(0, len(old_groups))
    group = old_groups[index]
    app.groupHelp.delete_group_by_index(index)
    time.sleep(0.5)
    old_groups.remove(group)
    new_groups = app.groupHelp.get_group_list()
    assert sorted(old_groups) == sorted(new_groups)