import nashpy as nash
import os
from colorama import init, Fore, Style


def nash_eq(kicker_payoffs):
    """ Returns the probabilities that the CPU kicker and goalie will act towards the natural side of the goalie.

        Parameters:
            kicker_payoffs (array): array of payoffs the kicker has for each decision grouping, taken from research
                                    paper

        Returns:
            KickerNaturalProb (float), GoalieNaturalProb (float): probabilities that the kicker and goalie should act
                                                                  towards the kicker's natural side in order to be in
                                                                  equilibrium.

    """
    goalie_payoffs = 100 - kicker_payoffs
    pk = nash.Game(kicker_payoffs, goalie_payoffs)
    nash_equilibrium = list(pk.support_enumeration())
    kicker_natural_prob = nash_equilibrium[0][0][0]
    goalie_natural_prob = nash_equilibrium[0][1][0]
    return kicker_natural_prob, goalie_natural_prob


def print_to_file(player_goals, cpu_goals, result):
    """ Prints the results of each game, including the amount of goals the user and CPU scored and the winner, to a file
        called results.dat.

        Parameters:
            player_goals (int): number of goals the player scored
            cpu_goals (int): number of goals the CPU scored
            result (int): the name of the winner, either CPU or the name the user entered at the beginning of the game

        Returns:
            None
    """
    exists = os.path.isfile('results.dat')
    # If the results file is already created, just add the new game data. If not, add a line that tells what data is in
    # each line and another with the game data.
    if exists:
        results = open('results.dat', 'a')
        results.write('%d, %d, %s\n' % (player_goals, cpu_goals, result))
        results.close()
    else:
        results = open('results.dat', 'w+')
        results.write('Player Goals, CPU Goals, Winner\n')
        results.write('%d, %d, %s\n' % (player_goals, cpu_goals, result))
        results.close()
    print('Results saved! Come back soon!')


def print_in_color(text, color):
    """ Returns text in a specified color (either red, green, or yellow).

        Parameters:
            text (str): the text that is to be colored
            color (str): the color that the text should be (either red, green, or yellow)

        Returns:
            A string of the text whose foreground color has been changed to the color specified. The foreground color is
            also reset so that subsequent text is not colored.

        """
    color = color.lower()
    init(autoreset=True)
    if color == 'red':
        return Fore.RED + Style.BRIGHT + text + Fore.RESET + Style.RESET_ALL
    elif color == 'green':
        return Fore.GREEN + Style.BRIGHT + text + Fore.RESET + Style.RESET_ALL
    elif color == 'yellow':
        return Fore.YELLOW + Style.BRIGHT + text + Fore.RESET + Style.RESET_ALL
    else:
        return 'Color not supported. Try RED or GREEN.'
