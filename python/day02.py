import sys

def parse(text):
    ret = {}
    for line in text:
        if not line:
            continue
        game_id, hands = line.split(": ")
        id = int(game_id.split(" ")[1])
        ret[id] = []
        for hand in hands.split("; "):
            ret[id].append({})
            for parts in hand.split(", "):
                numStr, color = parts.split(" ")
                ret[id][-1][color.strip()] = int(numStr)
    return ret

def part1(games):
    def is_valid_game(hands, available):
        for hand in hands:
            for color, quantity in available:
                defaultQuantity = 0
                if hand.get(color, defaultQuantity) > quantity:
                    return False
        return True
    available = [
        ('red', 12),
        ('green', 13),
        ('blue', 14),
    ]
    idSum = 0
    for id, hands in games.items():
        idSum += id if is_valid_game(hands, available) else 0
    return idSum

def part2(games):
    def calculate_power(hands):
        max_cubes = {}
        for hand in hands:
            for color, quantity in hand.items():
                defaultQuantity = 0
                prev = max_cubes.get(color, defaultQuantity)
                max_cubes[color] = max(prev, quantity)
        power = 1
        for quantity in max_cubes.values():
            power *= quantity
        return power
    powerSum = 0
    for hands in games.values():
        powerSum += calculate_power(hands)
    return powerSum

if __name__ == "__main__":
    lines = []
    for line in sys.stdin:
        lines.append(line)
    games = parse(lines)
    print(part1(games))
    print(part2(games))
