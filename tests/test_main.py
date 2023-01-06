import unittest
from unittest.mock import patch
from pathlib import Path

from src.reverse_text.main import reverse_string, reverse_text_from_file


class TestReverseString(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = [
            ("a!bc1d test2test", "d!cb1a tset2tset"),
            ("abs1", "sba1"),
            ("123", "123")
        ]

    def test_raise_exception(self):
        with self.assertRaises(TypeError):
            reverse_string(123)

    def test_normal_behavior(self):
        for passed_value, expected_value in self.cases:
            with self.subTest(passed_value=passed_value, expected_value=expected_value):
                self.assertEqual(reverse_string(passed_value), expected_value)


class TestReverseTextFromFile(unittest.TestCase):
    def setUp(self) -> None:
        self.read_lines = [
            "a!bc1d test2test",
            "abs1",
            "123",
        ]
        self.expected_lines = '\n'.join([
            "d!cb1a tset2tset",
            "sba1",
            "123"
        ])
        self.passed_pass = 'test/path'
        self.filename = 'test.name'

    @patch('src.reverse_text.main.read_text_from_file')
    @patch('src.reverse_text.main.write_text_into_file')
    def test_normal_behavior(self, mock_write_text_into_file, mock_read_text_from_file):
        mock_read_text_from_file.return_value = self.read_lines
        reverse_text_from_file(self.passed_pass, self.filename)
        path = Path(self.passed_pass).absolute().parent / self.filename
        args, kwargs = mock_write_text_into_file.call_args
        self.assertEqual(args, (path, self.expected_lines))

    def test_raise_exception_first_arg(self):
        with self.assertRaises(TypeError):
            reverse_text_from_file(123, 'test_string')

    def test_raise_exception_second_arg(self):
        with self.assertRaises(TypeError):
            reverse_text_from_file('test_string', 123)


if __name__ == '__main__':
    unittest.main()
