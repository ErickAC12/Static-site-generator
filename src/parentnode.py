from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode needs tag")
        if self.children is None or self.children == []:
            raise ValueError("ParentNode needs children")

        children_string = ''.join(map(lambda child: child.to_html(),
                                      self.children))

        if self.props is None or self.props == {}:
            return f'<{self.tag}>{children_string}</{self.tag}>'

        props_string = ' '.join(map(lambda item: f'{item[0]}="{item[1]}"',
                                    self.props.items())).strip()

        return f'<{self.tag} {props_string}>{children_string}</{self.tag}>'
