def A_Ex4(g, u):
    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in g.get(node, []):
            dfs(neighbor)

    dfs(u)
    return "".join(sorted(visited))
# Example usage:
g = {   'a': ['b', 'c'],
        'b': ['d'],
        'c': ['d', 'e'],
        'd': [],
        'e': []}
u = 'a'
result = A_Ex4(g, u)
print(result)  # Output: 'abcde'
