class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        # preprocess x, n
        adj_n = n
        adj_x = x
        if n < 0:
            adj_n = -n
            adj_x = 1 / x

        # actual pow
        return self._pow(adj_x, adj_n)

    def _pow(self, x: float, n: int) -> float:
        assert n > 0

        if n == 1:
            return x

        if n % 2:
            return x * self._pow(x * x, n // 2)
        else:
            return self._pow(x * x, n // 2)

