from main import name_serch, shelf_search
import unittest
from unittest import mock
from parameterized import parameterized

class TestName_serch(unittest.TestCase):
    # def setUp(self) -> None:
    #     ...
    #
    # def tearDown(self) -> None:
    #     ...

    @parameterized.expand(([
        ['2207 876234', 'Документ на полке №:1'],
        ['11-2', 'Документ на полке №:1'],
        ['35', 'Документа с таким номером не найдено'],
    ]))
    def test_shelf_search(self, req, ans):
        mock.builtins.input = lambda _: req
        self.assertEqual(shelf_search(), ans)
