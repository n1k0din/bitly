import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


load_dotenv()

BITLY_TOKEN = os.getenv('BITLY_TOKEN')
BITLY_API_URL = 'https://api-ssl.bitly.com/v4'


def create_argument_parser():
    parser = argparse.ArgumentParser(description='Сокращает ссылку или выдает \
        количество кликов по битлинку')
    parser.add_argument('url', help='URL для обработки')

    return parser


def create_auth_headers(token):
    return {'Authorization': f'Bearer {token}'}


def remove_scheme_from_url(url):
    parsed = urlparse(url)
    return parsed._replace(scheme='').geturl()


def is_bitlink(token, url):
    headers = create_auth_headers(token)

    stripped_url = remove_scheme_from_url(url)

    bitlink_info_method = f'/bitlinks/{stripped_url}'
    bitlink_info_url = f'{BITLY_API_URL}{bitlink_info_method}'

    response = requests.get(bitlink_info_url, headers=headers)

    return response.ok


def shorten_link(token, url):
    headers = create_auth_headers(token)

    shorten_method = '/shorten'
    shorten_url = f'{BITLY_API_URL}{shorten_method}'

    payload = {'long_url': url}

    response = requests.post(shorten_url, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()['link']


def count_clicks(token, bitlink):
    headers = create_auth_headers(token)

    stripped_url = remove_scheme_from_url(bitlink)

    count_clicks_method = f'/bitlinks/{stripped_url}/clicks/summary'
    count_clicks_url = f'{BITLY_API_URL}{count_clicks_method}'

    params = {'units': -1}

    response = requests.get(count_clicks_url, headers=headers, params=params)
    response.raise_for_status()

    return response.json()['total_clicks']


def process_url(token, url):
    if is_bitlink(token, url):
        try:
            clicks_amount = count_clicks(token, url)
        except requests.exceptions.HTTPError:
            return 'Кажется, нет такой ссылки'

        return f'Количество кликов: {clicks_amount}'

    try:
        bitlink = shorten_link(token, url)
    except requests.exceptions.HTTPError as e:
        return f'{e}\nНе удалось получить сокращенную ссылку, проверьте ввод'

    return f'{bitlink}'


def main():
    arg_parser = create_argument_parser()
    user_link = arg_parser.parse_args().url

    print(process_url(BITLY_TOKEN, user_link))


if __name__ == '__main__':
    main()
