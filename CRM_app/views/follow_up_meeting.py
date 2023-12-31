from django.shortcuts import render, redirect
from django.views import View
from CRM_app.models import Meeting
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from CRM_app.models import Meeting, Comment
from django.shortcuts import get_object_or_404

class FollowUpMeeting(View):
    @method_decorator(login_required)
    def get(self, request,follow_up_id):
        return render(request, 'follow_up_meeting.html',{'id': id})
    
    def post(self, request, follow_up_id):
        descripcion = request.POST.get('descripcion')
        autor = request.POST.get('autor')
        meeting = get_object_or_404(Meeting, id=follow_up_id)

        if not (descripcion and autor):
            return render(request, 'follow_up_meeting.html', {'error_message': "Proporcione todos los datos"})


        # Crear el comentario
        comment = Comment(meeting=meeting, autor=autor, contenido=descripcion)
        comment.save()

        # Redirigir a alguna parte o regresar al formulario con un mensaje
        return redirect(f'/calendar/all')
