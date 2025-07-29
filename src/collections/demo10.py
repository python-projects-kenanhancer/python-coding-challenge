def countdown(n: int):
    while n > 0:
        yield n
        n -= 1


for number in countdown(5):
    print(number)


print(list(countdown(5)))


class Countdown:
    def __init__(self, start: int):
        self.start = start

    def __iter__(self):
        return CountdownIterator(self.start)


class CountdownIterator:
    def __init__(self, current):
        self.current = current

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

    def __iter__(self):
        return self


for i in Countdown(5):
    print(i)

print("Countdown finished.")
