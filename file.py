import requests
from urllib.parse import urlsplit

# 37.677751 55.75771

def requests_image(file_url):
    i = requests.get(file_url)
    if i.status_code == requests.codes.ok:
        with open(str(file_url[:25] + '.png'), 'wb') as file:
            file.write(i.content)
        return "Запрос успешно выполнен"
    else:
        return "Не удалось выполнить запрос :("


print('Введите координаты местности, два действительных числа через пробел:')
l, d = map(float, input().split())
print('Введите масштаб, вещественное число от 100 до 90000:')
m = float(input())

static_request = "https://static-maps.yandex.ru/1.x/?ll={},{}&spn={},{}&l=map".format(
    d, l, 90 / m, 90 / m)
print(static_request)
print(requests_image(static_request))
