from xml.etree import ElementTree as ET

from django.utils.safestring import mark_safe
from django import template
from django.conf import settings

register = template.Library()


@register.filter(name="mail_to")
def mail_to(input_str):
    """
    Create link `mailto:`
    """
    link_mailto = ET.Element("a", {"href": f"mailto:{input_str}"})
    link_mailto.text = input_str
    return mark_safe(ET.tostring(link_mailto, encoding="unicode"))


def media_folder_products(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам продуктов
    products_images/product1.jpg --> /media/products_images/product1.jpg
    """
    if not string:
        string = 'products_images/default.jpg'

    return f'{settings.MEDIA_URL}{string}'


@register.filter(name='media_folder_users')
def media_folder_users(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам пользователей
    users_avatars/user1.jpg --> /media/users_avatars/user1.jpg
    """
    if not string:
        string = 'users_avatars/default.jpg'

    return f'{settings.MEDIA_URL}{string}'

register.filter('media_folder_products', media_folder_products)

# Or you can register tag like this
# register.filter("mail_to", mail_to)