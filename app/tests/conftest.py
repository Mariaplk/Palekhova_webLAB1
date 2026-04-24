from datetime import datetime
from contextlib import contextmanager

import pytest
from flask import template_rendered

from app import app as application


@pytest.fixture
def app():
    return application


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
@contextmanager
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)

    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


@pytest.fixture
def posts_list():
    return [
        {
            'title': 'Заголовок тестового поста',
            'text': 'Текст тестового поста',
            'author': 'Иванов Иван Иванович',
            'date': datetime(2025, 3, 10),
            'image_id': '123.jpg',
            'comments': [
                {
                    'author': 'Петров Петр Петрович',
                    'text': 'Первый комментарий',
                    'replies': [
                        {
                            'author': 'Сидоров Сидор Сидорович',
                            'text': 'Ответ на комментарий',
                            'replies': []
                        }
                    ]
                }
            ]
        }
    ]
