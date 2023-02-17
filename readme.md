### Amazing fast-API repos

- [awesome-fastapi](https://github.com/mjhea0/awesome-fastapi)

### Run the app

```
uvicorn main:app --reload
```

- main : python module (file main.py)
- app : object inside main.py/instance of FastAPI ()
- --reload : restarts the server after code changes,only used in development

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
-
