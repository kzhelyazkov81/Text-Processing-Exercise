def emoticon_finder(text):
    result = [text[i] + text[i+1] for i in range(len(text)) if text[i] == ':' and text[i+1] != ' ']
    result = '\n'.join(result)
    print(result)


text = input()
emoticon_finder(text)
