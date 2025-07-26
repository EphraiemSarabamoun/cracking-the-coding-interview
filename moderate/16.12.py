class Element:
    def __init__(self, tag: str, attrs: dict[str, str], children: list['Element']):
        self.tag = tag
        self.attrs = attrs
        self.children = children

def encode_xml(root: Element, tag_map: dict[str, int], attr_map: dict[str, int]) -> str:
    def encode(e: Element) -> list[int]:
        code = [tag_map[e.tag]]
        for name, val in e.attrs.items():
            code.append(attr_map[name])
            code.append(int(val))  # Assume int values
        code.append(0)  # End attrs
        for child in e.children:
            code.extend(encode(child))
        code.append(0)  # End tag
        return code
    codes = encode(root)
    return ' '.join(map(str, codes))