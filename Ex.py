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

    def give(self):
        self.pop(0)
        self.size -= 1
        self._check_state()

