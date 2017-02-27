

class TreeNode:
    def __init__(self, name, version=None, license=None, pkg_url=None, pkg_type=None):
        self.name = name
        self.version = version
        self.license = license
        self.pkg_url = pkg_url
        self.pkg_type = pkg_type
        self.children = []

    def add_child(self, child):
        self.children.append(child)


    @staticmethod
    def recursive_print_children(tree_node):
        for child in tree_node.children:
            print child.name, " - ", child.version, " - ", child.license
            if len(child.children) != 0:
                TreeNode.recursive_print_children(child.children)