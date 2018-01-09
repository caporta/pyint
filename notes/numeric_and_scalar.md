Numeric & Scalar Types
======================

- **int**
  - unlimited precision signed integer

_ **float**
  - IEEE-754 double precision (64-bit)
  - 53 bits of binary precision
  - 15-17 bits of decimal precision
  - [{sign = 1 bit}{exponent = 11 bits}{mantissa = 52 bits}]
  - thus, you can convert any decimals with 15 significant figures
  into floats and back without loss of information
  - `sys.float_info` object prints metadata on float properties and bounds

- **decimal.Decimal**
  - std lib module `decimal` containing the class `Decimal`
  - floating point
  - configurable (although finite) precision
  - defaults to 28 digits of decimal precision
  - print configuration data via `decimal.getcontext()`
  - _always quote literal fractional values_
    - avoids necessary rounding when internally converted to Base 2
  - `decimal.getcontext().traps[decimal.FloatOperation] = True`
    - adds FloatOperation exception to the exception whitelist `traps`
    - enforces rules against passing a float to a Decimal or attempting to operate on one
  - constructed values preserve precision of the module context setting
    - e.g. `decimal.getcontext().prec = 6; Decimal('1.234567') + Decimal(1) => Decimal('2.23457')`
  - supports `Infinity`, `-Infinity`, & `NaN`
  - functions of math module _cannot be used_ with Decimal type
    - alternatively, many class methods are provided directly on `Decimal`

- **fraction.Fraction**
  - std lib module `fractions` containing the class `Fraction`
  - rational numbers
  - interoperable with int, float, and Decimal types
    - caveat: be careful with float precision
  - as with Decimals, can be constructed with a string
  - unsurprising arithmetic
  - does not support some math module equivalents
    - e.g. `.sqrt()` because the result may be irrational
    - exceptions include `.ceil()` & `.floor()`

- **complex**
  - built-in
  - represents complex numbers
  - EE notation for _imaginary numbers_: `j=√-1`
  - e.g. `3 + 4j`
  - constructor can be passed int(s) or string args
    - string arg _may_ have parentheses but _must not_ contain spaces
  - `real` and `imag` attributes break down `complex` types to component parts
  - `conjugate()` reproduces full complex notation
  - does not support math module, but has `cmath` equivalent

- **abs()**
  - built-in function
  - gives the distance from zero (non-negative magnitude)

- **round()**
  - built-in function
  - performs _decimal_ rounding for all scalar number types
  - behavior biased toward _even numbers_
    - e.g. `round(1.5) => 2; round(2.5) => 2`
  - fundamentally a _decimal operation_ so can give suprising results for `float` values

- **number base conversions**
  - _`bin()`_ => base 2
    - literal: 0b101010
  - _`oct()`_ => base 8
    - literal: 0o52
  - _`hex()`_ => base 16
    - literal: 0x2a
  - _`int(x, base)`_ => bases 2 to 36
    - defaults to base 10
    - unary is not supported

- **datetime**
  - std library module
  - _immutable instances_
  - types:
    - **date** — proleptic Gregorian calendar
      - year | month | day
    - **time** — ideal day time (ignoring leap seconds)
      - hour | minute | second | microsecond
      - can be in either `naive` or `aware` modes
        - `aware` times contain knowledge of timezones & daylight savings
          - via `tzinfo` (abstract) & `timezone` (`utcoffset()`)
    - **datetime** — composite of `date` and `time` types
    - **timedelta** — duration expressing diff between `date` or `datetime` instances
      - constructor accepts and _sums_:
        - days | seconds | microseconds | milliseconds | minutes | hours | weeks
      - instances _store_ only:
        - days | seconds | microseconds
  - does not provide exhaustive timezone data; for this, use one of the following libs:
    - pytz
    - python-dateutil
