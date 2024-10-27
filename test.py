import io
import unittest
from main import rhombus
from unittest import mock


class TestRhombus(unittest.TestCase):

    # Correctly prints a rhombus shape with odd size dimensions
    def test_rhombus_odd_size(self):
        expected_output = ('*\n ***\n*****\n ***\n  *\n')

        with mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rhombus(3)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Correctly prints a rhombus shape with odd dimensions
    def test_rhombus_odd_dimensions(self):
        expected_output = ('  *\n ***\n*****\n ***\n  *\n')

        with mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rhombus(3)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Handles zero size input without errors
    def test_rhombus_zero_size(self):
        expected_output = ""

        with mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rhombus(0)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Handles zero as input without errors
    def test_rhombus_zero_input(self):
        expected_output = ""
        with mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rhombus(0)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Manages negative size input gracefully without errors
    def test_rhombus_negative_size(self):
        expected_output = ""

        with mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rhombus(-3)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Manages negative input values gracefully
    def test_rhombus_negative_input(self):
        expected_output = ""
        with mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rhombus(-3)
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
