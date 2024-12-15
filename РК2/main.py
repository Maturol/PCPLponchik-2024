from operator import itemgetter

class Chapter: # Раздел

    def __init__(self, chapterID: int, num_of_pages: int, name: str, documentID: int):
        self.chapterID = chapterID
        self.num_of_pages = num_of_pages # Количество страниц в разделе
        self.name = name # Название раздела
        self.documentID = documentID

    def __repr__(self) -> str: return self.name

class Document: #Документ

    def __init__(self, documentID: int, name: str):
        self.documentID = documentID
        self.name = name # Название документа

    def __repr__(self) -> str: return self.name

class ChaDoc:

    def __init__(self, chapterID: int, documentID: int):
        self.chapterID = chapterID
        self.documentID = documentID


# Списки объектов классов
Documents = [
    Document(1, "Документ о исследовании влияния изменений климата на биоразнообразие"),
    Document(2, "Бизнес-план открытия кофейни"),
    Document(3, "Учебный план по предмету 'История искусств"),
    Document(4, "Договор аренды недвижимости"),
    Document(5, "Документ о изучении микробиома человека")
]

Chapters = [
    Chapter(1, 5, "Методология", 1),
    Chapter(2, 8, "Результаты и обсуждения", 1),
    Chapter(3, 2, "Заключение", 1),
    Chapter(4, 4, "Описание компании", 2),
    Chapter(5, 6, "Анализ рынка", 2),
    Chapter(6, 7, "Финансовый план", 2),
    Chapter(7, 10, "Тематический план", 3),
    Chapter(8, 6, "Методические рекомендации", 3),
    Chapter(9, 4, "Список литературы", 3),
    Chapter(10, 3, "Общие положения", 4),
    Chapter(11, 6, "Права и обязанности сторон", 4),
    Chapter(12, 1, "Споры и разногласия", 4),
    Chapter(13, 3, "Введение", 5),
    Chapter(14, 4, "Методология исследования", 5),
    Chapter(15, 5, "Результаты", 5)
]

ChaDocs = [ # Многие ко многим
    ChaDoc(1,1),
    ChaDoc(1,3),
    ChaDoc(1,5),
    ChaDoc(2,2),
    ChaDoc(2,4),
    ChaDoc(3,1),
    ChaDoc(3,3),
    ChaDoc(3,5),
    ChaDoc(4,2),
    ChaDoc(5,3),
    ChaDoc(6,4),
    ChaDoc(7,1),
    ChaDoc(8,4),
    ChaDoc(8,2),
    ChaDoc(9,5),
    ChaDoc(9,3),
    ChaDoc(10,2),
    ChaDoc(11,1),
    ChaDoc(11,4),
    ChaDoc(12,3),
    ChaDoc(13,2),
    ChaDoc(14,5),
    ChaDoc(15,3),
    ChaDoc(15,2)
]

def first_task(Documents, Chapters):
        request1 = [(d, list(filter(lambda i: i.documentID == d.documentID, Chapters)))
                    for d in Documents
                    if ("Документ" in d.name)
                    ]
        return request1

def second_task(Documents, Chapters):
        request2 = []
        for d in Documents:
            d_chapters = list(filter(lambda i: i.documentID == d.documentID, Chapters))
            Ch_count = []
            if (len(d_chapters) > 0):
                Ch_count = [p.num_of_pages for p in d_chapters]
            Ch_av_count = 0
            if(len(Ch_count) > 0):
                Ch_av_count = round(sum(Ch_count) / len(Ch_count), 2)
            request2.append((d.name, Ch_av_count))
        request2.sort(key=itemgetter(1), reverse=True)
        return request2

def third_task(many_to_many):
        request3 = []
        for i in many_to_many:
            if i[0][0] == 'М':
                request3.append((i[0], i[2]))
        return request3

def main():
    one_to_many: list = [(d.name, c.name, c.num_of_pages)
                         for c in Chapters
                         for d in Documents
                         if (c.documentID == d.documentID)
                         ]
    
    many_to_many_temp: list = [(d.name, cd.chapterID, cd.documentID)
                               for d in Documents
                               for cd in ChaDocs
                               if (d.documentID == cd.documentID)
                               ]
    
    many_to_many: list = [(c.name, c.num_of_pages, docname)
                          for docname, chapterID, documentID in many_to_many_temp
                          for c in Chapters
                          if (c.chapterID == chapterID)
                          ]
    
    # Запрос E1
    # Вывести список всех документов, которые имеют в названии "Документ", и для каждого документа - список разделов в нём
    print("\nЗапрос E1\n")
    print(first_task(Documents, Chapters))

    # Запрос E2
    # Вывести список документов со средним количеством страниц в разделах в каждом документе, отсортированных по убыванию
    print ("\nЗапрос E2\n")
    print(second_task(Documents, Chapters))

    # Запрос E3
    # Вывести список разделов, название которых начинается с буквы "М", и названия их документов
    print("\nЗапрос E3\n")
    print(third_task(many_to_many))

if (__name__ == "__main__"):
    main()