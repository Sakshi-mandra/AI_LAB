# 1. linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # index where target was found

    return -1  # target not found

 
# 2. binary search    
def binary_search(arr, target, start, end):
    if start > end:
           return -1
       
    mid = start + (end-start) // 2
    
    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        return binary_search(arr, target, mid+1, end)
    else:
        return binary_search(arr, target, start, mid-1) 
           
 
   
numbers = [10, 25, 70, 89, 108]

result = linear_search(numbers, 25)
result = binary_search(numbers, 89, 0, len(numbers)-1)

if result != -1:
    print("Found at index:", result)
else:
    print("Not found")
    
from collections import deque


# Graph Representation (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# 3. Breadth-First Search (BFS)
def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return order

# 4. Depth-First Search (DFS)
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
        
    visited.add(node)
    order = [node]
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            order.extend(dfs_recursive(graph, neighbor, visited))
            
    return order


if __name__ == "__main__":
    start = 'A'
    
    print("Graph Structure:", graph)
    print("-" * 50)
    print(f"BFS Traversal (from '{start}'):        ", bfs(graph, start))
    print(f"DFS Recursive (from '{start}'):        ", dfs_recursive(graph, start))   

