"""
Lab 2: Search Algorithms in Artificial Intelligence
1. Best First Search (Greedy)
2. A* Search
3. AO* Search (AND-OR Graph)
4. Hill Climbing Search
"""

import heapq

# 1. BEST FIRST SEARCH (GREEDY)
def best_first_search(graph, heuristics, start, goal):
    """
    Evaluates nodes based solely on heuristic value h(n).
    """
    open_list = [(heuristics[start], start, [start])]
    visited = set()

    while open_list:
        h_val, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, h_val

        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristics[neighbor], neighbor, path + [neighbor]))

    return None, float('inf')


# 2. A* SEARCH ALGORITHM
def a_star_search(graph, heuristics, start, goal):
    """
    Evaluates nodes based on f(n) = g(n) + h(n).
    """
    open_list = [(heuristics[start], 0, start, [start])]
    g_scores = {start: 0}

    while open_list:
        f_score, g_score, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, g_score

        for neighbor, weight in graph.get(current, []):
            tentative_g = g_score + weight

            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristics[neighbor]
                heapq.heappush(open_list, (f_score, tentative_g, neighbor, path + [neighbor]))

    return None, float('inf')


# 3. AO* SEARCH (AND-OR GRAPH)
class AOStar:
    """
    Solves AND-OR graph structures by recursively updating cost estimates.
    """
    def __init__(self, graph, heuristics, start):
        self.graph = graph
        self.heuristics = heuristics
        self.start = start
        self.solution_graph = {}

    def get_cost(self, node):
        if node not in self.graph:
            return self.heuristics.get(node, 0), []

        min_cost = float('inf')
        best_branch = []

        for branch in self.graph[node]:
            # Sum up costs for AND branches
            cost = sum(self.heuristics[child] + weight for child, weight in branch)
            if cost < min_cost:
                min_cost = cost
                best_branch = branch

        return min_cost, best_branch

    def search(self, node):
        cost, best_branch = self.get_cost(node)
        self.heuristics[node] = cost
        self.solution_graph[node] = best_branch

        for child, weight in best_branch:
            if child in self.graph:
                self.search(child)

    def run(self):
        self.search(self.start)
        return self.solution_graph


# 4. HILL CLIMBING ALGORITHM
def hill_climbing(graph, heuristics, start, goal):
    """
    Iterative local search moving to the best immediate neighbor.
    """
    current = start
    path = [current]

    while current != goal:
        neighbors = graph.get(current, [])
        if not neighbors:
            break

        # Pick neighbor with lowest heuristic h(n)
        next_node = min(neighbors, key=lambda x: heuristics[x[0]])[0]

        # Stop if no strictly better neighbor is available
        if heuristics[next_node] >= heuristics[current]:
            print(f"   [Hill Climbing] Local maximum / plateau hit at: {current}")
            break

        current = next_node
        path.append(current)

    return path


# MAIN EXECUTION
if __name__ == "__main__":
    # Standard Graph Setup for Best-First, A*, and Hill Climbing
    graph = {
        'A': [('B', 2), ('C', 1)],
        'B': [('D', 5), ('E', 2)],
        'C': [('F', 3)],
        'D': [],
        'E': [('G', 1)],
        'F': [('G', 4)],
        'G': []
    }

    heuristics = {
        'A': 6,
        'B': 4,
        'C': 4,
        'D': 7,
        'E': 2,
        'F': 3,
        'G': 0
    }

    start_node = 'A'
    goal_node = 'G'

    print("=" * 50)
    print("LAB 2: AI SEARCH ALGORITHMS DEMONSTRATION")
    print("=" * 50)

    # 1. Best First Search
    bfs_path, _ = best_first_search(graph, heuristics, start_node, goal_node)
    print("\n1. Best First Search Path:")
    print("   ", " -> ".join(bfs_path) if bfs_path else "No Path Found")

    # 2. A* Search
    a_star_path, total_cost = a_star_search(graph, heuristics, start_node, goal_node)
    print("\n2. A* Search Path:")
    print(f"    {' -> '.join(a_star_path)} (Total Cost g(n): {total_cost})")

    # 3. AO* Search
    ao_graph = {
        'A': [[('B', 1), ('C', 1)], [('D', 1)]],  # Branch 1: (B AND C), Branch 2: D
        'B': [[('G', 1)]],
        'C': [[('H', 1)]]
    }
    ao_heuristics = {'A': 10, 'B': 6, 'C': 3, 'D': 12, 'G': 0, 'H': 0}

    ao_solver = AOStar(ao_graph, ao_heuristics, 'A')
    solution = ao_solver.run()

    print("\n3. AO* Solution Subtree:")
    for parent, children in solution.items():
        child_names = [c[0] for c in children]
        print(f"   {parent} -> {child_names if child_names else 'GOAL'}")

    # 4. Hill Climbing
    hc_path = hill_climbing(graph, heuristics, start_node, goal_node)
    print("\n4. Hill Climbing Path:")
    print("   ", " -> ".join(hc_path))
    print("=" * 50)