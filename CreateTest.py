"""Клас TestCreator:
    Метод __ініціалізації__():
        self.tests = []  // Список для зберігання тестів

    Метод add_test(test_name, questions, test_type):
        новий_test = {
            'name': test_name,  // Назва тесту
            'questions': questions,  // Список запитань
            'type': test_type  // Тип тесту (тест або вікторина)
        }
        self.tests.append(новий_test)  // Додати тест до списку
        self.save_tests()// Зберегти тести в бінарному файлі

    Метод save_tests():
        with open("tests.dat", "wb") as file:
            pickle.dump(self.tests, file)

    Метод load_tests(filename):
        // Логіка для завантаження тестів з бінарного файлу
