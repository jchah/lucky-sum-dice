import random
import matplotlib
import matplotlib.pyplot as plt

TRIALS = 1000000000
trials_completed = 0
matplotlib.use('Qt5Agg')


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turns = 0

    sum_frequency = {i: 0 for i in range(3, 19)}

    def roll_dice(self):
        global trials_completed
        die1, die2 = random.randint(1, 6), random.randint(1, 6)
        dice_sum = die1 + die2
        self.turns += 1

        if die1 == die2:
            bonus_roll = random.randint(1, 6)
            dice_sum += bonus_roll

        Player.sum_frequency[dice_sum] += 1
        self.score += dice_sum
        trials_completed += 1


def play_game(players, target_score=50):
    players = [Player(name) for name in players]
    game_over = False

    while not game_over:
        for player in players:
            player.roll_dice()

            if player.score >= target_score:
                game_over = True

    highest_score = max(player.score for player in players)
    winners = [player for player in players if player.score == highest_score]

    while len(winners) > 1:
        for player in winners:
            player.roll_dice()
        highest_score = max(winner.score for winner in winners)
        winners = [winner for winner in winners if winner.score == highest_score]

    winner = winners[0]
    return winner, players


def play_game_for_trials(players, trials):
    global trials_completed
    while trials_completed < trials:
        play_game(players)


def plot_distribution():
    x = list(range(3, 19))
    frequencies = [Player.sum_frequency[key] for key in x]

    plt.bar(x, frequencies)
    plt.title(f"Distribution of Dice Rolls over {TRIALS} Trials")
    plt.xlabel("Sum of Dice Rolls")
    plt.ylabel("Frequency")
    plt.xticks(x)
    plt.show()

    total_trials = sum(frequencies)

    probabilities = [freq / total_trials for freq in frequencies]

    print(frequencies)
    print(probabilities)

    plt.bar(x, probabilities)
    plt.title(f"Probability Distribution of Dice Rolls over {TRIALS} Trials")
    plt.xlabel("Sum of Dice Rolls")
    plt.ylabel("Probability")
    plt.xticks(x)
    plt.show()


players_list = ["Alice", "Bob", "Charlie"]
play_game_for_trials(players_list, TRIALS)
plot_distribution()
