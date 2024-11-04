from textnode import TextNode, TextType


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
                        tmp_string_array[j] = TextNode(tmp_string_array[j], text_type)
                    else:
                        tmp_string_array[j] = TextNode(tmp_string_array[j], TextType.TEXT)
            new_nodes.extend(tmp_string_array)
        else:
            raise Exception
        (f"Node in index {i} doesn't contain delimiter '{delimiter}'")

    return new_nodes
