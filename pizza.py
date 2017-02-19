# RCLH
import sys


def pizzaParser(fileName):
    # type str -> (int, int, int, int, int[][])
    with open(fileName) as f:
        content = f.readlines()
    r, c, l, h = content[0].split()
    matrix = []
    for i in range(int(r)):
        j = [x for x in content[i + 1][:-1]]
        matrix.append(j)
    return int(r), int(c), int(l), int(h), matrix


def solveRec(r, c, l, h, matrix):
    def count(oi, oj, ei, ej, what):
        counter = 0
        if (oi, oj, ei, ej, what) in count_mem:
            return count_mem[(oi, oj, ei, ej, what)]
        for i in range(oi, ei + 1):
            for j in range(oj, ej + 1):
                if matrix[i][j] == what:
                    counter = counter + 1
        count_mem[(oi, oj, ei, ej, what)] = counter
        return counter

    def numberOfCells(oi, oj, ei, ej):
        return (ei - oi + 1) * (ej - oj + 1)

    def isGoodSlice(oi, oj, ei, ej):
        number_of_t = count(oi, oj, ei, ej, 'T')
        number_of_m = count(oi, oj, ei, ej, 'M')
        return h >= numberOfCells(oi, oj, ei, ej) and l <= number_of_t and l <= number_of_m

    def rec(oi, oj, ei, ej, curr_sum, part):
        if ei == r or ej == c or oi == r or oj == c or h < numberOfCells(oi, oj, ei, ej):
            return curr_sum, part
        if (oi, oj, ei, ej, curr_sum) in mem:
            return mem[(oi, oj, ei, ej)][0], mem[(oi, oj, ei, ej)][1]
        new_sum = curr_sum
        if isGoodSlice(oi, oj, ei, ej):
            new_sum = new_sum + numberOfCells(oi, oj, ei, ej)

        # not ending this slice and continuing right
        s1, part1 = rec(oi, oj, ei, ej + 1, curr_sum, part)

        # not ending this slice and continuing down
        s2, part2 = rec(oi, oj, ei + 1, ej, curr_sum, part)
        s3 = 0
        s4 = 0
        if isGoodSlice(oi, oj, ei, ej):
            # taking this slice and going right
            s3, part3 = rec(oi, ej + 1, oi, ej + 1, new_sum, part + [(oi, oj, ei, ej)])
            # taking this slice and going down
            s4, part4 = rec(ei + 1, oj, ei + 1, oj, new_sum, part + [(oi, oj, ei, ej)])

        s5, part5 = rec(oi, oj + 1, oi, oj + 1, curr_sum, part)
        s6, part6 = rec(oi + 1, oj, oi + 1, oj, curr_sum, part)

        if s1 == max(s1, s2, s3, s4, s5, s6):
            sres, partres = s1, part1
        elif s2 == max(s1, s2, s3, s4, s5, s6):
            sres, partres = s2, part2
        elif s3 == max(s1, s2, s3, s4, s5, s6):
            sres, partres = s3, part3
        elif s4 == max(s1, s2, s3, s4, s5, s6):
            sres, partres = s4, part4
        elif s5 == max(s1, s2, s3, s4, s5, s6):
            sres, partres = s5, part5
        elif s6 == max(s1, s2, s3, s4, s5, s6):
            sres, partres = s6, part6

        mem[(oi, oj, ei, ej,)] = (sres, partres)

        return sres, partres

    mem = {}
    count_mem = {}
    res = rec(0, 0, 0, 0, 0, [])

    print res[0], res[1].__len__()
    for x in res[1]:
        print x[0], x[1], x[2], x[3]


def main():
    sys.setrecursionlimit(100500)
    r, c, l, h, matrix = pizzaParser('mid.txt')
    solveRec(r, c, l, h, matrix)


if __name__ == "__main__":
    main()
