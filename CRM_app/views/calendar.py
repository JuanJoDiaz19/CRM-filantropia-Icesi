from django.shortcuts import render
from django.views import View
from CRM_app.models import Event, Allie, Meeting
import json
from django.core.serializers.json import DjangoJSONEncoder

class Calendar(View):
    def get(self, request, allie_id):

        events_data = []

        if allie_id != "all":
            ally= Allie.objects.get(id= allie_id)
            events = Event.objects.filter(eventallie__allie_id=int(allie_id))
            meetings = Meeting.objects.filter(allie_id=int(allie_id))
            for event in events:
                allies = list(Allie.objects.filter(eventallie__event=event).values('name'))
                allies_names = ", ".join([ally['name'] for ally in allies])
                events_data.append({
                    'title': event.name,
                    'event_type': event.event_type_id.name,
                    'description': event.description,
                    'objective': event.objective,
                    'start': event.date.strftime('%Y-%m-%d'),  # Convert date to string
                    'allies': allies_names,
                    'color': 'blue'  # Color para eventos
                })

            for meeting in meetings:
                events_data.append({
                    'title': meeting.title,
                    'event_type': meeting.meeting_type_id.name,
                    'description': meeting.description,
                    'objective': meeting.objective,
                    'start': meeting.date.strftime('%Y-%m-%d'),  # Convert date to string
                    'allies': meeting.allie_id.name,
                    'color': 'red'  # Color para reuniones
                })
                
            
            return render(request, 'calendar.html', {'events_data': json.dumps(events_data, cls=DjangoJSONEncoder),'error_message': "Ya existe un aliado con este documento", 'ally':ally})
            
        else:
            events = Event.objects.all()
            meetings = Meeting.objects.all()
            for event in events:
                allies = list(Allie.objects.filter(eventallie__event=event).values('name'))
                allies_names = ", ".join([ally['name'] for ally in allies])
                events_data.append({
                    'title': event.name,
                    'event_type': event.event_type_id.name,
                    'description': event.description,
                    'objective': event.objective,
                    'start': event.date.strftime('%Y-%m-%d'),  # Convert date to string
                    'allies': allies_names,
                    'color': 'blue'  # Color para eventos
                })

            for meeting in meetings:
                events_data.append({
                    'title': meeting.title,
                    'event_type': meeting.meeting_type_id.name,
                    'description': meeting.description,
                    'objective': meeting.objective,
                    'start': meeting.date.strftime('%Y-%m-%d'),  # Convert date to string
                    'allies': meeting.allie_id.name,
                    'color': 'red'  # Color para reuniones
                })
                
            return render(request, 'calendar.html', {'events_data': json.dumps(events_data, cls=DjangoJSONEncoder)})

        

        
