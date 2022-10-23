import re
import getopt
import sys

file_name = 'lookup_public_pgp.py'


def read_input(argv):
    try:
        opts, args = getopt.getopt(argv, "e:", ["email="])
        if len(opts) == 0:
            print(f'usage: {file_name} -e <email>')
            sys.exit(2)

    except getopt.GetoptError:
        print(f'{file_name} -e <email>')

    for opt, arg in opts:
        if opt in ('-e', '--email'):
            return arg


def format_email_to_file_name(_email: str):
    return re.sub('[^A-Za-z0-9_]+', '', _email)


def save_public_key(_data: bytes, _name: str):
    with open(_name, "w") as file:
        file.write(_data.decode("utf-8"))


