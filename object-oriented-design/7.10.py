import random
class MineSweeper:
    def __init__(self):
        self.board = Board()
        self.game_over = False
    def play(self):
        while not self.game_over:
            response = input("Enter row and column as row,col. Rows are 0-3, columns are 0-3 \n")
            row,col = response.split(",")
            row = int(row)
            col = int(col)
            if row < 0 or row > 3 or col < 0 or col > 3 or self.board.board[row][col].is_revealed:
                print("Space is occupied or out of bounds or already revealed")
                continue
            self.board.board[row][col].is_revealed = True
            if self.board.board[row][col].is_mine:
                print("Game Over, YOU LOSE")
                self.game_over = True
                return
            else:
                self.board.board[row][col].is_revealed = True
                self.print_board()

            self.game_over = self.check_for_game_over()
        self.print_board()
        print("Game Over, YOU WIN")
    def print_board(self):
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[0])):
                if not self.board.board[i][j].is_revealed:
                    print("X",end=" ")
                else:
                    if self.board.board[i][j].is_mine:
                        print("*",end=" ")
                    else:
                        count = 0
                        for neighbor in self.board.board[i][j].neighbors:
                            if neighbor.is_mine:
                                count += 1
                        print(str(count),end=" ")
            print()
    def check_for_game_over(self):
        for row in self.board.board:
            for col in row:
                if col.is_mine or col.is_revealed:
                    continue
                else:
                    return False
        return True

class Board:
    def __init__(self):
        self.board = [[Position(i,j) for j in range(4)] for i in range(4)]
        self.initialize_neighbors()
    def initialize_neighbors(self):
        for i in range(4):
            for j in range(4):
                if i > 0:
                    self.board[i][j].neighbors.append(self.board[i-1][j])
                if i < 3:
                    self.board[i][j].neighbors.append(self.board[i+1][j])
                if j > 0:
                    self.board[i][j].neighbors.append(self.board[i][j-1])
                if j < 3:
                    self.board[i][j].neighbors.append(self.board[i][j+1])
                if i > 0 and j > 0:
                    self.board[i][j].neighbors.append(self.board[i-1][j-1])
                if i > 0 and j < 3:
                    self.board[i][j].neighbors.append(self.board[i-1][j+1])
                if i < 3 and j > 0:
                    self.board[i][j].neighbors.append(self.board[i+1][j-1])
                if i < 3 and j < 3:
                    self.board[i][j].neighbors.append(self.board[i+1][j+1])

class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.neighbors = []
        self.is_mine = random.random() < 0.1
        self.is_revealed = False

if __name__ == "__main__":
    minesweeper = MineSweeper()
    minesweeper.play()
