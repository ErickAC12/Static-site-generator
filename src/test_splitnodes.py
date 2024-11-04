import unittest

from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):
    def test_splitnodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is also a text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
                TextNode("This is also a text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_splitnodes_nottypetext(self):
        node = TextNode(
                "This is text with a `code block` word, but not type text",
                TextType.ITALIC)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a `code block` word, but not type text",
                         TextType.ITALIC)
            ]
        )
