from main import add_self
import unittest
from unittest import mock
from parameterized import parameterized

class TestName_serch(unittest.TestCase):

    @parameterized.expand(([
        ['2', 'Такая полка уже сужествует'],
        ['4','Полка добавлена'],
        ['1','Такая полка уже сужествует'],
    ]))
    def test_add_self(self, shelf, ans):
        mock.builtins.input = lambda _: shelf
        self.assertEqual(add_self(), ans)