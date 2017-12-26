Functions
=========

- **first-class functions**
  - functions can be treated like any other object
    - passed as function arguments
    - returned from functions

- **callable instances**
  - `__call__()`
  - can grant a class instance the ability to be called like a function
  - helps define functions that maintain state (e.g. caches between calls)
  - can provide attributes and methods to query and modify hidden state

- **callable classes**
  - calling a class invokes the constructor
  - class object callable is a factory function that produces new instances when invoked

- **conditional expression**
  - PEP308
  - `true_value if condition else false_value`

- **timeit**
  - benchmarking function

- **lambdas**
  - _expression_ which evaluates to a function
  - anonymous
  - argument list terminated by colon
  - zero or more args supported (`lambda:`)
  - body is a single _expression_ with no statements
  - return value is _implicitly_ provided by expression. No explicit `return` statement permitted
  - no docstrings
  - awkward or impossible to test (so keep them simple)

- **callable() built-in**
  - predicate function
  - returns boolean to evaluate if a given object is callable

- **extended formal argument syntax**
  - _formal arguments_: arguments at the function definition site
  - _\*args_
    - accepts arbitrary positional arguments
  - _\*\*kwargs_
    - accepts arbitrary keyword arguments
  - these parameters are ordered
    - \*args before \*\*kwargs
    - regular args parameters defined before \*args are invoked positionally
    - regular arg parameters defined after \*args must be invoked as keyword args
    - \*\*\kwargs must come last (except if you have default args as well)
  - can be forwarded to inner function calls

- **extended actual argument syntax**
  - _actual arguments_: arguments at the function call site
  - \* => unpacks series type
  - \*\* => unpacks mapping type
  - do not necessarily correspond to their formal argument counterparts

- **extended call syntax**
  - Use '\*' to unpack iterable series or mappings into positional arguments
  - Common idiom for transposition: `list(zip(*list))`
