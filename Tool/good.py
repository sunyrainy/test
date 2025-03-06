class Good:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("A new good has been created with name: {} and price: {}".format(self.name, self.price))

if __name__ == '__main__':
    good1 = Good("apple", 1.5)
    print(good1.name)