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
        self.is_finish = True
        for cup in self:
            if not cup.is_finish:
                self.is_finish = False


class TreeStep:
    step_log = []
    t = 0
    list_step = []

    def __init__(self, modal):
        self.modal = modal

    def recursive_play(self, current_step):
        i = 0
        # print("modal: ")
        # for cup in modal:
        #    print(cup, i, cup.is_full, cup.is_finish)
        #    i += 1
        self.t +=1
        # print(self.t)
        self.modal.move(current_step)
        step_list = self.modal.ability
        self.modal.check_finish()
        # print(step_list)
        for step in step_list:
            if self.modal.is_finish:
                break
            if step == (current_step[1], current_step[0]):
                # print("step except: ", step, "  Current: ", current_step)
                continue
            self.recursive_play(step)
        if self.modal.is_finish:
            self.step_log.insert(0, current_step)
        self.t -=1
        self.modal.redo(current_step)


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
