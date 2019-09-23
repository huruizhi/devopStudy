"""devopStudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from idc.views import IdcViewSetV7
from users.views import UserViewset
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from cabinet.views import CabinetViewSet
from servers.views import ManufacturerViewSet, ProductViewSet, ServerViewSet, ServerAutoReportViewSet, \
    NetworkDeviceViewSet, IPViewSet


route = DefaultRouter()
route.register("idcs", IdcViewSetV7)
route.register("users", UserViewset)
route.register("cabinet", CabinetViewSet)
route.register("Manufacturer", ManufacturerViewSet)
route.register("Product", ProductViewSet)
route.register("ServerAutoReport", ServerAutoReportViewSet, base_name='ServerAutoReport')
route.register("Server", ServerViewSet, base_name='Server')
route.register("NetworkDevice", NetworkDeviceViewSet)
route.register("IP", IPViewSet)

# route.register("Server", ServerViewSet)

urlpatterns = [
    url('^', include(route.urls)),
    url('^api-auth', include('rest_framework.urls', namespace="rest_framework")),
    url('^docs', include_docs_urls("运维平台接口文档")),
    url('^openapi', get_schema_view(
        title="Your Project",
        description="API for all things"
    ), name='openapi-schema'),
]
