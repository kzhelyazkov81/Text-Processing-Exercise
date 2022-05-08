def replace(data):
    result = ''
    last_ch = ''
    for ch in data:
        if ch != last_ch:
            result += ch
            last_ch = ch
    print(result)


text = input()
replace(text)
