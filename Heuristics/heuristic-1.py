#
# I used this to learn more about minimax https://brilliant.org/wiki/minimax/
# I used this to learn about the optimization about minimax https://levelup.gitconnected.com/improving-minimax-performance-fc82bc337dfd
# I referenced David Nolles slides about the minimax from 09-26-23 entitles Games
#
#
#
# Emmanuel Velazquez 11/28/23
#


from parameters import *
from minimax import probability_of_time
from minimax import value


def expected_value_over_delays(state, ply):
    """Calculate the expected utility over all possible randomly selected
    Guardian delay times. Return this expected utility value."""
    val = 0.0
    # Loop through all possible delay times
    for delay in range(min_time_steps, max_time_steps):
        # Set the time remaining in the game state to the current delay
        state.time_remaining = delay
        # Calculate the expected utility by multiplying the probability of the delay
        # with the value of the state after the delay
        val = val + (probability_of_time(delay) * value(state, ply))
    return val


def heuristic_value(state):
    """Return an estimate of the expected payoff for the given state of
    game play without performing any look-ahead search. This value must
    be between the maximum payoff value and the additive inverse of the
    maximum payoff."""

    val = 0.0
    # Calculate absolute values of board size and player/computer locations
    board_size_abs = abs(board_size)
    w_loc_abs = abs(state.w_loc)
    e_loc_abs = abs(state.e_loc)

    # Calculate values for the player and the computer based on the absolute locations
    player_value = board_size_abs - w_loc_abs
    computer_value = board_size_abs - e_loc_abs

    # Determine the heuristic value based on the comparison of player and computer values
    if player_value == computer_value:
        val = -25 if state.current_turn is Player.west else 25
    elif player_value > computer_value:
        val = -100 if state.current_turn is Player.west else -50
    else:
        val = 100 if state.current_turn is Player.east else 50

    return val
