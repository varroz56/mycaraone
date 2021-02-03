import django_filters

from .models import Booking


class BookingDatesFilter(django_filters.FilterSet):
    """ This is to filter bookings by start and end date """

    """ using django_filters to render the filtered motorhome results in the motorhome view """
    # # daily rental fee search for less tahn or equal results
    # booked_from__lte = django_filters.NumberFilter(
    #     field_name="booked_from", lookup_expr='lte')
    # # seats and berths to be gte
    # booked_until__gte = django_filters.NumberFilter(
    #     field_name="booked_until", lookup_expr='gte')
    date_range = django_filters.DateFromToRangeFilter(field_name='date_range')
    class Meta:
        model = Booking
        exclude = '__all__'