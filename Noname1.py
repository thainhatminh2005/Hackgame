class Cup(list):
    max = 4
    is_finish = False
    is_full = False

    def __init__(self, *color_list):
        super(Cup, self).__init__(color_list)
        self.size = len(self)
        if self.size in range(1, 5):
            self.first_color = self[0]
        else:
            self.first_color = None
        if self.size == 4:
            self.is_full = True

    def add(self, color):
        self.insert(0, color)
        self.size += 1
        self.first_color = color
        if self.size == 4:
            self.is_full = True

    def pour(self):
        self.pop(0)
        self.size -= 1
        if self.size in range(1, 5):
            self.first_color = self[0]
        else:
            self.first_color = None
        self.is_full = False

    def check_finish(self):
        if self.size == 0:
            self.is_finish = True
        else:
            cup = self[0]
            self.is_finish = True
            for cup_check in self:
                if cup != cup_check:
                    self.is_finish = False


class Modal(list):
    ability = []
    is_finish = False

    def __init__(self, *modal):
        super(Modal, self).__init__(modal)
        self.length = len(self)
        self.get_move()

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
        x = step[0]
        y = step[1]
        color = self[x].first_color
        self[x].pour()
        self[y].add(color)

    def check_finish(self):
        self.is_finish = True
        for cup in self:
            if not cup.is_finish:
                self.is_finish = False


class TreeStep:
    step_log = []

    def __init__(self, modal):
        self.modal = modal

    def recursive_play(self, step):
        self.modal.move(step)
        step_list = self.modal.get_move()
        self.modal.check_finish()
        for step in step_list:
            if self.modal.is_finish:
                break
            self.recursive_play(step)
        if self.modal.is_finish:
            self.step_log.insert(0, step)


if __name__ == '__main__':
    modal = Modal(
        Cup(1, 2, 3, 4),
        Cup(5, 6, 7, 8),
        Cup(7, 9, 1, 6),
        Cup(4, 9, 5, 10),
        Cup(7, 11, 10, 6),

        Cup(7, 2, 6, 4),
        Cup(3, 2, 8, 12),
        Cup(5, 12, 8, 9),
        Cup(11, 11, 8, 1),
        Cup(12, 10, 9, 3),

        Cup(2, 1, 4, 3),
        Cup(5, 10, 12, 11),
        Cup(),
        Cup()
    )

    tree = TreeStep(modal)
    tree.recursive_play((0, 0))
    tree.step_log.reverse()
    print(tree.modal.ability)
