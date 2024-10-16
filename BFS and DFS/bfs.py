#
# bfs.py
#
# This file provides a function implementing breadth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# I used this website to better my understanding of BFS https://favtutor.com/blogs/breadth-first-search-python
# I also used this website to refresh my memory of working with python syntax https://www.pythontutorial.net/python-basics/python-syntax/
# https://www.youtube.com/watch?v=HZ5YTanv5QE this video helped me further my understanding of BFS and the uses of pop
#
#
# Emmanuel Velazquez 09/24/23
#


from route import Node
from route import Frontier


def BFS(problem, repeat_check=False):
    """Perform breadth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    root_node = Node(problem.start)
    frontier = Frontier(root_node)
    # Set to keep track of explored locations
    explored = set()

    # Get the next node from the frontier
    while not frontier.is_empty():
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
