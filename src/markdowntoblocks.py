def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        cleaned_block = block.strip()
        cleaned_blocks.append(cleaned_block)
    return cleaned_blocks
