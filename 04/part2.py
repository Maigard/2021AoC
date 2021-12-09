class Board(object):
    def __init__(self, numbers):
        self.numbers = numbers
        self.marked = [[False for j in range(5)] for i in range(5)]
        self.lastDrawn = None

    def mark(self, number):
        for (y, row) in enumerate(self.numbers):
            try:
                x = row.index(number)
                self.marked[y][x] = True
                break
            except ValueError:
                pass
        else:
            return
        self.marked[y][x] = True
        self.lastDrawn = number

    def check_won(self):
        for row in range(5):
            for col in range(5):
                if not self.marked[row][col]:
                    break
            else:
                return True

        for col in range(5):
            for row in range(5):
                if not self.marked[row][col]:
                    break
            else:
                return True
        return False

    def score(self):
        sum = 0
        for row in range(5):
            for col in range(5):
                if not self.marked[row][col]:
                    sum += int(self.numbers[row][col])
        return sum * int(self.lastDrawn)

    def __repr__(self):
        ret = ""
        for row in range(5):
            for col in range(5):
                if self.marked[row][col]:
                    ret += "*"
                ret += f"{self.numbers[row][col]}\t"
            ret += "\n"
        return ret

def parse_input(filename):
    inputs = open(filename, "r")
    draws = inputs.readline().strip().split(",")
    inputs.readline()
    boards = []
    numbers = []
    for line in  inputs.readlines():
        line = line.strip().split()
        if len(line) == 0:
            boards.append(Board(numbers))
            numbers = []
        else:
            numbers.append(line)
    boards.append(Board(numbers))
    return (draws, boards)

def main():
    (draws, boards) = parse_input("04/inputs.txt")
    for draw in draws:
        if len(boards) > 1:
            boardsLeft = []
            for board in boards:
                board.mark(draw)
                if not board.check_won():
                    boardsLeft.append(board)
            boards = boardsLeft
        else:
            boards[0].mark(draw)
            if boards[0].check_won():
                print(boards[0].score())
                break
main()