from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import TheNews, TypeNews


class NewsSerializer(ModelSerializer):

    class Meta:
        model = TheNews
        fields = '__all__'


class ListNewsSerializer(ModelSerializer):
    name_type = SerializerMethodField(read_only=True)
    color = SerializerMethodField(read_only=True)

    class Meta:
        model = TheNews
        fields = (
            'name',
            'short_description',
            'name_type',
            'color'
        )

    def get_name_type(self, obj: TheNews) -> str:
        return obj.type_of_news.name

    def get_color(self, obj: TheNews) -> str:
        return obj.type_of_news.color


class TypesSerializer(ModelSerializer):

    class Meta:
        model = TypeNews
        fields = '__all__'
