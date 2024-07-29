from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Налаштування Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_money_store.settings')

app = Celery('the_money_store')

# Завантаження конфігураційних налаштувань
app.config_from_object('django.conf:settings', namespace='CELERY')

# Завантаження задач з файлів задач
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get-crypto-icons-every-minute': {
        'task': 'your_app_name.tasks.get_crypto_icons',
        'schedule': crontab(minute='*/1'),  # Запуск кожну хвилину
    },
}