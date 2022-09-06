from main import doc_remove
import unittest
from unittest import mock
from parameterized import parameterized

class TestName_serch(unittest.TestCase):

    @parameterized.expand(([
        ['2207 876234', 'данные обновлены'],
        ['11-2', 'данные обновлены'],
        ['35', 'Введен некорректный номер документа'],
    ]))
    def test_name_serch(self, req, ans):
        mock.builtins.input = lambda _: req
        self.assertEqual(doc_remove(), ans)