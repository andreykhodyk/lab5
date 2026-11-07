numbers = list(map(int, input().split()))

while len(numbers) > 0:
    index = 2 % len(numbers)
    numbers.pop(index)
    print(numbers)