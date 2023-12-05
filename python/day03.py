import sys

def part1(input):
    parsed = []
    lineLen = -1
    for lineNum, line in enumerate(input):
        line = line.strip()
        if lineLen > 0:
            if len(line) != lineLen:
                exit(1)
        else:
            lineLen = len(line)
        inNumber = False
        for pos, c in enumerate(line):
            b = pos - 1 if pos > 0 else 0
            neighbors = set(line[pos + 1:pos + 2])
            if pos > 0:
                neighbors.update(line[pos - 1])
            if lineNum > 0:
                neighbors.update(set(input[lineNum - 1][b:pos + 2]))
            if lineNum < len(input) - 1:
                neighbors.update(set(input[lineNum + 1][b:pos + 2]))
            if c.isdigit():
                if not inNumber:
                    inNumber = True
                    parsed.append((int(c), neighbors))
                else:
                    parsed[-1] = ((10 * parsed[-1][0]) + int(c), parsed[-1][1].union(neighbors))
            else:
                inNumber = False
    sum = 0
    for enginePart in parsed:
        symbols = [x for x in enginePart[1] if not (x.isdigit() or x.isspace() or x == ".")]
        hasAdjecentSymbols = len(symbols) > 0
        if hasAdjecentSymbols:
            sum += enginePart[0]
    return sum

def part2(input):
    parts = []
    lineLen = len(input[0].strip())
    for line in input:
        line = line.strip()
        if len(line) != lineLen:
            exit(0)
    def is_symbol(c):
      if c.isdigit():
          return False
      if c.isspace():
          return False
      if c == ".":
          return False
      return True
    def get_adjecent_numbers(l, n):
        def get_numbers_from_line(l, n):
            if l < 0 or l >= len(input):
                return []
            if n < 0 or n >= lineLen:
                return []
            def get_number_at_pos(l, n):
                if n < 0 or n >= lineLen:
                    return None
                if not input[l][n].isdigit():
                    return None
                ret = 0
                while True:
                    if n < 1:
                        break
                    if not input[l][n-1].isdigit():
                        break
                    n -= 1
                while True:
                    if n == lineLen:
                        return ret
                    if input[l][n].isdigit():
                        ret = (10 * ret) + int(input[l][n])
                        n += 1
                    else:
                        return ret
            if input[l][n].isdigit():
                return [get_number_at_pos(l,n)]
            else:
                ret = [get_number_at_pos(l, n - 1), get_number_at_pos(l, n + 1)]
                ret = [n for n in ret if n != None]
                return ret
        ret = get_numbers_from_line(l - 1, n) + get_numbers_from_line(l, n) + get_numbers_from_line(l + 1, n)
        return ret

    for lineNum in range(0, len(input)):
        for pos in range(0, lineLen):
            c = input[lineNum][pos]
            if not is_symbol(c):
                continue
            nums = get_adjecent_numbers(lineNum, pos)
            parts.append((c, nums))

    gearRatioSum = 0
    for enginePart in parts:
        if enginePart[0] != "*":
            continue
        if len(enginePart[1]) != 2:
            continue
        gearRatio = enginePart[1][0] * enginePart[1][1]
        gearRatioSum += gearRatio
    return gearRatioSum



if __name__ == '__main__':
    puzzle = [line for line in sys.stdin]
    print(part1(puzzle))
    print(part2(puzzle))
