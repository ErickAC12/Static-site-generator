import unittest

from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter, split_nodes_link, split_nodes_image, text_to_textnodes


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

    def test_splitnodesimage(self):
        node = TextNode(
                "This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
                new_nodes,
                [
                    TextNode("This is text with an image ", TextType.TEXT),
                    TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
                    TextNode(" and ", TextType.TEXT),
                    TextNode(
                        "to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"
                    ),
                ]
        )

    def test_splitnodesimage_nomatches(self):
        node = TextNode(
                "This is text without an image [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
                new_nodes,
                [
                    TextNode("This is text without an image [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                    TextType.TEXT),
                ]
        )

    def test_splitnodeslink(self):
        node = TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
                new_nodes,
                [
                    TextNode("This is text with a link ", TextType.TEXT),
                    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                    TextNode(" and ", TextType.TEXT),
                    TextNode(
                        "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                    ),
                ]
        )

    def test_splitnodeslink_nomatches(self):
        node = TextNode(
                "This is text without a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
                new_nodes,
                [
                    TextNode("This is text without a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
                    TextType.TEXT),
                ]
        )

    def test_splitnodes_totextnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(
                text_to_textnodes(text),
                [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                ])

    def test_splitnodes_totextnodes_nomatches(self):
        text = "This text doesn't have any modifications"
        self.assertEqual(
                text_to_textnodes(text),
                [
                    TextNode("This text doesn't have any modifications", TextType.TEXT)
                ]
        )
