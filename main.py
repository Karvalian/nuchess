#!/usr/bin/python3
import chess
import numpy as np

class Main(object):
    def __init__(self, board=None):
        if board == None:
            self.board = chess.Board()
        else:
            self.board = board
    def serialize(self):
        pp = self.board.shredder_fen()
        return pp

    def edges(self):
        return list(self.board.legal_moves)

    def value(self):
        return 1

if __name__ == "__main__":
    m = Main()
    print(m.edges())
