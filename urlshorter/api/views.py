from rest_framework import generics
from . import serializers
from .models import Link


class LinkList(generics.ListCreateAPIView):
    '''ListCreateAPIView gives a common handler of
    API-methods: get и post for the list.
    '''
    serializer_class = serializers.LinkSerializer

    def get_queryset(self):
        queryset = Link.objects.all()
        long_url = self.request.query_params.get('long_url')
        short_url = self.request.query_params.get('short_url')
        if long_url is not None:
            queryset = queryset.filter(long_url=long_url)
        if short_url is not None:
            queryset = queryset.filter(short_url=short_url)
        return queryset


class LinkDetail(generics.RetrieveUpdateDestroyAPIView):
    '''RetrieveUpdateDestroyAPIView gives a common handler of
    API-methods: get, update и delete for one entity.
    '''
    queryset = Link.objects.all()
    serializer_class = serializers.LinkSerializer
