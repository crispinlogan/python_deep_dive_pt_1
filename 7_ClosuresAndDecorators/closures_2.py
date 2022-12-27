####
# From 103 - Closure Applications - Part 1
####
# SHOW THE CLASS AVERAGER, NAIVE CLOSURE AVERAGE (~7.30M) AND GOOD CLOSURE THAT WORKS (NONLOCAL KEYWROD REQUIRED)
class Averager:
    def __init__(self) -> None:
        self.numbers = []

    # def add_number(self, number):
    #     self.numbers.append(number)
    #     return sum(self.numbers) / len(self.numbers)

    # don't need to use call at all, just might be easier!
    def __call__(self, number):
        self.numbers.append(number)
        return sum(self.numbers) / len(self.numbers)

a = Averager()
a(2)
a(5)
a(1)

# but we can also write as a closure
def averager():
    numbers = []
    def inner(number):
        numbers.append(number)
        return sum(numbers) / len(numbers)
    return inner

b = averager()
b(2)
b(5)
b(1)


# # can also speed up doing the following
# def averager():
#     total = 0
#     cnt = 0
#     def inner(number):
#         total += number
#         cnt += 1
#         return total / cnt
#     return inner

# c = averager()
# c(2)
# c(5)
# c(1)

# you'll see the above fails as we need tohe nonlocal keyword,
# otherwise the total and cnt in the inner fn are local
def averager():
    total = 0
    cnt = 0
    def inner(number):
        nonlocal total
        nonlocal cnt
        total += number
        cnt += 1
        return total / cnt
    return inner

d = averager()
d(2)
d(5)
d(1)

# ALSO SHOWS A QUICK EXAMPLE OF CLASS VS CLOSURE FOR A TIMER
from time import perf_counter
class Timer:
    def __init__(self) -> None:
        self.start = perf_counter()

    def __call__(self) -> float:
        return perf_counter() - self.start


t = Timer()
t()
t()
t()

# or as a closure
def timer():
    start = perf_counter()
    def inner():
        return perf_counter() - start
    return inner

t2 = Timer()
t2()
t2()
t2()