
class Catalogue:
    # products = []

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        list_letter = [x for x in self.products if x[0] == first_letter]
        return list_letter

    def __repr__(self):
        sorted_list = sorted(self.products)
        print(f"Items in the {self.name} catalogue:")
        # print(*sorted_list, sep='\n')
        print('\n'.join(sorted_list))


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
