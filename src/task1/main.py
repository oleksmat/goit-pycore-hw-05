def caching_fibonacci():
    """
        Returns function to calculate `n`-th Fibonacci number with internal
        cache.

        When Fibonacci function is called, it recursively calculates values
        before `n` if they were not calculated before. If a value was cached,
        function short-circuits and stack unwinding happens.

        There is no way to purge the cache - if an `n`-th number was calculated
        once, every number between `2` and `n` (inclusive) will be cached with
        the instance of a function.
    :return:
    """
    cache: dict[int, int] = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            print(f'Cache hit for {n}')
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]
    return fibonacci
