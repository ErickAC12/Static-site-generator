from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode needs tag")
        if self.tag is None:
            return self.value
        if self.props is None or self.props == {}:
            return f'<{self.tag}>{self.value}</{self.tag}>'

        props_string = ' '.join(map(lambda item: f'{item[0]}="{item[1]}"',
                                    self.props.items())).strip()
        return f'<{self.tag} {props_string}>{self.value}</{self.tag}>'
