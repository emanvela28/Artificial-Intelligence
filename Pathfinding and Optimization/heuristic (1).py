#
# heuristic.py
#
# This script defines a utility class that can be used as an implementation
# of a frontier state (location) evaluation function for use in route-finding
# heuristic search algorithms. When a HeuristicSearch object is created,
# initialization code can be executed to prepare for the use of the heuristic
# during search. In particular, a RouteProblem object is typically provided 
# when the HeuristicFunction is created, providing information potentially
# useful for initialization. The actual heuristic cost function, simply
# called "h_cost", takes a state (location) as an argument.
#
# YOUR COMMENTS INCLUDING CITATIONS
# I used most of my code from coding assignment from PA0 to see how I rooted nodes and used logic for state checking
# I used this video to learn more about heuristic search and A* search: https://www.youtube.com/watch?v=71CEj4gKDnE
# I used this article to read more about heuristic search: https://en.wikipedia.org/wiki/Heuristic_(computer_science)
# I also referenced Class slides regarding different search types delivered on 09/12/23
# YOUR NAME - THE DATE
# Emmanuel Velazquez 10/17/2023


import route


class HeuristicFunction:
    """A heuristic function object contains the information needed to
    evaluate a state (location) in terms of its proximity to an optimal
    goal state."""

    def __init__(self, problem=None):
        self.problem = problem
        # PLACE ANY INITIALIZATION CODE HERE
        self.cost = problem.map
        self.time = 0
        time = 0
        count = 0

        # Get a lost of all locations in the road map
        places = problem.map.locations()

        # Make empty lists to store visited locations
        visit = []
        visit2 = []

        # Iterate through each unknown in the list named places
        for unknown in places:

            # Calculate road segments from unknown to all other locations
            road = problem.action_cost(unknown, end=None)
            # Mark the location as visited
            visit.append(unknown)
            # Iterate through road segments
            for segment in road:
                # Check to see if the unknown location is in either list and increase count if it is.
                if unknown in visit or visit2:
                    count += 1
                    # Calculate time based on the road segment and add it to time
                time = time + problem.action_cost(unknown, segment)
                count += 1
                # Add the segment to the list to mark it as visited
                visit2.append(segment)

        self.time = time/count

    def h_cost(self, loc=None):
        """An admissible heuristic function, estimating the cost from
        the specified location to the goal state of the problem."""
        # a heuristic value of zero is admissible but not informative
        value = 0.0
        if loc is None:
            return value
        else:
            # PLACE YOUR CODE FOR CALCULATING value OF loc HERE
            # value = self.problem.map.euclidean_distance(loc, self.problem.goal)
            # value = self.cost.euclidean_distance(loc, self.problem.goal)/4.8
            value = self.cost.euclidean_distance(loc, self.problem.goal)/self.time
            return value
