from enum import IntEnum
class Othello:
    def __init__(self):
        self.board = Board()
        self.turn = Player.WHITE
        self.game_over = False
    def play_move(self):
        response = input("Enter row and column as row,col. Rows are 0-2, columns are 0-2 \n")
        row,col = response.split(",")
        print(row,col)
        row = int(row)
        col = int(col)
        print(row,col)
        if row < 0 or row > 2 or col < 0 or col > 2 or self.board.board[row][col] != 0:
            print("Space is occupied or out of bounds")
            return
        self.board.board[row][col] = self.turn.value
        self.flip()
        self.turn = Player.BLACK if self.turn == Player.WHITE else Player.WHITE
    def print_board(self):
        for row in self.board.board:
            print(row)
    def flip(self):
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[0])):
                if i == 0 or i == len(self.board.board)-1:
                    if self.board.board[i][j] != self.turn.value and (self.board.board[i][j-1] == self.turn.value and self.board.board[i][j+1] == self.turn.value):
                        self.board.board[i][j] = self.turn.value
                if j == 0 or j == len(self.board.board[0])-1:
                    if self.board.board[i][j] != self.turn.value and (self.board.board[i-1][j] == self.turn.value and self.board.board[i+1][j] == self.turn.value):
                        self.board.board[i][j] = self.turn.value
                else:
                    if self.board.board[i][j] != self.turn.value and ((self.board.board[i-1][j] == self.turn.value and self.board.board[i+1][j] == self.turn.value) or (self.board.board[i][j-1] == self.turn.value and self.board.board[i][j+1] == self.turn.value)):
                        self.board.board[i][j] = self.turn.value
    def check_for_game_over(self):
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[0])):
                if self.board.board[i][j] == 0:
                    return False
        return True

    def play_game(self):
        while self.game_over == False:
            self.print_board()
            self.play_move()
            self.game_over = self.check_for_game_over()
        self.print_board()
        print("Game Over")

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)] # make a three by three board

class Player(IntEnum):
    WHITE = 1
    EMPTY = 0
    BLACK = -1

if __name__ == "__main__":
    game = Othello()
    game.play_game()
