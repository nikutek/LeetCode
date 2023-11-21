class ChessBoard:
    def __init__(self, n):
        self.boardsize = n
        self.board = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append("_")
            self.board.append(row)

    def placeQueen(self, x, y):
        if not((0 <= x <= self.boardsize-1) and (0 <= y <= self.boardsize-1)):
            print("Niepoprawne pole")
            return
        if self.board[y][x] =="Q" or self.board[y][x] =="x":
            print("Nie można tu postawić hetmana")
            return

        else:
            self.board[y][x] = "Q"

            # wykluczenie pól pod biciem w poziomie
            for i in range(self.boardsize):
                if self.board[i][x] != "Q": self.board[i][x] = 'x'

            # wykluczenie pól pod biciem w pionie
            for i in range(self.boardsize):
                if self.board[y][i] !="Q": self.board[y][i] = "x"

            # wykluczenie pól pod biciem na skos
            offset = 1;
            for i in range(x+1, self.boardsize):
                if y+offset < self.boardsize: #prawo/dol
                    self.board[y+offset][i] = "x"
                if y-offset >=0: #prawo/gora
                    self.board[y-offset][i] = "x"
                offset+=1

            offset = 1
            for i in range(x-1, -1, -1):
                if y+offset < self.boardsize:
                    self.board[y+offset][i] = "x"
                if y-offset >= 0:
                    self.board[y-offset][i] = "x"
                offset+=1


    def getFirtAvailableSquare(self):
        for  y, i in enumerate(self.board):
            for  x, j in enumerate(i):
                if j != "x" and j!="Q": return x,y
        return None

    def printBoard(self):
        for i in self.board:
            print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    zad = ChessBoard(8)
    flag = True
    while flag:
        try:
            x, y = zad.getFirtAvailableSquare()
        except:
            flag = False
            break

        zad.placeQueen(x, y)
        print(x, y)
        zad.printBoard()
        print("------------------------------------------")
    zad.printBoard()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
