class Countdown:
    def __init__(self, start: int):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        value = self.start
        self.start -= 1
        return value


for i in Countdown(5):
    print(i)
