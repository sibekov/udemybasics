from random import randint

scores = {"computer": 0, "player1": 0}


class Board:
    """The main board class. Sets the board size,ships, the player1's name and
    the board type ie player1's board or computer's board.
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"
        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannnot add any more ships!")
        else:
            self.ships.append((x, y))
        if self.type == "player1":
            self.board[x][y] = "@"


def random_point(size):
    """
    Helper funtion to return a random integer between 0 and size
    """
    return randint(0, size - 1)


def valid_coordinates(x, y, board):
    """
    validate that the cordinates inputs that validates that not yet guessed.
    Validate that they are not outside our board.
    """
    listvar = [0, 1, 2, 3, 4]
    try:
        if x not in listvar:
            raise ValueError(f"Sorry you entered invalid input {x}!")
    except ValueError as e:
        print(f"Invalid guess: {e}, which is outside the range, please try any of the following numbers 0, 1, 2, 3, 4\n")
        return False
    try:
        if y not in listvar:
            raise ValueError(f"Sorry you entered invalid input {y}!")
    except ValueError as e:
        print(f"Invalid guess: {e}, which is outside the range, please try one of the following numbers 0, 1, 2, 3, 4\n")
        return False
    try:
        if (x, y) in board.guesses:
            raise ValueError(f"Sorry you have already guessed {(x,y)}!")
    except ValueError as e:
        print(f"Invalid guess:{e},please try again.\n")
        return False
    try:
        if type(x) is str:
            raise ValueError(f"Sorry you have supplied a string {x}!")
    except ValueError as e:
        print(f"Invalid guess: {e}, please try one of the following numbers 0, 1, 2, 3, 4\n")
        return False
    return True


def populate_board(board):
    """
    choose random row and random column and put a ship there.
    """
    x = random_point(5)
    y = random_point(5)
    board.add_ship(x, y)


def ismynumber(x):
    """
    check if input is a number
    """
    while True:
        try:
            x = int(input('Enter your number:'))
            return x
        except ValueError as x:
            print(f"Sorry you have supplied: {x} Which is not a Whole Number! please try one of the following numbers 0, 1, 2, 3, 4\n")


def make_guess(board):
    """
    if it is computer guess it choses random column and a rondom column.
    if it is a player guess then it promts the input.
    """
    x = None
    y = None
    if board.type == "computer":
        while True:
            x = ismynumber(x)
            y = ismynumber(y)
            if (valid_coordinates(x, y, board)):
                break
        return board.guess(x, y)
    else:
        x = random_point(5)
        y = random_point(5)
    board.guess(x, y)
    return board.guess(x, y)


def play_game(computer_board, player_board):
    """
    playing the game
    """
    for i in range(5):
        print(f"{player_board.name}'s Board")
        player_board.print()
        print(f"{computer_board.name}'s Board")
        computer_board.print()
        results = make_guess(computer_board)
        print(f"{player_board.name} guessed: {computer_board.guesses[-1]}")
        print(f"{player_board.name} {results}ed!!!")
        if results == "Hit":
            scores["player1"] = scores["player1"]+1
        answer = make_guess(player_board)
        print(f"{computer_board.name} guessed: {player_board.guesses[-1]}")
        print(f"{computer_board.name} {answer}ed!!!")
        if answer == "Hit":
            scores["computer"] = scores["computer"]+1
        print(18*"--")
        print("After this round, the scores are:")
        print(f"{player_board.name}: {scores['player1']}.{computer_board.name}: {scores['computer']}")
        print(18*"--")


def new_game():
    """
    Start a new game. Sets the board size and number of ships, rests the scores
    and initialises the boards.
    """
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player1"] = 0
    print("-"*35)
    print("Welcome to ALTIMATE BATTLESHIP!!!")
    print(f"Board Size: {size}, Number of ships:{num_ships}")
    print("Top left corner is row: 0, col:0 ")
    print("-"*35)
    player_name = input("Please enter your name: \n")
    print("-"*35)
    computer_board = Board(size, num_ships, "computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player1")
    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)
    play_game(computer_board, player_board)



new_game()
