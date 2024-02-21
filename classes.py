class Product:
    name: str
    description: str
    price: float
    amount: int

    def __init__(self, name, description, price, amount):
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount

    @classmethod
    def create_new_prod(cls, new_prod_list):
        new_prod_list: str
        name, description, price, amount = new_prod_list.split(', ')
        return cls(name, description, price, amount)

    @property
    def check_price(self):
        self.price
    @check_price.setter
    def check_price(self, new_price):
        if int(new_price) <= 0:
            print ('Цена введена некорректно')


class Category:
    name: str
    description: str
    product: list

    def __init__(self, name, description, product):
         self.name = name
         self.description = description
         self.__product = product


    def add_product(self, new_prod,new_description, new_price, new_amount):
        new_prod: str
        self.__product.append(Product(name=new_prod,description=new_description,price=new_price, amount=new_amount))
        return self.__product

    @property
    def show_amount_prod(self):
        prod_list = []
        for i in self.__product:
            new_repr = f'{i.name}, {i.price} руб. Остаток: {i.amount} шт.\n'
            prod_list.append(new_repr)
        return prod_list


#Cat1 = Category("Смартфоны", "Смартфоны, как средство не только коммуникации", [Product("Samsung Galaxy C23 Ultra", "Смартфон 2019 года", 80, 120)])
#print(Cat1.add_product("Samsung Galaxy C24 Ultra"))
#Cat1.add_product("Samsung Galaxy C25 Ultra", "Смартфон 2020 года", 100,150 )
#Cat1.add_product("Samsung Galaxy C26 Ultra", "Смартфон 2021 года", 140, 90)
#Cat1.add_product("Samsung Galaxy C27 Ultra","Смартфон 2024 года",50, 250)
#print(vie_prods(Cat1.show_prod(Cat1))
#print(*Cat1.show_amount_prod)
