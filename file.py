from PIL import Image
import requests
from io import BytesIO

print('Введите координаты местности, два действительных числа через пробел:')
l, d = map(float, input().split())
print('Введите масштаб, вещественное число от 100 до 90000:')
m = float(input())

url = "https://static-maps.yandex.ru/1.x/?ll={},{}&spn={},{}&l=map".format(
    l, d, 90 / m, 90 / m)
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.save("map.png")
