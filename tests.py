import unittest
from functions.get_files_info import get_files_info

class TestGetFileInfoFunction(unittest.TestCase):
    def test_calc_info(self):
        self.assertEqual(
            get_files_info("calculator", "."),
            """Result for current directory:
- main.py: file_size=564 bytes, is_dir=False
- tests.py: file_size=1330 bytes, is_dir=False
- pkg: file_size=4096 bytes, is_dir=True"""
        )

    def test_calc_info_two(self):
        self.assertEqual(
            get_files_info("calculator", "pkg"),
            """Result for 'pkg' directory:
- __pycache__: file_size=4096 bytes, is_dir=True
- calculator.py: file_size=1720 bytes, is_dir=False
- render.py: file_size=753 bytes, is_dir=False"""
        )

    def test_calc_info_three(self):
        self.assertEqual(
            get_files_info("calculator", "/bin"),
            """Result for '/bin' directory:
Error: Cannot list "/bin" as it is outside the permitted working directory"""
        )

    def test_calc_info_four(self):
        self.assertEqual(
            get_files_info("calculator", "../"),
            """Result for '../' directory:
Error: Cannot list "../" as it is outside the permitted working directory"""
        )

if __name__ == '__main__':
    unittest.main()