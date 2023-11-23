class ChessBoard:
    def __init__(self, n):
        self.boardsize = n
        self.board = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append('_')
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




    def getNearestAvailableSquares(self, x=0, y=0):
        upDistance = 0
        downDistance = 0
        leftDistance = 0
        rightDistance = 0

        squaresAvailable = []
        while len(squaresAvailable)==0:
            if upDistance== 8 or downDistance == 8 or leftDistance == 8 or rightDistance == 8: return []
            for i in range(upDistance+1):
                for square in self.board[y-i][x-leftDistance:x+rightDistance+1]:
                    if square !="x" and square!="Q": squaresAvailable.append(square)
            for i in range(1,downDistance+1):
                for square in self.board[y + i][x-leftDistance:x+rightDistance+1]:
                    if square !="x" and square!="Q": squaresAvailable.append(square)


            if y-upDistance>0:upDistance+=1
            if y+downDistance < self.boardsize-1: downDistance += 1
            if x-leftDistance>0: leftDistance+=1
            if x+rightDistance < self.boardsize: rightDistance +=1
        return squaresAvailable


    # def findFirstSolution(self):
    #     flag = True
    #     while flag:
    #         self.placeQueen(0,0 )
    #         print(self.getNearestAvailableSquares(0,0))






    def printBoard(self):
        for i in self.board:
            print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    boardSize = 4;

    zad = ChessBoard(boardSize)
    usedColumns = []
    for y in range(zad.boardsize):
        row = zad.board[y]
        for x, square in enumerate(row):
            if x not in usedColumns and zad.board[y][x] != "x":
                zad.placeQueen(x, y)
                usedColumns.append(x)





        # for x in range(zad.boardsize):
        #     zad.placeQueen(x, row)

        zad.printBoard()
        print('-----------------------')



