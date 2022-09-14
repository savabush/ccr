from typing import Callable
from core.models import TheNews, TypeNews
from rest_framework.test import APIClient
import pytest


@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture
def data_of_news() -> dict:
    payload = {
        'name': 'test',
        'short_description': 'testtesttesttest',
        'long_description': 'testtesttesttesttesttesttesttesttest'
                            'ttesttesttesttestesttesttesttesttesttesttest',
        'type_of_news': 1
    }
    return payload


@pytest.fixture
def created_news(created_types: Callable) -> None:
    payload = (
        {
            'name': 'test',
            'short_description': 'testtesttesttest',
            'long_description': 'testtesttesttesttesttesttesttesttest'
                                'ttesttesttesttestesttesttesttesttesttesttest',
            'type_of_news': 1
        },
        {
            'name': 'TEST',
            'short_description': 'TETESTSTTESTTEST',
            'long_description': 'TETESTSTTESTTESTTETESTSTTESTTESTTETESTSTTESTTEST'
                                'TETESTSTTESTTESTTETESTSTTESTTESTTETESTSTTESTTEST',
            'type_of_news': 2
        }
    )
    TheNews.objects.bulk_create(payload)


@pytest.fixture
def data_of_type() -> dict:
    payload = {
        'name': 'red',
        'color': '#ff0000'
    }
    return payload


@pytest.fixture
def created_types() -> None:
    payload = (
        {
            'name': 'red',
            'color': '#ff0000'
        },
        {
            'name': 'black',
            'color': '#000000'
        }
    )
    TypeNews.objects.bulk_create(payload)


@pytest.fixture
def id_of_news(created_news: Callable) -> int:
    return TheNews.objects.all().first().id


@pytest.fixture
def id_of_type(created_types: Callable) -> int:
    return TypeNews.objects.all().first().id
