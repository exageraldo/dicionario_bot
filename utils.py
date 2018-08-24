def get_args(args):
    resultado = {}
    if len(args) == 2:
        resultado['palavra'] = args[0]
        resultado['max'] = try_to_int(args[1])
    elif len(args) == 1:
        resultado['palavra'] = args[0]
        resultado['max'] = None
    return resultado


def try_to_int(number):
    try:
        return int(number)
    except:
        return None
