from django.shortcuts import render
from django.views import View
from CRM_app.models import Event, Allie
import json
from django.core.serializers.json import DjangoJSONEncoder

class Calendar(View):
    def get(self, request):
        events = Event.objects.all()
        events_data = []

        for event in events:
            allies = list(Allie.objects.filter(eventallie__event=event).values('name'))
            allies_names = ", ".join([ally['name'] for ally in allies])
            events_data.append({
                'title': event.name,
                'event_type': event.event_type_id.name,
                'description': event.description,
                'objective': event.objective,
                'start': event.date.strftime('%Y-%m-%d'),  # Convert date to string
                'allies': allies_names
            })

        return render(request, 'calendar.html', {'events_data': json.dumps(events_data, cls=DjangoJSONEncoder)})