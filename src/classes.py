from abc import ABC, abstractmethod


class BaseProduct(ABC):  # pragma: no cover

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @abstractmethod
    def new_product(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class MixinClass:

    def __repr__(self):
        self.product_log()

    def product_log(self):
        print(f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})")


class Product(MixinClass, BaseProduct):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity
        super().__repr__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):

        if isinstance(self, type(other)):
            sum1 = self.price * self.quantity
            sum2 = other.price * other.quantity
            return sum1 + sum2
        else:
            raise TypeError

    @classmethod
    def new_product(cls, params: dict):
        new_name, new_description, new_price, new_quantity = (
            params["name"],
            params["description"],
            params["price"],
            params["quantity"],
        )
        return cls(new_name, new_description, new_price, new_quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                ans = str(input("Вы ввели цену ниже прошлой, подтвердите изменение цены (y/n,да/нет)"))
                if ans.lower() == "y":
                    self.__price = new_price


class Category:
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = []
        if products:
            for i in products:
                self.add_product(i)
        Category.category_count += 1

    def __str__(self):
        summ = 0
        for i in self.__products:
            summ += i.quantity
        return f"{self.name}, количество продуктов: {summ} шт."

    def add_product(self, product):
        if not isinstance(product, Product) or not issubclass(type(product), Product):
            raise TypeError("Нельзя добавлять объекты не типа Класс")
        else:
            self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        my_list = []
        for i in self.__products:
            my_list.append(f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.\n")
        return my_list

    def middle_price(self):
        try:
            prod_count = len(self.__products)
            summ = 0
            for i in self.__products:
                summ += i.price

            return summ / prod_count
        except:
            return 0


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
