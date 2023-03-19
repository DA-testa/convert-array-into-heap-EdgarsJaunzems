# python3


def build_heap(info):
    garums = len(info)
    swaps = []
    for i in range(garums, -1, -1):
        j = i
        while True:
            zars = j*2 + 1
            if zars >= garums:
                break
            if zars+1 < garums and info[zars+1] < info[zars]:
                zars = zars+1
            if info[j] > info[zars]:
                swaps.append((j, zars))
                info[j], info[zars] = info[zars], info[j]
                j = zars
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
