from string import ascii_lowercase


def extract_func(text):
    current_num = int(''.join([num for num in text if num.isdigit()]))
    result = 0
    for i in range(len(text)):
        if text[i].isalpha():
            index = ascii_lowercase.index(text[i].lower()) + 1
            if i == 0:
                if text[i].islower():
                    result = current_num * index
                else:
                    result = current_num / index
            else:
                if text[i].islower():
                    result += index
                else:
                    result -= index
    return result


def letters_change(data):
    result = 0
    for num in data:
        result += extract_func(num)
    print(f'{result:.2f}')


data = input().split()
letters_change(data)

