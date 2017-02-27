"""
To compile the grammar and gather the requirements data from input requirements.txt

Source code for following functions are used from
https://www.python.org/dev/peps/pep-0508/#complete-grammar:
format_full_version(info)
get_compiled_list_using_grammar(package_list)
"""
import os
import platform
import re
import sys

from parsley import makeGrammar

from src.compile.grammar import grammar


def get_package_list_from_requirement_file(req_file_path):
    return get_package_list_using_compiled_grammar(read_requirements_from_file(req_file_path))


def read_requirements_from_file(req_file_path):
    try:
        with open(req_file_path) as f:
            return perform_requirement_regex_match(f.read())

    except IOError:
        print "Can't open " + req_file_path
        sys.exit(0)


def perform_requirement_regex_match(file_content):
    requirement_regex = "(^[^#\n]+)"
    return re.findall(requirement_regex, file_content, flags=re.MULTILINE)


def get_package_list_using_compiled_grammar(package_list):
    if hasattr(sys, 'implementation'):
        implementation_version = format_full_version(sys.implementation.version)
        implementation_name = sys.implementation.name
    else:
        implementation_version = '0'
        implementation_name = ''
    bindings = {
        'implementation_name': implementation_name,
        'implementation_version': implementation_version,
        'os_name': os.name,
        'platform_machine': platform.machine(),
        'platform_python_implementation': platform.python_implementation(),
        'platform_release': platform.release(),
        'platform_system': platform.system(),
        'platform_version': platform.version(),
        'python_full_version': platform.python_version(),
        'python_version': platform.python_version()[:3],
        'sys_platform': sys.platform,
    }

    compiled = makeGrammar(grammar, {'lookup': bindings.__getitem__})
    return [compiled(package).specification() for package in package_list]


def format_full_version(info):
    version = '{0.major}.{0.minor}.{0.micro}'.format(info)
    kind = info.releaselevel
    if kind != 'final':
        version += kind[0] + str(info.serial)
    return version

