import unittest 
from odin_slides.utils import (
    format_prompt,
    format_info,
    format_warning,
    format_error,
    ensure_list,
)


class TestUtils(unittest.TestCase):
    """
    Test suite for the presentation module functions.
    """

    def test_format_prompt(self):
        """Test format_prompt function."""
        self.assertEqual(format_prompt("Test"), "\x1b[36mTest> \x1b[0m")

    def test_format_info(self):
        """Test format_info function."""
        self.assertEqual(format_info("Test"), "\x1b[32mTest\x1b[0m")

    def test_format_warning(self):
        """Test format_warning function."""
        self.assertEqual(format_warning("Test"), "\x1b[33mWarning: Test\x1b[0m")

    def test_format_error(self):
        """Test format_error function."""
        self.assertEqual(format_error("Test"), "\x1b[31mError: Test\x1b[0m")



    def test_ensure_list_dict(self):
        """Test ensure_list function with a dictionary."""
        result = ensure_list({"key": "value"})
        self.assertEqual(result, [{"key": "value"}])

    def test_ensure_list_list(self):
        """Test ensure_list function with a list."""
        result = ensure_list(["item1", "item2"])
        self.assertEqual(result, ["item1", "item2"])

    def test_ensure_list_exception(self):
        """Test ensure_list function with an invalid input type."""
        with self.assertRaises(TypeError):
            ensure_list("invalid")

if __name__ == "__main__":
    unittest.main()
