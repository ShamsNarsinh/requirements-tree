

def parse_command_line_arguments():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("req_path", help="Path to python package requirement file")
    # parser.add_argument("-a", "--all", help="Display all meta-information about packages available on PyPI",
    #                     action="store_true")
    return parser.parse_args()

