class GroupHelper:
    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def delete_group_by_index(self, index):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        print(index)
        nodes = tree.tree_root().children()
        print(nodes[index].text())
        nodes[index].click()
        # for node in root.children():
        #     print(node.text())
        #    if node.text() == name:
        #        print("str")
        #       node.click()
      #  group_list = [node.text() for node in root.children()]
     #   self.group_editor.window(title=name).click()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
     #   delete_group_window = self.group_editor.window(title="Delete group")
        self.delete_group_window = self.app.application.window(title="Delete group")
        self.delete_group_window.wait("visible")
        self.delete_group_window.window(auto_id="uxOKAddressButton").click()


      #  self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()
