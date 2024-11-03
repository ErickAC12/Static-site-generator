from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError()
        if self.tag is None:
            return self.value
        props_text = ' '.join(map(lambda item: f'{item[0]}="{item[1]}"',
                                  self.props.items())).strip()
        return f'<{self.tag} {props_text}>{self.value}</{self.tag}>'
