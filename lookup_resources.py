import json
from enum import Enum
from typing import List


class RemoteType(Enum):
    EMAIL = 1


class Remote(object):
    name: str
    path: str
    type: RemoteType

    def __init__(self, name: str, path: str, _type: RemoteType):
        self.name = name
        self.path = path
        self.type = _type


class Resources(object):
    remote: List[Remote]

    def __init__(self, remote: List[Remote]):
        self.remote = remote


def from_json(data, cls):
    if issubclass(cls, Resources):
        _list: List[Remote] = list()
        for res in data['remote']:
            _list.append(from_json(res, Remote))
        return Resources(_list)
    elif issubclass(cls, Remote):
        return Remote(data['name'], data['path'], RemoteType(data['type']))
    else:
        return data


def load_resources(path: str = "lookup_resources.json") -> Resources:
    with open(path, "r", encoding="utf-8") as file:
        return from_json(json.load(file), Resources)
