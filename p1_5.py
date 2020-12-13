class MoneyBox:
    def __init__(self, capacity):
        self.sum = 0
        self.capacity = capacity

    def can_add(self, v):
        if self.sum + v <= self.capacity:
            return True
        return False

    def add(self, v):
        self.sum += v
        return self.sum


class Buffer:
    def __init__(self):
        self.buf = []

    def add(self, *a):
        self.buf += a
        while len(self.buf) >= 5:
            sum = 0
            for i in range(5):
                sum += self.buf[i]
            print(sum)
            if len(self.buf) > 5:
                self.buf = self.buf[5:]
            else:
                self.buf = []

    def get_current_part(self):
        return self.buf