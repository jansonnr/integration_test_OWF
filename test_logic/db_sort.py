class DBSort:
    def chek_user(self, users: list, email: str):
        users_for_assert = []
        for user in users:
            users_for_assert.append(user.get('email'))
        if email in users_for_assert:
            return True
        else:
            return False
