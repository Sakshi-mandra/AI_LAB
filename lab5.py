"""
LAB 05: Minimax Algorithm with Alpha-Beta Pruning for Game Playing
Aim: Implement the Minimax decision algorithm to determine optimal moves
     in a two-player zero-sum adversarial game environment.
"""

import math

def minimax(depth, node_index, maximizing_player, values, max_depth):

    # Terminal node
    if depth == max_depth:
        return values[node_index]

    if maximizing_player:
        return max(
            minimax(depth + 1, node_index * 2, False,
                    values, max_depth),
            minimax(depth + 1, node_index * 2 + 1, False,
                    values, max_depth)
        )

    else:
        return min(
            minimax(depth + 1, node_index * 2, True,
                    values, max_depth),
            minimax(depth + 1, node_index * 2 + 1, True,
                    values, max_depth)
        )


# Utility values of terminal states
values = [3, 5, 2, 9, 12, 5, 23, 23]

max_depth = 3

optimal_value = minimax(
    0, 0, True, values, max_depth
)

print("Optimal value:", optimal_value)