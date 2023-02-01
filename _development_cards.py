from pycatan._game import DevelopmentCard


def choose_development_card(current_player):
    # Choose a development card
    print("What card do you want to play?")
    dev_cards = [
        card
        for card, amount in current_player.development_cards.items()
        if amount > 0 and card is not DevelopmentCard.VICTORY_POINT
    ]
    for i in range(len(dev_cards)):
        print("%d: %s" % (i, dev_cards[i]))
        card_to_play = dev_cards[int(input("->  "))]
