#
# ucost.py
#
# This file provides a function implementing uniform cost search for a
# route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS
# I used most of my code from coding assignment from PA0 to see how I rooted nodes and used logic for state checking
# I used this article to read more about uniformed search: https://www.educba.com/uniform-cost-search/
# I watched this video to learn more about uniform cost search: https://www.youtube.com/watch?v=dRMvK76xQJI
# I also referenced Class slides regarding different search types delivered on 09/12/23
# YOUR NAME - THE DATE
# Emmanuel Velazquez 10/17/2023


from route import Node
from route import Frontier


def uniform_cost_search(problem, repeat_check=False):
    """Perform uniform cost search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE

    # We begin by rooting the node at the beginning of the problem
    root = Node(problem.start)

    # This not is then added to the frontier where g allows us to sort nodes by path cost.
    fifo = Frontier(root, sort_by='g')

    # Explored allows us to store nodes that we have already explored
    explored = [root.loc]

    # If our starting location is the goal, then we will return this node as a solution
    if problem.is_goal(root.loc):
        return root

    # Our loop is going to continue until the whole frontier is explored
    while not fifo.is_empty():

        # We are removing nodes with the lowest path cost first
        node = fifo.pop()

        # If this node is the solution, the renturn the node
        if problem.is_goal(node.loc):
            return node

        # Expand the node with child nodes
        node_list = node.expand(problem)
        for child in node_list:

            # Check if we have already explored the child node
            if repeat_check:

                # If the location of child node is not in the explored, then we will append it to the explored list
                if child.loc not in explored:
                    explored.append(child.loc)
                    # We will add the child node to the frontier to explore further
                    fifo.add(child)
                else:
                    # Check to see if the frontier contains the child node and if it does it means we have a known path
                    # and we check to see if the new path cost is lower than the previous node, and if it is then we
                    # will add it to the frontier
                    if fifo.contains(child) and child.path_cost < (fifo.__getitem__(child)):
                        fifo.__delitem__(child)
                        fifo.add(child)
            else:
                # If repeat check is false then we are going to ass the current node to the frontier without checking.
                fifo.add(child)

    return None
