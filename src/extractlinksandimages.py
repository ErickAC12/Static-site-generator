import re


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    if len(matches) == 0:
        raise Exception("Didn't find any match")

    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    if len(matches) == 0:
        raise Exception("Didn't find any match")

    return matches
