def ft_reduce(function_to_apply, iterable):
    try:
        it = iter(iterable)
        result = next(it)
        for item in it:
            result = function_to_apply(result, item)
        return result
    except TypeError:
        return None