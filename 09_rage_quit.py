def message(word):
    unique_symbols = ''
    current_message = ''
    rage_message = ''
    i = 0
    while i < len(word):
        if not word[i].isdigit():
            if word[i].isalpha():
                symbol = word[i].upper()
            else:
                symbol = word[i]
            current_message += symbol
            if symbol not in unique_symbols:
                unique_symbols += symbol
            i += 1
        else:
            repeat = word[i]
            if i < len(word) - 1:
                if word[i+1].isdigit():
                    repeat += word[i+1]
                    i += 1
            i += 1
            repeat = int(repeat)
            rage_message += repeat * current_message
            current_message = ''
    print(f'Unique symbols used: {len(unique_symbols)}')
    print(rage_message)


data = input()
message(data)