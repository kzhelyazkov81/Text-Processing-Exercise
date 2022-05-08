import string


def valid_name(data):
    expected_elements = string.digits + string.ascii_letters + "-" + "_"
    for name in data:
        valid = True
        if 3 > len(name) or len(name) > 16:
            valid = False
        elif len([x for x in name if x in expected_elements]) != len(name):
            valid = False
        elif valid:
            print(name)

d = input().split(', ')
valid_name(d)
