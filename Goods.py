
class Good():

    def __init__(self, list):
        self.price = float(list[0])
        self.rating = float(list[1])
        self.id = int(list[2])
        self.weight = float(list[3])
        self.size = int(list[4])


class Cart():

    goods = []

    def __init__(self, customer, good):
        self.customer = customer
        self.price = 0
        self.addGood(good)

    def addGood(self, g):
        self.goods.append(g)


        self.price += g.price

    def removeGood(self, g):
        self.goods.remove(g)
        self.price -= g.price