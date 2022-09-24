from project_news_app.celery import shared_task
import time


@shared_task
def print_screen(n):
    i = 0
    while i < n+1:
        time.sleep(1)
        print(i)
        i += 1
    print('Hello')