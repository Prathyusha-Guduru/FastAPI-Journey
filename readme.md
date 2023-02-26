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
- However, we can add [type hints](https://fastapi.tiangolo.com/python-types/) to variables in python

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
- It’s worth mentioning that Pydantic always tries to coerce the type you annotated. For example, if you try to pass “30” to the agefield, this would still work even though this field expects an integer value. Pydantic handles this situation off the shelf.
- Pydantic takes type hints seriously throws Validationg errors when type hints are not followed while assignin values
- Pydatnic provides a list of built-in types for many use cases like that need specific validations such as paths, e
  mail addresses, IP addresses, to name a few.
- Pydantic allows you to natively add some validation on each field by wrapping it inside the Field class.
  For example:
  - you can add constraints on the length of the string fields by using the Field’s max_lengthand min_length arguments
  - you can set boundaries on the numerical fields by using the Field’s ge and le arguments. (ge: greater or equal, le: lower or equal).

```
from pydantic import BaseModel
from typing import Optional, List

class Person(BaseModel):
first_name: str
last_name: str
interest: Optional[List[str]]

data = {"first_name": "Ahmed", "last_name": "Besbes"}
person = Person(**data)
print(person)

# first_name='Ahmed' last_name='Besbes' address=None interests=None

```

### [Understanding async & await](https://youtu.be/t5Bo1Je9EmE)

- code rounties and futures (futures are similar to promises in javascripts)

### [Operations / HTTP methods](https://testfully.io/blog/http-methods/)

Normally we use:
(post and patch are not idempotent)

- `POST` : to create data.
- `GET` : to read data.
- `PUT` : to update data.
- `DELETE` : to delete data.
- `PATCH` : to update data partially (only provided fields)
- `HEAD` : to read data without response body (usually used before get to determine the Content-length i.e size of data)
- `OPTIONS` : to get information about the possible communication options for a given URL (Permitted HTTP methods)
- `TRACE` : for diagnosis purposes

### Path and query parameters

```
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```

here `item_id` is a path parameter

- You can declare the type of a path parameter in the function, using standard Python type annotations:

```
@app.get("/items/{item_id}")
async def read_item(item_id : int):
    return {"item_id": item_id}
```

#### **Query parameters and string validations**

**To show that a query parameters is not-required :**

```
@app.get("/items/")
async def read_items(q: Union[str, None] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

```

To add some more valdations, we can use `Query()`, it should be imported from fastapi

```
from typing import Union

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

```

**NOTE**</br>
You can add regular expressions for validating as well, Eg : </br>
`Query(default=None, min_length=3, max_length=50, regex="^fixedquery$")`

<br></br>

**To show that a parameter is optional**

- Do not set default value to None
  Eg </br>
  `q: str`
- Set default value to ellipses </br>
  `(q: str = Query(default=..., min_length=3)`
- Use pydantic's Required </br>
  `q: str = Query(default=Required, min_length=3)`

**Multiple query parameters**

- with using Query(), you can declare it to recieve a list of query parameters, Eg : </br>
  `(q: Union[List[str], None] = Query(default=None)`

### [Understanding Enums](https://youtu.be/MO-I8Sun_jw)

```
from enum import Enum

# values should be unique
class State(Enum):
  PLAYING = 0
  PAUSED = 1
  GAME_OVER = 2

  print(state.PLAYING)

```

### Request body

- Your API almost always has to send a response body. But clients don't necessarily need to send request bodies all the time.

- To declare a request body, you use Pydantic models with all their power and benefits.

### [Understanding RESTful web API design](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)

### Understanding templating

- https://youtu.be/yu0TbJ2BQso
