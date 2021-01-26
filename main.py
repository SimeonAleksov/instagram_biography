import settings
import requests
import os
import json

cookie = os.getenv("COOKIE")
users = os.getenv("USER_FILE")


def save_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def run_bot(url, user_file, headers, *args, **kwargs):
    data = []
    headers['Cookie'] = cookie
    for user in list(map(int, open(user_file).readlines())):
        response = requests.get(url.format(user_id=user), headers=headers)
        for arg in args:
            users_dict = {
                arg: response.json().get('user').get(arg)
            }
        users_dict = {
            'username': response.json().get('user').get('username'),
            'biography': response.json().get('user').get('biography'),
            'follower_count': response.json().get('user').get('follower_count'),
        }
        for obj in args:
            users_dict.update({
                obj: response.json().get('user').get(obj)
            })
        data.append(users_dict)
        save_json(data, 'users_data.json')


if __name__ == '__main__':
    run_bot(settings.URL, users, settings.HEADERS)
