# from shop.models import Product, Category
# from shop.views import product_create, product_delete, product_detail, product_list, product_update

# cat = Category("phones")
# Category("dyson")
# Category("food")
# obj1 = Product("iphone", 234, "...", 3, cat)
# obj2 = Product("lenovo", 32, "...", 5, cat)
# obj3 = Product("samsung", 76, "...", 10, cat)

# from pprint import pprint
# # pprint(product_create())
# pprint(product_list())
# id_ = input("Введите продукт для обновления: ")
# pprint(product_update(id_))
# # pprint(product_list())
# # while True:
# #     id_ = input("Введите id продукта: ")
# #     pprint(product_detail(id_))

from urls import urlpatterns
from pprint import pprint

while True:
    try:
        url, arg = input("Введите адрес: ").split('/')
    except ValueError:
        print('Enter a valid url')
        continue

    found = False
    for uri, view in urlpatterns:
        # print("url =", url, "uri =", uri)
        if uri.split('/')[0] == url:
            found = True
            
            try:
                if arg:
                    pprint(view(arg))
                else:
                    pprint(view())
            except Exception as e:
                print(e)

    if not found:
        print("404 Url Not Found")

