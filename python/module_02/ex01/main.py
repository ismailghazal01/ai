def what_are_the_vars(*args, **kwargs):
    obj = ObjectC()

    for i, arg in enumerate(args):
        setattr(obj, "var_" + str(i), arg)

    for key, value in kwargs.items():
        if hasattr(obj, key):
            return None
        setattr(obj, key, value)

    return obj


class ObjectC(object):
    pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            print("{}: {}".format(attr, getattr(obj, attr)))
    print("end")