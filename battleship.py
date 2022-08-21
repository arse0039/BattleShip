# Author: Brandon Arsenault
# Date: 03/03/22
# GitHub Username: arse0039

class WrongPlayer(Exception):
    def __str__(self):
        return "Invalid Player Selection! NO CHEATING"


def create_grid(grid_size):
    """ This is a global function that creates and returns dictionary object to be used to make a visual 
    game board for our ShipGame. The keys are the letter designators for each row of the game board and the
    values are lists with a number of elements equal to the integer argument passed into the grid_size parameter. 
    Each element will be filled with an 'open board tile' visual that we can print to the console later in program."""
    grid = {}
    for i in range(grid_size):
        char = chr(65+i)
        grid_row = ["|_|" for i in range(grid_size)]
        grid[char] = grid_row
    return grid


class Ship:
    """ This is a Ship Class. It is used to create individual ship objects. Each ship has coordinates it takes
    up on the game board, a starting coordinate for placement, a length, and an orientation! """

    def __init__(self, coord, length, orientation):
        self._coord = coord
        self._length = length
        self._orientation = orientation
        self._coord_list = []

    def __repr__(self):
        """ Repr method to output a cleaner object descriptions when looking at Ship objects stored
        in a player's ship list."""
        orient = "horizontal"
        if self._orientation == "V":
            orient = "vertical"
        return f'Ship at {self._coord}: {orient} placement. {self._length} spaces'

    def ship_coords(self):
        """ This is a Ship class method that moves the ship's coordinates into it's coordinate list based
        off the ship's starting coordinate, length, and orientation."""
        row_letter = self._coord[:1]
        column_number = int(self._coord[1:])
        if self._orientation == "H":
            for i in range(self._length):
                row_string = f"{row_letter}{(column_number+i)}"
                self._coord_list.append(row_string)
        elif self._orientation == "V":
            char_num = ord(row_letter)
            for k in range(self._length):
                col_string = f"{chr(char_num+k)}{column_number}"
                self._coord_list.append(col_string)

    def ship_hit(self, coord):
        """ This is a Ship Class method that removes a coordinate from a ship's coordinate list when
        it gets hit by a torpedo. It accepts a single parameter - the coordinate that needs to be 
        removed from the list. """
        for coordinate in self._coord_list:
            if coordinate == coord:
                self._coord_list.remove(coord)

    def get_coord_list(self):
        """ Get method to return the Ship's coordinate list. """
        return self._coord_list


