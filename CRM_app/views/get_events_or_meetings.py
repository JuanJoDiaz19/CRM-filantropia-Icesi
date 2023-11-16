from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from CRM_app.models import Event, Allie, Meeting, Comment
import json


@csrf_exempt
def getEventsOrMeetings(request):
    if request.method == 'POST':
        data =  json.loads(request.body)
        type_filter = data.get('type')
        if type_filter == 'Evento':
            events = Event.objects.all()  # Aquí debes filtrar según tu lógica de negocio
        else:
            events = Meeting.objects.all()  # Aquí debes filtrar según tu lógica de negocio
        
        # Asumiendo que tienes una función que formatea los eventos o reuniones para el calendario
        formatted_events = format_for_calendar(events)
        return JsonResponse(formatted_events, safe=False)

    return JsonResponse({'error': 'Invalid request'}, status=400)

def format_for_calendar(events):
    # Esta función tomaría una lista de eventos y los formatearía
    # para su uso en FullCalendar o en tu frontend.
    formatted_events = []
    for event in events:
        allies = list(Allie.objects.filter(eventallie__event=event).values('name'))
        allies_names = ", ".join([ally['name'] for ally in allies])
        # Formatear cada evento como un diccionario con los campos requeridos por FullCalendar
        formatted_events.append({
            'id': event.id,
            'title': event.name,
            'event_type': event.event_type_id.name,
            'description': event.description,
            'objective': event.objective,
            'start': event.date.strftime('%Y-%m-%d'),
            'allies': allies_names,
            'color': '#0159A1',  
            'type': "Evento"
        })
    return formatted_events