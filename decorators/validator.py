def check_non_negative(index):
    def validator(fn):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError('Argument {} must be non-negative.'.format(index))
            return fn(*args)
        return wrap
    return validator


@check_non_negative(1)
def create_list(value, size):
    return [value] * size
