products = {
    100: {"name": "Americano", "price": 125},
    200: {"name": "Brewed Coffee", "price": 100},
    300: {"name": "Cappuccino", "price": 120},
    400: {"name": "Espresso", "price": 120},
    500: {"name": "Latte", "price": 140},
    600: {"name": "Cold Brew", "price": 200},
    1000: {"name": "Tiramisu", "price": 150},
    1100: {"name": "Red Velvet", "price": 130},
    1200: {"name": "Mango Cream Pie", "price": 200}
}


def get_product(code):
    return products[code]


def get_products():
    product_list = []

    for i, v in products.items():
        product = v
        product.setdefault("code", i)
        product_list.append(product)
    return product_list



branches = {
    1: {"name": "Katipunan", "phonenumber": "09278351144"},
    2: {"name": "Tomas Morato", "phonenumber": "09178516673"},
    3: {"name": "Eastwood", "phonenumber": "09066923785"},
    4: {"name": "Tiendesitas", "phonenumber": "09987716564"},
    5: {"name": "Arcovia", "phonenumber": "09175417540"},
}


def get_branch(code):
    return branches[code]


def get_branches():
    branch_list = []
    for i, v in branches.items():
        branch = v
        branch.setdefault("code", i)
        branch_list.append(branch)
    return branch_list


users = {
    "Caitlynn":{"password":"MoonSun",
                         "first_name":"Caitlynn",
                         "last_name":"Liam"},
    "Trey":{"password":"MoonSun",
                         "first_name":"Travis",
                         "last_name":"Novales"},
    "Reg":{"password":"MoonSun",
                         "first_name":"Regina",
                         "last_name":"See"},
}


def get_user(username):
    try:
        return users[username]
    except KeyError:
        return None