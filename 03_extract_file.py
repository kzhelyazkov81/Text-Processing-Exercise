def name_subtract(data):
    needed_information = data[-1].split('.')
    filename = needed_information[0]
    extension = needed_information[1]
    print(f'File name: {filename}')
    print(f'File extension: {extension}')


data = input().split('\\')
name_subtract(data)
