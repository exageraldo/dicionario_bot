def get_args(args):
    """
    Will manipulate all received parameters
    ---------------------------------------
    required: args [0] -> word
    optional: args [1] -> maximum size
    """
    resultado = {}
    if len(args) == 2:
        resultado['palavra'] = args[0]
        resultado['max'] = try_to_int(args[1])
    elif len(args) == 1:
        resultado['palavra'] = args[0]
        resultado['max'] = None
    return resultado


def try_to_int(number):
    """
    Will try to transform the parameter into integer
    """
    try:
        return int(number)
    except:
        return None
