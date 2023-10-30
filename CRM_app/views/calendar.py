from django.shortcuts import render
from django.views import View
from CRM_app.models import Event, Allie, Meeting, ContactInfo
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.mail import send_mail

class Calendar(View):
    def get(self, request, allie_id):
        events_data = []

        if allie_id != "all":
            ally = Allie.objects.get(id=allie_id)
            events = Event.objects.filter(eventallie__allie_id=int(allie_id))
            meetings = Meeting.objects.filter(allie_id=int(allie_id))
            for event in events:
                allies = list(Allie.objects.filter(eventallie__event=event).values('id', 'name'))
                allies_data = []
                for ally in allies:
                    contacts = ContactInfo.objects.filter(allie_id=ally['id'])
                    contact_info = [{'email': contact.email} for contact in contacts]
                    allies_data.append({
                        'id': ally['id'],
                        'name': ally['name'],
                        'contacts': contact_info
                    })

                events_data.append({
                    'title': event.name,
                    'event_type': event.event_type_id.name,
                    'description': event.description,
                    'objective': event.objective,
                    'start': event.date.strftime('%Y-%m-%d'),
                    'allies': allies_data,
                    'color': 'blue',
                    'type': 'event'
                })

            for meeting in meetings:
                allies = list(Allie.objects.filter(id=meeting.allie_id.id).values('id', 'name'))
                allies_data = []
                for ally in allies:
                    contacts = ContactInfo.objects.filter(allie_id=ally['id'])
                    contact_info = [{'email': contact.email} for contact in contacts]
                    allies_data.append({
                        'id': ally['id'],
                        'name': ally['name'],
                        'contacts': contact_info
                    })

                events_data.append({
                    'title': meeting.title,
                    'event_type': meeting.meeting_type_id.name,
                    'description': meeting.description,
                    'objective': meeting.objective,
                    'start': meeting.date.strftime('%Y-%m-%d'),
                    'allies': allies_data,
                    'color': 'red',
                    'type': 'meeting'
                })

            return render(request, 'calendar.html', {'events_data': json.dumps(events_data, cls=DjangoJSONEncoder),'error_message': "Ya existe un aliado con este documento", 'ally':ally})
            
        else:
            events = Event.objects.all()
            meetings = Meeting.objects.all()
            for event in events:
                allies = list(Allie.objects.filter(eventallie__event=event).values('id', 'name'))
                allies_data = []
                for ally in allies:
                    contacts = ContactInfo.objects.filter(allie_id=ally['id'])
                    contact_info = [{'email': contact.email} for contact in contacts]
                    allies_data.append({
                        'id': ally['id'],
                        'name': ally['name'],
                        'contacts': contact_info
                    })

                events_data.append({
                    'title': event.name,
                    'event_type': event.event_type_id.name,
                    'description': event.description,
                    'objective': event.objective,
                    'start': event.date.strftime('%Y-%m-%d'),
                    'allies': allies_data,
                    'color': 'blue',
                    'type': 'event'
                })

            for meeting in meetings:
                allies = list(Allie.objects.filter(id=meeting.allie_id.id).values('id', 'name'))
                allies_data = []
                for ally in allies:
                    contacts = ContactInfo.objects.filter(allie_id=ally['id'])
                    contact_info = [{'email': contact.email} for contact in contacts]
                    allies_data.append({
                        'id': ally['id'],
                        'name': ally['name'],
                        'contacts': contact_info
                    })

                events_data.append({
                    'title': meeting.title,
                    'event_type': meeting.meeting_type_id.name,
                    'description': meeting.description,
                    'objective': meeting.objective,
                    'start': meeting.date.strftime('%Y-%m-%d'),
                    'allies': allies_data,
                    'color': 'red',
                    'type': 'meeting'
                })

            return render(request, 'calendar.html', {'events_data': json.dumps(events_data, cls=DjangoJSONEncoder)})
