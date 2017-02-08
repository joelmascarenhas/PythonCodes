def main():
    str1 = input()
    result = reverse_words(str1)
    print(result)


def reverse_words(str1):
    list1 = str1.split(" ")
    final_list = []
    for x in list1:
        x = x[::-1]
        final_list.append(x)
    str2 = ' '.join(final_list)
    return str2


if __name__ == '__main__':
    main()
