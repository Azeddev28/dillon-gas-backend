import factory
import factory.fuzzy
from apis.inventory.models import Category, Item

class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    name = factory.fuzzy.FuzzyChoice(['Gas Refill', 'Cylinder', 'Engine Oil'])
    category = factory.fuzzy.FuzzyChoice(Category.objects.all())
    bar_code = factory.fuzzy.FuzzyInteger(9000000000, 9999999999)
    description = factory.Faker('catch_phrase')
    weight = factory.fuzzy.FuzzyInteger(1, 9)