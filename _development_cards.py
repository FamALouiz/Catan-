from pycatan._game import DevelopmentCard
from pycatan._resource import Resource
from _global_game import game, renderer
from _building_phase import choose_path, label_letters, get_coord_sort_by_xy


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
    develpoment = dev_cards[card_pick]
    return develpoment


def choose_hex(hex_coords, prompt):
    # Label all the hexes with a letter
    hex_list = [game.board.hexes[i] for i in hex_coords]
    hex_list.sort(key=lambda h: get_coord_sort_by_xy(h.coords))
    hex_labels = {hex_list[i]: label_letters[i] for i in range(len(hex_list))}
    renderer.render_board(hex_labels=hex_labels)
    letter = input(prompt)
    letter_to_hex = {v: k for k, v in hex_labels.items()}
    return letter_to_hex[letter].coords


def move_robber(current_player):
    # Don't let the player move the robber back onto the same hex
    hex_coords = choose_hex(
        [c for c in game.board.hexes if c != game.board.robber],
        "Where do you want to move the robber? ",
    )
    game.board.robber = hex_coords
    potential_players = list(game.board.get_players_on_hex(hex_coords))
    print("Choose who you want to steal from:")
    for p in potential_players:
        i = game.players.index(p)
        print("%d: Player %d" % (i + 1, i + 1))
    p = int(input("->  ")) - 1
    # If they try and steal from another player they lose their chance to steal
    to_steal_from = game.players[p] if game.players[p] in potential_players else None
    if to_steal_from:
        resource = to_steal_from.get_random_resource()
        current_player.add_resources({resource: 1})
        to_steal_from.remove_resources({resource: 1})
        print("Stole 1 %s for player %d" % (resource, p + 1))


def choose_resource(message):
    print(message)
    resources = []
    for i, resource in zip(range(len(Resource)), Resource):
        print(f"{i}: {resource}")
        resources.append(resource)
    while True:
        resource_pick = int(input("-> "))
        if resource_pick > len(Resource) - 1:
            print("Invalid pick")
            continue
        break
    return resources[resource_pick]


def play_development(current_player, develpoment):

    if develpoment is DevelopmentCard.KNIGHT:
        move_robber(current_player)

    elif develpoment is DevelopmentCard.YEAR_OF_PLENTY:
        # Have the player choose 2 resources to receive
        for _ in range(2):
            resource = choose_resource("What resource do you want to receive?")
            # Add that resource to the player's hand
            current_player.add_resources({resource: 1})

    elif develpoment is DevelopmentCard.ROAD_BUILDING:
        # Allow the player to build 2 roads
        for _ in range(2):
            valid_path_coords = game.board.get_valid_road_coords(current_player)
            path_coords = choose_path(
                valid_path_coords, "Choose where to build a road: "
            )
            game.build_road(current_player, path_coords, cost_resources=False)

    elif develpoment is DevelopmentCard.MONOPOLY:
        # Choose a resource
        resource = choose_resource("What resource do you want to take?")
        # Remove that resource from everyone else's hands and add it to the current player's hand
        for i in range(len(game.players)):
            player = game.players[i]
            if player is not current_player:
                amount = player.resources[resource]
                player.remove_resources({resource: amount})
                current_player.add_resources({resource: amount})
                print("Took %d from player %d" % (amount, i + 1))
    return
