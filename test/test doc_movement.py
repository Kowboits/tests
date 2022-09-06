from main import doc_movement
import unittest
from unittest import mock
from parameterized import parameterized

class TestName_serch(unittest.TestCase):

    @parameterized.expand(([
        ['2207 876234', '2', 'Данные обновлены'],
        ['11-2', '2','Ошибка: проверьте номер документа или номер полки для перемещения'],
        ['35', '1','Ошибка: проверьте номер документа или номер полки для перемещения'],
    ]))
    def test_name_serch(self, numb, shelf, ans):
        mock.builtins.input = lambda _: numb
        mock.builtins.input = lambda _: shelf
        self.assertEqual(doc_movement(), ans)