from events.models import Event
from templates.models import Template
from users.models import User
import redis
import json
import logging
import os
from notification import notification_service

redis_client = redis.from_url("redis://localhost:6379/0")

while True:
    payload = redis_client.brpopl('payloads', 0)
    if not payload:
        continue
    payload = json.loads(payload[1].decode())
    redis_client.set('lock', 'acquired', ex=30)
    try:
        event = Event.objects.get(pk=payload['event'])
        template = Template.objects.get(pk=payload['template'])
        users = User.objects.filter(pk__in=payload['users'])
    except (Event.DoesNotExist, Template.DoesNotExist, User.DoesNotExist):
        logging.exception('One of the required objects does not exist')
        redis_client.delete('lock')
        continue
    if event.real_time:
        try:
            notification_service.trigger_notification(event, template, users)
        except Exception as e:
            logging.exception('Failed to trigger notification')
            redis_client.lpush('payloads_dlq', json.dumps(payload))
            continue
        else:
            redis_client.delete('lock')
            continue
    else:
        try:
            notification_service.trigger_notification(event, template, users)
        except Exception as e:
            logging.exception('Failed to trigger notification')
            redis_client.lpush('payloads_dlq', json.dumps(payload))
    redis_client.delete('lock')
