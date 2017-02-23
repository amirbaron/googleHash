import sys


def video_parser(fileName):
    # list of V1,..,VN-1 - MB per video
    # list of Ld0,...Ldn-1 - milli
    # Mec Ei, Cj -> Latency between endpoint and cache or -1 in milli
    # Rev -> number of requests for this video from this endpoint. (int)
    with open(fileName) as f:
        content = f.readlines()
    V, E, R, C, X = content[0].split()
    V = int(V)
    E = int(E)
    R = int(R)
    C = int(C)
    X = int(X)
    content = content[1:]
    videos = content[0].split()
    content = content[1:]
    Ldarr = []
    Mec = [[-1 for c in range(C)] for e in range(E)]
    for i in range(E):
        Ld, K = content[0].split()
        Ld = int(Ld)
        K = int(K)
        Ldarr.append(Ld)
        content = content[1:]
        for j in range(K):
            c, Lc = content[0].split()
            c = int(c)
            Lc = int(Lc)
            Mec[i][c] = Lc
            content = content[1:]
    Rev = [[0 for v in range(V)] for i in range(E)]
    for i in range(R):
        Rv, Re, Rn = content[i].split()
        Rv = int(Rv)
        Re = int (Re)
        Rn = int(Rn)
        Rev[Re][Rv] = Rn

    return V, E, R, C, X, videos, Ldarr, Mec, Rev

def main():
    sys.setrecursionlimit(100500)
    V, E, R, C, X, videos, Ldarr, Mec, Rev = video_parser('input.txt')
    print V
    print E
    print R
    print C
    print X
    print videos
    print Ldarr
    print Mec
    print Rev


if __name__ == "__main__":
    main()
