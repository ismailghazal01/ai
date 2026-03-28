def ft_filter(function_to_apply, iterable):
    try:
        for item in iterable:
            if function_to_apply(item):
                yield item
    except TypeError:
        return None