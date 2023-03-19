# python3


def build_heap(data):
    swaps = []
    # try to achieve  O(n) and not O(n2)
    length = len(data)
    for s in range(length, -1, 1):
        a = s
        while True:
            tree = a*2+1
            if tree >= length:
                break
            if tree+1<length and data[tree] > data[tree+1]:
                tree = tree+1
            if data[a] > data[tree]:
                swaps.append(a, tree)
                data[a],data[tree] = data[tree],data[a]
                a=tree
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
        file = open("./tests/" + name,'r')
        n = int(file.readline())
        read = file.readline()
        data =list(map(int, read.split()))

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
