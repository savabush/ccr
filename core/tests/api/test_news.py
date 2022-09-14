from .fixtures import *


class TestStatusCodes:

    @pytest.mark.django_db
    def test_get_status_code_200_of_all_news(
            self,
            client: APIClient,
            created_news: dict
    ) -> None:
        response = client.get('/api/v1/news/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_all_news(self, client: APIClient) -> None:
        response = client.get('/api/v1/news/')
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_get_status_code_200_of_create_news(
            self,
            client: APIClient,
            data_of_news: dict
    ) -> None:
        response = client.post('/api/v1/news/', data=data_of_news)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_400_of_create_news(self, client: APIClient) -> None:
        response = client.post('/api/v1/news/')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_get_status_code_200_of_get_news_by_id(
            self,
            client: APIClient,
            id_of_news: int
    ) -> None:
        response = client.get(f'/api/v1/news/{id_of_news}')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_get_news_by_id(self, client: APIClient) -> None:
        response = client.get('/api/v1/news/1')
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_get_status_code_200_of_update_news(
            self,
            client: APIClient,
            id_of_news: int,
            data_of_news: dict
    ) -> None:
        response = client.put(f'/api/v1/news/{id_of_news}', data=data_of_news)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_update_news(self, client: APIClient) -> None:
        response = client.put('/api/v1/news/1')
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_get_status_code_200_of_delete_news(
            self,
            client: APIClient,
            id_of_news: int,
            data_of_news: dict
    ) -> None:
        response = client.delete(f'/api/v1/news/{id_of_news}')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_delete_news(self, client: APIClient) -> None:
        response = client.delete('/api/v1news/1')
        assert response.status_code == 404


class TestResponsesData:

    @pytest.mark.django_db
    def test_create_news(self, client: APIClient, data_of_news: dict) -> None:
        response = client.post('/api/v1/news/', data=data_of_news)
        data = response.data
        assert data == data_of_news

    @pytest.mark.django_db
    def test_len_after_create_news(self, client: APIClient, created_news: dict) -> None:
        response = client.get('/api/v1/news/')
        data = response.data
        assert len(data) == 2

    @pytest.mark.django_db
    def test_len_after_create_news_with_query_params(
            self,
            client: APIClient,
            created_news: dict
    ) -> None:
        response = client.get('/api/v1/news?type=red')
        data = response.data
        assert len(data) == 1

    @pytest.mark.django_db
    def test_get_news_by_id(
            self, client: APIClient,
            data_of_news: dict,
            id_of_news: int
    ) -> None:
        response = client.get(f'/api/v1/news/{id_of_news}')
        data = response.data
        assert data['name'] == data_of_news['name']
        assert data['short_description'] == data_of_news['short_description']
        assert data['long_description'] == data_of_news['long_description']
        assert data['type_of_news'] == data_of_news['type_of_news']

    @pytest.mark.django_db
    def test_update_news_by_id(
            self, client: APIClient,
            data_of_news: dict,
            id_of_news: int
    ) -> None:
        response = client.put(f'/api/v1/news/{id_of_news}', data=data_of_news)
        data = response.data
        assert data['name'] == data_of_news['name']
        assert data['short_description'] == data_of_news['short_description']
        assert data['long_description'] == data_of_news['long_description']
        assert data['type_of_news'] == data_of_news['type_of_news']
