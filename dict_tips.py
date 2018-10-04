import operator


def merge_dict(x: dict, y: dict) -> dict:
    """
    Python merges dictionary keys in the order listed in the expression,
    overwriting duplicates from left to right.
    e.g.
    x = {'a': 1, 'b': 2}
    y = {'b': 3, 'c': 4}
    z = {**x, **y}
    print(z)
    > {'c': 4, 'a': 1, 'b': 3}
    :param x: dictionary - first dict to merge
    :param y: dictionary - second dict to merge
    :return: dictionary - merged dictionary
    """
    return {**x, **y}


def get_method(x: dict, x_key):
    print('dict.get() method')
    if x.get(x_key):
        print('Key:',  x_key, 'does not exist')
        return x.get(x_key)
    else:
        print('Key:', x_key, 'does exist')
        return None


def get_syntax(x: dict, x_key):
    print('dict[key] syntax')
    try:
        x[x_key]
    except KeyError:
        print('Key:', x_key, 'does not exist')
        return None
    else:
        print('Key:', x_key, 'does exist')
        return x[x_key]


if __name__ == "__main__":
    X = {'a': 1, 'b': 2}
    Y = {'b': 3, 'c': 4}
    z = merge_dict(X, Y)
    print(z)
    print(help(merge_dict))

    xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
    print(sorted(xs.items(), key=lambda x: x[1]))

