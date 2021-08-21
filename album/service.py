from django_filters import rest_framework as filters
from .models import Albums

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
	pass


class AlbumsFilter(filters.FilterSet):
	tags = CharFilterInFilter(field_name='tag__name', lookup_expr='in')
	year = filters.RangeFilter()

	class Meta:
		model = Albums
		fields = ['tags', 'year']