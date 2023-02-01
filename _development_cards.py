from pycatan._game import DevelopmentCard


def choose_development_card(current_player):
    # Choose a development card
    print("What card do you want to play?")
    dev_cards = [
        card
        for card, amount in current_player.development_cards.items()
        if amount > 0 and card is not DevelopmentCard.VICTORY_POINT
    ]
    if len(dev_cards) == 0:
        print("You don't have any development card to play")
        return False
    for i in range(len(dev_cards)):
        print("%d: %s" % (i, dev_cards[i]))

    while True:
        card_pick = int(input("->  "))

        if card_pick > len(dev_cards) - 1:
            print("Invalid card pick")
            continue
        break
    card_to_play = dev_cards[card_pick]
    return card_to_play


def play_development(develpoment):
    # TBD
    return
