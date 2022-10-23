import qrcode


def create_qr_from_string(_name: str, _data: str):
    img = qrcode.make(_data)
    print(f'Creating qr code {_name}')
    img.save(_name)