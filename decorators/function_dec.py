"""
we want to store these functions' return values in ascii,
but requiring each to implement `ascii()` would lack
scalability and maintainability.

using a decorator solves for this.
"""
def escape_unicode(fn):
    def wrap(*args, **kwargs):
        x = fn(*args, **kwargs)
        return ascii(x)
    return wrap

@escape_unicode
def vegetable():
    return 'blomkål'

@escape_unicode
def animal():
    return 'bjørn'

@escape_unicode
def mineral():
    return 'stål'
