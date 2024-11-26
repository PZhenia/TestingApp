class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.progress = UserProgress()

class UserProgress:
    def __init__(self):
        self.test_attempts = {}

    def add_attempt(self, test_title, score):
        if test_title not in self.test_attempts:
            self.test_attempts[test_title] = []
        self.test_attempts[test_title].append(score)

    def view_progress(self):
        return "\n".join([f"{test}: {scores}" for test, scores in self.test_attempts.items()])

    def get_statistics(self):
        total_tests = len(self.test_attempts)
        average_score = (
            sum(sum(scores) for scores in self.test_attempts.values()) / total_tests
            if total_tests > 0 else 0
        )
        return f"Total Tests: {total_tests}, Average Score: {average_score:.2f}"

class BaseUser:
    def __init__(self, username):
        self.username = username
        self.progress = UserProgress()

    def has_access_to_create_tests(self):
        return False  # За замовчуванням, користувачі не мають права створювати тести.

    def get_user_type(self):
        return "Base User"

class StandardUser(BaseUser):
    def __init__(self, username, password):
        super().__init__(username)
        self.password = password

    def has_access_to_create_tests(self):
        return True  # Стандартні користувачі мають доступ до створення тестів.

    def get_user_type(self):
        return "Standard User"

class GuestUser(BaseUser):
    def __init__(self, username="Guest"):
        super().__init__(username)

    def get_user_type(self):
        return "Guest User"

