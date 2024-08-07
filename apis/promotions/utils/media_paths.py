from uuid import uuid4


def promotion_image_path(instance, filename):
    return f'images/promotions/{instance.uuid}/{uuid4()}_{filename}'
