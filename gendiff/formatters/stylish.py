"""Stylish module - apply stylish view to diff (by default)"""

INDENT_SIZE = 4


def get_indent(depth: int, indent_size: int = INDENT_SIZE) -> str:
    return ' ' * (depth * indent_size - 2)


def to_string(value, depth: int) -> str:
    if isinstance(value, bool):
        return 'true' if value else 'false'

    if value is None:
        return 'null'

    if isinstance(value, dict):
        indent = get_indent(depth)
        current_indent = indent + (" " * (INDENT_SIZE + 2))
        lines = []
        for k, v in value.items():
            lines.append(f'{current_indent}{k}: {to_string(v, depth + 1)}')
        result = '\n'.join(lines)
        return f'{{\n{result}\n  {indent}}}'

    return value


def get_root_node(node, depth):
    children = node.get('children')
    lines = map(lambda child: iter_(child, depth + 1), children)
    result = '\n'.join(lines)
    return f'{{\n{result}\n}}'


def get_nested_node(node, depth):
    children = node.get('children')
    indent = get_indent(depth, indent_size=INDENT_SIZE)
    lines = map(lambda child: iter_(child, depth + 1), children)
    result = '\n'.join(lines)
    return f'{indent}  {node["key"]}: {{\n{result}\n  {indent}}}'


def get_changed_node(node, depth):
    indent = get_indent(depth, indent_size=INDENT_SIZE)
    formatted_value1 = to_string(node.get('old_value'), depth)
    formatted_value2 = to_string(node.get('new_value'), depth)
    line1 = f'{indent}- {node["key"]}: {formatted_value1}\n'
    line2 = f'{indent}+ {node["key"]}: {formatted_value2}'
    result = line1 + line2
    return result


def get_unchanged_node(node, depth):
    formatted_value = to_string(node.get('value'), depth)
    indent = get_indent(depth, indent_size=INDENT_SIZE)
    return f'{indent}  {node["key"]}: {formatted_value}'


def get_removed_node(node, depth):
    formatted_value = to_string(node.get('value'), depth)
    indent = get_indent(depth, indent_size=INDENT_SIZE)
    return f'{indent}- {node["key"]}: {formatted_value}'


def get_added_node(node, depth):
    formatted_value = to_string(node.get('value'), depth)
    indent = get_indent(depth, indent_size=INDENT_SIZE)
    return f'{indent}+ {node["key"]}: {formatted_value}'


def iter_(node: dict, depth=0) -> str:
    types = {
        'root': get_root_node,
        'nested': get_nested_node,
        'changed': get_changed_node,
        'unchanged': get_unchanged_node,
        'removed': get_removed_node,
        'added': get_added_node,
    }

    if node['type'] in types:
        return types[node['type']](node, depth)

    else:
        raise ValueError("Unknown node type")


def format_(node: dict):
    return iter_(node)
