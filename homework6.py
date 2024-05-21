my_list = ['banana', 'apple', 'melon', 'strawberry', 'watermelon', 'kiwi', 'orange']
print('Мой список: ', my_list)
print('Первый элемент:', my_list[0], "\nПоследний элемент:", my_list[-1])
print("Подсписок:", my_list[2:5])
my_list[2] = 'peach'
print("Измененный список:", my_list)
print()
my_dict = {"Russia": "Moscow", "UK": "London", "Japan": "Tokyo", "South Korea": "Seoul"}
print("Страны и их столицы",my_dict)
print("Столица Великобритании:",my_dict["UK"])
my_dict["Russia"] = "St. Petersburg"
my_dict.update({"USA" : "Washington"})
print("Найди ошибки:",my_dict)