from pprint import pprint

class Product:
    name = str # Атрибут name - название продукта(строка)
    weight = float # Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.)
    category = str # Атрибут category - категория товара (строка).
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt' # Инкапсулированный атрибут __file_name = 'products.txt'
    def __init__(self):
        self.__file_name = open('products.txt')
        self.__file_name.close()

    def get_products(self):
        file = open('products.txt', 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        for product in products:
            if str(product) not in self.get_products():
                file = open('products.txt', 'a')
                file.write(product.__str__() + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())