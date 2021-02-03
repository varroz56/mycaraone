import django_filters
from .models import Motorhome

# choice filed declaration
CATEGORY_CHOICES = (
    ('BASIC', 'Basic'),
    ('COMFORT', 'Comfort'),
    ('PREMIUM', 'Premium'),
)

GROUP_CHOICES = (
    ('SINGLE', 'Single'),
    ('COUPLE', 'Couple'),
    ('FAMILY', 'Family'),
)


class MotorhomeFilter(django_filters.FilterSet):
    """ using django_filters to render the filtered motorhome results in the motorhome view """
    # daily rental fee search for less tahn or equal results
    daily_rental_fee__lte = django_filters.NumberFilter(
        field_name="daily_rental_fee", lookup_expr='lte')
    # seats and berths to be gte
    seats__gte = django_filters.NumberFilter(
        field_name="seats", lookup_expr='gte')
    persons_to_sleep__gte = django_filters.NumberFilter(
        field_name="persons_to_sleep", lookup_expr='gte')

    class Meta:
        model = Motorhome
        fields = ['category', 'good_for_groups']
