import django_filters
from django.contrib.auth import get_user_model


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(name='username', lookup_expr='icontains')

    class Meta:
        model = get_user_model()
        fields = ['username']
