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
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    inputs = input()
    inputs = inputs.upper()


    # input from keyboard
    if inputs.startswith("I"):
        n = int(input())
        data = list(map(int, input().split()))
    if inputs.startswith("F"):
        name = input()
        name = "tests/" + str(name)
        with open(name, 'r') as edit:
            n = int(edit.readline())
            data = list(map(int, edit.readline().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)


    # this number should be less than 4n (less than 4*len(data))
    assert(len(swaps))<=4*n
    # output all swaps
    print(len(swaps))
    
    
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
