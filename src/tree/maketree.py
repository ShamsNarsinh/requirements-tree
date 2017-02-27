from src import apicall
from pkg_type_enum import PkgTypeEnum
import treenode


class MakeTree:
    def __init__(self, req_list):
        self.req_list = req_list
        self.root_node = treenode.TreeNode("root")

    def process_requirements_list(self):
        for req in self.req_list:
            pkg_data = apicall.get_data_for_a_package(req[0])
            pkg_node = treenode.TreeNode(req[0], pkg_data["version"], pkg_data["license"], pkg_data["package_url"],
                                         PkgTypeEnum.REQUIREMENT)
            self.root_node.add_child(pkg_node)

        treenode.TreeNode.recursive_print_children(self.root_node)