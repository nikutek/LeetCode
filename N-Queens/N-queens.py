from pathlib import Path

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

    def printBoard(self):
        for i in self.board:
            print(i)


def solveNQueens(n):
    def is_safe(board, row, col):
        # Sprawdź, czy można umieścić hetmana na danym polu
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                return False
            if col + (row - i) < len(board) and board[i][col + (row - i)] == 'Q':
                return False
        return True

    def place_queens(board, row):
        # Jeśli doszliśmy do końca planszy, dodaj obecne ułożenie do wyników
        if row == len(board):
            result.append([row[:] for row in board])
            return
        # Próbuj umieścić hetmana na każdym polu w bieżącym wierszu
        for col in range(len(board)):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                place_queens(board, row + 1)
                board[row][col] = '_'

    result = []
    chessboard = ChessBoard(n)
    place_queens(chessboard.board, 0)
    return result


if __name__ == '__main__':
    n = 20  # Możesz zmienić rozmiar szachownicy
    solutions = solveNQueens(n)

    isFileThere = Path("./N{}.txt".format(n)).is_file()
    if not isFileThere: f = open("./N{}.txt".format(n), "a")



    for solution in solutions:
        for row in solution:
            if not isFileThere: f.write(' '.join(row)+'\n')
            print(' '.join(row))

        if not isFileThere: f.write('-----------------------------------------------------------\n\n')
        print("\n")

    print('Ilość możliwych rozwiązań: ', len(solutions))