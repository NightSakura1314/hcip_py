import Function._dome_ as t

t.sit()


# print(t.Dog.sit)

# t.Dog.sit

class menu():
    def __int__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


x = menu(1, "西红柿", 20)
y = menu(2, "sadas", 23)
z = menu(3, "sadasd asa fsda", 3124)
caidan = [x, y, z]
for i in caidan:
    print(i.id, i.name, i.price)
