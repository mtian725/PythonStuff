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
    for x in target:
        exists = False
        for y in set:
            if x == y:
                exists = True
        if not exists:
            return False
    return True

def mean(lst):
    if len(lst) == 0:
        return None
    else:
        sum = 0
        for x in lst:
            sum += x
        return sum / len(lst)

def to_decimal(lst):
    num = 0
    dec_eql = (2 ** len(lst))/2
    for x in lst:
        num += x * dec_eql
        dec_eql = dec_eql/2
    return int(num)

def factorize(num):
    out = []
    factor = 2
    while num > 1:
        if num % factor == 0:
            out.append(factor)
            num = int(num/factor)
        else:
            factor += 1
    return out

def rotate(lst):
    front = lst[0]
    lst.remove(lst[0])
    lst.append(front)
    return lst

def substr(str, target):
    target_len = len(target)
    if target_len < 1:
        return True
    str_len = len(str)
    curr_index = 0
    while curr_index < (str_len - target_len):
        if str[curr_index] == target[0]:
            temp_index = 1
            out = True
            while temp_index < target_len:
                if not (str[curr_index + temp_index] == target[temp_index]):
                    out = False
                temp_index += 1
            if out:
                return True
        curr_index += 1
    return False

def longest_sequence(str):
    start_index = 0
    end_index = 1
    if len(str) < 1:
        return None
    else:
        curr_char = 0
        next_char = 1
        while next_char < len(str)-1:
            if str[curr_char] == str[next_char]:
                str_len = 1
                while (curr_char + str_len) < len(str) and str[curr_char] == str[curr_char + str_len]:
                    str_len += 1
                if str_len > (end_index - start_index):
                    start_index = curr_char
                    end_index = curr_char + str_len
                curr_char += str_len
                next_char = curr_char + 1
            else:
                curr_char += 1
                next_char += 1
        return str[start_index:end_index]

def main():
    # Testing guass function
    print("Testing guass")
    print(guass(0) == 0)
    print(guass(3) == 6)
    print(guass(10) == 55)
    print(guass(-17) == -1)
    print()

    # Testing in_range
    print("Testing in_range")
    print(in_range([1,2,3], 2, 4) == 2)
    print(in_range([1,2,3], 4, 7) == 0)
    print()

    # Testing subset
    print("Testing subset")
    print(subset([1,2,3,4,5], [1,5,2]) == True)
    print(subset([1,2,3,4,5], [1,2,7]) == False)
    print(subset(['a','b','c'],[]) == True)
    print()

    # Testing mean
    print("Testing mean")
    print(mean([2.0,4.0,9.0]) == 5.0)
    print(mean([]) == None)
    print()

    # Testing to_decimal
    print("Testing to_decimal")
    print(to_decimal([1,0,0]) == 4)
    print(to_decimal([1,1,1,1]) == 15)
    print()

    # Testing factorize
    print("Testing factorize")
    print(factorize(5) == [5])
    print(factorize(12) == [2,2,3])
    print()

    # Testing rotate
    print("Testing rotate")
    print(rotate([1,2,3,4]) == [2,3,4,1])
    print(rotate([6,7,8,5]) == [7,8,5,6])
    print()

    # Testing substr
    print("Testing substr")
    print(substr("rustacean", "ace") == True)
    print(substr("rustacean", "rcn") == False)
    print(substr("rustacean", "") == True)
    print()

    # Testing longest_sequence
    print("Testing longest_sequence")
    print(longest_sequence("ababbba") == "bbb")
    print(longest_sequence("aaabbb") == "aaa")
    print(longest_sequence("xyz") == "x")
    print(longest_sequence("") == None)
    print()

    return

if __name__ == "__main__":
    main()
