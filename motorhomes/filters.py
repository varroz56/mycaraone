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
    class Meta:
        model = Motorhome
        fields = ['seats', 'persons_to_sleep', 'daily_rental_fee', 'category', 'good_for_groups']
