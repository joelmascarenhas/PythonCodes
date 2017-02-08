def main():
    str1 = input()
    result = reverse_words_order(str1)
    print(result)


def reverse_words_order(str1):
    list1 = str1.split(" ")
    final_list = []
    list1 = list1[::-1]
    str2 = ' '.join(list1)
    return str2

if __name__ == '__main__':
    main()
