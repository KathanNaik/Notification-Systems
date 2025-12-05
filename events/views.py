import json
from django.http import JsonResponse
from django.views import View
from .models import Event

class EventCRUDView(View):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                event = Event.objects.get(pk=pk)
            except Event.DoesNotExist:
                return JsonResponse(status=404, data={'message': 'Event not found'})
            return JsonResponse(status=200, data={
                'id': event.pk,
                'title': event.title,
                'description': event.description,
            })
        else:
            events = Event.objects.all()
            data = []
            for event in events:
                data.append({
                    'id': event.pk,
                    'title': event.title,
                    'description': event.description,
                })
            return JsonResponse(status=200, data=data)

    def post(self, request):
        data = request.data
        if 'title' not in data or 'description' not in data:
            return JsonResponse(status=400, data={'message': 'title and description are required'})
        event = Event.objects.create(title=data['title'], description=data['description'])
        return JsonResponse(status=201, data={
            'id': event.pk,
            'title': event.title,
            'description': event.description,
        })

    def put(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return JsonResponse(status=404, data={'message': 'Event not found'})
        data = request.data
        if 'title' in data:
            event.title = data['title']
        if 'description' in data:
            event.description = data['description']
        event.save()
        return JsonResponse(status=200, data={
            'id': event.pk,
            'title': event.title,
            'description': event.description,
        })

    def delete(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return JsonResponse(status=404, data={'message': 'Event not found'})
        event.delete()
        return JsonResponse(status=204, data={'message': 'Event deleted'})
