def is_beautiful_string(inputString):

    r = [inputString.count(i) for i in string.ascii_lowercase]

    return r[::-1] == sorted(r)
