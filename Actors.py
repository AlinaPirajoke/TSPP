import random
from Goods import Cart, Good
from Server import Site, Server

class Customer():

    def __init__(self, money, card, name, address):
        self.money = money
        self.card = card
        self.name = name
        self.address = address


    def doSomething(self, server):
        print(f"Клиент {self.name} зашёл на сайт")
        site = server.showSite()
        server.addCustomer(self)
        site.showGoods()
        while 1:
            goods = site.search()
            print(f"Клиент {self.name} ищет товары")
            if random.randint(0, 1):
                site.filterArray()
                print(f"Клиент {self.name} фильтрует поисковую выдачу")
            if random.randint(0, 1):
                site.sortArray()
                print(f"Клиент {self.name} упорядочивает поисковую выдачу")
            if random.randint(0, 1):
                site.askQuestion("Почему")
                print(f"Клиент {self.name} задал вопрос")
            if random.randint(0, 1):
                continue
            elif random.randint(0, 1):
                good = goods[random.randint(0, len(goods)-1)]
                site.addToCart(good, self)
                print(f"Клиент {self.name} добавил в корзину {good.id}")
                if random.randint(0, 1):
                    site.buyGoods(self)
                    print(f"Клиент {self.name} совершил покупку")
                    break
            else:
                print(f"Клиент {self.name} ущёл")
                return

        #order = post.getOrder()
        print(f"Клиент {self.name} получил заказ")

    def takeMoney(self, sum):
        if self.money >= sum:
            self.money -= sum
            return sum
        else: return 0


class Administrator(Customer):

    def __init__(self, money, card, name, address, salary, server):
        super().__init__(money, card, name, address)
        self.salary = salary
        self.server = server
        self.server.addAdmin(self)

    def doSomething(self):
        if random.randint(0, 1):
            self.server.editConfig()
            print(f"Администратор {self.name} изменил сервер")
        else:
            self.server.site.editConfig()
            print(f"Администратор {self.name} изменил сайт")

    def addGood(self, good):
        if random.randint(0,2):
            print(f"Администратор {self.name} одобрил")
            self.server.addGood(good)

        else: print(f"Администратор {self.name} отказал")

class Seller():

    def __init__(self, rating, name, server):
        self.rating = rating
        self.name = name
        server.addSeller(self)
        self.site = server.showSite()

    def answerOnQuestion(self, question):
        print(f"Продавец {self.name} ответил на вопрос")
        return "Потому что"

    def collectOrder(self, order):
        print(f"Продавец {self.name} собрал заказ")
        return order

    def doSomething(self):
        for i in range(3):
            if random.randint(0,1):
                good = Good([random.randint(0, 3000), 5, random.randint(0, 1000000), random.randint(0, 10), random.randint(0, 30)])
                print(f"Продавец {self.name} хочет добавить товар")
                self.site.askAdmin(good)
            else:
                good = self.site.search()
                good = good[random.randint(0, len(good)-1)]
                print(f"Продавец {self.name} хочет удалить товар")
                self.site.removeGood(good)


