# PYTHON OBJECT ORIENTATION

---

Take data and functionality and _wrap_ it into `classes`

-  `Class`:
   -  Blueprint for new objects. Defines `attributes` and `methods`
-  `Method`:
   -  function defined on class. Can see or change attributes on `instance`
-  `Class method`
   -  function defined on `class`. Called on `class`, not individual `instance`.

---

# Instances

Like in JS, you make an `instance` by calling the `class`

```py
# 'Counter' is a built-in class from the 'collections' library. We can use it to create an object with keys (based on the iterable from which we created the Counter) and values (which are the count of each key). And we have a few methods we can run on it.

from collections import Counter

# make instance of a counter
counts = Counter("hello world")

type(counts)    # 'collections.Counter'

isinstance(counts, Counter) # True

# help(Counter) is a useful investigation tool
```

```py
from datetime import date

# built in data types (eg. int, list, str, ...) are NOT capitalized, even though they are Classes

my_date = date(1987, 7, 9)
my_date.weekday()
```

Instances in JS:

-  get/set attribute of object: `o.name` or `o['name']`
-  call method: `o.method()` or `o['method']()`

In Python:

-  get/set attribute of object: `o.name`
-  call method: `o.method()`
-  retrieve value from dictionary: `o['my-key']`
   -  a `Class object` is NOT the same as a `dictionary`

---

# Defining our own Custom Classes

Making classes is similar to JS:

```py
class Triangle:
    "Right triangle"

    def __init__(self, a, b):
        "Create triangle from a and b sides."
        self.a = a
        self.b = b

    def get_hypotenuse(self):
        "Get hypotenuse (length of 3rd side)."
        return math.sqrt(self.a ** 2 + self.b ** 2)

    def get_area(self):
        "Get area of triangle"
        return (self.a * self.b) / 2

    def describe(self):
        return f"My area is {self.get_area()}"
```

## `__init__`

-  `__init__` is kinda like the constructor function in JS. It will be called when we instantiate the class

## `self`

-  `self` is similar to `this`

   -  `this` is maybe a bit mysterious. it automatically gets created
   -  `self` is explicit: you MUST list it as the first argument of methods
      -  it's just a normal variable otherwise
