import os, time
from celery import Celery, shared_task
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_app1.settings')

app = Celery('news_app1')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_mon_8am': {
        'task': 'news_app1.tasks.weekly_mailing_tasks',
        'schedule': crontab(hour=8, minute=0, day_of_week='mon'),
    }
}
