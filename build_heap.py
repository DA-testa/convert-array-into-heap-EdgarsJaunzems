# python3


def build_heap(data):
    swaps = []
    length = len(data)
    for i in range(length, -1, -1):
        j = i
        while True:
            tree = j*2 + 1
            if tree >= length:
                break
            if tree+1 < length and data[tree] > data[tree+1] :
                tree = tree+1
            if data[j] > data[tree]:
                swaps.append((j, tree))
                data[j], data[tree] = data[tree], data[j]
                j = tree
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
