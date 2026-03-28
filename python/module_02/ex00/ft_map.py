def ft_map(function_to_apply, iterable):
    try:
        for item in iterable:
            yield function_to_apply(item)
    except TypeError:
        return None