Decorators
==========

- replace, modify, or enhance functions _without changing their definitions_
  - calling code does not need to change
  - decorator mechanism uses the modified function's original name
- **implemented as a callable object that takes and returns other callables**
  - e.g. a function that takes and returns other functions
```
@my_decorator
def my_function(x, y):
    return x + y
```
- **order of ops:**
  1. compiles base function
  2. passes base function to decorator
  3. binds return value of the decorator to the name of the base function

- multiple decorators can be applied to the same function
  - processed in _reverse order_

- naive decorators can _lose important metadata_
  - `functools.wraps()` properly updates metadata on wrapped functions

- useful as _function argument validators_
  - factory functions that return decorators (that return wrappers...)
