import sys
import urllib.request
import argparse

from lookup_resources import load_resources, Resources
from qr import create_qr_from_string
from file import save_public_key
from urllib.error import HTTPError


def search_for_pub_key(_url: str):
    with urllib.request.urlopen(_url) as response:
        return response.read()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email", help="searches for pgp keys for given email")
    parser.add_argument("-qr", "--qr_code", help="specifies the path for generated qr code")
    parser.add_argument("-f", "--file", help="specifies the path for downloaded pgp key")
    args = parser.parse_args()

    resources: Resources = load_resources()
    found_pgp = None

    for remote in resources.remote:
        if args.email:
            url = remote.path.format(email=args.email)
            try:
                found_pgp = search_for_pub_key(url)
            except HTTPError:
                continue
        else:
            sys.stderr.write('Provide at least email param!\n')
            sys.exit(2)

    if found_pgp is None:
        sys.stderr.write(f'No public PGP keys were found!\n')
        sys.exit(2)

    if args.qr_code:
        create_qr_from_string(args.qr_code, url)
    if args.file:
        save_public_key(found_pgp, args.file)

    sys.stdout.write(found_pgp.decode("utf-8"))
