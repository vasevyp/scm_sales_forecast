from django.template.defaultfilters import slugify
# from control.models import StockItem

'''Функция для создания slug из имени на кирилице'''


def do_slug(name):
    my_string = str(name).translate(str.maketrans("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                                                  "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA"))
    slug = slugify(my_string)
    return slug
