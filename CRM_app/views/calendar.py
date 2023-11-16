from django.shortcuts import render, get_object_or_404
from django.views import View
from CRM_app.models import Event, Allie, Meeting, Comment
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

class Calendar(View):
    def get(self, request, allie_id):
        events_data = []

        # Obtiene el aliado si allie_id no es 'all', de lo contrario establece a None
        ally = get_object_or_404(Allie, id=allie_id) if allie_id != "all" else None
        events = Event.objects.filter(eventallie__allie_id=int(allie_id)) if ally else Event.objects.all()
        meetings = Meeting.objects.filter(allie_id=int(allie_id)) if ally else Meeting.objects.all()

        # Procesa los eventos
        for event in events:
            allies = list(Allie.objects.filter(eventallie__event=event).values('name'))
            allies_names = ", ".join([ally['name'] for ally in allies])
            comments = Comment.objects.filter(event=event).order_by('fecha')
            comments_formatted = [
                {
                    'autor': comment.autor,
                    'contenido': comment.contenido,
                    'fecha': comment.fecha.strftime('%Y-%m-%d %H:%M'),
                }
                for comment in comments
            ]
            events_data.append({
                'id': event.id,
                'title': event.name,
                'event_type': event.event_type_id.name,
                'description': event.description,
                'objective': event.objective,
                'start': event.date.strftime('%Y-%m-%d'),
                'allies': allies_names,
                'color': '#0159A1',  # Color azul para eventos
                'comments': comments_formatted, 
                'type': "Evento"
            })

        # Procesa las reuniones y sus comentarios
        for meeting in meetings:
            comments = Comment.objects.filter(meeting=meeting).order_by('fecha')
            comments_formatted = [
                {
                    'autor': comment.autor,
                    'contenido': comment.contenido,
                    'fecha': comment.fecha.strftime('%Y-%m-%d %H:%M'),
                }
                for comment in comments
            ]
            events_data.append({
                'id': meeting.id,
                'title': meeting.title,
                'event_type': meeting.meeting_type_id.name,
                'description': meeting.description,
                'objective': meeting.objective,
                'start': meeting.date.strftime('%Y-%m-%d'),
                'allies': meeting.allie_id.name,
                'color': '#0FAE65',  # Color verde para reuniones
                'comments': comments_formatted,  # Agrega los comentarios al evento de reunión
                'type': "Reunion"
            })

        # Define el mensaje de error si es necesario
        error_message = "Ya existe un aliado con este documento" if ally else ""

        # Prepara el contexto para la plantilla
        context = {
            'events_data': json.dumps(events_data, cls=DjangoJSONEncoder),
            'error_message': error_message,
            'ally': ally
        }

        return render(request, 'calendar.html', context)

