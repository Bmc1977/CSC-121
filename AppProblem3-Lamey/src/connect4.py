from result import Result
from grid import Grid


INTRO = """
Welcome to Connect-4! This is a game for two players, Red and Blue. 
Red goes first. To play, just pick which column you want to drop a 
stone in (starting with the leftmost column being 1, the next column 
being 2, etc). Here's the state of the board at the start of the game:
"""


def main():
    print(INTRO)
    board = Grid()  # this is your Grid class
    print(board)  # you'll need a __str__ method
    player = "Red"

    # These two lines are a "priming read" so that the loop condition makes sense
    # right from the start. If this were any more complex, I'd probably wrap these
    # in a little function to avoid the duplicate code.

    result = None

    target = int(input("What's your play?"))
    result = board.drop(player, target)

    while result != Result.WIN and result != Result.DRAW:
        if result == Result.ILLEGAL:
            print(f"Sorry, {target} is not a legal column number. ")
        else:
            if player == "Red":
                player = "Blue"
            else:
                player = "Red"
            print("Nice play. Here's the board: ")
            print(board)
            print(f"{player}'s turn now!")

        # these either replay an illegal move or let the next player play,
        # depending on what happened in the if statement above

        target = int(input("What's your play? "))
        result = board.drop(player, target)

    print(board)
    if result == Result.DRAW:
        print("A hard-fought game! It ends in a draw.")
    else:
        print(f"Nicely played, {player}! What a champ.")
    print("Thanks for playing!")

if __name__ == '__main__':
   main()