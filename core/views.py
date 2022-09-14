from typing import Union, Type
from django.db.models import QuerySet
from django.utils.decorators import method_decorator
from rest_framework.viewsets import ModelViewSet
from .models import TheNews, TypeNews
from .serializers import NewsSerializer, TypesSerializer, ListNewsSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

type_of_news = openapi.Parameter(
    name='type',
    in_=openapi.IN_QUERY,
    description='Type of News',
    type=openapi.TYPE_STRING
)


@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        manual_parameters=[type_of_news]
    )
)
class TheNewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = TheNews.objects.all()

    def get_serializer_class(self) -> Union[Type[ListNewsSerializer], Type[NewsSerializer]]:
        if self.action == 'list':
            return ListNewsSerializer
        return self.serializer_class

    def get_queryset(self) -> QuerySet:
        if self.action == 'list':
            if type_news := self.request.query_params.get('type'):
                return TheNews.objects.select_related('type_of_news')\
                    .filter(type_of_news__name=type_news)
            return TheNews.objects.select_related('type_of_news').all()
        return self.queryset


class TypeNewsViewSet(ModelViewSet):
    serializer_class = TypesSerializer
    queryset = TypeNews.objects.all()
