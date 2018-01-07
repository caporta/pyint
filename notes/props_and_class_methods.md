Class Attributes & Methods
==========================

- **class attributes**
  - Defined as normal variable names within the class scope
  - Can be accessed internally via `ClassName.attribute_name`
    - can also be accessed via `self.attribute_name`, _but_:
      - Less explicit and readable
      - Assignment via `self` will _create new instance attribute_ of the same name,
      leaving the class attribute unchanged

- **static methods**
  - Can be defined with the `@staticmethod` decorator
  - Does not have direct knowledge of their defining class,
  they simply allow us to group a function in the class scope
  - Use when:
    - No access needed to either _class_ or _instance_ objects
    - Most likely an implementation detail of the class
    - May be able to be implemented as a module scope function

- **class methods**
  - Can be defined with the `@classmethod` decorator
  - Use when:
    - Requires access to the class object to call other class methods or the constructor
    - Factory functions
  - _Can be overridden in subclasses_
    - For polymorphic dispatching of class methods, method **must be called on `self`**
    - In turn, calling classmethods on `ClassName` prevents overriding

- **setting & getting**
  - leverages encapsulation
  - idiomatic when defined using `@property` (getter) & `@propname.setter` decorators
  - overriding a setter in a derived class involves qualifying prop with base class name
    - e.g. `@BaseClassName.propname.setter
    - this behavior can get complex across larger inheritence hierarchies
      - refactor this setter/getter complexity with Template Method design pattern
