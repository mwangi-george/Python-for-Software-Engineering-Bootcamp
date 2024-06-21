from typing import Union, Optional


def test_func():
    return "test"


val = test_func()
print(val)

# Any


def test_func(a):
    return a


# defining the type of something
# take an integer and return an integer
def test_func(a: int) -> int:
    return a


def test_print(a: str) -> None:
    print(a)


def division(a: int, b: int) -> Union[float, None]:
    """
    Strict types:

    Uses Union since we may not know what to expect 
    """
    if b != 0:
        return a / b


# similar function using Optional

def division(a: int, b: int) -> Optional[float]:
    """
    Strict types:

    If what to return is a value, it will be a float, if not, None

    An optional response, either a value or none
    """
    if b != 0:
        return a / b
