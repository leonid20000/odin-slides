import unittest
from unittest.mock import MagicMock
from odin_slides.presentation import (
    find_most_similar_layout,
    find_content_placeholder,
    find_slide_layout_by_name,
    create_presentation,
    build_slides_with_llm,
)
from pptx.enum.shapes import MSO_SHAPE_TYPE

class TestPresentationFunctions(unittest.TestCase):
    """
    Test suite for the presentation module functions.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.prs = MagicMock()
        self.bad_prs = MagicMock()
        self.default_layout = MagicMock()
        self.imaginary_layout = MagicMock()
        self.similar_layout = MagicMock()
        self.slide = MagicMock()
        self.shape = MagicMock()

        self.prs.slide_layouts = [self.default_layout, self.imaginary_layout, self.similar_layout]
        self.default_layout.name = "Title and Content"
        self.imaginary_layout.name = "Imaginary Layout"
        self.similar_layout.name = "Titled Content"  # Similar to "Title and Content"

    def test_find_most_similar_layout(self):
        """
        Test the find_most_similar_layout function.
        """
        self.assertEqual(find_most_similar_layout(self.prs, "Title and Content"), self.default_layout)
        self.assertIsNone(find_most_similar_layout(self.bad_prs, "Title and Content"))

    def test_find_content_placeholder(self):
        """
        Test the find_content_placeholder function.
        """
        self.slide.shapes = [self.shape]
        self.shape.shape_type = "Not a Placeholder"
        self.assertIsNone(find_content_placeholder(self.slide))

        self.shape.shape_type = MSO_SHAPE_TYPE.PLACEHOLDER
        self.shape.placeholder_format.idx = 0
        self.assertIsNone(find_content_placeholder(self.slide))

        self.shape.placeholder_format.idx = 1
        self.assertEqual(find_content_placeholder(self.slide), self.shape)

    def test_find_slide_layout_by_name(self):
        """
        Test the find_slide_layout_by_name function.
        """
        self.assertEqual(find_slide_layout_by_name(self.prs, "Title and Content"), self.default_layout)
        self.assertEqual(find_slide_layout_by_name(self.prs, "Imaginary Layout"), self.imaginary_layout)
        self.assertEqual(find_slide_layout_by_name(self.prs, "Titled Content"), self.similar_layout)
        self.assertIsNone(find_slide_layout_by_name(self.prs, "Unknown Layout"))

    def test_create_presentation(self):
        # TODO: Write unit test for create_presentation function
        pass

    def test_build_slides_with_llm(self):
        # TODO: Write unit test for build_slides_with_llm function
        pass

if __name__ == '__main__':
    unittest.main()
