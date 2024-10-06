"""Клас TestManager:
    Метод __ініціалізації__():
        self.creator = TestCreator()  // Створення об'єкта TestCreator
        self.taker = TestTaker()  // Створення об'єкта TestAttempt
        self.current_user = None  // Користувач ще не залогінений

    Метод register():
        username = отримати_ім'я_користувача()
        User.register_user(username)  // Реєстрація нового користувача
        відобразити_повідомлення("Користувача зареєстровано.")

    Метод login():
        username = отримати_ім'я_користувача()
        user = User.load_user(username)  // Завантажити дані користувача
        Якщо усе вірно:
            self.current_user = user
            Вивести відповідні повідомлення, про успішність виконання або ж неуспішність

    Метод user_actions():
        Якщо self.current_user == None:
            Вивести повідомленні про те, що треба увійти або зареєструватися в системі

           Вивести_вікно_доступних_дій()

    Метод create_test(test_name, questions):
        self.creator.add_test(test_name, questions)  // Додати тест через TestCreator
        Відобразити_повідомлення("Тест '{test_name}' успішно створено.")

Метод create_test():
    test_name = отримати_назву_тесту
    test_type = запитати_тип_тесту()  // вибір типу теста
    questions = отримати_запитання()
    self.creator.add_test(test_name, questions, test_type)  // Створення тесту за допомогою TestCreator

    Метод view_progress():
        progress = self.taker.get_progress(self.current_user)  // Отримати прогрес через TestAttempt
        відобразити_результати(progress)

    Метод load_tests(filename):
        self.creator.load_tests(filename)  // Завантажити тести з файлу

