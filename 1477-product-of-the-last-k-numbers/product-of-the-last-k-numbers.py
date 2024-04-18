class ProductOfNumbers:

    def __init__(self):
        self.products = []
        self.product = 1
        

    def add(self, num: int) -> None:
        if num:
            self.product *= num
            self.products.append(self.product)
        else:
            self.products = []
            self.product =  1

    def getProduct(self, k: int) -> int:
        if len(self.products)< k:
            return 0
        elif k == len(self.products):
            return self.product
        else:
            if len(self.products) == k:
                return self.products[-1]
            elif len(self.products) > k:
                return self.products[-1] // self.products[len(self.products) - k - 1]
            else:
                return 0

