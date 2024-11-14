import unittest
from extracttitle import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extracttitle(self):
        markdown = "# This is the title\nnothing here\n## or here"
        self.assertEqual(extract_title(markdown),
                         "This is the title")

    def test_extracttitle_double_title(self):
        markdown = "nothing here\n ## or here\n# This is the title\n# Other title"
        self.assertEqual(extract_title(markdown),
                         "This is the title")

    def test_extracttitle_no_title(self):
        markdown = "nothing here\n## no title"
        with self.assertRaises(Exception) as ex:
            extract_title(markdown)
        self.assertEqual(str(ex.exception), "No title found")
