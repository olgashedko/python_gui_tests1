import random
import time


def test_delete_group(app):
    if len(app.groupHelp.get_group_list()) == 1:
        app.groupHelp.add_new_group("group1")
    old_groups = app.groupHelp.get_group_list()
    print(old_groups)
    index = random.choice(range(0, len(old_groups)))
    print(index)
    group = old_groups[index]
#    group = random.choice(old_groups)
    print(group)
    app.groupHelp.delete_group_by_index(index)
  #  app.groupHelp.delete_group_by_index(group)
    time.sleep(0.5)
    old_groups.remove(group)
    new_groups = app.groupHelp.get_group_list()
    print(new_groups)
    print(old_groups)
  #  new_groups = app.groupHelp.get_group_list()
  #  assert sorted(old_groups) == sorted(new_groups)