from psycopg2.extras import RealDictCursor


class UserRepository:

    def __init__(self, connection):
        '''

        :param connection: соединение с БД
        '''
        self.connection = connection

    def get_users(self) -> list:
        '''
        Получение списка пользователей из БД в виде словоря, берем всех пользователей
        :return:
        '''
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
        return users

    def delete_users(self):
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM aspnetusers')
        self.connection.commit()
