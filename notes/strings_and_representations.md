Strings and Representations
===========================

- two functions for making string representations from Python objects
  1. `str()` via `__str__()`
  2. `repr()` via `__repr__()`

- **repr()**
  - built-in
  - produces an _unambiguous_ string representation of an object
    - should include type + any identifying fields
    - as a guideline for `repr()` design, it should operate as close as possible to source code
  - use when:
    - intended for developers
    - exactness is more important than human-friendliness
    - suited for debugging
    - includes identifying info
    - generally best for logging
  - should generally contain _more information_ than the result of `str()`
  - as a rule, you should _always write_ a `repr()` for your classes (default is not very helpful)
  - used when showing _elements of a collection_

- **str()**
  - built-in
  - produces a _readable_, human-friendly representation of an object
  - use when:
    - intended for clients
  - _note:_ `str()` is also the string constructor
  - by default, `str()` simply calls `repr()` (but `repr()` does not call `str()`)
  - used by:
    - `print()`
    - `format()`

- _Sometimes the `repr()` of an object will be shorter than it's `str()`_
  - e.g. representing tabular data with `str()`, but only class + header metadata w/ `repr()`

- **format()**
  - invokes `__format__()`
    - `__format__()` takes optional format spec after colon as arg
      - e.g. `'{:format_spec}'.format(obj)`
  - by default, `__format__()` just calls `__str__()`
  - passing `!r` to `{placeholder}` forces the use of `__repr()__`
  - passing `!s` to `{placeholder}` forces the use of `__str()__`

- **reprlib**
  - _standard library_ module
  - supports alternative implementations of `repr()`
    - limits otherwise excessive string length
    - useful for abbreviating the representations of large collections
  - `reprlib.repr()` as drop-in replacement for `repr()`
  - functionality encapsulated in `reprlib.Repr` class
    - supports customization via subclassing
  - instantiates a singleton instance via `reprlib.aRepr`
    - used by Python and debuggers

- **asci()**
  - replaces non-ASCII characters with escape sequences

- **ord()**
  - converts a single character string to its _integer_ Unicode codepoint
  - inverse of `chr()`
    - `chr(ord(x)) == x  # true`

- **chr()**
  - convers an _integer_ Unicode codepoint to a single character string
  - inverse of `ord()`
    - `ord(chr(y)) == y  # true`
