def fib(n):
    if n < 2:
        return n
    else:
        second_to_last = 0
        last = 1
        result = 1

        for _ in range(1, n):
            result = second_to_last + last
            second_to_last, last = last, result

        return result
