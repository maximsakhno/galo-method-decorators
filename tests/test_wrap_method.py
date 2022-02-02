from functools import wraps
from typing import Callable
from unittest.mock import Mock, call

import pytest

from galo_method_decorators import wrap_method


def test_single_decorator() -> None:
    class Test:
        def test(self) -> None:
            pass

    def decorator(wrappee: Callable) -> Callable:
        @wraps(wrappee)
        def wrapper(*args, **kwargs):
            mock(*args, **kwargs)
            return wrappee(*args, **kwargs)

        return wrapper

    mock = Mock()
    test = Test()
    wrap_method(test.test, decorator)
    test.test()
    mock.assert_called_once_with(test)


def test_double_decorator() -> None:
    class Test:
        def test(self) -> None:
            pass

    def decorator1(wrappee: Callable) -> Callable:
        @wraps(wrappee)
        def wrapper(*args, **kwargs):
            mock.decorator1(*args, **kwargs)
            return wrappee(*args, **kwargs)

        return wrapper

    def decorator2(wrappee: Callable) -> Callable:
        @wraps(wrappee)
        def wrapper(*args, **kwargs):
            mock.decorator2(*args, **kwargs)
            return wrappee(*args, **kwargs)

        return wrapper

    mock = Mock()
    test = Test()
    wrap_method(test.test, decorator1)
    wrap_method(test.test, decorator2)
    test.test()
    mock.assert_has_calls(
        [
            call.decorator2(test),
            call.decorator1(test),
        ]
    )


def test_not_method() -> None:
    def test():
        pass

    def decorator(wrappee: Callable) -> Callable:
        @wraps(wrappee)
        def wrapper(*args, **kwargs):
            return wrappee(*args, **kwargs)

        return wrapper

    with pytest.raises(TypeError):
        wrap_method(test, decorator)
