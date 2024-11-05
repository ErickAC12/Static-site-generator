from textnode import TextNode, TextType
from extractlinksandimages import extract_markdown_links, extract_markdown_images


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for i in range(len(old_nodes)):
        if old_nodes[i].text_type != TextType.TEXT:
            new_nodes.append(old_nodes[i])
        elif delimiter in old_nodes[i].text:
            tmp_string_array = old_nodes[i].text.split(delimiter)

            if len(tmp_string_array) >= 3 and len(tmp_string_array) % 2 == 1:
                for j in range(len(tmp_string_array)):
                    if j != 0 and j % 2 == 1:
                        tmp_string_array[j] = TextNode(tmp_string_array[j],
                                                       text_type)
                    else:
                        tmp_string_array[j] = TextNode(tmp_string_array[j],
                                                       TextType.TEXT)
            new_nodes.extend(tmp_string_array)
        else:
            raise Exception
        (f"Node in index {i} doesn't contain delimiter '{delimiter}'")

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            try:
                matches = extract_markdown_images(node.text)
                last_index = 0
                for match in matches:
                    alt, url = match
                    start_index = node.text.find(f"![{alt}]({url})")
                    if start_index != 1:
                        if start_index > last_index:
                            new_nodes.append(TextNode(
                                node.text[last_index:start_index],
                                TextType.TEXT))
                        new_nodes.append(TextNode(
                            text=alt,
                            text_type=TextType.IMAGE,
                            url=url))
                        last_index = start_index + len(f"![{alt}]({url})")
                if last_index < len(node.text):
                    new_nodes.append(TextNode(
                        node.text[last_index:],
                        TextType.TEXT))
            except Exception:
                new_nodes.append(node)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            try:
                matches = extract_markdown_links(node.text)
                last_index = 0
                for match in matches:
                    alt, url = match
                    start_index = node.text.find(f"[{alt}]({url})")
                    if start_index != 1:
                        if start_index > last_index:
                            new_nodes.append(TextNode(
                                node.text[last_index:start_index],
                                TextType.TEXT))
                        new_nodes.append(TextNode(
                            text=alt,
                            text_type=TextType.LINK,
                            url=url))
                        last_index = start_index + len(f"[{alt}]({url})")
                if last_index < len(node.text):
                    new_nodes.append(TextNode(
                        node.text[last_index:],
                        TextType.TEXT))
            except Exception:
                new_nodes.append(node)

    return new_nodes
