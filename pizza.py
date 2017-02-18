# RCLH
import struct


def pizzaParser(fileName):
    # type str -> (int, int, int, int, int[][])
    with open(fileName) as f:
        content = f.readlines()
    r, c, l, h = content[0].split()
    matrix = []
    for i in range(int(r)):
        j = [x for x in content[i+1][:-1]]
        matrix.append(j)

    return r, c, l, h, matrix


def main():
    r, c, l, h, matrix = pizzaParser('input.txt')

if __name__ == "__main__":
    main()
