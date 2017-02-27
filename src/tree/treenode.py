"""

"""
class TreeNode:
    def __init__(self, name, all_info=None, pkg_type=None):
        self.name = name
        self.all_info = all_info
        self.pkg_type = pkg_type
        self.children = []

    def __str__(self, level=0):
        result = "\t"*level+repr(self.name)+"\n"
        for child in self.children:
            result += child.__str__(level+1)
        return result

    def __repr__(self):
        return '<tree node representation>'

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, children_list):
        self.children.extend(children_list)

    # def recursive_print_children(self, tree_node):
    #     for child in tree_node.children:
    #         print child.name
    #         if len(child.children) != 0:
    #             self.recursive_print_children(child.children)

