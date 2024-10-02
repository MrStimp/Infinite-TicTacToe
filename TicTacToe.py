
class TicTacToe:
    def __init__(self):
        self.player1Moves = []
        self.player2Moves = []
        self.totalMoves = []
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.crosses = True
        self.moveNumber = 1

    def displayBoard(self):
        for row in self.board:
            print(row)

    def inputMove(self):
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        return x - 1, y - 1

    def addMove(self, x, y):
        if self.board[x][y] != 0:
            print("Cell taken >")
            return False

        if self.crosses:
            self.board[x][y] = 1
            self.player1Moves.append((x, y))
        else:
            self.board[x][y] = 2
            self.player2Moves.append((x, y))
        self.removeMove()
        return True

    def checkWin(self):
        winning_combinations = [
            [(0, 0), (0, 1), (0, 2)],  # top row
            [(1, 0), (1, 1), (1, 2)],  # middle row
            [(2, 0), (2, 1), (2, 2)],  # bottom row
            [(0, 0), (1, 0), (2, 0)],  # left column
            [(0, 1), (1, 1), (2, 1)],  # middle column
            [(0, 2), (1, 2), (2, 2)],  # right column
            [(0, 0), (1, 1), (2, 2)],  # main diagonal
            [(0, 2), (1, 1), (2, 0)],  # anti-diagonal
        ]

        for combination in winning_combinations:
            values = [self.board[x][y] for x, y in combination]
            if values == [1, 1, 1]:
                # print("Player 1 (X) wins!")
                return True
            elif values == [2, 2, 2]:
                # print("Player 2 (O) wins!")
                return True
            
        # TODO need to change
        if all(cell != 0 for row in self.board for cell in row):
            return False

        return False

    def removeMove(self):
        if self.crosses and len(self.player1Moves) > 3:
            x, y = self.player1Moves.pop(0)
            self.board[x][y] = 0

        elif len(self.player2Moves) > 3:
            x, y = self.player2Moves.pop(0)
            self.board[x][y] = 0

    def gameLoop(self):
        gameOver = False

        while not gameOver:
            self.displayBoard()
            if self.crosses:
                print("Crosses go > ")
            else:
                print("Naughts go > ")

            x, y = self.inputMove()
            while not self.addMove(x, y):
                x, y = self.inputMove()

            if self.checkWin():
                break

            if self.crosses:
                self.crosses = False
            else:
                self.crosses = True

    def earlyMoves(self):
        if self.moveNumber < 3:
            if self.crosses:
                for i in range(4 - self.moveNumber):
                    self.player1Moves.pop()

                for move in self.player1Moves:
                    x,y = move
                    self.board[x][y] = 1

            else:
                for i in range(4 - self.moveNumber):
                    self.player2Moves.pop()

                for move in self.player2Moves:
                    x,y = move
                    self.board[x][y] = 2




def main():
    game = TicTacToe()

    game.gameLoop()



if __name__ == "__main__":
    main()
