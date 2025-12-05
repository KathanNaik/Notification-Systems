from django.http import JsonResponse
from django.views import View
from .models import Templates
class TemplateCRUDView(View):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                template = Templates.objects.get(pk=pk)
            except Templates.DoesNotExist:
                return JsonResponse(status=404, data={'message': 'Template not found'})
            return JsonResponse(status=200, data={
                'id': template.pk,
                'name': template.name,
                'content': template.content,
                'event': template.event.pk,
            })
        else:
            templates = Templates.objects.all()
            data = []
            for template in templates:
                data.append({
                    'id': template.pk,
                    'name': template.name,
                    'content': template.content,
                    'event': template.event.pk,
                })
            return JsonResponse(status=200, data=data)

    def post(self, request):
        data = request.data
        if 'name' not in data or 'content' not in data or 'event' not in data:
            return JsonResponse(status=400, data={'message': 'name, content and event are required'})
        try:
            event = Templates.objects.get(pk=data['event'])
        except Templates.DoesNotExist:
            return JsonResponse(status=404, data={'message': 'Event not found'})
        template = Templates.objects.create(name=data['name'], content=data['content'], event=event)
        return JsonResponse(status=201, data={
            'id': template.pk,
            'name': template.name,
            'content': template.content,
            'event': template.event.pk,
        })

    def put(self, request, pk):
        try:
            template = Templates.objects.get(pk=pk)
        except Templates.DoesNotExist:
            return JsonResponse(status=404, data={'message': 'Template not found'})
        data = request.data
        if 'name' in data:
            template.name = data['name']
        if 'content' in data:
            template.content = data['content']
        if 'event' in data:
            try:
                event = Templates.objects.get(pk=data['event'])
            except Templates.DoesNotExist:
                return JsonResponse(status=404, data={'message': 'Event not found'})
            template.event = event
        template.save()
        return JsonResponse(status=200, data={
            'id': template.pk,
            'name': template.name,
            'content': template.content,
            'event': template.event.pk,
        })

    def delete(self, request, pk):
        try:
            template = Templates.objects.get(pk=pk)
        except Templates.DoesNotExist:
            return JsonResponse(status=404, data={'message': 'Template not found'})
        template.delete()
        return JsonResponse(status=204, data={'message': 'Template deleted'})


