from main import documents_update
import unittest
from unittest import mock
from parameterized import parameterized

class TestName_serch(unittest.TestCase):

    @parameterized.expand(([
        ["passport", '2207 876234', "Василий Гупкин", '1', 'база данных обновлена'],
        ["passport", '2207 876234', "Василий Гупкин", '5', 'база данных обновлена']
    ]))
    def test_name_serch(self, type, numb, name, shelf, ans):
        mock.builtins.input = lambda _: type
        mock.builtins.input = lambda _: numb
        mock.builtins.input = lambda _: name
        mock.builtins.input = lambda _: shelf
        self.assertEqual(documents_update(), ans)