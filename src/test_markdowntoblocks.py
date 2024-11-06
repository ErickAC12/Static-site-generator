import unittest
from markdowntoblocks import markdown_to_blocks


class TestMarkdowntoblocks(unittest.TestCase):
    def test_markdowntoblocks(self):
        markdown = "# This is a heading\n\n" + "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n" + "* This is the first list item in a list block\n" + "* This is a list item\n" + "* This is another list item\n"
        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ]
        )
