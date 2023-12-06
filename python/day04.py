import sys

def parse(input):
    cards = []
    for line in input:
        if not line:
            continue
        _, content = line.split(": ")
        def set_from_string(s):
            return set([int(s_) for s_ in s.split()])
        winners, ours = content.split(" | ")
        cards.append((set_from_string(winners), set_from_string(ours)))
    return cards

def part1(cards):
    sumPoints = 0
    for card in cards:
        matches = card[0].intersection(card[1])
        numMatches = len(matches)
        points = 0 if numMatches == 0 else 2**(numMatches - 1)
        sumPoints += points
    return sumPoints

def part2(cards):
    instances = [1] * len(cards)
    for i, card in enumerate(cards):
        matches = card[0].intersection(card[1])
        numMatches = len(matches)
        for j in range (i + 1, numMatches + i + 1):
            if j >= len(instances):
                break
            instances[j] += instances[i]
    return sum(instances)



if __name__ == '__main__':
    puzzle = [line for line in sys.stdin]
    cards = parse(puzzle)
    print(part1(cards))
    print(part2(cards))

