import settings
import requests
import os
import json

cookie = os.getenv("COOKIE")
users = os.getenv("USER_FILE")


def save_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def run_bot(url, user_file, headers):
    data = []
    headers['Cookie'] = cookie
    for user in open(user_file).readlines():
        response = requests.get(url.format(user_id=user), headers=headers)
        users_dict = {
            'username': response.json().get('user').get('username'),
            'biography': response.json().get('user').get('biography'),
            'follower_count': response.json().get('user').get('follower_count')
        }
        data.append(users_dict)
        save_json(data, 'users_data.json')


if __name__ == '__main__':
    run_bot(settings.URL, users, settings.HEADERS)
