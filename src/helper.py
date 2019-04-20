class Helper(object):
    @staticmethod
    def __is_prime(number: int, it=2):
        if number < 1:
            raise ValueError('Please enter positive number!')

        if number == 2:
            return True

        if number == 1:
            return False

        if number - 1 == it:
            return number % it != 0

        if number % it != 0 and Helper.__is_prime(number, it + 1):
            return True

        return False

    @staticmethod
    def is_prime(number: int):
        return Helper.__is_prime(number, 2)
