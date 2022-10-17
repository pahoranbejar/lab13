def wrap_in_box(text):
    size = len(text)
    return '-' * (size+4) + '\n| ' + text + ' |\n' + '-' * (size+4)


print(wrap_in_box("hi"))
