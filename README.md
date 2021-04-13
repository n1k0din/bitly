# Обрезка ссылок с помощью Битли

Консольная утилита для сокращения ссылок с помощью [bit.ly](https://bit.ly).
Умеет сокращать ссылки и сообщать количество переходов по сокращенным ссылкам.

## Установка

### Получите ключ к API

1. Зарегистрируйтесь на [bit.ly](https://bit.ly/).
2. Получите ключ в [генераторе токенов](https://bitly.com/a/oauth_apps).
3. Поместите ключ в файл `.env` в виде.
```
BITLY_TOKEN=ваш_ключ
```

### Подготовка скрипта

1. Скачайте код и перейдите в папку проекта.
    ```bash
    git clone https://github.com/n1k0din/bitly.git
    ```  
    ```bash
    cd bitly
    ```
2. Установите вирт. окружение.
    ```bash
    python -m venv venv
    ```
3. Активируйте.
    ```bash
    venv\Scripts\activate.bat
    ```
    или
    ```bash
    source venv/bin/activate
    ```
4. Установите необходимые пакеты.
    ```bash
    pip install -r requirements.txt
    ```

## Запуск
```
python main.py URL
```

### Примеры

- Сократить ссылку http://ya.ru.
    ```
    python main.py http://ya.ru
    ```

- Получить количество переходов по сокращенной ссылке https://bit.ly/abc123.
    ```
    python main.py https://bit.ly/abc123
    ```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
