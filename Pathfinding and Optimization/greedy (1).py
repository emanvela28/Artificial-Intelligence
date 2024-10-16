#
# greedy.py
#
# This file provides a function implementing greedy best-first search for
# a route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier. Also, this function uses heuristic function objects defined
# in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
# I used most of my code from coding assignment from PA0 to see how I rooted nodes and used logic for state checking
# I used this article to read more about greedy first search:
# https://www.codecademy.com/resources/docs/ai/search-algorithms/greedy-best-first-search
# I used this article to read more about greedy first search:
# https://www.geeksforgeeks.org/greedy-best-first-search-algorithm/
# I watched this video to learn more about greedy-first search: https://www.youtube.com/watch?v=dv1m3L6QXWs
# I also referenced Class slides regarding different search types delivered on 09/12/23
# YOUR NAME - THE DATE
# Emmanuel Velazquez 10/17/2023

from route import Node
from route import Frontier


def greedy_search(problem, h, repeat_check=False):
    """Perform greedy best-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    # Create a root node with the start location of the problem
    root = Node(problem.start)
    # Create a frontier (priority queue) with the root node as the initial element, sorted by the heuristic value h(n)
    # alone. The algorithm prioritizes nodes with lower heuristic values.
    fifo = Frontier(root, sort_by='h')
    # Create a list called explored with the locations of the explored nodes
    explored = [root.loc]

    # If the root node location is the goal location, if it is return the node as a solution.
    if problem.is_goal(root.loc):
        return root

    while not fifo.is_empty():
        # Pop the node with the lowest h value from the frontier and expand it in the search
        node = fifo.pop()
        # Check the location of the popped node, if it's the goal then return the node.
        if problem.is_goal(node.loc):
            return node

        # Expand the node to generate child nodes using h.
        node_list = node.expand(problem, h_fun=h)
        for child in node_list:
            # Perform state checking
            if repeat_check:
                # If the child node is not in the explored list, then add the child node to the list
                if child.loc not in explored:
                    explored.append(child.loc)
                    fifo.add(child)
            else:
                # If it is false, add all the nodes to the frontier
                fifo.add(child)

    return None
