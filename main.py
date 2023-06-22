from Goods import Cart, Good
from Actors import Customer, Seller, Administrator
from Server import Site, Server

if __name__ == '__main__':
    server = Server()
    seller = Seller(4, "Иван",  server)
    customer = Customer(10000, "2002047463848274", "Андрей", "Москва")
    admin = Administrator(2000, "2002047396848029", "Анастасия", "Нижневартовск", 2000, server)

    admin.doSomething()
    customer.doSomething(server)
    seller.doSomething()

