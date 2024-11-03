import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_parentnode(self):
        node = ParentNode(
            "a",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
            {
                "target": "_blank"
            }
        )
        self.assertEqual(node.to_html(),
                         '<a target="_blank"><b>Bold text</b>Normal text</a>')

    def test_parentnode_noprops(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(),
                         "<p><b>Bold text</b>Normal text</p>")

    def test_parentnode_notag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
        )

        with self.assertRaises(ValueError) as ex:
            node.to_html()

        self.assertEqual(str(ex.exception), "ParentNode needs tag")

    def test_parentnode_nochildren(self):
        node = ParentNode(
            "p",
            [],
        )

        with self.assertRaises(ValueError) as ex:
            node.to_html()

        self.assertEqual(str(ex.exception), "ParentNode needs children")

    def test_parentnode_nestednodes(self):
        node = ParentNode(
            "div",
            [

                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
            ],
            {
                "style": "color: red"
            },
        )
        self.assertEqual(node.to_html(),
                         '<div style="color: red"><p><b>Bold text</b>Normal text</p></div>')
