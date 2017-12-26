Local Functions
===============

- **local functions**
  - like module-level function definitions, local functions are defined at runtime
  - useful for specialized, one-off functions
  - aid in code organization and readibility
  - similar to lambda, but more generalized
    - may contain multiple expressions
    - may contain statements

- **closures**
  - maintain references to objects from earlier scopes
  - commonly used as _function factories_
    - functions that return new, specialized functions
  - require `nonlocal` keyword to bind to var from enclosing scope (much like `global`)
    - `SyntaxError` will be thrown if the variable name doesn't exist
