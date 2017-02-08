def main():
    str1 = input()
    k = int(input())
    var = removekdigits(str1,k)
    print(var)


def removekdigits(str1, k):
    if k == 0:
        return str1
    elif k >= len(str1):
        return '0'
    else:
        flag = 0
        while k > 0:
            flag = 0
            for i in range(0, len(str1)-1):
                if str1[i] > str1[i+1]:
                    flag = 1
                    break
            k -= 1
            if flag == 0:
                str1 = str1[0:i+1]
            else:
                str1 = str1[0:i] + str1[i+1:]
        return str1

if __name__ == '__main__':
    main()


