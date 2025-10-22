from __future__ import annotations

import asyncio
import functools
import time
from typing import Callable, Iterable, Iterator, Optional, TypeVar

# Typhilfen für generische Funktionen/Decorator
T = TypeVar("T")
R = TypeVar("R")

# === Level 1: Basics ===

def add(a: int, b: int) -> int:
    """Addiert zwei Zahlen."""
    return a + b


def greet(name: str = "Welt") -> str:
    """Erzeugt einen Grußtext; zeigt Default-Argumente und f-Strings."""
    return f"Hallo, {name}!"


def is_even(n: int) -> bool:
    """Prüft, ob n gerade ist."""
    return n % 2 == 0


def safe_divide(a: float, b: float) -> Optional[float]:
    """Teilt a durch b; gibt None zurück, falls b == 0 (Fehlerbehandlung)."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


# === Level 2: Rekursion & Generatoren ===

def factorial(n: int) -> int:
    """Fakultät per Rekursion; validiert die Eingabe."""
    if n < 0:
        raise ValueError("n muss >= 0 sein")
    return 1 if n <= 1 else n * factorial(n - 1)


@functools.lru_cache(maxsize=None)
def fib(n: int) -> int:
    """n-te Fibonacci-Zahl mit Memoization (lru_cache)."""
    if n < 0:
        raise ValueError("n muss >= 0 sein")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fibonacci_seq(limit: int) -> Iterator[int]:
    """Generator, der die ersten 'limit' Fibonacci-Zahlen liefert."""
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


# === Level 3: Höhere Funktionen & Closures ===

def apply_and_sum(xs: Iterable[T], f: Callable[[T], float]) -> float:
    """Wendet f auf jedes Element an und summiert die Ergebnisse."""
    return sum(f(x) for x in xs)


def make_multiplier(factor: int) -> Callable[[int], int]:
    """Erzeugt eine Funktion, die ihr Argument mit 'factor' multipliziert (Closure)."""
    def mul(x: int) -> int:
        return x * factor

    return mul


# === Level 4: Decorators & Context Manager ===

def measure(func: Callable[..., R]) -> Callable[..., R]:
    """Decorator, der die Laufzeit einer Funktion misst und ausgibt."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):  # type: ignore[misc]
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration_ms = (time.perf_counter() - start) * 1000
        print(f"{func.__name__} dauerte {duration_ms:.2f} ms")
        return result

    return wrapper


@functools.lru_cache(maxsize=None)
@measure
def compute_primes(limit: int) -> list[int]:
    """Eratosthenes-Sieb: Alle Primzahlen <= limit.
    Mit Caching (lru_cache) + Zeitmess-Decorator.
    """
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    p = 2
    # Klassische Sieb-Implementierung
    while p * p <= limit:
        if sieve[p]:
            start = p * p
            step = p
            sieve[start : limit + 1 : step] = b"\x00" * (((limit - start) // step) + 1)
        p += 1
    return [i for i, is_prime in enumerate(sieve) if is_prime]


# Kontextmanager per Dekorator
import contextlib


@contextlib.contextmanager
def timer(label: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        duration_ms = (time.perf_counter() - start) * 1000
        print(f"[{label}] {duration_ms:.2f} ms")


# === Level 5: Async/await ===
async def fetch_double(x: int) -> int:
    """Asynchrone Funktion, simuliert IO (Sleep) und gibt 2*x zurück."""
    await asyncio.sleep(0.1)
    return x * 2


async def async_demo() -> None:
    results = await asyncio.gather(*(fetch_double(i) for i in range(5)))
    print("async results:", results)


# Praktische Helfer (partial)
add10 = functools.partial(add, 10)


def main() -> None:
    print("=== Level 1: Basics ===")
    print("add(2, 3) ->", add(2, 3))
    print("greet() ->", greet())
    print("greet('Anna') ->", greet("Anna"))
    print("is_even(4) ->", is_even(4))
    print("safe_divide(3, 0) ->", safe_divide(3, 0))

    print("\n=== Level 2: Rekursion & Generatoren ===")
    print("factorial(5) ->", factorial(5))
    print("fib(10) ->", fib(10))
    print("list(fibonacci_seq(7)) ->", list(fibonacci_seq(7)))

    print("\n=== Level 3: Höhere Funktionen & Closures ===")
    print(
        "apply_and_sum(range(1,6), lambda x: x*x) ->",
        apply_and_sum(range(1, 6), lambda x: x * x),
    )
    times3 = make_multiplier(3)
    print("make_multiplier(3)(7) ->", times3(7))
    print("add10(5) ->", add10(5))

    print("\n=== Level 4: Decorators & Context Manager ===")
    with timer("compute_primes(50000)"):
        primes = compute_primes(50000)
    print(f"Anzahl Primzahlen bis 50000: {len(primes)}")
    _ = compute_primes(3000)  # zweite Messung (aus Cache schneller + Decorator-Ausgabe)

    print("\n=== Level 5: Asyncio ===")
    asyncio.run(async_demo())


if __name__ == "__main__":
    main()

