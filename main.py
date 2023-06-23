from Goods import Cart, Good
from Actors import Customer, Seller, Administrator
from Server import Site, Server

if __name__ == '__main__':
    print("Нажмите, что бы заставить работать:\n"
          "1- Администратор\n"
          "2- Клиент\n"
          "3- Продавец\n")
    server = Server()
    seller = Seller(4, "Иван",  server)
    customer = Customer(10000, "2002047463848274", "Андрей", "Москва")
    admin = Administrator(2000, "2002047396848029", "Анастасия", "Нижневартовск", 2000, server)
    while 1:
        a = int(input("Введите команду:"))
        if a == 1: admin.doSomething()
        elif a == 2: customer.doSomething(server)
        elif a == 3: seller.doSomething()
        else: break

