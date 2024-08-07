

def item_image_path(instance, filename):
    return f'images/items/{instance.uuid}_{filename}'


def category_image_path(instance, filename):
    return f'images/categories/{instance.uuid}_{filename}'
