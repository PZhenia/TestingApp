class User:
    def __init__(self, username):
        self.username = username      # Ім'я користувача
        self.completed_tests = {}     # Словник: ключ - назва тесту, значення - результат
        self.progress = 0             # Загальний прогрес (наприклад, % успішних тестів)

    def update_progress(self, test_name, score):
        #Оновлює інформацію про пройдені тести і прогрес
        """set self.completed_tests[test_name] to score
        call self._calculate_progress()"""

    def _calculate_progress(self):
        #Метод для розрахунку загального прогресу користувача
        """if self.completed_tests is not empty:
            set total_tests to length of self.completed_tests
            set total_score to sum of values in self.completed_tests
            set self.progress to (total_score / total_tests)
        else:
            set self.progress to 0"""

    def save_user_data(self, file_path):
        #Зберігає дані користувача у бінарний файл
        """open file at file_path in write-binary mode as f
        serialize self and write to f"""

    def load_user_data(file_path):
        #Завантажує дані користувача з бінарного файлу
        """open file at file_path in read-binary mode as f
        return deserialized object from f"""
