from collections import deque

def route_between_nodes(graph: Graph,node1: Node, node2: Node) -> bool:
    if node1 == node2:
        return True
    queue = deque([node1])
    visited = set([node1])
    while queue:
        node = queue.popleft()
        for neighbor in node.neighbors:
            if neighbor == node2:
                return True
            elif neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return False