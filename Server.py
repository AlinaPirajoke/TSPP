import random
from Goods import Cart, Good


class Site():

    def __init__(self, server):
        self.server = server

    def search(self):
        print("Поиск товаров...")
        goods = self.server.searchGoods()
        self.showGoods()
        return goods

    def showGoods(self):
        print("Товары показаны")

    def filterArray(self):
        print("Товары отсортированны")

    def sortArray(self):
        print("Товары упорядоченны")

    def askQuestion(self, question):
        answer = self.server.redirectQues(question)
        print("Доставка вопроса")
        return answer

    def showQuestion(self, seller, question):
        return seller.answerOnQuestion(question)

    def addToCart(self, good, customer):
        self.server.addToCart(good, customer)

    def buyGoods(self, customer):
        self.server.buyGoods(customer)

    def sellersPage(self, seller, order):
        return seller.collectOrder(order)

    def editConfig(self):
        print("Произошло изменение сайта")

    def askAdmin(self, good):
        if len(self.server.admins) == 0:
            return "Нет свободных администраторов"
        else:
            return self.server.admins[random.randint(0, len(self.server.admins)-1)].addGood(good)

    def removeGood(self, good):
        self.server.removeGood(good)


class Server():
    customers = []
    sellers = []
    admins = []
    carts = []
    goods = []

    def __init__(self):
        self.site = Site(self)
        self.readGoods()

    def readGoods(self):
        f = open("goods.txt")
        gl = f.readlines()
        f.close()
        for g in gl:
            self.goods.append(Good(g.split(", ")))

    def addGood(self, good):
        self.goods.append(good)
        print(f"В систему был добавлен товар под номером {good.id}")

    def showSite(self):
        return self.site

    def removeGood(self, good):
        self.goods.remove(good)
        print(f"Из системы был удалён товар под номером {good.id}")

    def addCustomer(self, new):
        print(f"В систему вошёл клиент {new.name}")
        self.customers.append(new)

    def addSeller(self, new):
        print(f"В систему вошёл продавец { new.name }")
        self.sellers.append(new)

    def addAdmin(self, new):
        print(f"В систему вошёл администратор {new.name}")
        self.admins.append(new)

    def redirectQues(self, question):
        if len(self.sellers) == 0: return "Нет свободных консультантов"
        else:
            return self.sellers[random.randint(0, len(self.sellers)-1)].answerOnQuestion(question)

    def addToCart(self, good, customer):
        for i in self.carts:
            if i.customer == customer:
                i.addGood(good)
                return
        self.carts.append(Cart(customer, good))
        print(f"Товар {good.id} добавлен в корзину {customer.name}")

    def buyGoods(self, customer):
        for i in self.carts:
            if i.customer == customer:
                summ = 0
                for g in i.goods:
                    summ += g.price

                if customer.takeMoney(summ):
                    if len(self.sellers):
                        seller = self.sellers[random.randint(0, len(self.sellers))]
                        order = self.site.sellersPage(seller, i)
                        print("Оплата произведена успешно")
                        return order

                    else: print("Ошибка, нет свободных продавцов")
                    return None

                else:
                    print("Ошибка, у клиента недостаночно денег")
                    return None

    def searchGoods(self):
        print("Производится поиск товаров")
        return self.goods

    def editConfig(self):
        print("Произошло изменение сервера")





