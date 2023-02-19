### Amazing fast-API repos

- [awesome-fastapi](https://github.com/mjhea0/awesome-fastapi)

### Run the app

```
uvicorn main:app --reload
```

- main : python module (file main.py)
- app : object inside main.py/instance of FastAPI ()
- --reload : restarts the server after code changes,only used in development

### [Understanding \*args and \*\*kargs](https://www.stechies.com/doubleasterisks-python/)

- \*args for non-keyword arguments
- \*\*kargs for keyword arguments
- In the case of numeric data values, the single asterisks (\*) work as a multiplication operator, while the double- asterisks (\*\*) work as an exponentiation operator.
- In a function definition, the single asterisk (\*) takes an iterator like a list and extends it into a series of arguments, whereas the double-asterisk (\*\*) takes dictionary only and expands it.

### [Understand type hints](https://youtu.be/QORvB-_mbZ0)

- [typing](https://docs.python.org/3/library/typing.html) is an in-built module in python
- type annotations are used for documentation purposes
- Unlike python, statically typed languages like C++ AND Java, its compulsory to declare a type to the variable before assigning a value
- Python is dymanically typed so we dont have to specify the type
- However, we can add type hints to variables in python

```
x:str = 1
```

- this is simply for documentation he the code wont throw an error even if you have mismatches with your types
- To solve this, you can use "mypy" to run a static code analysis
  <br></br>
  `pip install mypy`

  `mypy {path to the file} `

- Function Anotations

  ```
    def add_numbers(a : int, b: int, c:int) -> int:
      return a+b+c
  ```

  the "-> int" in the function defines that the function will return an int

- List Types
  - `from typing import List`
- Dictionary Types
  - `from typing import Dict`
- Set Types

  - `from typing import Set`

- Optional Type

  ```
  from typing import Optional
  def foo(Optional output : bool=False):
      pass
  ```

- Any type

  ```
  def foo(output : Any):
  pass
  ```

- Sequenece type (lists, tuples, strings etc)

  - only indexible sequences
  - sets don't work because they are indexible

- Callable
- Tuples
- TypeVar
  - placeholder type
- Union
  - to combine 1 or more possible types

### Check Interactive Docs

- visit localhost/docs or localhost/redoc
- docs is provided by swagger, redoc is provided by redoc

### [Understand Dataclasses](https://towardsdatascience.com/9-reasons-why-you-should-start-using-python-dataclasses-98271adadc66)

- The motivation behind this module is that we sometimes define classes that only act as data containers and when we do that, we spend a consequent amount of time writing boilerplate code with tons of arguments, an ugly **init** method and many overridden functions. Dataclasses alleviates this problem while providing additional useful methods under the hood.
- Example :

**Without dataclass**

```
class Person():
    def __init__(self, first_name, last_name, age, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
```

**With dataclass**

```
from dataclasses import dataclass
@dataclass
class Person:
     first_name: str
     last_name: str
     age: int
     job: str
```

<br></br>

### [Understanding Pydantic](https://towardsdatascience.com/8-reasons-to-start-using-pydantic-to-improve-data-parsing-and-validation-4f437eae7678)

- [Pydantic](https://docs.pydantic.dev/) is a library that provides data validation and settings management using type annotations.
- Install :
  `pip install pydantic`
-
