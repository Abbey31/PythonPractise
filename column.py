import random
numbers = [random.randrange(1, 6) for i in range(50)]
from collections import Counter
counter = Counter(numbers)
for value, count in sorted(counter.items()):
    print(f'{value:<4}{count}')