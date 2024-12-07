import contextlib
from time import perf_counter
from typing import Generator


@contextlib.contextmanager
def timer(subject: str = "time") -> Generator[None, None, None]:
    """print the elapsed time. (only used in debugging)"""
    start = perf_counter()
    yield
    elapsed = perf_counter() - start
    elapsed_ms = elapsed * 1000
    print(f"{subject} elapsed {elapsed_ms:.4f}ms")