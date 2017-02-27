import re
from src import apicall
from pkg_type_enum import PkgTypeEnum
import treenode


class MakeTree:
    def __init__(self, req_list):
        self.req_list = req_list
        self.root_node = treenode.TreeNode("root")

    def process_requirements_list(self, version_flag=False):
        for req in self.req_list:
            pkg_node = self.create_tree_node_for_package(req[0])
            self.root_node.add_child(pkg_node)
            pkg_node.add_children(self.add_dependencies_of_pkg_node(pkg_node))
        # treenode.TreeNode.recursive_print_children(self.root_node)
        return self.root_node

    def add_dependencies_of_pkg_node(self, pkg_node):
        dep_node_list = []
        try:
            dep_list = pkg_node.all_info["requires_dist"]
        except KeyError:
            return []
        for dep in dep_list:
            dep_name = self.return_package_name_from_require_dist_string(dep)
            dep_node_list.append(self.create_tree_node_for_package(dep_name))
        return dep_node_list

    def return_package_name_from_require_dist_string(self, dep):
        package_regex = "(.+?)([(;\n]|$)"
        return str(re.match(package_regex, dep).group(1)).rstrip()

    def create_tree_node_for_package(self, pkg_name):
        pkg_data = apicall.get_data_for_a_package(pkg_name)
        return treenode.TreeNode(pkg_name, pkg_data, PkgTypeEnum.REQUIREMENT)