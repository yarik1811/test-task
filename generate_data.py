import json
import random
import uuid


def write_json(file_path: str, data) -> None:
    """
    Запись данных в JSON-файл
    :param file_path: Путь к файлу, в который сохранить данные
    :param data: Данные, которые необходимо сохранить
    :return: None
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def generate_data():
    return {
        '_id': str(uuid.uuid4()),
        'birthday': '01.11.1977', # День Рождения
        'language': 'ru', # Язык на котором предпочтительно говорить с пассажиром
        'gender' : 'f', # пол f(female) - женский, m(male) - мужской
        'avatar': 'http://link.to/image',
        'initials': {
            # Оригинальные
            'international':
                {
                    'name' : 'Natalia',
                    'secondName': 'Arizherovna',
                    'surname' : 'Gamidova',
                },
            # Международные
            'original':
                {
                    'name': 'Наталья',
                    'secondName': 'Арижеровна',
                    'surname': 'Гамидова',
                }
        },
        'documents':
            {
                # ps - внутренний российский паспорт
                'ps': [{
                'number': 'XXXX XXXXXX'
                }],
                # psp - российский международный паспорт
                'psp': [{
                    'number': 'XX-XX-XXXXXXXXX',
                    'expireDate': 100500,
                    'country': 'RUS',
                }]
            },
        # Контактные данные
        'email': 'example@example.com',
        'phone': '+70000000000',
        # Физический адрес проживания
        'address': {
        'country': 'Россия',
        'city': 'Краснодар',
        'state': 'Краснодарский Край',
        'address': 'ул. Пушкина, д.1, кв. 1',
        'zipCode': 350012
        },
        # Данные из бонусной программы
        'status': {
        'id': 842987349234, # id пользователя в бонусной программе
        '2cardNo' : 9999999999, # Номер карты, печатается на физическом носителе у держателя
        'accNo': 10000000, # Номер аккаунта держателя карты
        'level': 'BASIC' # Статус привелегий в бонусной программе
        },
        # Каналы по кототорым можно коммуницировать с пользователями и какие из них подтверждены
        # allowed - разрешён для отправки данных
        # verified - подтвержден, верифицирован
        'channels':
            {
                'email':
                    {
                        'allowed': False,
                        'verified': random.choice([True, False])
                    },
                'sms':
                    {
                        'allowed': False,
                        'verified': random.choice([True, False])
                    },
                'post':
                    {
                        'allowed': False,
                        'verified': random.choice([True, False])
                    },
                'phone':
                    {
                        'allowed': True,
                        'verified': random.choice([True, False])
                    }
        }
    }

data = [generate_data() for _ in range(1000)]

write_json('generated_data.json', data)