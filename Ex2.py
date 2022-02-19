from enum import Enum


class State(Enum):

    full = 1
    null = 2
    middle = 3


class Cup(list):

    def __init__(self, *color_list):
        super(Cup, self).__init__(color_list)
        self.size = len(self)
        self._check_state()

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

    def _check_state(self):
        if self.size == 0:
            self.state = State.null
        elif self.size == 4:
            self.state = State.full
        else: self.state = State.middle

    def _check_finish(self):
        if self.state == State.null:
            self.finished = True
        elif self.state == State.full and self.is_one_color():
            self.finished = True

    def is_one_color(self):
        color = self[0]
        for check_color in self:
            if check_color != color:
                return False
        return True

    def accept_give(self):
        if self.state == State.null:
            return False
        elif self.is_one_color():
            return False
        else:
            return True

    def accept_take(self, color):
        if self.state == State.full:
            return False
        elif self[0] != color:
            return False
        else:
            return True

    def take(self, color):
        self.insert(0, color)
        self.size += 1
        self._check_state()
        self._check_finish()

    def give(self):
        self.pop(0)
        self.size -= 1
        self._check_state()

    def copy(self):
        cup = Cup()
        for color in self:
            cup.append(color)
        return cup


class Modal(list):
    ability = []
    finished = False

    def __init__(self, *modal):
        super(Modal, self).__init__(modal)
        self.length = len(self)
        # self.get_move()

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
                accept = self[x].accept_give() and self[y].accept_take(self[x][0])
                if accept:
                    self.ability.append((x, y))

    def move(self, step):
        # print("move: ", step)
        x = step[0]
        y = step[1]
        self[x].give()
        self[y].take(self[x][0])
        self._check_finish()
        self.get_move()

    def copy(self):
        modal = Modal()
        for cup in self:
            modal.append(cup.copy())
        return modal

    def _check_finish(self):
        self.finished = True
        for cup in self:
            if not cup.finished:
                self.finished = False
a = Modal(
    Cup(1,2),
    Cup(1,4)
)
b = a.copy()

print(a, b, a is b, a == b)