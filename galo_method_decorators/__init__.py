"""
A library that allows you to use decorators for instance methods without affecting the methods in
the class.
"""

from types import MethodType
from typing import Callable

__version__ = "0.1.0"


__all__ = [
    "wrap_method",
]


def wrap_method(method: Callable, decorator: Callable[[Callable], Callable]) -> None:
    if not isinstance(method, MethodType):
        raise TypeError(method, MethodType)

    self = method.__self__
    func = method.__func__
    name = func.__name__
    wrapped_func = decorator(func)
    wrapped_method = MethodType(wrapped_func, self)
    setattr(self, name, wrapped_method)
