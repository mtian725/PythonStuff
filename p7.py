def guass(num):
    if num < 0:
        return -1
    else:
        return (int) ((num) * (num + 1) / 2)

def in_range(lst, s, e):
    counter = 0
    for x in lst:
        if x >= s and x <= e:
            counter += 1
    return counter

def subset(set, target):
    return 0

def mean(lst):
    return 0

def to_decimal(lst):
    return 0

def factorize(num):
    return 0

def rotate(lst):
    return 0

def substr(str, target):
    return 0

def longest_sequence(str):
    return 0

def main():
    # Testing guass function
    print(guass(0))
    print(guass(0) == 0)
    print(guass(3))
    print(guass(3) == 6)
    print(guass(10))
    print(guass(10) == 55)
    print(guass(-17))
    print(guass(-17) == -1)

    print()
    # Testing in_range
    print(in_range([1,2,3], 2, 4))
    print(in_range([1,2,3], 2, 4) == 2)
    print(in_range([1,2,3], 4, 7))
    print(in_range([1,2,3], 4, 7) == 0)

    return

if __name__ == "__main__":
    main()
