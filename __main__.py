"""
Main execution file of the project
"""
from src.compile import compiler
from src.tree import maketree
from src import helper


def main(args = None):
    """The main routine."""
    args = helper.parse_command_line_arguments()

    print "Reading requirements...",
    req_list = compiler.get_package_list_from_requirement_file(args.req_path)
    print "Done!"
    dep_tree = maketree.MakeTree(req_list)
    print "Collecting information from PyPI...\n"
    print dep_tree.process_requirements_list()

if __name__ == "__main__":
    main()
