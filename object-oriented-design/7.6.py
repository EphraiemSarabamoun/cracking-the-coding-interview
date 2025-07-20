class Jigsaw:
    def __init__(self, pieces):
        self.pieces = pieces

class Piece:
    def __init__(self, id):
        self.id = id
        self.connected_pieces = []
        