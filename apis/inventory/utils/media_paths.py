from uuid import uuid4


def item_image_path(instance, filename):
    return f'images/items/{instance.uuid}/{uuid4()}_{filename}'


def category_image_path(instance, filename):
    return f'images/categories/{instance.uuid}/{uuid4()}_{filename}'
