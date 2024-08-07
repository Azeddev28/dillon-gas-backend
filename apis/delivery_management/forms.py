from cities_light import forms
from cities_light.models import City


class DGCityForm(forms.CityForm):
    def save(self, commit):
        if self.cleaned_data.get('delivery_enabled') == True:
            region = self.cleaned_data.get('region')
            region.delivery_enabled = True
            region.save()

        return super().save(commit)


class DGRegionForm(forms.CityForm):
    def save(self, commit):
        if self.cleaned_data.get('delivery_enabled') == True:
            City.objects.filter(region__name=self.cleaned_data.get('name')).update(delivery_enabled=True)

        return super().save(commit)
