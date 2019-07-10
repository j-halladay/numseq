def primes(n):
    list1 = []
    for x in range(1, n):
        result = is_prime(x)
        if result:
            list1.append(x)

    return list1


def is_prime(n):
    mark = 0
    for factor in range(1, n):
        if n % factor == 0:
            mark += 1
        if mark > 1:
            return False
    return True
