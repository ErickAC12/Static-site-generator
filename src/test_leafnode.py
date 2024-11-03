import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leafnode(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def test_leafnode_noprops(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node, node2)

    def test_leafnode_tohtml(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node_text = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), node_text)

    def test_leafnode_notag(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(node.to_html(), node.value)

    def test_leafnode_novalue(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError) as ex:
            node.to_html()
        self.assertEqual(str(ex.exception), "LeafNode needs tag")
