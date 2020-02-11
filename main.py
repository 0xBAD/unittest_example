def is_prime(num):
    if num in (2, 3, 5, 7):
        return True
    if num < 2 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 2 == 0:
        return False

    return True



