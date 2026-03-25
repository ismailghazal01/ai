def ft_progress(lst):
    total = len(lst)

    for i, elem in enumerate(lst):
        percent = int((i / total) * 100)
        print(f"{percent}%...", end="\r")
        yield elem