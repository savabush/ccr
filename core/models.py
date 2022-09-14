from django.db import models
from django.core.validators import RegexValidator


class TypeNews(models.Model):

    color_validator = RegexValidator(
        regex=r'#[A-Z\d]+',
        message="The color of type in the format #XXXXXX "
                "(X - number from 0 to 9 or capital letters from A to Z)"
    )

    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7,  validators=[color_validator], unique=True)

    def __str__(self) -> models.CharField:
        return self.name


class TheNews(models.Model):

    name = models.CharField(max_length=50)
    short_description = models.TextField(max_length=50)
    long_description = models.TextField(max_length=1000)
    type_of_news = models.ForeignKey(TypeNews, related_name='news', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self) -> models.CharField:
        return self.name
