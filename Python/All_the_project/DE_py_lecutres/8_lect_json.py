import json

# json_file = json.load(f)
# загрузка json из файла и сохранение в dict или list

# json_list = json.loads(json_text)
# загрузка json из строки и сохранение в dict или list

# with open('user.json', 'r', encoding='utf-8') as f:
#     json_file = json.load(f)
#
# print(f'{type(json_file) = }\n{json_file = }')
# print(f'{json_file["name"] = }')
# print(f'{json_file["address"]["geo"] = }')
# print(f'{json_file["email"] = }')

# --------------------------------------------------------------
# json в python
# --------------------------------------------------------------

import json

json_text = """
[
{
    "userId": 1,
    "id": 9,
    "title": "nesciunt iure omnis dolorem tempora et accusantium",
    "body": "consectetur animi nesciunt iure dolore"
},
{
    "userId": 1,
    "id": 10,
    "title": "optio molestias id quia eum",
    "body": "quo et expedita modi cum officia vel magni"
},
{
    "userId": 2,
    "id": 11,
    "title": "et ea vero quia laudantium autem",
    "body": "delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus"
},
{
    "userId": 2,
    "id": 12,
    "title": "in quibusdam tempore odit est dolorem",
    "body": "praesentium quia et ea odit et ea voluptas et"
}
]"""

# print(f'{type(json_text) = }\n{json_text = }')
# json_list = json.loads(json_text)   # loads - load str
# print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list = }')

# --------------------------------------------------------------
# python в json
# --------------------------------------------------------------

import json

# json.dump(my_dict, f)
# сохранение dict или list в файл (которые предварительно открыли для записи) в виде json

# dict_to_json_text = json.dumps(my_dict)
# сохранение dict или list в виде json строки

import json

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование",
                "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}

# print(f'{type(my_dict) = }\n{my_dict = }')
# with open('new_user.json', 'w') as f:
#     json.dump(my_dict, f)       # ensure_ascii=False - для записи без экранирования

# dict_to_json_text = json.dumps(my_dict)                         # "last_name": "\u0421\u043c\u0438\u0442"
# print(f'{type(dict_to_json_text) = }\n{dict_to_json_text}')     # "last_name": "Смит"
#
# dict_to_json_text = json.dumps(my_dict, ensure_ascii=False)
# print(f'{type(dict_to_json_text) = }\n{dict_to_json_text}')

# -----------------------------------
# Доп.параметры
# ----------------------------------

res = json.dumps(my_dict, indent=2,
                 separators=(',', ':'),
                 sort_keys=True)

# indent - форматирование с отступами
# separators - принимает кортеж: символ-разделитель элементов, разделитель ключа и значения.
# sort_keys - отвечает за сортировку ключей по алфавиту.

# По умолчанию - после : - пробел. Его можно убрить и сэкономить место. indent=2 запише не в строку, а более читаемо

# ----------------------------------
import json

a = 'Hello world!'
b = {key: value for key, value in enumerate(a)} # генерация словаря: {0: 'H', 1: 'e', 2: 'l', 3: 'l', 4: 'o', 5: ' ', 6: 'w', 7: 'o', 8: 'r', 9: 'l', 10: 'd', 11: '!'}

c = json.dumps(b, indent=3, separators=(';', '= '))
print(c)
# !!! разделители заменили => это не объект json