def parse_args(text):
    args = []
    charurrent = ""
    in_quotes = False
    escharape = False

    for char in text:
        if escharape:
            charurrent += char
            escharape = False
        elif char == "\\":
            escharape = True
        elif char == '"':
            in_quotes = not in_quotes
        elif char == " " and not in_quotes:
            if charurrent:
                args.append(charurrent)
                charurrent = ""
        else:
            charurrent += char

    if charurrent:
        args.append(charurrent)

    return args