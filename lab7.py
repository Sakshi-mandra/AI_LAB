"""
LAB 07: Forward Chaining and Backward Chaining Algorithms
Aim: Implement Forward Chaining and Backward Chaining to perform logical
    reasoning and infer conclusions from a set of facts and rules.
"""

class KnowledgeBase:
    """
    Represents a Rule-Based Knowledge Base.
    Rules are stored as tuples: (premises_set, conclusion)
    Example: ({'A', 'B'}, 'C') represents "IF A AND B THEN C"
    """
    def __init__(self, rules, initial_facts):
        self.rules = rules
        self.facts = set(initial_facts)


# PART A: FORWARD CHAINING
print("Forward chaining ------------------------------------")
def forward_chaining(facts, rules, goal):
    facts = set(facts)

    while True:
        new_fact_added = False

        for conditions, conclusion in rules:
            if set(conditions).issubset(facts):
                if conclusion not in facts:
                    facts.add(conclusion)
                    print("Inferred:", conclusion)
                    new_fact_added = True

        if goal in facts:
            print("Goal achieved:", goal)
            return True

        if not new_fact_added:
            break

    print("Goal cannot be proved:", goal)
    return False


# Initial facts
facts = ["A", "B"]

# Rules: (conditions, conclusion)
rules = [
    (["A", "B"], "C"),
    (["C"], "D"),
    (["D"], "E")
]

goal = "E"

print("Initial facts:", facts)
forward_chaining(facts, rules, goal)

# PART B: BACKWARD CHAINING
print("Backward chaining ------------------------------------")
def backward_chaining(goal, facts, rules, visited=None):
    if visited is None:
        visited = set()

    # If the goal is already a known fact
    if goal in facts:
        print("Fact found:", goal)
        return True

    # Avoid infinite loops
    if goal in visited:
        return False

    visited.add(goal)

    # Find rules that conclude the goal
    for conditions, conclusion in rules:
        if conclusion == goal:
            print("Trying to prove:", goal)

            # Every condition must be proved
            if all(
                backward_chaining(condition, facts, rules, visited.copy())
                for condition in conditions
            ):
                print("Proved:", goal)
                return True

    print("Cannot prove:", goal)
    return False


# Known facts
facts = {"A", "B"}

# Rules: (conditions, conclusion)
rules = [
    (["A", "B"], "C"),
    (["C"], "D"),
    (["D"], "E")
]

goal = "E"

print("Goal:", goal)

if backward_chaining(goal, facts, rules):
    print("Goal successfully proved.")
else:
    print("Goal could not be proved.")