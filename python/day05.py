import sys

def parse(input: list[str]):
    seeds: list[int] = []
    conversions: list[tuple[tuple[str, str], list[tuple[int, int, int]]]] = []
    for line in input:
        line = line.strip()
        if not line:
            continue
        if line.startswith("seeds: "):
            if len(seeds) != 0:
                exit(1)
            seeds = [int(x) for x in line.split()[1:]]
            continue
        if "-to-" in line:
            conversions.append((tuple(line.replace("-", " ").split()[0:3:2]), []))
            continue
        conversions[-1][1].append(tuple([int(x) for x in line.split()]))
    return (seeds, conversions)

def calc_lowest_location(seeds: list[int], maps: list[tuple[tuple[str, str], list[tuple[int, int, int]]]]):
    def perform_conversion(input, conversions):
        for entry in conversions[1]:
            dest = entry[0]
            source = entry[1]
            r = entry[2]
            if (input >= source) and (input < source + r):
                converted = input - source + dest
                return converted
        return input
    lowest = -1
    for seed in seeds:
        l = seed
        for map_ in maps:
            l = perform_conversion(l, map_)
        if lowest < 0 or l < lowest:
            lowest = l
    return lowest

def part1(parsed: tuple[list[int], list[tuple[tuple[str, str], list[tuple[int, int, int]]]]]):
    seeds, maps = parsed[0], parsed[1]
    return calc_lowest_location(seeds, maps)
        

# def part2(parsed: tuple[list[int], list[tuple[tuple[str, str], list[tuple[int, int, int]]]]]):
#     seeds, maps = parsed[0], parsed[1]
#     lowest = -1
#     for idx in range(0, len(seeds), 2):
#         seedList = list(range(seeds[idx], seeds[idx] + seeds[idx + 1]))
#         localLowest = calc_lowest_location(seedList, maps)
#         if lowest < 0 or localLowest < lowest:
#             lowest = localLowest
#     return lowest

if __name__ == '__main__':
    puzzle = [line for line in sys.stdin]
    parsed = parse(puzzle)
    print(part1(parsed))
    print(part2(parsed))

