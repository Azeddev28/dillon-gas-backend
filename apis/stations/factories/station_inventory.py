import factory
import factory.fuzzy

from apis.inventory.models import Item
from apis.stations.models import StationInventoryItem

class StationInventoryItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StationInventoryItem

    item = factory.fuzzy.FuzzyChoice(Item.objects.all())
    quantity = factory.fuzzy.FuzzyInteger(1, 9)
    price = factory.fuzzy.FuzzyInteger(100, 900)
