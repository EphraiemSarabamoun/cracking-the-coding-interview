class Jigsaw:
    def __init__(self, pieces):
        self.pieces = {piece.id: piece for piece in pieces}
        self.solved = False
    def fitsWith(self, piece1, piece2):
        return piece1.id in piece2.connected_pieces 
    def fitPieces(self):
        piece1_id = int(input("Enter first piece to fit from list: " + str(self.pieces.keys()) + "\n"))
        if piece1_id not in self.pieces:
            print("Piece not found")
            return
        piece2_id = int(input("Enter second piece to fit from list: " + str(self.pieces.keys()) + "\n"))
        if piece2_id not in self.pieces:
            print("Piece not found")
            return
        if self.fitsWith(self.pieces[piece1_id], self.pieces[piece2_id]):
            print("Pieces fit together triggered")
            if self.pieces[piece1_id].is_connected:
                self.pieces[piece2_id].is_connected = True 
            if self.pieces[piece2_id].is_connected:
                self.pieces[piece1_id].is_connected = True
            else:
                print("Pieces fit but are not connected to starting piece")
        else:
            print("Pieces do not fit together")
        print(piece.is_connected for piece in self.pieces.values())
        if all(piece.is_connected for piece in self.pieces.values()):
            self.solved = True
            print("Jigsaw solved")
            return

class Piece:
    def __init__(self, id, is_connected = False):
        self.id = id
        self.connected_pieces = []
        self.is_connected = is_connected


if __name__ == "__main__":
    piece0 = Piece(0, is_connected=True)
    piece1 = Piece(1)
    piece2 = Piece(2)
    piece0.connected_pieces = [1]   # Starting piece connects to 1
    piece1.connected_pieces = [0, 2]  # Piece 1 connects to 0 and 2
    piece2.connected_pieces = [1]
    jigsaw = Jigsaw([piece0, piece1, piece2])
    while not jigsaw.solved:
        jigsaw.fitPieces()