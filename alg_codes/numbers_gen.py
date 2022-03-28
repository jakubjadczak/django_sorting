import random


class DataGenerator:

    @staticmethod
    def __decrease(n: int, T: list):
        length = len(T)
        for i in range(length):
            num = T[n//2-i-1]-random.randint(1, 4)
            if num < 0:
                num = num * -1
            elif num == 0:
                num = 1

            T.append(num)

        return T

    @staticmethod
    def __increase(n: int):
        T = []
        try:
            start = random.randint(1, n//10)
        except ValueError:
            start = 1

        T.append(start)
        for _ in range(n//2-1):
            num = random.randint(start+1, start+random.randint(2, n//2))
            start = num
            T.append(num)

        return T

    def a_shape(self, n: int):
        T = self.__increase(n)
        T = self.__decrease(n, T)
        return T

    def v_shape(self, n: int):
        T = self.__increase(n)
        T = self.__decrease(n, T)
        L = T[n//2:] + T[:n//2]
        return L

    def increase(self, n):
        return self.__increase(n*2)

    def decrease(self, n):
        return self.__increase(n*2)[::-1]

    @staticmethod
    def random_number(n):
        T = []
        for _ in range(n):
            T.append(random.randint(1, 10*n))

        return T
