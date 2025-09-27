import json
import os


def read_json(file_path: str) -> dict:
    """
    Чтение JSON-файла в dict
    :param file_path: Путь к json-файлу
    :return: Словарь с данными данные из json-файла
    """
    if file_path not in os.listdir('.'):
        print(f'Файл {file_path} не найден в текущей директории')
        return {}
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json(file_path: str, data) -> None:
    """
    Запись данных в JSON-файл
    :param file_path: Путь к файлу, в который сохранить данные
    :param data: Данные, которые необходимо сохранить
    :return: None
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def get_problem_data(users_uids: list, families: dict) -> tuple[list, list]:
    """
    Извлечение проблемных данных
    :param users_uids: Список содержащий _id всех пользователей
    :param families: Список семей
    :return: Структура из списка _id проблемных семей и _id проблемных юзеров
    """

    only_owner = []
    missing_users = []
    for item in families:
        if len(item['participants']) == 0:
            only_owner.append(item['_id'])
            continue
        for participant in item['participants']:
            if participant['participant'] not in users_uids:
                missing_users.append(participant['participant'])

    return only_owner, missing_users



users = read_json('users.json')
users_uids = [u['_id'] for u in users]
families = read_json('families.json')

only_owner, missing_users = get_problem_data(users_uids, families)
write_json('only_owner.json', only_owner)
write_json('missing_users.json', missing_users)

print(f'Всего юзеров: {len(users)}')
print(f'Всего семей: {len(families)}\n'
      f'Семей состоящих только из владельца: {len(only_owner)}\n'
      f'Участников семей отсутствующих в users.json: {len(missing_users)}')



