from typing import Callable, ParamSpec

from foo import foo

_P = ParamSpec("_P")

def bar(obj: Callable[_P, None], /, *args: _P.args, **kwargs: _P.kwargs) -> None: ...
