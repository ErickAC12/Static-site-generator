class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        return " ".join(map(lambda prop: f'{prop[0]}="prop[1]"',
                            self.props.items())).strip()

    def __eq__(self, other):
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

    def __repr__(self):
        children = str(map(lambda item: f'{item} ', self.children)).strip()
        props = str(map(lambda item: f'{item[0]}: {item[1]}, ',
                        self.props.values())).strip(", ")
        return f'tag: {self.tag}, value: {self.value}, children: {children}, props: {props}'
