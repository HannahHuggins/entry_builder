from unittest import TestCase
from random import entry_builder


class TestHello_world(TestCase):
    def test_entry_contain_sys_key(self):
        # arrange

        # action
        entry = entry_builder()
        res = "sys" in entry

        self.assertTrue(res)

    def test_sys_contains_id_key(self):
        sys_dict = entry_builder().get("sys")
        res = "id" in sys_dict

        self.assertTrue(res)

    def test_entry_contains_name(self):
        entry = entry_builder()
        res = "name" in entry

        self.assertTrue(res)

    def test_entry_contains_description(self):
        entry = entry_builder()
        res = "description" in entry

        self.assertTrue(res)

    def test_entry_conatains_fields(self):
        entry = entry_builder()
        res = "fields" in entry

        self.assertTrue(res)
