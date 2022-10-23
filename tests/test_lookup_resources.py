import unittest
from unittest import TestCase

from lookup_resources import load_resources, Resources, RemoteType


class Test(TestCase):
    # noinspection PyBroadException
    def test_should_load_json_resources_properly(self):
        try:
            resources = load_resources("lookup_resources_test.json")
            self.assertEqual(type(resources), Resources)
            self.assertIsNotNone(resources.remote)
            self.assertEqual(len(resources.remote), 1)

            remote = resources.remote[0]
            self.assertEqual(remote.name, "test_name")
            self.assertEqual(remote.path, "test_path")
            self.assertEqual(remote.type, RemoteType.EMAIL)
        except:
            self.fail()


if __name__ == '__main__':
    unittest.main()
