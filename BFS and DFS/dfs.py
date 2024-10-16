#
# dfs.py
#
# This file provides a function implementing depth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
# 
# I watched this video to understand the implementation of DFS in python https://www.youtube.com/watch?v=Sbciimd09h4
# # I also used this website to refresh my memory of working with python syntax https://www.pythontutorial.net/python-basics/python-syntax/
# https://www.youtube.com/watch?v=Urx87-NMm6c this video was useful in understanding DFS and pop and stack
#
# Emmanuel Velazquez 09/23/23
# 


from route import Node
from route import Frontier


def DFS(problem, repeat_check=False):
    """Perform depth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # Give the frontier a starting place, rooting the node at the starting location of the problem
    root_node = Node(problem.start)
    # Use a stack for DFS
    frontier = Frontier(root_node, stack=True)


    # Set to keep track of explored locations
    explored = set()
    while not frontier.is_empty():
        # Get the next node from the frontier
        node = frontier.pop()

        # Solution found
        if problem.is_goal(node.loc):
            return node

        # Skip already explored locations
        if repeat_check:
            if node.loc in explored:
                continue

        explored.add(node.loc)

        # Expand the current node and add child nodes to the frontier
        child_nodes = node.expand(problem)
        frontier.add(child_nodes)

    # No solution found
    return None
