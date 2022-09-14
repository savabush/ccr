from .fixtures import *


class TestStatusCodes:

    @pytest.mark.django_db
    def test_get_status_code_200_of_all_types(
            self,
            client: APIClient,
            created_types: dict
    ) -> None:
        response = client.get('/api/v1/types/')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_all_types(self, client: APIClient) -> None:
        response = client.get('/api/v1/types/')
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_get_status_code_200_of_create_types(
            self,
            client: APIClient,
            data_of_type: dict
    ) -> None:
        response = client.post('/api/v1/types/', data=data_of_type, format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_400_of_create_types(self, client: APIClient) -> None:
        response = client.post('/api/v1/types/')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_get_status_code_200_of_get_types_by_id(
            self,
            client: APIClient,
            id_of_type: dict
    ) -> None:
        response = client.get(f'/api/v1/types/{id_of_type}')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_get_type_by_id(self, client: APIClient) -> None:
        response = client.get('/api/v1/types/1')
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_get_status_code_200_of_update_type(
            self,
            client: APIClient,
            id_of_type: int,
            data_of_type: dict
    ) -> None:
        response = client.put(f'/api/v1/types/{id_of_type}', data=data_of_type, format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_update_type(self, client: APIClient) -> None:
        response = client.put('/api/v1/types/1')
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_get_status_code_200_of_delete_type(
            self,
            client: APIClient,
            id_of_type: int,
            data_of_type: dict
    ) -> None:
        response = client.delete(f'/api/v1/types/{id_of_type}')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_status_code_404_of_delete_type(self, client: APIClient) -> None:
        response = client.delete('/api/v1/types/1')
        assert response.status_code == 404


class TestResponsesData:

    @pytest.mark.django_db
    def test_create_type(self, client: APIClient, data_of_type: dict) -> None:
        response = client.post('/api/v1/test/', data=data_of_type, format='json')
        data = dict(response.data)
        assert data['name'] == data_of_type['name']
        assert data['color'] == data_of_type['color']

    @pytest.mark.django_db
    def test_len_after_create_types(self, client: APIClient, created_types: dict) -> None:
        response = client.get('/api/v1/types/')
        data = response.data
        assert len(data) == 2

    @pytest.mark.django_db
    def test_get_type_by_id(
            self,
            client: APIClient,
            data_of_type: dict,
            id_of_type: int
    ) -> None:
        response = client.get(f'/api/v1/types/{id_of_type}')
        data = response.data
        assert data['name'] == data_of_type['name']
        assert data['color'] == data_of_type['color']

    @pytest.mark.django_db
    def test_update_type_by_id(
            self,
            client: APIClient,
            data_of_type: dict,
            id_of_type: int
    ) -> None:
        response = client.put(f'/api/v1/types/{id_of_type}', data=data_of_type, format='json')
        data = response.data
        assert data['name'] == data_of_type['name']
        assert data['color'] == data_of_type['color']
