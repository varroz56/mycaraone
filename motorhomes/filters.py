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

    class Meta:
        model = Motorhome
        fields = ['seats', 'persons_to_sleep', 'category', 'good_for_groups']
