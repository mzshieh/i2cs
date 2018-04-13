def tokens():
    while True:
        try:
            buffer = input()
        except EOFError:
            break
        for tok in buffer.strip().split():
            yield tok

token_it = iter(tokens())

def get_int():
    global token_it
    tok = next(token_it,None)
    try:
        ret = int(tok)
    except ValueError:
        ret = None
    return ret

def get_float():
    global token_it
    tok = next(token_it,None)
    try:
        ret = float(tok)
    except ValueError:
        ret = None
    return ret

def get_str():
    global token_it
    tok = next(token_it,None)
    return tok
