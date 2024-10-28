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