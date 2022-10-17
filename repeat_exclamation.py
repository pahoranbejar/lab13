def repeat_exclamation(message, end, repeat):
    result = ''
    for x in range(repeat):
        result += end

    return message + result


print(repeat_exclamation("how r u", "?", 10))
