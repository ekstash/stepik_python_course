class ExtendedStack(list):

    def sum(self):
        s = self.pop() + self.pop()
        self.append(s)

    def sub(self):
        s = self.pop() - self.pop()
        self.append(s)

    def mul(self):
        s = self.pop() * self.pop()
        self.append(s)

    def div(self):
        s = self.pop() // self.pop()
        self.append(s)
