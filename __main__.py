import argparse
from src.compile import compiler
from src.tree import maketree
def main(args = None):
    """The main routine."""

    args = parse_command_line_arguments()
    req_list = compiler.get_package_list_from_requirement_file(args.req_path)
    dep_tree = maketree.MakeTree(req_list)
    dep_tree.process_requirements_list()
    #print req_list


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("req_path", help="Path to python package requirement file")
    parser.add_argument("-l", "--license", help="Show package dependency tree along with package license",
                        action="store_true")
    parser.add_argument("-v", "--version", help="Show package dependency tree along with package version",
                        action="store_true")
    parser.add_argument("-url", "--url", help="Show package dependency tree along with package URL",
                        action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    main()