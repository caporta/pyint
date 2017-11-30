Functions
=========

- **callable instances**
  - `__call__()`
  - can grant a class instance the ability to be called like a function

- **callable classes**
  - calling a class invokes the constructor
  - class object callable is a factory function that produces new instances when invoked

- **conditional expression**
  - PEP308
  - `true_value if condition else false_value`

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
  - returns boolean to evaluate if a given object is callable
