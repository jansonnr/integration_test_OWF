from psycopg2.extras import RealDictCursor


class UserRepository:

    def __init__(self, connection):
        self.connection = connection

    def get_users(self) -> list:
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
        return users
