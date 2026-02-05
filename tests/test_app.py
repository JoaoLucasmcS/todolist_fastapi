from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá, mundo!'}  # Assert


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'usertest',
            'email': 'test@test.com',
            'password': 'teste1234',
        },
    )  # Act

    assert response.status_code == HTTPStatus.CREATED  # Assert
    assert response.json() == {
        'username': 'usertest',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')  # Act

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'username': 'usertest', 'email': 'test@test.com', 'id': 1}]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'alice',
            'email': 'alice.souza@teste.com',
            'password': 'senha123',
        },
    )  # Act

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'alice',
        'email': 'alice.souza@teste.com',
        'id': 1,
    }  # Asserts


def test_update_user_deve_retornar_usuario_nao_encontrado(client):
    response = client.put(
        '/users/777',
        json={
            'username': 'alice',
            'email': 'alice.souza@teste.com',
            'password': 'senha123',
        },
    )  # Act

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'user not found'}


def test_get_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice.souza@teste.com',
    }  # Asserts


def test_get_user_deve_retornar_nao_encontrado(client):
    response = client.get('/users/777')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'user not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_deve_retornar_usuario_nao_encontrado(client):
    response = client.delete('/users/777')  # Act

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'user not found'}
