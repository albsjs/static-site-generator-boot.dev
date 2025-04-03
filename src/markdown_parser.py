class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        if self.tag is None:
            return self.value or ""
        
        props_str = ""
        for prop, value in self.props.items():
            props_str += f' {prop}="{value}"'
        
        if self.tag == "img":
            return f"<{self.tag}{props_str} />"
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        
        if self.value is not None:
            return f"<{self.tag}{props_str}>{self.value}{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"

def markdown_to_html_node(markdown):
    lines = markdown.split("\n")
    root = HTMLNode(tag="div", children=[])
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Handle headers
        if line.startswith("# "):
            root.children.append(HTMLNode(tag="h1", value=line[2:].strip))