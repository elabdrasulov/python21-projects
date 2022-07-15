from urls import urlpatterns
import pprint

while True:
    try:
        url, arg = input(
            "Введите адрес \n(cars/, create/, detail/id, update/id, delete/id, comment/):\n"
            ).split('/')
    except ValueError:
        print('Введите корректный адрес')
        continue

    found = False
    for uri, view in urlpatterns:
        if uri.split("/")[0] == url:
            found = True

            try:
                if arg:
                    pprint.pprint(view(arg))
                else:
                    pprint.pprint(view())
            except Exception as e:
                print(e)

    if not found:
        print("404 Url Not Found")