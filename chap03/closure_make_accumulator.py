def make_accumulator():
    total = 0
    def accumulate(value):
        nonlocal total
        total += value
        return total
    return accumulate

acc = make_accumulator()

print(acc(10))
print(acc(5))