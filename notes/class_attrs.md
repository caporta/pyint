Class Attributes
================

- Defined as normal variable names within the class scope
- Can be accessed internally via `ClassName.attribute_name`
  - can also be accessed via `self.attribute_name`, _but_:
    - Less explicit and readable
    - Assignment via `self` will _create new instance attribute_ of the same name,
      leaving the class attribute unchanged
