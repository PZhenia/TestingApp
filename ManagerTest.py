import pickle
import os
from user import User  # Імпорт класу User
from test import Test  # Імпорт класу Test

USERS_FILE = 'users.dat'
TESTS_FILE = 'tests.dat'

# Абстрактний базовий клас для зберігання даних
class DataManager:
    def load_data(self, filename, default):
        raise NotImplementedError("Method must be implemented in subclasses")

    def save_data(self, filename, data):
        raise NotImplementedError("Method must be implemented in subclasses")

# Клас для роботи з користувачами
class UserDataManager(DataManager):
    def load_data(self, filename, default):
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                return pickle.load(f)
        return default

    def save_data(self, filename, data):
        with open(filename, 'wb') as f:
            pickle.dump(data, f)

# Клас для роботи з тестами
class TestDataManager(DataManager):
    def load_data(self, filename, default):
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                return pickle.load(f)
        return default

    def save_data(self, filename, data):
        with open(filename, 'wb') as f:
            pickle.dump(data, f)

class ManagerTest:
    def __init__(self):
        self.user_manager = UserDataManager()  # Використовуємо UserDataManager для роботи з користувачами
        self.test_manager = TestDataManager()  # Використовуємо TestDataManager для роботи з тестами
        
        # Завантажуємо дані
        self.users = self.user_manager.load_data(USERS_FILE, {})
        self.tests = self.test_manager.load_data(TESTS_FILE, [])
        
        self.load_default_tests()  # Завантажити тести за замовчуванням при ініціалізації

    def save_user(self, user):
        self.users[user.username] = user
        self.user_manager.save_data(USERS_FILE, self.users)

    def save_test(self, test):
        self.tests.append(test)
        self.test_manager.save_data(TESTS_FILE, self.tests)

    def load_default_tests(self):
        # Завантажуємо тести за замовчуванням, якщо немає тестів
        if not self.tests:
            for test in DEFAULT_TESTS:
                self.tests.append(test)
            self.test_manager.save_data(TESTS_FILE, self.tests)
