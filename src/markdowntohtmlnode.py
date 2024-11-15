import re
from markdowntoblocks import markdown_to_blocks
from blocktoblocktype import block_to_block_type
from parentnode import ParentNode
from leafnode import LeafNode
from splitnodes import text_to_textnodes
from textnode import text_node_to_html_node


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
            text_nodes = text_to_textnodes(block.lstrip('# '))
            html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]
            div.children.append(
                    ParentNode(tag='h1', children=html_nodes))
        elif block_type == 'heading 2':
            text_nodes = text_to_textnodes(block.lstrip('## '))
            html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]
            div.children.append(
                    ParentNode(tag='h2', children=html_nodes))
        elif block_type == 'heading 3':
            text_nodes = text_to_textnodes(block.lstrip('### '))
            html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]
            div.children.append(
                    ParentNode(tag='h3', children=html_nodes))
        elif block_type == 'heading 4':
            text_nodes = text_to_textnodes(block.lstrip('#### '))
            html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]
            div.children.append(
                    ParentNode(tag='h4', children=html_nodes))
        elif block_type == 'heading 5':
            text_nodes = text_to_textnodes(block.lstrip('##### '))
            html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]
            div.children.append(
                    ParentNode(tag='h5', children=html_nodes))
        elif block_type == 'heading 6':
            text_nodes = text_to_textnodes(block.lstrip('###### '))
            html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]
            div.children.append(
                    ParentNode(tag='h6', children=html_nodes))
        elif block_type == 'code':
            text_nodes = text_to_textnodes(block.strip('```'))
            html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]
            pre = ParentNode(tag='pre', children=[
                ParentNode(tag='code', children=html_nodes)
            ])
            div.children.append(pre)
        elif block_type == 'quote':
            new_block = remove_start_chars_in_lines(block, ['> '])
            text_nodes = text_to_textnodes(new_block)
            html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]
            div.children.append(
                    ParentNode(tag='blockquote', children=html_nodes))
        elif block_type == 'unordered list':
            new_block = remove_start_chars_in_lines(block, ['* ', '- '])
            lines = new_block.split('\n')
            unordered_list = ParentNode(tag='ul', children=[])
            for line in lines:
                text_nodes = text_to_textnodes(line)
                html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]
                unordered_list.children.append(
                        ParentNode(tag='li', children=html_nodes))
            div.children.append(unordered_list)
        elif block_type == 'ordered list':
            new_block = remove_start_chars_in_lines(block, [re.compile(r'\d+\. \s*')])
            lines = new_block.split('\n')
            ordered_list = ParentNode(tag='ol', children=[])
            for line in lines:
                text_nodes = text_to_textnodes(line)
                html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]
                ordered_list.children.append(
                        ParentNode(tag='li', children=html_nodes))
            div.children.append(ordered_list)
        elif block_type == 'normal paragraph':
            text_nodes = text_to_textnodes(block)
            html_nodes = [text_node_to_html_node(tn) for tn in text_nodes]
            div.children.append(
                    ParentNode(tag='p', children=html_nodes))
    return div
