import unittest
from blocktoblocktype import block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_blocktoblocktype(self):
        blocks = ["# Heading 1",
                  "```python\nprint('Hello, World!')\n```",
                  "> This is a quote block\n> with multiple lines.",
                  "* Unordered list item 1\n* Unordered list item 2",
                  "1. Ordered list item 1\n2. Ordered list item 2",
                  "This is a normal paragraph."]
        result_blocks = []
        for block in blocks:
            result_blocks.append(block_to_block_type(block))
        self.assertEqual(
                result_blocks,
                [
                    'heading 1',
                    'code',
                    'quote',
                    'unordered list',
                    'ordered list',
                    'normal paragraph'
                ])
