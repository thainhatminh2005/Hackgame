class Modal(list):
    ability = []
    finished = False

    def __init__(self, *modal):
        super(Modal, self).__init__(modal)
        self.length = len(self)
        self.get_move()

    def __eq__(self, other):
        def __eq__(self, other):
            if list(self) == list(other):
                return True
            else:
                return False

    def __ne__(self, other):
        if list(self) != list(other):
            return True
        else:
            return False

    def get_move(self):
        self.ability = []
        for x in range(0, self.length):
            for y in range(0, self.length):
                if self[x] is self[y] \
                        or self[y].is_full \
                        or self[x].first_color is None:
                    continue
                if self[x].first_color == self[y].first_color \
                        or self[y].first_color is None:
                    self.ability.append((x, y))

    def move(self, step):
        print("move: ", step)
        x = step[0]
        y = step[1]
        color = self[x].first_color
        self[x].pour()
        self[y].add(color)
        self.check_finish()
        self.get_move()

    def redo(self, step):
        new_step = (step[1], step[0])
        self.move(new_step)
        print("redo:", new_step)

    def check_finish(self):
        self.finished = True
        for cup in self:
            if not cup.finished:
                self.finished = False
a = Modal(
    Cup(1,2),
    Cup(1,4)
)