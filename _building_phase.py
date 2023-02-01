from pycatan import Game
from pycatan.board import BeginnerBoard, BoardRenderer
import string

game = Game(BeginnerBoard())
renderer = BoardRenderer(game.board)


def get_coord_sort_by_xy(c):
    x, y = renderer.get_coords_as_xy(c)
    return 1000 * x + y


label_letters = string.ascii_lowercase + string.ascii_uppercase + "123456789"


def choose_intersection(intersection_coords, prompt):
    # Label all the letters on the board
    intersection_list = [game.board.intersections[i] for i in intersection_coords]
    intersection_list.sort(key=lambda i: get_coord_sort_by_xy(i.coords))
    intersection_labels = {
        intersection_list[i]: label_letters[i] for i in range(len(intersection_list))
    }
    renderer.render_board(intersection_labels=intersection_labels)
    # Prompt the user
    letter = input(prompt)
    letter_to_intersection = {v: k for k, v in intersection_labels.items()}
    intersection = letter_to_intersection[letter]
    return intersection.coords


def choose_path(path_coords, prompt):
    # Label all the paths with a letter
    path_list = [game.board.paths[i] for i in path_coords]
    path_labels = {path_list[i]: label_letters[i] for i in range(len(path_coords))}
    renderer.render_board(path_labels=path_labels)
    # Ask the user for a letter
    letter = input(prompt)[0]
    # Get the path from the letter entered by the user
    letter_to_path = {v: k for k, v in path_labels.items()}
    return letter_to_path[letter].path_coords


def building_phase():
    player_order = list(range(len(game.players)))
    for i in player_order + list(reversed(player_order)):
        current_player = game.players[i]
        print("Player %d, it is your turn!" % (i + 1))
        coords = choose_intersection(
            game.board.get_valid_settlement_coords(
                current_player, ensure_connected=False
            ),
            "Where do you want to build your settlement? ",
        )
        game.build_settlement(
            player=current_player,
            coords=coords,
            cost_resources=False,
            ensure_connected=False,
        )
        current_player.add_resources(
            game.board.get_hex_resources_for_intersection(coords)
        )
        # Print the road options
        road_options = game.board.get_valid_road_coords(
            current_player, connected_intersection=coords
        )
        road_coords = choose_path(
            road_options, "Where do you want to build your road to? "
        )
        game.build_road(
            player=current_player, path_coords=road_coords, cost_resources=False
        )
