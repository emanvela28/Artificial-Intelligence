#
# astar.py
#
# This file provides a function implementing A* search for a route finding
# problem. Various search utilities from "route.py" are used in this function,
# including the classes RouteProblem, Node, and Frontier. Also, this function
# uses heuristic function objects defined in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
# I used most of my code from coding assignment from PA0 to see how I rooted nodes and used logic for state checking
# I used this video to learn more about heuristic search and A* search: https://www.youtube.com/watch?v=71CEj4gKDnE
# I used this video to learn more about A* search: https://www.youtube.com/watch?v=i0x5fj4PqP4
# I used this article to read more about A* search: https://www.geeksforgeeks.org/a-search-algorithm/
# I also referenced Class slides regarding different search types delivered on 09/12/23
# YOUR NAME - THE DATE
# Emmanuel Velazquez 10/17/2023


from route import Node
from route import Frontier


def a_star_search(problem, h, repeat_check=False):
    """Perform A-Star search to solve the given route finding problem,
    returning a solution node in the search tree, corresponding to the goal
    location, if a solution is found. Only perform repeated state checking if
    the provided boolean argument is true."""

    # Root the node at the starting location of the problem
    root = Node(problem.start)
    # Create the frontier with priority queue with the root node sorted by combined cost
    # Where f is the path from the root and heuristic value
    fifo = Frontier(root, sort_by='f')
    # Create a list called explored with the locations of the explored nodes
    explored = [root.loc]

    # If the current location is the goal, then return the node
    if problem.is_goal(root.loc):
        return root

    while not fifo.is_empty():
        # Pop the lowest f value in the frontier and explore it
        node = fifo.pop()

        # If it is a solution, return the node
        if problem.is_goal(node.loc):
            return node
        # Expand the current node to generate child nodes with heuristic function h.
        node_list = node.expand(problem, h_fun=h)

        # For every child node in the list check if the state, if not explored add to list
        for child in node_list:
            if repeat_check:
                if child.loc not in explored:
                    explored.append(child.loc)
                    fifo.add(child)
                else:
                    # If the child is in the frontier and the combined value is less than the previous, update the list
                    # If the child's location is not in the reached list, add it to the frontier
                    if fifo.contains(child) and (child.h_eval+child.path_cost) < (fifo.__getitem__(child)):
                        fifo.__delitem__(child)
                        fifo.add(child)
            else:
                # Add the nodes to the frontier
                fifo.add(child)

    return None