class ShipGame:
    def __init__(self):
        self._player = "first"
        self._grid_size = 10
        self._player_1_grid = create_grid(self._grid_size)
        self._player_1_ships = []
        self._player_2_grid = create_grid(self._grid_size)
        self._player_2_ships = []
        self._current_state = "UNFINISHED"

    def display_grid(self, player):
        """ This method displays a visual game board for the user to see. It takes a single parameter, 
        player, and prints that player's board to the console."""
        if player == "first":
            keys = list(self._player_1_grid.keys())
            values = list(self._player_1_grid.values())
            string_header = [f"{item}" for item in range(1, self._grid_size+1)]
            print("    " + "  ".join(string_header))
            for i in range(self._grid_size):
                print(f"{keys[i]}: {''.join(values[i])}")
        elif player == "second":
            keys = list(self._player_2_grid.keys())
            values = list(self._player_2_grid.values())
            string_header = [f"{item}" for item in range(1, self._grid_size+1)]
            print("    " + "  ".join(string_header))
            for i in range(self._grid_size):
                print(f"{keys[i]}: {''.join(values[i])}")

    def place_ship(self, player, length, coords, orientation):
        """ This allows players to place ships. It accepts 4 parameters:
        the player who wants to place the ship, the length of the ship tp be placed, the starting
        coordinate of the ship placement, and the orientation of the ship. It first verifies that the
        placement is legal. If it is not, it will return False. Otherwise, it updates the visual game
        board, creates a Ship class, and adds the ship object to the player's ship list."""
        coords = coords.upper()
        starting_index = int(coords[1:])
        starting_row = ord(coords[:1])
        orientation = orientation.upper()
        max_height = ord("A") + self._grid_size
        if length < 2:
            return False

        if player == "first" and orientation == "H":
            potential_coords = [
                f"{chr(starting_row)}{(starting_index+i)}" for i in range(length)]
            # Check to make sure any of the potential coordinates are not already taken
            for coord in potential_coords:
                for each_ship in self._player_1_ships:
                    if coord in each_ship.get_coord_list():
                        return False
            # if the starting coord plus length exceed the board size
            if starting_index + length > self._grid_size + 1:
                return False
            else:
                # add a ship object to their list
                self._player_1_ships.append(Ship(coords, length, orientation))
                # and add the coords to the ship class list
                self._player_1_ships[-1].ship_coords()
                for i in range(length):
                    # Update the visual board
                    self._player_1_grid[coords[:1]][(
                        starting_index + i)-1] = "|X|"
                return True
        if player == "first" and orientation == "V":         # Do it again for the column orientation
            potential_coords = [
                f"{chr(starting_row+i)}{starting_index}" for i in range(length)]
            # Check to make sure any of the potential coordinates are not already taken
            for coord in potential_coords:
                for each_ship in self._player_1_ships:
                    if coord in each_ship.get_coord_list():
                        return False
            if starting_row + length > max_height:
                return False
            else:
                self._player_1_ships.append(Ship(coords, length, orientation))
                self._player_1_ships[-1].ship_coords()
                for k in range(length):
                    self._player_1_grid[chr(
                        starting_row + k)][(starting_index)-1] = "|X|"
                return True

        if player == "second" and orientation == "H":
            potential_coords = [
                f"{chr(starting_row)}{starting_index+i}" for i in range(length)]
            # Check to make sure any of the potential coordinates are not already taken
            for coord in potential_coords:
                for each_ship in self._player_2_ships:
                    if coord in each_ship.get_coord_list():
                        return False
            if starting_index + length > self._grid_size + 1:  # if starting coord plus length exceeds the board size
                return False
            else:
                self._player_2_ships.append(Ship(coords, length, orientation))
                self._player_2_ships[-1].ship_coords()
                for i in range(length):
                    # Update the visual board
                    self._player_2_grid[coords[:1]][(
                        starting_index + i)-1] = "|X|"
                return True
        if player == "second" and orientation == "V":
            potential_coords = [
                f"{chr(starting_row+i)}{starting_index}" for i in range(length)]
            # Check to make sure any of the potential coordinates are not already taken
            for coord in potential_coords:
                for each_ship in self._player_2_ships:
                    if coord in each_ship.get_coord_list():
                        return False
            if starting_row + length > max_height:
                return False
            else:
                self._player_2_ships.append(Ship(coords, length, orientation))
                self._player_2_ships[-1].ship_coords()
                for k in range(length):
                    self._player_2_grid[chr(
                        starting_row + k)][(starting_index)-1] = "|X|"
                return True

    def player_switch(self):
        """ A quick method to help with the switching of player turns. To be used in the 
        fire_torpedo method"""
        if self._player == "first":
            self._player = "second"
        else:
            self._player = "first"

    def fire_torpedo(self, player, coord):
        """ This is a class method that fires torpedoes at the other player's board in order to destroy their 
        ships, killing all crew members, solely for the player's own amusement. Pretty sick if you ask me. It 
        accepts two parameters - the player firing the shot, and the coordinate on the opposing player's board
        they wish to shoot at. If it is not that player's turn or the game has already been won by a player, it
        will return False. Otherwise, if the shot is a miss, it will simply change to the other player's turn. If
        it is a hit, it will update the visual game board, remove that coordinate from the Ship object's coordinate
        list, update the player's Ship list if the shot sunk a ship, check to see if a player won the game, and FINALLY
        will change the change the player turn. """
        if player != self._player or self._current_state != "UNFINISHED":
            return
        coord = coord.upper()
        column = int(coord[1:])-1
        row = coord[:1]
        if player == "first":
            for ships in self._player_2_ships:
                if coord in ships.get_coord_list():
                    # remove the coordinate from the ship node
                    ships.ship_hit(coord)
                    # if all of the ship's nodes have been hit
                    if len(ships.get_coord_list()) == 0:
                        # remove it from the player's ship list
                        self._player_2_ships.remove(ships)
                    # if the player's ship list is empty, they lose
                    if len(self._player_2_ships) == 0:
                        self._current_state = "FIRST_WON"
                    # update the visual game board
                    self._player_2_grid[row][column] = "|*|"
                    self.player_switch()                    # switch player turn
                    return True
            self._player_2_grid[row][column] = "|o|"
            self.player_switch()
            return False

        if player == "second":
            for ships in self._player_1_ships:
                if coord in ships.get_coord_list():
                    # remove the coordinate from the ship node
                    ships.ship_hit(coord)
                    # if all of the ship's nodes have been hit
                    if len(ships.get_coord_list()) == 0:
                        # remove it from the player's ship list
                        self._player_1_ships.remove(ships)
                    # if the player's ship list is empty, they lose
                    if len(self._player_1_ships) == 0:
                        self._current_state = "SECOND_WON"
                    # update the visual game board
                    self._player_1_grid[row][column] = "|*|"
                    self.player_switch()                    # switch player turn
                    return True
            self._player_1_grid[row][column] = "|o|"
            self.player_switch()
            return False

    def get_num_ships_remaining(self, player):
        """ This is a method that returns the number of remaining ships a player has
        on their board. It accepts one parameter - the player whose board needs a good checkin'.
        It will return the length of that player's ship list, which is the number of Ship objects
        they have on their board."""
        if player == "first":
            return len(self._player_1_ships)
        elif player == "second":
            return len(self._player_2_ships)
        else:
            raise WrongPlayer

    def get_current_state(self):
        return self._current_state

    def get_player(self):
        return self._player


