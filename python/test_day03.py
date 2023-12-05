import day03

example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()

def test_part1():
    assert day03.part1(example) == 4361

def test_part2():
    assert day03.part2(example) == 467835
