from collections.abc import Callable

one_string: str = ''
one_inter: int = 0
one_float: float = 0.0
one_boolean: bool = False
one_set: set = {1, 2, 3}
one_list: list = []
one_tuple: tuple = 1, 2, 3
one_dict: dict = {}


def sum(x: int, y: int, z: float) -> float:
    return x + y + z


list_of_integer: list[int] = [1, 2, 3, 4]
list_of_strings: list[str] = ['a', 'b', 'c']
list_of_tuples: list[tuple] = [(1, 'a'), (2, 'b')]
list_of_list_of_int: list[list[int]] = [[1], [2], [4, 5]]


one_dict: dict[str, int] = {
    "A": 0,
    "B": 1,
}

one_dict_of_list: dict[str, list[int]] = {
    "a": [1, 2],
    "b": [3, 4]
}


one_set_of_integer: set[int] = {1, 2, 3}

strings_and_integers: str | int = 1  # Union
strings_and_integers = "A"
strings_and_integers = 2

un_list: list[int | str] = [1, 2, 3, 'a']


def minus(x: int, y: float = 0) -> float:
    return x - y


sum_integers = Callable[[int, int], int]


def execute(func: sum_integers, a: int, b: int) -> int:
    return func(a, b)


def sum2(a: int, b: int) -> int:
    return a+b


print(execute(sum2, 1, 2,))
