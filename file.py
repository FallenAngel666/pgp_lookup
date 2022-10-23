def save_public_key(_data: bytes, _name: str):
    with open(_name, "w") as file:
        file.write(_data.decode("utf-8"))
