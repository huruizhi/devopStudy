import django_filters
from .models import Server
from django.db.models import Q


class ServerFilter(django_filters.FilterSet):
    # hostname = django_filters.CharFilter(name='hostname', lookup_expr='icontains')
    hostname = django_filters.CharFilter(method='search_hostname')

    def search_hostname(self, qs, name, value):
        return qs.filter(Q(hostname__icontains=value) | Q(ip__exact=value))

    class Meta:
        model = Server
        fields = ['hostname']
