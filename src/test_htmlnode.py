import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_htmlnode(self):
        node = HTMLNode("tag", "value", ["children"], {"props": "propValue"})
        node2 = HTMLNode("tag", "value", ["children"], {"props": "propValue"})
        self.assertEqual(node, node2)

    def test_htmlnode_none(self):
        node = HTMLNode()
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(node, node2)

    def test_different_htmlnode(self):
        node = HTMLNode("tag", "value", ["children"], {"props": "propValue"})
        node2 = HTMLNode("tag", "different", ["children"], {"props": "propValue"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("tag", "value", ["children"], {"props": "propValue"})
        node2 = HTMLNode("tag", "value", ["children"], {"props": "propValue"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())
