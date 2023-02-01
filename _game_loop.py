import random
from _global_game import game
from _buildings import build_something
from _trading import trade
from _development_cards import choose_development_card


def player_move(current_player_num):
    # Print the player's resources
    current_player = game.players[current_player_num]
    print("Player %d, you have these resources:" % (current_player_num + 1))
    for res, amount in zip(
        current_player.resources.keys(), current_player.resources.values()
    ):
        print("%s: %d" % (res, amount))
    print("and you have these development cards")
    for dev_card, amount in zip(
        current_player.development_cards.keys(),
        current_player.development_cards.values(),
    ):
        print("    %s: %d" % (dev_card, amount))
    while True:
        # Prompt the player for an action
        print("Choose what to do:")
        print("1 - Build something")
        print("2 - Trade")
        print("3 - Play a dev card")
        choice = int(input("->  "))
        if choice == 1:
            build_something(current_player)
        elif choice == 2:
            trade(current_player)
        elif choice == 3:
            development_chosen = choose_development_card(current_player)
        else:
            print("Invalid move")
        if choice in [1, 2, 3]:
            current_player_num = (current_player_num + 1) % len(game.players)
            return current_player_num


def game_loop():
    current_player_num = 0
    while True:
        print("Player %d, it is your turn now" % (current_player_num + 1))
        # Roll the dice
        dice = random.randint(1, 6) + random.randint(1, 6)
        print("Player %d rolled a %d" % (current_player_num + 1, dice))
        if dice == 7:
            # TBA
            current_player_num = player_move(current_player_num)
            pass
        else:
            game.add_yield_for_roll(dice)
            current_player_num = player_move(current_player_num)
