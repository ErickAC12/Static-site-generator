import unittest
from markdowntohtmlnode import markdown_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode


class TestMarkdownToHTMLNode(unittest.TestCase):
    maxDiff = None

    def test_markdowntohtmlnode(self):
        markdown = "# Heading 1\n\n```python\nprint('Hello, World!')\n```\n\n> This is a quote block\n> with multiple lines.\n\n* Unordered list item 1\n* Unordered list item 2\n\n1. Ordered list item 1\n2. Ordered list item 2\n\nThis is a normal paragraph."
        expected_node = ParentNode(tag='div', children=[
                             LeafNode(tag='h1', value='Heading 1'),
                             ParentNode(tag='pre', children=[
                                LeafNode(tag='code', value="python\nprint('Hello, World!')\n"),
                             ]),
                             LeafNode(tag='blockquote', value='This is a quote block\nwith multiple lines.'),
                             ParentNode(tag='ul', children=[
                                 LeafNode(tag='li', value='Unordered list item 1'),
                                 LeafNode(tag='li', value='Unordered list item 2')
                             ]),
                             ParentNode(tag='ol', children=[
                                 LeafNode(tag='li', value='Ordered list item 1'),
                                 LeafNode(tag='li', value='Ordered list item 2')
                             ]),
                             LeafNode(tag='p', value='This is a normal paragraph.'),
                         ])
        result_node = markdown_to_html_node(markdown)

        self.assertEqual(result_node.to_html(), expected_node.to_html())
