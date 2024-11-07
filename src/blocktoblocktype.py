def block_to_block_type(markdown):
    if markdown.startswith('# '):
        return 'heading 1'
    elif markdown.startswith('## '):
        return 'heading 2'
    elif markdown.startswith('### '):
        return 'heading 3'
    elif markdown.startswith('#### '):
        return 'heading 4'
    elif markdown.startswith('##### '):
        return 'heading 5'
    elif markdown.startswith('###### '):
        return 'heading 6'

    if markdown.startswith('```') and markdown.endswith('```'):
        return 'code'

    lines = markdown.split('\n')

    if all(line.startswith('>') for line in lines):
        return 'quote'

    if all(line.startswith(('* ', '- ')) for line in lines):
        return 'unordered list'

    # Ordered
    is_ordered_list = True
    expected_number = 1

    for line in lines:
        if not line.startswith(f'{expected_number}. '):
            is_ordered_list = False
            break
        expected_number += 1

    if is_ordered_list:
        return 'ordered list'

    return 'normal paragraph'
