"""
we want to store these functions' return values in ascii,
but requiring each to implement `ascii()` would lack
scalability and maintainability.

using a decorator solves for this.
"""
def encode_unicode(fn):
    def wrap(*args, **kwargs):
        x = fn(*args, **kwargs)
        return ascii(x)
    return wrap

@encode_unicode
def vegetable():
    return 'blomkål'

@encode_unicode
def animal():
    return 'bjørn'

@encode_unicode
def mineral():
    return 'stål'
