from django.shortcuts import render

# Create your views here.
from .models import Idc
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import IdcSerializer
from rest_framework.reverse import reverse


@api_view(["GET", "POST"])
def idc_list(request, *args, **kwargs):
    if request.method == "GET":
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = IdcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT"])
def idc_detail(request, pk, *args, **kwargs):
    try:
        queryset = Idc.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = IdcSerializer(queryset)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = IdcSerializer(queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def api_root(request, format=None, *args, **kwargs):
    if request.method == "GET":
        return Response({
            "idcs": reverse('idc_list', request=request, format=format),
            # "idc_detail": reverse('idc_detail', 2, request=request, format=format)
        })

# ############# 版本3 ############


from rest_framework.views import APIView


class IdcList(APIView):
    def get(self, request, format=None):
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IdcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


from django.http import Http404


class IdcDetail(APIView):

    def get_obj(self, pk):
        try:
            Idc_obj = Idc.objects.get(pk=pk)
            return Idc_obj
        except Idc.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_obj(pk)
        serializer = IdcSerializer(queryset)
        return Response(serializer.data)

    def post(self, request, pk, format=None):

        queryset = self.get_obj(pk)
        serializer = IdcSerializer(queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_obj(pk)
        queryset.delete()
        return Response(status.HTTP_204_NO_CONTENT)


# ################ 版本4 ################

from rest_framework import mixins, generics


class IdcListV4(generics.GenericAPIView,
               mixins.ListModelMixin,
               mixins.CreateModelMixin):

    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class IdcDetailV4(generics.GenericAPIView,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):

    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# ################ 版本5 ################

class IdcListV5(generics.ListCreateAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer


class IdcDetailV5(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

# ################ 版本6 ################


from rest_framework import viewsets


class IdcListV6(viewsets.GenericViewSet,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                mixins.CreateModelMixin
                ):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer


# ################ 版本7 ################


from rest_framework import viewsets


class IdcViewSetV7(viewsets.ModelViewSet):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
