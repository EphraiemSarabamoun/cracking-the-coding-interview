from collections import defaultdict, deque

def build_order(projects,dependencies):
    adjacency_list = defaultdict(list)
    in_degree = {proj: 0 for proj in projects}

    for prereq, dependent in dependencies:
        adjacency_list[prereq].append(dependent)
        in_degree[dependent] += 1
    
    queue = deque()
    for proj in projects:
        if in_degree[proj] == 0:
            queue.append(proj)
    
    order = []
    while queue:
        current_proj = queue.popleft()
        order.append(current_proj)
        for dependent in adjacency_list[current_proj]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)
    
    if len(order) == len(projects):
        return order
    return None

if __name__ == "__main__":
    projects = ["a","b","c","d","e","f"]
    dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
    print(build_order(projects,dependencies))

    
    

