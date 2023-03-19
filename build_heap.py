# python3


def build_heap(data):
    swaps = []
    # try to achieve  O(n) and not O(n2)
    length = len(data)
    for r in range(length, -1, 1):
        t = r
        while True:
            tree = t*2+1
            if tree >= length:
                break
            if tree+1<length and data[tree] > data[tree+1]:
                tree = tree+1
            if data[t] > data[tree]:
                swaps.append(t, tree)
                data[t],data[tree] = data[tree],data[t]
                t = tree
            else:
                break
    return swaps


def main():
    option = str(input())
    if "I" in option:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
        return
    if "F" in option:
        file = str(input())
        file = "tests/" + str(file)
        with open(file, 'r') as pakete:
            n = int(pakete.readline())
            data = list(map(int, pakete.readline().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        return 


if __name__ == "__main__":
    main()
