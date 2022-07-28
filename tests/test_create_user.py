import pytest

from test_data.Identity_data import VALID_REGISTER_DATA
from test_logic.db_sort import DBSort


@pytest.mark.incremental
@pytest.mark.usefixtures('http_client', 'db_connect', 'del_user_bd')
@pytest.mark.parametrize('valid_register_data', VALID_REGISTER_DATA, scope="class")
class TestSuccessCreateUser:

    def test_register(self, http_client, valid_register_data):
        # Act
        register_response = http_client.register(valid_register_data.get('register'))

        # Assert
        assert register_response.status_code == 200

    def test_login(self, http_client, valid_register_data):
        # Act
        register_response = http_client.login(valid_register_data.get('login'))

        # Assert
        assert register_response.status_code == 200

    def test_get_user_data(self, db_connect, valid_register_data):
        '''users = db_connect.get_users()
        user = register_data.get_dict
        assert DBSort().chek_user(users, user('email'))'''
