## Special methods we already know
`__init__`, `__repr__`, `__call__`, `__enter__`, `__exit__`(with context), `__new__`(@classmethod),
`__getattr__`, `__setattr__`(setattr)
One special field is `__dict__`, `__doc__`

## Use `__getattr__`, `__getattribute__` for Lazy Attributes in Python classes
- Similar to `__call__`, `__repr__`, `__str__`. We can induct that both `__getattr__` and `__getattribute__` are special
methods in a Python class.
- Python makes dynamic behavior or attributes possible with the `__getattr__` and `__getattribute__` special methods.

### What is `__getattr__` special method
For fallback implementation, when we want to find an attribute dynamically in an object.
Fetch an attribute dynamically can be roughly understood as we are trying to find an attribute that is not implemented
in the origin class.
- **`__getattr__`** special method is only called when the attribute does not exist in our object.
- ** `__setattr__`** special method can be defined with our own setattr logic
- **`__getattribute__`** special method
  - `__getattribute__` special method is invoked everytime when we access attributes in a Python object
  - `__getattr__` special method is invoked only when the attribute we are accessing is missing from the Python object
