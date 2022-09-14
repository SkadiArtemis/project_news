from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostCategory, UserCategory


@receiver(m2m_changed, sender=PostCategory)
def message_for_subscribers(sender, instance, created, **kwargs):
    if created:
        for cat in PostCategory.objects.filter(post=instance):
            for subscribe in UserCategory.objects.filter(category=cat.category):
                msg = EmailMultiAlternatives(
                    subject=instance.title,
                    body=instance.contents,
                    from_email='******@yandex.ru',
                    to=[subscribe.subscriber],
                )
                html_content = render_to_string(
                    'templates/subscribe_message.html',
                    {
                        'new': instance,
                        'recipient': subscribe.subscriber
                    }
                )

                msg.attach_alternative(html_content, "text/html")
                msg.send()