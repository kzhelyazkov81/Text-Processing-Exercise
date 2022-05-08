def caesar_cipher(text):
    result = ''.join([chr(ord(ch)+3) for ch in text])
    print(result)


text = input()
caesar_cipher(text)
