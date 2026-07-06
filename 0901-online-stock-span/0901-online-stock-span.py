class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []

    def next(self, price: int) -> int:
        # Current price permanently store karo
        self.prices.append(price)
        # Current index gor ki jgh ye likha h kyunki ye baar baar price le rha h har ek call par
        i = len(self.prices) - 1
        while self.stack and self.prices[self.stack[-1]] <= self.prices[i]:
            self.stack.pop()
        if not self.stack:
            span = i + 1
        else:
            span = i - self.stack[-1]
        self.stack.append(i)
        return span