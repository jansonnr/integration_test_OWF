from tests.context import TestContext

VALID_REGISTER_DATA = [TestContext.from_dict({
    "register": {"email": "test1@yahoo.com",
                 "password": "Test123456",
                 "confirmPassword": "Test123456",
                 "lastName": "Иванов",
                 "firstName": "Алексей",
                 "patronymic": "Вячеславочич",
                 "phoneNumber": "+79999999999"},
    "login": {"email": "test1@yahoo.com",
              "password": "Test123456"}}),
    TestContext.from_dict({
        "register": {"email": "test2@yahoo.com",
                     "password": "Test123456",
                     "confirmPassword": "Test123456",
                     "lastName": "Иванов",
                     "firstName": "Алексей",
                     "phoneNumber": "+79999999999"},
        "login": {"email": "test2@yahoo.com",
                  "password": "Test123456"}})]


