def lex(code) -> [str]:
    tokens = []
    i = 0
    while i < len(code):
        if code[i] == ' ':
            pass
        elif code[i] in ['+', '-']:
            tokens.append(code[i])
        else:
            num = ''
            print(i)
            while (i < len(code)) and code[i].isdigit():
                num += code[i]
                i += 1
            i -= 1
            tokens.append(int(num))
        i +=1
    return tokens