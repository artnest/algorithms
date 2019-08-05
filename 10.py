class Step:
    def __init__(self, x=0, y=0, direction=None):
        self.x = x
        self.y = y
        self.direction = direction


class Solver:
    def __init__(self):
        self.stack = []
        self.x = 0
        self.y = 0
        self.direction = None

    def solve(self):
        self.stack.append(Step(solved_labyrinth[0].index(0), 0, None))  # TODO change init direction to 'left'
        solved_labyrinth[0][solved_labyrinth[0].index(0)] = 1
        self.step_down()

        for i in range(1, n):
            # self.x = row.index(0)
            # self.stack.append(Step(self.x, self.y, None))  # TODO change init direction to 'left'
            # solved_labyrinth[0][x] = 1
            # row[self.x] = 1

            self.direction = self.stack.pop().direction
            # if not direction:
            #     self.step_down()
            # elif direction == "down":
            #     self.step_left()
            if not self.direction:
                self.step_down()
            elif self.direction == "down":
                if self.x - 1 > 0 and self.x - 1 == 0:
                    self.step_left()
                elif self.y + 1 < n and self.y + 1 == 0:
                    self.step_down()
                elif self.x + 1 < m and self.x + 1 == 0:
                    self.step_right()
                elif self.y - 1 > 0 and self.y - 1 == 0:
                    self.step_up()
            elif self.direction == "left":
                if self.x - 1 > 0 and self.x - 1 == 0:
                    pass  # ...

            self.stack.append(Step(self.x, self.y, self.direction))
            solved_labyrinth[self.y][self.x] = 1

    def step_down(self):
        self.y += 1
        self.direction = "down"

    def step_left(self):
        self.x -= 1
        self.direction = "left"

    def step_right(self):
        self.x += 1
        self.direction = "right"

    def step_up(self):
        self.y -= 1
        self.direction = "up"


if __name__ == '__main__':
    with open("in.txt") as fin:
        n, m = fin.readline().split()
        n = int(n)
        m = int(m)

        labyrinth = [[0] * m for i in range(n)]
        for i, line in enumerate(fin.readlines()):
            for j, wall in enumerate(line):
                if wall == "1":
                    labyrinth[i][j] = 1

        # TODO change to parsing on reading

        solved_labyrinth = labyrinth.copy()
        solver = Solver()
        solver.solve()