def ship_place(game, player, ship_list):
    if player == 'first':
        print('Player 1, place your ships!')
    else:
        print('Go ahead, player 2, place your ships!')
    for ship in ship_list:
        coordinate = input(
            f"Place your {ship} at a coordinate between 'A1' and 'J10': ")
        placement = input(
            "Choose 'H' for horizontal or 'V' for vertical placement: ")
        legal_placement = game.place_ship(
            player, ship_list[ship], coordinate, placement)
        while legal_placement == False:
            print('That space is taken! Here is your current board:')
            game.display_grid('first')
            print(f"Try placing your {ship} again")
            coordinate = input(
                f"Place your {ship} at a coordinate between 'A1' and 'J10': ")
            placement = input(
                "Choose 'H' for horizontal or 'V' for vertical placement: ")
            legal_placement = game.place_ship(
                player, ship_list[ship], coordinate, placement)
        game.display_grid(player)


def shots_fired(game, ship_list):
    player = game.get_player()
    if player == 'first':
        player_str = 'Player 1'
    else:
        player_str = 'Player 2'
    p1_ships = game.get_num_ships_remaining('first')
    p2_ships = game.get_num_ships_remaining('second')
    print(f'\n Let\'s battle! {player_str}, you are up!')
    shot = input(
        'Where do you want to fire? Choose a coordinate between A1 and J10!')
    attempt = game.fire_torpedo(player, shot)
    print('HIT!') if attempt else print('MISS!')
    if player == 'first':
        p2_new = game.get_num_ships_remaining('second')
        if p2_new < p2_ships:
            print('SHIP SUNK!')
    if player == 'second':
        p1_new = game.get_num_ships_remaining('second')
        if p1_new < p1_ships:
            print('SHIP SUNK!')


def main():
    game = ShipGame()
    ship_list = {
        'patrol boat': 2
        # 'submarine': 3,
        # 'destroyer': 4,
        # 'carrier': 5
    }
    player = 'first'
    ship_place(game, player, ship_list)
    print('Great job, player 1! Player 2, you\'re up! I hope you didn\'t peek!')
    player = "second"
    ship_place(game, player, ship_list)

    game_state = game.get_current_state()
    while game_state == 'UNFINISHED':
        shots_fired(game, ship_list)
        game_state = game.get_current_state()

    print(game.get_current_state())


if __name__ == '__main__':
    main()
