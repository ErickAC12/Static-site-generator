import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_none_url(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_nodeToHtml_text(self):
        node = TextNode("This is only text", TextType.TEXT)
        self.assertEqual(text_node_to_html_node(node).to_html(),
                         'This is only text')

    def test_nodeToHtml_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        self.assertEqual(text_node_to_html_node(node).to_html(),
                         '<b>This is bold text</b>')

    def test_nodeToHtml_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        self.assertEqual(text_node_to_html_node(node).to_html(),
                         '<i>This is italic text</i>')

    def test_nodeToHtml_code(self):
        node = TextNode("This is code text", TextType.CODE)
        self.assertEqual(text_node_to_html_node(node).to_html(),
                         '<code>This is code text</code>')

    def test_nodeToHtml_link(self):
        node = TextNode("This is a link", TextType.LINK,
                        "https://www.google.com")
        self.assertEqual(text_node_to_html_node(node).to_html(),
                         '<a href="https://www.google.com">This is a link</a>')

    def test_nodeToHtml_image(self):
        node = TextNode("This is an image", TextType.IMAGE,
                        "../images/cool_pic.png")
        self.assertEqual(text_node_to_html_node(node).to_html(),
                         '<img src="../images/cool_pic.png" alt="This is an image"></img>')


if __name__ == "__main__":
    unittest.main()
