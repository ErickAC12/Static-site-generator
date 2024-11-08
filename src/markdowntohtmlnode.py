import re
from markdowntoblocks import markdown_to_blocks
from blocktoblocktype import block_to_block_type
from parentnode import ParentNode
from leafnode import LeafNode


def remove_start_chars_in_lines(block, patterns):
    lines = block.split('\n')
    new_lines = []

    for line in lines:
        new_line = line
        for pattern in patterns:
            if isinstance(pattern, str):
                if new_line.startswith(pattern):
                    new_line = new_line[len(pattern):]
            elif hasattr(pattern, 'match'):
                new_line = re.sub(pattern, '', new_line)
        new_lines.append(new_line)
    return '\n'.join(new_lines)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    div = ParentNode(tag='div', children=[])
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == 'heading 1':
            div.children.append(
                    LeafNode(tag='h1', value=block.lstrip('# ')))

        elif block_type == 'heading 2':
            div.children.append(
                    LeafNode(tag='h2', value=block.lstrip('## ')))

        elif block_type == 'heading 3':
            div.children.append(
                    LeafNode(tag='h3', value=block.lstrip('### ')))

        elif block_type == 'heading 4':
            div.children.append(
                    LeafNode(tag='h4', value=block.lstrip('#### ')))

        elif block_type == 'heading 5':
            div.children.append(
                    LeafNode(tag='h5', value=block.lstrip('##### ')))

        elif block_type == 'heading 6':
            div.children.append(
                    LeafNode(tag='h6', value=block.lstrip('###### ')))

        elif block_type == 'code':
            pre = ParentNode(tag='pre', children=[
                LeafNode(tag='code', value=block.strip('```'))])
            div.children.append(pre)

        elif block_type == 'quote':
            new_block = remove_start_chars_in_lines(block, ['> '])
            div.children.append(
                    LeafNode(tag='blockquote', value=new_block))

        elif block_type == 'unordered list':
            new_block = remove_start_chars_in_lines(block, ['* ', '- '])
            lines = new_block.split('\n')
            unordered_list = ParentNode(tag='ul', children=[])
            for line in lines:
                unordered_list.children.append(
                        LeafNode(tag='li', value=line))
            div.children.append(unordered_list)

        elif block_type == 'ordered list':
            new_block = remove_start_chars_in_lines(block, [re.compile(r'\d+\. \s*')])
            lines = new_block.split('\n')
            ordered_list = ParentNode(tag='ol', children=[])
            for line in lines:
                ordered_list.children.append(
                        LeafNode(tag='li', value=line))
            div.children.append(ordered_list)

        elif block_type == 'normal paragraph':
            div.children.append(
                    LeafNode(tag='p', value=block))
    return div
