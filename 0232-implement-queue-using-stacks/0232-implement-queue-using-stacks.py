class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if self.s2:
            return self.s2.pop()
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1] if self.s2 else None
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2[-1] if self.s2 else None

    def empty(self) -> bool:
        if self.s1 or self.s2:
            return False
        else:
            return True