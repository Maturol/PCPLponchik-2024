import main
import unittest

class ClassTest(unittest.TestCase):
    def test_first(self):
        test_list_1 = [main.Document(1, "Документ о медведях"), main.Document(2, "Библиотека"), main.Document(3, "Наука")]
        test_list_2 = [main.Chapter(1, 10, "Примечание", 1), main.Chapter(2, 12, "Книга", 2), main.Chapter(3, 5, "Физика", 3)]
        self.assertEqual(main.first_task(test_list_1, test_list_2), [(d, list(filter(lambda i: i.documentID == d.documentID, test_list_2))) for d in test_list_1 if ("Документ" in d.name)])
    
    def test_second(self):
        test_list_1 = [main.Document(1, "Скульптинг"), main.Document(2, "Эксперимент 2"), main.Document(3, "Виноград")]
        test_list_2 = [main.Chapter(1, 12, "Анатомия головы", 1), main.Chapter(2, 5, "Результаты", 2), main.Chapter(3, 9, "Цвет", 3)]
        self.assertEqual(main.second_task(test_list_1, test_list_2), [("Скульптинг", 12), ("Виноград", 9), ("Эксперимент 2", 5)])

    def test_third(self):
        test_list = [("Марс", 5, "Планеты"), ("Земля", 3, "Планеты"), ("Мел", 2, "Изобразительное искусство")]
        self.assertEqual(main.third_task(test_list), [("Марс", "Планеты"), ("Мел", "Изобразительное искусство")])

if __name__ == '__main__':
    unittest.main()