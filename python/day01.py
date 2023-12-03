
import sys

substrings = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum1 = 0
sum2 = 0

for line in sys.stdin:
    if not line:
        continue
    digits = "".join(filter(lambda c: c.isdigit(), line))
    sum1 += (10 * int(digits[0])) + int(digits[-1])

    iMin = len(line)
    left = 0
    for value, s in enumerate(substrings):
        i = line.find(s, 0, iMin + 1)
        if i < 0:
            continue
        iMin = i
        left = value if value < 10 else value - 9
    iMax = 0
    right = 0
    for value, s in enumerate(substrings):
        i = line.rfind(s, iMax)
        if i < 0:
            continue
        iMax = i
        right = value if value < 10 else value - 9
    sum2 += (10 * left) + right

 
print(sum1)
print(sum2)
