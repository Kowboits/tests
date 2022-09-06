from main import name_serch, shelf_search
import unittest
from unittest import mock
from parameterized import parameterized

class TestName_serch(unittest.TestCase):

    @parameterized.expand(([
        ['2207 876234', 'Документ на имя: Василий Гупкин'],
        ['11-2', 'Документ на имя: Геннадий Покемонов'],
        ['35', 'Документа с таким номером не найдено'],
    ]))
    def test_name_serch(self, req, ans):
        mock.builtins.input = lambda _: req
        self.assertEqual(name_serch(), ans)