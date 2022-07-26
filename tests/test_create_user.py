import psycopg2
import pytest

from config import APP_BASE_URL, DB_CONNECTION_PARAMS
from app_driver.owf_http_client import OwfHttpClient
from test_data.create_user import data_create_user
from app_driver.db_users import UserRepository
from tests.context import TestContext


@pytest.mark.parametrize('register_data', data_create_user, scope="class")
class TestSuccessCreateUser:

    def setup_class(self):
        self.client = OwfHttpClient(APP_BASE_URL)
        self.connection = psycopg2.connect(
            dbname=DB_CONNECTION_PARAMS.get('dbname'),
            user=DB_CONNECTION_PARAMS.get('user'),
            password=DB_CONNECTION_PARAMS.get('password'),
            host=DB_CONNECTION_PARAMS.get('host')
        )

        self.user_repository = UserRepository(self.connection)

    def test_register(self, register_data):
        # Act
        register_response = self.client.register(register_data.get('register'))

        # Assert
        assert register_response.status_code == 200

    def test_login (self, register_data ):
        # Act
        register_response = self.client.login(register_data.get('login'))

        # Assert
        assert register_response.status_code == 200

    def test_get_user_data(self, register_data):
        self.user_repository.get_users()

    def test_cleaner_bd(self, register_data):
        self.user_repository.delete_users()

    def teardown_class(self):
        self.connection.close()
