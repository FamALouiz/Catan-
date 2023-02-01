from _global_game import game
from pycatan._game import BuildingType, DevelopmentCard
from _building_phase import choose_path, choose_intersection


def build_road(current_player):
    # Check the player has enough resources
    if not current_player.has_resources(BuildingType.ROAD.get_required_resources()):
        print("You don't have enough resources to build a road")
        return False
    # Get the valid road coordinates
    valid_coords = game.board.get_valid_road_coords(current_player)
    # If there are none
    if not valid_coords:
        print("There are no valid places to build a road")
        return False
    # Have the player choose one
    path_coords = choose_path(valid_coords, "Where do you want to build a road?")
    game.build_road(current_player, path_coords)


def build_city(current_player):
    # Check the player has enough resources
    if not current_player.has_resources(BuildingType.CITY.get_required_resources()):
        print("You don't have enough resources to build a city")
        return False
    # Get the valid coords to build a city at
    valid_coords = game.board.get_valid_city_coords(current_player)
    # Have the player choose one
    coords = choose_intersection(valid_coords, "Where do you want to build a city?  ")
    # Build the city
    game.upgrade_settlement_to_city(current_player, coords)


def build_settlement(current_player):
    # Check the player has enough resources
    if not current_player.has_resources(
        BuildingType.SETTLEMENT.get_required_resources()
    ):
        print("You don't have enough resources to build a settlement")
        return False
    # Get the valid coords to build a city at
    valid_coords = game.board.get_valid_settlement_coords(current_player)
    # Have the player choose one
    coords = choose_intersection(
        valid_coords, "Where do you want to build a settlement?  "
    )
    # Build the city
    game.build_settlement(current_player, coords)


def build_development(current_player):
    # Check the player has the resources to build a development card
    if not current_player.has_resources(DevelopmentCard.get_required_resources()):
        print("You do not have the resources to build a development card")
        return False
    # Build a card and tell the player what they build
    dev_card = game.build_development_card(current_player)
    print("You built a %s card" % dev_card)


def build_something(current_player):
    # Assume possibility
    road_possible = True
    city_possible = True
    settlement_possible = True
    developement_possible = True
    while True:
        print("What do you want to build/buy? ")
        print("1 - Settlement")
        print("2 - City")
        print("3 - Road")
        print("4 - Development card")
        print("5 - End Turn")
        building_choice = int(input("->  "))
        if building_choice == 1 and settlement_possible:
            # If can't build then set it to false for time management
            settlement_possible = build_settlement(current_player)
        elif building_choice == 2 and city_possible:
            # If can't build then set it to false for time management
            city_possible = build_city(current_player)
        elif building_choice == 3 and road_possible:
            # If can't build then set it to false for time management
            road_possible = build_road(current_player)
        elif building_choice == 4 and developement_possible:
            developement_possible = build_development(current_player)
        elif building_choice == 5:
            break
        else:
            print("Not a valid move")
