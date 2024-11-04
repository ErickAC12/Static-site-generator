import unittest
from extractlinksandimages import extract_markdown_images, extract_markdown_links


class TestExtractLinksAndImages(unittest.TestCase):
    def test_extractimages(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
                extract_markdown_images(text),
                [
                    ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                    ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
                ]
        )

    def test_extractlinks(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(
                extract_markdown_links(text),
                [
                    ("to boot dev", "https://www.boot.dev"),
                    ("to youtube", "https://www.youtube.com/@bootdotdev")
                ]
        )
