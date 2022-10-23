import sys
import urllib.request

from lookup_resources import load_resources
from qr import create_qr_from_string
from file import read_input, format_email_to_file_name, save_public_key
from urllib.error import HTTPError

lookup_url = 'https://mail-api.proton.me/pks/lookup?op=get&search='


def get_full_key_url(_mail: str):
    return f'{lookup_url}{_mail}'


def search_for_pub_key(_mail: str):
    with urllib.request.urlopen(get_full_key_url(_mail)) as response:
        return response.read()


if __name__ == "__main__":
    email = read_input(sys.argv[1:])
    name = format_email_to_file_name(email)

    load_resources()

    try:
        pub_key = search_for_pub_key(email)
        save_public_key(pub_key, f'{name}.asc')
        create_qr_from_string(f'{name}.png', get_full_key_url(email))
    except HTTPError:
        print(f'No public PGP keys for the email {email} found.')
