
class UserRepository:

    def __init__(self, connection):
        self.connection = connection

    def get_users(self) -> list:
        with self.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM users')
            records = cursor.fetchall()

            users = list()
            for row in records:
                users.append({
                    'id': row[0],
                    'first_name': row[1],
                    'last_name': row[2],
                    'patronymic': row[3],
                    'email': row[4],
                    'phone_number': row[5]
                })

            return users
