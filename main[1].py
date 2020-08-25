from Classes.PKGame import *
from Classes.Player import *
from functions import *

if __name__ == '__main__':
    # Create game using payoffs from data set
    kicker_payoffs = np.array([[63.6, 94.6], [89.3, 43.7]])

    # Define probabilities for Kicker and Goalie using the results of the Nash Eq Calculation
    kicker_natural_prob, goalie_natural_prob = nash_eq(kicker_payoffs)

    # Create game and let it run, allowing the user to play again or open results file at the end
    user_choice = ''
    while user_choice != 'q':
        PKgame = PKGame()
        player_goals, CPU_goals, winner = PKgame.game(kicker_payoffs, kicker_natural_prob, goalie_natural_prob)
        print_to_file(player_goals, CPU_goals, winner)
        user_choice = input('Press q to quit, h to view history and quit, or any other key to play again:\n')
        if user_choice == 'h':
            os.system('results.dat')
            user_choice = 'q'
            
    
