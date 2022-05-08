def explode(text):
    exploded_list = []
    index = 0
    strength = 0
    while index < len(text):
        exploded_list.append(text[index])
        if text[index] == '>':
            index += 1
            strength += int(text[index])
            if strength == 0:
                exploded_list.append(text[index])
            while True:
                if text[index] == '>':
                    break
                strength -= 1
                if strength <= 0:
                    strength = 0
                    index += 1
                    break
                index += 1
                if index >= len(text):
                    break
        else:
            index += 1
    result = ''.join(exploded_list)
    print(result)


text = list(input())
explode(text)
