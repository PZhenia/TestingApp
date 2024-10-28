import pickle
import os
from user import User  # Імпорт класу User
from test import Test  # Імпорт класу Test

USERS_FILE = 'users.dat'
TESTS_FILE = 'tests.dat'

class ManagerTest:
    def __init__(self):
        self.users = self.load_data(USERS_FILE, {})
        self.tests = self.load_data(TESTS_FILE, [])
        self.load_default_tests()  # Завантажити тести за замовчуванням при ініціалізації

    def load_data(self, filename, default):
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                return pickle.load(f)
        return default

    def save_data(self, filename, data):
        with open(filename, 'wb') as f:
            pickle.dump(data, f)

    def save_user(self, user):
        self.users[user.username] = user
        self.save_data(USERS_FILE, self.users)

    def save_test(self, test):
        self.tests.append(test)
        self.save_data(TESTS_FILE, self.tests)

    def load_default_tests(self):
        if not self.tests:  # Завантажувати тільки, якщо немає тестів
            for test in DEFAULT_TESTS:
                self.tests.append(test)
            self.save_data(TESTS_FILE, self.tests)


