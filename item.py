class Invoice:
    """
    Object that contains data about a invoice, such as date, name of customer, and total price.
    """

    def __init__(self,date, name_1, name_2, company,address, currency1, currency2, total):
        self.address = address
        self.currency1 = currency1
        self.currency2 = currency2
        self.company = company
        self.name_2 = name_2
        self.name_1 = name_1
        self.date = date
        self.total =total


class Item:
    """
    Creates a product which has a description, quantity, and price
    """
    def __init__(self, description, quantity, price):
        self.quantity = quantity
        self.description = description
        self.price = price
        self.subtotal = quantity*price


if __name__ == '__main__':
    test = Item(description="Cement",quantity=2,  price=20)
    print(test.subtotal)